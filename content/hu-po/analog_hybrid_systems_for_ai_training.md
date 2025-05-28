---
title: Analog hybrid systems for AI training
videoId: Hxv_y_bI3zA
---

From: [[hu-po]] <br/> 

Analog hybrid systems present a novel approach to [[Hardware for AI training and deployment | AI training]], aiming to overcome the limitations of conventional [[Hardware for AI training and deployment | digital hardware]] by integrating specialized analog components known as Stochastic Processing Units (SPUs) <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>. This approach centers on accelerating complex optimization methods for machine learning models <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## The Need for New Hardware Paradigms

The advancement of [[Hardware for AI training and deployment | digital hardware]] is encountering fundamental limits, often referred to as the ending of Moore's Law and Denard's Law <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This presents an opportunity for specialized, unconventional [[Hardware for AI training and deployment | hardware]] that can address the ever-growing computational demands of AI <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

Conventional [[Hardware for AI training and deployment | digital hardware]] limits the range of training algorithms that can be practically used <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. Most deep learning systems currently employ relatively simplistic optimizers, such as stochastic gradient descent (SGD), Adam, and their variants, which are primarily first-order methods <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. While second-order training methods offer better convergence properties, they are rarely used in practice for large-scale training due to significant [[Hardware for AI training and deployment | hardware]] limitations <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Thermodynamic Computing

Thermodynamic computers, sometimes referred to as probabilistic computers, occupy a space between digital and quantum computers <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Unlike digital computers that operate with ones and zeros via transistors, or quantum computers that leverage quantum states of matter, thermodynamic computers utilize natural processes, specifically the vibration and interaction of matter, to perform computations <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This involves using heat and the resulting molecular vibrations to perform linear algebra computations <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

Such systems are particularly well-suited for tasks involving randomness, like probabilistic and generative AI <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. Key players in this emerging field include:
*   **Normal Computing:** A startup that publicly released a paper on "Thermodynamic Natural Gradient Descent" <a class="yt-timestamp" data-t="02:54:55">[02:54:55]</a>. They maintain a public GitHub repository with their code and papers <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **Extropic:** Another prominent company in the probabilistic computing space, though they are noted for being more secretive and not publicly releasing their work <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a>.

A challenge for these systems is the need for thermal insulation to prevent external factors from interfering with the precise vibrations of matter <a class="yt-timestamp" data-t="01:00:32">[01:00:32]</a>. This isolation is crucial for accurate computation <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

## Second-Order Optimization and Loss Landscapes

The core advantage of thermodynamic computers lies in their ability to efficiently perform second-order optimization methods, specifically Natural Gradient Descent (NGD) <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### Understanding Loss Landscapes

Training a neural network involves minimizing a "loss function," which quantifies how well the model performs on a given task <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. This minimization process can be visualized as navigating a "loss landscape," where the parameters of the neural network determine the "location" and the loss function determines the "height" of that location <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. The goal is to find the global minimum of this landscape <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

### First-Order vs. Second-Order Methods

*   **First-Order Methods (e.g., SGD, Adam):** These methods, like SGD, use only the first derivative (gradient or slope) of the loss function to determine the direction of the next step <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. This is akin to looking only at the immediate velocity on the landscape <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   **Second-Order Methods (e.g., NGD):** These methods use the second derivative of the loss function, or approximations like the Hessian or Fisher Information Matrix, to understand the "curvature" of the loss landscape <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. This additional information allows for more informed and potentially larger steps towards the minimum, leading to faster convergence in terms of iterations <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.

Modern neural networks have billions of parameters, resulting in incredibly complex, high-dimensional loss landscapes <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>. In such complex spaces, understanding the curvature through second-order derivatives becomes crucial for efficient optimization <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>.

### The Computational Challenge

While NGD theoretically converges faster (fewer iterations), each iteration is far more computationally expensive on [[Hardware for AI training and deployment | digital hardware]] <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. The runtime for NGD on digital computers scales cubically (O(N³)) with the number of parameters (N), and memory scales quadratically (O(N²)) <a class="yt-timestamp" data-t="00:52:28">[00:52:28]</a>. In contrast, SGD and Adam scale linearly (O(N)) <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>. This explains why NGD is rarely used in practice <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.

However, thermodynamic computers can perform NGD with linear scaling (O(N)) in both runtime and memory, making it as efficient as SGD on these specialized systems <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>.

## Hybrid Analog-Digital Architecture

The proposed system for "Thermodynamic Natural Gradient Descent" (TGD) is a hybrid digital-analog architecture <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. It combines a conventional GPU with a Stochastic Processing Unit (SPU), which is the analog thermodynamic computer <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

### Component Roles:
*   **GPU (Digital):**
    *   Stores the model architecture <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.
    *   Handles data loading, mini-batches, and general accessory work <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.
    *   Calculates the first-order gradient (Delta L) and components of the Fisher Information Matrix (Jacobian and Hessian) <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>.
*   **SPU (Analog/Thermodynamic):**
    *   Receives the gradient and Fisher Matrix components from the GPU via a Digital-to-Analog Converter (DAC) <a class="yt-timestamp" data-t="00:27:59">[00:27:59]</a>.
    *   Evolves physically (molecules vibrating, heat dissipating) to calculate an estimate of the natural gradient <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>.
    *   Returns the natural gradient estimate to the GPU via an Analog-to-Digital Converter (ADC) <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>.
    *   Operates asynchronously, leveraging the incredibly fast "clock speed of the universe" (the natural speed of molecular vibration and heat dissipation) <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>.

The SPU's ability to efficiently solve linear systems by naturally evolving to an equilibrium state, defined by a Boltzmann distribution, is key <a class="yt-timestamp" data-t="00:55:07">[00:55:07]</a>. Theoretically, this equilibrium state provides a perfect estimate of the natural gradient <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>. Crucially, numerical evidence suggests that samples can be taken even before full equilibrium is reached without significant performance degradation <a class="yt-timestamp" data-t="00:58:22">[00:58:22]</a>.

A unique aspect is that the time allowed for the SPU to evolve allows for a smooth interpolation between SGD (zero delay) and NGD (infinite delay), enabling fine-tuning of the optimization strategy <a class="yt-timestamp" data-t="01:01:11">[01:01:11]</a>.

### Geopolitical Implications
The hardware components of these systems, like the FPGAs for digital-to-analog conversion, may utilize chips from companies like Texas Instruments <a class="yt-timestamp" data-t="03:16:04">[03:16:04]</a>. This highlights a potential geopolitical advantage, as it could reduce reliance on offshore chip manufacturers like TSMC, aligning with desires for [[Hardware for AI training and deployment | geographically diversified chip supply chains]] <a class="yt-timestamp" data-t="03:26:04">[03:26:04]</a>.

### Implicit Momentum Effect

An interesting finding is that a non-zero delay time in the SPU's operation can improve performance <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>. This "delay" appears to have a "momentum effect" <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>.
> The device retains information about the curvature of the previous quadratic approximation while being subjected to the updated quadratic approximation. This effect propagates across iterations which is reminiscent of momentum. <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>

Unlike explicit momentum terms stored in digital memory, this is a form of inherent momentum, where residual "thermal heat" or vibrational information from previous batches persists within the SPU, influencing subsequent computations <a class="yt-timestamp" data-t="01:15:37">[01:15:37]</a>.

## Current Performance and Future Outlook

Early results, primarily from simulations, demonstrate that TGD can achieve lower training loss faster compared to Adam, even when accounting for per-iteration runtime differences <a class="yt-timestamp" data-t="01:09:49">[01:09:49]</a>. These demonstrations have been conducted on "toy problems," such as convolutional networks for MNIST classification and fine-tuning a DistilBERT model with LoRA on a small question-answering dataset <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>.

The slowest part of the current hybrid system is the conversion of information between the analog SPU and the digital GPU <a class="yt-timestamp" data-t="01:04:46">[01:04:46]</a>. This suggests that future advancements might involve performing more computations directly within the thermodynamic domain <a class="yt-timestamp" data-t="01:05:03">[01:05:03]</a>.

While promising, the technology is still in its early "proof of concept" phase, similar to early quantum computing <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>. Widespread availability and integration into production environments are likely decades away <a class="yt-timestamp" data-t="01:05:34">[01:05:34]</a>. It remains to be seen whether these systems will become ubiquitous consumer devices or remain specialized [[Hardware for AI training and deployment | hardware]] used primarily in data centers for [[Hardware for AI training and deployment | AI training]] <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>.