---
title: Quantum circuits and ansatz in neural networks
videoId: ABEkChn3inY
---

From: [[hu-po]] <br/> 

[[basics_of_quantum_computing_and_operators | Quantum computing]] describes quantum information typically represented by an N-qubit system within a Hilbert space. The dimensionality of this space grows exponentially as 2^N with the number of qubits <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>. Operations on these quantum states are mathematically described by applying a quantum circuit or a quantum gate <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>.

## Quantum Gates and Operators
A quantum gate is a unitary operator that transforms a quantum state <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>. Examples include:
*   **Hadamard (H) Gate:** This fundamental single-qubit gate is crucial for generating superposition states. Applying the Hadamard gate to a qubit in state 0 or 1 places it into an equal superposition of both, meaning it's neither strictly 0 nor 1 but a combination <a class="yt-timestamp" data-t="00:37:47">[00:37:47]</a>. Applying it twice returns the qubit to its original state, indicating it is its own inverse <a class="yt-timestamp" data-t="00:38:47">[00:38:47]</a>.
*   **Pauli Operators (X, Y, Z):** These are also unitary operators. For example, the Pauli X gate performs a rotation of Pi radians around the X-axis <a class="yt-timestamp" data-t="01:42:41">[01:42:41]</a>, while the Pauli Z gate flips a qubit's state from 0 to 1 and vice versa <a class="yt-timestamp" data-t="01:08:12">[01:08:12]</a>.
*   **Rotation Gates (Rx, Ry, Rz):** These allow for rotations around specific axes (X, Y, Z) by a parameterized angle (Theta), offering more fine-grained control than a simple flip <a class="yt-timestamp" data-t="01:42:41">[01:42:41]</a>.
*   **Controlled-NOT (CNOT) Gate:** This is a two-qubit gate where one qubit acts as a control and the other as a target. If the control qubit is in state 1, the target qubit is flipped; otherwise, it remains unchanged <a class="yt-timestamp" data-t="01:27:40">[01:27:40]</a>. CNOT gates are instrumental in creating and manipulating entanglement between qubits <a class="yt-timestamp" data-t="01:29:11">[01:29:11]</a>.

## Ansatz in Quantum Neural Networks
In [[basics_of_quantum_computing_and_operators | quantum computing]], an "ansatz" (German for "initial condition" or "assumption") refers to a quantum circuit with a predetermined geometry (connectivity and gates) that expresses a time-evolution unitary operator <a class="yt-timestamp" data-t="00:50:31">[00:50:31]</a>. They are essentially parameterized quantum circuits (PQCs) <a class="yt-timestamp" data-t="01:36:44">[01:36:44]</a>.

### Role in Quantum Neural Networks
In [[quantum_selfattention_neural_networks | quantum self-attention neural networks]] (QSAN), an ansatz serves multiple purposes:
*   **Data Encoding:** A "U_encode" ansatz converts classical input data (e.g., text tokens) into corresponding quantum states by applying a Hadamard gate to put qubits in superposition, followed by a unitary operation based on the input data <a class="yt-timestamp" data-t="00:59:10">[00:59:10]</a>.
*   **Queries, Keys, and Values:** Separate ansatze (Uq, Uk, Uv) are used to represent the queries, keys, and values, each parameterized by learnable angles (Theta_q, Theta_k, Theta_v) <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>. These are not represented as traditional matrices but as quantum circuits <a class="yt-timestamp" data-t="01:01:14">[01:01:14]</a>.
*   **Expressive Power:** Repeated application of circuit structures (e.g., rotations and CNOT gates) within an ansatz enhances its expressive power, allowing the quantum system to explore a diverse set of states, beneficial for optimization tasks <a class="yt-timestamp" data-t="01:25:57">[01:25:57]</a>.

### Structure of an Ansatz
A typical ansatz consists of single-qubit rotations (like Rx, Ry) and CNOT entangling gates. These gates are applied to pairs of qubits to create entanglement <a class="yt-timestamp" data-t="01:29:06">[01:29:06]</a>. The repetition of these steps builds the depth of the quantum circuit <a class="yt-timestamp" data-t="01:31:30">[01:31:30]</a>.

### Initialization and Training
Ansatz parameters (the rotation angles) are typically initialized from a Gaussian distribution with a mean of zero and a small standard deviation (e.g., 0.01) <a class="yt-timestamp" data-t="02:11:16">[02:11:16]</a>. This means initial rotations are very small <a class="yt-timestamp" data-t="02:12:24">[02:12:24]</a>. The optimization of these parameters is achieved through stochastic gradient descent, leveraging analytical gradients, which means that backpropagation is possible through these quantum circuits <a class="yt-timestamp" data-t="02:03:31">[02:03:31]</a>.

## Practical Considerations and Analogies to Classical Neural Networks
*   **Hybrid Approach:** [[quantum_selfattention_neural_networks | Quantum self-attention neural networks]] often employ a hybrid approach, where quantum circuits process initial data, and classical computers handle tasks like calculating attention coefficients and final predictions <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>.
*   **[[highdimensional_spaces_and_information_storage_in_neural_nets | High-Dimensional Feature Spaces]]:** Quantum computers leverage exponentially large Hilbert spaces to create [[highdimensional_spaces_and_information_storage_in_neural_nets | high-dimensional feature spaces]] for word correlations, potentially uncovering hidden relationships that are difficult to find classically <a class="yt-timestamp" data-t="02:20:09">[02:20:09]</a>.
*   **Depth and Parameters:** Currently, quantum neural networks are "shallow," meaning they cannot have too many consecutive operations due to noise propagation <a class="yt-timestamp" data-t="01:22:22">[01:22:22]</a>. For instance, a [[quantum_selfattention_neural_networks | QSAN]] model might have only a few dozen parameters, orders of magnitude less than classical deep learning models <a class="yt-timestamp" data-t="02:13:52">[02:13:52]</a>.
*   **[[challenges_of_quantum_machine_learning | Noise Robustness]]:** A critical design consideration for [[quantum_selfattention_neural_networks | quantum machine learning]] algorithms on [[simulated_versus_real_quantum_computing | near-term quantum devices]] is robustness to noise, as external disturbances can propagate and lead to incorrect answers <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Simulations vs. Real Hardware:** Most [[quantum_selfattention_neural_networks | quantum machine learning]] research and algorithm testing are done via classical simulations rather than on actual quantum hardware due to the high cost and limited accessibility of real quantum computers <a class="yt-timestamp" data-t="01:58:37">[01:58:37]</a>.