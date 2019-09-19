import numpy as np
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Initialize variables
circuit = QuantumCircuit(2, 2)

# Add gates
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

# Visualize the Circuit
circuit.draw()
