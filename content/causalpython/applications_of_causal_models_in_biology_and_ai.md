---
title: Applications of causal models in biology and AI
videoId: gazCIKYEv44
---

From: [[causalpython]] <br/> 

Causal models play a crucial role in understanding complex systems, from natural phenomena to artificial intelligence. Dr. Robert Ness, a senior researcher at Microsoft Research, highlights their application in biology, particularly in [[causal discovery and inference in AI | causal discovery]] and experimental design, and their growing importance in advancing artificial intelligence, including decision-making and generative models.

## Causal Models in Biology

Dr. Ness's journey into [[Causal AI and its application in different sciences | causal modeling]] was significantly influenced by his background in economics and statistics, which led him to systems biology during his PhD. His preference for natural sciences over financial markets stemmed from the idea of "ground truth" – the belief that in natural sciences, there's an underlying reality being modeled, even if the model is an approximation <a class="yt-timestamp" data-t="04:09:11">[04:09:11]</a>. He sought to work with complex and dynamic systems, aiming to build models that simulate natural processes like the workings of a cell <a class="yt-timestamp" data-t="04:34:37">[04:34:37]</a>.

During his PhD, Dr. Ness was introduced to the task of using [[causal discovery and inference in AI | causal discovery algorithms]] (also known as structure learning) to reconstruct biological pathways, specifically signal transduction pathways, from single-cell data <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

### Challenges and Solutions

A main challenge was to build tools that were practically useful to biologists and laboratory analysts, beyond just generating a causal directed acyclic graph (DAG) <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>. Biologists typically don't just want a DAG; they want to use it for purposes like learning new biomarkers, drug discovery, or understanding previously unknown signaling pathways <a class="yt-timestamp" data-t="07:07:10">[07:07:10]</a>.

To address this, Dr. Ness focused on integrating [[causal discovery and inference in AI | causal discovery]] with experimental design <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>. This involved using Bayesian experimental design methods where the DAG is an intermediate step to a final outcome, dealing with uncertainty and guiding decisions on what and how much to measure in a sequential workflow <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>. This approach aimed to automate processes for biological and molecular biology research goals <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.

### Evaluating Causal Structures

Initially, evaluation involved comparing learned graphs to known ground truth graphs using metrics like precision-recall or structural Hamming distance <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>. However, when the ground truth model is unknown, Bayesian reasoning was employed to:
*   Deal with uncertainty <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.
*   Incorporate prior knowledge about the system's size, shape, or disallowed interactions (e.g., certain proteins never interacting) <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>.
This method provides guarantees that, with more data and specific evaluation criteria, the model will move towards the correct answer even without knowing the exact ground truth <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>.

## Causal Models in Artificial Intelligence

### Causal Decision Making and Reinforcement Learning

[[Causal AI and machine learning intersection | Causal decision theory]] contrasts with empirical decision theory, emphasizing attending to the consequences of actions rather than just maximizing expected utility conditional on interaction <a class="yt-timestamp" data-t="11:12:00">[11:12:00]</a>. While traditional approaches might lead to suboptimal results in certain scenarios (like Newcomb's Problem), a mature understanding of causal models allows their incorporation into automated decision theory <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.

Examples include:
*   [[Causal AI and machine learning intersection | Causal Bandits]]: Applying causal knowledge to optimization in systems with unknown or adversarial causal factors <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.
*   [[Causal AI and machine learning intersection | Causal Reinforcement Learning]] (RL):
    *   **Sample Efficiency**: Using causal assumptions to learn models more efficiently in high-dimensional settings, making otherwise intractable problems tractable <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>.
    *   **Credit Assignment**: Understanding why a policy led to a certain outcome, using methods like attribution or root cause analysis from [[Causality in AI | causal inference]] <a class="yt-timestamp" data-t="13:24:00">[13:24:00]</a>.

Traditional deep reinforcement learning often models everything as a Markov Decision Process, folding all information into a "state" variable and ignoring causal nuances <a class="yt-timestamp" data-t="17:31:00">[17:31:00]</a>. While this is often sufficient for maximizing reward, it can lead to suboptimal decisions when actions change the environment in ways not captured by simple state transitions <a class="yt-timestamp" data-t="18:35:00">[18:35:00]</a>. [[Causal reasoning in artificial intelligence | Causality]] helps identify when these differences occur <a class="yt-timestamp" data-t="18:40:00">[18:40:00]</a>. Furthermore, conditioning on certain data can be detrimental due to biases like colliders or mediators, a consideration often overlooked in traditional RL <a class="yt-timestamp" data-t="20:28:00">[20:28:00]</a>.

It's crucial to identify practical scenarios where [[Causality in AI | causal models]] are *necessary* rather than just helpful for toy problems <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>. For example, the optimal action that maximizes expected reward might be the same whether considered associatively or interventionally <a class="yt-timestamp" data-t="24:22:00">[24:22:00]</a>. The challenge is to identify cases where the optimal action for an *interventional* outcome differs from a purely associative one, and to demonstrate this in real-world contexts like robotics or protein folding <a class="yt-timestamp" data-t="25:55:00">[25:55:00]</a>. [[Causal AI and its application in different sciences | Causal analysis]] provides clear guidelines for when traditional methods might be error-prone or lead to different, suboptimal outcomes <a class="yt-timestamp" data-t="26:51:00">[26:51:00]</a>.

### Human-like Causal Reasoning and AGI

For Artificial General Intelligence (AGI), the ability to reason about cause and effect is paramount <a class="yt-timestamp" data-t="29:45:00">[29:45:00]</a>. This involves drawing inspiration from computational psychology, where human reasoning abilities are modeled computationally <a class="yt-timestamp" data-t="30:10:00">[30:10:00]</a>. [[Causal reasoning in artificial intelligence | Causal inference theory]] provides the framework to specify assumptions and inductive biases that allow conclusions beyond what observed data alone can provide <a class="yt-timestamp" data-t="31:16:00">[31:16:00]</a>.

A key distinction arises between answering objective causal questions (e.g., "Does this drug treat this illness?") and emulating human reasoning, which might include cognitive biases or inaccurate heuristics <a class="yt-timestamp" data-t="33:18:00">[33:18:00]</a>. While objective truth is crucial for scientific and engineering applications, capturing human-like reasoning, even with its imperfections, is important for developing AGI <a class="yt-timestamp" data-t="34:16:00">[34:16:00]</a>. The ability to model these biases and then potentially "turn them off" in deployed algorithms would be a powerful advancement <a class="yt-timestamp" data-t="34:51:00">[34:51:00]</a>.

One example of human cognitive bias relevant to [[causal reasoning in artificial intelligence | causal AI]] is the tendency to engage in less counterfactual simulation for the absence of actions or events (e.g., "failing to maintain a machine") compared to actions that did happen (e.g., "breaking a machine") <a class="yt-timestamp" data-t="35:55:00">[35:55:00]</a>. Algorithmically addressing this could involve scoping out negative events to make counterfactual reasoning easier <a class="yt-timestamp" data-t="37:15:00">[37:15:00]</a>.

### Advancements in Causal Modeling with Probabilistic Programming

A paper co-authored by Dr. Ness demonstrated that if a causal quantity is identifiable using the do-calculus (a graphical identification framework), then implementing this system in a probabilistic programming framework (like PyMC or Pyro) guarantees unbiased estimation of the [[application of causal machine learning in medicine | causal effect]] <a class="yt-timestamp" data-t="39:19:00">[39:19:00]</a>. This bridges the gap for model-based machine learning practitioners, showing that their latent variable models can be used for [[Causal reasoning in AI | causal inference]] provided the causal identification is proven <a class="yt-timestamp" data-t="41:01:00">[41:01:00]</a>. Libraries like `y0` in Python can programmatically verify identifiability <a class="yt-timestamp" data-t="41:25:00">[41:25:00]</a>.

The newly released Cairo library (built on Pyro) further abstracts complex [[Causal AI and machine learning intersection | causal inference]] operations, making it easier to work with concepts like parallel world counterfactual reasoning in structural causal models <a class="yt-timestamp" data-t="47:30:00">[47:30:00]</a>. Cairo emphasizes the parallel between causal uncertainty and Bayesian uncertainty, making [[Causality in AI | causality]] more accessible to probabilistic machine learning practitioners <a class="yt-timestamp" data-t="48:10:00">[48:10:00]</a>.

### Future Directions: Causal Representation Learning and Generative AI

The next "big thing" in [[Causality in AI | causality]] is likely [[advancements in causal modeling and AI | causal representation learning]] <a class="yt-timestamp" data-t="49:48:00">[49:48:00]</a>. This involves learning latent representations that directly correspond to true causes in the data-generating process. [[Causality in AI | Causal principles]] (like modularity and invariance under intervention) can guide the learning of these abstractions, enabling theoretically sound and practically useful models <a class="yt-timestamp" data-t="50:04:00">[50:04:00]</a>.

A compelling example is generative AI (e.g., Midjourney, Stable Diffusion) <a class="yt-timestamp" data-t="51:02:00">[51:02:00]</a>. Users often want to make precise, localized changes (e.g., "blue glasses instead of red glasses") without unintended side effects <a class="yt-timestamp" data-t="51:30:00">[51:30:00]</a>. This is a counterfactual question: "What would this image look like if the glasses were red, and nothing else changed *except what is causally downstream* of the glasses color?" Current models struggle with this, often introducing artifacts <a class="yt-timestamp" data-t="52:21:00">[52:21:00]</a>. If generative models could operate semantically on learned [[Causal AI and machine learning intersection | causal representations]], they would offer users intuitive "knobs" for precise control, similar to editing text in an LLM <a class="yt-timestamp" data-t="53:23:00">[53:23:00]</a>.

### Large Language Models (LLMs) and Causality

The question of whether Large Language Models learn a "world model" often refers to whether they learn a Structural Causal Model <a class="yt-timestamp" data-t="55:00:00">[55:00:00]</a>. The Causal Hierarchy Theorem (Pearl's Causal Ladder) states that answering causal questions at higher levels of abstraction (interventions, counterfactuals) requires assumptions at that same level <a class="yt-timestamp" data-t="55:50:00">[55:50:00]</a>.
*   **Level 1: Associational** (observational statistics) <a class="yt-timestamp" data-t="56:06:00">[56:06:00]</a>
*   **Level 2: Interventions** (causal effects, requiring a causal DAG) <a class="yt-timestamp" data-t="56:08:00">[56:08:00]</a>
*   **Level 3: Counterfactuals** (reasoning across worlds, requiring an SCM) <a class="yt-timestamp" data-t="56:11:00">[56:11:00]</a>

While LLMs can empirically answer causal and counterfactual questions, they often "hallucinate" <a class="yt-timestamp" data-t="57:44:00">[57:44:00]</a>. To ensure reliable causal answers, the necessary level-three assumptions must exist either in the training data (unlikely given how current models are trained), the model architecture, parameterization, or the prompt itself <a class="yt-timestamp" data-t="58:43:00">[58:43:00]</a>.

Dr. Ness's research explores incorporating [[Causal AI and its application in different sciences | causal information]] directly into the Transformer architecture, aiming for theoretical guarantees similar to those obtained with latent variable models <a class="yt-timestamp" data-t="01:00:06">[01:00:06]</a>. This includes using structural knowledge (e.g., a "three-act structure" in film scripts) to enable the model to simulate outcomes not seen in training data <a class="yt-timestamp" data-t="01:11:09">[01:11:09]</a>. The goal is not just causal correctness but to provide "knobs" that align models with human abstract thinking, augmenting human creativity <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

This approach signifies a shift from merely scaling models with more data to leveraging inherent structure and depth in data (e.g., GitHub repo history and execution traces for code generation), potentially enabling GPT-4 level capabilities with smaller datasets <a class="yt-timestamp" data-t="01:03:18">[01:03:18]</a>. This future involves recognizing that the past, present, and future are inherently causal <a class="yt-timestamp" data-t="01:06:02">[01:06:02]</a>.