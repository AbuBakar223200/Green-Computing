# 🌿 GreenInfer: Sustainable AI Benchmarking

> **Paper Title:** *GreenInfer: A Systematic Carbon Footprint and Energy Benchmarking of Small vs. Large Language Models across Downstream NLP Tasks on Consumer Hardware*  
> **Course:** Green Computing  
> **Target:** IEEE Conference (e.g., IEEE STI, IEEE IGSC, IEEE SusTech)  
> **Branch:** `brainstorming`

---

## 📌 Repository Overview

This repository contains the complete research planning, related literature survey, and benchmarking suite for evaluating the energy efficiency, carbon footprint ($\text{gCO}_2\text{eq}$), and accuracy of Small Language Models (SLMs) vs. Large Language Models (LLMs) on consumer-grade hardware.

- 📄 **Research Proposal & Literature Gaps:** [`PLAN.md`](./PLAN.md)
- 📚 **Related Research Papers (2024–2026):** [`papers.md`](./papers.md)
- 📁 **Downloaded Full-Text Papers (PDFs):** [`papers/`](./papers/)
- ⚙️ **Benchmark Implementation:**
  - `prepare_data.py`: Caches 50 evaluation samples per task (SST-2, SQuAD 2.0, CNN/DailyMail, HumanEval).
  - `benchmark.py`: Runs models via Ollama API and tracks physical energy & carbon emissions via CodeCarbon (Windows EMI).
  - `analyze.py`: Generates academic Pareto frontier figures and formatted LaTeX summary tables.
  - `run_all.ps1`: Automated PowerShell execution harness.

---

## 💻 Hardware Setup
- **Processor:** AMD Ryzen 5 5500U with Radeon Graphics (6C/12T, 2.10 GHz)
- **RAM:** 16.0 GB (15.4 GB usable)
- **OS:** Windows 11 (64-bit)
- **Telemetry:** CodeCarbon 3.3.2 with Windows Energy Meter Interface (RAPL)
- **Runtime:** Ollama Local REST API
