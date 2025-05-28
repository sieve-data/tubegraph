---
title: Second order optimization in machine learning
videoId: Hxv_y_bI3zA
---

From: [[hu-po]] <br/> 

[[optimization_methods_in_machine_learning | Second-order optimization]] methods are advanced techniques for training machine learning models that offer improved convergence properties compared to [[comparison_between_first_and_second_order_methods | first-order]] methods like Stochastic Gradient Descent (SGD) and Adam <a class="yt-timestamp" data-t="03:24:49">[03:24:49]</a>. While theoretically superior, their practical application has been limited due to significant hardware constraints and computational complexity <a class="yt-timestamp" data-t="03:28:30">[03:28:30]</a>.

## Limitations of Digital Hardware and First Order Methods

Conventional digital hardware, such as CPUs and GPUs, primarily relies on binary (ones and zeros) computations implemented with transistors on silicon <a class="yt-timestamp" data-t="07:34:50">[07:34:50]</a>. These systems are highly efficient for [[comparison_between_first_and_second_order_methods | first-order]] training but struggle with the demands of [[comparison_between_first_and_second_order_methods | second-order]] methods <a class="yt-timestamp" data-t="06:56:47">[06:56:47]</a>.

The widespread use of "simplistic optimizers" like SGD and Adam in deep learning is a direct consequence of these hardware limitations <a class="yt-timestamp" data-t="06:31:37">[06:31:37]</a>. While effective, these methods only consider the immediate slope (first derivative) of the loss landscape, leading to potentially slower convergence or issues like getting stuck in local minima <a class="yt-timestamp" data-t="17:45:06">[17:45:06]</a>.

The stagnation of Moore's Law, which predicts the exponential increase in transistors on a chip, has prompted a search for specialized, unconventional hardware to meet the growing demand for computation in AI <a class="yt-timestamp" data-t="04:41:43">[04:41:43]</a>.

## Understanding the Loss Landscape

The process of training a neural network involves minimizing a "loss function" across a "loss landscape" <a class="yt-timestamp" data-t="13:31:21">[13:31:21]</a>. This landscape represents the output of the loss function for every possible combination of a model's parameters <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>. The goal of gradient descent is to find the global minimum of this landscape <a class="yt-timestamp" data-t="14:19:07">[14:19:07]</a>.

*   **First-Order Methods:** These methods, like SGD, use the first derivative (gradient) to determine the direction of steepest descent, taking small steps towards a minimum <a class="yt-timestamp" data-t="17:45:06">[17:45:06]</a>. The "learning rate" dictates the size of these steps <a class="yt-timestamp" data-t="15:05:46">[15:05:46]</a>. A large learning rate can lead to overshooting the minimum, while a small one can result in slow training or getting trapped in local minima <a class="yt-timestamp" data-t="15:07:07">[15:07:07]</a>.
*   **Second-Order Methods:** In contrast, [[comparison_between_first_and_second_order_methods | second-order]] methods utilize the second derivative (curvature) of the loss landscape <a class="yt-timestamp" data-t="18:07:07">[18:07:07]</a>. This additional information allows for more informed and efficient steps, especially in complex, high-dimensional spaces where modern [[large_language_models_as_optimizers | Large Language Models]] operate <a class="yt-timestamp" data-t="18:50:56">[18:50:56]</a>. By understanding the curvature, these methods can navigate the landscape more effectively and achieve faster convergence <a class="yt-timestamp" data-t="43:34:49">[43:34:49]</a>.

## Key Matrices in Second Order Optimization

*   **Jacobian Matrix:** Represents all the first partial derivatives of a vector-valued function <a class="yt-timestamp" data-t="41:34:39">[41:34:39]</a>.
*   **Hessian Matrix:** Represents all the second partial derivatives of a function, capturing its curvature <a class="yt-timestamp" data-t="42:00:23">[42:00:23]</a>.
*   **Fisher Information Matrix (FIM) / The Fisher:** In natural gradient descent (NGD), the FIM acts as a substitute for the Hessian <a class="yt-timestamp" data-t="41:02:44">[41:02:44]</a>. Calculating the true FIM is often not feasible as it requires access to the underlying probability density function <a class="yt-timestamp" data-t="40:12:00">[40:12:00]</a>.
*   **Empirical Fisher Information Matrix:** An approximation of the FIM that can be computed from observed data <a class="yt-timestamp" data-t="42:23:09">[42:23:09]</a>.
*   **Curvature Matrix:** A general term for a matrix (like the Hessian or Fisher) that captures information about the loss landscape's curvature <a class="yt-timestamp" data-t="46:27:08">[46:27:08]</a>. For effective [[second_order_optimization_in_machine_learning | second-order optimization]], this matrix should ideally be "positive semi-definite," meaning the optimal point can be a single point or a continuous "channel" of points <a class="yt-timestamp" data-t="46:52:48">[46:52:48]</a>.

## Thermodynamic Natural Gradient Descent (TGD)

Normal Computing, a startup, introduced "Thermodynamic Natural Gradient Descent" (TGD) as a novel approach to leverage [[second_order_optimization_in_machine_learning | second-order optimization]] for [[finetuning_machine_learning_models | training machine learning models]] <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

### Probabilistic/Thermodynamic Computers
TGD relies on a new class of "thermodynamic" or "probabilistic" computers, which operate distinctively from both digital and quantum computers <a class="yt-timestamp" data-t="07:26:08">[07:26:08]</a>. Unlike digital computers with their binary states, or quantum computers that harness quantum states of matter, probabilistic computers leverage the natural vibrations and heat dissipation of matter (an Orstein-Uhlenbeck process) to perform computations <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. These processes are inherently well-suited for calculations involving randomness, such as those in probabilistic and generative AI <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.

### Hybrid Digital-Analog Architecture
The TGD algorithm utilizes a hybrid digital-analog loop involving a traditional GPU and a specialized "Stochastic Processing Unit" (SPU) <a class="yt-timestamp" data-t="03:48:58">[03:48:58]</a>.
*   **GPU's Role:** The GPU stores the model architecture, processes mini-batches, and calculates the initial gradient and the (empirical) Fisher Information Matrix (composed of Jacobian and Hessian components) <a class="yt-timestamp" data-t="26:09:47">[26:09:47]</a>.
*   **SPU's Role:** The SPU, the analog thermodynamic computer, receives these digital inputs via a Digital-to-Analog Converter (DAC) <a class="yt-timestamp" data-t="28:00:19">[28:00:19]</a>. It then performs the computationally intensive part of determining the [[second_order_optimization_in_machine_learning | natural gradient]] by allowing its physical system to evolve to an equilibrium state governed by a Boltzmann distribution <a class="yt-timestamp" data-t="55:25:31">[55:25:31]</a>. The result is then sent back to the GPU via an Analog-to-Digital Converter (ADC) <a class="yt-timestamp" data-t="28:16:04">[28:16:04]</a>.

A crucial advantage is that the SPU's evolution can occur asynchronously, allowing the GPU to continue other tasks while the SPU performs its natural computation <a class="yt-timestamp" data-t="28:44:00">[28:44:00]</a>.

### Computational Efficiency
The primary benefit of TGD is its drastic reduction in the computational complexity of [[second_order_optimization_in_machine_learning | natural gradient descent]]. On digital computers, NGD typically has a runtime complexity of O(N³) and memory complexity of O(N²), where N is the number of parameters <a class="yt-timestamp" data-t="52:28:42">[52:28:42]</a>. This makes it prohibitively expensive for large models. However, TGD, leveraging the SPU, achieves a linear O(N) runtime and memory cost, similar to [[comparison_between_first_and_second_order_methods | first-order]] methods like SGD and Adam <a class="yt-timestamp" data-t="53:01:00">[53:01:00]</a>. This makes [[second_order_optimization_in_machine_learning | second-order optimization]] practically feasible.

The "clock speed" of the SPU is determined by the fundamental speed at which molecules vibrate and heat dissipates, which is significantly faster than a GPU's clock speed <a class="yt-timestamp" data-t="59:04:00">[59:04:00]</a>. Furthermore, numerical evidence suggests that accurate estimates of the natural gradient can be obtained even before the SPU reaches full equilibrium, allowing for rapid iterations <a class="yt-timestamp" data-t="58:22:00">[58:22:00]</a>.

Interestingly, the duration for which the SPU is allowed to evolve (its "delay time") can act as an interpolation parameter:
*   A zero delay time effectively makes TGD behave like SGD <a class="yt-timestamp" data-t="01:01:51">[01:01:51]</a>.
*   An infinite delay time yields a pure [[second_order_optimization_in_machine_learning | natural gradient descent]] <a class="yt-timestamp" data-t="01:01:55">[01:01:55]</a>.
This allows for a tunable balance between [[comparison_between_first_and_second_order_methods | first-order]] and [[second_order_optimization_in_machine_learning | second-order]] behavior <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>.

### Inherent Momentum Effect
A fascinating property of TGD is its inherent "momentum effect" <a class="yt-timestamp" data-t="01:12:29">[01:12:29]</a>. In traditional optimizers, momentum terms explicitly store information about past gradient directions to help escape local minima <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. In TGD, when a new batch of data is fed to the SPU, there's a "little bit of leftover thermal heat or vibrational information" from the previous batch <a class="yt-timestamp" data-t="01:36:35">[01:36:35]</a>. This residual physical state acts as a non-explicit form of momentum, carrying information across iterations and potentially improving [[performance_and_efficiency_in_machine_learning_models | performance]] <a class="yt-timestamp" data-t="01:16:07">[01:16:07]</a>.

## Current Status and Future Outlook

While TGD presents a compelling theoretical advantage, its practical demonstration is still in early stages <a class="yt-timestamp" data-t="01:19:41">[01:19:41]</a>.
*   **Proof of Concept:** Current results are based on simulated TGD rather than actual hardware <a class="yt-timestamp" data-t="01:19:08">[01:19:08]</a>.
*   **Toy Problems:** The method has been tested on relatively simple tasks like MNIST classification (using a CNN) and [[finetuning_machine_learning_models | fine-tuning]] a DistilBERT model on a small question-answering dataset (Stanford Question Answering Dataset) <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>.
*   **Promising but Early:** In these toy problems, TGD generally achieves a lower loss faster than Adam <a class="yt-timestamp" data-t="01:09:37">[01:09:37]</a>. However, the gains are marginal and the "error bars" on the results indicate variability <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>.

The development of dedicated analog thermodynamic computers is crucial for the broader adoption of TGD <a class="yt-timestamp" data-t="01:17:07">[01:17:07]</a>. If scaled successfully, these chips could establish a significant market in [[energy_and_compute_optimization_in_ai_models | AI model training]]. The current slowest link in the hybrid system is the digital-to-analog and analog-to-digital conversion between the GPU and SPU <a class="yt-timestamp" data-t="01:04:46">[01:04:46]</a>, hinting at a potential future where all computations are performed in the probabilistic space <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>. This also ties into geopolitical considerations, as companies like Normal Computing and [[xtropical_machine_learning | Xtropic]] could offer a domestically sourced alternative for advanced computing, reducing reliance on foreign chip manufacturers <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

Despite its early stage, TGD represents a compelling direction for [[optimization_methods_in_machine learning | optimization methods in machine learning]], leveraging novel hardware paradigms to overcome long-standing computational barriers in [[second_order_optimization_in_machine_learning | second-order optimization]].