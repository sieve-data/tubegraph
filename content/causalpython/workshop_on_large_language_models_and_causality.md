---
title: Workshop on large language models and causality
videoId: FC-rNx5qGR0
---

From: [[causalpython]] <br/> 

A workshop focusing on the intersection of [[causality_and_large_language_models | causality and large language models]] (LLMs) is being organized as part of the 38th annual Conference on Advanced Announcements in Artificial Intelligence (AAAI) <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. This event is scheduled for February 27th in Vancouver <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a><a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a>.

## Workshop Theme and Goals
The workshop aims to explore the rapidly evolving subfield at the intersection of [[causality_and_large_language_models | causality and large language models]] <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>. It seeks to foster discussion and cross-pollination of ideas between different fields, acknowledging that this area is far from settled <a class="yt-timestamp" data-t="21:17:00">[21:17:00]</a><a class="yt-timestamp" data-t="21:22:00">[21:22:00]</a>. The organizers anticipate "fireworks" and real communication that could lead to new works and different perspectives <a class="yt-timestamp" data-t="27:06:00">[27:06:00]</a>. A key question being posed is whether LLMs reason and how they do so, and if it aligns with [[causality_in_large_language_models | structural causal models]] (SCMs) <a class="yt-timestamp" data-t="27:46:00">[27:46:00]</a>.

## Organizers
The organizing team for the workshop includes:
*   Alex (speaker) <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>
*   Mate (speaker) <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>
*   Lian Wain <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>
*   Amit Sharma from Microsoft (original author of DoWhy) <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>
*   Dave from TU Darmstadt (now professor in Eindhoven, seeking PhD students in [[causality_and_large_language_models | causality]]) <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a><a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>
*   Christian Kasting <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>

Dave and Christian were Mate's supervisors and have co-authored several papers on [[causality_and_large_language_models | causality]] <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.

## Invited Speakers and Notable Contributions
The workshop will feature a lineup of distinguished speakers:
*   **Judea Pearl:** Will join virtually for the opening remarks <a class="yt-timestamp" data-t="28:09:00">[28:09:00]</a>. Mate also posed a riddle related to Judea Pearl's quote: "As X-rays are to the surgeon, graphs are for causation" <a class="yt-timestamp" data-t="29:08:00">[29:08:00]</a>.
*   **Andrew Lampinen** from DeepMind/Google DeepMind <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a><a class="yt-timestamp" data-t="20:06:00">[20:06:00]</a>. His paper, "Passive learning of active causal strategies in agents and language models," shows that [[large_language_models_and_causal_reasoning | language models can generalize causal structures]] under certain criteria <a class="yt-timestamp" data-t="19:16:00">[19:16:00]</a><a class="yt-timestamp" data-t="19:33:00">[19:33:00]</a>.
*   **Emre Kiciman** from Microsoft Research <a class="yt-timestamp" data-t="28:18:00">[28:18:00]</a>.
*   **Mela VHA** from Cambridge University <a class="yt-timestamp" data-t="28:24:00">[28:24:00]</a>.
*   **Guy Van den Broeck** <a class="yt-timestamp" data-t="28:35:00">[28:35:00]</a>.

Accepted papers will also be presented, including those co-authored by researchers like Melanie Mitchell from the Santa Fe Institute <a class="yt-timestamp" data-t="28:49:00">[28:49:00]</a>.

## History and Key Papers in [[Causality and Large Language Models]]

The organizers provide a brief overview of the research history that inspired the workshop <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.

### "Understanding Causality with Large Language Models: Feasibility and Opportunities" (April 2023)
This paper by Chang Chong from Microsoft Research was identified as an early "position paper" <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a><a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>. It explored potential uses of [[large_language_models_and_causal_reasoning | LLMs for causal discovery]] and [[causal_inference_models_and_ai_workshops | causal inference]], including as feature extractors or partial knowledge extractors <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>. It mentioned using ChatGPT with Desi (an end-to-end causal discovery and inference algorithm) to recover causal graphs <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

### "Causal Reasoning in Large Language Models: Opening a New Frontier for Causality" (April/May 2023)
This paper presented surprising results, including GPT-4 achieving almost human-level performance on the cross-counterfactual reasoning benchmark <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a><a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>. However, early evaluation methods for these models were considered intuitive but not very systematic, with questions remaining about memorization versus reasoning <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a><a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>. Mate describes this as potentially the first "technical" paper in the field, moving towards evaluation <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>.

### "Causal Parrots: Large Language Models May Talk Causality But Are Not Causal"
Co-authored by Mate, this paper, with a title inspired by an earlier work on "statistical parrots," provides key insights into the capabilities of LLMs in [[causality_and_large_language_models | causality]] <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a><a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>.

Key insights from this paper:
*   It confirms and broadens previous evaluation results <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.
*   The conceptual takeaway revolves around the [[causality_in_large_language_models | Structural Causal Model]] (SCM) as a modeling framework <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.
*   The hypothesis, referred to as "meta SCMs," suggests that LLMs learn from data (like Wikipedia) which contains "correlations of causal facts" <a class="yt-timestamp" data-t="13:20:00">[13:20:00]</a><a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>. For example, "altitude causes temperature" is a widely agreed-upon causal direction <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>. If such facts are collated in the training data, LLMs can pick up on these patterns and answer causally correctly, even without "understanding" in a typical sense <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>. This idea is conjectured to be more general and applicable to various domains and representations <a class="yt-timestamp" data-t="17:27:00">[17:27:00]</a><a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>.

### "SEAL: Assessing Causal Reasoning in Language Models"
This paper, co-authored by Jiaying Li and Bernhard Schölkopf, represents a move towards more [[systematic_evaluation_of_language_models_in_causality | systematic evaluation of language models in causality]] <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a><a class="yt-timestamp" data-t="22:40:00">[22:40:00]</a><a class="yt-timestamp" data-t="22:56:00">[22:56:00]</a>. The authors built a causal engine to generate descriptions of causal situations with natural language and corresponding ground truths <a class="yt-timestamp" data-t="23:11:00">[23:11:00]</a>.

Key findings:
*   LLMs generally perform poorly on tasks requiring causal reasoning (correlational, interventional, and counterfactual queries) in a raw setting, often performing at random chance <a class="yt-timestamp" data-t="23:26:00">[23:26:00]</a><a class="yt-timestamp" data-t="23:36:00">[23:36:00]</a>.
*   A strategy called "causal Chain of Thought" (inspired by the Chain of Thought strategy) can significantly improve the performance of models like GPT-4 on these tasks, though still far from early enthusiastic results <a class="yt-timestamp" data-t="23:54:00">[23:54:00]</a><a class="yt-timestamp" data-t="24:07:00">[24:07:00]</a>.
*   The paper also contributes a large public dataset called CADER, containing causal pairs with ground truths <a class="yt-timestamp" data-t="24:30:00">[24:30:00]</a><a class="yt-timestamp" data-t="24:50:00">[24:50:00]</a>.

## Current Challenges and Future Directions
The discussion highlights several open questions:
*   How do we know if models are building an internal world model, and how can it be tested <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>? This question was also raised by Judea Pearl in conversation with Yann LeCun <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>.
*   Are models like Sora building a world model, or rather many local approximations that produce realistic outputs but still show inconsistencies <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a><a class="yt-timestamp" data-t="16:15:00">[16:15:00]</a>?
*   The philosophical question of what constitutes [[causality_and_large_language_models | causality]] within images or videos, and the role of time <a class="yt-timestamp" data-t="17:46:00">[17:46:00]</a>.
*   The definition of a "causal variable," a question emphasized by Sander Beckers, is becoming increasingly deep and relevant for future progress <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a><a class="yt-timestamp" data-t="18:56:00">[18:56:00]</a>.

> [!INFO] Recommendation for Audience
> To explore the literature on [[large_language_models_and_causality | Large Language Models and Causality]], a good strategy is to check the references in any of the discussed papers, as the field involves vastly different authors and covers a wide range of relevant topics <a class="yt-timestamp" data-t="26:26:00">[26:26:00]</a>.