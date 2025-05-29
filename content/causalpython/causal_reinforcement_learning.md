---
title: Causal Reinforcement Learning
videoId: gazCIKYEv44
---

From: [[causalpython]] <br/> 

Causal Reinforcement Learning (RL) is an emerging area that integrates principles of causality into traditional reinforcement learning frameworks. It is considered a branch of [[Causal Reasoning in DecisionMaking | causal decision theory]] and [[Integration of causal reasoning in machine learning | causal sequential decision-making]] <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

## Motivation for Causal RL

Traditional reinforcement learning methods, particularly model-free approaches like Q-learning, primarily focus on optimizing actions based on observed statistical patterns and rewards <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. This approach assumes that a "state variable" can capture all necessary information about the world <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. However, this can lead to issues where the goal of optimizing (the thing being optimized) and the actual outcome are different, potentially leading to error-prone results <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

While traditional RL is often sufficient for many problems, there are scenarios where ignoring causal nuances can lead to suboptimal decisions <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. Specifically, actions that maximize expected reward might differ from actions that maximize expected reward when considering how those actions causally change the environment <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. This is particularly relevant when:
*   Maximizing outcomes under circumstances not seen in training data <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
*   Actions that maximize the outcome based on association are different from those that maximize it when accounting for causal dynamics <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
*   The state variable does not contain all information required for causal identifiability, leading to biases or incomplete understanding <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

## Advantages of Causal RL

Integrating causal assumptions into RL offers several key benefits:

*   **Sample Efficiency** <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>: Causal assumptions about the data generating process allow for inferences that would not be possible from merely modeling statistical patterns <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This can make intractable problems tractable, especially in high-dimensional settings <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   **Credit Assignment and Root Cause Analysis** <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>: Causal RL can help understand *how* or *why* a policy led to a certain outcome, enabling tasks like attribution methods or root cause analysis <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Human-like Decision Making** <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>: Humans often reason by imagining hypothetical scenarios and conditioning on outcomes in those "potential outcomes" worlds, rather than just conditioning on observed data <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. This makes human reasoning very sample efficient, as one doesn't need to directly experience something to learn from it <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. [[Causal models in autonomous driving | Causal models]] provide the language and semantics for building algorithms that mimic this human-like reasoning <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   **New Capabilities**: Causal reasoning can unlock capabilities in RL that were not previously available, especially in scenarios where traditional methods struggle <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.

## Challenges and Future Directions

A significant challenge for [[Causal AI and machine learning | causal AI]] researchers is moving beyond "toy problems" that demonstrate the limitations of non-causal approaches, and instead identifying practical, high-value scenarios where a causal model is genuinely necessary <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. This requires deep domain knowledge <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.

One promising area for future development is **causal representation learning** <a class="yt-timestamp" data-t="00:49:48">[00:49:48]</a>. This involves learning latent representations that correspond to actual causes in the data generating process, using causal knowledge to define how these causes should behave (e.g., modularity, invariance) <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>. This could have a huge impact, particularly in [[Generative AI and Causal Models | generative AI]], where users desire semantic control over generated content (e.g., changing glasses color without affecting other elements in an image) <a class="yt-timestamp" data-t="00:51:10">[00:51:10]</a>. This would allow for semantic-level reasoning, rather than just pixel-level manipulation <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.

Another direction involves incorporating causal information directly into the structure of deep learning models, such as Transformer architectures <a class="yt-timestamp" data-t="01:00:11">[01:00:11]</a>. This could provide theoretical guarantees, similar to how the do-calculus ensures validity in probabilistic programming frameworks <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>. The goal is to align models with human abstract thinking, enhancing creative processes and allowing for more targeted control <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>. This approach contrasts with solely scaling models by increasing data, instead focusing on leveraging innate structure in data to achieve more powerful models with smaller datasets <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>.

### Comparison with Causal Decision Theory

[[Causal Reinforcement Learning in causal inference – Link name: role_of_reinforcement_learning_in_causal_inference | Causal reinforcement learning]] is seen as deeply related to [[Causal Reasoning in DecisionMaking | causal decision theory]] <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. While causal decision theory has historical contrasts with "empirical decision theory" (which focuses on consequences of actions vs. maximizing expected utility conditional on interaction), modern understanding of [[Causal AI and its connection to machine learning | causal models]] allows their incorporation into end-to-end analysis for automated decision-making <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

An example of [[Causal AI and machine learning | causal AI]] application is [[causal_ai_and_machine_learning | causal bandits]], where an adversarial relationship with a confounder requires estimating a causal effect in a partially identified setting, often using methods like causal Thompson sampling <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This addresses how to apply causal knowledge to optimization in systems with unknown causal factors that would lead to suboptimal decisions with traditional Bandit methods <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.