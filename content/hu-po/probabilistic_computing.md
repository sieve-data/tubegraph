---
title: Probabilistic computing
videoId: Hxv_y_bI3zA
---

From: [[hu-po]] <br/> 

Probabilistic computing, also referred to as thermodynamic computing, represents a new class of computer designed to address the growing demand for computation as traditional digital hardware approaches fundamental limits like the end of Moore's Law and Denard's Law <a class="yt-timestamp" data-t="04:41:45">[04:41:45]</a>. These specialized, unconventional machines sit "in between" [[hybrid_quantumclassical_computing | quantum computers]] and digital computers <a class="yt-timestamp" data-t="07:28:44">[07:28:44]</a>.

Instead of relying on binary ones and zeros like digital computers <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a> or quantum states like quantum computers <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>, probabilistic computers leverage natural processes, specifically the vibration of matter (atoms and molecules), to perform computation <a class="yt-timestamp" data-t="08:24:28">[08:24:28]</a>. This approach is well-suited for tasks involving randomness, such as probabilistic and [[generative_latent_space_reasoning | generative AI]] <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>, and can be exploited for linear algebra computations <a class="yt-timestamp" data-t="09:16:03">[09:16:03]</a>.

## Key Players

*   **Normal Computing AI**
    *   A startup that launched from stealth <a class="yt-timestamp" data-t="05:59:01">[05:59:01]</a>.
    *   They are actively publishing papers and open-sourcing their code, which distinguishes them from some competitors <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>.
    *   Their mission is to make AI universally scalable <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.
    *   The paper discussed, "Thermodynamic Natural Gradient Descent," was released by Normal Computing on May 22, 2024 <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.
    *   They use Texas Instruments chips for digital-to-analog conversion <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. This choice is significant due to the geopolitical advantage of U.S.-based chip manufacturing <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

*   **Extropic**
    *   Considered a more famous probabilistic computing company <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
    *   Noted for generally not releasing their work or publishing papers, unlike Normal Computing <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>.

## How it Works: Thermodynamic Natural Gradient Descent (TNGD)

Probabilistic computing enables **Thermodynamic Natural Gradient Descent (TNGD)**, a novel algorithm designed to perform second-order optimization for neural networks <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>. This is a significant advancement over the common first-order methods like SGD (Stochastic Gradient Descent) and Adam, which are primarily used in deep learning due to hardware limitations <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.

### First vs. Second Order Optimization

*   **First Order Methods (e.g., SGD, Adam):**
    *   Rely on the first derivative (slope) of the loss landscape <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a>.
    *   They take small steps down the steepest path <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.
    *   Effective for simple loss landscapes but can struggle with complex surfaces or get stuck in local minima <a class="yt-timestamp" data-t="43:51:00">[43:51:00]</a>.
    *   More efficient to compute on digital computers compared to second-order methods <a class="yt-timestamp" data-t="24:08:00">[24:08:00]</a>.

*   **Second Order Methods (e.g., Natural Gradient Descent - NGD):**
    *   Utilize the second derivative (curvature) of the loss landscape <a class="yt-timestamp" data-t="18:07:00">[18:07:00]</a>.
    *   This provides more information about the shape of the landscape, allowing for better, potentially larger, gradient steps <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>.
    *   NGD explicitly accounts for the curvature of the loss landscape using the Fisher Information Matrix (or its empirical approximation) <a class="yt-timestamp" data-t="38:43:00">[38:43:00]</a>.
    *   The Fisher Information Matrix serves as a substitute for the Hessian (second derivative matrix) in NGD <a class="yt-timestamp" data-t="41:05:00">[41:05:05]</a>.
    *   The Hessian and Jacobian (first derivative matrix) are used to compute the Fisher Information Matrix <a class="yt-timestamp" data-t="45:56:00">[45:56:00]</a>.
    *   While theoretically converging in fewer iterations <a class="yt-timestamp" data-t="23:18:00">[23:18:00]</a>, NGD has historically been computationally expensive on digital hardware (O(N^3) runtime, O(N^2) memory) <a class="yt-timestamp" data-t="52:23:00">[52:23:00]</a>.

### The Hybrid Digital-Analog System

TNGD is implemented on a [[hybrid_quantumclassical_computing | hybrid digital-analog system]] consisting of a GPU (digital) and an SPU (Stochastic Processing Unit - analog/thermodynamic) <a class="yt-timestamp" data-t="25:17:00">[25:17:00]</a>.

1.  **GPU's Role:**
    *   Stores the neural network model architecture <a class="yt-timestamp" data-t="26:12:00">[26:12:00]</a>.
    *   Handles standard digital tasks like data loading and calculating the first-order gradient (Delta L) and the Jacobian and Hessian matrices <a class="yt-timestamp" data-t="28:51:00">[28:51:00]</a>.

2.  **SPU's Role:**
    *   The core thermodynamic computer <a class="yt-timestamp" data-t="25:56:00">[25:56:00]</a>.
    *   Receives the gradient, Jacobian, and Hessian from the GPU via a Digital-to-Analog Converter (DAC) <a class="yt-timestamp" data-t="28:00:00">[28:00:00]</a>.
    *   These inputs modify the dynamics of the SPU, allowing it to "evolve" or dissipate heat <a class="yt-timestamp" data-t="28:14:00">[28:14:00]</a>.
    *   The SPU settles towards an equilibrium state defined by a [[bayesian_statistics_and_applications_in_machine_learning | Boltzmann distribution]] <a class="yt-timestamp" data-t="55:27:00">[55:27:00]</a>.
    *   This equilibrium state provides an estimate of the natural gradient <a class="yt-timestamp" data-t="55:54:00">[55:54:00]</a>.
    *   Samples are taken from the SPU and sent back to the GPU via an Analog-to-Digital Converter (ADC) <a class="yt-timestamp" data-t="28:05:00">[28:05:00]</a>.

3.  **Asynchronous Operation:**
    *   The GPU and SPU can operate asynchronously <a class="yt-timestamp" data-t="28:36:00">[28:36:00]</a> because the "clock speed" of nature (the rate at which molecules vibrate and dissipate heat) is incredibly fast – significantly faster than a GPU's clock speed <a class="yt-timestamp" data-t="59:40:00">[59:40:00]</a>.
    *   Crucially, numerical evidence shows that accurate samples of the natural gradient can be taken even before the SPU fully reaches equilibrium, without significantly harming performance <a class="yt-timestamp" data-t="58:22:00">[58:22:00]</a>.

### Advantages of TNGD

*   **Computational Efficiency:** TNGD drastically reduces the runtime and memory complexity of NGD from O(N^3) runtime and O(N^2) memory to a linear O(N) for both, matching the efficiency of SGD/Adam <a class="yt-timestamp" data-t="52:53:00">[52:53:00]</a>.
*   **Momentum Effect:** The physical nature of the SPU introduces an emergent "momentum" effect <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>. When a new batch of data is fed, residual thermal/vibrational information from previous batches remains <a class="yt-timestamp" data-t="15:57:00">[15:57:00]</a>. This built-in history helps overcome local minima, similar to explicit momentum terms in algorithms like Adam <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>. A non-zero delay time can even improve performance due to this effect <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.
*   **Smooth Interpolation:** The time allowed for the SPU to evolve acts as a toggle <a class="yt-timestamp" data-t="01:01:50">[01:01:50]</a>. A zero evolution time is equivalent to SGD, while infinite time approaches NGD. This allows for a smooth interpolation between first-order and second-order optimization <a class="yt-timestamp" data-t="01:01:11">[01:01:11]</a>.

## Current State and Challenges

*   **Early Development:** The technology is still in its early stages, with companies like Normal Computing building "demos" and proof-of-concept setups <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. These are not yet production-ready systems for training large models like Llama 4 <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.
*   **Thermal Isolation:** Probabilistic computers are highly sensitive to external perturbations, requiring thermal insulation to prevent interference with the atomic vibrations <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
*   **Simulated vs. Real Hardware:** The paper's reported performance relies on a *simulated* TNGD, not actual physical hardware <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>. This is a common practice in early-stage quantum computing research as well <a class="yt-timestamp" data-t="01:19:15">[01:19:15]</a>. The simulation itself can be computationally intensive, requiring high-end GPUs like the Nvidia A100 <a class="yt-timestamp" data-t="01:22:50">[01:22:50]</a>.
*   **Performance Metrics:** While TNGD outperforms Adam and other second-order optimizers in toy problems (e.g., CNN on MNIST, DistillBert fine-tuning on SQuAD) <a class="yt-timestamp" data-t="01:08:52">[01:08:52]</a>, the practical implications rely on the future availability and scalability of physical analog thermodynamic computers <a class="yt-timestamp" data-t="01:17:07">[01:17:07]</a>.
*   **Analog-to-Digital Conversion Bottleneck:** Currently, the slowest part of the hybrid system is the conversion of analog information from the SPU back into digital information for the GPU <a class="yt-timestamp" data-t="01:04:46">[01:04:46]</a>. This suggests a potential future where all computations might be performed in thermodynamic/probabilistic space, eliminating the need for digital components for certain tasks <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>. However, this is likely decades away <a class="yt-timestamp" data-t="01:05:34">[01:05:34]</a>.

## Potential Future

Probabilistic computing is unlikely to immediately replace all digital computers <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>. It may first find its niche in specialized data centers for AI training, where its advantages in second-order optimization for complex loss landscapes are most beneficial <a class="yt-timestamp" data-t="01:05:54">[01:05:54]</a>. The ability to efficiently train [[ai_algorithms_and_computational_constraints | AI algorithms and computational constraints]] is a significant market opportunity <a class="yt-timestamp" data-t="01:38:09">[01:38:09]</a>.