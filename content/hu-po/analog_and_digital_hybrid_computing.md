---
title: Analog and digital hybrid computing
videoId: Hxv_y_bI3zA
---

From: [[hu-po]] <br/> 

Analog and digital hybrid computing represents a novel approach to overcome the limitations of conventional digital hardware in training advanced AI models <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This emerging paradigm, championed by companies like Normal Computing, leverages the strengths of both digital and analog processing units to achieve more efficient optimization methods <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## Introduction to Thermodynamic Natural Gradient Descent (TNGD)

The core of this advancement is the **Thermodynamic Natural Gradient Descent (TNGD)** algorithm <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This algorithm, detailed in a paper released on May 22, 2024, by Normal Computing, presents a new [[hybrid_architectures_and_transformer_block_efficiency | hybrid digital-analog algorithm]] for training neural networks that is equivalent to Natural Gradient Descent (NGD) <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>, <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

Traditional deep learning relies on simplistic optimizers like Stochastic Gradient Descent (SGD) and Adam due to hardware limitations <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. These are first-order methods <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, meaning they only consider the immediate slope (first derivative) of the loss landscape to determine the direction of optimization <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. Second-order methods, like NGD, account for the curvature (second derivative) of the loss landscape, offering potentially faster and more efficient convergence to optimal parameters <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>, <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.

However, a single iteration of NGD is typically more computationally expensive than SGD or Adam on digital computers <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. This is why NGD has been rarely used in practice for large-scale training <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.

## The Role of Thermodynamic (Probabilistic) Computers

[[future_of_thermodynamic_computing | Thermodynamic computers]], also known as probabilistic computers, are positioned between traditional digital computers and [[quantum_computing_advancements | quantum computers]] <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>, <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.
*   **Digital computers** operate on ones and zeros, implemented with transistors on silicon <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Quantum computers** rely on quantum states of matter and wave functions <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Thermodynamic computers** utilize the natural phenomenon of matter vibration and heat dissipation to perform computations, particularly excelling at tasks involving randomness, such as probabilistic and generative AI <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>, <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. This is described by processes like the Orstein-Uhlenbeck process, a fancy term for Brownian motion <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

TNGD, designed for these specialized machines, aims to achieve the computational efficiency of a first-order training method while still accounting for the curvature of the loss landscape with a second-order method <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

## Hybrid Architecture: GPU and SPU

The TNGD approach utilizes a [[hybrid_architectures_and_transformer_block_efficiency | hybrid digital-analog architecture]] comprising a Graphics Processing Unit (GPU) and a Stochastic Processing Unit (SPU) <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>, <a class="yt-timestamp" data-t="00:48:58">[00:48:58]</a>.

*   **GPU (Digital Component):** Stores the model architecture, handles data loading, mini-batches, and provides the initial gradient and Fisher Information Matrix (or its components like Jacobian and Hessian) <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>, <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>. It uses standard digital tools like PyTorch <a class="yt-timestamp" data-t="01:06:53">[01:06:53]</a>.
*   **SPU (Analog/Thermodynamic Component):** This unit is designed to efficiently compute the second-order terms, specifically the natural gradient, by exploiting natural physical processes <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>, <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>.
    *   The SPU is thermally insulated to prevent external factors from interfering with its sensitive operations <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>, <a class="yt-timestamp" data-t="01:06:17">[01:06:17]</a>.
    *   Information is transferred between the GPU and SPU using Digital-to-Analog (DAC) and Analog-to-Digital (ADC) converters <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>.
    *   The SPU computes by allowing its internal molecular system to "evolve" or dissipate heat, reaching an equilibrium state governed by a Boltzmann distribution <a class="yt-timestamp" data-t="00:55:07">[00:55:07]</a>, <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>.
    *   This process can occur asynchronously, as the "clock speed of nature" (the speed at which atoms vibrate and heat dissipates) is significantly faster than a GPU's clock speed <a class="yt-timestamp" data-t="00:59:04">[00:59:04]</a>, <a class="yt-timestamp" data-t="00:59:40">[00:59:40]</a>.

### Computational Efficiency

The primary advantage of TNGD on this [[hybrid_architectures_and_transformer_block_efficiency | hybrid architecture]] lies in its drastically reduced computational complexity <a class="yt-timestamp" data-t="00:53:15">[00:53:15]</a>.

| Method                    | Runtime Complexity (per iteration) | Memory Complexity      |
| :------------------------ | :--------------------------------- | :--------------------- |
| SGD / Adam (First Order)  | O(N)                               | O(N)                   |
| NGD (Digital Computer)    | O(N³)                              | O(N²)                  |
| TNGD (Hybrid Analog-Digital) | O(N)                               | O(N) (Construction & Storage) |

*N* represents the number of trainable parameters in the model <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a>. This linear scaling for TNGD makes second-order optimization feasible for large [[transformerbased_model_architectures | transformer-based model architectures]] <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>.

### The Loss Landscape and Second-Order Methods

The goal of training a neural network is to minimize a loss function, which can be visualized as navigating a "loss landscape" in a high-dimensional space <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>, <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>.

*   **First-order methods** like SGD take steps based only on the immediate slope (gradient) <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.
*   **Second-order methods** incorporate information about the curvature (e.g., using the Hessian or Fisher Information Matrix) <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. This allows for more informed and potentially larger steps, leading to faster convergence, especially in complex loss surfaces <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.

### Intrinsic Momentum Effect

Intriguingly, the TNGD system exhibits a "momentum effect" <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>. While conventional optimizers explicitly store and apply a momentum vector from previous steps to avoid getting stuck in local minima <a class="yt-timestamp" data-t="01:13:06">[01:13:06]</a>, the thermodynamic computer inherently retains some residual "thermal information" from previous data batches <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>. This leftover vibrational energy from the SPU effectively acts as a form of non-explicit momentum, allowing the system to continue moving in a general direction even if the immediate gradient flattens out <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>.

## Industry Landscape and Geopolitical Implications

Normal Computing is a startup operating in the [[future_of_thermodynamic_computing | thermodynamic computing]] space, having recently emerged from "stealth mode" <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. Unlike some secretive companies like Extropic, Normal Computing actively publishes its research papers and open-sources its code on GitHub <a class="yt-timestamp" data-t="01:02:49">[01:02:49]</a>.

This field also has significant geopolitical implications. With the ending of Moore's Law and Denard's Law for digital hardware, there's a push for specialized, unconventional hardware <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Companies like Normal Computing, by using chips from US-based manufacturers like Texas Instruments (which has fabs in the US), offer a pathway for developing chip technology that is geopolitically dependable and reduces reliance on foreign fabs, such as those in Taiwan <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.

## Current Status and Future Outlook

While TNGD shows promise, the technology is still in early development <a class="yt-timestamp" data-t="01:19:41">[01:19:41]</a>.
*   **Simulated Results:** The current demonstrated superiority of TNGD over state-of-the-art digital first- and second-order training methods (on tasks like MNIST classification and DistilBERT fine-tuning) comes from *simulated* environments, not direct hardware implementations <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>, <a class="yt-timestamp" data-t="01:19:21">[01:19:21]</a>.
*   **Toy Problems:** The experiments are conducted on relatively simple "toy problems" (e.g., ConvNet on MNIST, LoRA for DistilBERT on a small question-answering dataset) <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>, <a class="yt-timestamp" data-t="01:10:24">[01:10:24]</a>. It remains to be seen how it scales to training large, [[stateoftheart_video_generation_and_multimodal_models | state-of-the-art multimodal models]] <a class="yt-timestamp" data-t="01:13:30">[01:13:30]</a>.
*   **Slowest Link:** Currently, the slowest part of the hybrid system is the digital-to-analog and analog-to-digital conversion between the GPU and SPU <a class="yt-timestamp" data-t="01:04:44">[01:04:44]</a>.

The practical implications of TNGD rely on the future availability and scalability of analog thermodynamic computers <a class="yt-timestamp" data-t="01:17:06">[01:17:06]</a>. It's uncertain if these will become ubiquitous consumer technologies or remain specialized tools for data centers and AI training <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>. Despite the early stage, the ability to efficiently perform second-order optimization for AI models presents a significant opportunity for this new class of hardware <a class="yt-timestamp" data-t="01:38:05">[01:38:05]</a>.