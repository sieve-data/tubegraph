---
title: role of causality in generalization
videoId: relI7Q9A03g
---

From: [[causalpython]] <br/> 

The Causal Bandits podcast welcomed Dr. Andrew Lampinen, a Senior Research Scientist at Google DeepMind, to discuss [[causality_and_machine_learning | causality and machine learning]], particularly focusing on its [[role_of_causality_in_agentbased_systems | role in generalization]] for large language models (LLMs) <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. Lampinen's background includes studies in mathematics, physics, and cognitive psychology <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>.

## Causality and Generalization in Large Language Models

A key distinction in Dr. Lampinen's recent paper, published in late 2023, is the concept of "active" versus "passive" strategies in the context of LLMs and [[causality_and_causal_models | causal models]] <a class="yt-timestamp" data-t="01:30:52">[01:30:52]</a>.

### Active vs. Passive Strategies
While LLMs are trained passively by processing language data from the internet, this data is not necessarily purely observational <a class="yt-timestamp" data-t="02:12:12">[02:12:12]</a>. For instance, scientific papers, Stack Overflow posts (where users debug by trying experiments), and even conversations involve interventions <a class="yt-timestamp" data-t="02:40:02">[02:40:02]</a>. Thus, even though LLMs learn passively, they are learning from interventional data, which contains real causal information <a class="yt-timestamp" data-t="03:00:02">[03:00:02]</a>.

### Learning Causal Strategies
The paper explores how this type of training data can lead to causal strategies or understanding that [[applications_and_challenges_of_causality_in_generative_modeling | generalize beyond the training data]] <a class="yt-timestamp" data-t="03:20:02">[03:20:02]</a>.
By passively observing others' interventions, models can discover a strategy for intervening that they can apply in new situations to discover new causal structures for a downstream goal <a class="yt-timestamp" data-t="03:45:02">[03:45:02]</a>. Dr. Lampinen's empirical findings suggest that models can learn a generalizable strategy for intervening to determine causal structures purely from passively observing interventions <a class="yt-timestamp" data-t="03:52:02">[03:52:02]</a>.

In controlled experiments, a simpler model was trained on a distribution of data showing interventions on causal Directed Acyclic Graphs (DAGs) <a class="yt-timestamp" data-t="04:41:02">[04:41:02]</a>. The model observed sequences of interventions and goals (e.g., maximize a variable) <a class="yt-timestamp" data-t="04:59:02">[04:59:02]</a>. The key test was whether the model, after passive training, could actively intervene to discover and exploit new causal structures on unseen DAGs at test time <a class="yt-timestamp" data-t="05:20:02">[05:20:02]</a>. The results demonstrated that the system could apply passively observed causal strategies to actively intervene, discover new causal structures, and exploit them <a class="yt-timestamp" data-t="05:43:02">[05:43:02]</a>. The model approximated correct causal reasoning much more closely than simpler heuristic or associational strategies <a class="yt-timestamp" data-t="05:58:02">[05:58:02]</a>.

### Contrasting with "Causal Parrots"
Another paper, "Causal Parrots," hypothesized that LLMs learn a "meta-structural causal model" based on correlations of causal facts in training data, concluding that LLMs "can talk [[causality_in_artificial_intelligence | causality]] but do not reason causally" <a class="yt-timestamp" data-t="06:38:02">[06:38:02]</a>. Dr. Lampinen's results suggest a contradiction, indicating that models *are* capable of discovering a causal reasoning algorithm that can be applied in a new, generalizable way, given a good enough training regime <a class="yt-timestamp" data-t="06:52:02">[06:52:02]</a>. While natural data may contain more correlations and fewer interventions, LLMs, when tested on tasks requiring experimenting to discover causal structures (especially with prompt explanations), learn to do this effectively <a class="yt-timestamp" data-t="07:51:02">[07:51:02]</a>. This implies sufficient interventional data in LLM training distributions for these strategies to be discovered <a class="yt-timestamp" data-t="08:00:02">[08:00:02]</a>.

## Training Paradigms and Generalization

### Importance of Explanations
Structuring the training regime plays a crucial role. For example, giving a natural language explanation of why a [[role_of_reinforcement_learning_in_causal_inference | reinforcement learning]] agent receives a reward, and asking it to predict those explanations, can improve what it learns and how it generalizes out of distribution, even with confounded data <a class="yt-timestamp" data-t="09:12:02">[09:12:02]</a>.

### Addressing Error Accumulation
Autoregressive models might accumulate errors over long sequences, as each subsequent token or data point is conditioned on previous, potentially erroneous, generations <a class="yt-timestamp" data-t="13:14:02">[13:14:02]</a>. However, current LLMs can sometimes self-correct using techniques like Chain of Thought <a class="yt-timestamp" data-t="14:04:02">[14:04:02]</a>. The system's architecture, including its context length and ability to reconsider prior context, can impact its error correction capabilities <a class="yt-timestamp" data-t="14:21:02">[14:21:02]</a>.

Passive learning tends to be less efficient and leads to worse out-of-distribution generalization <a class="yt-timestamp" data-t="14:42:02">[14:42:02]</a>. Simplistic passive learning strategies can cause a system to break down once it operates actively and moves off its training data distribution <a class="yt-timestamp" data-t="14:56:02">[14:56:02]</a>. Techniques from offline [[role_of_reinforcement_learning_in_causal_inference | reinforcement learning]], like Dagger, use limited interventional data to guide the system back to the data distribution, fostering robustness <a class="yt-timestamp" data-t="15:11:02">[15:11:02]</a>. The active [[role_of_reinforcement_learning_in_causal_inference | reinforcement learning]] used in LLM fine-tuning acts as a form of interventional data <a class="yt-timestamp" data-t="15:26:02">[15:26:02]</a>.

### Causal Data Fusion
There's an interesting parallel between these ideas and the [[causality_and_causal_models | causal inference]] literature on "causal data fusion," which involves mixing observational and interventional data <a class="yt-timestamp" data-t="16:05:02">[16:05:02]</a>. This can help recover causal structure and maximize inference efficiency <a class="yt-timestamp" data-t="16:14:02">[16:14:02]</a>. Such an approach could help systems efficiently determine necessary causal structures by focusing interventions on relevant variables, potentially informed by observational "prior knowledge" <a class="yt-timestamp" data-t="16:47:02">[16:47:02]</a>.

## Nature of Generalization and Rationality

### Causality as a Tool for Generalization
[[Causality]] is a useful tool for generalization, particularly for real-world and agentic systems <a class="yt-timestamp" data-t="21:50:02">[00:21:50]</a>. Intuitions about confounding and intervention are practical for thinking about generalization problems in agentic systems <a class="yt-timestamp" data-t="22:04:02">[02:04:02]</a>.

### Humans, Formal Reasoning, and Generalization
Dr. Lampinen views symbolic reasoning systems as useful tools for intelligent systems, rather than intelligence itself <a class="yt-timestamp" data-t="23:36:02">[23:36:02]</a>. Humans are not naturally strong logical or mathematical reasoners without extensive training <a class="yt-timestamp" data-t="23:46:02">[23:46:02]</a>. Intelligence often takes the form of a continuous, fuzzy reasoning system, where symbolic logic serves as a tool to tackle specific constrained problems <a class="yt-timestamp" data-t="24:10:02">[24:10:02]</a>.

The ability to generalize to abstract structures, where superficial details are orthogonal to the underlying structure, is crucial for tasks like those in François Chollet's ARC tests <a class="yt-timestamp" data-t="32:00:02">[32:00:02]</a>. Recent work by Taylor Webb and Keith Holyoak on analogical reasoning problems shows that later-generation LLMs are performing increasingly well, sometimes nearly as well as humans, on such tasks <a class="yt-timestamp" data-t="32:22:02">[32:22:02]</a>.

However, formal reasoning in humans requires years of rigorous education <a class="yt-timestamp" data-t="32:44:02">[32:44:02]</a>. There is a tendency to overestimate human natural reasoning abilities, particularly because researchers conducting these studies are highly educated individuals <a class="yt-timestamp" data-t="33:19:02">[33:19:02]</a>. Both humans and LLMs perform better on logical problems when the semantic content supports their logical reasoning and worse when it contradicts it <a class="yt-timestamp" data-t="33:58:02">[33:58:02]</a>.

### Bounded Rationality
The objective of humans and LLMs is not necessarily to be rational reasoners, but rather to be adaptive to the situations they encounter <a class="yt-timestamp" data-t="41:18:02">[41:18:02]</a>. Being "less rational" in a strict logical sense might lead to better decisions across the distribution of everyday situations <a class="yt-timestamp" data-t="41:31:02">[41:31:02]</a>. This concept aligns with "bounded rationality," where humans, with limited resources, make "irrational" choices that are overall beneficial or more accurate in common situations <a class="yt-timestamp" data-t="41:59:02">[41:59:02]</a>.

### Fragility of Over-Constrained Systems
Overly constraining reasoning processes in systems, based on assumptions like requiring formal logical reasoning, can make the system more fragile <a class="yt-timestamp" data-t="44:20:02">[44:20:02]</a>. If real-world situations deviate from these assumptions, the system can break down <a class="yt-timestamp" data-t="44:32:02">[44:32:02]</a>.
Dr. Lampinen's approach uses objectives like explanation prediction to encourage systems to represent important concepts without overly constraining their internal computations, leading to softer, more robust influence <a class="yt-timestamp" data-t="44:43:02">[44:43:02]</a>. This aligns with "The Bitter Lesson" from Rich Sutton, which suggests that building in specific solutions works at small scale but tends to break down when systems are scaled <a class="yt-timestamp" data-t="45:40:02">[45:40:02]</a>. Softer solutions, such as providing explanations or altering data distributions, are often more effective and scalable <a class="yt-timestamp" data-t="46:01:02">[46:01:02]</a>.

## Challenges in Generalization: Lab vs. Reality
Working in controlled laboratory settings is important for understanding system behavior <a class="yt-timestamp" data-t="46:50:02">[46:50:02]</a>. However, the real world acts as a crucial "forcing function" against overfitting, ensuring that algorithms generalize beyond specific toy problems <a class="yt-timestamp" data-t="47:01:02">[47:01:02]</a>. Building systems like image processing or language models that can handle any natural input is a powerful way to test and validate ideas <a class="yt-timestamp" data-t="47:37:02">[47:37:02]</a>.

## Dr. Andrew Lampinen's Background and Approach

### Influence of Physics, Mathematics, and Psychology
Dr. Lampinen's foundation in physics and mathematics has been highly useful, providing intuitions for linear algebra and programming that are broadly applicable in statistics, cognitive psychology, and [[machine_learning_and_causality | machine learning]] <a class="yt-timestamp" data-t="20:18:02">[20:18:02]</a>. His doctoral studies in cognitive psychology offered valuable lessons in experimental design and rigorous statistical analysis <a class="yt-timestamp" data-t="48:27:02">[48:27:02]</a>. Cognitive psychology also emphasizes bridging from observations to abstract models, a valuable skill for understanding complex systems <a class="yt-timestamp" data-t="48:50:02">[48:50:02]</a>.

### Advice for Learning Complex Fields
For those entering complex fields like [[causality_and_machine_learning | causality]] or [[role_of_reinforcement_learning_in_causal_inference | reinforcement learning]], Dr. Lampinen advises "playing around with it" – coding up concepts, changing parameters, and observing how the system behaves <a class="yt-timestamp" data-t="35:28:02">[35:28:02]</a>. This hands-on approach helps build intuitions crucial for understanding <a class="yt-timestamp" data-t="35:50:02">[35:50:02]</a>. His message to the causal community is to build more holistic systems that can bridge understanding across multiple levels of abstraction, including raw data, causal abstractions, and counterfactual questions <a class="yt-timestamp" data-t="36:36:02">[36:36:02]</a>.