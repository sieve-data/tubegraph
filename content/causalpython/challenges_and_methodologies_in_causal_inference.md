---
title: Challenges and methodologies in causal inference
videoId: Vz5n5SamDAc
---

From: [[causalpython]] <br/> 

Causal inference is a critical field focused on understanding cause-and-effect relationships from data. This article explores the challenges and methodologies in this domain, drawing insights from Dr. Emer Kicaj, Senior Principal Research Manager at Microsoft Research and a core developer of the [[tools_and_frameworks_for_causal_analysis | DoWhy Library]] <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.

## The Journey to Causality: From Correlation to Causation

Dr. Kicaj's journey into causality was driven by a recurring frustration in computational social science: research papers, despite being well-grounded in theory and data analysis, would often conclude with the caveat that "correlation is not causation" due to observational data <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>, <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>. This highlighted a significant [[challenges_in_causal_inference_and_statistical_analysis | challenge]] in identifying true causal relationships. The realization that [[causal_inference_methods_and_applications | causal inference]] could, under certain conditions, enable causal claims from observational data spurred his commitment to the field <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>, <a class="yt-timestamp" data-t="09:45:00">[09:45:00]</a>.

His initial learning path involved grappling with Pearl's "Causality" book <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>, which he found challenging for beginners <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>, <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>. A key turning point was Rosenbaum's paper on propensity scores, which clarified how observational data could hint at causality by simulating randomized control trials through balancing control and treatment groups <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>, <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>. This mechanical understanding proved foundational for his approach to causal analysis <a class="yt-timestamp" data-t="30:06:00">[30:06:00]</a>.

## Current [[challenges_in_causal_inference_and_statistical_analysis | Challenges in Causal Inference]]

From a practical standpoint, a major [[challenges_in_causal_analysis_in_different_settings | challenge]] is the widespread deployment of causal methods in decision-making processes <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>, <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. Education on basic [[causal_inference_concepts_and_applications | causal concepts]] and how to work with them is still critical <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>. Academically, while algorithms for specific tasks are well-developed, there's a need for more complex modeling of intricate systems, especially those with feedback loops over time <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>, <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.

### The Role of Assumptions

A core principle in [[causal_inference_and_its_applications | causal analysis]] is that causality cannot be derived solely from data; it requires incorporating domain knowledge about the data generating process and plausible mechanisms <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>, <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. This need for external assumptions is a significant [[challenges_of_causal_inference_and_counterfactual_thinking | challenge]], as domain experts traditionally had to figure this out independently <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>, <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.

## Methodologies and Tools

### The DoWhy Library and PiWhy Ecosystem

The [[tools_and_frameworks_for_causal_analysis | DoWhy Library]], co-created by Dr. Kicaj and Amit Sharma, was initially developed as a pedagogical tool to broaden the usage of [[causal_inference_methods_and_applications | causal analysis approaches]] <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>, <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>. It emphasizes a four-stage process for causal analysis:
1.  **Modeling**: Defining causal assumptions and models <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.
2.  **Identification**: Analyzing models to identify causal estimands and approaches to answer causal questions <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>.
3.  **Estimation**: Performing statistical estimation to calculate values from data <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
4.  **Refutation**: Validating or attempting to refute assumptions <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>.

This four-step structure is crucial regardless of the specific causal estimation methods used <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>. The refutation step, in particular, aligns with Karl Popper's philosophy of falsifiability, acknowledging that while theories can be falsified, they can never be definitively proven correct <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>, <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>.

DoWhy's growth led to its transition into the independent PiWhy organization, fostering a broader community beyond its Microsoft origins with contributions from Amazon, MIT, Columbia, and Carnegie Mellon <a class="yt-timestamp" data-t="15:57:00">[15:57:00]</a>, <a class="yt-timestamp" data-t="16:29:00">[16:29:00]</a>. This collaboration among major market players like Microsoft and Amazon to develop open-source tools is seen as a way to empower the community and make data and computing more valuable <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>, <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>.

### Leveraging Large Language Models (LLMs)

LLMs are emerging as a significant augmentation to [[causal_inference_and_its_applications | causal analysis]]. While LLMs may not currently reason causally, their embedded knowledge can serve as a "Common Sense database" <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>, <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. This information can assist domain experts in:
*   Setting up [[causal_inference_concepts_and_applications | causal assumptions]] <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
*   Identifying plausible causal mechanisms <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.
*   Critiquing existing assumptions, highlighting potential omissions or errors <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>, <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

LLMs can alleviate the burden on domain experts by providing a starting point, such as an initial knowledge graph, which then motivates experts to engage, criticize, and share their specialized knowledge <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>, <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>, <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

However, a key debate revolves around whether LLMs can truly learn causal "world models" or merely approximate them locally <a class="yt-timestamp" data-t="21:42:00">[21:42:00]</a>, <a class="yt-timestamp" data-t="21:45:00">[21:45:00]</a>. While LLMs might observe many counterfactual scenarios that could lead to a causal model, they are primarily modeling language, not the world directly <a class="yt-timestamp" data-t="22:49:00">[22:49:00]</a>, <a class="yt-timestamp" data-t="22:50:00">[22:50:00]</a>. The ability to simulate physics, as seen in models like Sora, is often approximate and local, prioritizing creative output over strict physical accuracy <a class="yt-timestamp" data-t="25:16:00">[25:16:00]</a>, <a class="yt-timestamp" data-t="25:51:00">[25:51:00]</a>.

## Future Directions

For the [[tools_and_frameworks_for_causal_analysis | DoWhy]] and PiWhy ecosystem, one exciting project is PiWhy LLM, an experimental library exploring how LLMs can be integrated into the analysis process <a class="yt-timestamp" data-t="19:39:00">[19:39:00]</a>, <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>. This includes using LLMs to generate causal graphs, critique assumptions, and potentially assist in identification analyses (e.g., identifying instrumental variables) or even generating code for analyses <a class="yt-timestamp" data-t="19:56:00">[19:56:00]</a>, <a class="yt-timestamp" data-t="20:12:00">[20:12:00]</a>.

A significant area for growth in the causal Python community is making partial identification, sensitivity analysis, and proximal learning more accessible <a class="yt-timestamp" data-t="37:45:00">[37:45:00]</a>, <a class="yt-timestamp" data-t="37:47:00">[37:47:00]</a>, <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>. These concepts are often underutilized but can be crucial for making optimal decisions even when a model cannot be fully specified <a class="yt-timestamp" data-t="38:07:00">[38:07:00]</a>, <a class="yt-timestamp" data-t="38:25:00">[38:25:00]</a>. There is a need for tools that simplify the technical implementation of these methods for busy practitioners <a class="yt-timestamp" data-t="38:42:00">[38:42:00]</a>, <a class="yt-timestamp" data-t="38:57:00">[38:57:00]</a>.

Finally, Dr. Kicaj sees continued effort in leveraging foundation models to model more complex, physics-style systems, potentially opening up a broad range of exciting applications <a class="yt-timestamp" data-t="41:10:00">[41:10:00]</a>, <a class="yt-timestamp" data-t="41:14:00">[41:14:00]</a>.

## Conclusion

The field of [[causal_inference_and_its_applications | causal inference]] is continuously evolving to address the [[papers_on_practical_challenges_in_causal_research | challenges]] of deriving causal insights from data. The development of robust tools like DoWhy, the collaborative spirit of the PiWhy ecosystem, and the emerging potential of LLMs all point towards a future where causal analysis is more accessible and widely applied to critical real-world problems <a class="yt-timestamp" data-t="33:36:00">[33:36:00]</a>, <a class="yt-timestamp" data-t="33:41:00">[33:41:00]</a>.