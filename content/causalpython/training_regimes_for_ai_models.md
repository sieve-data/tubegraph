---
title: training regimes for AI models
videoId: relI7Q9A03g
---

From: [[causalpython]] <br/> 

Traditional discussions of [[causal AI and machine learning | machine learning]] models in the context of causality often use terms like "interventional," "observational," or "counterfactual," drawn from Pearl's causal hierarchy <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. However, recent research introduces new concepts like "active" and "passive" strategies to better describe the training and deployment of large language models (LLMs) <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.

## Passive vs. Active Strategies

Although language models are [[developing_effective_machine_learning_models | trained passively]] by processing language data from the internet, this data is not purely observational <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. Internet language data is inherently interventional, containing:
*   Scientific papers detailing experiments <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.
*   Stack Overflow posts where users debug by trying experiments <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   Conversations where each statement is an intervention <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

This means that even when LLMs learn passively, they are learning from data that originates from interventions <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. This distinction is crucial because it implies that language models can discover generalizable causal strategies <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. By passively observing others' interventions, models can learn a strategy for intervening that they can then apply in new situations to discover new causal structures for [[developing_effective_machine_learning_models | downstream goals]] <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.

### Structured Learning Tasks
To study this, researchers train simpler models on controlled data distributions, showing interventions on causal directed acyclic graphs (DAGs) <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>. In these tasks, a model observes a series of interventions on a DAG and a goal (e.g., maximize a variable), followed by interventions to achieve that goal <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. The objective is to see if a model trained passively on this interventional data can generalize to actively intervene at test time to discover and exploit new causal structures <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.

Similar to how a language model becomes active when interacting with a user, systems trained passively can apply observed causal strategies to actively intervene, discover new causal structures, and exploit them <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. These models perform significantly better than heuristic or associational baselines <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>.

### Explanations and Training Paradigms
Explanations play a vital role in [[developing_effective_machine_learning_models | structuring the training regime]] for models <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>. Providing natural language explanations, especially in prompts, can improve a model's ability to learn and generalize, even in confounded data scenarios <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

The current training paradigm for LLMs is primarily driven by what works and allows for data at scale <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>. However, there's potential to leverage auxiliary tasks to help models better understand data <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>. For example, conditioning models on a signal of quality, like a reward estimate, during training can help disentangle the training process and enable the system to generate higher-quality responses at test time <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>. This is analogous to techniques in offline reinforcement learning (RL) like Decision Transformer or Upside-Down RL <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.

## Language Models as Agents

The term "agent" is broad, and LLMs can be considered passively [[biological_inspirations_in_ai_models | trained agents]] <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. An agent is a system that takes inputs (observations) and produces output actions in a sequential decision-making problem <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. This includes LLMs, game-playing engines (chess, Go, Atari), and other systems that interact with an environment <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>.

A key distinction in training agents is whether interaction with the environment occurs at training time or only at testing time <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>. Often, agents are initially trained passively by observing expert demonstrations (e.g., Starcraft or Go players) <a class="yt-timestamp" data-t="12:14:00">[12:14:00]</a>. This is followed by reinforcement learning training, where the agent interacts with the environment and receives rewards <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>. This multi-stage approach is also used for LLMs:
1.  **Passive Training:** Large amounts of human-generated language data from the internet <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>.
2.  **Fine-tuning:** Adjusting the model on specific datasets.
3.  **Reinforcement Learning Step:** Training a reward model based on human preferences for language responses, then using this to reward the models for desired outputs <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.

## Challenges and Future Directions

### Error Accumulation and Intervention
Autoregressive models can accumulate errors over long sequences because each subsequent token or data point conditions on previous generations, which may contain errors <a class="yt-timestamp" data-t="13:11:00">[13:11:00]</a>. While state-of-the-art LLMs show some ability to error-correct (e.g., through Chain of Thought reasoning) <a class="yt-timestamp" data-t="13:56:00">[13:56:00]</a>, systems are not yet proficient at this <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>. The ability to reconsider prior context is crucial for error correction <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>.

Passive learning tends to be less efficient and can lead to worse generalization out of distribution <a class="yt-timestamp" data-t="14:42:00">[14:42:00]</a>. When a passively trained system becomes active and moves off its original data distribution, it can break down because it hasn't encountered such situations before <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>. Techniques like DAgger from the offline RL literature incorporate small amounts of interventional data to help the system recover to the data distribution if it deviates <a class="yt-timestamp" data-t="15:09:00">[15:09:00]</a>.

### Data Fusion and Induction
The concept of [[causal inference models and AI workshops | causal data fusion]], which involves mixing observational and interventional data, can help recover causal structures and maximize inference efficiency <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>. This approach can make models more efficient in determining necessary causal structures and avoid exploring irrelevant variables <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>.

### Beyond Formal Reasoning
While formal reasoning is a trained ability for humans, requiring years of education <a class="yt-timestamp" data-t="32:44:00">[32:44:00]</a>, LLMs are increasingly performing well on analogical reasoning tasks, similar to human analogy problems <a class="yt-timestamp" data-t="31:40:00">[31:40:00]</a>. Both humans and LLMs perform better on logical problems when semantic content supports their reasoning and worse when it contradicts it <a class="yt-timestamp" data-t="33:53:00">[33:53:00]</a>. This suggests that the objective of humans and LLMs is not necessarily to be perfectly rational reasoners but to be adaptive to encountered situations, which may involve "irrationality" that aids performance in common scenarios <a class="yt-timestamp" data-t="41:18:00">[41:18:00]</a>. This aligns with theories of bounded rationality, where systems operate effectively with limited resources <a class="yt-timestamp" data-t="41:59:00">[41:59:00]</a>.

### Robustness and Scalability
Overly constraining AI systems with strong assumptions about how they *should* reason (e.g., formal logical reasoning) can make them fragile <a class="yt-timestamp" data-t="44:15:00">[44:15:00]</a>. If the real-world situation doesn't perfectly match these assumptions, the system may break down <a class="yt-timestamp" data-t="44:32:00">[44:32:00]</a>. Softer approaches, like using explanation prediction objectives to encourage relevant representations without over-constraining internal computations, can be more robust <a class="yt-timestamp" data-t="44:43:00">[44:43:00]</a>.

This principle is known as "The Bitter Lesson" in the [[lessons_from_hedge_funds_applied_to_ai_development | machine learning community]], which suggests that building in specific solutions only works at small scales, and these often break down when systems are scaled up <a class="yt-timestamp" data-t="45:40:00">[45:40:00]</a>. Therefore, softer solutions that change data distribution or provide explanations can be more effective and scalable <a class="yt-timestamp" data-t="46:01:00">[46:01:00]</a>.

### Lab vs. Reality
While controlled, "toy" settings are crucial for understanding AI system behavior <a class="yt-timestamp" data-t="46:50:00">[46:50:00]</a>, the real world acts as a "forcing function" that encourages models not to overfit <a class="yt-timestamp" data-t="47:01:00">[47:01:00]</a>. Researchers may inadvertently design tests that perfectly suit their algorithms, but real-world deployment reveals where assumptions fail <a class="yt-timestamp" data-t="47:12:00">[47:12:00]</a>. Building systems for natural images or language queries helps ensure that ideas are truly solving the problem, not just a simplified version <a class="yt-timestamp" data-t="47:37:00">[47:37:00]</a>.

The future of [[causal AI and machine learning | causal AI and machine learning]] involves combining formalisms like Pearl's do-calculus with dynamical systems and soft learning approaches <a class="yt-timestamp" data-t="52:55:00">[52:55:00]</a>. It's important to question whether the goal is human-like systems or superhuman systems in specific regards <a class="yt-timestamp" data-t="55:09:00">[55:09:00]</a>. A unified perspective showing that interventions (like AB tests) and simulations are special cases or operationalizations of [[causal inference models and AI workshops | causal inference]] and structural causal models can be highly beneficial for the community <a class="yt-timestamp" data-t="56:32:00">[56:32:00]</a>.