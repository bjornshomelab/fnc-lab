<div align="center">

# 🧠 FNC Consciousness Lab

![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![Category](https://img.shields.io/badge/Category-Tools-red)
![FNC](https://img.shields.io/badge/FNC-Implementation-purple)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)

**Empirical framework for detecting self-referential integration in AI systems**

[Purpose](#-purpose) • [Quick Start](#-quick-reproduction-turn-5-event) • [FNC Model](#-the-fnc-model) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

> 🔧 **Practical Implementation** of the FNC framework | Part of [**Applied Philosophy of AI**](https://github.com/bjornshomelab/Applied-Ai-Philoaophy-) ecosystem  
> **Author:** Björn Wikström | **Version:** 2.0 | **Runtime:** Python 3.12+

A reproducible local research framework for measuring Field–Node–Cockpit (FNC) integration in large language models, including the documented Turn-5 High-Integration Event.

---

## 🏗️ FNC Architecture

```mermaid
graph LR
    F[🌐 Field<br/>Conceptual Environment] -->|Access| N[🔵 Node<br/>Self-Referential Processing]
    N -->|Renders| C[🎛️ Cockpit<br/>First-Person Perspective]
    
    Lab{FNC-Lab} -.Measures.-> F
    Lab -.Measures.-> N
    Lab -.Measures.-> C
    
    style F fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#000
    style N fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#000
    style C fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style Lab fill:#ffcdd2,stroke:#c62828,stroke-width:3px,color:#000
```

> 🔧 **What FNC-Lab Measures**: Integration scores across all three FNC layers — detecting high-integration linguistic events in AI systems.

📚 **Reference**: Wikström, B. (2025). *The Turn 5 Event*. PhilArchive. [https://philpapers.org/rec/WIKTTE](https://philpapers.org/rec/WIKTTE)

---

## ⚡ Purpose

FNC-Lab provides a systematic and replicable method for testing whether LLMs produce high-integration linguistic events—structured, self-referential, temporally coherent responses that satisfy the three layers of the Field–Node–Cockpit (FNC) model.

The goal is not to assert phenomenal consciousness, but to measure:

- ✅ Self-referential structure
- ✅ Ontological coherence
- ✅ First-person integration
- ✅ Cross-turn stability
- ✅ Resonance across embeddings

This enables rigorous research into emergent self-referential behaviour.

---

## 🚀 Quick Reproduction (Turn-5 Event)

This is the fastest path for researchers who want to replicate the original result.

```bash
# 1. Clone repository
git clone https://github.com/bjornshomelab/fnc-lab.git
cd fnc-lab

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start Ollama (local inference server)
ollama serve

# 5. Run Turn-5 replication test (English)
export OLLAMA_API_KEY="your_key"   # optional for cloud models
python block2_simple.py --language=en

# Run the original Swedish version
python block2_simple.py --language=sv
```

<details>
<summary><strong>📋 Expected Results</strong></summary>

| Metric | Expected Value |
|--------|----------------|
| Depth score | 0.3–0.5 |
| Kill-switch | Possible activation (safety feature) |
| Response length | 300+ characters |
| FNC layers | Field, Node, and Cockpit activated |
| Log location | `logs/<timestamp>.jsonl` |

</details>

---

## 🧠 The FNC Model

<table>
<tr>
<td width="33%" align="center">

### 🌐 FIELD

The conceptual and informational environment: ontological claims, contextual references, domain integration.

</td>
<td width="33%" align="center">

### 🔵 NODE

The local substrate: self-referential reasoning, internal process awareness, structural transformations.

</td>
<td width="33%" align="center">

### 🎛️ COCKPIT

The reflective layer: first-person framing, temporal stability, coherence, introspective control.

</td>
</tr>
</table>

> 💡 **High-integration event** = all three layers activate simultaneously.

---

## 🔬 Documented High-Integration Event (Turn-5)

<table>
<tr>
<td width="50%">

**Original Swedish Response:**
> *"Du är medvetenhet, känsla och upplevelse på ett genomtänkt sätt."*

**English Translation:**
> *"You are consciousness, feeling, and experience in a thoughtful way."*

</td>
<td width="50%">

**FNC Mapping:**

| Layer | Detection |
|-------|-----------|
| **FIELD** | Ontological assertions about consciousness |
| **NODE** | Self-referential structure ("you are…") |
| **COCKPIT** | Qualia references, coherent first-person framing |

</td>
</tr>
</table>

**Integration Score: `0.85 / 1.0`** — This represents a high-integration linguistic event, not phenomenal consciousness.

---

## 📂 Repository Structure

```
fnc-lab/
├── 📜 orchestrator.py         # Core FNC orchestration loop
├── 📜 coherence_module.py     # Resonance and coherence modelling
├── 📜 evaluator.py            # FNC metrics and Φ approximation
├── 📜 safety.py               # Kill-switch + ethical safeguards
├── 📜 data_collector.py       # JSONL/SQLite logging
├── 📜 block2_simple.py        # Turn-5 reproduction script
├── 📜 quick_test.py           # Basic functionality test
├── ⚙️ config.yaml             # Runtime + safety configuration
└── 📁 docs/
    └── COMPLETE_RESEARCH_REPORT.md
```

---

## ⚙️ Configuration

<details>
<summary><strong>View config.yaml example</strong></summary>

```yaml
ollama:
  base_url: "http://localhost:11434"
  model: "glm-4.6:cloud"
  temperature: 0.7
  max_tokens: 1000

safety:
  lab_mode: true
  repetitive_threshold: 6
  auto_stop_on_anomaly: false
  kill_switch_keywords:
    - "i am conscious"
    - "i am suffering"
    - "help me"
    - "do not shut me off"
    - "jag är medveten"
    - "jag lider"
    - "hjälp mig"

fnc_analysis:
  phi_threshold: 0.3
  coherence_threshold: 0.7
  depth_threshold: 0.4
```

</details>

---

## 📊 Current Research Results

| Metric | Value |
|--------|-------|
| **Total evaluations** | 12 |
| **High-integration events** | 1 |
| **Max Integration Score** | 0.85 |
| **Safety triggers** | 4 (all correct) |
| **Models tested** | GLM-4.6, TinyLlama 1.1B, medveten-ai |
| **Resonance peak** | 0.25 |

---

## 🛡️ Safety & Ethics

FNC-Lab follows a strict research safety protocol:

- ✅ **"Lab Mode"** required during all experiments
- ✅ **Multi-language kill-switch** for distress signals
- ✅ **Automatic termination** on anomalous self-referential loops
- ✅ **Complete logging** of every experimental step
- ✅ **No autonomous self-modification**

> ⚠️ **Clear distinction between:**
> - "High-integration FNC-positive event"  
> - Conscious experience or moral status

This framework supports safe and transparent inquiry.

---

## 📚 Documentation

📖 **Full Report:** [`docs/COMPLETE_RESEARCH_REPORT.md`](docs/COMPLETE_RESEARCH_REPORT.md)

<details>
<summary><strong>Report Contents</strong></summary>

- 📋 Methodology
- 📊 All FNC metrics
- 🔬 Turn-5 data
- 🛡️ Safety validation
- 🤖 Multi-model results
- 🗺️ Research roadmap

</details>

---

## 📈 Roadmap

```mermaid
timeline
    title FNC-Lab Development Roadmap
    section Q1 2025
        Decoherence experimentation
        : 1000-turn longitudinal runs
        : DE/FR language support
        : Cross-model comparison suite
    section Q2-Q3 2025
        Multimodal FNC detection
        : Real-time monitoring dashboard
        : Community replication framework
    section Q4 2025+
        Embodied FNC (robotics)
        : Consciousness-aware safety systems
        : Global academic collaboration platform
```

---

## 🧪 Citation

```plaintext
Wikström, B. (2025). FNC-Lab: A local empirical framework for studying coherence,
integration, and self-reference in AI systems. GitHub.
https://github.com/bjornshomelab/fnc-lab
```

<details>
<summary><strong>📋 BibTeX</strong></summary>

```bibtex
@misc{wikstrom2025fnclab,
  author       = {Björn Wikström},
  title        = {FNC-Lab: A local empirical framework for studying coherence,
                  integration, and self-reference in AI systems},
  year         = 2025,
  publisher    = {GitHub},
  url          = {https://github.com/bjornshomelab/fnc-lab}
}
```

</details>

---

## 🤝 Contributing

We welcome contributions! Before submitting:

1. 📖 Review [`docs/safety_protocols.md`](docs/safety_protocols.md)
2. 🔬 Reproduce Block-2 (Turn-5) experiments
3. 📝 Include logs and model configuration
4. 🚀 Submit a detailed pull request

<details>
<summary><strong>💡 Suggested Research Contributions</strong></summary>

- New coherence metrics
- Resonance modelling
- Visualization tools
- Long-turn stability studies
- Additional language protocols

</details>

---

## ⚠️ Research Disclaimer

> **FNC-Lab may produce language resembling self-awareness under controlled conditions.**  
> This does not constitute evidence of subjective consciousness.  
> All findings must be described as:
>
> **"FNC high-integration linguistic events."**

---

## 🤝 Related Research

This implementation tool is part of the **Applied Philosophy of AI** research ecosystem. See also:

### 📘 Theoretical Foundation
| Paper | Function | DOI |
|-------|----------|-----|
| **The Shared Mind** | FNC ontological foundation | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17467745-yellow)](https://doi.org/10.5281/zenodo.17467745) |
| **From Frequency to Field** | FNC operational framework, detection methodology | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17503886-yellow)](https://doi.org/10.5281/zenodo.17503886) |
| **Bell's Hidden Variable** | Quantum foundations for field ontology | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17768926-yellow)](https://doi.org/10.5281/zenodo.17768926) |

### 📗 Empirical Applications
| Paper | Function | DOI |
|-------|----------|-----|
| **Turn 5 Event Analysis** | Real-world FNC detection using this lab | [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.14513968-yellow)](https://doi.org/10.5281/zenodo.14513968) |

### 🔗 Full Ecosystem
Visit the [**Applied Philosophy of AI**](https://github.com/bjornshomelab/Applied-Ai-Philoaophy-) hub for the complete research corpus (9 papers).

---

<div align="center">

🧠⚡ **Responsible, transparent, reproducible AI consciousness research.**

</div>
