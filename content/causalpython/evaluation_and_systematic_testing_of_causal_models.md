---
title: Evaluation and Systematic Testing of Causal Models
videoId: FC-rNx5qGR0
---

From: [[causalpython]] <br/> 

The evaluation and systematic testing of [[structural_causal_models_and_causal_discovery | causal models]] and large language models (LLMs) in their ability to perform [[machine_learning_and_causal_inference_methodologies | causal inference]] has been a significant area of focus and discussion in recent research.

## Early Explorations of Causality and LLMs

The intersection of [[structural_causal_models_and_causal_discovery | causality]] and LLMs began to be explored in early 2023. A foundational paper, "Understanding Causality with Large Language Models: Feasibility and Opportunities" by Chang Chong from Microsoft Research, was an early position paper discussing potential uses of LLMs for [[structural_causal_models_and_causal_discovery | causal discovery]] and [[machine_learning_and_causal_inference_methodologies | causal inference]] <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This paper also highlighted the use of tools like Desi, an end-to-end [[structural_causal_models_and_causal_discovery | causal discovery]] and inference algorithm, alongside ChatGPT to recover causal graphs <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

Another key early paper, "Causal Reasoning and Large Language Models: Opening a New Frontier for Causality" (April/May 2023), presented surprising results, including GPT-4 achieving almost human-level performance on a cross-counterfactual reasoning benchmark <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. However, early research faced [[challenges_in_evaluating_causal_models | challenges in evaluating causal models]], with questions arising about what was in the training data, the extent of memorization, and potential reasoning capabilities <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Causal Parrots: A Conceptual Framework

The paper "Causal Parrots: Large Language Models May Talk Causality But Are Not Causal," co-authored by Mate (one of the speakers), Morris W., Dave, and Christian, offered a different perspective on evaluation <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This work aimed to confirm and broaden the picture of earlier findings.

> [!NOTE] Key Insights
> The core conceptual takeaway from "Causal Parrots" is related to the [[structural_causal_models_and_causal_discovery | structural causal model]] (SCM) framework <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. The authors hypothesize that LLMs learn "correlations of causal facts" (a term coined by Christian) from their training data, such as Wikipedia, where causal relationships (e.g., altitude causes temperature) are implicitly collated <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. This suggests that LLMs can correctly answer causal questions because they are adept at picking up these correlations, rather than inherently understanding causality in the way a human might <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. The paper introduces the concept of "meta SCMs," where an SCM generates data that itself contains knowledge about causal facts and structure <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

This idea of "correlations of causal facts" is more general and could apply to any domain or type of representation, whether text or images, where SCMs can generate data about other SCMs <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.

## Challenges in Evaluating Internal World Models

A significant [[challenges_in_evaluating_causal_models | challenge in evaluating causal models]] from LLMs lies in determining if they build an internal "world model." Judia Pearl has raised this question, asking how researchers can actually know and test for such a capability <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

This challenge is exemplified by models like OpenAI's Sora, which produces realistically looking videos <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. While impressive, inconsistencies in Sora's videos suggest it does not build a general physics simulator or a comprehensive world model, but rather many local approximations that produce realistic appearances <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

## Learning and Generalizing Causal Structures

Research has also explored whether LLMs can learn and generalize causal structures:

*   **"Passive Learning of Active Causal Strategies in Agents and Language Models"** by Andrew Lampinen (DeepMind/Google DeepMind) and colleagues showed that language models *can* generalize causal structures if certain criteria are met <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. Andrew Lampinen was an invited speaker at the related workshop <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
*   **"The Duality between Attention and Causal Inference in Foundational Models"** by Chang Chong suggested that models might possibly learn causal structures or strategies under certain circumstances, implying the need to constrain the problem space to talk meaningfully about [[structural_causal_models_and_causal_discovery | causality]] <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.

## Systematic Evaluation Approaches

The move towards more rigorous and [[challenges_in_evaluating_causal_models | systematic evaluation of causal models]] and LLMs is evident in later research:

*   **"SEAL: Assessing Causal Reasoning in Language Models"** by Jiing Jing and Bernard Schölkopf represents a significant step in systematic evaluation <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.
    *   **Causal Engine:** The authors built a causal engine to generate descriptions of causal situations in natural language, along with ground truths <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>.
    *   **Levels of Causation:** Models were tested on tasks involving different levels of causation: correlational, interventional, and counterfactual queries <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>.
    *   **Performance:** Initially, most LLMs performed poorly, often at random chance levels in raw settings <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.
    *   **Causal Chain of Thought:** A key contribution was the "Causal Chain of Thought" strategy, inspired by the Chain of Thought prompting, which significantly improved the performance of later models like GPT-4 on these tasks, though still short of early enthusiastic results <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.
    *   **CADET Dataset:** The paper also contributed the CADET dataset, a large public dataset of causal pairs with ground truths <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>.
    *   This systematic approach provides a framework to confirm that the evaluated quantities are indeed causal, adhering to the "letter of causation" as articulated by Judea Pearl <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>.

## Future Directions

The field of [[structural_causal_models_and_causal_discovery | causality]] and LLMs is "far away from settled" and requires more ideas, discussion, and cross-pollination between different fields <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>. Researchers continue to explore the question of what constitutes a causal variable, which is gaining increasing depth and relevance for future progress in the field <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.