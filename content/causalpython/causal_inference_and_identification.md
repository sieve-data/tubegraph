---
title: Causal Inference and Identification
videoId: gazCIKYEv44
---

From: [[causalpython]] <br/> 

[[Causal inference concepts and applications | Causal inference]] involves reasoning about cause and effect relationships <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>. A key concept within this field is **identification**, which refers to whether a causal effect can be uniquely determined from observed data given a specific causal model <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## The Importance of Identification

Without identification, the quantity one is trying to optimize and the quantity being optimized are different, leading to very error-prone scenarios <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. In such cases, if a causal effect is not identified, traditional methods might lead to suboptimal decisions <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

## Identification through Causal Models

[[Causal Discovery and Analysis | Causal models]], often represented as Directed Acyclic Graphs (DAGs), provide the assumptions necessary to determine if a causal effect is identifiable <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>, <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. The structure of a causal DAG specifies direct relationships between state, action, and reward over time <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.

The process of identification involves using data (observational or experimental) to learn the causal properties of a system, typically the structure of a causal DAG <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### The Role of Do-Calculus

The **do-calculus** is a formal framework used to prove whether an intervention distribution (the effect of an action) is identifiable from observational data <a class="yt-timestamp" data-t="00:39:36">[00:39:36]</a>. If a model's intervention distribution is identified by the do-calculus or another graphical identification framework, then sampling procedures from that model are valid <a class="yt-timestamp" data-t="00:39:36">[00:39:36]</a>. This means if a quantity is identifiable using do-calculus, an unbiased estimate of the causal effect can be produced <a class="yt-timestamp" data-t="00:42:08">[00:42:08]</a>.

While the do-calculus can be complex, it has been algorithmized, allowing libraries like `y0` in Python to determine if a query of interest is identifiable given observed data <a class="yt-timestamp" data-t="00:41:21">[00:41:21]</a>, <a class="yt-timestamp" data-t="00:41:30">[00:41:30]</a>, <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.

## Bayesian and Probabilistic Programming Approaches

A Bayesian approach to identification deals with uncertainty and incorporates prior knowledge about the system's structure, like the size or shape of the system, or what interactions are not allowed <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. This approach aims to provide guarantees that, with more data and specific evaluation criteria, the analysis will move towards the correct answer even if the true ground truth is unknown <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

Probabilistic programming frameworks (e.g., PyMC, Stan, Pyro) allow users to explicitly define a system model with variables and their distributions <a class="yt-timestamp" data-t="00:42:21">[00:42:21]</a>. Research has shown that if a causal quantity is identifiable using the do-calculus, implementing the system in such a framework guarantees a good, unbiased estimate of the causal effect <a class="yt-timestamp" data-t="00:42:03">[00:42:03]</a>. This opens up the world of [[causal_inference_methods_and_applications | causal reasoning]] to those familiar with latent variable models and probabilistic programming <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>, <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>. Libraries like Cairo, built on Pyro, are designed to abstract away the complex inference aspects of [[causal_inference_and_decision_making | causal inference]], making it more accessible <a class="yt-timestamp" data-t="00:47:39">[00:47:39]</a>, <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.

## Identification in Machine Learning and AI

### Causal Reinforcement Learning

Traditional reinforcement learning often folds all environmental factors into a "state" variable, potentially ignoring causal nuances <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. This can lead to suboptimal decisions when the actions that maximize expected reward without considering how they change the environment differ from actions that do <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. Causality helps understand when and how these differences occur <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.

[[Causal inference and its applications | Causal reinforcement learning]] leverages causal assumptions to improve sample efficiency, which is crucial in high-dimensional settings <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>, <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. It also assists in credit assignment, framing questions about why a policy led to a certain outcome as a causal problem <a class="yt-timestamp" data-t="00:13:24">[0:13:24]</a>. While basic reinforcement learning often works in many practical problems, there are specific, high-value scenarios where a causal model is essential for reliable outcomes, especially when dealing with unseen circumstances or when the state variable lacks all necessary information for [[understanding_partial_identification_in_causal_analysis | causal identifiability]] <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>, <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>, <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

### Artificial General Intelligence (AGI) and Large Language Models

From a causal perspective, an AGI system would be able to reason about cause and effect <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>. This involves modeling how humans reason, including their causal reasoning capabilities, which is a step towards AGI <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>, <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>.

The [[causal_discovery_versus_causal_inference | Causal Hierarchy Theorem]] (also known as Pearl's Causal Ladder) highlights the different levels of causal reasoning:
1.  **Associational**: Observational statistics (e.g., correlation) <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>.
2.  **Interventional**: Estimating causal effects (e.g., "do X") <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>.
3.  **Counterfactual**: Reasoning about "what if" scenarios across different hypothetical worlds <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a>.

To answer questions at a certain level, assumptions from at least that same level are required <a class="yt-timestamp" data-t="00:56:31">[00:56:31]</a>. For example, answering counterfactual questions requires Level 3 assumptions, often in the form of a structural causal model <a class="yt-timestamp" data-t="00:56:44">[00:56:44]</a>.

Large language models (LLMs) can answer causal questions empirically, but they can "hallucinate" <a class="yt-timestamp" data-t="00:57:07">[00:57:07]</a>, <a class="yt-timestamp" data-t="00:57:44">[00:57:44]</a>. The challenge is to understand if LLMs possess the underlying causal assumptions (Level 3 for counterfactuals) needed for reliable causal reasoning <a class="yt-timestamp" data-t="00:58:43">[00:58:43]</a>. These assumptions might exist in the training data, model architecture, parameterization, or prompt <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>. Incorporating causal information directly into the Transformer architecture itself could provide theoretical guarantees for answering causal queries reliably <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>, <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>.

### Causal Representation Learning

A significant future development in causality is **causal representation learning** <a class="yt-timestamp" data-t="00:49:48">[00:49:48]</a>. This field aims to learn latent representations that correspond to actual causes in the data-generating process <a class="yt-timestamp" data-t="00:50:12">[00:50:12]</a>. The knowledge of causality can be used to identify desiderata for how these learned causes should behave (e.g., modularity, invariance) <a class="yt-timestamp" data-t="00:50:20">[00:50:20]</a>.

In generative AI, for instance, users want to make specific, localized changes (e.g., changing glasses color) without altering causally unrelated parts of an image <a class="yt-timestamp" data-t="00:51:30">[00:51:30]</a>. This requires operating semantically on learned causal abstractions or representations behind the image <a class="yt-timestamp" data-t="00:52:40">[00:52:40]</a>. Better causal representations could allow for "knobs" that users can turn to make precise, causally consistent adjustments in generative models, augmenting creative processes <a class="yt-timestamp" data-t="00:53:19">[00:53:19]</a>, <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.