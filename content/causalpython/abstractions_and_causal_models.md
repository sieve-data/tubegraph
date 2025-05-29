---
title: Abstractions and Causal Models
videoId: rM25vt_ZmFc
---

From: [[causalpython]] <br/> 

Abstractions are a key concept in computer science and play a crucial role in [[causal_reasoning_and_structural_causal_models | causal reasoning]] <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. They allow for the understanding of complex systems by looking at them from different scopes and levels of description <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.

## Defining Causal Abstractions

The concept of abstractions in a [[causality_and_causal_models | causal]] sense originated from a 2017 paper by Rünz et al. on the "causal consistency of structural causal models" (SCMs) <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>. This work explores how to equate two different [[causal_reasoning_and_structural_causal_models | structural causal models]] (SCMs) when they represent different levels of abstraction <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.

The core idea involves distinguishing between low-level and high-level variables <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>. For example, total cholesterol in the body can be considered a high-level variable, while its components, HDL and LDL lipoproteins, are low-level variables <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>. The challenge in [[causal_reasoning_and_structural_causal_models | causal]] abstraction, particularly within Pearl's formalism, is to ensure that [[interventions_and_causal_models | interventions]] made at one level are consistently respected at other levels <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.

This perspective leads to fundamental questions such as "where do the variables come from?" or "what is even a [[causality_and_causal_models | causal]] variable to begin with?" <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>. Abstractions are crucial for addressing these questions by allowing us to capture characteristics of systems at different scopes <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.

## Causality as a Useful Abstraction

[[Causality and Causal Models | Causality]] can be viewed as a "useful shortcut" or a "useful abstraction" <a class="yt-timestamp" data-t="13:01:00">[13:01:00]</a>. This concept is discussed by Judea Pearl, and also by Jonas Peters, Dominik Janzing, and Bernhard Schölkopf in their book *Elements of Causal Inference* (2017) <a class="yt-timestamp" data-t="15:02:00">[15:02:02]</a>.

In physics, a system can be described by fine-grained differential equations <a class="yt-timestamp" data-t="15:24:00">[15:24:00]</a>. [[Causality and Causal Models | Causality]] acts as a second rung on this hierarchy, kicking out unnecessary detail while still being sufficient and necessary to answer specific hypotheses <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>. This can be compared to the distinction between model-based and model-free reinforcement learning, where an agent doesn't need a full model to determine the next best action, but rather an intuitive understanding <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>.

> [!EXAMPLE] Neuroscience and Abstraction
> In neuroscience, fields like connectomics aim to build a detailed map of the brain at the neuron level, capturing every detail <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>. While this level of detail is certainly sufficient, it might be *too* detailed for many hypotheses <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>. Just as a physicist chooses a level of abstraction for a problem, so too must researchers choose the appropriate level for [[causal_reasoning_and_structural_causal_models | causal models]] <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.

## Abstractions in Large Language Models and Causal Reasoning

The concept of abstractions is also relevant to the discussion surrounding [[large_language_models_and_causal_reasoning | Large Language Models]] (LLMs) <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>. The "meta SCM" formalism proposes that LLMs, which primarily learn correlations, can answer [[causality_and_causal_models | causal]] questions correctly because there are underlying correlations among [[causality_and_causal_models | causal]] facts themselves <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>.

> [!INFO] The Meta SCM Conjecture
> The conjecture states that LLMs are trained on existing [[causality_and_causal_models | causal]] knowledge, which is often codified in textual representations (e.g., textbooks, Wikipedia) <a class="yt-timestamp" data-t="22:46:00">[22:46:00]</a>. If one asks, for instance, if altitude causes temperature, the text-based knowledge base likely contains the correct [[causality_and_causal_models | causal]] direction <a class="yt-timestamp" data-t="22:14:00">[22:14:00]</a>. The meta SCM is a higher-level structural [[causal model]] that describes relationships between other SCMs or causal statements <a class="yt-timestamp" data-t="26:01:00">[26:01:00]</a>. This implies a hierarchy where the LLM's learning of textual correlations about [[causal]] facts is formalized <a class="yt-timestamp" data-t="26:27:00">[26:27:00]</a>.

The ability of LLMs like GPT-4 to perform well on [[causal_reasoning_in_language_models | causal reasoning]] tasks might stem from their capacity to implicitly learn these correlations of [[causality_and_causal_models | causal]] facts from vast amounts of text data <a class="yt-timestamp" data-t="22:51:00">[22:51:00]</a>. However, this doesn't necessarily mean the LLM "understands" in a human sense, but rather "knows" by leveraging its trained knowledge base <a class="yt-timestamp" data-t="24:51:00">[24:51:00]</a>.

## Abstractions and Explainability in Causal Models

The debate around "white-box" versus "black-box" models and explainability in AI is also tied to abstractions <a class="yt-timestamp" data-t="37:32:00">[37:32:00]</a>. While humans are good at generating plausible [[causal]] explanations (e.g., counterfactual reasoning in personal experience <a class="yt-timestamp" data-t="38:01:00">[38:01:00]</a>), these explanations might not always be accurate or reflect true underlying causes, as seen in neuroscientific experiments with split-brain patients <a class="yt-timestamp" data-t="40:48:00">[40:48:00]</a>.

The desire for white-box models in AI stems from the hope that they will be inherently understandable and explainable <a class="yt-timestamp" data-t="41:47:00">[41:47:00]</a>. However, even explicit, white-box systems like large linear programs can become too complex for humans to process and understand at scale <a class="yt-timestamp" data-t="43:35:00">[43:35:00]</a>.

This suggests that white-boxiness and explainability are intertwined but distinct concepts <a class="yt-timestamp" data-t="41:35:00">[41:35:00]</a>. The goal should be to obtain faithful explanations from systems, regardless of whether they are black-box or white-box <a class="yt-timestamp" data-t="44:57:00">[44:57:00]</a>.

## Current and Future Directions

The field of [[causality_and_causal_models | causal]] research continues to develop, with two main strands:
1.  **Causal Discovery**: The problem of learning the [[causal]] graph structure from data <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.
2.  **Causal Inference**: Modeling assumptions and drawing sound conclusions based on a given graph <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>.

A significant challenge lies in bridging the gap between these two strands, and also in exploring more philosophical questions about [[causality and causal models | causality]], such as defining [[causality_and_causal_models | causal]] variables and broadening the conceptual horizon <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>. Connecting [[causality_and_causal_models | causality]] with logic and symbolic AI is another promising area, as demonstrated by the NeurIPS 2022 workshop titled "Neurocausal and Symbolic AI" <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

Despite significant progress in [[applications_of_causal_models_in_business_and_marketing | industrial adoption]], challenges remain, such as the need for standardized benchmarks to effectively [[evaluating_causal_models_in_practice | evaluate causal models]] <a class="yt-timestamp" data-t="50:28:00">[50:28:00]</a>. Ultimately, [[causality_and_causal_models | causal]] AI is envisioned as an "AI assistant" that helps in personalized applications, such as medicine <a class="yt-timestamp" data-t="53:28:00">[53:28:00]</a>. Building trust in these AI systems will be paramount, and [[building_trust_in_ai_systems_through_causal_models | causal models]] contribute to this trust by providing a framework for understanding `why` something happens.