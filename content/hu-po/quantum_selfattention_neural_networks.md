---
title: Quantum selfattention neural networks
videoId: ABEkChn3inY
---

From: [[hu-po]] <br/> 

This article explores a paper on [[Deep Learning and Neural Networks|quantum self-attention neural networks]] for text classification, focusing on an approach that implements [[Attention mechanism and its role in neural networks|self-attention]] in the quantum realm <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. The research, from Baidu Research Institute for Quantum Computing in China and the Center for Quantum Software Information in Sydney, Australia, aims to establish meaningful quantum applications in artificial intelligence, including natural language processing (NLP) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Motivation and Context
The paper seeks to build better intuition around [[Quantum machine learning advancements|quantum machine learning]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. While the self-[[Attention mechanism and its role in neural networks|attention mechanism]] is a fundamental component of popular Transformer architectures, its implementation in the quantum world is a novel exploration <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The goal is to see if self-[[Attention mechanism and its role in neural networks|attention]] performs well when adapted for [[Quantum computing advancements|quantum computers]] <a class="yt-timestamp" data-t="00:58:21">[00:58:21]</a>.

Previous efforts in [[Quantum natural language processing (QNLP)|Quantum NLP]] (QNLP) faced limitations due to heavy syntactic pre-processing and syntax-dependent network architectures, making them impractical for larger datasets <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. The proposed Quantum Self-Attention Neural Network (QSANN) aims to overcome these drawbacks by introducing the [[Attention mechanism and its role in neural networks|self-attention mechanism]] into [[Deep Learning and Neural Networks|quantum neural networks]] <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

## Fundamental Quantum Concepts
*   **Qubit**: Unlike classical bits (0 or 1), a qubit can exist in a superposition of both 0 and 1 simultaneously <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It's represented as a vector where coefficients describe the probability of being 0 or 1 <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.
*   **Hilbert Space**: This is a mathematical vector space where quantum states (qubits) are described and manipulated <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. Its dimensionality grows exponentially with the number of qubits (2^N for N qubits) <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.
*   **Bra-Ket Notation**: A standard notation in quantum mechanics to represent quantum states and operations <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>. A "ket" (`|ψ⟩`) denotes a column vector, and a "bra" (`⟨ψ|`) denotes its conjugate transpose (a row vector) <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>.
*   **Quantum Gates (Unitary Operators)**: These are operations that transform quantum states, analogous to logic gates in classical computing <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.
    *   **Hadamard Gate (H)**: A fundamental single-qubit gate that creates a superposition of states <a class="yt-timestamp" data-t="00:37:47">[00:37:47]</a>. Applying it to a qubit in state 0 or 1 puts it in an equal superposition of both <a class="yt-timestamp" data-t="00:38:23">[00:38:23]</a>. It is its own inverse <a class="yt-timestamp" data-t="00:39:04">[00:39:04]</a>.
    *   **Pauli Operators (X, Y, Z)**: These are rotation gates that rotate the qubit state around the X, Y, or Z axes <a class="yt-timestamp" data-t="00:36:24">[00:36:24]</a>. For example, the Pauli Z gate flips a qubit's state from 0 to 1 and vice versa <a class="yt-timestamp" data-t="01:08:12">[01:08:12]</a>.
    *   **Controlled-NOT (C-NOT) Gate**: A two-qubit gate where one qubit (control) determines if the other qubit (target) is flipped <a class="yt-timestamp" data-t="01:27:38">[01:27:38]</a>. These gates are crucial for creating [[Quantum entanglement|entanglement]] between qubits <a class="yt-timestamp" data-t="01:29:19">[01:29:19]</a>.
*   **Quantum Measurement**: The process of extracting classical information from a quantum state <a class="yt-timestamp" data-t="01:41:26">[01:41:26]</a>. When a measurement is performed, the quantum state "collapses" into one of its basis states, losing the superposition information <a class="yt-timestamp" data-t="01:41:47">[01:41:47]</a>.

## Noisy Intermediate-Scale Quantum (NISQ) Devices
The paper focuses on implementing QSANN on [[Quantum computing advancements|NISQ devices]] <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>.
*   **Definition**: These are quantum devices available in the era prior to full error correction of [[Quantum computing advancements|quantum computers]] <a class="yt-timestamp" data-t="01:03:36">[01:03:36]</a>.
*   **Characteristics**: They have "intermediate scale" (tens to a few hundreds of qubits) and are "noisy" due to decoherence from external environments <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>. This noise means quantum algorithms need to be "shallow" (not too many consecutive operations) <a class="yt-timestamp" data-t="01:04:19">[01:04:19]</a>.
*   **Significance**: Despite limitations, NISQ devices with 50-100 qubits have already demonstrated "quantum advantage" over powerful classical computers for specific tasks <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

## Quantum Self-Attention Neural Network (QSANN) Architecture
QSANN is a hybrid approach combining quantum and classical components for text classification <a class="yt-timestamp" data-t="00:59:58">[00:59:58]</a>.

### Overall Structure
The network consists of multiple [[Quantum circuits and ansatz in neural networks|quantum self-attention layers]] (QSALs) followed by a classical fully connected layer for binary prediction <a class="yt-timestamp" data-t="01:29:51">[01:29:51]</a>.

### Input Encoding
Classical input data (text tokens, represented as D-dimensional vectors) are first encoded into high-dimensional quantum states <a class="yt-timestamp" data-t="00:49:46">[00:49:46]</a>. This is done using a [[Quantum circuits and ansatz in neural networks|quantum ansatz]] (U_encode) that transforms the classical input into a superposition of quantum states <a class="yt-timestamp" data-t="01:00:40">[01:00:40]</a>.

### Quantum Self-Attention Layer (QSAL)
A QSAL leverages three [[Quantum circuits and ansatz in neural networks|quantum ansätze]]: `U_Q` (query), `U_K` (key), and `U_V` (value), each parameterized by `Theta_Q`, `Theta_K`, and `Theta_V` respectively <a class="yt-timestamp" data-t="01:01:14">[01:01:14]</a>.

*   **Ansatz Structure**: These [[Quantum circuits and ansatz in neural networks|ansätze]] (or parameterized quantum circuits) consist of single-qubit rotation gates (RX, RY) and repeated C-NOT gates <a class="yt-timestamp" data-t="01:25:21">[01:25:21]</a>. The C-NOT gates entangle the qubits, while the repeated rotations increase the expressiveness of the ansatz <a class="yt-timestamp" data-t="01:31:52">[01:31:52]</a>.
*   **Gaussian Projected Quantum Self-Attention**:
    *   To compute [[Attention mechanism and its role in neural networks|self-attention]] coefficients, the quantum states generated by the query (`U_Q`) and key (`U_K`) ansätze are first measured, collapsing them into one-dimensional classical representations (`Z_QS`, `Z_KJ`) <a class="yt-timestamp" data-t="01:18:20">[01:18:20]</a>.
    *   A Gaussian function is then applied to these classical representations to derive the self-attention coefficients <a class="yt-timestamp" data-t="01:20:08">[01:20:08]</a>. This step is chosen to overcome limitations of direct inner-product self-attention in quantum data <a class="yt-timestamp" data-t="01:17:52">[01:17:52]</a>.
*   **Output Computation**: The final output of the QSAL is a classically weighted sum of the measured values (from `U_V` ansatz) <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>. This output is then fed into the next QSAL, forming a residual connection <a class="yt-timestamp" data-t="01:15:48">[01:15:48]</a>.

## Training QSANN
The QSANN is trained using a standard supervised learning approach <a class="yt-timestamp" data-t="01:45:08">[01:45:08]</a>.
*   **Loss Function**: A mean squared error (MSE) loss function is used, combined with L2 regularization terms for the classical weights and biases of the final layer <a class="yt-timestamp" data-t="01:49:01">[01:49:01]</a>.
*   **Optimization**: The network parameters are optimized using Stochastic Gradient Descent (SGD) with the Adam optimizer <a class="yt="02:00:25">[02:00:25]</a>.
*   **Gradient Calculation**: The analytical gradients for both classical and quantum parameters are derived. Critically, the partial derivatives of the quantum measurements with respect to the ansatz parameters (Theta) can be evaluated via the parameter shift rule <a class="yt-timestamp" data-t="02:06:26">[02:06:26]</a>. This ensures that the entire hybrid network is differentiable, allowing for backpropagation through the quantum layers <a class="yt-timestamp" data-t="02:09:09">[02:09:09]</a>.
*   **Initialization**: All [[Quantum circuits and ansatz in neural networks|ansatz]] parameters and classical weights are initialized from a Gaussian distribution with a mean of zero and a small standard deviation (0.01) <a class="yt-timestamp" data-t="02:11:16">[02:11:16]</a>.

## Experimental Results
The experiments are conducted on public text classification datasets (Yelp, IMDb, Amazon) <a class="yt-timestamp" data-t="01:59:29">[01:59:29]</a>. All quantum parts of the experiment are accomplished via classical simulation, not on actual [[Quantum computing advancements|quantum hardware]] <a class="yt-timestamp" data-t="01:58:34">[01:58:34]</a>.

*   **Performance**: QSANN outperforms existing QNLP models and a simple classical [[Attention mechanism and its role in neural networks|self-attention neural network]] on the text classification tasks <a class="yt-timestamp" data-t="02:03:07">[02:03:07]</a>. The quantum network utilizes significantly fewer parameters (e.g., 49) compared to its classical counterpart (e.g., 785) <a class="yt-timestamp" data-t="02:13:52">[02:13:52]</a>.
*   **Robustness to Noise**: The method demonstrates robustness to low-level quantum noise (e.g., depolarizing and amplitude damping channels) <a class="yt-timestamp" data-t="01:59:50">[01:59:50]</a>. As noise levels increase, the accuracy remains relatively stable, confirming its noise resilience <a class="yt-timestamp" data-t="02:19:14">[02:19:14]</a>.
*   **Limitations**: The datasets used are very small (e.g., 17 words, 130 sentences, or up to 1000 sequences with a few dozen words each) <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>. The quantum circuits are also "shallow" (e.g., only 6 layers deep), reflecting the limitations of [[Quantum computing advancements|NISQ devices]] <a class="yt-timestamp" data-t="01:53:15">[01:53:15]</a>. The paper acknowledges that more advanced techniques like positional encoding and multi-head [[Attention mechanism and its role in neural networks|attention]] could be explored for future generative models <a class="yt-timestamp" data-t="02:21:03">[02:21:03]</a>.

## Conclusion
The paper successfully proposes a [[Quantum self-attention neural networks|quantum self-attention neural network]] for text classification that is implementable on [[Quantum computing advancements|near-term quantum devices]] and exhibits noise resilience <a class="yt-timestamp" data-t="02:20:43">[02:20:43]</a>. While the problem domain and model size are small, this work serves as a proof of concept, demonstrating the potential for combining [[Attention mechanism and its role in neural networks|self-attention]] with [[Deep Learning and Neural Networks|quantum neural networks]] in QNLP and [[Quantum machine learning advancements|QML]] <a class="yt-timestamp" data-t="02:20:56">[02:20:56]</a>.