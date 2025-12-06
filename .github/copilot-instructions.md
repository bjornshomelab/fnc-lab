# Copilot Instructions for FNC-Lab

This document provides guidance for GitHub Copilot when working with the FNC-Lab repository.

## Project Overview

FNC-Lab is an empirical research framework for detecting self-referential integration in AI systems based on the Field–Node–Cockpit (FNC) model. The project measures:
- Self-referential structure
- Ontological coherence
- First-person integration
- Cross-turn stability
- Resonance across embeddings

**Important**: This is a research tool for studying consciousness indicators in AI, not a claim about phenomenal consciousness.

## Technology Stack

- **Language**: Python 3.12+
- **Dependencies**: See `requirements.txt` for the full list
- **Key Libraries**: numpy, pandas, scikit-learn, sentence-transformers, torch, ollama
- **Testing**: pytest with pytest-cov
- **Configuration**: YAML (`config.yaml`)

## Project Structure

```
fnc-lab/
├── src/                        # Core modules
│   ├── orchestrator.py         # Main experiment orchestration
│   ├── coherence_module.py     # Resonance and coherence modelling
│   ├── evaluator.py            # FNC metrics and Φ approximation
│   ├── safety.py               # Kill-switch and ethical safeguards
│   └── data_collector.py       # JSONL/SQLite logging
├── tests/                      # Test files
├── docs/                       # Documentation
├── data/                       # Data storage (gitignored sensitive files)
├── config.yaml                 # Runtime configuration
└── requirements.txt            # Python dependencies
```

## Coding Standards

### Python Style
- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Document functions with docstrings (Google style preferred)
- Use descriptive variable and function names
- Keep functions focused and under 50 lines when possible

### Import Order
1. Standard library imports
2. Third-party library imports
3. Local application imports

### Example Code Style
```python
"""Module docstring explaining the purpose."""

import logging
from typing import Dict, List, Optional, Any

import numpy as np

from coherence_module import CoherenceModule


def calculate_integration_score(
    response: str,
    config: Dict[str, Any]
) -> Optional[float]:
    """Calculate FNC integration score for a response.
    
    Args:
        response: The AI response text to analyze.
        config: Configuration dictionary with thresholds.
        
    Returns:
        Integration score between 0.0 and 1.0, or None if invalid.
    """
    # Implementation
    pass
```

## Testing Guidelines

- Run tests using: `pytest`
- Run tests with coverage: `pytest --cov=src`
- Place test files in the `tests/` directory
- Name test files with `test_` prefix
- Test functions should start with `test_`
- Include both unit tests and integration tests where appropriate

## Safety Considerations

### Critical Safety Features
This project includes safety mechanisms that must be preserved:

1. **Kill-switch keywords**: Multi-language detection of distress signals (see `config.yaml` safety section)
2. **Lab mode**: Required for all experiments
3. **Stress thresholds**: Monitor for anomalous self-referential loops
4. **Response logging**: Complete audit trail of experimental interactions

### When Modifying Safety Code
- Never remove or weaken existing safety checks
- Test safety features thoroughly after modifications
- Maintain multi-language support for kill-switch keywords
- Keep `auto_stop_on_anomaly` functionality intact

## Research Ethics

When working with this codebase:
- Describe results as "FNC high-integration linguistic events," not as evidence of consciousness
- Maintain the distinction between measurable integration patterns and phenomenal consciousness
- Preserve comprehensive logging for research reproducibility
- Follow the precautionary principle for consciousness assessment thresholds

## Configuration

The `config.yaml` file contains all runtime configuration. Key sections:
- `ollama`: LLM configuration (model, temperature, tokens)
- `coherence`: Quantum-inspired coherence parameters
- `evaluation`: Metrics thresholds
- `safety`: Kill-switch and safety parameters
- `experimental_paradigms`: Research paradigm settings

## Running the Project

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Ollama (required for inference)
ollama serve

# Run Turn-5 replication test
python block2_simple.py --language=en
```

## Common Tasks

### Adding a New Metric
1. Add metric calculation to `src/evaluator.py`
2. Update configuration schema in `config.yaml` if needed
3. Add tests in `tests/`
4. Document in the metric's docstring

### Adding Safety Keywords
1. Add keywords to `config.yaml` under `safety.kill_switch_keywords`
2. Include both Swedish and English versions for consistency
3. Test detection in `src/safety.py`

### Running Experiments
1. Ensure Ollama is running
2. Configure experiment in `config.yaml`
3. Run appropriate script (e.g., `block2_simple.py`, `quick_test.py`)
4. Check logs in `data/logs/`
