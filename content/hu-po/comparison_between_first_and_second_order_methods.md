---
title: Comparison between first and second order methods
videoId: Hxv_y_bI3zA
---

From: [[hu-po]] <br/> 

In the realm of machine learning, optimization algorithms are crucial for training models by minimizing a chosen loss function across a complex *loss landscape* <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. These algorithms can be broadly categorized into first-order and second-order methods, distinguished by the type of derivative information they utilize <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.

## Loss Landscape Explained
The *loss landscape* is a visualization where the "height" represents the value of the loss function for different combinations of a model's parameters <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. For a neural network with billions of parameters, this landscape exists in a high-dimensional space <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>. The goal of an optimizer is to find the *global minimum*, the lowest point in this landscape where the model's performance is optimal <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

## First Order Optimization Methods
First order methods are the most commonly used optimization algorithms in deep learning <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.

### Definition and Examples
First order methods primarily use the first derivative of the loss function, known as the *gradient* <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. This gradient indicates the "slope" or "velocity" of the *loss landscape* at a given point, guiding the model's parameters in the direction of steepest descent <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.

Common examples include:
*   Stochastic Gradient Descent (SGD) <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
*   Adam <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a> and its variants <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>

### Computational Efficiency
These methods are widely adopted due to their computational and memory efficiency on conventional digital hardware <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>.
*   **Runtime**: O(N), linear with respect to the number of parameters (N) <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>.
*   **Memory**: O(N), linear with respect to the number of parameters (N) <a class="yt-timestamp" data-t="00:52:15">[00:52:15]</a>.

### Limitations
While efficient, first order methods have limitations:
*   They are "blind" to the overall "curvature" of the *loss landscape* <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>, only considering the immediate slope <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   They can struggle with complex *loss landscapes* or get stuck in local minima <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   Achieving optimal performance often requires careful tuning of the learning rate, which determines the step size <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. This can involve techniques like *learning rate scheduling* <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.
*   Some first order methods, like Adam, incorporate "momentum" to help overcome local minima by maintaining a history of previous steps <a class="yt-timestamp" data-t="01:12:56">[01:12:56]</a>.

## Second Order Optimization Methods
[[second_order_optimization_in_machine_learning | Second order optimization]] methods leverage more sophisticated mathematical information about the *loss landscape*.

### Definition and Examples
[[second_order_optimization_in_machine_learning | Second order optimization]] methods utilize the second derivative of the loss function, which captures information about the "curvature" or "acceleration" of the *loss landscape* <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. This additional information allows for more informed and efficient parameter updates <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>.

*   **Natural Gradient Descent (NGD)**: A prominent [[second_order_optimization_in_machine_learning | second order method]] <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. NGD is equivalent to minimizing the Kullback-Leibler (KL) Divergence between probability distributions <a class="yt-timestamp" data-t="00:36:20">[00:36:20]</a>.
    *   NGD uses the *Fisher Information Matrix* (often shortened to "the Fisher") as a substitute for the *Hessian* matrix <a class="yt-timestamp" data-t="00:41:05">[00:41:05]</a>.
    *   The *Hessian* represents the second partial derivatives <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>, while the *Jacobian* represents the first partial derivatives <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>.
    *   The *empirical Fisher information matrix* is often used as an approximation when the true Fisher is not feasible <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>.
    *   The curvature matrix (e.g., Fisher or Hessian) must be positive semi-definite, meaning the optimal point can be a single point or a "channel" of points <a class="yt-timestamp" data-t="00:47:18">[00:47:18]</a>.

### Advantages
[[second_order_optimization_in_machine_learning | Second order methods]] offer theoretical advantages:
*   **Faster Convergence**: NGD requires fewer iterations than SGD to converge to the same loss value <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.
*   **Improved Navigation**: They can better navigate the curvature of complex *loss landscapes*, especially with models having many parameters <a class="yt-timestamp" data-t="00:43:35">[00:43:35]</a>.
*   **Larger Steps**: Access to curvature information allows for potentially larger, more informed gradient steps <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.

### Traditional Computational Cost
Despite their theoretical benefits, [[second_order_optimization_in_machine_learning | second order methods]] like NGD are rarely used in practice for large-scale training with conventional digital computers <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This is due to severe hardware limitations <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Runtime**: O(N^3), cubic with respect to the number of parameters <a class="yt-timestamp" data-t="00:52:31">[00:52:31]</a>.
*   **Memory**: O(N^2), quadratic with respect to the number of parameters <a class="yt-timestamp" data-t="00:52:34">[00:52:34]</a>.
This makes them computationally expensive and memory-intensive per iteration <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>.

## Thermodynamic Natural Gradient Descent (TNGD): A Game Changer
The emergence of specialized, unconventional hardware, such as thermodynamic computers, presents an opportunity to overcome the limitations of [[second_order_optimization_in_machine_learning | second order methods]] <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### What is Thermodynamic Computing?
Thermodynamic (or probabilistic) computers operate between conventional digital computers and quantum computers <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. They perform computation by exploiting natural processes, such as the vibration and dissipation of energy in matter (thermodynamic processes) <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This is sometimes described as an Orstein-Uhlenbeck process, a fancy way to refer to Brownian motion <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

### Hybrid Digital-Analog System
The proposed TNGD algorithm operates on a hybrid digital-analog architecture, combining a GPU with a Stochastic Processing Unit (SPU) <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>:
1.  **GPU's Role**: Stores the model architecture, processes mini-batches, calculates the first-order gradient, and provides initial information about the *Fisher* or *Hessian/Jacobian* matrices <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.
2.  **SPU's Role**: The SPU is the thermodynamic computer. It takes in digital information from the GPU via a Digital-to-Analog Converter (DAC) <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. The SPU then "evolves" by allowing its molecules to vibrate and settle towards an equilibrium state <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>, defined by a Boltzmann distribution relating energy and temperature <a class="yt-timestamp" data-t="00:55:31">[00:55:31]</a>.
3.  **Natural Gradient Estimation**: As the SPU reaches equilibrium, its state provides an estimate of the natural gradient <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>. This analog information is converted back to digital via an Analog-to-Digital Converter (ADC) and sent to the GPU for parameter updates <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>.
4.  **Asynchronous Operation**: The GPU and SPU can operate asynchronously, with the SPU's "nature clock speed" (molecular vibration) being significantly faster than the GPU's clock speed <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>. Crucially, numerical evidence shows that samples can be taken from the SPU even before perfect equilibrium is reached without significant performance degradation <a class="yt-timestamp" data-t="00:58:23">[00:58:23]</a>.

### Computational Efficiency of TNGD
This hybrid approach drastically reduces the computational and memory overhead traditionally associated with [[second_order_optimization_in_machine_learning | second order methods]] <a class="yt-timestamp" data-t="01:16:50">[01:16:50]</a>:
*   **Runtime**: O(N), similar to first-order methods <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>.
*   **Memory**: O(N), similar to first-order methods <a class="yt-timestamp" data-t="00:53:07">[00:53:07]</a>.

This makes [[second_order_optimization_in_machine_learning | Natural Gradient Descent]] feasible for large-scale AI model training <a class="yt-timestamp" data-t="00:53:15">[00:53:15]</a>.

### Inherent Momentum Effect
A fascinating discovery is that the non-zero delay time in the SPU (the time it takes for molecules to evolve) introduces a "momentum effect" <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>. The device retains residual thermal/vibrational information from previous batches, which propagates across iterations and acts as a non-explicit form of momentum, potentially allowing TNGD to outperform even pure NGD <a class="yt-timestamp" data-t="01:15:47">[01:15:47]</a>.

### Interpolation Between First and Second Order Methods
TNGD allows for a smooth interpolation between SGD and NGD simply by controlling the time the system is allowed to evolve <a class="yt-timestamp" data-t="01:01:11">[01:01:11]</a>.
*   **Zero Evolution Time (T=0)**: Effectively performs SGD (first order) <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>.
*   **Infinite Evolution Time (T=∞)**: Theoretically performs NGD (second order) <a class="yt-timestamp" data-t="01:01:55">[01:01:55]</a>.
In practice, a small, non-zero evolution time provides the benefits of [[second_order_optimization_in_machine_learning | second order optimization]].

## Current State and Future Outlook
While TNGD shows significant promise, it is still in its early stages:
*   **Proof of Concept**: The paper by Normal Computing demonstrates TNGD's superiority over state-of-the-art first and second order methods on classification tasks (e.g., ConvNet on MNIST) and language model fine-tuning (e.g., LoRA for DistilBERT on SQuAD) <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>.
*   **Simulated Results**: Importantly, these results are currently based on *simulated* thermodynamic computers, not necessarily actual hardware in all experiments <a class="yt-timestamp" data-t="01:18:52">[01:18:52]</a>.
*   **Hardware Development**: Building robust and scalable thermodynamic computers that don't require extensive thermal isolation remains a significant challenge <a class="yt-timestamp" data-t="01:31:17">[01:31:17]</a>. The slowest part of the current hybrid system is the digital-to-analog conversion <a class="yt-timestamp" data-t="01:04:51">[01:04:51]</a>.
*   **Geopolitical Implications**: Companies like Normal Computing and Xtropic are attracting investment not just for technical reasons, but also for the potential to develop chip manufacturing independent of current global dependencies, like Taiwan's TSMC <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.

The future of these [[second_order_optimization_in_machine_learning | second order methods]] enabled by new hardware is yet to be fully determined <a class="yt-timestamp" data-t="01:06:05">[01:06:05]</a>. They could become specialized tools for AI training data centers, or, if issues like thermal isolation are solved, revolutionize computing by enabling a new generation of ubiquitous, nature-based computers <a class="yt-timestamp" data-t="01:06:05">[01:06:05]</a>.