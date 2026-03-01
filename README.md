# Explainable AI (XAI) — AIMS Course Practicals

**African Institute for Mathematical Sciences (AIMS)**
Course taught by [Inga Strümke](https://www.ntnu.edu/employees/inga.strumke) — NTNU & Norwegian OpenAI Lab

---

## Overview

This repository contains my practical notebooks from the XAI course at AIMS. The course provided a rigorous, hands-on introduction to the theory and practice of Explainable AI — spanning classical interpretable models, post-hoc explanation methods, and cutting-edge interpretability for deep learning architectures (CNNs and Transformers).

The notebooks progress from foundational concepts (linear model coefficients, decision trees) through to modern techniques like Concept Activation Vectors and Transformer attention analysis.

---

## Skills & Techniques Covered

| Technique | Scope | Model Type | Key Concept |
|---|---|---|---|
| Coefficients & Effect Plots | Global | Linear Models | Direct interpretation, collinearity |
| Decision Tree Interpretation | Global | Decision Trees | Inherently interpretable models |
| LIME | Local | Model-agnostic | Local linear approximation |
| Shapley Values (from scratch) | Global | Model-agnostic | Cooperative game theory |
| SHAP | Local / Global | Tree + Deep | Efficient Shapley estimation |
| Partial Dependence Plots (PDP) | Global | Model-agnostic | Marginal feature effects |
| Accumulated Local Effects (ALE) | Global | Model-agnostic | Correlation-robust effects |
| Counterfactual Explanations | Local | Model-agnostic | Minimal-change recourse |
| Surrogate Models | Global | Model-agnostic | Interpretable approximations |
| LOFO / SAGE | Global | Model-agnostic | Leave-one-feature-out importance |
| CNN Filter & Activation Visualization | Local | CNNs | Feature map analysis |
| Activation Maximization | Local | CNNs | Learned concept visualization |
| CAV / TCAV | Concept-based | CNNs & ViTs | Human-defined concept probing |
| Grad-SAM | Local | Transformers | Attention × gradient attribution |
| Attention Visualization | Local | Transformers | Multi-head attention analysis |
| SHAP for Text | Local | NLP (BERT) | Token-level importance |

---

## Repository Structure

```
AIMS_XAI_Course/
│
├── interpretations.ipynb        # Foundations: linear models, decision trees, feature importance
│
├── LIME/
│   ├── titanic_LIME.ipynb       # Tabular LIME on Titanic survival (XGBoost)
│   └── image_LIME.ipynb         # Image LIME on ImageNet with ResNet18
│
├── Shapley_SHAP/
│   ├── Shapley.ipynb            # Shapley values from scratch (game theory + ML)
│   └── SHAP.ipynb               # SHAP for tabular (diabetes) and image (MNIST) data
│
├── PDP_ALE/
│   ├── partial_dependence_plot.ipynb   # PDP on loan approval dataset (PyTorch NN)
│   └── accumulated_local_effects.ipynb # ALE vs PDP on California housing
│
├── Counterfactuals/
│   ├── Counterfactuals_titanic.ipynb   # Single-objective counterfactuals
│   └── Counterfactuals_multiobj.ipynb  # Multi-objective counterfactual search
│
├── Surrogate Models/
│   └── surrogate_modes.ipynb    # Global and local surrogate models
│
├── LOFO_SAGE/
│   ├── LOFO.ipynb               # Leave-One-Feature-Out on bike sharing (XGBoost)
│   └── SAGE.ipynb               # SAGE stochastic Shapley-based importance
│
├── CNN/
│   ├── cnn_interpretability.ipynb  # Filter viz, feature maps, activation maximization
│   └── cnn_attributions.ipynb      # Gradient-based saliency & attribution maps
│
├── CAV/
│   └── TCAV-resnet.ipynb        # TCAV: "striped" concept on zebra classification
│
└── Transformers/
    └── Transformers.ipynb       # Grad-SAM, SHAP, attention viz for BERT & ViT
```

---

## Highlights

### Shapley Values — Built from First Principles
Derived Shapley values from cooperative game theory (cab-sharing, cat-mice examples), then applied them to ML feature attribution using both R² and distance correlation as characteristic functions. This grounded the widely-used SHAP library in its mathematical foundations.

### TCAV — Concept-Based Interpretability
Implemented Testing with Concept Activation Vectors (Kim et al., 2018) on ResNet18 and Vision Transformer (ViT-base). Trained linear probes on internal layer activations to detect human-defined concepts (e.g., "striped" textures), then computed TCAV scores via directional derivatives — achieving 100% TCAV score confirming the zebra-striped relationship.

### Counterfactual Search with Loss Optimization
Implemented counterfactual explanation search using a composite loss:
`λ · (prediction − target)² + L1_distance`, with random search and λ-tuning to balance prediction change against feature perturbation cost.

### Transformers Interpretability
Applied multiple complementary explanation methods to BERT (sentiment classification) and ViT:
- **Grad-SAM**: attention × gradient products to identify important tokens
- **SHAP**: token-level importance with fixed-context masking
- **Attention visualization**: per-head, per-layer attention pattern analysis

---

## Datasets Used

| Dataset | Task | Size |
|---|---|---|
| Titanic | Binary classification | 891 samples |
| Bike Sharing Demand | Regression | 17K samples |
| Diabetes (sklearn) | Regression | 442 samples |
| Diabetes Prediction | Classification | 80K samples |
| Loan Approval | Binary classification | 505 samples |
| California Housing | Regression | 20K samples |
| MNIST | Image classification | 70K images |
| ImageNet (via ResNet18) | Image classification | Pre-trained |

---

## Tech Stack

**Deep Learning:** PyTorch, torchvision, torch-lucent, HuggingFace Transformers
**Explainability:** SHAP, LIME, custom implementations
**Classical ML:** scikit-learn, XGBoost, optuna
**Data & Viz:** NumPy, pandas, matplotlib, seaborn, scikit-image
**Statistics:** scipy, dcor (distance correlation)

---

## About the Course

The XAI course at AIMS was taught by **Inga Strümke**, a researcher at NTNU and the Norwegian OpenAI Lab, whose work focuses on the foundations and applications of explainable and trustworthy AI. The course combined mathematical rigor — grounding methods in statistics, game theory, and optimization — with practical implementation across diverse ML paradigms.

---

## Getting Started

```bash
# Clone the repository
git clone <repo-url>
cd AIMS_XAI_Course

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```
