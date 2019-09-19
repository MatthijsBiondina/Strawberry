import numpy as np
from qiskit import QuantumCircuit, execute, Aer


from src.utils.tools import *

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Initialize variables
circuit = QuantumCircuit(2, 2)

# Add gates
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

# Visualize the Circuit
qdraw(circuit)

# Simulate the Experiment
job = execute(circuit, simulator, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)

qhist(counts)
