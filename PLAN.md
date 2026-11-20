# 🌿 GreenInfer: Research Proposal & Idea Lock

> **Document Type:** Research Idea Specification & Literature Gap Lock  
> **Course:** Green Computing (Term Paper & Conference Target)  
> **Target Status:** Conference Publication Track (IEEE Format)  
> **Experimental Testbed:** `ABU_BAKAR_LAP` (Windows 11) and Apple M1 MacBook Air (macOS)

---

## 1. Paper Title & Classification

### Recommended Primary Title:
> **GreenInfer: Cross-Platform Energy, Carbon, and Quality Benchmarking of Small vs. Large Language Models on Windows and Apple Silicon Laptops**

### Alternative Publication Titles:
1. *Is Bigger Always Greener? Quantifying the Carbon–Quality Trade-off in Local LLM Inference across Consumer Platforms*
2. *Towards Carbon-Aware Edge Intelligence: Comparing Quantized Language-Model Inference on Windows x64 and Apple Silicon*
3. *GreenBench-Edge: Cross-Platform Energy and CO₂ Benchmarking of Quantized SLMs on Commodity Hardware*

### Course Syllabus Alignment:
* **Primary Domain:** **Domain B — Sustainable AI & Green Machine Learning**
* **Subdomain:** Energy-Efficient Deep Learning Architectures / Carbon Footprint Benchmark of LLM Inference
* **Cross-Cutting Dimension:** **Domain D — Green Software Engineering & Code Optimization** (cross-platform runtime profiling and measurement telemetry)

---

## 2. One-Sentence Research Story (The Pitch)

> *This study systematically benchmarks quantized Small and Large Language Models (0.5B–8B) on a Windows/AMD laptop and an Apple Silicon/macOS laptop to determine how model size, task type, and hardware platform affect output quality, latency, throughput, energy use, and carbon emissions, and to identify device-specific Pareto-optimal choices for sustainable local AI.*

The study will test—rather than assume—that smaller models preserve acceptable task quality while consuming less energy than 7B–8B baselines. Numerical reduction factors will be reported only after the experiments.

---

## 3. Background & Motivation

The exponential adoption of generative Artificial Intelligence and Large Language Models (LLMs) has increased the energy demand of computing infrastructure. Although model training is energy intensive, repeated inference can also contribute substantially to a model's operational footprint.

To mitigate this environmental cost, the Green AI movement advocates efficiency-first deployment. Concurrently, capable **Small Language Models (SLMs)**—such as Microsoft Phi-3.5, Alibaba Qwen-2.5, and Meta Llama-3.2—have demonstrated useful performance within parameter envelopes below four billion.

Most carbon benchmarking studies focus on hyperscale datacenters and high-end accelerators such as NVIDIA A100/H100 GPUs. In contrast, students, researchers, and software engineers often run models locally on consumer laptops. These devices differ substantially in processor architecture, memory design, operating system, runtime backend, and power management. GreenInfer therefore studies both model-size trade-offs and platform effects using a Windows x64/AMD laptop and an Apple Silicon/macOS laptop.

The study will investigate:
- Which model size provides the best quality–energy balance for each NLP task on each device?
- How much energy and carbon can be saved by choosing a 0.5B–3.8B model instead of a 7B–8B model when the larger model is feasible?
- How do latency, throughput, memory constraints, and energy behavior differ between the two consumer platforms?

---

## 4. The Literature Review Gaps

Reviewers at IEEE/ACM conferences expect a paper to address explicit limitations in prior work. `GreenInfer` targets four related gaps:

### Literature Gap 1: The Consumer-Grade and Cross-Platform Hardware Blind Spot
* **What prior literature does:** Many influential carbon studies benchmark datacenter-grade GPUs, TPUs, or cloud infrastructure with server-level telemetry.
* **The Gap:** There is limited empirical evidence for local inference on ordinary laptops, especially controlled comparisons between Windows x64/AMD systems and Apple Silicon/macOS systems.

### Literature Gap 2: Absence of Task-Granularity Carbon Mapping
* **What prior literature does:** NLP benchmarks usually report quality metrics such as accuracy, F1, ROUGE, or Pass@1 without mapping those results to measured inference energy.
* **The Gap:** Prior work provides little guidance about which task difficulties justify larger parameter counts. The task-specific quality–carbon Pareto frontier for local inference remains underexplored.

### Literature Gap 3: Limited Empirical Measurement of Quantized Edge Inference
* **What prior literature does:** Quantization research often emphasizes memory footprint, throughput, and quality loss under formats such as 4-bit and 8-bit compression.
* **The Gap:** Physical or consistently estimated energy, watt-hours per 1,000 generated tokens, and localized carbon emissions for quantized models on consumer devices are less frequently reported.

### Literature Gap 4: Platform and Telemetry Comparability
* **What prior literature does:** Studies commonly report results from one hardware/software stack and may treat runtime-level energy estimates as directly comparable.
* **The Gap:** Windows and macOS may expose different energy sources and measurement boundaries. A reproducible methodology must identify the runtime backend and distinguish package energy, whole-device energy, and estimated energy before making absolute cross-device claims.

### Literature Contrast Matrix (Your Paper vs. State of the Art)

| Feature / Dimension | Luccioni et al. (2023) | Patterson et al. (2021) | SLM-Bench (2026) | Bannour et al. (2021) | **GreenInfer (This Paper)** |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Target Hardware** | Datacenter GPUs | Google TPU Pods | Datacenter GPUs | Simulated Clouds | **Windows/AMD and Apple Silicon consumer laptops** |
| **Operational Phase** | Inference | Pre-training | Inference | Training/Inference | **Downstream local inference** |
| **Energy Telemetry** | Measured | Proprietary | Estimated | Survey/Theoretical | **Platform-specific sources, pilot-validated and disclosed** |
| **CO₂ Emissions** | Yes | Yes | No | Estimated | **Energy × documented grid factor** |
| **Task Granularity** | Generic prompts | Multi-task | Enterprise routing | General NLP | **4 tasks: SST-2, SQuAD 2.0, CNN/DailyMail, HumanEval** |
| **Model-Size Range** | Limited | Limited | Multiple | Limited | **0.5B–8B quantized models, subject to device feasibility** |
| **Local / Offline Focus** | No | No | No | No | **Yes, through Ollama Local API** |
| **Cross-Platform Analysis** | No | No | Limited | No | **Device-stratified Windows vs. macOS comparison** |

---

## 5. Research Questions (RQs)

The paper will answer four empirical questions:

* **RQ1 — Energy Scalability:** How do energy use ($\text{kWh}$ and $\text{Wh/1k tokens}$), latency, and throughput scale with model size (0.5B $\rightarrow$ 8B) on each consumer device?
* **RQ2 — Quality–Carbon Pareto Frontier:** For sentiment classification, question answering, summarization, and code generation, where is the Pareto-optimal boundary between task quality and carbon footprint on each device?
* **RQ3 — Cross-Platform Effect:** Under matched workloads and model configurations, how do `ABU_BAKAR_LAP` and the Apple M1 MacBook Air differ in feasibility, latency, throughput, and energy behavior? Which differences can be compared directly given the validated telemetry boundaries?
* **RQ4 — Green Routing Advantage:** How much annual energy, carbon, and electricity cost could be saved under a documented workload by routing simpler tasks to smaller models rather than defaulting to 7B–8B models?

Results will first compare model sizes **within each device**. Cross-device analysis will follow as a separate stage; observations from the two laptops will not be pooled as though they came from identical hardware.

---

## 6. Proposed Technical Methodology

### 6.1 Experimental Devices

| Device ID | Hardware | Memory | Operating System | Notes |
|:---|:---|:---|:---|:---|
| **`ABU_BAKAR_LAP`** | AMD Ryzen 5 5500U, 6 cores/12 threads, 2.10 GHz | 16 GB RAM | Windows 11 | Record OS build, power mode, and actual Ollama backend before testing. |
| **`MACBOOK_AIR_M1`** | MacBook Air `MacBookAir10,1` (`MGN63ZP/A`), Apple M1, 8 cores (4 performance + 4 efficiency) | 8 GB unified memory | macOS | Record the exact macOS version, power mode, swap use, and actual Ollama backend before testing. |

Private identifiers—including serial numbers, device/product IDs, hardware UUIDs, and provisioning UDIDs—will not be collected or published.

### 6.2 Existing Public Benchmark Datasets

GreenInfer will **not create or label a new dataset**. It will download, select, and locally cache samples from four established public benchmarks:

| Task | Existing dataset | Planned sample | Primary quality measure |
|:---|:---|---:|:---|
| Sentiment classification | SST-2 | 50 | Accuracy |
| Question answering | SQuAD 2.0 | 50 | Exact Match and token-level F1 |
| Summarization | CNN/DailyMail | 50 | ROUGE-1/ROUGE-2/ROUGE-L |
| Code generation | HumanEval | 50 | Pass@1 in an isolated evaluation environment |

The same cached examples, prompts, references, and evaluation logic will be used on both devices.

### 6.3 Model Spectrum

| Tier | Model | Parameters | Comparison requirement |
|:---|:---|---:|:---|
| Ultra-compact | Qwen-2.5 | 0.5B | Same artifact and quantization on both devices |
| Compact SLM | Qwen-2.5 | 1.5B | Same artifact and quantization on both devices |
| Small model | Llama-3.2 | 3B | Same artifact and quantization on both devices |
| Efficient reasoning | Phi-3.5 Mini | 3.8B | Same artifact and quantization on both devices |
| Mid-size baseline | Mistral | 7B | Run only if the device completes without unacceptable memory pressure |
| Large baseline | Llama-3.1 | 8B | Run only if the device completes without unacceptable memory pressure |

The exact Ollama tag, model digest, quantization, model file size, context limit, output-token limit, and sampling settings will be recorded. If the 8 GB Mac cannot run a 7B or 8B model reliably without heavy swap use, the outcome will be reported as a hardware-feasibility result rather than omitted or represented as a normal run.

### 6.4 Controlled Execution Protocol

For every model–task combination:

1. Use the same cached dataset sample, prompt template, model artifact, context/output limits, and decoding parameters on both devices.
2. Run an explicitly documented warm-up before measured trials and apply the same model-cache policy.
3. Conduct **three measured trials per configuration per device** and report mean, standard deviation, and individual-run data.
4. Keep each laptop plugged in, use a fixed documented power mode, close unnecessary applications, and record relevant background conditions.
5. Monitor memory pressure and swap/page-file use. Flag or exclude a trial according to a predefined rule if paging makes it non-comparable.
6. Record the device ID, OS version/build, Ollama version, compute backend, model digest, quantization, task, trial number, input/output token counts, and timestamps with every observation.
7. Preserve load failures, out-of-memory events, throttling observations, and infeasible configurations as reported experimental outcomes.

### 6.5 Measurement and Telemetry

| Category | Metrics / controls |
|:---|:---|
| **Runtime** | Ollama Local REST API; actual platform backend and version recorded separately |
| **Performance** | End-to-end latency, generation duration, prompt/output tokens, tokens per second |
| **Energy** | Total energy ($\text{kWh}$) and $\text{Wh/1k}$ output tokens, with source and measurement boundary documented |
| **Carbon** | $\text{gCO}_2\text{eq}$ derived from measured/estimated energy using the same stated Bangladesh grid factor for deployment scenarios |
| **Task quality** | Accuracy, Exact Match/F1, ROUGE, and HumanEval Pass@1 as appropriate |
| **System state** | Power mode, plugged-in state, warm-up, cache policy, memory pressure, paging/swap, and thermal/throttling observations |

Telemetry will be validated in a pilot on **each** device before the full experiment. The Windows pilot will validate CodeCarbon 3.3.2 with the available Windows EMI source. The macOS pilot will identify and validate the energy source exposed on the M1 system. For both platforms, the paper will disclose whether the value represents CPU/package energy, whole-system energy, or an estimate.

Absolute energy values will be compared across devices only if their measurement boundaries are sufficiently equivalent. If they are not, the paper will emphasize within-device energy ratios and treat direct absolute Windows-versus-macOS energy comparison as a limitation. Latency, throughput, quality, and feasibility can still be compared under matched workloads.

### 6.6 Empirical Deliverables

* **Table 1:** Device and software configuration, including telemetry source and measurement boundary.
* **Table 2:** Per-device quality, latency, throughput, energy, and carbon metrics for every model–task configuration.
* **Figure 1:** Energy per 1,000 output tokens across model sizes, separated by device.
* **Figure 2:** A quality–carbon Pareto frontier for each task and device.
* **Figure 3:** Windows-versus-macOS latency, throughput, and model-feasibility comparison.
* **Scenario analysis:** Annualized energy, carbon, and cost savings reported separately for each device and workload assumption.

---

## 7. Expected Findings, Hypotheses & Contributions

All numerical outcomes below are hypotheses; final claims will be based on the measured results.

### Contribution 1: Reproducible Cross-Platform Consumer-Hardware Benchmark
GreenInfer will provide a device-stratified benchmark of task quality, energy, carbon, latency, throughput, and model feasibility for six quantized language models on a Windows x64/AMD laptop and an Apple Silicon/macOS laptop.

### Contribution 2: Device-Specific Task–Model Pareto Frontiers
The experiment will test whether:
- 0.5B–1.5B models are sufficient for low-complexity classification tasks;
- 3B–3.8B models form a favorable quality–energy trade-off for question answering and summarization;
- 7B–8B models provide enough additional code-generation quality to justify their resource cost;
- the optimal model-size “knee” changes between `ABU_BAKAR_LAP` and the M1 MacBook Air.

### Contribution 3: Platform Feasibility and Telemetry Guidance
The study will document the practical consequences of conventional RAM versus unified memory, differing inference backends, memory pressure, swap/page-file use, and telemetry boundaries. Conclusions will distinguish measured evidence from platform limitations.

### Contribution 4: Green Deployment Guidance for Developing Economies
The study will translate device-specific energy measurements into clearly scoped environmental and economic scenarios using a documented Bangladesh electricity-grid carbon factor and electricity-price assumption. It will not treat carbon as a hardware-only property.

---

## 8. Paper Structure Skeleton (IEEE Format, 6 Pages)

| Section | Title | Content / Focus | Page Budget |
|:---:|:---|:---|:---:|
| **§1** | **Introduction** | Green AI motivation, consumer/cross-platform gap, RQs, contributions | 0.9 page |
| **§2** | **Related Work** | Green AI, SLMs, local inference, energy profiling, telemetry comparability | 0.8 page |
| **§3** | **Experimental Methodology** | Both device specifications, existing datasets, model controls, backends, telemetry validation | 1.3 pages |
| **§4** | **Empirical Results & Analysis** | Per-device scaling, Pareto curves, feasibility, and Windows–macOS comparison | 1.7 pages |
| **§5** | **Discussion & Green Guidelines** | SLM-first routing, platform effects, grid scenarios, threats to validity | 0.8 page |
| **§6** | **Conclusion & Future Work** | Evidence-based findings and future external-meter/multi-device validation | 0.5 page |
| **§7** | **References** | 20–25 peer-reviewed citations | End of paper |

---

## 9. One-Month Work Breakdown Schedule (8 Full Working Days)

| Day | Core focus | Deliverable |
|:---:|:---|:---|
| **Day 1** | Two-device setup | Record OS/runtime/backend details; download and cache samples from the four existing datasets; pull identical model artifacts |
| **Day 2** | Pilot and telemetry validation | Test the 0.5B model on both devices; verify metric boundaries, CSV attribution, prompts, quality scoring, and repeatability |
| **Day 3** | Small-model experiments | Run 0.5B and 1.5B configurations on both devices, three measured trials each |
| **Day 4** | Medium-model experiments | Run 3B and 3.8B configurations on both devices, three measured trials each |
| **Day 5** | Large-model feasibility and experiments | Pilot 7B/8B memory feasibility, then run valid configurations; record swap, failures, or constraints explicitly |
| **Day 6** | Device-stratified analysis | Validate data; generate per-device tables, Pareto plots, and Windows–macOS comparisons |
| **Day 7** | Paper drafting | Draft introduction, related work, methodology, results, discussion, and limitations |
| **Day 8** | Audit and polishing | Verify platform attribution and claims; review statistics, figures, citations, and final IEEE PDF |

---

## 10. Target Conferences for Publication

1. **IEEE Sustainable Technologies for Industry 5.0 (IEEE STI)**
   * *Focus:* Green computing, resilient and energy-efficient AI systems, Industry 5.0 applications.
   * *Track:* Green Information and Communication Technology.
   * *Acceptance Value:* IEEE Xplore indexed, highly respected regional conference.
2. **IEEE International Green and Sustainable Computing Conference (IGSC)**
   * *Focus:* Computing energy efficiency and carbon minimization.
   * *Acceptance Value:* A strong specialized venue for green computing research.
3. **IEEE Technologies for Sustainability (IEEE SusTech)**
   * *Focus:* Practical sustainability technologies, energy measurements, and eco-software engineering.
