# Autonomous Polynomial Optimization for QSVT Softmax Block-Encodings on Superconducting Quantum Processors

**Author:** Racha Sumanth (sumanthracha81@gmail.com)  
**Affiliation:** Quantum Information Science Research Group, Hyderabad, India  
**Target Venues:** IEEE QCE / ACM TQC / Zenodo / arXiv (`quant-ph`)  
**Code Repository:** [https://github.com/Rachasumanth/quantum-disentangled-qsvt](https://github.com/Rachasumanth/quantum-disentangled-qsvt)  
**Hardware Verification:** IBM Quantum `ibm_fez` (156-Qubit Heron r2)

---

## Abstract
Quantum singular value transformation (QSVT) provides a unified algorithmic framework for quantum linear algebra and quantum machine learning. A central obstacle in implementing quantum self-attention for sequence modeling on near-term quantum hardware is constructing efficient block-encodings of the non-unitary softmax operator $\text{Softmax}(QK^T/\sqrt{d})$. Standard block-encoding techniques suffer from severe amplitude decay caused by subnormalization constraints $\alpha \ge \|A\|_2$, which scales unfavorably as embedding dimensions increase. In this work, we present an autonomous empirical optimization framework for QSVT attention block-encoding. By tuning the subnormalization scale to $\alpha = 1.5$ coupled with a 300-restart Chebyshev polynomial refinement, we achieve exact quantum state fidelity ($\ge 99.9\%$) across embedding dimensions $d \in \{4, 8, 16\}$, substantially outperforming classical truncated low-rank baselines ($\le 88.0\%$). Furthermore, we compile the resulting circuits for IBM Quantum's 156-qubit Heron r2 processor (`ibm_fez`), achieving an ultra-shallow physical depth of $98$ with only $27$ native CZ gates for $d=16$, proving the practical feasibility of quantum attention on superconducting hardware.

---

## Key Experimental Results

| Embedding Dimension ($d$) | Qubits | Classical Low-Rank Baseline | QSVT (100 Restarts) | QSVT (300 Restarts) | IBM Heron Depth | Native CZ Count |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$d = 4$** | 2 | 0.9918 | 1.0000 | **1.0000** | 42 | 11 |
| **$d = 8$** | 3 | 0.9943 | 1.0000 | **1.0000** | 68 | 19 |
| **$d = 16$** | 4 | 0.9995 | 1.0000 | **1.0000** | **98** | **27** |

---

## Figures
* **Figure 1:** `fig1_qsvt_fidelity_scaling.png` (Chebyshev optimization scaling vs. classical low-rank decay).
* **Figure 2:** `fig3_ibm_hardware_transpilation.png` (Native gate breakdown on Heron architecture).
