---
title: Large Language Models and causation
videoId: rM25vt_ZmFc
---

From: [[causalpython]] <br/> 

Maich, a dedicated researcher with interests in AI, philosophy, and neuroscience, has co-authored papers at the intersection of [[Causality and large language models | causality and large language models]] <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. He co-organized the NeurIPS Causal workshop in 2022 <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. His journey into [[machine_learning_and_causality | machine learning and causality]] began with Judea Pearl's "The Book of Why," which "sparked the flame of interest" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. He initially studied computer security and robotics before stumbling upon the book during his master's studies <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. His underlying motivation across these fields has been the foundational question of trying to understand "what intelligence is" and getting it "operationalized" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

He believes that causal reasoning is "necessary but not necessarily sufficient for intelligence" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, differentiating his view from those who might argue it's also sufficient <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Maich's Position on Large Language Models and Causality

Maich advocates for greater transparency in academic papers regarding researchers' philosophical grounding, including their stance on the [[large_language_models_and_causality | scaling hypothesis for LLMs]] <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. He considers himself an advocate of [[large_language_models_and_causality | LLMs]] for their capabilities <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.

However, from a causal perspective, his primary question is whether [[large_language_models_and_causality | LLMs]] are truly causal <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>. While models like GPT-4 show impressive performance on causal questions, significantly outperforming GPT-3, he notes that "it's actually incredible" <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. This leads to the question: "when it gets it right, why does it get it right?" <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>

### The "Correlations of Causal Facts" Conjecture and Meta SCM

Maich and his colleagues propose the "correlations of causal facts" conjecture to explain how [[large_language_models_and_causality | LLMs]] perform well on causal questions <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.

> "If they only learn correlations, then for them to answer some causal questions correctly, that would imply that there were some correlations on these causal questions and causal answers" <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.

This intuition suggests that [[large_language_models_and_causality | LLMs]] train on existing causal knowledge, which is often textual <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. For example, if a textbook states that altitude causes temperature, an [[large_language_models_and_causality | LLM]] learning to predict the next best word would likely associate "causing" with altitude and temperature, given sufficient textual data <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.

To formalize this, they introduce the concept of **Meta Structural Causal Models (Meta SCMs)** <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>. A Meta SCM is an SCM on a "meta level" or higher level of hierarchy that talks about other SCMs <a class="yt-timestamp" data-t="00:26:18">[00:26:18]</a>. It functions as a "dance between two models" <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>:
1.  A regular SCM (e.g., altitude influencing temperature) <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>.
2.  A Meta SCM that captures insights about the first SCM itself, such as the assumption that altitude causes temperature <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>.

This implies that the [[large_language_models_and_causality | LLMs]] are training on correlations found in the training data related to these causal facts <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

[!NOTE]
Maich emphasizes that this is a conjecture, as empirical results are available, but no definite proof exists <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>.

### Scaling Laws and LLM Performance

The speaker discusses [[large_language_models_and_causality | scaling laws]] in the context of [[large_language_models_and_causality | LLMs]] and their causal reasoning abilities <a class="yt-timestamp" data-t="00:34:29">[00:34:29]</a>. He acknowledges that GPT-4 performs significantly better than previous generations, which some attribute to scale <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>. However, he believes that while scale is certainly necessary, ultimate success will be a "combination of both" scale and "ingenuity and conceptual development" <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>. He sees a future where AI acts as an assistant, especially in fields like personalized medicine <a class="yt-timestamp" data-t="00:53:28">[00:53:28]</a>.

### Critique of Evaluation Benchmarks

Maich is critical of some conclusions drawn from [[large_language_models_and_causality | LLMs]]' performance on causal tasks <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>. He specifically mentions the **Tuebingen data set**, used to evaluate LLMs' causal powers <a class="yt-timestamp" data-t="00:30:39">[00:30:39]</a>. While the models show high accuracy on this dataset, he argues that the dataset contains "very obscure pairs" of variables <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>. He gives an example of variables like "something produced by some object X at time Y," making it difficult for an [[large_language_models_and_causality | LLM]] to infer causality if it doesn't understand the underlying concepts or names <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>.

[!CAUTION]
Maich states that relying solely on "very simple metrics like accuracy" and not considering the quality of the data can lead to misleading conclusions <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.

## [[Logical reasoning in large language models | Logical Reasoning]] and Abstraction in Causality

Maich believes that the connection between [[machine_learning_and_causality | machine learning and causality]] needs to be broadened <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. He highlights the importance of **abstractions** in causal research <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. Abstractions, in a causal sense, involve understanding how different levels of variables (e.g., total cholesterol vs. HDL/LDL) relate within [[machine_learning_and_causal_inference_methodologies | structural causal models (SCMs)]] while respecting interventions <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This concept helps address fundamental questions like "where do the variables come from?" and "what is even a causal variable?" <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

Maich also emphasizes the missing connection to [[logical_reasoning_in_large_language_models | logic]] in causal research <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. He co-organized the 2022 NeurIPS [[workshop_on_large_language_models_and_causality_at_aaai_2024 | workshop on large language models and causality at AAAI 2024]] titled "Neuro-Causal and Symbolic AI," which aimed to bridge neural networks, causality, and logic-based (symbolic) AI <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. He sees causality and logic as "two sides of the same coin" <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

He agrees with Judea Pearl's idea that causality can be viewed as a "useful shortcut" or "useful abstraction" <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>, kicking out unnecessary details from physical models while still being sufficient and necessary for addressing specific hypotheses <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. This aligns with the idea that complex systems like traffic congestion don't require focusing on individual screws but rather higher-level descriptions <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

### Explainability and White Box Models

Maich discusses the debate around white box versus black box models in [[machine_learning_and_causal_inference_methodologies | causal AI]] <a class="yt-timestamp" data-t="00:37:32">[00:37:32]</a>. While the community often desires white box models for understanding, he argues that "white boxiness and explanations are kind of intertwined but they are still independent concepts" <a class="yt-timestamp" data-t="00:41:35">[00:41:35]</a>. He points out that even explicitly constructed white box models, like large linear programs, can become uninterpretable to humans at scale <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>.

> "Explanation does not go along white boxiness... Black box can just be fine as long as we get explanations from that system that are faithful and that do the job" <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.

He introduces their work on **Structural Causal Explanations**, a recursive algorithm that uses graph structure and quantitative knowledge (e.g., coefficients in linear causal models) to provide causal explanations <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>. An example is explaining why an individual patient's mobility is poor based on their health and age, even when their nutrition is good <a class="yt-timestamp" data-t="00:45:39">[00:45:39]</a>. This provides "individualist causation" rather than population-level "type causation" <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>.

### Hype Cycles in Machine Learning

Maich reflects on the "hype cycles" in [[machine_learning_and_causality | machine learning]] <a class="yt-timestamp" data-t="00:57:09">[00:57:09]</a>. Historically, there have been "AI winters" following periods of exaggerated expectations <a class="yt-timestamp" data-t="00:57:38">[00:57:38]</a>. However, he feels that the current phase of growth in AI "doesn't feel like it's slowing down; it's just increasing" <a class="yt-timestamp" data-t="00:58:55">[00:58:55]</a>. He disagrees with the notion of "toning down" the buzz, emphasizing the importance of scientific discourse and not separating AI from [[machine_learning_and_causality | machine learning]] <a class="yt-timestamp" data-t="00:59:40">[00:59:40]</a>.

### Recommendations for Learning Causality

For those starting in causality, Maich recommends:
*   The "Causality" textbook by Pearl (as a reference book) <a class="yt-timestamp" data-t="01:06:49">[01:06:49]</a>.
*   "Elements of Causal Inference" by Jonas Peters and others (for those from a [[machine_learning_and_causality | machine learning]] background) <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>.
*   A survey on [[machine_learning_and_causality | machine learning and causality]] by Jean-Baptiste Cadeau <a class="yt-timestamp" data-t="01:07:20">[01:07:20]</a>.
*   Lectures by Jonas Peters and Elias Bareinboim <a class="yt-timestamp" data-t="01:07:42">[01:07:42]</a>.
*   The Causal Discussion Group website (`discuss.causality.link`) and its Slack channel <a class="yt-timestamp" data-t="01:06:30">[01:06:30]</a>.

He acknowledges that [[machine_learning_and_causality | causality]] is often taught in a formalized way, and he believes that "formalism seems necessary" for discussing modeling assumptions and drawing sound conclusions <a class="yt-timestamp" data-t="01:09:02">[01:09:02]</a>. While intuition can be helpful, he warns that "there's a lot of wrong intuition...about causation" <a class="yt-timestamp" data-t="01:09:58">[01:09:58]</a>. His advice to those starting their journey in causality is simple: "If you're passionate about this, if you think this is meaningful, this would be fun, I think it will be fun, so do it. Just do it" <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>.