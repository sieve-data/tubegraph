---
title: Natural gradient descent vs stochastic gradient descent
videoId: Hxv_y_bI3zA
---

From: [[hu-po]] <br/> 

## Introduction to Optimization Methods
Optimization methods are crucial in machine learning for training models by minimizing a [[Loss Landscape]]. The goal is to find the global minimum of this landscape, representing the optimal parameters for the model <a class="yt-timestamp" data-t="01:14:27">[01:14:27]</a>.

Most deep learning models today use relatively simplistic optimizers like [[Stochastic Gradient Descent | stochastic gradient descent]] (SGD), Adam, and their variants <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. These are primarily [[Continuous vs Discrete Optimization | first-order optimization methods]] <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.

## First-Order vs. Second-Order Optimization

### First-Order Methods (e.g., SGD, Adam)
First-order methods, such as SGD and Adam, rely on the first derivative (the gradient or slope) of the [[Loss Landscape | loss function]] at a given point <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a>.
*   They look at the immediate slope to determine the direction of movement <a class="yt-timestamp" data-t="01:17:51">[01:17:51]</a>.
*   Updates involve taking small steps in the direction of the negative gradient of the loss function <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>, defined by a learning rate <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.
*   Because they only consider the immediate slope, they often require small learning rates to avoid overshooting the minimum <a class="yt-timestamp" data-t="01:15:13">[01:15:13]</a>.
*   **Computational Complexity:** For digital computers, SGD and Adam have a linear runtime and memory cost relative to the model size (O(N)) <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. This efficiency makes them popular for large models <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

### Second-Order Methods (e.g., Natural Gradient Descent)
Second-order methods, like [[Natural Gradient Descent | natural gradient descent]] (NGD), utilize information from the second derivative (curvature) of the [[Loss Landscape | loss function]] <a class="yt-timestamp" data-t="01:18:07">[01:18:07]</a>.
*   They consider the curvature of the landscape, which provides a more informed direction and magnitude for the step <a class="yt-timestamp" data-t="01:18:10">[01:18:10]</a>.
*   This allows them to take potentially larger, more efficient steps towards the minimum <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   NGD can better navigate complex loss surfaces, making them powerful for models with billions of parameters where the [[Loss Landscape | loss landscape]] is highly complicated <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
*   The update rule for NGD involves the inverse of the [[Fisher Information Matrix]] (also known as the Fisher), which acts as a substitute for the Hessian matrix <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
    *   **Jacobian:** Represents first-order partial derivatives <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.
    *   **Hessian:** Represents second-order partial derivatives <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.
    *   The Fisher Information Matrix captures information about the [[Loss Landscape | loss landscape]]'s curvature <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

#### Limitations of Traditional NGD
Historically, [[Natural Gradient Descent | natural gradient descent]] has been rarely used in practice for large-scale training due to hardware limitations <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.
*   A single iteration of NGD is generally more computationally expensive than SGD or Adam <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
*   **Computational Complexity:** On digital computers, NGD typically incurs a cubic runtime (O(N^3)) and a quadratic memory cost (O(N^2)) relative to the model size <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. This makes it prohibitively slow for large models <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.

## The Role of New Hardware: Thermodynamic Computers
The ending of Moore's Law and Denard's Law for digital hardware presents an opportunity for specialized, unconventional hardware <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. [[Thermodynamic gradient descent | Thermodynamic computers]], also called probabilistic computers, are a new type of analog computer <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
*   Unlike digital computers that operate with ones and zeros <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>, or quantum computers that rely on quantum states of matter <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>, thermodynamic computers use the natural vibration of matter to perform computations <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.
*   These processes, like the dissipation of heat, are inherently well-suited for computations involving randomness, such as probabilistic and generative AI <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.
*   Companies like Normal Computing are developing these technologies, using a hybrid digital-analog system <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.

### Hybrid Digital-Analog System for [[Thermodynamic gradient descent | Thermodynamic Natural Gradient Descent]] (TGD)
The proposed [[Thermodynamic gradient descent | Thermodynamic Natural Gradient Descent]] (TGD) algorithm uses a hybrid system combining a GPU (digital) and a Stochastic Processing Unit (SPU) (analog/thermodynamic) <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
*   The GPU stores the model architecture, handles data loading, and calculates the first-order gradient and the Fisher matrix (or its components like Jacobian and Hessian) <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
*   This information is sent to the SPU via a Digital-to-Analog Converter (DAC) <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   The SPU then uses physical processes (vibration of atoms, dissipation of heat) to efficiently compute the second-order natural gradient <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   The calculated natural gradient is sent back to the GPU via an Analog-to-Digital Converter (ADC) <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   This process can occur asynchronously, as the "clock speed" of nature (molecule vibration) is incredibly fast compared to a GPU's clock speed <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
*   **Computational Complexity for TGD:** TGD drastically reduces the runtime and memory complexity of NGD from cubic/quadratic to linear (O(N)) <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>. This means NGD can now be performed at a computational cost similar to SGD on specialized hardware <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>.

### Intrinsic Momentum Effect
A fascinating discovery with TGD is an intrinsic momentum effect <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>.
*   In traditional SGD, momentum terms are explicitly added to help overcome local minima in the [[Loss Landscape | loss landscape]] <a class="yt-timestamp" data-t="01:13:09">[01:13:09]</a>. This involves storing a history of previous gradient steps <a class="yt-timestamp" data-t="01:14:22">[01:14:22]</a>.
*   With TGD, when a new batch of data is fed into the SPU, there's still residual thermal information (vibrations) from the previous batch <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>. This "heat memory" acts as a non-explicit momentum, allowing the system to implicitly retain information about the previous curvature and aid in convergence <a class="yt-timestamp" data-t="01:16:07">[01:16:07]</a>.

## Empirical Results and Future Outlook
The paper "Thermodynamic Natural Gradient Descent" demonstrates the superiority of TGD through numerical experiments <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **Tasks:** They tested TGD on a classification task (CNN on MNIST) and [[Latent diffusion model for neural networks | language model fine-tuning]] (LoRA for DistilBERT on Stanford Question Answering Dataset) <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>.
*   **Findings:** TGD generally achieves a lower loss faster than Adam/SGD in terms of iterations <a class="yt-timestamp" data-t="01:09:42">[01:09:42]</a>. For language modeling, a hybrid approach combining NGD with Adam updates gave the best performance <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.
*   **Simulation vs. Hardware:** It's important to note that these results were obtained using *simulated* thermodynamic computers, not necessarily the physical hardware itself <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>.
*   **Future:** The practical implications of TGD rely on the future availability and scalability of analog thermodynamic computers <a class="yt-timestamp" data-t="01:17:07">[01:17:07]</a>. While the concept is promising for efficiently training AI systems <a class="yt-timestamp" data-t="01:38:13">[01:38:13]</a>, the technology is still in its early stages (proof of concept) <a class="yt-timestamp" data-t="01:44:06">[01:44:06]</a>, with current systems being highly specialized and sensitive to external factors <a class="yt-timestamp" data-t="01:31:22">[01:31:22]</a>.