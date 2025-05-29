---
title: Historical Development and Key Papers on Causality and AI
videoId: FC-rNx5qGR0
---

From: [[causalpython]] <br/> 

The intersection of [[causality_in_ai | causality and AI]] is a rapidly evolving field, with significant developments in understanding how large language models (LLMs) interact with causal concepts. This article provides an overview of key papers and milestones that have shaped this area.

## Early Explorations: Feasibility and Initial Thoughts

The conversation around [[causality_in_ai | causality in AI]], specifically concerning Large Language Models (LLMs), gained significant traction in April 2023 <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.

### Understanding Causality with Large Language Models

One of the earliest position papers that explored the potential at the [[intersection_of_causality_and_ai_technologies | intersection of causality and AI technologies]] was "Understanding Causality with Large Language Models: Feasibility and Opportunities" by Chang Chong from Microsoft Research <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. This paper presented initial thoughts on what could be achieved in this domain <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.

Early experiments involved using tools like ChatGPT alongside Desi, an end-to-end causal discovery and inference algorithm, to recover causal graphs <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. At this stage, the approach to these topics was not yet systematic <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

### Causal Reasoning and Large Language Models

Following shortly in April-May 2023, the paper "Causal Reasoning and Large Language Models: Opening a New Frontier for Causality" highlighted surprising results <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>. Notably, GPT-4 demonstrated near-human level performance on the "cross counterfactual reasoning benchmark" <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>. However, challenges remained in evaluating these models, particularly concerning the extent of memorization versus genuine [[causal_reasoning_in_ai | causal reasoning]] from their training data <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>. This paper is considered one of the first technical contributions in this area <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>.

## Unpacking Causal Parrots and World Models

The concept of how LLMs handle [[causality_in_ai | causality]] was further explored in "Causal Parrots: Large Language Models May Talk Causality But Are Not Causal." This paper, co-authored by Mateusz (Mat), Morris Vrek, Dave, and Christian Casting, was inspired by an earlier work on "statistical parrots" <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.

### The "Meta-SCM" Hypothesis

The paper confirmed some prior evaluation results while also broadening the understanding of LLMs' capabilities from a causal perspective <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>. A key conceptual takeaway involves the Structural Causal Model (SCM) framework <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>. An SCM involves nodes, edges (structural information), and functions defining relationships between variables <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.

The paper introduced the concept of "meta-SCMs," hypothesizing that LLMs learn "correlations of causal facts" within their training data <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>. For example, if Wikipedia articles contain knowledge about causal structures like "altitude causes temperature," LLMs become adept at picking up these correlations <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>. This allows them to answer causal questions correctly, even without a deep "understanding" in a human sense <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>. This "correlations of causal facts" idea, coined by Christian, suggests that SCMs can generate data about other SCMs, regardless of whether that data is text or images <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>.

### The World Model Debate

This discussion ties into the ongoing debate about whether models like LLMs or video generation models (e.g., Sora) truly build an internal "world model" <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>. Judea Pearl has questioned how to test for such internal world models, a question for which there isn't a clear answer yet <a class="yt-timestamp" data-t="15:02:00">[15:02:00]</a>. While Sora produces highly realistic videos, inconsistencies suggest it builds local approximations rather than a general physics simulator <a class="yt-timestamp" data-t="16:15:00">[16:15:00]</a>. This highlights a fundamental question: what constitutes a "causal variable" within various data modalities like images or videos <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>?

## Advancements in Causal Strategies and Systematic Evaluation

### Passive Learning of Active Causal Strategies

"Passive Learning of Active Causal Strategies in Agents and Language Models" by Andrew Lampinen from DeepMind (now Google DeepMind) and colleagues, including Stephanie Chan, was another significant contribution <a class="yt-timestamp" data-t="19:16:00">[19:16:00]</a>. This paper demonstrated that language models can generalize causal structures if specific criteria are met <a class="yt-timestamp" data-t="19:33:00">[19:33:00]</a>. It introduced perspectives from cognitive science, physics, and common sense to [[causal_reasoning_in_artificial_intelligence | causal reasoning in artificial intelligence]] <a class="yt-timestamp" data-t="20:29:00">[20:29:00]</a>.

### The Duality Between Attention and Causal Inference

Chang Chong also co-authored "The Duality between Attention and Causal Inference in Foundational Models," which suggests that these models might learn causal structures or strategies under certain constrained circumstances <a class="yt-timestamp" data-t="21:46:00">[21:46:00]</a>.

### Causal Reasoning in Language Models (CaSiL)

A significant shift towards more systematic evaluation came with the paper "Causal Reasoning in Language Models (CaSiL)" by Jiying Jing and co-authored by Bernhard Schölkopf, a prominent figure in [[causality_in_ai | causality]] <a class="yt-timestamp" data-t="22:25:00">[22:25:00]</a>. This paper moved beyond intuitive evaluations, building a causal engine to generate descriptions of causal situations in natural language <a class="yt-timestamp" data-t="23:08:00">[23:08:00]</a>.

Models were tasked with answering questions across different "levels of causation" (correlational, interventional, and counterfactual queries) <a class="yt-timestamp" data-t="23:26:00">[23:26:00]</a>. Initial results showed that models often performed poorly, close to random chance <a class="yt-timestamp" data-t="23:38:00">[23:38:00]</a>. However, a key contribution was the "Causal Chain of Thought" strategy, inspired by the "Chain of Thought" approach <a class="yt-timestamp" data-t="24:01:00">[24:01:00]</a>. This strategy significantly improved performance, especially for later models like GPT-4, though still not reaching the initial enthusiastic results <a class="yt-timestamp" data-t="24:12:00">[24:12:00]</a>.

The paper also contributed a large public dataset called "Cadder," containing causal pairs with ground truths, aiding future research in [[causal_discovery_and_inference_in_ai | causal discovery and inference in AI]] <a class="yt-timestamp" data-t="24:32:00">[24:32:00]</a>.

## The Path Forward: Continuing Research and Discussion

The field of [[advancements_in_causal_modeling_and_ai | advancements in causal modeling and AI]], particularly concerning LLMs, is far from settled, necessitating ongoing discussion and cross-pollination of ideas across different disciplines <a class="yt-timestamp" data-t="21:15:00">[21:15:00]</a>.

The 38th Annual Conference on Advances in Artificial Intelligence (AAAI) in Vancouver will host a workshop dedicated to [[causality_in_ai | causality and LLMs]] <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. This event aims to foster real communication and inspire new research <a class="yt-timestamp" data-t="27:33:00">[27:33:00]</a>.

Invited speakers for the workshop include:
*   Judea Pearl (virtually) <a class="yt-timestamp" data-t="28:09:00">[28:09:00]</a>
*   Andrew Lampinen <a class="yt-timestamp" data-t="28:16:00">[28:16:00]</a>
*   Emre Kiciman from Microsoft Research <a class="yt-timestamp" data-t="28:18:00">[28:18:00]</a>
*   Marilena Vlahopoulou from Cambridge University <a class="yt-timestamp" data-t="28:24:00">[28:24:00]</a>
*   Guy Van den Broeck <a class="yt-timestamp" data-t="28:35:00">[28:35:00]</a>
*   Melanie Mitchell from Santa Fe Institute <a class="yt-timestamp" data-t="28:49:00">[28:49:00]</a>

As Judea Pearl famously stated, "As x-rays are to the surgeon, graphs are for causation," emphasizing the necessity of graphical representations for [[causal_reasoning_in_artificial_intelligence | reasoning about causal models]] <a class="yt-timestamp" data-t="29:40:00">[29:40:00]</a>. This quote underscores the foundational role of understanding causality in the development of truly intelligent systems.