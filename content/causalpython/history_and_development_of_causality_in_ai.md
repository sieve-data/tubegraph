---
title: History and development of causality in AI
videoId: FC-rNx5qGR0
---

From: [[causalpython]] <br/> 

The intersection of [[causality_in_artificial_intelligence | causality]] and large language models (LLMs) is a significant area of focus in modern AI research <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This field is concerned with how AI, like humans, needs to adapt to and understand an ever-changing world <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Early Explorations (2023)

The formal exploration of [[causality_in_artificial_intelligence | causality]] in LLMs largely began in April 2023 with a seminal position paper by Chang Chong from Microsoft Research, titled "Understanding [[causality_in_artificial_intelligence | Causality]] with Large Language Models: Feasibility and Opportunities" <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. This paper was among the first to discuss the potential intersection of these two fields <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

Initial demonstrations included using Chat GPT alongside Desi, an end-to-end causal discovery and inference algorithm, to recover causal graphs <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. At this early stage, systematic approaches to these topics were still undefined <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. The paper explored the potential for LLMs in causal discovery and [[causal_ai_and_machine_learning | causal inference]], serving as feature extractors or partial knowledge extractors <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. The question was posed whether the focus should be on "causal discovery" or "causal knowledge extraction" with LLMs <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

In April/May 2023, another significant paper, "Causal Reasoning and Large Language Models: Opening a New Frontier for [[causality_in_artificial_intelligence | Causality]]", emerged <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This paper presented surprising results, including GPT-4 achieving near-human performance on the cross-counterfactual reasoning benchmark <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. However, early evaluation methods were intuitive rather than systematic, and the influence of training data memorization on performance was unclear <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. This paper was considered the first technical work in this intersection, moving towards evaluation <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

## Critiques and Conceptual Frameworks

A paper titled "Causal Parrots: Large Language Models May Talk [[causality_in_artificial_intelligence | Causality]] But Are Not Causal" by M. v. R. Mate, Morris Riedel, Dave Madras, and Christian Kading, offered a critical perspective <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. The title was inspired by an earlier paper on statistical parrots <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. This paper confirmed some prior evaluation results while broadening the understanding <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

Key insights from "Causal Parrots" include:
*   **Structural Causal Models (SCMs)**: LLMs, while performing well, may not operate at the same hierarchical level as SCMs, which recursively generate data containing knowledge about causal facts and structure <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. SCMs involve nodes, structural information about nodes and edges, and functions between edges <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Meta-SCMs and Correlations of Causal Facts**: The paper hypothesizes that LLMs learn from data sources like Wikipedia, which collate information on causal structures (e.g., altitude causing temperature). LLMs excel at picking up these "correlations of causal facts" <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>, allowing them to answer causally correct questions without necessarily understanding causality in a human sense <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. This concept of "correlations of causal facts" is a conjecture and not yet proven <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. This idea is more general and could apply to any domain or representation type, implying SCMs can generate data of other SCMs, regardless of whether it's text or images <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

The discussion extends to the debate about whether models like Jepa and Sora build an internal "world model" <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. Judia Pearl has questioned how to test for such a model <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. While Sora produces realistic videos, inconsistencies suggest it builds local approximations of a world model rather than a general physics simulator <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

Further philosophical questions arise regarding [[causality_in_artificial_intelligence | causality]] in images versus video, and its physical nature, including the role of time <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. The work of Sander Becka on "what a causal variable actually is" is highlighted as a fundamental and deep question for advancing the field <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

## Learning Causal Strategies

Another notable paper, "Passive Learning of Active Causal Strategies in Agents and Language Models" by Andrew Lampinen from Google DeepMind and colleagues, demonstrated that language models can generalize causal structures under certain criteria <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. This work emphasizes thinking about [[causality_in_artificial_intelligence | causality]] beyond specific frameworks, incorporating cognitive science, physics, and common sense perspectives <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.

A related paper by Chang Chong explored the duality between attention and [[causal_ai_and_machine_learning | causal inference]] in foundational models, showing that models might learn causal structures or strategies under constrained circumstances <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. This highlights the typical need to constrain the problem space in causal thinking to derive meaningful conclusions <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

## Systematic Evaluation

Progress shifted towards more systematic evaluation with papers like "SEAL: Assessing Causal Reasoning in Language Models" by J. Jing and Bernhard Schölkopf <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>. This paper introduced a "causal engine" to generate descriptions of causal situations in natural language with ground truths <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>. Models were tasked with correlational, interventional, and counterfactual queries <a class="yt-timestamp" data-t="00:23:33">[00:23:33]</a>.

Key findings from "SEAL" include:
*   **Performance**: LLMs generally perform poorly in raw settings, often at random chance levels, on these tasks <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>.
*   **Causal Chain of Thought**: A strategy inspired by the Chain of Thought, called "Causal Chain of Thought," significantly improves performance for later models like GPT-4, though still not matching earlier enthusiastic results <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.
*   **CADDer Dataset**: The paper also introduced CADDer, a large public dataset of causal pairs with ground truths, facilitating future research <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>. This dataset confirms that the evaluated quantities are indeed causal, following the "letter of causation" as defined by Pearl <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>.

This field remains far from settled, requiring continued discussion, cross-pollination of ideas, and new research <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

> [!quote] Judia Pearl
> "As x-rays are to the surgeon, graphs are for causation." <a class="yt-timestamp" data-t="00:29:44">[00:29:44]</a>