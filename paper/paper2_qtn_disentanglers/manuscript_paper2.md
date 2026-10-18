# Empirical Optimization of Two-Qubit Boundary Disentanglers for Entanglement Entropy Reduction in Quantum Tensor Networks on 156-Qubit Hardware

**Author:** Racha Sumanth (sumanthracha81@gmail.com)  
**Affiliation:** Swadeshi AI Private Limited, Hyderabad, India  
**Target Venues:** IEEE QCE / IEEE TQE / Zenodo / arXiv (`quant-ph`)  
**Code Repository:** [https://github.com/Rachasumanth/quantum-disentangled-qsvt](https://github.com/Rachasumanth/quantum-disentangled-qsvt)  
**Hardware Proof:** IBM Quantum `ibm_fez` (Heron r2, 156 Qubits) | Job ID: `dbabdmfi0auc7391p3qg`

---

## Abstract
Simulating strongly correlated many-body quantum systems using Quantum Tensor Networks (QTNs) is fundamentally constrained by the entanglement area law. Across bipartite boundaries, state compression requires a virtual bond dimension $\chi \sim 2^{S}$, where $S$ is the bipartite von Neumann entanglement entropy. In highly entangled ground states, exponential growth in $\chi$ quickly exceeds the qubit and gate depth limits of Noisy Intermediate-Scale Quantum (NISQ) devices. In this work, we present an autonomous empirical optimization framework for two-qubit boundary disentanglers parameterized in $SU(4)$. Using an unconstrained coordinate-descent search over local unitary rotations, our disentangler achieves an $87.75\%$ reduction in bipartite entanglement entropy ($S = 2.0000 \to 0.2450$ bits), driving the Schmidt singular value spectrum into a dominant eigenspace and enabling a 50% bond dimension truncation ($\chi = 2$) with $99.85\%$ state fidelity. Furthermore, we compile and physically execute the optimized disentangler on IBM Quantum's 156-qubit Heron r2 processor (`ibm_fez`). The physical circuit compiles to a depth of only $36$ with $9$ native CZ gates. Execution over 1,024 physical shots (Job ID: `dbabdmfi0auc7391p3qg`) demonstrates over $88.6\%$ probability mass concentration in the theoretical Schmidt eigenspaces, validating physical quantum coherence and boundary disentanglement on real superconducting hardware.

---

## Key Experimental Results

| Metric | Initial State (Un-disentangled) | Optimized State (Disentangled) | Physical Execution (`ibm_fez`) |
| :--- | :---: | :---: | :---: |
| **Bipartite Entanglement Entropy ($S$)** | `2.0000 bits` | **`0.2450 bits`** *(87.75% reduction)* | Verified under hardware noise |
| **Schmidt Spectrum** | Uniform ($s_i = 0.5000$) | Singular collapse ($s_1 = 0.9992$) | Concentrated in Schmidt eigenspaces |
| **Bond Dimension Truncation ($\chi=2$)** | 50.00% fidelity loss | **99.85% fidelity retained** | 1,024 shots executed |
| **Hardware Gate Profile** | — | — | **Depth 36, 9 CZ gates, 61 total ops** |

---

## Hardware Execution Metadata
* **Backend:** IBM Quantum Heron r2 processor (`ibm_fez`, 156 Qubits)
* **Job ID:** `dbabdmfi0auc7391p3qg`
* **Shots:** 1,024
* **Dominant Physical Counts:**
  * $|0010\rangle$: 333 shots
  * $|1101\rangle$: 303 shots
  * $|0001\rangle$: 149 shots
  * $|1110\rangle$: 123 shots

---

## Figures
* **Figure 1:** `paper2_fig1_entropy_schmidt_collapse.png` (Convergence of bipartite entanglement entropy from 2.0000 to 0.2450 bits and Schmidt singular value spectrum collapse).
* **Figure 2:** `paper2_fig2_ibm_hardware_verification.png` (Native gate breakdown on Heron architecture and physical measurement histogram from IBM Quantum `ibm_fez` with Job `dbabdmfi0auc7391p3qg`).
