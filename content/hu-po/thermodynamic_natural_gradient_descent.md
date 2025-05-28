---
title: Thermodynamic natural gradient descent
videoId: Hxv_y_bI3zA
---

From: [[hu-po]] <br/> 

Thermodynamic Natural Gradient Descent (TNGD) is a novel approach to optimizing neural networks, leveraging specialized hardware known as [[future_of_thermodynamic_computing | thermodynamic or probabilistic computers]]. This method, detailed in a paper released on May 22, 2024, by Normal Computing, aims to overcome the limitations of traditional digital hardware in performing advanced optimization techniques. The official name of the paper is "Thermodynamic Natural Gradient Descent" <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

## Limitations of Current Hardware and Optimization Methods

Conventional digital hardware, such as GPUs, limits the range of training algorithms that can be effectively used <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>. Most deep learning models currently utilize relatively simplistic optimizers like stochastic gradient descent (SGD) and Adam <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>. These are [[gradientbased_optimization_vs_language_modelbased_optimization | first-order methods]], primarily because digital computers are not efficient at performing [[gradientbased_optimization_vs_language_modelbased_optimization | second-order training]] <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.

The ending of Moore's Law and Dennard's Law for digital hardware presents an opportunity for specialized, unconventional hardware <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. Digital computers are hitting fundamental limits in transistor scaling, yet the need for computation continues to grow <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.

## Introduction to Thermodynamic/Probabilistic Computers

Thermodynamic computers, also referred to as probabilistic computers, exist conceptually between traditional digital computers and quantum computers <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.
*   **Digital Computers**: Operate on ones and zeros, implemented with transistors and silicon <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.
*   **Quantum Computers**: Rely on quantum states of matter and wave functions, still in very early stages of development <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>.
*   **Thermodynamic/Probabilistic Computers**: Utilize the vibration of matter (like atoms in a lattice) to perform computations <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. They "compute with nature" by exploiting natural physical processes, such as thermodynamic processes involving heat <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>. These are well-suited for computations involving randomness, like probabilistic and generative AI <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.

Normal Computing AI is a startup that launched from stealth, developing a probabilistic computer for generative AI <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>. Another company in this space is Extropic, though they do not publicly release their work or code <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.

### Stochastic Processing Unit (SPU) Hardware

Normal Computing introduces a new hardware component called the Stochastic Processing Unit (SPU), which is the analog thermodynamic computer <a class="yt-timestamp" data-t="25:36:00">[25:36:00]</a>.
*   **Hybrid System**: TNGD operates in a hybrid digital-analog loop, involving both a GPU (digital) and an SPU (analog) <a class="yt-timestamp" data-t="25:08:00">[25:08:00]</a>.
*   **SPU Function**: The SPU's primary role is to compute the difficult [[gradientbased_optimization_vs_language_modelbased_optimization | second-order]] term, specifically the natural gradient, by using physical processes <a class="yt-timestamp" data-t="26:45:00">[26:45:00]</a>.
*   **Thermal Isolation**: SPUs require thermal insulation or isolation from the outside world to prevent external factors like heat from interfering with the precise vibrations of the material <a class="yt-timestamp" data-t="27:03:00">[27:03:00]</a>. This is a common challenge, similar to quantum computers <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>.
*   **Digital-to-Analog Conversion (DAC)**: Information is sent from the GPU (digital) to the SPU (analog) via a DAC <a class="yt-timestamp" data-t="28:00:00">[28:00:00]</a>. Analog-to-digital conversion (ADC) sends results back to the GPU <a class="yt-timestamp" data-t="28:05:00">[28:05:00]</a>.
*   **Components**: The SPU circuit board includes unit cells and couplings. For their demos, they built three identical copies to verify matrix inversion <a class="yt-timestamp" data-t="29:50:00">[29:50:00]</a>. They use Texas Instruments (TI) chips for the FPGA involved in data conversion and uploading/downloading data <a class="yt-timestamp" data-t="31:16:00">[31:16:00]</a>. This highlights a geopolitical advantage, as TI has fabs in the US, reducing reliance on overseas chip manufacturing <a class="yt-timestamp" data-t="32:24:00">[32:24:00]</a>.

## Thermodynamic Natural Gradient Descent (TNGD) Explained

Optimization in machine learning involves finding the minimum of a [[numerical_gradients_vs_analytical_gradients | loss landscape]] <a class="yt-timestamp" data-t="14:10:00">[14:10:00]</a>.
*   **Loss Landscape**: A visualization of the loss function's value across different model parameters <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>. In practice, modern neural networks have billions of parameters, making the loss landscape a high-dimensional space <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>. Gradient descent aims to find the global minimum of this landscape <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.
*   **First-Order Methods**: Like SGD, use only the first derivative (gradient) of the loss function, indicating the slope and basic direction of movement <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a>. They effectively measure "velocity" in the loss landscape <a class="yt-timestamp" data-t="18:04:00">[18:04:00]</a>.
*   **Second-Order Methods**: Use the second derivative (e.g., Hessian or Fisher Information Matrix) to understand the curvature of the loss landscape <a class="yt-timestamp" data-t="18:07:00">[18:07:00]</a>. This provides more information, allowing for potentially larger and more efficient steps toward the minimum <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>. Second-order methods are more powerful for complex loss surfaces <a class="yt-timestamp" data-t="43:49:00">[43:49:00]</a>.

### Natural Gradient Descent (NGD)

Natural Gradient Descent (NGD) is a [[gradientbased_optimization_vs_language_modelbased_optimization | second-order optimization]] method that typically converges in fewer iterations than SGD to the same loss value <a class="yt-timestamp" data-t="23:18:00">[23:18:00]</a>. However, a single iteration of NGD is much more computationally expensive than SGD or Adam on digital computers <a class="yt-timestamp" data-t="23:57:00">[23:57:00]</a>.

The NGD update rule involves the inverse of the Fisher Information Matrix (often simply called the Fisher) <a class="yt-timestamp" data-t="39:28:00">[39:28:00]</a>. The Fisher Matrix captures information about the loss landscape's curvature and acts as a substitute for the Hessian matrix <a class="yt-timestamp" data-t="41:05:00">[41:05:00]</a>. Because the true Fisher Information Matrix is difficult to compute, an "empirical Fisher Information Matrix" is often used as an approximation <a class="yt-timestamp" data-t="42:23:00">[42:23:00]</a>. The SPU specifically calculates the Jacobian (first-order partial derivatives) and Hessian (second-order partial derivatives) matrices, which can then be used to derive the Fisher Information Matrix <a class="yt-timestamp" data-t="45:56:00">[45:56:00]</a>.

A "positive semi-definite" curvature matrix is required for these methods to work <a class="yt-timestamp" data-t="46:27:00">[46:27:00]</a>. A positive definite matrix implies a single, clear minimum, while a positive semi-definite matrix indicates multiple possible solutions, like a channel of optimal points <a class="yt-timestamp" data-t="47:15:00">[47:15:00]</a>.

### TNGD's Hybrid Approach

TNGD is a hybrid algorithm where the GPU handles the model architecture, data loading, and calculation of the gradient and Fisher information matrix (specifically, the Jacobian and Hessian) <a class="yt-timestamp" data-t="26:12:00">[26:12:00]</a>. This information is then sent to the SPU <a class="yt-timestamp" data-t="26:36:00">[26:36:00]</a>.

The SPU then allows its internal system of particles to "evolve" under the influence of this input <a class="yt-timestamp" data-t="28:21:00">[28:21:00]</a>. This evolution is described by an Ornstein-Uhlenbeck process, which is a mathematical model for Brownian motion <a class="yt-timestamp" data-t="12:28:00">[12:28:00]</a>. The SPU settles to an equilibrium state defined by a Boltzmann distribution, which describes the probability of a system being in a certain state based on its energy and temperature <a class="yt-timestamp" data-t="55:27:00">[55:27:00]</a>. This equilibrium state provides an estimate of the natural gradient <a class="yt-timestamp" data-t="55:54:00">[55:54:00]</a>.

Crucially, while theory suggests the system needs to evolve to "infinity" to reach a perfect equilibrium state, numerical evidence shows that samples can be taken even before full equilibrium is reached without significant performance harm <a class="yt-timestamp" data-t="58:21:00">[58:21:00]</a>. This is because the "clock speed of nature" (the speed at which molecules vibrate and heat dissipates) is incredibly fast, much faster than a GPU's clock speed <a class="yt-timestamp" data-t="59:04:00">[59:04:00]</a>.

### Interpolation and Implicit Momentum

TNGD allows for a smooth interpolation between SGD and NGD. If the "time" allowed for the SPU to evolve (the delay before reading the state) is zero, the system effectively performs SGD. If infinite time is allowed, it performs NGD <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>. This offers a tunable mechanism to adjust the balance between [[gradientbased_optimization_vs_language_modelbased_optimization | first-order]] and [[gradientbased_optimization_vs_language_modelbased_optimization | second-order]] optimization <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>.

A surprising finding is that a non-zero delay time can actually improve performance <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>. This is due to a "momentum effect": the SPU device retains residual thermal/vibrational information from previous batches of data <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>. This non-explicit momentum helps to overcome local minima in the loss landscape, similar to how explicit momentum terms are used in optimizers like Adam <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## Performance and Future Implications

### Computational Complexity
TNGD drastically reduces the computational overhead of NGD.
*   **SGD/Adam**: Linear scaling with model size (O(N) runtime, O(N) memory) <a class="yt-timestamp" data-t="52:08:00">[52:08:00]</a>.
*   **NGD (Digital)**: Cubic scaling with model size (O(N^3) runtime, O(N^2) memory), making it impractical for large models <a class="yt-timestamp" data-t="52:31:00">[52:31:00]</a>.
*   **TNGD (Hybrid)**: Achieves linear scaling (O(N) runtime, O(N) memory), similar to SGD/Adam, by offloading the complex second-order calculations to the SPU <a class="yt-timestamp" data-t="53:01:00">[53:01:00]</a>.

### Experimental Results
Normal Computing evaluated TNGD on two toy problems:
1.  **Classification Task**: A convolutional network (ConvNet) trained on the MNIST dataset (classifying handwritten digits) <a class="yt-timestamp" data-t="01:08:17">[01:08:17]</a>. TNGD appeared to achieve a lower loss faster than Adam, even when accounting for runtime differences, though the error bars were significant <a class="yt-timestamp" data-t="01:09:49">[01:09:49]</a>.
2.  **Language Model Fine-tuning**: Fine-tuning a LoRA (Low-Rank Adaptation) for a DistilBERT model on the Stanford Question Answering Dataset (SQuAD) <a class="yt-timestamp" data-t="01:10:24">[01:10:24]</a>. Pure TNGD performed worse than Adam, but a hybrid approach using the natural gradient estimate in conjunction with the Adam update rule yielded the best performance <a class="yt-timestamp" data-t="01:10:59">[01:10:59]</a>.

**Important Note**: These results were obtained using a *simulated* thermodynamic computer, not the actual hardware <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>.

### Current Limitations and Future Outlook
The slowest part of the current TNGD system is the conversion between analog and digital information (the "gray arrows" between GPU and SPU) <a class="yt-timestamp" data-t="01:04:46">[01:04:46]</a>. This suggests that future advancements might involve performing more, if not all, computation within the thermodynamic domain <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>.

While promising, the technology is still in its early stages ("proof of concept" mode) <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. It will likely take years before these computers reach production quality for large-scale tasks like training frontier models <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. The future market for these chips remains uncertain: they might remain highly specialized for AI training in specific data centers, or they could become ubiquitous, replacing digital computers entirely <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>.

TNGD offers a potential breakthrough for training AI models more efficiently by enabling practical [[numerical_gradients_vs_analytical_gradients | second-order optimization]], a critical step as AI models continue to grow in size and complexity <a class="yt-timestamp" data-t="01:38:05">[01:38:05]</a>.