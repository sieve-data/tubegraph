---
title: Machine learning and causality
videoId: rM25vt_ZmFc
---

From: [[causalpython]] <br/> 

The "Causal Bandits Podcast" explores the intersection of [[Causality in AI | causality]] and [[Machine learning and causal inference methodologies | machine learning]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This article summarizes insights from an interview with Maich, a dedicated researcher passionate about AI, philosophy, and Neuroscience, who has co-authored papers on the intersection of [[Large language models and causality | causality and large language models]] and graph neural networks <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Maich's Journey into Causality

Maich's interest in [[Causality in AI | causality]] was sparked by Judea Pearl's *The Book of Why* <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>, after initially studying AI in computer science at TU Darmstadt <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Before focusing on [[Causality in AI | causality]], his computer science studies began with computer security and IT security <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. He was convinced by Professor Jan Peters to shift towards robotics and reinforcement learning <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. His interests then expanded to Neuroscience and other topics related to intelligence <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

The common thread across these diverse fields was a foundational question: "What is intelligence?" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Maich believes that [[Causal inference and machine learning | causal reasoning]] is necessary for intelligence, though not necessarily sufficient <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Current State of Causal Research

Maich identifies two main strands in [[Causality in AI | causal]] research:
*   **Causal Discovery:** The problem of obtaining a causal graph from data <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, which is more akin to [[Machine learning and causal inference methodologies | machine learning]] <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Causal Inference:** Focusing on sound conclusions based on modeling assumptions, often from an existing graph <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

He notes missing elements in the field, including:
*   Bridges between these two strands <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   More philosophical exploration, broadening the horizon of questions asked <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   Research into abstractions <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   Stronger connections to logic and symbolic AI <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This was a key focus of the NeurIPS 2022 workshop, "Neuro-Causal and Symbolic AI," which aimed to intersect neural networks, [[Causality in AI | causality]], and logic-based symbolic AI <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## The Importance of Abstractions

As a computer scientist, Maich views abstraction as a key concept <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. In a causal sense, abstractions involve equating structural causal models (SCMs) at different levels of detail, ensuring consistency under interventions <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. An example is relating high-level variables like total cholesterol to low-level variables like HDL and LDL <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

Maich highlights the fundamental question: "Where do the variables come from?" and "What is even a causal variable?" <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. Abstractions are crucial for representing the world at different scopes while still capturing essential characteristics <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

He agrees with Pearl's idea that [[Causality in AI | causality]] can be viewed as a "useful abstraction" <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>, kicking out unnecessary details from fine-grained physics models while remaining sufficient to answer specific hypotheses <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. This is analogous to model-free reinforcement learning, where an agent doesn't calculate precise physics but learns the best action intuitively <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. He draws a parallel to Neuroscience and Connectomics, which aims to map the brain at a micro-level, possibly providing sufficient detail but potentially being too fine-grained for many questions <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

## [[Large language models and causality | Large Language Models (LLMs) and Causality]]

Maich positions himself as an advocate for LLMs but approaches them from a [[Causality in AI | causal]] perspective, questioning whether they genuinely reason causally <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.

### Correlations of Causal Facts Conjecture
The core idea behind his paper with Christian Castings and Maurits van der Plas is the "Correlations of Causal Facts" conjecture <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. It proposes that if LLMs learn correlations, their correct answers to causal questions imply that these questions and answers are correlated within their training data <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. Knowledge, including causal insights from experiments (e.g., altitude causing temperature drop), is written down in textbooks and encyclopedias, which then become training data for LLMs <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.

### Meta SCM Formalism
To formalize this, they proposed the "Meta SCM" formalism <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>. This concept describes a higher-level Structural Causal Model (SCM) that talks about other SCMs, representing the causal insights and assumptions about the world as variables <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. An LLM might be training on correlations found in the textual representations of these causal facts <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

### Scaling Laws and LLM Evaluation
Maich is critical of evaluating LLMs' [[Causality in AI | causal]] powers based on simple metrics like accuracy on certain datasets <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>. He specifically points to the Tubingen data set, which contains obscure pairs of variables that an LLM cannot logically reason about without specific world knowledge (e.g., names like "John" or "Mary" in a causal diagram) <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>. He emphasizes the importance of considering the data quality and biases in evaluation <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.

Regarding scaling laws, Maich believes scale is certainly necessary for intelligence, drawing an analogy to the human brain's 100 billion neurons and their vast connectivity <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>. However, his personal take, biased by the [[Causality in AI | causality]] and symbolic AI perspectives, is that it will require a combination of scale and conceptual ingenuity <a class="yt-timestamp" data-t="00:36:01">[00:36:01]</a>. This aligns with the neuro-symbolic approach <a class="yt-timestamp" data-t="00:36:47">[00:36:47]</a>.

## White Box vs. Black Box Models in [[Causal AI and machine learning intersection | Causal AI]]

Maich acknowledges that humans are not always good at [[Causal inference and machine learning | causal reasoning]], especially in complex policy decisions <a class="yt-timestamp" data-t="00:38:39">[00:38:39]</a>, despite being excellent at counterfactuals in personal experience <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>. He agrees with the idea that humans can be "black box reasoners" for themselves <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.

He argues that white boxiness does not necessarily mean explainability <a class="yt-timestamp" data-t="00:42:31">[00:42:31]</a>. For example, large linear programs, while explicit and structurally understood, can be too complex for humans to process and fully explain <a class="yt-timestamp" data-t="00:43:19">[00:43:19]</a>. The concept of "explanation" itself is not universally defined in cognitive science <a class="yt-timestamp" data-t="00:42:11">[00:42:11]</a>. Maich suggests that black box models can be perfectly fine as long as they provide faithful and useful explanations <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>.

His own work, "Structural Causal Explanations" (SCE), proposes a recursive algorithm that uses a graph structure and quantitative causal knowledge (e.g., coefficients in linear causal models) to provide explanations <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>. For instance, in a [[Application of causal machine learning in medicine | medical context]], it could explain why a patient's mobility is poor by tracing it back to their health and age, even if other factors like nutrition are good <a class="yt-timestamp" data-t="00:45:39">[00:45:39]</a>. This algorithm focuses on individual-level causation, providing sound conclusions based on a causal model <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>.

## Adoption of Causality in Practice

Maich has mixed feelings about the current state of [[Application of causal machine learning in medicine | causality]] adoption <a class="yt-timestamp" data-t="00:49:52">[00:49:52]</a>. He believes there's much scientific and philosophical work still to be done <a class="yt-timestamp" data-t="00:49:58">[00:49:58]</a>. He also questions the reliance on benchmarks and "objective" metrics in [[Machine learning and causal inference methodologies | machine learning]], citing *The Myth of the Objective* <a class="yt-timestamp" data-t="00:50:30">[00:50:30]</a>.

However, he also sees significant success, especially with practitioners applying causal discovery to discover surprising relations in real-world data, such as biomedical data <a class="yt-timestamp" data-t="00:52:28">[00:52:28]</a>. He views [[Causal AI and machine learning intersection | AI]] as an assistant, enabling personalized medicine and other applications, much like AI assists mathematicians in finding new theorems <a class="yt-timestamp" data-t="00:53:25">[00:53:25]</a>.

## Collaborations and Influences

Maich collaborated with Peta Veličković from DeepMind after reaching out to him at the Eastern European Machine Learning Summer School <a class="yt-timestamp" data-t="00:54:31">[00:54:31]</a>. Their most important contribution was building a bridge between geometric deep learning (specifically graph neural networks) and [[Causality in AI | causality]] (structural causal models) <a class="yt-timestamp" data-t="00:55:40">[00:55:40]</a>, opening a new research direction <a class="yt-timestamp" data-t="00:56:31">[00:56:31]</a>.

Regarding [[Machine learning and causal inference methodologies | machine learning]] hype cycles, Maich believes the current cycle is different and not slowing down <a class="yt-timestamp" data-t="00:58:55">[00:58:55]</a>. He advocates for scientific discourse rather than departments "decoupling" from AI to avoid implications, arguing that separating AI from ML is not possible nor advisable <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>.

His personal hero from the *Oppenheimer* movie (which he viewed as a documentary) is Kurt Gödel, the logician known for his incompleteness theorems <a class="yt-timestamp" data-t="01:01:31">[01:01:31]</a>. Gödel's incredible achievements, life story, and even his humorous encounter during his US citizenship test where he found a flaw in the Constitution, make him stand out <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>.

Besides *The Book of Why* <a class="yt-timestamp" data-t="01:03:54">[01:03:54]</a>, Maich appreciates books like Randall Munroe's *What If?*, Daniel Kahneman's *Thinking, Fast and Slow*, and Johann Wolfgang von Goethe's *Faust* and *West-Eastern Divan*, which combines multicultural themes <a class="yt-timestamp" data-t="01:04:36">[01:04:36]</a>.

## Advice for Aspiring Causal Researchers

For those starting in [[Causality in AI | causality]], Maich recommends:
*   The Causal Discussion Group website: [discuss.quality.link](https://discuss.quality.link/) <a class="yt-timestamp" data-t="01:06:30">[01:06:30]</a>, which lists numerous resources.
*   Judea Pearl's *Causality* (as a reference book) <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>.
*   Jonas Peters' *Elements of Causal Inference* (especially for [[Machine learning and causal inference methodologies | machine learning]] practitioners) <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>.
*   A survey by Jean Kaddour and colleagues specific to [[Causal inference and machine learning | causal machine learning]] <a class="yt-timestamp" data-t="01:07:18">[01:07:18]</a>.
*   Lectures by Jonas Peters and Elias Bareinboim <a class="yt-timestamp" data-t="01:07:42">[01:07:42]</a>.

He emphasizes that formalism is necessary for [[Causality in AI | causality]] because it provides a formal language for discussing modeling assumptions and deriving sound conclusions <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a>. While intuition is valuable, there's a "double-edged sword" because it can lead to wrong intuitions about causation <a class="yt-timestamp" data-t="01:09:57">[01:09:57]</a>.

His final encouragement to the community is: "If you're passionate about this, if you think this is meaningful, this would be fun, I think it will be fun. So do it. Just do it." <a class="yt-timestamp" data-t="01:10:33">[01:10:33]</a>.