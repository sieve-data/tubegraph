---
title: The role of large language models in causal analysis
videoId: Vz5n5SamDAc
---

From: [[causalpython]] <br/> 

Dr. Emre Kiciman, Senior Principal Research Manager at Microsoft Research and one of the core developers of the DoWhy Library, discusses the evolving role of [[Causality and large language models | large language models (LLMs)]] in [[causal analysis | causal analysis]] and [[causal inference | causal inference]] <a class="yt-timestamp" data-t="01:10:39">[01:10:39]</a>. He highlights the shift from mere correlational analysis to robust causal decision-making, emphasizing the importance of understanding underlying causal mechanisms <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.

## Journey to Causality and the Need for Causal Analysis

Dr. Kiciman's interest in [[causal analysis | causality]] stemmed from his work in computational social science, analyzing large-scale social media data to understand human behavior and decisions <a class="yt-timestamp" data-t="08:20:01">[08:20:01]</a>. A recurring frustration in academic conferences was the inevitable conclusion that, despite well-grounded theories and data analysis, findings were based on observational data, meaning "correlation is not causation" <a class="yt-timestamp" data-t="09:05:01">[09:05:01]</a>. This limitation, where researchers often had to admit "we don't really know," prompted him to learn [[causal inference | causal inference]] to make stronger claims from observational data <a class="yt-timestamp" data-t="09:30:01">[09:30:01]</a>.

He initially struggled with Pearl's "Causality" book but found clarity with Rosenbaum's paper on propensity scores, which provided an intuition for how observational data could hint at [[causal analysis | causality]] by simulating randomized control trials through balancing control and treatment groups <a class="yt-timestamp" data-t="10:03:01">[10:03:01]</a>.

## Current Role of [[Large Language Models and Causal Reasoning | Large Language Models]] in Causality

While Dr. Kiciman believes the question of whether [[Large language models and causality | LLMs]] can truly reason causally is still open, he doesn't think they do so *right now* <a class="yt-timestamp" data-t="01:41:01">[01:41:01]</a>. However, he is "very excited" about their potential to augment the [[causal analysis | causal analysis]] process <a class="yt-timestamp" data-t="02:01:01">[02:01:01]</a>.

### Augmenting Causal Analysis with LLMs

[[Large Language Models and Causal Reasoning | LLMs]] can assist in the crucial initial stages of [[causal analysis | causal analysis]] by leveraging their vast embedded knowledge about the world, effectively acting as a "Common Sense database" <a class="yt-timestamp" data-t="01:52:01">[01:52:01]</a>. This support is vital because [[causality and large language models | causal inference]] cannot be derived from data alone; it requires prior knowledge about the data-generating process and plausible mechanisms <a class="yt-timestamp" data-t="02:46:01">[02:46:01]</a>. Previously, domain experts had to figure this out independently <a class="yt-timestamp" data-t="03:00:01">[03:00:01]</a>.

Specific scenarios where [[Large language models and causality | LLMs]] are most useful today include:
*   **Suggesting Plausible Causal Mechanisms**: Users can provide an open question and dataset, and the [[Large Language Models and Causal Reasoning | LLM]] can suggest plausible causal mechanisms to consider <a class="yt-timestamp" data-t="03:21:01">[03:21:01]</a>.
*   **Critiquing Causal Assumptions**: [[Large language models and causality | LLMs]] can review a user's proposed causal assumptions, identify potential missing elements, and suggest areas needing more verification or validation <a class="yt-timestamp" data-t="03:34:01">[03:34:01]</a>. This significantly alleviates the burden on domain experts <a class="yt-timestamp" data-t="03:54:01">[03:54:01]</a>.
*   **Constructing Knowledge Graphs**: In conversations with others, it has been noted that [[Large language models and causality | LLMs]] not only speed up the process of constructing knowledge graphs with domain experts but also motivate experts to share their knowledge by presenting them with an initial, critiquable graph <a class="yt-timestamp" data-t="04:01:01">[04:01:01]</a>.

## Challenges and Opportunities in Causality

From a practical standpoint, a major challenge is the wider deployment of [[causal methods | causal methods]] for decision-making <a class="yt-timestamp" data-t="06:07:01">[06:07:01]</a>. Education on basic [[causal concepts | causal concepts]] remains critical <a class="yt-timestamp" data-t="06:21:01">[06:21:01]</a>. Academically, there's a broad opportunity to tackle more complex problems beyond simple effect inference, such as modeling physical processes with feedback loops over time <a class="yt-timestamp" data-t="06:46:01">[06:46:01]</a>.

### The DoWhy Library and PiWhy Ecosystem

Dr. Kiciman co-created the DoWhy library with Amit Sharma as a pedagogical example to broaden the usage of [[causal analysis | causal methods]] <a class="yt-timestamp" data-t="13:08:01">[13:08:01]</a>. DoWhy structures [[causal analysis | causal analysis]] around four stages <a class="yt-timestamp" data-t="14:11:01">[14:11:01]</a>:
1.  **Modeling Assumptions**: Coming up with causal models and assumptions <a class="yt-timestamp" data-t="14:16:01">[14:16:01]</a>.
2.  **Identification**: Analyzing models to identify a causal estimand and an approach to answer the causal question <a class="yt-timestamp" data-t="14:22:01">[14:22:01]</a>.
3.  **Estimation**: Performing statistical estimation to calculate values from data <a class="yt-timestamp" data-t="14:29:01">[14:29:01]</a>.
4.  **Refutation**: Validating or attempting to refute assumptions <a class="yt-timestamp" data-t="14:36:01">[14:36:01]</a>. This final step is inspired by Karl Popper's philosophy of falsifiability, recognizing that while assumptions cannot be proven correct, data can contradict them <a class="yt-timestamp" data-t="17:54:01">[17:54:01]</a>.

DoWhy has since grown into the independent PiWhy organization, an ecosystem of libraries with contributions from Microsoft, Amazon, MIT, Columbia, and Carnegie Mellon (e.g., `CausalLearn` package) <a class="yt-timestamp" data-t="15:54:01">[15:54:01]</a>. This collaboration across major organizations aims to empower the community to make better decisions with [[causal analysis | causal analysis]], making data and computing more valuable <a class="yt-timestamp" data-t="17:11:01">[17:11:01]</a>.

## The Future: [[Large Language Models and Causal Reasoning | LLMs]], World Models, and Physics Simulation

A key future direction for Dr. Kiciman is the `piy_llm` project, an experimental library focused on integrating [[Large Language Models and Causal Reasoning | LLMs]] into the `DoWhy` analysis process <a class="yt-timestamp" data-t="19:39:01">[19:39:01]</a>. This involves using [[Large Language Models and Causal Reasoning | LLMs]] to:
*   Generate causal graphs <a class="yt-timestamp" data-t="19:56:01">[19:56:01]</a>.
*   Critique assumptions <a class="yt-timestamp" data-t="19:59:01">[19:59:01]</a>.
*   Provide support for identification analyses, such as suggesting instrumental variables using domain knowledge <a class="yt-timestamp" data-t="20:08:01">[20:08:01]</a>.
*   Potentially even help code up analyses <a class="yt-timestamp" data-t="20:20:01">[20:20:01]</a>.

### Can LLMs Learn Causal World Models?

The debate about whether models like GPT or Sora can learn [[causal world models | causal world models]] is a "hot discussion" in AI <a class="yt-timestamp" data-t="20:37:01">[20:37:01]</a>. Dr. Kiciman believes it's *plausible* for [[Large language models and causality | LLMs]] to learn [[causal models | causal models]] due to the vast amount of counterfactual scenarios they've observed in data <a class="yt-timestamp" data-t="21:49:01">[21:49:01]</a>. However, he doesn't think they *are* doing so explicitly right now, and their "population support" (observing the full scope of possible situations) might be limited <a class="yt-timestamp" data-t="22:27:01">[22:27:01]</a>.

A critical "meta question" is that [[Large Language Models and Causal Reasoning | LLMs]] are primarily modeling *language*, not the world itself <a class="yt-timestamp" data-t="22:47:01">[22:47:01]</a>. Learning a causal model of language is distinct from learning a causal model of the world <a class="yt-timestamp" data-t="22:54:01">[22:54:01]</a>. Moving foundation models to operate on more direct observations of the world, rather than just language, will offer clearer insights into what the models are capturing <a class="yt-timestamp" data-t="23:20:01">[23:20:01]</a>.

Regarding claims that models like Sora are "physics simulators," Dr. Kiciman considers this an overstatement <a class="yt-timestamp" data-t="24:03:01">[24:03:01]</a>. While they might learn an "approximate local simulation" of physics, they often "skip corners" or "violate physics" for creative purposes, like generating visually impressive but physically impossible scenarios (e.g., pirate ships battling in a coffee cup with waves) <a class="yt-timestamp" data-t="25:14:01">[25:14:01]</a>. The challenge is controlling these models when true physical accuracy is required <a class="yt-timestamp" data-t="26:43:01">[26:43:01]</a>.

### Causal Control of Generative Models

There's a growing interest in learning how to [[tools_and_frameworks_for_causal_analysis | causally control]] the generation process of models <a class="yt-timestamp" data-t="31:41:01">[31:41:01]</a>. This means creating "knobs" to modify specific aspects of the output (e.g., an image) without regenerating it from scratch <a class="yt-timestamp" data-t="31:55:01">[31:55:01]</a>. This approach involves leveraging external knowledge that cannot be easily expressed through simple text commands, using other "knobs" to impose desired behavior <a class="yt-timestamp" data-t="33:17:01">[33:17:01]</a>.

## Motivation and Outlook

Dr. Kiciman is motivated by the potential to impact real-world problems and push the boundaries of technology in socially important ways <a class="yt-timestamp" data-t="33:36:01">[33:36:01]</a>. He emphasizes the importance of the causal Python community not losing sight of the end goal: solving real problems with [[causal analysis | causal methods]] <a class="yt-timestamp" data-t="36:00:01">[36:00:01]</a>. This can involve deep algorithmic work, software engineering to improve data ingestion, or even better documentation <a class="yt-timestamp" data-t="36:08:01">[36:08:01]</a>.

One area identified for significant impact in applied [[causal inference | causal inference]] is making partial identification, sensitivity analysis, and proximal learning more accessible <a class="yt-timestamp" data-t="37:45:01">[37:45:01]</a>. Many practitioners don't realize these methods might be sufficient for optimal decision-making even when a model cannot be fully specified, or they lack the technical know-how to implement them <a class="yt-timestamp" data-t="38:23:01">[38:23:01]</a>.