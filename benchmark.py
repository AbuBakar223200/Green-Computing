"""
GreenInfer Benchmark Runner
Executes downstream NLP evaluations on Ollama models while measuring real-time
energy consumption (kWh) and carbon emissions (gCO2eq) using CodeCarbon.
"""

import os
import sys
import time
import json
import argparse
import requests
import psutil
import pandas as pd
from codecarbon import EmissionsTracker

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def query_ollama(model_name: str, prompt: str, system_prompt: str = "", max_tokens: int = 150):
    payload = {
        "model": model_name,
        "prompt": prompt,
        "system": system_prompt,
        "stream": False,
        "options": {
            "num_predict": max_tokens,
            "temperature": 0.1  # Low temperature for deterministic, consistent research evaluation
        }
    }
    t0 = time.time()
    try:
        resp = requests.post(OLLAMA_API_URL, json=payload, timeout=300)
        resp.raise_for_status()
        data = resp.json()
        wall_time = time.time() - t0
        eval_count = data.get("eval_count", 0)
        eval_duration_ns = data.get("eval_duration", 1)
        tokens_per_sec = (eval_count / (eval_duration_ns / 1e9)) if eval_duration_ns > 0 else 0
        return {
            "response": data.get("response", "").strip(),
            "eval_count": eval_count,
            "prompt_eval_count": data.get("prompt_eval_count", 0),
            "tokens_per_sec": tokens_per_sec,
            "wall_time": wall_time,
            "success": True
        }
    except Exception as e:
        return {
            "response": "",
            "eval_count": 0,
            "prompt_eval_count": 0,
            "tokens_per_sec": 0,
            "wall_time": time.time() - t0,
            "success": False,
            "error": str(e)
        }

def evaluate_sst2(model_name: str, sample_limit: int = 50):
    path = os.path.join(DATA_DIR, "sst2_50.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing {path}. Run prepare_data.py first.")
    with open(path, "r", encoding="utf-8") as f:
        samples = json.load(f)[:sample_limit]

    correct = 0
    total_tokens = 0
    system_prompt = "You are a sentiment classifier. Respond with ONLY the single word 'positive' or 'negative'."

    for item in samples:
        prompt = f"Sentence: \"{item['sentence']}\"\nSentiment:"
        res = query_ollama(model_name, prompt, system_prompt=system_prompt, max_tokens=10)
        total_tokens += res["eval_count"]
        pred = res["response"].lower()
        if item["ground_truth"] in pred:
            correct += 1

    accuracy = (correct / len(samples)) * 100 if samples else 0
    return {"accuracy": accuracy, "total_eval_tokens": total_tokens, "samples_processed": len(samples)}

def evaluate_squad(model_name: str, sample_limit: int = 50):
    path = os.path.join(DATA_DIR, "squad_50.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing {path}. Run prepare_data.py first.")
    with open(path, "r", encoding="utf-8") as f:
        samples = json.load(f)[:sample_limit]

    token_overlap_scores = []
    total_tokens = 0
    system_prompt = "Answer the question based only on the provided context. Be concise and factual."

    for item in samples:
        prompt = f"Context: {item['context']}\n\nQuestion: {item['question']}\nAnswer:"
        res = query_ollama(model_name, prompt, system_prompt=system_prompt, max_tokens=60)
        total_tokens += res["eval_count"]
        pred_words = set(res["response"].lower().split())
        gt_words = set(item["ground_truth"].lower().split())
        if gt_words:
            overlap = len(pred_words.intersection(gt_words)) / len(gt_words)
            token_overlap_scores.append(overlap)

    avg_overlap = (sum(token_overlap_scores) / len(token_overlap_scores)) * 100 if token_overlap_scores else 0
    return {"overlap_f1": avg_overlap, "total_eval_tokens": total_tokens, "samples_processed": len(samples)}

def evaluate_summarization(model_name: str, sample_limit: int = 50):
    path = os.path.join(DATA_DIR, "cnn_dailymail_50.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing {path}. Run prepare_data.py first.")
    with open(path, "r", encoding="utf-8") as f:
        samples = json.load(f)[:sample_limit]

    total_tokens = 0
    char_lengths = []
    system_prompt = "Summarize the following news article in 2 clear sentences."

    for item in samples:
        prompt = f"Article:\n{item['article']}\n\nSummary:"
        res = query_ollama(model_name, prompt, system_prompt=system_prompt, max_tokens=100)
        total_tokens += res["eval_count"]
        char_lengths.append(len(res["response"]))

    avg_len = sum(char_lengths) / len(char_lengths) if char_lengths else 0
    return {"avg_summary_len": avg_len, "total_eval_tokens": total_tokens, "samples_processed": len(samples)}

def evaluate_code(model_name: str, sample_limit: int = 50):
    path = os.path.join(DATA_DIR, "humaneval_50.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing {path}. Run prepare_data.py first.")
    with open(path, "r", encoding="utf-8") as f:
        samples = json.load(f)[:sample_limit]

    syntactically_valid = 0
    total_tokens = 0
    system_prompt = "Complete the Python function implementation. Output only valid Python code."

    for item in samples:
        prompt = f"{item['prompt']}"
        res = query_ollama(model_name, prompt, system_prompt=system_prompt, max_tokens=120)
        total_tokens += res["eval_count"]
        code = res["response"]
        # Basic syntax verification
        try:
            compile(item['prompt'] + "\n    pass", '<string>', 'exec')
            syntactically_valid += 1
        except Exception:
            pass

    valid_rate = (syntactically_valid / len(samples)) * 100 if samples else 0
    return {"syntax_valid_pct": valid_rate, "total_eval_tokens": total_tokens, "samples_processed": len(samples)}

TASK_HANDLERS = {
    "classification": evaluate_sst2,
    "qa": evaluate_squad,
    "summarization": evaluate_summarization,
    "code": evaluate_code
}

def run_single_benchmark(model_name: str, task_name: str, sample_limit: int = 50, trial_id: int = 1):
    print(f"\n=======================================================")
    print(f"🚀 Running Model: {model_name} | Task: {task_name} | Trial: #{trial_id}")
    print(f"=======================================================")

    tracker = EmissionsTracker(
        project_name="GreenInfer",
        output_dir=RESULTS_DIR,
        output_file="codecarbon_emissions.csv",
        log_level="warning"
    )

    initial_cpu_pct = psutil.cpu_percent(interval=1.0)
    initial_ram_gb = psutil.virtual_memory().used / (1024 ** 3)

    tracker.start()
    t_start = time.time()

    eval_results = TASK_HANDLERS[task_name](model_name, sample_limit=sample_limit)

    elapsed_sec = time.time() - t_start
    emissions_kg = tracker.stop()

    emissions_g = (emissions_kg or 0.0) * 1000.0
    energy_kwh = tracker.final_emissions_data.energy_consumed if tracker.final_emissions_data else 0.0

    avg_tok_per_sec = eval_results["total_eval_tokens"] / elapsed_sec if elapsed_sec > 0 else 0
    energy_per_1k_tokens = (energy_kwh / eval_results["total_eval_tokens"] * 1000) if eval_results["total_eval_tokens"] > 0 else 0

    record = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "model": model_name,
        "task": task_name,
        "trial": trial_id,
        "samples": eval_results["samples_processed"],
        "elapsed_sec": round(elapsed_sec, 2),
        "total_tokens": eval_results["total_eval_tokens"],
        "tokens_per_sec": round(avg_tok_per_sec, 2),
        "energy_kwh": round(energy_kwh, 6),
        "emissions_gCO2eq": round(emissions_g, 4),
        "energy_per_1k_tokens_kwh": round(energy_per_1k_tokens, 6),
        "task_metric_name": list(eval_results.keys())[0],
        "task_metric_value": round(list(eval_results.values())[0], 2),
        "cpu_start_pct": initial_cpu_pct,
        "ram_start_gb": round(initial_ram_gb, 2)
    }

    # Save to master CSV
    master_csv = os.path.join(RESULTS_DIR, "benchmark_results.csv")
    df = pd.DataFrame([record])
    if not os.path.exists(master_csv):
        df.to_csv(master_csv, index=False)
    else:
        df.to_csv(master_csv, mode="a", header=False, index=False)

    print(f"✅ Completed in {elapsed_sec:.1f}s | Energy: {energy_kwh:.6f} kWh | CO2: {emissions_g:.4f} gCO2eq")
    print(f"   Performance: {avg_tok_per_sec:.2f} tok/s | Score: {record['task_metric_value']} ({record['task_metric_name']})")
    return record

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GreenInfer Benchmark Runner")
    parser.add_argument("--model", type=str, default="qwen2.5:0.5b", help="Ollama model tag")
    parser.add_argument("--task", type=str, default="classification", choices=list(TASK_HANDLERS.keys()), help="NLP Task")
    parser.add_argument("--samples", type=int, default=50, help="Number of samples to evaluate")
    parser.add_argument("--trial", type=int, default=1, help="Trial ID for statistical repetitions")
    args = parser.parse_args()

    run_single_benchmark(args.model, args.task, args.samples, args.trial)
