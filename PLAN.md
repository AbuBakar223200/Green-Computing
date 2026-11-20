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

### 6.1 Scope and Generalization Boundary

GreenInfer is a **paired case study of two complete consumer hardware–software stacks**, not a population-level comparison of all Windows and macOS systems. Its conclusions will apply to the tested `ABU_BAKAR_LAP` and M1 MacBook Air under the documented configurations. Differences cannot be attributed to the operating system alone because processor architecture, memory organization, acceleration backend, cooling, and power management also differ. Accordingly, the paper will describe observed device-level differences and will not claim that one operating-system family is universally more efficient.

### 6.2 Experimental Devices

| Device ID | Hardware | Memory | Operating System | Notes |
|:---|:---|:---|:---|:---|
| **`ABU_BAKAR_LAP`** | AMD Ryzen 5 5500U, 6 cores/12 threads, 2.10 GHz | 16 GB RAM | Windows 11 | Record OS build, power mode, memory configuration, and actual inference backend before testing. |
| **`MACBOOK_AIR_M1`** | MacBook Air `MacBookAir10,1` (`MGN63ZP/A`), Apple M1, 8 cores (4 performance + 4 efficiency) | 8 GB unified memory | macOS | Record the exact macOS version, power mode, swap use, and actual inference backend before testing. |

Private identifiers—including serial numbers, device/product IDs, hardware UUIDs, and provisioning UDIDs—will not be collected or published.

### 6.3 Existing Datasets and Fixed Sample Manifest

GreenInfer will **not create or label a new dataset**. It will download, select, and locally cache samples from four established public benchmarks:

| Task | Existing dataset | Planned measured subset | Primary quality measure |
|:---|:---|---:|:---|
| Sentiment classification | SST-2 | 50, stratified by label | Accuracy and invalid-output rate |
| Question answering | SQuAD 2.0 | 50, balanced answerable/unanswerable | Official Exact Match and token-level F1 |
| Summarization | CNN/DailyMail 3.0.0 | 50 complete, length-stratified articles | ROUGE-1/ROUGE-2/ROUGE-Lsum |
| Code generation | HumanEval | 50 fixed tasks, reported as **HumanEval-50** | Pass@1 in an isolated evaluation environment |

Before any model results are inspected, one fixed random seed will be used to create a sample manifest containing dataset repository/revision, selected example IDs, labels or answerability strata, and SHA-256 checksums. The same manifest, cached examples, prompts, references, and scoring logic will be used on both devices. SQuAD contexts and CNN/DailyMail articles will not be truncated in a way that removes required evidence; examples must fit the predeclared context limit in full. HumanEval completions will be generated during the measured interval but executed afterward in a disposable, network-disabled sandbox with time, memory, process, and filesystem limits.

### 6.4 Primary Matched-Family and Secondary Model Comparisons

The **primary scaling analysis** will minimize model-family confounding by using one Qwen-2.5 family under one common quantization:

| Primary model | Parameters | Comparison requirement |
|:---|---:|:---|
| Qwen-2.5 | 0.5B | Identical model artifact, digest, and quantization on both devices |
| Qwen-2.5 | 1.5B | Identical model artifact, digest, and quantization on both devices |
| Qwen-2.5 | 3B | Identical model artifact, digest, and quantization on both devices |
| Qwen-2.5 | 7B | Subject to the preregistered device-feasibility criteria |

The intended primary format is the same Q4 quantization on both devices; the exact Ollama tag, model digest, quantization method, and file size will be verified and frozen before data collection. Any change to this common format will be documented before the first measured run.

A **secondary practical-deployment analysis** may evaluate Llama-3.2 3B, Phi-3.5 Mini 3.8B, Mistral 7B, and Llama-3.1 8B. These heterogeneous models compare candidate deployments, not a causal parameter-scaling law, because architecture, tokenizer, training data, and instruction tuning vary by family. A secondary model that cannot meet the feasibility criteria on a device will be reported as constrained or infeasible rather than silently omitted.

### 6.5 Controlled Execution Protocol

For every model–task configuration:

1. Use the same sample manifest, prompt template, model artifact, context/output limits, stop sequences, and decoding parameters on both devices.
2. Record the exact model digest, quantization, template, context size, output-token limit, seed, temperature, top-p/top-k, and repeat settings.
3. Explicitly load the model and perform a documented unmeasured warm-up before steady-state trials; measure cold-load cost separately if reported.
4. Conduct **three randomized measured blocks per configuration per device**. Counterbalance run order so model size is not confounded with experiment time or temperature.
5. Keep each laptop plugged in, stabilize battery charge, use a fixed documented power mode and display/network state, close unnecessary applications, and record relevant background conditions.
6. Start telemetry only after warm-up, generate and preserve every raw response and API timing, stop telemetry before offline quality scoring, and then explicitly unload the model.
7. Wait for a predeclared thermal/power settling condition rather than using only a fixed short delay.
8. Record device ID, OS version/build, runtime and dependency versions, compute backend, Git commit, task, trial, UTC timestamps, token counts, peak memory, swap/page-file delta, and thermal/throttling observations.
9. Preserve request failures, invalid outputs, load failures, out-of-memory events, and retries as data; do not silently convert them into task scores.

### 6.6 Preregistered Model-Feasibility Criteria

A pilot will set a common per-request timeout and confirm the thresholds below before the full experiment. Each device–model combination will be classified as:

* **Feasible:** the model loads, completes all measured examples after at most one documented retry per transient failure, shows no severe OS memory-pressure state, increases swap/page-file use by less than 512 MB during the measured batch, and does not lose more than 20% generation throughput from the first to the last quartile of requests.
* **Memory- or thermally constrained:** the workload completes but exceeds the swap/page-file threshold, enters a severe memory-pressure or throttling state, or loses more than 20% sustained throughput.
* **Infeasible:** the model cannot load, encounters an out-of-memory termination, or completes fewer than 95% of examples within the fixed timeout after the retry rule.

All thresholds, failures, paging, and constrained runs will be reported. In particular, a constrained or infeasible 7B/8B result on the 8 GB MacBook Air is a valid hardware-capacity finding, not missing data.

### 6.7 Measurement and Telemetry Decision

| Category | Metrics / controls |
|:---|:---|
| **Runtime** | Same Ollama version where supported; exact platform backend recorded separately |
| **Performance** | Time to first token, prompt-evaluation duration/throughput, generation duration/throughput, end-to-end latency, median and p95 latency |
| **Energy** | Gross batch energy, idle-adjusted batch energy, energy/query, Wh/1k output tokens, and Wh/1k total processed tokens |
| **Carbon** | $\text{gCO}_2\text{eq}$ calculated post hoc from energy using a cited Bangladesh grid factor and sensitivity range |
| **Task quality** | Accuracy, official SQuAD EM/F1, ROUGE, and sandboxed HumanEval-50 Pass@1 as appropriate |
| **Reliability** | Failure/retry rate, invalid-output rate, peak memory, paging/swap, thermal pressure, and model feasibility class |

The preferred cross-device energy boundary is the **same external AC wall-power meter** used for both laptops. Before data collection, the meter model, sampling/logging method, resolution, stated accuracy, synchronization procedure, and measured boundary will be documented. Both gross wall energy and energy above an independently measured idle baseline will be reported while charger, battery, display, network, and power-mode conditions are controlled.

CodeCarbon/Windows EMI and the validated macOS telemetry source will be retained as diagnostic measurements and used to identify component behavior and throttling. The paper will state whether each source is measured or modeled and whether it covers CPU/package, SoC components, or the whole device.

If a suitable common external meter is unavailable, GreenInfer will **not rank the two laptops by absolute energy or carbon**. It will compare absolute energy only within each device, report within-device model energy ratios, and restrict cross-device comparison to quality, latency, throughput, memory behavior, and feasibility. This fallback measurement mode must be declared before final data collection.

Carbon will be calculated after measurement as:

\[
\text{gCO}_2\text{eq}=\text{energy}_{\text{kWh}}\times\text{grid intensity}_{\text{gCO}_2\text{eq}/\text{kWh}}
\]

The grid-factor source, geography, publication year, accounting basis, and electricity-price assumption will be cited. Auto-geolocated or silent fallback emission factors will not be used for the matched scenario.

### 6.8 Sampling and Statistical Analysis Plan

The three measured blocks are technical repetitions; they do not turn two laptops into representative samples of Windows and Mac populations. Analysis will therefore use estimation rather than a population-level “Windows vs. Mac” significance claim.

* Report every trial plus mean, median, standard deviation, p95 where relevant, and 95% confidence intervals.
* Use paired within-device model ratios for energy and latency, preserving the randomized block structure.
* Use bootstrap confidence intervals over examples for Accuracy, SQuAD EM/F1, ROUGE, and Pass@1; report the uncertainty caused by the 50-example subsets.
* If the pilot coefficient of variation for batch energy or latency exceeds 5%, expand every affected configuration from three to five measured blocks under the same protocol.
* Compute non-dominated quality–energy Pareto points separately for each task and device. Do not average incompatible task-quality scales into one score.
* Report energy per correct answer only for tasks where correctness is well defined, together with the underlying success and failure counts.

### 6.9 Threats to Validity

The final paper will explicitly discuss:

* **External validity:** one physical unit per platform supports a two-device case study, not general Windows/macOS conclusions.
* **Construct validity:** software telemetry may have different boundaries; direct energy ranking requires the common external meter.
* **Internal validity:** devices differ simultaneously in ISA, CPU/GPU acceleration, memory architecture, cooling, OS, and power management, so observed differences are whole-stack effects.
* **Model confounding:** the matched Qwen family supports the primary size analysis; heterogeneous secondary models do not isolate parameter count.
* **Benchmark validity:** public tasks may occur in model training data; model release dates, model-card decontamination claims, and contamination risk will be reported.
* **Sampling and truncation:** fixed 50-example subsets have wide uncertainty and must not be represented as full benchmark scores; required source evidence will not be truncated away.
* **Thermal and order effects:** warm-up, settling, randomized blocks, and throttling records reduce but do not eliminate these effects.
* **Carbon uncertainty:** emissions depend on the chosen grid factor, time/geography, and energy boundary rather than hardware alone.

### 6.10 Reproducibility Package

Subject to dataset and model licenses, the project will release:

* the Git commit, environment/lock files, Python and dependency versions, OS/runtime versions, and analysis environment;
* exact model tags, digests/hashes, quantization details, runtime settings, and backend allocation;
* versioned prompt templates, decoding configuration, dataset revision, fixed sample manifest, and manifest checksum;
* per-example raw responses, error categories, token/timing fields, and offline quality scores;
* per-trial raw and summarized telemetry, idle-baseline measurements, meter metadata, and run-order log;
* analysis scripts that regenerate every table, confidence interval, feasibility classification, and Pareto figure.

The released metadata will use study device IDs and will exclude personal identifiers and secrets.

### 6.11 Empirical Deliverables

* **Table 1:** Device, software, model-artifact, backend, power-state, and telemetry configuration.
* **Table 2:** Per-device quality, latency, throughput, memory, reliability, energy, and carbon results with uncertainty.
* **Table 3:** Feasible, constrained, and infeasible model configurations with failure evidence.
* **Figure 1:** Energy per query and per 1,000 tokens across primary matched-family model sizes, separated by device.
* **Figure 2:** Computed quality–energy Pareto frontier for each task and device.
* **Figure 3:** Windows-laptop versus M1-Mac latency, throughput, memory, and feasibility case-study comparison.
* **Scenario analysis:** Annualized energy, carbon, and cost savings reported separately for each device, workload assumption, and quality threshold.
* **Reproducibility archive:** Sample manifest, configurations, raw outputs, raw telemetry, and analysis materials needed to reproduce the paper.

---

## 7. Expected Findings, Hypotheses & Contributions

All numerical outcomes below are hypotheses; final claims will be based on the measured results.

### Contribution 1: Reproducible Cross-Platform Consumer-Hardware Case Study
GreenInfer will provide a device-stratified case study of task quality, energy, carbon, latency, throughput, memory behavior, and model feasibility for a matched Qwen-2.5 scaling family on one Windows x64/AMD laptop and one Apple Silicon/macOS laptop. Any heterogeneous secondary models will be reported separately as practical deployment candidates.

### Contribution 2: Device-Specific Task–Model Pareto Frontiers
The experiment will test whether:
- 0.5B–1.5B models are sufficient for low-complexity classification tasks;
- the matched 3B model provides a favorable quality–energy trade-off for question answering and summarization;
- the matched 7B model provides enough additional quality to justify its resource cost where it is feasible;
- the optimal model-size “knee” changes between `ABU_BAKAR_LAP` and the M1 MacBook Air;
- heterogeneous secondary models change the practical deployment choice without being mistaken for a controlled parameter-scaling result.

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
| **§3** | **Experimental Methodology** | Scope boundary, devices, fixed sample manifest, matched model family, feasibility rules, energy protocol, statistics | 1.5 pages |
| **§4** | **Empirical Results & Analysis** | Per-device scaling, uncertainty, Pareto curves, feasibility, and two-device case-study comparison | 1.6 pages |
| **§5** | **Discussion & Green Guidelines** | SLM-first routing, whole-stack effects, grid scenarios, threats to validity | 0.8 page |
| **§6** | **Conclusion & Future Work** | Evidence-based findings and future multi-device replication | 0.4 page |
| **§7** | **References** | 20–25 peer-reviewed citations | End of paper |

---

## 9. One-Month Work Breakdown Schedule (8 Full Working Days)

| Day | Core focus | Deliverable |
|:---:|:---|:---|
| **Day 1** | Freeze study inputs | Record OS/runtime/backend details; create the fixed dataset manifest; freeze Qwen artifacts, prompts, settings, and checksums |
| **Day 2** | Pilot and measurement decision | Test 0.5B on both devices; validate the common wall meter or declare the within-device fallback; verify scoring and feasibility thresholds |
| **Day 3** | Small-model randomized blocks | Run matched Qwen 0.5B and 1.5B configurations on both devices, three measured blocks each |
| **Day 4** | Medium/large matched-family blocks | Run matched Qwen 3B and pilot/run 7B under the preregistered feasibility rules |
| **Day 5** | Secondary candidates and reruns | Test selected Llama/Phi/Mistral candidates; expand high-variance cells to five blocks; record constrained/infeasible outcomes |
| **Day 6** | Device-stratified analysis | Score saved outputs offline; calculate uncertainty, feasibility classes, Pareto frontiers, and scoped two-device comparisons |
| **Day 7** | Paper and reproducibility package | Draft all sections and assemble manifests, configurations, raw outputs/telemetry, and analysis materials |
| **Day 8** | Audit and polishing | Verify scope, platform attribution, statistics, threats to validity, reproducibility, citations, and final IEEE PDF |

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
