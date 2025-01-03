from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit , transpile
import numpy as np
import matplotlib.pyplot as plt


# Parameters
n_qubits = 3  # Number of qubits for representing the system
n_steps = 10  # Number of simulation steps
theta = np.pi / 4  # Rotation angle for simulation

def create_harmonic_oscillator_circuit(n_qubits, n_steps, theta):
    """
    Create a quantum circuit simulating a quantum harmonic oscillator.
    :param n_qubits: Number of qubits
    :param n_steps: Number of steps in the simulation
    :param theta: Rotation angle
    :return: QuantumCircuit
    """
    qc = QuantumCircuit(n_qubits)
    
    # Initialize all qubits to superposition
    qc.h(range(n_qubits))

    for _ in range(n_steps):
        # Apply rotations (analogous to time evolution)
        for i in range(n_qubits):
            qc.rx(theta, i)

        # Apply entanglement between qubits
        for i in range(n_qubits - 1):
            qc.cx(i, i + 1)

    qc.measure_all()  # Measure all qubits at the end
    return qc

# Build the circuit
qc = create_harmonic_oscillator_circuit(n_qubits, n_steps, theta)


simulator = AerSimulator()

# Transpile the circuit for the simulator
transpiled_circuit = transpile(qc, backend=simulator)

# Run the transpiled circuit on the simulator
result = simulator.run(transpiled_circuit).result()

# Get the counts (measurement outcomes)
counts = result.get_counts()
# Visualize the results
plot_histogram(counts)
plt.title("Quantum Harmonic Oscillator Simulation")
plt.show()
