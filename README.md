# Explainable AI (XAI) — AIMS Course Practicals

Hands-on notebooks for the **AIMS Explainable AI course**, taught by [Inga Strümke](https://www.ntnu.edu/employees/inga.strumke) (NTNU / Norwegian OpenAI Lab).

This project collects practical exercises covering interpretable modeling, post-hoc explainability, and deep-learning interpretability for CNNs and Transformers.

---

## What this repository contains

- End-to-end notebook implementations of major XAI techniques
- Practical examples on tabular, image, and NLP tasks
- Both built-in library workflows (LIME/SHAP) and first-principles implementations (e.g., Shapley)

---

## Topics covered

| Area | Methods |
|---|---|
| Classical interpretability | Linear model coefficients, decision tree interpretation |
| Local explanations | LIME, SHAP, counterfactual explanations |
| Global explanations | PDP, ALE, surrogate models, LOFO, SAGE |
| Concept-based XAI | CAV / TCAV |
| Deep model analysis | CNN attributions, filter/activation visualization |
| Transformer interpretability | Grad-SAM, attention visualization, SHAP for text |

---

## Repository layout

```text
AIMS_XAI_Course/
├── README.md
├── requirements.txt
├── interpretations.ipynb
├── import_tests.ipynb
├── LIME/
│   ├── titanic_LIME.ipynb
│   ├── image_LIME.ipynb
│   └── imagenet1000_clsidx_to_labels.txt
├── Shapley_SHAP/
│   ├── Shapley.ipynb
│   ├── SHAP.ipynb
│   └── mnist_cnn.pt
├── PDP_ALE/
│   ├── partial_dependence_plot.ipynb
│   └── accumulated_local_effects.ipynb
├── Counterfactuals/
│   ├── Counterfactuals_titanic.ipynb
│   ├── Counterfactuals_multiobj.ipynb
│   └── utils.py
├── Surrogate Models/
│   └── surrogate_modes.ipynb
├── LOFO_SAGE/
│   ├── LOFO.ipynb
│   └── SAGE.ipynb
├── CNN/
│   ├── cnn_interpretability.ipynb
│   └── cnn_attributions.ipynb
├── CAV/
│   └── TCAV-resnet.ipynb
└── Transformers/
    └── Transformers.ipynb
```

---

## Quick start

### 1) Clone and enter the project

```bash
git clone https://github.com/0xayman/AIMS_XAI_Course.git
cd AIMS_XAI_Course
```

### 2) Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Launch Jupyter

```bash
jupyter notebook
```

---

## Suggested notebook order

If you are new to XAI, a good sequence is:

1. `interpretations.ipynb`
2. `LIME/titanic_LIME.ipynb`
3. `Shapley_SHAP/Shapley.ipynb` then `Shapley_SHAP/SHAP.ipynb`
4. `PDP_ALE/partial_dependence_plot.ipynb` and `PDP_ALE/accumulated_local_effects.ipynb`
5. `Counterfactuals/Counterfactuals_titanic.ipynb`
6. `Surrogate Models/surrogate_modes.ipynb`
7. `LOFO_SAGE/LOFO.ipynb` and `LOFO_SAGE/SAGE.ipynb`
8. `CNN/cnn_interpretability.ipynb` and `CNN/cnn_attributions.ipynb`
9. `CAV/TCAV-resnet.ipynb`
10. `Transformers/Transformers.ipynb`

---

## Datasets and models used

The notebooks use common educational datasets and pre-trained model workflows, including Titanic, Diabetes, California Housing, MNIST, and ImageNet-backed examples.

Some notebooks may download assets on first run (model weights / dataset files), so internet access can be required.

---

## Tech stack

- **Core ML:** PyTorch, torchvision, scikit-learn, XGBoost
- **Explainability:** SHAP, LIME, SAGE, custom implementations
- **Data & plotting:** NumPy, pandas, matplotlib, seaborn, scikit-image
- **NLP / Transformers:** Hugging Face `transformers`

---

## Notes

- This repository is notebook-first and primarily focused on learning and experimentation.
- Runtime and memory requirements vary by notebook (especially image/transformer sections).
