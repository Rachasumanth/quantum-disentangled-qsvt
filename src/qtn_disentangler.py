"""
Two-Qubit Disentangler Optimization for Multi-Scale Quantum Tensor Networks.
"""
import numpy as np
import scipy.linalg as la
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace, entropy

class QTNBoundaryDisentangler:
    def __init__(self, step_scale=0.10, num_steps=60):
        self.step_scale = step_scale
        self.num_steps = num_steps
        self.thetas = np.random.randn(8) * 0.1

    @staticmethod
    def create_entangled_state():
        qc = QuantumCircuit(4)
        qc.h(0); qc.h(1)
        qc.cx(0, 2); qc.cx(1, 2); qc.cx(1, 3)
        qc.ry(1.2, 2); qc.cx(2, 3)
        return qc

    @staticmethod
    def parameterized_su4(thetas):
        qc = QuantumCircuit(4)
        qc.ry(thetas[0], 1); qc.rz(thetas[1], 1)
        qc.ry(thetas[2], 2); qc.rz(thetas[3], 2)
        qc.cx(1, 2)
        qc.ry(thetas[4], 1); qc.rz(thetas[5], 2)
        qc.cx(1, 2)
        qc.ry(thetas[6], 1); qc.ry(thetas[7], 2)
        return qc

    def optimize(self, qc_base):
        thetas = self.thetas.copy()
        for _ in range(self.num_steps):
            for i in range(8):
                tp = thetas.copy(); tp[i] += self.step_scale
                sp = float(entropy(partial_trace(Statevector.from_instruction(qc_base.compose(self.parameterized_su4(tp))), [2, 3]), base=2))
                
                tm = thetas.copy(); tm[i] -= self.step_scale
                sm = float(entropy(partial_trace(Statevector.from_instruction(qc_base.compose(self.parameterized_su4(tm))), [2, 3]), base=2))
                
                thetas[i] = tp[i] if sp < sm else tm[i]
                
        self.thetas = thetas
        qc_opt = qc_base.compose(self.parameterized_su4(thetas))
        sv_opt = Statevector.from_instruction(qc_opt)
        s_final = float(entropy(partial_trace(sv_opt, [2, 3]), base=2))
        return s_final, qc_opt
