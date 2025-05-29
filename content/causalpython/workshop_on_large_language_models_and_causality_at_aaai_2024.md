---
title: Workshop on Large Language Models and Causality at AAAI 2024
videoId: FC-rNx5qGR0
---

From: [[causalpython]] <br/> 

The Workshop on [[Large Language Models and Causality | Large Language Models and Causality]] is an event organized as part of the 38th annual Conference on Advances in Artificial Intelligence (AAAI 2024), held in Vancouver <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>, <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. The workshop aims to foster discussion and cross-pollination between different fields related to [[causality_in_ai | causality]] and [[large_language_models_and_causality | large language models]] (LLMs), as the field is "far away from settled" <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>. It is scheduled for February 27th <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.

## Organizers

The organizing team for the workshop includes <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>:
*   Mat (Mateja) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>
*   Lian Weng <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>
*   Amit Sharma (Microsoft), an original author of DoWhy <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   David Sontag (TU Damstadt, now professor in Ulm), who is seeking PhD students in [[causality_in_ai | causality]] <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>, <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>
*   Christian Gassing <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>

David and Christian previously worked with Mat as supervisors and co-authored papers on [[causality_in_ai | causality]] <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>, <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>, <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

## Historical Context and Inspirations

The workshop was inspired by the evolving literature on [[causality_and_large_language_models | causality and large language models]] <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. Key papers that shaped this area include:

### Early Position Paper (April 2023)
The earliest paper in this field was "Understanding Causality with Large Language Models: Feasibility and Opportunities" by Chang Chung from Microsoft Research <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This paper explored the potential of LLMs at the intersection of these two fields, with very early thoughts on their capabilities <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>, <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. An early demonstration involved using ChatGPT with Desi (an end-to-end causal discovery and inference algorithm) to recover causal graphs <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Initial Technical Evaluations (April-May 2023)
*   **"Causal Reasoning and Large Language Models: Opening a New Frontier for Causality"** <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>
    *   This paper presented surprising results, such as GPT-4 achieving almost human-level performance on the cross-counterfactual reasoning benchmark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
    *   It was considered one of the first technical papers in the field, focusing on evaluation as new models became available <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. However, concerns were raised about the evaluation methods, particularly regarding the unknown extent of memorization versus actual reasoning from training data <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

### The "Causal Parrots" Hypothesis
*   **"Causal Parrots: Large Language Models May Talk Causality but Are Not Causal"** <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>
    *   This paper, co-authored by Mat, Morris Wulff, David Sontag, and Christian Gassing, confirms some earlier evaluation results while broadening the understanding <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
    *   Its core conceptual insight is the "meta Structural Causal Models (SCMs)" hypothesis <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>, <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
    *   The hypothesis suggests that LLMs, like learning from Wikipedia, pick up on "correlations of causal facts" within their training data <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>, <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. For example, knowing that "altitude causes temperature" is a causal direction typically agreed upon, and LLMs become adept at answering such questions correctly due to these correlations, rather than true causal understanding <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>, <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>, <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
    *   This "correlations of causal effects" idea is posited to be more general, applying to any domain or representation where SCMs generate data about other SCMs, whether text or images <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>, <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.

### Learning Causal Strategies
*   **"Passive Learning of Active Causal Strategies in Agents and Language Models"** by Andrew Lampinen from DeepMind (now Google DeepMind) <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>, <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>
    *   This paper suggests that LLMs can generalize causal structures if certain criteria are met <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
    *   It encourages thinking about [[machine_learning_and_causality | machine learning and causality]] not just within specific frameworks (like the Pearlian framework) but also from cognitive science, physics, and common sense perspectives <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>, <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>, <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

### Systematic Causal Evaluation
*   **"SEAL: Assessing Causal Reasoning in Language Models"** by Jing Jing and Bernard Schölkopf <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>, <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>, <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>
    *   This paper marks a move towards more systematic evaluation of [[large_language_models_and_causality | LLMs]]' causal reasoning <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.
    *   The authors built a "causal engine" to generate natural language descriptions of causal situations with ground truths <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>.
    *   Models are tested on different levels of causation: correlational, interventional, and counterfactual queries <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>.
    *   Initially, most models perform poorly, often at random levels <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>, <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.
    *   A significant contribution is the "Causal Chain of Thought" strategy, inspired by Chain of Thought prompting, which helps models like GPT-4 perform much better, though still not perfectly <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>, <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>, <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>, <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.
    *   The paper also introduced "Cadder," a large public dataset of causal pairs with ground truths <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>, <a class="yt-timestamp" data-t="00:24:35">[00:24:35]</a>, <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>.

## Key Discussions and Concepts

### [[Application of large language models LLMs in causal discovery | LLMs in Causal Discovery and Knowledge Extraction]]
There is a debate whether LLMs should be referred to as performing "causal discovery" or "causal knowledge extraction." The latter term might be more appropriate and less confusing, as LLMs may be extracting pre-existing causal knowledge rather than truly discovering new causal relationships <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>, <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>, <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. The term "knowledge" itself can be ambiguous in an AI context <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

### World Models and Local Approximations
A key question in [[causality_in_ai | AI and causality]] is whether models like LLMs or video generation models (e.g., Sora) build an internal "world model" <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>, <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. While Sora produces realistic videos, inconsistencies suggest it builds "many local approximations of a world model" rather than a general physics simulator <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>, <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>, <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

### Defining Causal Variables
The discussion highlights the fundamental question "what a causal variable actually is," a question raised by Sander Beckers, which gains increasing appreciation as the field progresses <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>, <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>, <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

## Workshop Expectations

The workshop is anticipated to be an engaging event with opportunities for real communication, potentially leading to new research <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>, <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>. It aims to provide a platform to explore whether LLMs reason causally and how <a class="yt-timestamp" data-t="00:27:46">[00:27:46]</a>.

### Invited Speakers
The workshop features a lineup of distinguished speakers <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>:
*   **Judea Pearl:** Delivering virtual opening remarks <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>.
*   **Andrew Lampinen:** From Google DeepMind <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>.
*   **Emre Kiciman:** From Microsoft Research <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>.
*   **Mateja Vlaha:** From Cambridge University <a class="yt-timestamp" data-t="00:28:24">[00:28:24]</a>.
*   **Guy Van Den Broeck:** Known for contributions in lifted inference, [[causality_in_ai | causality]], and symbolic reasoning <a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a>, <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>.
*   Papers co-authored by **Melanie Mitchell** from Santa Fe Institute will also be presented <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>, <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>.

The organizers encourage interested individuals to attend if they are in Vancouver for AAAI, ask questions, and share their thoughts, emphasizing the need for more ideas and discussion in this nascent sub-field <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>, <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>, <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.