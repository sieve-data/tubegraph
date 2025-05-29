---
title: Systematic evaluation of language models in causality
videoId: FC-rNx5qGR0
---

From: [[causalpython]] <br/> 

The intersection of [[causality and large language models | causality]] and [[large language models and causality | large language models]] (LLMs) is a rapidly evolving field, marked by an increasing focus on systematically evaluating the causal reasoning capabilities of these models <a class="yt-timestamp" data-t="02:29:02">[02:29:02]</a>.

## Early Explorations and Initial Benchmarks

Early work in [[large language models and causality | LLMs]] and [[causality | causality]] began with exploring the feasibility and opportunities at their intersection <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>. A paper from April 2023, "Understanding [[causality in large language models | causality]] with [[large language models and causality | large language models]]: feasibility and opportunities" by Chang Chong from Microsoft Research, was an early position paper discussing what could be done <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. This paper explored the potential uses of [[large language models and causality | LLMs]] for causal discovery and causal inference, including their roles as feature or partial knowledge extractors <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>.

Another significant paper from April/May 2023, "[[Causal reasoning in language models | Causal reasoning]] and [[large language models | large language models]]: opening a new frontier for [[causality | causality]]", showed surprising results <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>. For instance, GPT-4 achieved "almost human-level performance" on the cross-counterfactual reasoning benchmark <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>. However, it was acknowledged that these were early papers, and good methods to evaluate these models were lacking, making it difficult to discern if the performance was due to memorization from training data or genuine reasoning <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

## The "Causal Parrots" Hypothesis

A paper titled "Causal Parrots: [[Large language models and causality | Large Language Models]] May Talk [[Causality | Causality]] But Are Not Causal" by Mat Vlastelica, Dave Damad, and Christian Schunn, inspired by an early paper on "statistical parrots," broadened the picture of [[evaluating causal models in practice | evaluating causal models]] <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>. The key conceptual insight of this paper revolves around the structural causal model (SCM) as a modeling framework <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.

The authors hypothesized that [[large language models and causality | LLMs]] might not "understand" [[causality | causality]] in a typical sense but rather learn "correlations of causal facts" <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>. This means that if training data (like Wikipedia) contains knowledge about causal structures (e.g., "altitude causes temperature"), and an [[large language models and causality | LLM]] is adept at picking up these correlations, it can correctly answer causal questions without true causal understanding <a class="yt-timestamp" data-t="13:26:00">[13:26:00]</a>. This concept, termed "meta-SCMs," suggests that the models learn from data that itself contains knowledge about causal facts and structure <a class="yt-timestamp" data-t="13:20:00">[13:20:00]</a>. This idea is a conjecture and has not been definitively proven <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.

This perspective suggests that the "correlations of causal effects" idea is general, potentially applying to any domain or type of representation <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>.

## Towards More Systematic Evaluation

The shift towards more systematic evaluation is evident in later research.

### Passive Learning of Active Causal Strategies

Andrew Lampinen from DeepMind (now Google DeepMind) and colleagues, including Stephanie Chan, authored "Passive learning of active causal strategies in agents and [[language models | language models]]" <a class="yt-timestamp" data-t="19:16:00">[19:16:00]</a>. This paper showed that [[large language models and causality | language models]] can generalize causal structures if certain criteria are met <a class="yt-timestamp" data-t="19:30:00">[19:30:00]</a>. This work highlights the importance of considering [[causality | causality]] from various perspectives, including cognitive science, physics, and common sense <a class="yt-timestamp" data-t="20:29:00">[20:29:00]</a>.

### The Duality Between Attention and Causal Inference

Another paper by Chang Chong explored "The Duality between Attention and [[Causal Inference in Language Models | Causal Inference]] in Foundational Models" <a class="yt-timestamp" data-t="21:46:00">[21:46:00]</a>. This research suggests that [[large language models and causality | models]] might learn causal structures or strategies under specific, constrained circumstances <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>. The need to constrain the problem space to meaningfully discuss [[causality | causality]] is a typical aspect of causal thinking <a class="yt-timestamp" data-t="22:13:00">[22:13:00]</a>.

### SEAL: A Systematic Benchmark

The paper "SEAL: Assessing [[Causal reasoning in language models | Causal Reasoning]] in [[language models | Language Models]]" by Jiaying Jing and co-authored by Bernhard Schölkopf, represents a significant step towards systematic evaluation <a class="yt-timestamp" data-t="22:37:00">[22:37:00]</a>.

Key contributions of the SEAL paper include:
*   **Causal Engine:** The authors built a causal engine that generates descriptions of causal situations in natural language with ground truths <a class="yt-timestamp" data-t="23:11:00">[23:11:00]</a>.
*   **Task Levels:** Tasks are designed to test different levels of [[causality | causation]], including correlational, interventional, and counterfactual queries <a class="yt-timestamp" data-t="23:26:00">[23:26:00]</a>.
*   **Performance:** Initially, [[large language models and causality | models]] in a raw setting often performed at a random level <a class="yt-timestamp" data-t="23:41:00">[23:41:00]</a>.
*   **Causal Chain of Thought:** A major contribution is the "Causal Chain of Thought" strategy, inspired by the Chain of Thought strategy <a class="yt-timestamp" data-t="24:01:00">[24:01:00]</a>. This strategy significantly improves the performance of later [[large language models and causality | models]] like GPT-4 on these tasks, bringing them much higher than random chance <a class="yt-timestamp" data-t="24:09:00">[24:09:00]</a>.
*   **Cadder Dataset:** The paper also introduced Cadder, a large public dataset of causal pairs with ground truths, available for future research <a class="yt-timestamp" data-t="24:32:00">[24:32:00]</a>.

This systematic approach, going deep into constructing the entire evaluation, moves beyond simply asking models for responses <a class="yt-timestamp" data-t="25:57:00">[25:57:00]</a>.

## The World Model Debate and Future Directions

The discussion around [[large language models and causality | LLMs]] and [[causal reasoning in language models | causal reasoning]] ties into the broader debate on whether these models construct internal "world models" <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>. Influential figures like Judea Pearl question how to know if these models build a world model and how to test for it, noting that there isn't a good answer currently <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.

For instance, OpenAI's Sora model, which produces realistic videos, has been suggested to build a world model <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>. However, it's argued that Sora likely builds "local approximations of a world model," rather than a general physics simulator, given observed inconsistencies in its videos <a class="yt-timestamp" data-t="16:15:00">[16:15:00]</a>. The "correlations of causal effects" idea could also apply here, where models might be learning relationships within images or video data, even raising philosophical questions about the existence of [[causality | causality]] within images themselves <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>.

The field of [[causality and large language models | causality]] and [[large language models | large language models]] is far from settled, requiring more ideas, discussion, and cross-pollination between different fields to move forward <a class="yt-timestamp" data-t="21:15:00">[21:15:00]</a>. Conferences and [[workshop on large language models and causality | workshops]] provide platforms for this crucial exchange, featuring leading researchers and discussions on whether [[large language models and causal reasoning | LLMs reason]] and how they do so <a class="yt-timestamp" data-t="27:33:00">[27:33:00]</a>.