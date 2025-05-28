---
title: Second order optimization methods in machine learning
videoId: Hxv_y_bI3zA
---

From: [[hu-po]] <br/> 

Second order optimization methods offer improved convergence properties compared to traditional gradient descent techniques but are rarely used in practice due to hardware limitations <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This article explores a novel approach, Thermodynamic Natural Gradient Descent (TNGD), which leverages specialized analog hardware to overcome these limitations.

## The Challenge of Digital Hardware

Conventional digital hardware, such as GPUs and CPUs, primarily relies on first-order optimization methods like Stochastic Gradient Descent (SGD) and Adam, or their variants <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. These methods are efficient for digital computers but are limited to using the first derivative (slope) of the loss landscape <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

The scaling limits predicted by Moore's Law and Dennard's Law for digital hardware present an opportunity for specialized, unconventional hardware <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The increasing demand for compute in machine learning necessitates new approaches <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

### Understanding the Loss Landscape

When training a neural network, the goal is to minimize a loss function <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. This loss function can be visualized as a "loss landscape" where each point represents the loss value for a specific set of model parameters <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. The objective of optimization is to find the global minimum of this landscape <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.

*   **First Order Methods**: These methods only consider the immediate slope (first derivative) at the current point, moving in the direction of steepest descent <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. While simple, they can be slow and prone to getting stuck in local minima, especially in complex, high-dimensional loss landscapes <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Second Order Methods**: These methods incorporate information about the curvature (second derivative) of the loss landscape <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. This additional information allows for more informed and efficient steps, potentially leading to faster convergence and better navigation of complex loss surfaces <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.

Second order methods leverage the "Hessian matrix" (containing second order derivatives) or approximations like the "Fisher Information Matrix" <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>.

## Natural Gradient Descent (NGD)

Natural Gradient Descent (NGD) is a second-order optimization method that uses the Fisher Information Matrix (often referred to simply as the "Fisher") as a substitute for the Hessian <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>. The update rule for NGD involves the inverse of the Fisher Matrix multiplied by the loss gradient <a class="yt-timestamp" data-t="00:39:28">[00:39:28]</a>.

NGD requires fewer iterations to converge to the same loss value compared to SGD <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>. However, a single iteration of NGD is typically much more computationally expensive than SGD or Adam when implemented on digital computers <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. This is because calculating and inverting the Fisher Matrix scales poorly with the number of model parameters ($O(N^3)$ runtime and $O(N^2)$ memory), making it impractical for [[Large Language Models and Optimization | large AI models]] <a class="yt-timestamp" data-t="00:52:23">[00:52:23]</a>.

## Thermodynamic Computing: A Solution for NGD

A new class of hardware, termed "thermodynamic computers" or "probabilistic computers," offers a path to making NGD computationally feasible <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

*   **How They Work**: These are analog computers that perform computations by exploiting natural physical processes, such as the vibration of matter (atoms or molecules) in response to heat <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This process can be formally described as an Ornstein-Uhlenbeck process <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. They are suited for computations involving randomness, like probabilistic and generative AI <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Normal AI**: A startup called Normal Computing is pioneering this field <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. They describe their system as a "probabilistic computer" designed for "generative AI for critical Enterprise" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Hybrid Digital-Analog System**: Normal AI proposes Thermodynamic Natural Gradient Descent (TNGD), a hybrid digital-analog algorithm for training neural networks <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   A Graphics Processing Unit (GPU) stores the model architecture, provides gradients (first-order information), and handles data loading <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.
    *   A Stochastic Processing Unit (SPU), which is the thermodynamic computer, is used to efficiently compute the second-order natural gradient <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.
    *   The GPU and SPU communicate via digital-to-analog and analog-to-digital converters <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. The SPU is thermally insulated to prevent external interference with its vibrational processes <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>.
*   **Efficiency Gains**: This hybrid system allows NGD to achieve linear computational complexity ($O(N)$ runtime and memory) with respect to model size, matching the [[Efficiency and performance of finetuning methods | efficiency]] of SGD and Adam <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>. This is a significant improvement over the cubic runtime of traditional NGD implementations <a class="yt-timestamp" data-t="00:52:31">[00:52:31]</a>.
    *   The SPU computes by allowing its physical system to "evolve" and settle to an equilibrium state, defined by a Boltzmann distribution, which provides an estimate of the natural gradient <a class="yt-timestamp" data-t="00:55:07">[00:55:07]</a>.
    *   The "clock speed" of the SPU is determined by the speed of natural processes, which is significantly faster than the clock speed of a digital GPU <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>.
    *   Crucially, samples can be taken from the SPU even before full equilibrium is reached without significantly harming performance <a class="yt-timestamp" data-t="00:58:22">[00:58:22]</a>.
*   **Geopolitical Implications**: The development of these specialized chips, particularly by U.S.-based companies like Normal Computing (which uses Texas Instruments chips <a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>), could reduce reliance on offshore chip manufacturing, addressing geopolitical concerns <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.

### The Momentum Effect

An interesting finding in TNGD is that a non-zero time delay in reading the SPU's state can actually improve performance <a class="yt-timestamp" data-t="01:00:11">[01:00:11]</a>. This delay appears to have a "momentum effect" <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>.

In traditional optimizers like Adam, momentum terms are explicitly added to accumulate a history of past gradients, helping to overcome local minima where the current gradient might be small <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. In TNGD, when a new batch of data is fed into the SPU, there's a residual thermal or vibrational information from the previous batch <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>. This "heat memory" provides a physical, implicit form of momentum, guiding the optimization process across iterations <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>.

Furthermore, TNGD offers a "smooth interpolation" between SGD and NGD, allowing users to choose the desired balance between first and second-order optimization by adjusting the time allowed for the SPU to evolve <a class="yt-timestamp" data-t="01:01:08">[01:01:08]</a>.

## Current State and Future Outlook

While promising, the technology is still in its early stages <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>. The paper from Normal Computing demonstrates TNGD's superiority over state-of-the-art first and second-order methods on classification tasks (e.g., a convolutional neural network on MNIST) and [[Techniques for Efficient Model FineTuning | language model fine-tuning]] (e.g., DistilBERT on a question-answering dataset) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a> <a class="yt-timestamp" data-t="01:10:18">[01:10:18]</a>. However, these are considered "toy problems" and the results are currently based on simulations rather than actual hardware usage <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>.

The practical implications of TNGD depend on the future availability and scalability of analog thermodynamic computers <a class="yt-timestamp" data-t="01:17:06">[01:17:06]</a>. The slowest part of the current hybrid system is the conversion between analog and digital information <a class="yt-timestamp" data-t="01:04:46">[01:04:46]</a>. This suggests that the future might involve either highly specialized data centers for AI training or, potentially, a complete shift of the entire technical stack to thermodynamic computing in the long term <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>.