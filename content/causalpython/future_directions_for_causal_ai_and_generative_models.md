---
title: Future directions for causal AI and generative models
videoId: Vz5n5SamDAc
---

From: [[causalpython]] <br/> 

The future of [[trends_in_causal_ai | causal AI]] and generative models involves a deeper integration of these technologies, particularly leveraging Large Language Models (LLMs) to augment and refine causal analysis processes [00:01:49]. The aim is to make causal methods more widely deployed and practically useful for decision-making across various industries [00:06:10].

## The Role of Large Language Models (LLMs) in Causal Analysis

While it is uncertain if LLMs can truly reason causally at present, the potential for them to do so in the future remains [00:01:41]. Currently, their embedded knowledge can serve as a "common sense database" about how the world operates, which is exciting for augmenting causal analysis [00:01:52].

LLMs are seen as a way to provide technological support for the crucial initial stages of causal analysis, specifically in setting up causal assumptions [00:02:20].

Key applications for LLMs in the context of [[causal_ai_and_machine_learning | causality]] and causal inference include:
*   **Suggesting Causal Mechanisms**: LLMs can help users explore plausible causal mechanisms for a given dataset and open question [00:03:25].
*   **Critiquing Assumptions**: They can review a user's proposed assumptions and highlight potential omissions or errors, indicating areas requiring further verification or validation [00:03:34]. This significantly alleviates the burden on domain experts, who no longer have to start from scratch [00:03:54].
*   **Knowledge Graph Construction**: LLMs can assist in constructing knowledge graphs with domain experts, speeding up the process and motivating experts to share their insights by providing an initial framework to critique [00:04:04].

The project Py-LLM is an experimental library exploring how LLMs can be incorporated into the analysis process with the Dy library [00:19:40]. It aims to use LLMs to:
*   Generate causal graphs [00:19:52].
*   Critique causal assumptions [00:19:56].
*   Potentially assist with identification-style analyses, such as identifying instrumental variables using domain knowledge [00:20:12].
*   Provide support for coding analyses [00:20:20].

It is expected that LLMs will be able to bootstrap and critique assumptions, especially at the beginning and end of the four-step causal analysis process [00:20:28].

## Modeling the World with Generative Models

There's a growing discussion about whether models like GPT and Sora, as well as large world models, can learn "world models" or "causal world models" [00:21:07]. It's plausible that by observing many counterfactual scenarios within vast datasets, generative models could learn a true causal model if it were the most efficient representation [00:21:49]. However, it is not believed that this has been intentionally achieved yet, and population support for all possible counterfactuals would be lacking, leading to unclear extrapolation behavior [00:22:15].

A key distinction is that large language models primarily model *language*, not directly the world [00:22:47]. The question then becomes whether learning a causal model of language can lead to a deeper understanding of the world [00:23:01]. As foundation models move beyond language to operate on more direct observations of the world, it will become clearer what they are truly capturing [00:23:20].

Regarding claims like Sora being a "physics simulator," this is considered an overstatement [00:24:03]. While such models might learn to be approximate or local physics simulators, they can still exhibit behaviors that "falsify" the claim of being a perfect simulator [00:24:07]. The key is whether a model learns shortcuts to produce plausible outputs or truly learns a correct or approximately correct function of how the world works locally [00:24:49].

For creative tasks like generating videos, it's acceptable if the model "skips corners" around physics to achieve a desired visual [00:25:51]. However, when accurate physics modeling is required, the challenge lies in providing the right controls and assumptions to ensure correct behavior [00:26:46]. This involves thinking about how to impose external knowledge through "knobs" beyond simple text commands to influence the model's behavior [00:33:05].

## Challenges and Opportunities in the Field

### Practical Deployment and Education
From a practical standpoint, a significant challenge is getting causal methods more widely deployed in all relevant decision-making contexts [00:06:07]. Education remains critical for understanding the basics of causal concepts [00:06:21]. The field needs to make more progress in this area compared to established fields like basic statistics [00:06:37].

### Academic Opportunities
Academically, there is a wide-open opportunity beyond the current deep focus on algorithms for a limited set of tasks [00:06:46]. With computers and data becoming more ubiquitous, there's a need to tackle a broader set of problems, including:
*   **Complex Modeling**: Developing more complex models for physical processes, especially those involving feedback loops over time [00:07:27]. This area presents a significant opportunity for finding the right approaches to model such systems [00:07:39].
*   **Partial Identification and Sensitivity Analysis**: These concepts are currently underutilized and underrepresented but could significantly advance applied [[causal_ai_and_machine_learning | causal inference]] [00:38:05]. Making them more accessible, particularly for those in industry who lack time for in-depth study, is crucial [00:38:42]. Dy already incorporates methods like those from Carlos Cinelli for sensitivity analysis, but there is potential for many more methods [00:39:15]. Graph representations for partial graphs are an early but promising area [00:40:00].

### Community Collaboration
The [[causal_ai_and_machine_learning | causal python]] community is healthy, with various libraries beyond PyWi (including Dy and EconML) like CausalPy [00:35:35]. The advice for the community is to focus on the end goal: the problems people are trying to solve with these methods [00:36:00]. This includes not only algorithmic advancements but also software engineering improvements (e.g., data ingestion) and better documentation [00:36:16].

The establishment of the PyWi organization, which houses Dy, was driven by the desire to broaden the usage of causal methods [00:15:41]. It became an independent organization from Microsoft GitHub to foster a wider community, attracting significant contributions from Amazon, MIT, Columbia, Carnegie Mellon (contributing the Causal-Learn package), and Wise [00:16:01]. This collaboration across major companies and academia is seen as inspiring, demonstrating that empowering the community to make better decisions with causal analysis increases the value of data and computing for everyone [00:17:01].

## The Generative Revolution: A New Frontier
The current "generative revolution" is likened to the early days of the commercial internet in the mid-1990s [00:28:01]. While the potential is clear (e.g., e-commerce, video), significant infrastructure and engineering work (like secure HTTP or fraud protection policies) are needed before the full impact is realized [00:28:20]. Although the pace of change is faster today, there will likely be unforeseen complementary technologies, similar to how smartphones enabled Uber and Lyft, that will further amplify the impact of AI [00:29:05].

The future involves continuing to make it practical to use LLMs to support the standard causal analysis process, for example, by suggesting causal graphs, identifying missing data or confounders, and critiquing analyses [00:40:35]. Another emerging direction is exploring how foundation models might help in modeling more complex physics-style systems, which could open up a broad range of exciting applications [00:41:07].

![[intersection_of_causal_ai_and_generative_ai]]
![[Generative AI and Causal Models]]
![[Applications and challenges of causality in generative modeling]]
![[Challenges and advancements in causal AI]]
![[Causality and AI Challenges and Opportunities]]
![[The Evolution of AI Technologies Deep Learning vs Causal AI]]