"""
GreenInfer Analysis & Visualization Suite
Reads results/benchmark_results.csv and outputs:
1. High-resolution figures for paper (energy vs accuracy Pareto frontier, energy per 1k tokens)
2. Formatted LaTeX tables ready for camera-ready paper
3. National grid carbon scaling calculations (e.g. Bangladesh 560 gCO2eq/kWh)
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
CSV_PATH = os.path.join(RESULTS_DIR, "benchmark_results.csv")
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

# Styling for academic conference figures
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'

def generate_visualizations():
    if not os.path.exists(CSV_PATH):
        print(f"❌ No results found at {CSV_PATH}. Run benchmarks first.")
        return

    df = pd.read_csv(CSV_PATH)
    if df.empty:
        print("❌ benchmark_results.csv is empty.")
        return

    # Group by model and task (averaging across trials)
    summary = df.groupby(['model', 'task']).agg({
        'energy_kwh': 'mean',
        'emissions_gCO2eq': 'mean',
        'tokens_per_sec': 'mean',
        'energy_per_1k_tokens_kwh': 'mean',
        'task_metric_value': 'mean',
        'elapsed_sec': 'mean'
    }).reset_index()

    print("\n=== SUMMARY DATA TABLE ===")
    print(summary[['model', 'task', 'energy_per_1k_tokens_kwh', 'tokens_per_sec', 'task_metric_value']])

    # 1. Plot: Energy per 1000 tokens across models
    plt.figure(figsize=(8, 4.5), dpi=300)
    for task in summary['task'].unique():
        task_data = summary[summary['task'] == task]
        plt.plot(task_data['model'], task_data['energy_per_1k_tokens_kwh'] * 1e3, marker='o', label=task.capitalize())

    plt.title("Energy Consumption per 1k Tokens Across Models (Consumer CPU)", fontsize=12, fontweight='bold')
    plt.xlabel("Model Architecture & Size", fontsize=11)
    plt.ylabel("Energy (Wh / 1000 Tokens)", fontsize=11)
    plt.xticks(rotation=20)
    plt.legend()
    plt.tight_layout()
    plot_path1 = os.path.join(FIGURES_DIR, "fig1_energy_per_1k_tokens.png")
    plt.savefig(plot_path1)
    plt.close()
    print(f" Saved Figure 1: {plot_path1}")

    # 2. Plot: Pareto Frontier: Task Performance vs Carbon Emissions (Classification Task as prime example)
    clf_data = summary[summary['task'] == 'classification']
    if not clf_data.empty:
        plt.figure(figsize=(7, 4.5), dpi=300)
        plt.scatter(clf_data['emissions_gCO2eq'], clf_data['task_metric_value'], color='#2ca02c', s=120, edgecolors='black')
        for _, row in clf_data.iterrows():
            plt.annotate(row['model'], (row['emissions_gCO2eq'], row['task_metric_value']),
                         textcoords="offset points", xytext=(0, 8), ha='center', fontsize=9)
        plt.title("Pareto Frontier: Accuracy vs Carbon Footprint (SST-2)", fontsize=12, fontweight='bold')
        plt.xlabel("Total Carbon Emissions (gCO2eq for 50 samples)", fontsize=11)
        plt.ylabel("Classification Accuracy (%)", fontsize=11)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plot_path2 = os.path.join(FIGURES_DIR, "fig2_pareto_accuracy_vs_carbon.png")
        plt.savefig(plot_path2)
        plt.close()
        print(f" Saved Figure 2: {plot_path2}")

    # 3. Export LaTeX Table for Paper
    latex_path = os.path.join(RESULTS_DIR, "table_summary.tex")
    pivot_energy = summary.pivot(index='model', columns='task', values='energy_per_1k_tokens_kwh')
    latex_code = pivot_energy.to_latex(float_format="%.5f", caption="Energy per 1,000 Tokens (kWh) across models and tasks on AMD Ryzen 5 5500U.")
    with open(latex_path, "w", encoding="utf-8") as f:
        f.write(latex_code)
    print(f" Saved LaTeX Table: {latex_path}")

if __name__ == "__main__":
    generate_visualizations()
