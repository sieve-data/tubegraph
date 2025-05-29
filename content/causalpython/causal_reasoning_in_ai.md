---
title: Causal reasoning in AI
videoId: relI7Q9A03g
---

From: [[causalpython]] <br/> 

This article summarizes insights from a discussion with Dr. Andrew Lampinen, a Senior Research Scientist at Google DeepMind, on the "Causal Bandits Podcast" <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. Dr. Lampinen's work explores the capacity of large language models (LLMs) and other AI systems to learn and apply [[causality_in_ai|causal reasoning]] principles.

## Active and Passive Strategies in Large Language Models

In a series of papers published in the second half of 2023, Dr. Lampinen's work introduces the concepts of "active" and "passive" strategies in the context of LLMs and [[causality_in_ai|causality]] <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. This naming convention differs from traditional machine learning terms like "interventional" or "observational" data, often extrapolated from Pearl's causal hierarchy <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.

> [!NOTE] Distinction between Passive Learning and Interventional Data
> Although language models are trained passively by processing language data from the internet, this data is not necessarily purely observational <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. For instance, scientific papers, Stack Overflow posts detailing debugging experiments, and even conversations involve "interventions" within the data <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. Therefore, LLMs can learn real [[causal_discovery_and_inference_in_ai|causal information]] from this passively absorbed, yet interventional, data <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.

This distinction is crucial because it implies that LLMs might possess [[generative_ai_and_causal_reasoning|causal strategies]] or understanding that can generalize beyond their training data <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. By passively observing others' interventions, models may discover a strategy for intervening themselves, which they can then apply in new situations to uncover new causal structures and achieve downstream goals <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

### Experimental Setup and Findings
To explore this, Dr. Lampinen's team conducted controlled experiments with simpler models trained on specific data distributions <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>. They trained models on data showing interventions on causal Directed Acyclic Graphs (DAGs), where the model observed series of interventions and goals (e.g., maximizing a variable) <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. The key question was whether models trained passively could generalize to actively intervene and discover new causal structures at test time, even on held-out causal structures <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.

The results showed that systems could apply passively observed [[causal_ai_and_its_role_in_experiments|causal strategies]] from training to actively intervene at test time, discovering and exploiting new causal structures <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>. These models approximated correct [[causal_reasoning_in_artificial_intelligence|causal reasoning]] much more closely than simpler heuristic or associational strategies <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>.

## LLMs and Causal Reasoning: Contradiction or Complement?

Dr. Lampinen's findings appear to contradict the "causal parrots" hypothesis, which suggests that LLMs learn a "meta-structural causal model" based on correlations of causal facts in training data, allowing them to "talk causality but not reason causally" <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. Dr. Lampinen argues that his results indicate models are capable of discovering a [[causal_reasoning_in_artificial_intelligence|causal reasoning]] algorithm that can be applied in a generalizable way <a class="yt-timestamp" data-t="06:55:00">[06:55:52]</a>.

The data mixture in natural language training is important; while it contains many correlations, it also includes interventional data <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>. When given explanations in prompts, LLMs can effectively learn to discover new causal structures not explicitly included in the prompt, suggesting sufficient interventional data for strategy discovery <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

## Training Paradigms and Generalization

The current training paradigm for LLMs is heavily driven by what works and allows for data at scale <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>. However, auxiliary tasks and explanations can significantly improve learning and generalization <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>. For example, providing a natural language explanation for a reinforcement learning agent's reward can enhance its learning <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

New approaches are emerging, such as conditioning models on a quality signal (e.g., a reward estimate) during training <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>. This allows models to learn from diverse data, including lower-quality examples, while still being able to generate high-quality responses at test time <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.

## LLMs as Agents

Dr. Lampinen views LLMs as a type of "agent" within the broader paradigm of passively trained agents <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. An agent is a system that takes inputs (observations) and produces output actions in a sequential decision-making problem <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. This includes language models that interact with users, as well as game-playing AI <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.

A key distinction is whether the agent interacts with the environment during training or only at testing time <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>. While agents are often trained partly on passive observational data (e.g., observing expert players), subsequent reinforcement learning (RL) or fine-tuning steps involve active interaction, where the agent learns from rewards based on its actions <a class="yt-timestamp" data-t="12:25:00">[12:25:00]</a>. This hybrid approach is common in LLM development, moving from passive internet data to fine-tuning and then RL based on human preferences <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>.

LLMs are considered useful sequential decision-making systems, particularly as tools for humans in tasks like writing, idea generation, or critiquing thinking <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>. While not yet autonomous, they are effective with human oversight <a class="yt-timestamp" data-t="18:06:00">[18:06:00]</a>.

## Addressing Error Accumulation in Autoregressive Models

Autoregressive models, by conditioning their next output on previous generations, can accumulate errors over long sequences <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>. However, state-of-the-art LLMs can exhibit some error correction abilities, for example, through "Chain of Thought" reasoning <a class="yt-timestamp" data-t="13:58:00">[13:58:00]</a>. The system's architecture and context length, allowing it to reconsider prior context, can affect its ability to correct errors <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>.

Passive learning can lead to poor generalization out of distribution, as systems tend to break down when they move off the training data distribution during active use <a class="yt-timestamp" data-t="14:42:00">[14:42:00]</a>. Techniques from offline reinforcement learning, like DAgger, provide interventional data that helps systems recover to the data distribution when they deviate <a class="yt-timestamp" data-t="15:06:00">[15:06:00]</a>. The fine-tuning and RL steps in LLM training serve a similar purpose, acting as a form of interventional data <a class="yt-timestamp" data-t="15:24:00">[15:24:00]</a>.

## Causal Data Fusion

The combination of observational and interventional data, known as causal data fusion, is a promising area <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>. By leveraging "prior knowledge" from observational sources to cue the system on relevant variables, it can learn to intervene more efficiently to determine causal structures, rather than exploring irrelevant variables <a class="yt-timestamp" data-t="16:42:00">[16:42:00]</a>.

## The Role of Causality in Generalization

[[causality_in_ai|Causality]] is a powerful tool for generalization <a class="yt-timestamp" data-t="21:28:00">[21:28:00]</a>. While mathematical systems might not always require a causal understanding (as they deal with equivalences), for real-world and agentic systems, [[causality_in_ai|causality]] offers useful intuitions for understanding how a system will generalize and where it might fail <a class="yt-timestamp" data-t="21:54:00">[21:54:00]</a>.

## Neuro-symbolic AI and Discrete vs. Continuous Reasoning

The integration of representation learning (soft, differentiable) with symbolic, discrete systems in [[causal_reasoning_in_artificial_intelligence|AI]] has a bright future <a class="yt-timestamp" data-t="23:07:00">[23:07:00]</a>. Dr. Lampinen believes that logical reasoning systems are useful tools for intelligent systems, but intelligence itself tends to take the form of a continuous, "fuzzy" reasoning system <a class="yt-timestamp" data-t="23:33:00">[23:33:00]</a>. Symbolic logic serves as a tool for these fuzzy systems to tackle specific constraint problems where logical systems excel <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>.

This perspective is rooted in the observation that humans are not inherently good logical or mathematical reasoners without extensive training <a class="yt-timestamp" data-t="23:46:00">[23:46:00]</a>. We build tools to augment our abilities. The most effective general approaches will involve fuzzy learning systems controlling and utilizing logical systems as tools <a class="yt-timestamp" data-t="24:35:00">[24:35:00]</a>.

This view contrasts with the idea of overly constraining a system with rigid logical reasoning processes <a class="yt-timestamp" data-t="44:03:00">[44:03:00]</a>. Such strong constraints can make a system fragile, causing it to "totally break down" when it encounters situations that don't perfectly match its assumptions <a class="yt-timestamp" data-t="44:25:00">[44:25:00]</a>. Softer solutions, like providing explanations or modifying data distribution, can be more effective and scalable, especially when dealing with complex, unknown problems where building in strong inductive biases might lead to brittle systems. This aligns with "The Bitter Lesson" by Rich Sutton, which suggests that strong, built-in assumptions work at small scale but tend to break down when scaled up <a class="yt-timestamp" data-t="45:40:00">[45:40:00]</a>.

## Human Causality and AI

Developmental psychologists like Alison Gopnik have shown that human babies systematically interact with the world to build world models, with an innate or evolutionarily developed motivation for this exploration <a class="yt-timestamp" data-t="25:25:00">[25:25:00]</a>. Some of Gopnik's famous studies involve children passively observing experiments before actively playing with detectors, analogous to the passive learning of interventional data described for LLMs <a class="yt-timestamp" data-t="27:38:00">[27:38:00]</a>.

While LLMs have shown some improvement in analogical reasoning problems, similar to some ARC tasks that test abstract structure independent of superficial details <a class="yt-timestamp" data-t="31:40:00">[31:40:00]</a>, there are still challenges. Dr. Lampinen suggests that formal reasoning in humans requires years of rigorous training, and we might overestimate how naturally good humans are at reasoning <a class="yt-timestamp" data-t="32:40:00">[32:40:00]</a>.

Humans and LLMs both perform better in logical reasoning when the semantic content supports the logic, and worse when it contradicts it <a class="yt-timestamp" data-t="33:49:00">[33:49:00]</a>. This suggests that the objective of humans and LLMs is not always to be perfectly "rational reasoners" in a logical sense, but rather to be "adaptive" to encountered situations <a class="yt-timestamp" data-t="41:18:00">[41:18:00]</a>. This concept aligns with "bounded rationality," where seemingly irrational behaviors might be optimal given limited resources or to be more accurate in everyday situations <a class="yt-timestamp" data-t="41:59:00">[41:59:00]</a>.

## Understanding in AI

"Understanding" in AI, like many properties, is viewed as a graded concept, not a discrete binary state <a class="yt-timestamp" data-t="29:02:00">[29:02:00]</a>. It refers to the richness of representation and the degree to which a system can generalize <a class="yt-timestamp" data-t="29:13:00">[29:13:00]</a>. While LLMs may lack understanding of certain phenomena (e.g., perception), they demonstrate some degree of understanding in their ability to answer questions correctly <a class="yt-timestamp" data-t="29:51:00">[29:51:00]</a>.

## Future of [[causality_in_ai|Causality]] and Machine Learning

The future intersection of [[causality_in_ai|causality]] and machine learning involves combining formalisms like Pearl's do-calculus with dynamical systems and differential equations <a class="yt-timestamp" data-t="52:55:00">[52:55:00]</a>. There's a vision for bridging "soft learning" with more formalized inference methods, acknowledging that humans primarily use soft learning skills over formal reasoning in daily life, but with underlying structural constraints <a class="yt-timestamp" data-t="53:13:00">[53:13:00]</a>.

A unified perspective is needed to address misconceptions in the community, such as viewing A/B testing as superior to [[causal_discovery_and_inference_in_ai|causal inference]] or dismissing the need for [[causality_in_ai|causal inference]] in simulations or digital twins <a class="yt-timestamp" data-t="56:06:00">[56:06:00]</a>. Interventions, A/B tests, and simulations can be seen as special cases or operationalizations within structural causal models, offering a cohesive framework <a class="yt-timestamp" data-t="56:32:00">[56:32:00]</a>. The grand goal for many sciences is to arrive at a more unified perspective <a class="yt-timestamp" data-t="57:27:00">[57:27:00]</a>.