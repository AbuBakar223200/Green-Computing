# 📚 GreenInfer: Related Research Papers (2024–2026)

> **10 Verified, Peer-Reviewed/arXiv Papers** directly related to the GreenInfer research gaps.  
> Each entry includes: verified arXiv link, authors, venue, key findings, and how it connects to our paper.

---

## Paper 1

**Title:** Power Hungry Processing: Watts Driving the Cost of AI Deployment?  
**Authors:** Alexandra Sasha Luccioni, Yacine Jernite, Emma Strubell  
**Year:** 2023 (presented at ACM FAccT 2024)  
**Link:** [https://arxiv.org/abs/2311.16863](https://arxiv.org/abs/2311.16863)  
**Venue:** ACM Conference on Fairness, Accountability, and Transparency (FAccT '24)

**Key Findings:**
- First comprehensive study measuring inference energy across multiple AI model types (text, image, multimodal)
- Generative models consume orders of magnitude more energy than task-specific fine-tuned models
- Cumulative inference deployment can match or exceed training energy footprint at scale
- Open-sourced evaluation methodology using CodeCarbon

**Relevance to GreenInfer:**
- **Foundational baseline paper** — we extend their inference benchmarking from datacenter GPUs to consumer CPUs
- They studied general model types; we provide task-specific granularity across 4 downstream NLP tasks
- Their hardware: NVIDIA A100 datacenter GPU → Our hardware: AMD Ryzen 5 consumer laptop

---

## Paper 2

**Title:** Towards Sustainable NLP: Insights from Benchmarking Inference Energy in Large Language Models  
**Authors:** Soham Poddar, Paramita Koley, Janardan Misra, Sanjay Podder, Niloy Ganguly, Saptarshi Ghosh  
**Year:** 2025  
**Link:** [https://arxiv.org/abs/2502.05610](https://arxiv.org/abs/2502.05610)  
**Venue:** NAACL 2025 (Main Conference)

**Key Findings:**
- Inference energy strongly correlates with output token length and response time
- Quantization significantly reduces inference energy consumption
- Optimal batch sizes and targeted prompt phrasing yield further energy savings
- Provides practical deployment guidelines for sustainable NLP

**Relevance to GreenInfer:**
- Validates our experimental variable choice (token count, response time) as key energy predictors
- Their experiments use datacenter-grade serving backends (vLLM, batched) → Ours uses local Ollama single-user inference on consumer hardware
- Supports our RQ1 (energy scaling) design; we complement their datacenter findings with edge-consumer data

---

## Paper 3

**Title:** How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM Inference  
**Authors:** Nidhal Jegham, Marwan Abdelatti, Lassad Elmoubarki, Abdeltawab Hendawi  
**Year:** 2025  
**Link:** [https://arxiv.org/abs/2505.09598](https://arxiv.org/abs/2505.09598)  
**Venue:** arXiv preprint

**Key Findings:**
- Benchmarked 30 state-of-the-art models across energy, water, and carbon footprint
- Reasoning-heavy models (o3, DeepSeek-R1) consume over 33 Wh per long prompt — 70× more than efficient nano models
- Uses Data Envelopment Analysis (DEA) for eco-efficiency ranking
- Scaling to 700M queries/day = electricity of 35,000 US homes

**Relevance to GreenInfer:**
- Their scope: commercial cloud API-based models → Our scope: local open-source models on consumer hardware
- They demonstrate the massive scale problem; we provide a practical mitigation path via local SLM deployment
- Their water footprint dimension is out of our scope but informs future work direction
- Supports our Gap 1 (they measure cloud; nobody measures consumer-grade hardware)

---

## Paper 4

**Title:** Sustainable LLM Inference for Edge AI: Evaluating Quantized LLMs for Energy Efficiency, Output Accuracy, and Inference Latency  
**Authors:** Erik Johannes Husom, Arda Goknil, Merve Astekin, Lwin Khin Shar, Andre Kåsen, Sagar Sen, Benedikt Andreas Mithassel, Ahmet Soylu  
**Year:** 2025  
**Link:** [https://arxiv.org/abs/2504.03360](https://arxiv.org/abs/2504.03360)  
**Venue:** arXiv preprint (SINTEF / Singapore Management University / Oslo Metropolitan University)

**Key Findings:**
- Evaluated 28 quantized LLMs from the Ollama library on a Raspberry Pi 4 (4GB RAM)
- Used hardware-level energy profiling across 5 benchmark datasets (CommonsenseQA, BIG-Bench Hard, TruthfulQA, GSM8K, HumanEval)
- Charts the balance between quantization level, energy efficiency, latency, and output accuracy on constrained edge devices
- Identifies optimal quantization configurations for sustainable edge AI deployment

**Relevance to GreenInfer:**
- **Most closely related paper** — also uses Ollama + quantized models + hardware-level energy measurement
- Their hardware: Raspberry Pi 4 (4GB, ARM) → Our hardware: AMD Ryzen 5 laptop (16GB, x64 Windows)
- They focus on extreme edge constraints; we focus on mainstream consumer laptops — a much larger user population
- Our Gap 3 (quantization carbon measurement) directly builds on and extends their work to Windows/x86 architecture

---

## Paper 5

**Title:** Emissions and Performance Trade-off Between Small and Large Language Models  
**Authors:** Anandita Garg, Uma Gaba, Deepan Muthirayan, Anish Roy Chowdhury  
**Year:** 2025 (January 2025)  
**Link:** [https://arxiv.org/abs/2601.08844](https://arxiv.org/abs/2601.08844)  
**Venue:** 3rd International Conference on Foundation and Large Language Models (IEEE FLLM)

**Key Findings:**
- Evaluated fine-tuned SLMs vs. LLMs across NLP, reasoning, and programming tasks
- In 4 out of 6 tasks, fine-tuned SLMs matched or closely maintained comparable performance to massive LLMs
- Demonstrates significant reductions in carbon emissions from inference when using SLMs
- Advocates for task-aware model selection as a Green AI strategy

**Relevance to GreenInfer:**
- Directly validates our central hypothesis (SLMs can replace LLMs for many tasks with carbon savings)
- Their method: fine-tuned SLMs → Our method: off-the-shelf quantized SLMs (zero fine-tuning needed, more practical)
- Their task count: 6 → Our task count: 4 (but with deeper energy granularity per task)
- Supports our RQ2 (Pareto frontier between accuracy and carbon)

---

## Paper 6

**Title:** Ground-Truthing AI Energy Consumption: Validating CodeCarbon Against External Measurements  
**Authors:** Raphael Fischer  
**Year:** 2025 (September 2025)  
**Link:** [https://arxiv.org/abs/2509.22092](https://arxiv.org/abs/2509.22092)  
**Venue:** arXiv preprint (Johannes Gutenberg University Mainz)

**Key Findings:**
- Systematically validates CodeCarbon's software-based energy estimates against hardware "ground-truth" measurements using external energy meters
- CodeCarbon's estimation errors can reach up to 40% under certain hardware/configuration conditions
- Errors stem from RAPL/NVML sampling gaps, missing peripheral energy draws, and unaccounted PUE factors
- Establishes that CodeCarbon reliably captures relative trends even when absolute values deviate

**Relevance to GreenInfer:**
- **Critical citation for our Methodology section** — justifies our use of CodeCarbon as a measurement tool
- We will cite this paper to acknowledge CodeCarbon's limitations and explain why we report relative comparisons (Model A vs. Model B) rather than claiming exact absolute watts
- Validates our Windows EMI-based tracking approach as a practical, accessible research methodology

---

## Paper 7

**Title:** GreenBench: Benchmarking Energy Efficiency and Carbon Footprint of Open-Source LLM Inference on Apple Silicon  
**Authors:** Rajeswari Kannan et al.  
**Year:** 2026 (August 2026)  
**Link:** [https://arxiv.org/abs/2608.28667](https://arxiv.org/abs/2608.28667)  
**Venue:** IEEE ICCUBEA 2026

**Key Findings:**
- Benchmarks open-source LLMs (3B–9B) on Apple M4 Pro with unified memory (48GB)
- Apple Silicon achieves 30–40× better energy per token than datacenter GPUs for single-user inference
- Smaller 3B models yield up to 62% less energy per token vs. 7B–9B models
- Uses macOS `powermetrics` for direct hardware-level power measurement
- Advocates making energy-per-token a standard benchmarking metric

**Relevance to GreenInfer:**
- **Closest sibling paper** — same concept (consumer hardware LLM energy benchmarking) but on Apple Silicon (macOS)
- Our paper fills the **Windows x86/AMD** gap that GreenBench does not cover
- Their hardware: Apple M4 Pro 48GB unified memory (premium consumer) → Our hardware: AMD Ryzen 5 16GB (mainstream budget consumer)
- Together with GreenBench, our paper would provide cross-platform coverage of consumer LLM inference efficiency

---

## Paper 8

**Title:** Intelligence per Watt: Measuring Intelligence Efficiency of Local AI  
**Authors:** Jon Saad-Falcon, Avanika Narayan, Christopher Ré, John Hennessy et al.  
**Year:** 2025 (November 2025)  
**Link:** [https://arxiv.org/abs/2511.07885](https://arxiv.org/abs/2511.07885)  
**Venue:** arXiv preprint (Stanford University / Together AI)

**Key Findings:**
- Introduces the **Intelligence per Watt (IPW)** metric: task accuracy divided by power consumed
- Evaluated 20+ local LMs (≤20B active parameters) across 8 hardware accelerators and 1M real-world queries
- Local LMs successfully answer 88.7% of single-turn chat and reasoning queries
- Local inference efficiency improved 5.3× between 2023 and 2025 (3.1× from algorithms, 1.7× from hardware)
- Viable locally-serviced workload share grew from 23.2% (2023) to 71.3% (2025)

**Relevance to GreenInfer:**
- Provides theoretical backing for our RQ3 (SLM-first routing saves carbon at scale)
- Their IPW metric informs our Pareto analysis design (accuracy/energy trade-off)
- Their scale: longitudinal multi-hardware study → Our scale: single-hardware deep-dive with task granularity
- Strongly supports our paper's narrative that local consumer inference is viable and green

---

## Paper 9

**Title:** Energy-Aware Code Generation with LLMs: Benchmarking Small vs. Large Language Models for Sustainable AI Programming  
**Authors:** Humza Ashraf, Syed Muhammad Danish, Aris Leivadeas, Yazan Otoum, Zeeshan Sattar  
**Year:** 2025 (August 2025)  
**Link:** [https://arxiv.org/abs/2508.08332](https://arxiv.org/abs/2508.08332)  
**Venue:** arXiv preprint

**Key Findings:**
- Benchmarked SLMs (StableCode-3B, StarCoderBase-3B, Qwen2.5-Coder-3B) vs. LLMs (GPT-4.0, DeepSeek-Reasoner) on 150 LeetCode problems
- In over 52% of evaluated problems, SLMs consumed the same or less energy than LLMs when producing correct outputs
- LLMs still lead on hard abstract reasoning correctness, but SLMs are competitive for foundational coding
- Evaluated runtime, memory usage, energy consumption, and functional correctness

**Relevance to GreenInfer:**
- Directly complements our HumanEval (code generation) task benchmark
- Their focus: code-only tasks with coding-specialized models → Our focus: 4 diverse NLP tasks including code generation
- Shows that even in code generation (the hardest task), SLMs can be competitive — supports our expected finding
- Their measurement: runtime energy of generated code → Our measurement: inference energy to produce the code

---

## Paper 10

**Title:** From Prompts to Power: Measuring the Energy Footprint of LLM Inference  
**Authors:** Xander Kayser et al.  
**Year:** 2025 (November 2025)  
**Link:** [https://arxiv.org/abs/2511.11147](https://arxiv.org/abs/2511.11147)  
**Venue:** arXiv preprint

**Key Findings:**
- Massive-scale empirical study: 32,500+ measurements across 21 GPU configurations and 155 model architectures
- Uses vLLM serving backend for production-realistic inference benchmarking
- Models prompt-level energy usage to build predictive estimators for unseen hardware/architectures
- Establishes energy consumption correlations with model size, quantization level, and prompt characteristics

**Relevance to GreenInfer:**
- Their scale: 21 GPU configurations, 155 models (datacenter-centric) → Our scale: 1 consumer CPU, 6 models (consumer-centric)
- Their predictive energy estimator could be validated against our real consumer-hardware measurements
- Demonstrates the field's hunger for empirical energy data — our consumer-hardware datapoints fill a unique niche
- Supports our Gap 1 (massive datacenter studies exist; consumer hardware studies do not)

---

## Summary Table

| # | Paper | Year | Hardware Focus | Our Differentiation |
|:---:|:---|:---:|:---|:---|
| 1 | Luccioni et al. — Power Hungry Processing | 2024 | Datacenter A100 GPU | We benchmark on consumer CPU |
| 2 | Poddar et al. — Sustainable NLP | 2025 | Datacenter (batched) | We benchmark single-user local inference |
| 3 | Jegham et al. — How Hungry is AI? | 2025 | Cloud APIs (30 models) | We benchmark local open-source models |
| 4 | Husom et al. — Sustainable Edge AI | 2025 | Raspberry Pi 4 (ARM) | We benchmark x86 Windows laptop |
| 5 | Garg et al. — SLM vs LLM Emissions | 2025 | General (fine-tuned) | We use off-the-shelf quantized models |
| 6 | Fischer — CodeCarbon Validation | 2025 | Validation study | We cite to justify our tool choice |
| 7 | Kannan et al. — GreenBench | 2026 | Apple Silicon (macOS) | We benchmark AMD/Windows (cross-platform) |
| 8 | Saad-Falcon et al. — Intelligence per Watt | 2025 | Multi-hardware (IPW) | We provide task-granular Pareto analysis |
| 9 | Ashraf et al. — Energy-Aware Code Gen | 2025 | Code tasks only | We cover 4 diverse NLP tasks |
| 10 | Kayser et al. — Prompts to Power | 2025 | 21 GPU configs (datacenter) | We fill the consumer hardware data gap |
