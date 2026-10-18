"""
Hardware Transpilation & Execution on IBM Quantum 156-Qubit Heron Architecture.
"""
import os
import json
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qtn_disentangler import QTNBoundaryDisentangler

def run_hardware_benchmark(token, backend_name="ibm_fez", shots=1024):
    service = QiskitRuntimeService(channel="ibm_quantum_platform", token=token)
    backend = service.backend(backend_name)
    print(f"[*] Targeting IBM Quantum Processor: {backend.name} ({backend.num_qubits} Qubits)")

    # Prepare optimized circuit
    dis = QTNBoundaryDisentangler()
    qc_base = dis.create_entangled_state()
    _, qc_opt = dis.optimize(qc_base)
    qc_opt.measure_all()

    # Transpilation
    pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
    t_qc = pm.run(qc_opt)
    print(f"[+] Transpiled Depth: {t_qc.depth()}, Ops: {dict(t_qc.count_ops())}")

    # Physical Execution
    sampler = Sampler(mode=backend)
    job = sampler.run([t_qc], shots=shots)
    print(f"[+] Physical Job Dispatched! Job ID: {job.job_id()}")
    return job

if __name__ == "__main__":
    TOKEN = os.environ.get("IBM_QUANTUM_TOKEN")
    if not TOKEN:
        raise ValueError("Please set IBM_QUANTUM_TOKEN environment variable.")
    run_hardware_benchmark(TOKEN)
