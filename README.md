
# Quantum Harmonic Oscillator Simulator

This repository contains a quantum simulation of a quantum harmonic oscillator implemented using **Qiskit** and the **AerSimulator** backend. The simulator models the dynamics of a quantum system, simulating the time evolution of a harmonic oscillator with multiple qubits. The project includes a quantum circuit that applies rotations and entanglement operations to simulate the oscillator's behavior over multiple steps.

## Features:
- **Quantum Circuit**: A custom quantum circuit that simulates a harmonic oscillator using rotations (Rx gates) and entanglement (CX gates).
- **AerSimulator**: The simulation is run on the **AerSimulator** backend of Qiskit, providing accurate and efficient quantum state evolution.
- **Visualization**: The simulation results are visualized in a histogram format, showing the measurement outcomes of the quantum system.
- **Flexible Parameters**: Users can specify the number of qubits, simulation steps, and rotation angle to explore various quantum system configurations.

## Installation:
1. Clone the repository:
   
   git clone https://github.com/Chitravansh/Quantum_Harmonic_Oscillator.git
   cd quantum-harmonic-oscillator-simulator
  

2. Set up a Python environment (optional but recommended):
  
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  

3. Install dependencies:
   
   pip install -r requirements.txt


4. Ensure that Qiskit and the AerSimulator backend are installed:
   
   pip install qiskit
   
5. Ensure qiskit environment is activated :
    
    conda activate qiskit-env
**
Some important tip to run this simulator : **
Steps to Install and Use qiskit-aer

    Ensure Proper Environment
    Verify you are using the right environment for Qiskit. If you installed Qiskit in a new environment (e.g., qiskit-env), activate it first:

conda activate qiskit-env

Install qiskit-aer Separately
Install the Aer package explicitly:

pip install qiskit-aer

Verify Installation
Test if qiskit-aer is correctly installed:

from qiskit.providers.aer import AerSimulator
print("AerSimulator is working!")

Run Quantum Circuit with AerSimulator
Here's a complete example using the AerSimulator:

from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
from qiskit import execute

# Create a simple quantum circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Use AerSimulator
simulator = AerSimulator()
job = execute(qc, simulator, shots=1024)
result = job.result()
   

## Usage:
To run the quantum harmonic oscillator simulation, execute the following Python script:

python quantum_harmonic_oscillator.py


The simulation will run for the specified number of steps and qubits, and it will display a histogram of the measurement outcomes.


## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

