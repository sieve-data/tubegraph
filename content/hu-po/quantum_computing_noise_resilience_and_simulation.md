---
title: Quantum computing noise resilience and simulation
videoId: ABEkChn3inY
---

From: [[hu-po]] <br/> 

Quantum computing is an emerging paradigm for fast computations that offers substantial advantages in solving valuable problems <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Major academic efforts in developing quantum algorithms on quantum hardware have led to powerful applications in optimization, cryptography, chemistry, and [[quantum_machine_learning|machine learning]] <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## Noisy Intermediate-Scale Quantum (NISQ) Devices

Current quantum devices are known as Noisy Intermediate-Scale Quantum (NISQ) devices <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. These devices typically have up to a few hundred physical qubits <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. The term "intermediate scale" refers to machines with tens to a few hundreds of qubits <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

### Challenges with NISQ Devices

NISQ devices are affected by both coherent and incoherent noise <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. This noise makes the practical implementation of many advantageous quantum algorithms less feasible <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. External environmental factors, such as stray photons or vibrations, can interfere with the quantum state of a qubit, causing errors that propagate through the system <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

Currently, NISQ devices cannot entirely eliminate these errors and do not yet employ full quantum error correction <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. Due to this noise, quantum algorithms designed for NISQ devices need to be "shallow," meaning they cannot have too many consecutive operations or deep layers <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

Despite these limitations, devices with 50 to 100 qubits have already demonstrated "quantum advantage" (or quantum supremacy) over the most powerful classical computers for certain carefully designed tasks <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>, <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Moore's Law and Quantum Computing

The "quantum volume," which is related to the number of qubits, has been increasing over the years <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. It has been suggested that to maintain pace with computational power, quantum machines may only need to grow by one qubit every two years <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

## Quantum Self-Attention Neural Networks (Q-SAN)

A new network architecture, [[quantum_selfattention_neural_networks | Quantum Self-Attention Neural Network (Q-SAN)]], has been proposed to establish meaningful quantum applications in fields like [[quantum_neural_networks_for_natural_language_processing | natural language processing (NLP)]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>, <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This architecture introduces the [[implementation_of_selfattention_on_quantum_systems | self-attention]] mechanism to [[quantum_neural_networks_for_natural_language_processing | quantum neural networks]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

Q-SAN addresses limitations of previous quantum NLP methods, such as heavy syntactic pre-processing and syntax-dependent network architectures, making it more practical for larger, real-world datasets <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>. It also possesses the desirable property of being implementable on near-term quantum devices <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Quantum Noise Resilience

A key feature of Q-SAN is its robustness to low-level quantum noises <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This resilience is crucial for practical implementation on existing NISQ devices, which are inherently noisy <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>, <a class="yt-timestamp" data-t="02:20:47">[02:20:47]</a>. Experiments have shown that Q-SAN maintains reasonable accuracy even with increasing levels of simulated noise, implying its noise resilience <a class="yt-timestamp" data-t="02:18:27">[02:18:27]</a>, <a class="yt-timestamp" data-t="02:19:14">[02:19:14]</a>.

### Hybrid Quantum-Classical Approach

Q-SAN employs a hybrid approach, combining quantum and classical components <a class="yt-timestamp" data-t="01:03:04">[01:03:04]</a>.

*   **Quantum Part**: Classical inputs (e.g., text tokens) are encoded into high-dimensional quantum states using "quantum ansats" (parameterized quantum circuits) <a class="yt-timestamp" data-t="01:51:56">[01:51:56]</a>, <a class="yt-timestamp" data-t="01:53:40">[01:53:40]</a>. These quantum states are then processed by quantum self-attention layers that involve operations like Hadamard gates (to create superpositions) and CNOT gates (to create entanglement between qubits) <a class="yt-timestamp" data-t="02:26:09">[02:26:09]</a>, <a class="yt-timestamp" data-t="02:29:06">[02:29:06]</a>. The parameters of these quantum layers (rotation angles) are learned during training <a class="yt-timestamp" data-t="02:28:57">[02:28:57]</a>.
*   **Classical Part**: After quantum processing, the quantum states are projected back to a low-dimensional classical feature space via quantum measurements <a class="yt-timestamp" data-t="01:53:47">[01:53:47]</a>, <a class="yt-timestamp" data-t="01:18:45">[01:18:45]</a>. A [[quantization_techniques_for_ai_models | Gaussian]] function is applied to these classical representations to obtain [[quantization_and_efficiency_in_ai_models | self-attention]] coefficients <a class="yt-timestamp" data-t="01:18:08">[01:18:08]</a>, <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a>. The final outputs are computed as classically weighted sums of the measured value parts, and these outputs are fed into a standard fully connected classical layer for binary prediction <a class="yt-timestamp" data-t="01:54:02">[01:54:02]</a>, <a class="yt-timestamp" data-t="02:29:06">[02:29:06]</a>.

### Training and Optimization

The loss function used is a mean squared error with regularization terms <a class="yt-timestamp" data-t="01:45:50">[01:45:50]</a>. Optimization is performed using stochastic gradient descent <a class="yt-timestamp" data-t="01:50:15">[01:50:15]</a>. The crucial aspect of training quantum circuits is that analytical gradients can be derived for the quantum layers, allowing for backpropagation through the entire hybrid network <a class="yt-timestamp" data-t="02:03:40">[02:03:40]</a>, <a class="yt-timestamp" data-t="02:09:09">[02:09:09]</a>. Parameters for the quantum ansats (rotation angles) and classical layers are initialized from a Gaussian distribution with zero mean <a class="yt-timestamp" data-t="02:11:16">[02:11:16]</a>.

## Simulation of Quantum Systems

Much of the research in quantum machine learning, including the development and evaluation of Q-SAN, is conducted through classical simulation rather than on actual quantum hardware <a class="yt-timestamp" data-t="01:58:37">[01:58:37]</a>. Tools like PennyLane (a Python library) allow researchers to create and simulate quantum circuits, exploring their behavior without direct access to a physical quantum computer <a class="yt-timestamp" data-t="01:54:01">[01:54:01]</a>. These simulations can run on various quantum backends, some of which are cloud-based services like Amazon Braket or IBM Quantum, offering access to actual (though still limited) quantum hardware for specific tasks <a class="yt-timestamp" data-t="01:55:02">[01:55:02]</a>. Google's Sycamore processor, for example, has 53 qubits <a class="yt-timestamp" data-t="01:56:17">[01:56:17]</a>.

The use of simulation is prevalent because physical quantum computers are large, expensive, and not widely accessible <a class="yt-timestamp" data-t="01:59:05">[01:59:05]</a>. While simulations are critical for development, the ultimate goal is to implement and validate algorithms on real, noise-resilient quantum hardware.