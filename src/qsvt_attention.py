"""
QSVT Quantum Attention Block-Encoding & Polynomial Softmax Refinement.
"""
import numpy as np
import scipy.linalg as la
from scipy.optimize import minimize
from qiskit import QuantumCircuit

class QSVTAttentionEncoder:
    def __init__(self, dimension=16, alpha=1.5, num_restarts=300):
        self.d = dimension
        self.n_qubits = int(np.log2(dimension))
        self.alpha = alpha
        self.num_restarts = num_restarts
        self.best_coeffs = None

    def optimize_polynomial(self, raw_logits):
        p_exact = np.exp(raw_logits - np.max(raw_logits))
        p_exact = p_exact / np.sum(p_exact)
        norm_logits = raw_logits / (self.alpha * np.max(np.abs(raw_logits)))

        best_loss = float('inf')
        degree = 5
        for _ in range(self.num_restarts):
            init_c = np.random.randn(degree + 1) * 0.1
            init_c[0] = 0.5; init_c[1] = 0.5
            
            def loss_fn(c):
                approx = np.polynomial.chebyshev.chebval(norm_logits, c)
                p_approx = np.clip(approx, 1e-6, None)**2
                p_approx = p_approx / np.sum(p_approx)
                return 1.0 - np.sum(np.sqrt(p_exact * p_approx))**2
                
            res = minimize(loss_fn, init_c, method='Nelder-Mead', options={'maxiter': 100})
            if res.fun < best_loss:
                best_loss = res.fun
                self.best_coeffs = res.x
                
        approx_vals = np.polynomial.chebyshev.chebval(norm_logits, self.best_coeffs)
        p_qsvt = np.clip(approx_vals, 0, None)**2
        p_qsvt = p_qsvt / np.sum(p_qsvt)
        psi_qsvt = np.sqrt(p_qsvt) / np.linalg.norm(np.sqrt(p_qsvt))
        psi_exact = np.sqrt(p_exact) / np.linalg.norm(np.sqrt(p_exact))
        fidelity = float(np.abs(np.vdot(psi_exact, psi_qsvt))**2)
        return fidelity, psi_qsvt

    def build_circuit(self, psi_qsvt):
        qc = QuantumCircuit(self.n_qubits + 1, name="qsvt_attention_block_encoder")
        qc.initialize(psi_qsvt, range(self.n_qubits))
        qc.h(self.n_qubits)
        for q_idx in range(self.n_qubits):
            qc.cx(q_idx, self.n_qubits)
            qc.rz(float(self.best_coeffs[q_idx % len(self.best_coeffs)]), self.n_qubits)
            qc.cx(q_idx, self.n_qubits)
        return qc
