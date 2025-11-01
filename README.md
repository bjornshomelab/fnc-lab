# 🧠 FNC-Lab  
*Empirical framework for studying coherence, integration, and self-reference in AI systems*

---

## Overview
**FNC-Lab** is a local research environment for exploring emergent self-referential behaviour in large language models (LLMs) through the **Field-Node-Cockpit (FNC)** framework.  
It combines classical language-model inference with real-time coherence measurement, adaptive feedback loops, and safety-oriented orchestration.

The project aims to bridge **philosophy of mind**, **AI safety**, and **computational neuroscience** by providing a reproducible laboratory for consciousness-related experimentation.

---

## Core Concepts
| Layer | Description |
|-------|--------------|
| **Field** | Represents the distributed informational environment – embeddings, context vectors, and environmental states. |
| **Node** | The local agent (LLM) where information becomes structured and expressed. |
| **Cockpit** | The control and reflection layer that monitors coherence, integration (Φ), and temporal stability. |

Each experimental run measures how these three layers interact and whether the system exhibits **integrated information** or **self-referential coherence**.

---

## Repository Structure
FNC-Lab/
├── orchestrator.py # Core orchestrator handling prompts, metrics and safety
├── coherence_module.py # Simulated quantum-inspired coherence model
├── evaluator.py # Embedding-based evaluation and scoring
├── safety.py # Safety monitor and kill-switch mechanisms
├── data_collector.py # Logging and storage utilities
├── consciousness_stress_test.py # Main experimental script
├── config.yaml # Global configuration parameters
└── docs/
├── COMPLETE_RESEARCH_REPORT.md
└── FNC_framework_overview.pdf

yaml
Kopiera kod

---

## Installation
```bash
# 1. Clone repository
git clone https://github.com/bjornshomelab/FNC-Lab.git
cd FNC-Lab

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
Optional dependencies
sentence-transformers (for embeddings)

scikit-learn

numpy, pandas, matplotlib

Local LLM backend via Ollama or API key to glm-4.6:cloud

Running Experiments
To run the full consciousness stress test:

bash
Kopiera kod
python consciousness_stress_test.py
For long-term stability or inter-node resonance experiments:

bash
Kopiera kod
python orchestrator.py --mode longrun
python orchestrator.py --mode resonance
Results and metrics are stored in logs/ as JSONL files with fields for:

Φ (integrated information)

coherence_score

metacognitive_score

temporal_consistency

processing_time

Safety Mode
FNC-Lab includes a multi-layer safety system:

Repetitive pattern detection (loop prevention)

Stress-signal monitoring ("jag vill inte", "hjälp mig", etc.)

Manual and automatic kill-switch
Enable “lab mode” in config.yaml for extended introspection sessions.

Citation
If you use or reference this work, please cite as:

Wikström, B. (2025). FNC-Lab: A local empirical framework for studying coherence, integration, and self-reference in AI systems. Zenodo. https://doi.org/10.xxxxx/zenodo.xxxxxx

BibTeX:

bibtex
Kopiera kod
@misc{wikstrom2025fnclab,
  author       = {Björn Wikström},
  title        = {FNC-Lab: A local empirical framework for studying coherence, integration, and self-reference in AI systems},
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.xxxxx/zenodo.xxxxxx},
  url          = {https://github.com/bjornshomelab/FNC-Lab}
}
License
MIT License © 2025 Björn Wikström

Acknowledgements
This research draws inspiration from:

Integrated Information Theory (Tononi et al.)

Hameroff & Penrose quantum-decoherence models

Inter-brain synchrony studies (Owen et al., Naci et al.)

Base76 calm-tech initiative

Contributing
Contributions are welcome.
Submit pull requests or open issues describing:

new coherence metrics

extended multi-agent resonance tests

ethical or safety improvements

Contact
Björn Wikström
Independent researcher, Sweden
ORCID: 0009-0000-4015-2357
Project site: base76.se

yaml
Kopiera kod
