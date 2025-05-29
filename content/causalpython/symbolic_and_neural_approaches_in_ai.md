---
title: Symbolic and neural approaches in AI
videoId: relI7Q9A03g
---

From: [[causalpython]] <br/> 

Dr. Andrew Lampinen, a Senior Research Scientist at Google DeepMind, discusses the role of symbolic and neural approaches in artificial intelligence, emphasizing how they can complement each other, with fuzzy, continuous systems potentially acting as the core intelligence utilizing symbolic methods as tools <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.

## Symbolic vs. Fuzzy Systems in AI

In the context of machine learning, particularly large language models (LLMs), a key distinction arises when discussing "active and passive strategies" <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. Lampinen notes that while LLMs are trained passively on language data (e.g., from the internet) <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>, this data is often [[causality_in_ai | Interventional]], containing scientific papers, debugging discussions, and conversations where each statement is an intervention <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. This allows models to discover causal strategies for intervention and apply them in new situations, generalizing beyond their training data <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

Lampinen's work, which includes experiments training simpler models on controlled distributions of data showing interventions on causal directed acyclic graphs (DAGs), suggests that passively observing others' interventions can lead to a generalizable strategy for determining causal structures <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. This contrasts with the hypothesis in the "Causal Parrots" paper, which suggests LLMs primarily learn a "meta-structural causal model" based on correlations <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>. While natural data may contain more correlations, sufficient [[causality_in_ai | interventional data]] can enable models to discover and apply [[causal_reasoning_in_artificial_intelligence | causal reasoning algorithms]] effectively, especially when provided with explanations in the prompt <a class="yt-timestamp" data-t="07:07:00">[07:07:07]</a>.

Regarding the "neuros ymbolic AI" field, Lampinen believes that combining representation learning (soft, differentiable) with symbolic systems (discrete) has a bright future <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. However, he views this relationship differently from many others:
*   **Symbolic systems as tools**: Logical reasoning systems are valuable tools for an intelligent system to use, particularly for constrained problems like those found in mathematics or computational sciences <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.
*   **Fuzzy systems as core intelligence**: True intelligence, in Lampinen's view, tends to take the form of a continuous, fuzzy reasoning system <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>. The most general and effective approaches will involve these fuzzy learning systems being in control, utilizing logical systems when appropriate <a class="yt-timestamp" data-t="00:24:35">[00:24:35]</a>.

## Human Reasoning and AI Rationality

Lampinen draws parallels between this perspective and human cognition:
*   **Humans are not inherently logical**: Humans are not naturally good at formal logical or mathematical reasoning without extensive training <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>. Tools are built to assist with these tasks, just as an intelligent AI system would use symbolic logic <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>.
*   **"Expert blind spot"**: Researchers, often being highly educated and rigorously trained, may overestimate the average person's natural ability for formal reasoning <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>. Both humans and language models perform better when the semantic content of a problem supports their logical reasoning and worse when it contradicts it <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>.
*   **Adaptive rationality**: The objective of both humans and language models is not necessarily to be perfectly rational reasoners, but to be adaptive to the situations they encounter daily <a class="yt-timestamp" data-t="00:41:21">[00:41:21]</a>. This means being "less rational" in a strictly logical sense might lead to better decisions across typical real-world distributions <a class="yt-timestamp" data-t="00:41:29">[00:41:29]</a>. This aligns with concepts like bounded rationality, where limited resources necessitate adaptive, rather than strictly optimal, inferences <a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>.

## System Design and Generalization

Overly constraining reasoning processes in AI systems, such as by imposing strict formal logic, can make them fragile <a class="yt-timestamp" data-t="00:44:23">[00:44:23]</a>. If assumptions about the world don't match reality, the system can completely break down <a class="yt-timestamp" data-t="00:44:32">[00:44:32]</a>. This aligns with "The Bitter Lesson" by Rich Sutton, which suggests that building in perceived "right ways" to solve problems might work at small scales but tends to fail when scaled up <a class="yt-timestamp" data-t="00:45:44">[00:45:44]</a>.

Instead, Lampinen advocates for "softer solutions" such as:
*   Using explanation prediction objectives to encourage systems to represent important information without overly constraining internal computations <a class="yt-timestamp" data-t="00:44:43">[00:44:43]</a>.
*   Changing the data distribution from which the system learns <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.

He emphasizes that language models, as sequential decision-making systems, are already useful tools, especially when human oversight is involved <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. Their ability to "error correct" in sequences, like in Chain of Thought reasoning, suggests a degree of adaptability <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

## The Future of [[intersection_of_causality_and_ai_technologies | Causality and AI]]

The future of [[causality_in_ai | causality]] and machine learning, particularly in the context of [[advancements_in_causal_modeling_and_ai | future AI advancements]], involves bridging different levels of abstraction <a class="yt-timestamp" data-t="00:52:55">[00:52:55]</a>. Lampinen suggests building more holistic systems capable of understanding across:
*   Raw data <a class="yt-timestamp" data-t="00:36:14">[00:36:14]</a>
*   Causal abstractions <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>
*   Counterfactual questions <a class="yt-timestamp" data-t="00:36:18">[00:36:18]</a>

Host Alex Mola highlights the importance of combining [[causality_in_ai | causal formalisms]] like Pearl's do-calculus with mathematical concepts such as differential equations and dynamical systems <a class="yt-timestamp" data-t="00:52:55">[00:52:55]</a>. He also stresses the need for a unified perspective that shows interventions (like A/B tests) and simulations as special cases or operationalizations of [[causality_in_ai | causal inference]] and [[causality_in_ai | structural causal models]] <a class="yt-timestamp" data-t="00:56:32">[00:56:32]</a>. This approach aims to make [[causality_in_ai | causality]] more accessible and to resolve misconceptions within the community <a class="yt-timestamp" data-t="00:55:54">[00:55:54]</a>.