
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
   

## Usage:
To run the quantum harmonic oscillator simulation, execute the following Python script:

python quantum_harmonic_oscillator.py


The simulation will run for the specified number of steps and qubits, and it will display a histogram of the measurement outcomes.


## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

