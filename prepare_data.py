"""
Data Preparation Script for GreenInfer
Downloads exactly 50 samples per benchmark task and stores them in ./data/ as clean JSON files.
Tasks:
1. Sentiment Classification: Stanford Sentiment Treebank (SST-2)
2. Question Answering: SQuAD 2.0
3. Summarization: CNN / DailyMail
4. Code Generation: HumanEval (or subset)
"""

import os
import json
from datasets import load_dataset

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)
SAMPLE_LIMIT = 50

def prepare_sst2():
    print(f"[*] Preparing SST-2 (Sentiment Classification, N={SAMPLE_LIMIT})...")
    dataset = load_dataset("glue", "sst2", split=f"validation[:{SAMPLE_LIMIT}]")
    data = []
    for item in dataset:
        data.append({
            "id": item["idx"],
            "sentence": item["sentence"],
            "ground_truth": "positive" if item["label"] == 1 else "negative"
        })
    out_path = os.path.join(DATA_DIR, "sst2_50.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"    Saved: {out_path}")

def prepare_squad():
    print(f"[*] Preparing SQuAD 2.0 (Question Answering, N={SAMPLE_LIMIT})...")
    dataset = load_dataset("rajpurkar/squad_v2", split="validation")
    data = []
    count = 0
    for item in dataset:
        # Pick entries that have answers
        if len(item["answers"]["text"]) > 0:
            data.append({
                "id": item["id"],
                "context": item["context"][:1000],  # Bound context length for CPU efficiency
                "question": item["question"],
                "ground_truth": item["answers"]["text"][0]
            })
            count += 1
            if count >= SAMPLE_LIMIT:
                break
    out_path = os.path.join(DATA_DIR, "squad_50.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"    Saved: {out_path}")

def prepare_cnn_dailymail():
    print(f"[*] Preparing CNN/DailyMail (Summarization, N={SAMPLE_LIMIT})...")
    dataset = load_dataset("cnn_dailymail", "3.0.0", split=f"test[:{SAMPLE_LIMIT}]")
    data = []
    for idx, item in enumerate(dataset):
        data.append({
            "id": idx,
            "article": item["article"][:1200],  # Bound article length for CPU efficiency
            "ground_truth": item["highlights"]
        })
    out_path = os.path.join(DATA_DIR, "cnn_dailymail_50.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"    Saved: {out_path}")

def prepare_humaneval():
    print(f"[*] Preparing HumanEval (Code Generation, N={SAMPLE_LIMIT})...")
    dataset = load_dataset("openai/openai_humaneval", split=f"test[:{SAMPLE_LIMIT}]")
    data = []
    for item in dataset:
        data.append({
            "id": item["task_id"],
            "prompt": item["prompt"],
            "entry_point": item["entry_point"]
        })
    out_path = os.path.join(DATA_DIR, "humaneval_50.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"    Saved: {out_path}")

if __name__ == "__main__":
    print("=== Downloading GreenInfer Evaluation Datasets ===")
    prepare_sst2()
    prepare_squad()
    prepare_cnn_dailymail()
    prepare_humaneval()
    print("=== All datasets prepared successfully! ===")
