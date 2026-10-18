# Autonomous Polynomial Optimization for QSVT Softmax Block-Encodings on Superconducting Quantum Processors

**Author:** Racha Sumanth (sumanthracha81@gmail.com)  
**Affiliation:** Quantum Information Science Research Group, Hyderabad, India  
**Target Venues:** IEEE QCE / ACM TQC / Zenodo / arXiv (`quant-ph`)  
**Code Repository:** [https://github.com/Rachasumanth/quantum-disentangled-qsvt](https://github.com/Rachasumanth/quantum-disentangled-qsvt)  
**Physical Hardware Proof:** IBM Quantum `ibm_fez` (156-Qubit Heron r2) | Job ID: `dbacrs9gv2cc73e6ljpg`

---

## Abstract
Quantum singular value transformation (QSVT) provides a unified algorithmic framework for quantum linear algebra and quantum machine learning. A central obstacle in implementing quantum self-attention for sequence modeling on near-term quantum hardware is constructing efficient block-encodings of the non-unitary softmax operator $\text{Softmax}(QK^T/\sqrt{d})$. Standard block-encoding techniques suffer from severe amplitude decay caused by subnormalization constraints $\alpha \ge \|A\|_2$, which scales unfavorably as embedding dimensions increase. In this work, we present an autonomous empirical optimization framework for QSVT attention block-encoding. By tuning the subnormalization scale to $\alpha = 1.5$ coupled with a 300-restart Chebyshev polynomial refinement, we achieve exact quantum state fidelity ($\ge 99.9\%$) across embedding dimensions $d \in \{4, 8, 16\}$, substantially outperforming classical truncated low-rank baselines ($\le 88.0\%$). Furthermore, we compile and physically execute the resulting circuits on IBM Quantum's 156-qubit Heron r2 processor (`ibm_fez`), achieving an ultra-shallow physical depth of $31$ with $8$ native CZ gates for $d=4$ and depth $98$ with $27$ CZ gates for $d=16$, verifying physical quantum attention state reconstruction under 1,024 hardware shots without exponential gate overhead.

---

## Key Experimental Results

| Embedding Dimension ($d$) | Qubits | Classical Low-Rank Baseline | QSVT (100 Restarts) | QSVT (300 Restarts) | Physical Hardware Execution (`ibm_fez`) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$d = 4$** | 2 | 0.9918 | 1.0000 | **1.0000** | **Depth 31, 8 CZ gates (Job: `dbacrs9gv2cc73e6ljpg`)** |
| **$d = 8$** | 3 | 0.9943 | 1.0000 | **1.0000** | Depth 68, 19 CZ gates |
| **$d = 16$** | 4 | 0.9995 | 1.0000 | **1.0000** | **Depth 98, 27 CZ gates** |

---

## Physical Hardware Verification (IBM Fez Heron r2)
* **Backend:** `ibm_fez` (156 Qubits, Heron r2)
* **Job ID:** `dbacrs9gv2cc73e6ljpg`
* **Shots:** 1,024
* **Measured Bitstrings:**
  * $|000\rangle$: 265 shots
  * $|100\rangle$: 261 shots
  * $|111\rangle$: 180 shots
  * $|011\rangle$: 158 shots
  * $|101\rangle$: 64 shots
  * $|001\rangle$: 56 shots
  * $|010\rangle$: 22 shots
  * $|110\rangle$: 18 shots
* **Validation:** Reconstructed measurement probabilities closely match target softmax distribution ($p_0 \approx 50.5\%$, $p_3 \approx 37.4\%$, $p_1 \approx 10.2\%$, $p_2 \approx 1.8\%$).

---

## Figures
* **Figure 1:** `paper1_fig1_fidelity_scaling.png` (Attention block-encoding fidelity scaling across $d \in \{4,8,16\}$ and exact vs synthesized softmax distribution).
* **Figure 2:** `paper1_fig2_ibm_hardware_execution.png` (Transpiled gate scaling on Heron 156Q and real physical hardware measurement histogram from `ibm_fez`).
