---
title: The role of deep learning and discrete program search in AI development
videoId: UakqL6Pj9xo
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Here is the modified article with inserted backlinks:

François Chollet, AI researcher at Google and creator of Keras, discusses the current state and future directions of Artificial Intelligence development, particularly focusing on the distinct roles and potential synergy of deep learning (exemplified by [[large_language_models_and_transfer_learning | Large Language Models or LLMs]]) and discrete program search/synthesis. This article, based on his insights, explores these two paradigms, their strengths, limitations, and how their combination might pave the way towards more general AI.

## Deep Learning and Large Language Models (LLMs)

LLMs, a prominent example of deep learning, have demonstrated significant capabilities but also possess inherent limitations according to Chollet.

### Nature and Strengths
LLMs are described as "big interpolative memor[ies]" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a> or "big parametric curve[s] fitted to a data distribution" <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. Their capabilities are scaled by attempting to "cram as much knowledge and patterns as possible into them" <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

*   **System 1 Thinking:** Deep learning models, particularly those trained with gradient descent on parametric curves, are considered a great fit for "System 1-type thinking," which includes pattern recognition, intuition, and memorization <a class="yt-timestamp" data-t="00:51:45">[00:51:45]</a>.
*   **Compute Efficiency in Learning:** The learning engine for deep learning is gradient descent, which is very compute-efficient due to a strong, informative feedback signal about where the solution lies <a class="yt-timestamp" data-t="00:50:13">[00:50:13]</a>.
*   **Reusable Building Blocks:** LLMs store reusable bits of programs, often as vector programs. Due to the need for compression within their fixed number of parameters, they learn to express new programs in terms of existing, previously learned components <a class="yt-timestamp" data-t="00:48:34">[00:48:34]</a>.

### Limitations
Despite their strengths, Chollet points out fundamental limitations.
*   **Memorization vs. Synthesis:** LLMs are very good at memorizing static programs or "a finite set of reasoning patterns" <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. When faced with a new puzzle, they tend to fetch an appropriate program from their "bank of solution programs" and reapply it, rather than performing "on-the-fly program synthesis" <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>, <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. They have a poor ability to synthesize new program templates or adapt existing ones, being "very much limited to fetching" <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>.
*   **Data Inefficiency:** Gradient descent is very data-inefficient, requiring a dense sampling of the operating space and data distribution to work effectively <a class="yt-timestamp" data-t="00:50:13">[00:50:13]</a>.
*   **Local Generalization:** Because their substrate is a "big parametric curve," LLMs are limited to "local generalization" <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>. They generalize within the data distribution they were trained on <a class="yt-timestamp" data-t="00:50:41">[00:50:41]</a>.
*   **Struggle with True Novelty:** This reliance on memorized patterns and local generalization means LLMs struggle with truly novel tasks, such as those presented by the [[arc_as_a_benchmark_for_machine_intelligence_and_its_resistance_to_memorization | ARC (Abstraction and Reasoning Corpus) benchmark]], which is designed to resist memorization <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

## Discrete Program Search and Synthesis

As an alternative or complementary approach, Chollet highlights discrete program search and program synthesis.

### Nature and Strengths
In program synthesis, a model is a "discrete graph of operators" built from a set of logical operators or a domain-specific language (DSL) <a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>.
*   **System 2 Thinking:** Discrete program search is seen as a great fit for "Type 2 thinking," which encompasses planning and reasoning. It excels at quickly figuring out a generalizable model from very few examples, such as an ARC puzzle <a class="yt-timestamp" data-t="00:51:59">[00:51:59]</a>.
*   **Data Efficiency:** The learning engine is combinatorial search. This process is extremely data-efficient, capable of learning a generalizable program from just one or two examples. This is why it performs well on ARC <a class="yt-timestamp" data-t="00:50:53">[00:50:53]</a>, <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **True Generalization:** This approach aims for broader or even "extreme generalization," moving beyond the local generalization of parametric models <a class="yt-timestamp" data-t="00:49:18">[00:49:18]</a>.

### Limitations
*   **Compute Inefficiency:** The primary drawback of discrete program search is its extreme compute inefficiency due to the risk of "combinatorial explosion" during the search process <a class="yt-timestamp" data-t="00:50:53">[00:50:53]</a>.

## The Path Forward: Hybrid Systems

Chollet argues that the future of AI development lies in merging deep learning and discrete program search, as they possess "very complementary strengths and limitations" <a class="yt-timestamp" data-t="00:51:22">[00:51:22]</a>.

### Merging Paradigms
The proposed hybrid system would have an outer structure based on discrete program search. The fundamental limitation of program search (combinatorial explosion) would be addressed by leveraging deep learning to "guide and to provide intuition in program space" <a class="yt-timestamp" data-t="00:52:37">[00:52:37]</a>, <a class="yt-timestamp" data-t="00:52:48">[00:52:48]</a>.
*   **Intuition and Guidance:** Deep learning models, acting as "intuition machines" <a class="yt-timestamp" data-t="00:53:16">[00:53:16]</a>, can suggest the initial shape of a solution, propose likely next steps in the search graph, or provide feedback on partial solutions <a class="yt-timestamp" data-t="00:53:03">[00:53:03]</a> - <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>.
*   **Knowledge Base:** Deep learning can also contribute common sense and general knowledge <a class="yt-timestamp" data-t="00:54:11">[00:54:11]</a>.
*   **On-the-Fly Synthesis Engine:** The goal is a system with an "on-the-fly synthesis engine that can adapt to new situations." This engine would fetch patterns and modules (which could be differentiable curves or algorithmic in nature) and assemble them via an intuition-guided process to create a generalizable model from very little data <a class="yt-timestamp" data-t="00:54:21">[00:54:21]</a>. Such a system, Chollet believes, "would solve ARC" <a class="yt-timestamp" data-t="00:54:56">[00:54:56]</a>.

### Hybrid Approaches and ARC
The Jack Cole approach to ARC, which involves test-time fine-tuning of an LLM on ARC tasks, is seen as an early form of program synthesis. The LLM contains numerous programming building blocks, and fine-tuning attempts to assemble these into a pattern matching the task <a class="yt-timestamp" data-t="01:14:39">[01:14:39]</a>. This represents one end of a spectrum: a "vector program database DSL of millions of building blocks" with "very shallow recombination" <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>. This contrasts with pure discrete program search, which uses a small DSL (100-200 primitives for ARC) but performs "very deep recombination" <a class="yt-timestamp" data-t="01:15:04">[01:15:04]</a>, <a class="yt-timestamp" data-t="01:16:01">[01:16:01]</a>.
The optimal solution, Chollet suggests, lies "somewhere in between" <a class="yt-timestamp" data-t="01:16:27">[01:16:27]</a>, leveraging memorization for a rich bank of primitives while also enabling deep search for broader generalization <a class="yt-timestamp" data-t="01:16:34">[01:16:34]</a>. Winners of the ARC competition are likely to be those who "manage to merge the deep learning paradigm and the discrete program search paradigm into one elegant way" <a class="yt-timestamp" data-t="01:29:16">[01:29:16]</a>.

### Impact
Successfully creating such a hybrid system, particularly one that can solve ARC, would represent the ability to "synthesize a problem-solving program from just two or three examples," which Chollet describes as "a new way to program" and "an entirely new paradigm for [[impact_of_ai_on_software_development_and_productivity | software development]]" <a class="yt-timestamp" data-t="01:26:14">[01:26:14]</a>, <a class="yt-timestamp" data-t="01:26:26">[01:26:26]</a>.

In conclusion, while deep learning models like LLMs are powerful for tasks involving pattern matching and interpolation from vast datasets, François Chollet posits that achieving more robust and general intelligence will require integrating these capabilities with the data-efficient, reasoning-oriented strengths of discrete program search and synthesis.