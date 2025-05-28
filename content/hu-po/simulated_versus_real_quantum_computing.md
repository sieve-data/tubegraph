---
title: Simulated versus real quantum computing
videoId: ABEkChn3inY
---

From: [[hu-po]] <br/> 

The field of [[quantum_computing_advancements | quantum computing advancements]] is rapidly progressing, involving both theoretical models and practical hardware implementations. A key distinction in current research and development lies between real, physical quantum computers and their simulated counterparts.

## Noisy Intermediate-Scale Quantum (NISQ) Devices

Current physical quantum computers are categorized as Noisy Intermediate-Scale Quantum (NISQ) devices <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. These devices are characterized by having up to a few hundred physical qubits <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### Characteristics of NISQ Devices
*   **Qubit Count**: Typically range from tens to a few hundreds of qubits <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>. Examples include Google's Sycamore chip with 53 qubits <a class="yt-timestamp" data-t="01:56:18">[01:56:18]</a>, or devices with up to 100 qubits <a class="yt-timestamp" data-t="01:56:40">[01:56:40]</a>.
*   **Noise**: They are affected by various types of noise, both coherent and incoherent, originating from the external environment <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>, <a class="yt-timestamp" data-t="01:10:09">[01:10:09]</a>. This noise makes the practical implementation of many advanced [[basics_of_quantum_computing_and_operators | quantum algorithms]] less feasible <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Quantum computers are kept in highly sensitive, super-cooled, and vibration-proof rooms to minimize external interference <a class="yt-timestamp" data-t="01:11:10">[01:11:10]</a>.
*   **Error Correction**: NISQ devices do not yet employ full quantum error correction <a class="yt-timestamp" data-t="01:10:40">[01:10:40]</a>.
*   **Shallow Algorithms**: Due to noise propagation, [[basics_of_quantum_computing_and_operators | quantum algorithms]] running on NISQ devices need to be "shallow," meaning they cannot have too many consecutive operations <a class="yt-timestamp" data-t="01:12:22">[01:12:22]</a>.
*   **Quantum Advantage**: Devices with 50 to 100 qubits have demonstrated "quantum supremacy" or "quantum advantage" on certain carefully designed tasks against the most powerful classical computers <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>, <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This refers to specific problems where a quantum computer can solve them better or faster than traditional computers <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## Quantum Machine Learning in the NISQ Era
The study of [[challenges_of_quantum_machine_learning | quantum machine learning]] (QML) in the NISQ era is still in its infancy <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. Developing [[quantum_circuits_and_anzats_in_neural_networks | QML algorithms]] that exploit the power of these devices is desirable <a class="yt-timestamp" data-t="01:15:04">[01:15:04]</a>.

## Simulation of Quantum Systems
The overwhelming majority of [[quantum_computing_advancements | quantum computing research]] and [[basics_of_quantum_computing_and_operators | quantum algorithms]] are developed and tested through simulation <a class="yt-timestamp" data-t="01:58:55">[01:58:55]</a>.

### Reasons for Simulation
*   **Cost and Access**: Physical quantum computers are extremely large and expensive, making direct access and experimentation limited <a class="yt-timestamp" data-t="01:59:05">[01:59:05]</a>.
*   **Feasibility**: Many theoretical [[basics_of_quantum_computing_and_operators | quantum algorithms]] are designed for ideal, error-corrected quantum computers that do not yet exist <a class="yt-timestamp" data-t="01:10:48">[01:10:48]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Simulations allow researchers to test these algorithms without the constraints of current hardware <a class="yt-timestamp" data-t="01:13:15">[01:13:15]</a>.

### Tools and Platforms for Simulation
*   **PennyLane**: A Python library that allows users to create [[quantum_circuits_and_anzats_in_neural_networks | quantum circuits]] and simulate quantum devices with varying qubit counts (e.g., two, three, or four qubits) <a class="yt-timestamp" data-t="01:54:01">[01:54:01]</a>, <a class="yt-timestamp" data-t="01:54:17">[01:54:17]</a>. PennyLane can also compile code to run on different quantum backends <a class="yt-timestamp" data-t="01:55:08">[01:55:08]</a>.
*   **Paddle Quantum**: A deep learning platform used for quantum simulations, particularly in the context of [[quantum_machine_learning_challenges | quantum machine learning]] <a class="yt-timestamp" data-t="02:00:06">[02:00:06]</a>.
*   **Online Simulators**: Websites like Quantum Inspire allow users to build and simulate small [[quantum_circuits_and_anzats_in_neural_networks | quantum circuits]] and understand the behavior of individual [[basics_of_quantum_computing_and_operators | quantum gates]] <a class="yt-timestamp" data-t="02:29:57">[02:29:57]</a>, <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.

## Hybrid [[analog_and_digital_hybrid_computing | Quantum and Classical Computing]]
Many current [[basics_of_quantum_computing_and_operators | quantum algorithms]], especially in the NISQ era, employ a [[analog_and_digital_hybrid_computing | hybrid approach]] that combines both quantum and classical components <a class="yt-timestamp" data-t="01:12:57">[01:12:57]</a>. For example, a quantum neural network might use quantum circuits for feature extraction, but then utilize classical computers for tasks like calculating loss functions and optimizing parameters <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>, <a class="yt-timestamp" data-t="00:56:30">[00:56:30]</a>.

## Accessibility of Real Quantum Computers
While most quantum research is simulated, some quantum hardware is becoming accessible through cloud platforms.
*   **Amazon Braket**: Offers access to real quantum devices for rent, although initial offerings might focus on simulation time <a class="yt-timestamp" data-t="01:55:34">[01:55:34]</a>.
*   **IBM Q**: Provides access to IBM's quantum systems <a class="yt-timestamp" data-t="01:55:25">[01:55:25]</a>.
*   **Google Cirq**: Associated with Google's quantum hardware, including chips like Sycamore <a class="yt-timestamp" data-t="01:55:25">[01:55:25]</a>.

In the future, as [[quantum_computing_advancements | quantum computing advancements]] continue, real quantum computers are expected to offer significant advantages over classical computers for certain problems <a class="yt-timestamp" data-t="01:57:36">[01:57:36]</a>.