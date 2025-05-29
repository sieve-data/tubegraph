---
title: Abstractions in causal reasoning
videoId: rM25vt_ZmFc
---

From: [[causalpython]] <br/> 

In [[causal_reasoning_in_artificial_intelligence | causal reasoning]], particularly within the realm of AI and machine learning, abstractions play a crucial role in simplifying complex systems and enabling meaningful analysis. The concept of abstraction allows researchers to view systems at different levels of detail, from fine-grained physical laws to higher-level, more intuitive causal relationships <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## Definition and Importance
For a computer scientist, abstraction is a key concept <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. In a causal context, abstractions involve equating two different [[understanding_and_applying_causal_graphs | structural causal models]] (SCMs) under conditions that allow for different levels of detail <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This means having low-level variables that compose a high-level variable, while still respecting possible interventions <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

A classic example of this is cholesterol in the body <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. "Total cholesterol" is a high-level variable, whereas its components like HDL and LDL are low-level variables. Understanding the causal relationships requires considering how interventions on these low-level components affect the high-level one <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

The importance of abstractions stems from fundamental questions in [[causal_reasoning_in_ai | causal AI]]:
*   Where do [[understanding_and_applying_causal_graphs | causal graphs]] come from? <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>
*   Where do the variables themselves come from? <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>
*   What constitutes a "causal variable" in the first place? <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>

Abstractions are essential for understanding how to represent and learn these variables, allowing systems to look at things from different scopes while still capturing their essential characteristics <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. For autonomous systems, making sense of abstractions is a crucial first step in interacting with the world <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

## Causality as a "Useful Abstraction"
The idea of causality itself can be viewed as a "convenient shortcut" or a "useful abstraction" <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This perspective aligns with Bertrand Russell's argument against causality and Pearl's counter-argument, suggesting that while causality might not exist at the most fundamental physical level, it is a valuable framework for understanding reality <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.

In *Elements of Causal Inference*, authors Jonas Peters, Bernhard Schölkopf, and Dominik Janzing present a table showing that differential equations (representing the most fine-grained physics of a system) are one level of abstraction, and causality is a "useful abstraction" at a second rung <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. This means it removes unnecessary detail from the underlying physical model while still being sufficient and necessary to answer specific causal hypotheses <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.

Analogies supporting this view include:
*   **Model-free reinforcement learning:** A baseball player doesn't calculate complex physics to hit a ball; their actions are based on an intuitive, model-free understanding of what to do next <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. This suggests that a full, detailed model is not always required for effective action.
*   **Connectomics in Neuroscience:** Mapping the brain at the neuron level (micrometer/nanometer scale) might capture everything about its functioning, but it's often too detailed for specific hypotheses about brain function <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. The level of abstraction needed depends on the question being asked <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

## Current Challenges and Future Directions
Despite progress, bridging the gap between [[causal_discovery_and_inference_in_ai | causal discovery]] (getting the graph from data) and [[causal_inference_in_practical_applications | causal inference]] (making sound conclusions based on assumptions) remains a challenge <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. There is also a need for more philosophical inquiry, asking fundamental questions that may broaden the horizon of [[causal_reasoning_in_artificial_intelligence | causal research]] <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

The connection of abstraction to logic is also highlighted. The 2022 NeurIPS workshop "Neuro-Causal and Symbolic AI" explored the intersection of neural networks ("neuro"), causality, and logic-based/symbolic AI, suggesting that these are "two sides of the same coin" <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

> "I think it's about interfaces, about broadening The Horizon these are missing things..." <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>

## Abstractions and Large Language Models (LLMs)
The concept of meta-SCMs (Structural Causal Models) is proposed to explain how [[generative_ai_and_causal_reasoning | Large Language Models]] (LLMs) can answer causal questions, despite primarily learning correlations <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. The conjecture is that LLMs learn "correlations of causal facts" from their training data <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. When a textbook discusses altitude causing temperature, an LLM learns this correlation between the question and the correct causal answer <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.

Meta-SCMs represent a higher hierarchical level, where one SCM talks about the causal insights (e.g., altitude causes temperature) that are then recorded in textual form. The LLM then trains on these textual representations of causal knowledge <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. This suggests that the behavioral aspect of *how* knowledge was acquired (through experiment or learning from text) becomes indistinguishable to the LLM <a class="yt-timestamp" data-t="00:28:32">[00:28:32]</a>.

## Conclusion
Abstractions are not just a convenient tool but a necessary component for understanding and developing [[causal_reasoning_in_ai | causal AI]]. They allow for focusing on relevant information at different levels of detail, simplifying complex systems, and bridging theoretical concepts with practical applications. The field continues to explore how to best define and utilize these abstractions to advance [[causal_inference_in_practical_applications | causal inference]] and enable more intelligent systems.