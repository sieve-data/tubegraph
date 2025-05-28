---
title: Future of thermodynamic computing
videoId: Hxv_y_bI3zA
---

From: [[hu-po]] <br/> 

Thermodynamic computing, also known as probabilistic computing, represents a new paradigm in hardware that could significantly impact the future of artificial intelligence (AI) and machine learning (ML) training <a class="yt-timestamp" data-t="01:13:09">[01:13:09]</a>. This emerging field is positioned between traditional digital computers and advanced quantum computers <a class="yt-timestamp" data-t="07:26:07">[07:26:07]</a>.

## Introduction to Thermodynamic Computing

[[thermodynamic_natural_gradient_descent | Thermodynamic computing]] utilizes natural processes, specifically the vibration of matter and the dissipation of heat, to perform computations <a class="yt-timestamp" data-t="08:50:47">[08:50:47]</a>. These "stochastic processing units" (SPUs) are well-suited for tasks involving randomness, such as probabilistic and generative AI <a class="yt-timestamp" data-t="09:11:03">[09:11:03]</a>. The underlying physical process is described as an Orstein-Uhlenbeck process, which is akin to Brownian motion <a class="yt-timestamp" data-t="01:12:28">[01:12:28]</a>.

Companies like Normal Computing are at the forefront of this technology, having recently emerged from stealth mode <a class="yt-timestamp" data-t="05:59:58">[05:59:58]</a>. Another notable company in this space is Extropic <a class="yt-timestamp" data-t="09:55:04">[09:55:04]</a>.

## Addressing Digital Hardware Limitations

The pursuit of new computing paradigms is driven by the perceived end of Moore's Law and Dennard's Law for digital hardware <a class="yt-timestamp" data-t="04:41:41">[04:41:41]</a>. Digital computers face fundamental limits as transistors cannot be made infinitely smaller <a class="yt-timestamp" data-t="05:14:02">[05:14:02]</a>. As the demand for compute continues to grow, specialized unconventional hardware becomes necessary <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.

Currently, most deep learning models rely on simplistic optimizers like Stochastic Gradient Descent (SGD) and Adam, largely due to the limitations of digital computers in efficiently performing second-order training methods <a class="yt-timestamp" data-t="06:26:02">[06:26:02]</a>.

## Advantages in AI Training: Second-Order Optimization

Thermodynamic computers offer a significant advantage by efficiently performing second-order optimization methods, specifically [[thermodynamic_natural_gradient_descent | Natural Gradient Descent (NGD)]] <a class="yt-timestamp" data-t="07:08:29">[07:08:29]</a>. While NGD converges in fewer iterations than SGD <a class="yt-timestamp" data-t="02:22:52">[02:22:52]</a>, a single iteration on a digital computer is computationally expensive (O(N^3) runtime and O(N^2) memory cost, where N is the number of parameters) <a class="yt-timestamp" data-t="05:26:07">[05:26:07]</a>.

This is where [[thermodynamic_natural_gradient_descent | thermodynamic computing]] shines. It allows NGD to operate with a linear runtime and memory complexity (O(N)), similar to SGD <a class="yt-timestamp" data-t="05:31:01">[05:31:01]</a>. This drastic reduction in computational overhead is a key factor for its future potential in training large AI models <a class="yt-timestamp" data-t="01:16:46">[01:16:46]</a>.

Second-order methods are crucial for navigating complex loss landscapes, which become more intricate as models grow to billions of parameters <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. They utilize information about the curvature of the loss landscape, allowing for more efficient optimization <a class="yt-timestamp" data-t="00:43:56">[00:43:56]</a>.

A unique feature of thermodynamic computers is their inherent "momentum effect" <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>. As new batches of data are fed, residual thermal information from previous batches remains, effectively acting as a non-explicit momentum term that helps overcome local minima <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>. This allows for smoother and potentially faster convergence.

## Hybrid Digital-Analog Systems

Current [[thermodynamic_natural_gradient_descent | thermodynamic computing]] systems operate in a hybrid digital-analog loop <a class="yt-timestamp" data-t="03:05:08">[03:05:08]</a>. A conventional GPU stores the model architecture, calculates the gradient and Fisher information Matrix, and handles data loading <a class="yt-timestamp" data-t="02:50:39">[02:50:39]</a>. This information is then sent to the analog thermodynamic computer (SPU) via a Digital-to-Analog Converter (DAC) <a class="yt-timestamp" data-t="02:59:58">[02:59:58]</a>. The SPU evolves by letting its molecules vibrate, effectively performing linear algebra computations based on thermodynamic processes <a class="yt-timestamp" data-t="09:16:11">[09:16:11]</a>. An estimate of the natural gradient is then sent back to the GPU via an Analog-to-Digital Converter (ADC) <a class="yt-timestamp" data-t="02:56:06">[02:56:06]</a>.

The "clock speed" of the SPU is determined by the speed at which molecules vibrate and dissipate heat, which is "incredibly fast" <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>. This asynchronous operation allows the GPU to continue its tasks while the SPU calculates the second-order gradient <a class="yt-timestamp" data-t="02:52:16">[02:52:16]</a>. Furthermore, numerical evidence suggests that accurate estimates of the natural gradient can be obtained even before the system reaches full equilibrium, significantly boosting practicality <a class="yt-timestamp" data-t="00:58:22">[00:58:22]</a>.

This hybrid approach also allows for a "smooth interpolation" between SGD and NGD by adjusting the time the system is allowed to evolve <a class="yt-timestamp" data-t="01:01:11">[01:01:11]</a>.

## Current State and Challenges

Thermodynamic computing is in its very early stages of development <a class="yt-timestamp" data-t="01:19:41">[01:19:41]</a>. Current demonstrations are proofs of concept, not production setups <a class="yt-timestamp" data-t="03:06:06">[03:06:06]</a>. For instance, Normal Computing's paper primarily used *simulated* thermodynamic gradient descent for its performance comparisons, rather than a physical device <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>. This aligns with [[simulated_versus_real_quantum_computing | quantum computing advancements]], where simulated results often precede real hardware performance <a class="yt-timestamp" data-t="01:19:15">[01:19:15]</a>.

Key challenges include:
*   **Thermal Isolation**: SPUs are extremely sensitive to external perturbations, requiring specialized thermal insulation systems <a class="yt-timestamp" data-t="02:04:14">[02:04:14]</a>.
*   **Digital-to-Analog Conversion**: The slowest link in the current hybrid system is the conversion of analog thermodynamic information back into digital data for the GPU <a class="yt-timestamp" data-t="01:04:46">[01:04:46]</a>.
*   **Proof of Scale**: While promising for toy problems (like classifying MNIST or fine-tuning DistilBERT on a small dataset) <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>, scaling these systems to train frontier models (e.g., Llama 4) remains to be demonstrated <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>.

Companies like Normal Computing are publicly sharing their work on platforms like GitHub <a class="yt-timestamp" data-t="01:02:45">[01:02:45]</a>, while others like Extropic operate in stealth mode, which may hinder collaborative progress <a class="yt-timestamp" data-t="01:02:50">[01:02:50]</a>.

## Future Outlook and Market Potential

The future of thermodynamic computing holds significant promise, particularly for [[future_trends_in_machine_learning_software_and_hardware | training AI models efficiently]] <a class="yt-timestamp" data-t="01:33:51">[01:33:51]</a>. The ability to perform second-order optimization with linear complexity could drastically reduce training times for large models.

**Potential Market Scenarios**:
1.  **Specialized Data Centers**: Due to thermal isolation challenges, thermodynamic chips might remain specialized hardware primarily used in data centers for AI training, rather than becoming ubiquitous consumer devices <a class="yt-timestamp" data-t="01:05:54">[01:05:54]</a>. This could lead to a bifurcation of computing, with specialized training computers (potentially hybrid) and digital inference computers (like Groq) <a class="yt-timestamp" data-t="01:23:51">[01:23:51]</a>.
2.  **Ubiquitous Adoption**: In a more distant future (potentially 50 years), if thermal isolation and other challenges are overcome, thermodynamic computers could replace digital computers entirely, becoming the foundation of all computing <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>. However, this is uncertain.

**Geopolitical Implications**:
The development of thermodynamic computing could also play a role in geopolitical strategies related to chip manufacturing <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>. By potentially allowing for the development of fabrication capabilities entirely within countries like the US (e.g., using Texas Instruments chips, which are made in the US <a class="yt-timestamp" data-t="03:31:34">[03:31:34]</a>), it could reduce reliance on foreign fabs, such as TSMC in Taiwan <a class="yt-timestamp" data-t="03:32:16">[03:32:16]</a>. This strategic independence makes these startups attractive to investors <a class="yt-timestamp" data-t="03:39:53">[03:39:53]</a>.

The future of this technology remains to be seen, but its potential for [[energy_and_compute_optimization_in_ai_models | optimizing AI training]] and its unique physical computing approach position it as a significant area to watch <a class="yt-timestamp" data-t="01:38:09">[01:38:09]</a>.