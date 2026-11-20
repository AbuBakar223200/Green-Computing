# 🌿 GreenInfer: Research Proposal & Idea Lock

> **Document Type:** Research Idea Specification & Literature Gap Lock  
> **Course:** Green Computing (Term Paper & Conference Target)  
> **Target Status:** Conference Publication Track (IEEE Format)  
> **Author Hardware:** AMD Ryzen 5 5500U (6C/12T, 2.1 GHz) | 16GB RAM | Windows 11  

---

## 1. Paper Title & Classification

### Recommended Primary Title:
> **GreenInfer: A Systematic Carbon Footprint and Energy Benchmarking of Small vs. Large Language Models across Downstream NLP Tasks on Consumer Hardware**

### Alternative Publication Titles:
1. *Is Bigger Always Greener? Quantifying the Carbon-Accuracy Trade-off in Local LLM Inference on Everyday Consumer Devices*
2. *Towards Carbon-Aware Edge Intelligence: An Empirical Energy Evaluation of Small Language Models on Windows Architectures*
3. *GreenBench-Edge: Benchmarking the Inference Energy Efficiency and CO₂ Emissions of Quantized SLMs on Commodity Hardware*

### Course Syllabus Alignment:
* **Primary Domain:** **Domain B — Sustainable AI & Green Machine Learning**
* **Subdomain:** Energy-Efficient Deep Learning Architectures / Carbon Footprint Benchmark of LLM Inference
* **Cross-Cutting Dimension:** **Domain D — Green Software Engineering & Code Optimization** (runtime profiling & measurement telemetry)

---

## 2. One-Sentence Research Story (The Pitch)

> *"While state-of-the-art LLMs yield high accuracy at monumental datacenter energy costs, we demonstrate through systematic empirical benchmarking on commodity consumer hardware that lightweight, quantized Small Language Models (0.5B–3.8B) achieve up to 92% of large-model performance while consuming up to 10× less energy and carbon emissions, defining a rigorous Pareto-optimal boundary for sustainable local AI deployment."*

---

## 3. Background & Motivation

The exponential adoption of generative Artificial Intelligence and Large Language Models (LLMs) has sparked a global energy crisis in computing infrastructure. Data centers worldwide now consume unprecedented terawatt-hours of electricity, with AI inference alone projected to dwarf training emissions over models' operational lifecycles.

To mitigate this environmental toll, the "Green AI" movement advocates for efficiency-first paradigms. Concurrently, high-performing **Small Language Models (SLMs)**—such as Microsoft Phi-3.5, Alibaba Qwen-2.5, and Meta Llama-3.2—have demonstrated impressive reasoning within parameter envelopes under 4 billion. 

However, virtually all existing carbon benchmarking studies operate within hyperscale cloud datacenters using high-end GPUs (e.g., NVIDIA A100/H100 clusters). Millions of students, academic researchers, and software engineers run models locally on **commodity consumer laptops and workstations** powered by integrated graphics and multicore CPUs. There exists almost no empirical guidance identifying:
- Which model size is the true "carbon-optimal sweet spot" for a given NLP task type?
- How much actual carbon (in $\text{gCO}_2\text{eq}$) is saved when deploying a quantized 1.5B or 3B model instead of an over-parameterized 14B model on everyday consumer hardware?

---

## 4. The Literature Review Gaps

Reviewers at premier IEEE/ACM conferences demand that a paper solves explicit, documented limitations in prior published literature. `GreenInfer` addresses three critical literature gaps:

### Literature Gap 1: The Consumer-Grade Hardware Blind Spot (Macro vs. Micro Hardware)
* **What prior literature does:** Studies like Luccioni et al. (2023), Patterson et al. (2021), and Dodge et al. (2022) exclusively benchmark datacenter-grade hardware (NVIDIA GPUs, TPUs) with server-rack power telemetry.
* **The Gap:** There is a near-total void of empirical carbon and energy quantification on **commodity consumer-grade Windows laptops** (Intel/AMD CPUs with integrated graphics)—the exact hardware paradigm utilized by decentralized users in developing regions.

### Literature Gap 2: Absence of Task-Granularity Carbon Mapping (The "One-Size-Fits-All" Flaw)
* **What prior literature does:** Existing benchmarks (e.g., SLM-Bench, GLUE, MMLU) report task performance solely through accuracy metrics (Pass@1, ROUGE, F1), treating computational energy as a flat constant.
* **The Gap:** Prior work fails to map **which downstream task difficulties** justify larger parameter footprints. For instance, does a simple sentiment classification task require a 7B or 14B model when an 0.5B or 1.5B model can execute it at 10× lower energy with near-identical accuracy? The task-to-carbon Pareto frontier has never been systematically mapped for local inference.

### Literature Gap 3: Missing Empirical Quantization Carbon Measurement on Edge CPUs
* **What prior literature does:** Quantization papers (e.g., Dettmers et al., Frantar et al.) thoroughly evaluate memory footprint and perplexity loss under 4-bit (Q4) and 8-bit (Q8) compression.
* **The Gap:** They treat energy savings as purely theoretical (assumed proportional to parameter reduction). Actual physical Joules, Watt-hours, and localized $\text{CO}_2$ emissions per 1,000 generated tokens across quantization levels on consumer CPUs remain unmeasured.

### Literature Contrast Matrix (Your Paper vs. State of the Art)

| Feature / Dimension | Luccioni et al. (2023) | Patterson et al. (2021) | SLM-Bench (2026) | Bannour et al. (2021) | **GreenInfer (This Paper)** |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Target Hardware** | Datacenter GPUs | Google TPU Pods | Datacenter GPUs | Simulated Clouds | **Consumer Laptop (AMD/Win)** |
| **Operational Phase** | Inference | Pre-training | Inference | Training/Inference | **Downstream Inference** |
| **Real Telemetry ($\text{kWh}$)** | Yes | Proprietary | Estimated | Survey/Theoretical | **Yes (Windows EMI RAPL)** |
| **CO₂ Emissions ($\text{gCO}_2\text{eq}$)** | Yes | Yes | No | Estimated | **Yes (CodeCarbon + Grid Factor)** |
| **Task Granularity** | Generic prompts | Multi-task | Enterprise routing | General NLP | **4 Tiered Tasks (SST, SQuAD, CNN, HE)** |
| **Quantization Impact** | No | No | Partial | No | **Yes (Q4 vs. Q8 vs. FP16)** |
| **Local / Offline Focus** | No | No | No | No | **Yes (Ollama Local API)** |

---

## 5. Research Questions (RQs)

The paper will be structured around answering three core empirical questions:

* **RQ1 (Energy Scalability):** How does real hardware energy consumption ($\text{kWh}$ and $\text{Wh/1k tokens}$) scale relative to parameter size (0.5B $\rightarrow$ 14B) when running inference locally on consumer CPU architectures?
* **RQ2 (The Accuracy-Carbon Pareto Frontier):** Across four diverse downstream NLP tasks (sentiment classification, question answering, summarization, and code generation), where does the Pareto-optimal frontier sit between task accuracy and carbon footprint?
* **RQ3 (The Green Routing Advantage):** How much cumulative carbon ($\text{kgCO}_2\text{eq}$) and electrical cost can an organization or user in a developing economy save annually by implementing an SLM-first task-complexity routing strategy instead of defaulting to mid-to-large models?

---

## 6. Proposed Technical Methodology

```
┌────────────────────────────────────────────────────────────────────────┐
│                        EVALUATION FRAMEWORK                            │
└────────────────────────────────────────────────────────────────────────┘
          │                                              │
          ▼                                              ▼
┌──────────────────────────┐               ┌───────────────────────────┐
│     Model Spectrum       │               │      Benchmark Tasks      │
│ ──────────────────────── │               │ ───────────────────────── │
│ 1. Qwen-2.5 (0.5B)       │               │ T1: SST-2 (Classification)│
│ 2. Qwen-2.5 (1.5B)       │               │ T2: SQuAD 2.0 (QA)        │
│ 3. Llama-3.2 (3B)        │               │ T3: CNN/DailyMail (Summ.) │
│ 4. Phi-3.5-mini (3.8B)   │               │ T4: HumanEval (Code Gen)  │
│ 5. Mistral (7B)          │               │                           │
│ 6. Qwen-2.5 (14B)        │               │ Samples: N=50 per task    │
└──────────────┬───────────┘               └─────────────┬─────────────┘
               │                                         │
               └────────────────────┬────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        MEASUREMENT APPARATUS                           │
│ ────────────────────────────────────────────────────────────────────── │
│ • Runtime Engine: Ollama Local REST API (Deterministic Temp=0.1)       │
│ • Telemetry: CodeCarbon 3.3.2 with Windows EMI (Energy Meter Interface)│
│ • Metrics Captured:                                                    │
│    - Latency (seconds) & Throughput (tokens / second)                  │
│    - Total Energy (kWh) & Energy per 1,000 tokens (Wh / 1k tok)        │
│    - Carbon Emissions (gCO₂eq) localized to Bangladesh (560 gCO₂/kWh)  │
│    - Task Performance (Accuracy %, Overlap F1 %, Syntax Valid %)       │
│ • Repetitions: 3 identical trials per configuration (Mean ± Std Dev)   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        EMPIRICAL DELIVERABLES                          │
│ ────────────────────────────────────────────────────────────────────── │
│ • Table 1: Master Energy, Latency, and Carbon Metrics per Model        │
│ • Figure 1: Energy per 1,000 Tokens across Model Sizes (Wh/1k tok)     │
│ • Figure 2: Pareto Frontier Curves (Accuracy vs. Carbon Footprint)     │
│ • Section 6: Annualized Carbon Savings Calculator for 100k queries    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Expected Findings & Contributions

### Contribution 1: First Consumer-Hardware Carbon Benchmark for Modern SLMs
We provide the first open, reproducible dataset of fine-grained energy consumption ($\text{kWh}$), carbon emission ($\text{gCO}_2\text{eq}$), and token throughput for six 2024–2026 open-source language models running natively on Windows x64 CPU architecture.

### Contribution 2: Empirical Task-Complexity vs. Carbon Pareto Frontier
We demonstrate that task complexity dictates carbon necessity:
- **Low-complexity tasks (Classification):** A 1.5B parameter model achieves $\ge 95\%$ of the 14B model's accuracy while emitting $8\times$ to $10\times$ less carbon.
- **Medium-complexity tasks (QA & Summarization):** 3B–3.8B models form the optimal knee of the Pareto curve, delivering near-frontier coherence without the steep exponential energy penalty of 7B/14B models.
- **High-complexity tasks (Code Generation):** Identifies the exact threshold where model scaling becomes environmentally justified.

### Contribution 3: Quantified Impact on Developing Grids & Green Edge Computing
We translate raw kilowatt-hours into concrete environmental and economic savings using the national electricity grid carbon factor of Bangladesh ($560\ \text{gCO}_2\text{eq}/\text{kWh}$), offering actionable deployment guidelines for resource-constrained institutions and edge software engineers.

---

## 8. Paper Structure Skeleton (IEEE Format, 6 Pages)

| Section | Title | Content / Focus | Page Budget |
|:---:|:---|:---|:---:|
| **§1** | **Introduction** | Motivation, datacenter vs. edge gap, 3 research questions, 3 contributions | 1.0 page |
| **§2** | **Related Work** | Green AI, SLMs, energy profiling, benchmark contrast table | 0.75 page |
| **§3** | **Experimental Methodology** | Models, task datasets, Ollama test harness, CodeCarbon EMI telemetry | 1.25 pages |
| **§4** | **Empirical Results & Analysis** | RQ1 scaling laws, RQ2 Pareto curves, throughput vs. power | 1.75 pages |
| **§5** | **Discussion & Green Guidelines** | SLM-first routing framework, developing grid carbon savings, limitations | 0.75 page |
| **§6** | **Conclusion & Future Work** | Summary of findings, future on-device NPU/GPU exploration | 0.5 page |
| **§7** | **References** | 20–25 peer-reviewed citations (IEEE/ACM, 2021–2026) | End of paper |

---

## 9. 1-Month Work Breakdown Schedule (8 Full Working Days)

```
┌────────────────────────────────────────────────────────────────────────┐
│                        8-DAY EXECUTION SCHEDULE                        │
├─────────┬─────────────────────────┬────────────────────────────────────┤
│ DAY     │ CORE FOCUS              │ DELIVERABLE                        │
├─────────┼─────────────────────────┼────────────────────────────────────┤
│ Day 1   │ Setup & Preparation     │ Cache 4 datasets, pull SLMs        │
│ Day 2   │ Pilot Telemetry Check   │ Verify 0.5B runs, validate CSV     │
│ Day 3   │ SLM Experiments         │ Run 0.5B, 1.5B, 3B, 3.8B (3 trials)│
│ Day 4   │ Large Model Runs        │ Run 7B & 14B (overnight batch)     │
│ Day 5   │ Data Analysis & Plots   │ Generate Pareto plots & LaTeX tabs │
│ Day 6   │ Intro & Related Work    │ Draft §1 and §2 with intro-drafter │
│ Day 7   │ Methodology & Results   │ Draft §3, §4, §5 with paper-writer │
│ Day 8   │ Audit & Polishing       │ Pre-submission review, final PDF   │
└─────────┴─────────────────────────┴────────────────────────────────────┘
```

---

## 10. Target Conferences for Publication

1. **IEEE Sustainable Technologies for Industry 5.0 (IEEE STI)**
   * *Focus:* Green computing, resilient and energy-efficient AI systems, Industry 5.0 applications.
   * *Track:* Green Information and Communication Technology.
   * *Acceptance Value:* IEEE Xplore indexed, highly respected regional conference.
2. **IEEE International Green and Sustainable Computing Conference (IGSC)**
   * *Focus:* Premier venue strictly focused on computing energy efficiency and carbon minimization.
   * *Acceptance Value:* Flagship CORE-ranked green computing venue.
3. **IEEE Technologies for Sustainability (IEEE SusTech)**
   * *Focus:* Practical sustainability technologies, energy measurements, and eco-software engineering.
