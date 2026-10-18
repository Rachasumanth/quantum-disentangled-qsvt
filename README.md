# Quantum Computing Research Publications: QSVT Attention & QTN Disentanglers

[![Qiskit](https://img.shields.io/badge/Qiskit-2.5.2-6929C4.svg)](https://qiskit.org/)
[![IBM Quantum](https://img.shields.io/badge/IBM_Quantum-Heron_156Q-0062FF.svg)](https://quantum.ibm.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Preprint](https://img.shields.io/badge/Preprints-Open_Access-B31B1B.svg)](https://github.com/Rachasumanth/quantum-disentangled-qsvt)

This repository contains two independent research papers, complete mathematical simulations, academic figures, and physical hardware artifacts executed on IBM Quantum's 156-qubit Heron r2 superconducting hardware (`ibm_fez`):

* **Author:** Racha Sumanth ([sumanthracha81@gmail.com](mailto:sumanthracha81@gmail.com))
* **Hardware Artifact:** IBM Quantum `ibm_fez` (Heron r2, 156 Qubits) | Job ID: `dbabdmfi0auc7391p3qg`

---

## 📄 The Two Research Papers

### 📑 Paper 1: QSVT Quantum Attention Block-Encoding
> **"Autonomous Polynomial Optimization for QSVT Softmax Block-Encodings on Superconducting Quantum Processors"**
> * **LaTeX Source:** [`paper/paper1_qsvt_attention/manuscript_paper1.tex`](paper/paper1_qsvt_attention/manuscript_paper1.tex)
> * **Markdown Paper:** [`paper/paper1_qsvt_attention/manuscript_paper1.md`](paper/paper1_qsvt_attention/manuscript_paper1.md)
> * **Key Contribution:** Resolves subnormalization amplitude collapse ($\alpha = 1.5$) via 300-restart Chebyshev polynomial synthesis, achieving $\ge 99.9\%$ fidelity across embedding dimensions $d \in \{4, 8, 16\}$ with circuit depth 98 (27 CZ gates) on IBM Heron.

### 📑 Paper 2: Multi-Scale QTN Boundary Disentanglers
> **"Empirical Optimization of Two-Qubit Boundary Disentanglers for Entanglement Entropy Reduction in Quantum Tensor Networks on 156-Qubit Hardware"**
> * **LaTeX Source:** [`paper/paper2_qtn_disentanglers/manuscript_paper2.tex`](paper/paper2_qtn_disentanglers/manuscript_paper2.tex)
> * **Markdown Paper:** [`paper/paper2_qtn_disentanglers/manuscript_paper2.md`](paper/paper2_qtn_disentanglers/manuscript_paper2.md)
> * **Key Contribution:** Unconstrained coordinate-descent parameterization of $SU(4)$ disentanglers reducing bipartite entanglement entropy by $87.75\%$ ($2.0000 \to 0.2450$ bits), achieving $99.85\%$ fidelity under $\chi=2$ bond dimension truncation. Physically verified on IBM Quantum `ibm_fez` (Job `dbabdmfi0auc7391p3qg`, 1,024 shots).

*(Note: A unified combined manuscript is also preserved in [`paper/manuscript.tex`](paper/manuscript.tex)).*

---

## 📌 Key Empirical Findings

| Metric | Classical / Un-disentangled Baseline | Optimized Quantum Result | Physical Hardware Result (`ibm_fez`) |
| :--- | :---: | :---: | :---: |
| **QSVT Attention Fidelity ($d=16$)** | `0.8800 – 0.9940` *(low-rank decay)* | **`1.0000`** *(300-restart Chebyshev)* | **Depth 98** *(27 CZ gates)* |
| **QTN Bipartite Entanglement Entropy** | `2.0000 bits` | **`0.2450 bits`** *(87.75% reduction)* | **Depth 36** *(9 CZ gates)* |
| **Bond Dimension ($\chi=2$) Fidelity** | `0.5000` *(50% loss)* | **`0.9985`** | **1,024 Physical Shots Verified** |

---

## 📊 Scientific Figures

* **Figure 1: QSVT Quantum Attention Fidelity Scaling**  
  ![Figure 1: QSVT Attention Fidelity Scaling](figures/fig1_qsvt_fidelity_scaling.png)

* **Figure 2: QTN Boundary Disentangler Optimization**  
  ![Figure 2: QTN Entanglement Recovery](figures/fig2_qtn_entropy_recovery.png)

* **Figure 3: Physical Gate Footprint on 156-Qubit IBM Heron**  
  ![Figure 3: Hardware Gate Breakdown](figures/fig3_ibm_hardware_transpilation.png)

---

## 🔬 Hardware Verification Artifact

The compiled circuits were physically dispatched to **IBM Quantum's 156-qubit Heron processor (`ibm_fez`)**:
* **Job ID:** `dbabdmfi0auc7391p3qg`
* **Status:** `COMPLETED`
* **Shots:** 1,024
* **Dominant Physical Measurement Counts:**
  * $|0010\rangle$: `333`
  * $|1101\rangle$: `303`
  * $|0001\rangle$: `149`
  * $|1110\rangle$: `123`
  *(Over 88.6% of physical probability mass concentrated in the theoretical Schmidt eigenspaces, validating physical coherence).*

Raw metadata is available in [`data/ibm_fez_job_results.json`](data/ibm_fez_job_results.json).

---

## 🚀 Quickstart & Reproduction

### 1. Installation
```bash
git clone https://github.com/Rachasumanth/quantum-disentangled-qsvt.git
cd quantum-disentangled-qsvt
pip install -r requirements.txt
```

### 2. Run QSVT Attention Optimization (Paper 1)
```bash
python3 -c "
from src.qsvt_attention import QSVTAttentionEncoder
import numpy as np
encoder = QSVTAttentionEncoder(dimension=16, alpha=1.5, num_restarts=100)
logits = np.random.randn(16) * 2.0
fid, _ = encoder.optimize_polynomial(logits)
print(f'Fidelity achieved: {fid:.4f}')
"
```

### 3. Run QTN Disentangler (Paper 2)
```bash
python3 -c "
from src.qtn_disentangler import QTNBoundaryDisentangler
dis = QTNBoundaryDisentangler()
qc = dis.create_entangled_state()
entropy_final, _ = dis.optimize(qc)
print(f'Final Entanglement Entropy: {entropy_final:.4f} bits (Baseline 2.0000)')
"
```

---

## 📚 Citations

```bibtex
@article{sumanth2026qsvt,
  title={Autonomous Polynomial Optimization for QSVT Softmax Block-Encodings on Superconducting Quantum Processors},
  author={Sumanth, Racha},
  journal={Preprint},
  year={2026}
}

@article{sumanth2026qtn,
  title={Empirical Optimization of Two-Qubit Boundary Disentanglers for Entanglement Entropy Reduction in Quantum Tensor Networks on 156-Qubit Hardware},
  author={Sumanth, Racha},
  journal={Preprint},
  year={2026}
}
```

---

## License
MIT License. See [LICENSE](LICENSE) for details.
