---
title: Causal Reasoning in DecisionMaking
videoId: yqKJ9pUQ6Q8
---

From: [[causalpython]] <br/> 

This article explores the evolution, challenges, and future directions of [[causal_inference_and_decision_making | causal reasoning]], particularly its role in decision-making, drawing insights from Professor Judea Pearl, often referred to as the "Godfather of modern [[causal_inference_and_decision_making | causality]]" <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

## The Genesis of Causal Thinking

Professor Pearl's journey into [[causal_inference_and_decision_making | causality]] was sparked by a high school anecdote from his logic teacher in the 1840s France <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. The story involved a smallpox vaccination program where initial data showed more people dying from vaccination itself than from smallpox <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. This led to protests to ban vaccination, even though the data actually proved its effectiveness – few people died from smallpox precisely because the vaccination was successful <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. The teacher intended to show that logic could rectify such paradoxes, but no formal language existed at the time to express concepts like "died from" a specific factor <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. This early experience motivated Professor Pearl to search for a language to formulate such causal relationships <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

## Evolution of Causal Models

The challenge of [[causal_inference_and_decision_making | causality]] in artificial intelligence became prominent in the 1980s <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>. While Bayesian networks were initially successful in managing uncertainty with Bayesian rules <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>, their success was largely attributed to being constructed in the causal direction <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. This led to the realization that something was missing <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

The move towards the formalism of [[causal_reasoning_and_structural_causal_models | structural causal models]] (SCMs) occurred around 1991, when Professor Pearl and Thomas Verma worked to formalize counterfactuals with deterministic functions <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. This was a "trauma" given two decades of work on probabilistic reasoning, as SCMs assumed uncertainty only from boundary conditions or error variables, with everything else being deterministic <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>.

## AI, Human Cognition, and Biases in Decision-Making

The work of Daniel Kahneman and Amos Tversky focused on systematic errors and biases in human reasoning <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>. Humans are constrained by resources, leading to quick decisions with inherent shortcuts and errors <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>. Large machines, however, do not have the same resource limitations and thus may not have these biases, as they can search deeper for more reasoned conclusions <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>. However, they could be limited by the samples they can access in their training sets <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>.

## [[causal_reasoning_in_language_models | Large Language Models]] and Causality

A significant debate exists regarding what large language models (LLMs) can learn, especially concerning "world models" <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>. While it has been shown that certain structures cannot be learned solely from observational data <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>, LLMs access a new kind of data: text produced by people who already possess causal models of the world <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>.

> [!quote] Judea Pearl on LLMs
> "These people have causal model of the world and so we can learn from their models. We can just copy the model. Okay, if you copy somebody's model of the world, it doesn't mean you learn the model of the world from data, you learn it from another person who had this model. So therefore they are not tied or constrained by the ladder of causation." <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>

This means LLMs can access data that contains both observational and interventional information, or even interactions <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>. However, LLMs might combine these causal models into a "salad of associations" or "salad of rumors" <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. LLMs often perform better on causal benchmarks when given concrete objects instead of abstract variables, similar to human cognition <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.

## Future Directions in Causal Research

Professor Pearl advises the [[causal_inference_and_decision_making | causal community]] to focus on:

*   **Personalized Medicine and Individualized Decision-Making**: Recent work suggests the feasibility of answering questions about the probability and quantification of harm for specific situations, not just populations <a class="yt-timestamp" data-t="18:53:00">[18:53:00]</a>. This also applies to political science, business, and [[causality_in_marketing_and_decisionmaking | marketing]] <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>.
*   **Automatic Scientists**: Systems that can decide on the best experiment to conduct next <a class="yt-timestamp" data-t="26:20:00">[26:20:00]</a>. This involves using existing knowledge and measurements to hypothesize new directions, possibly through local perturbations on existing models <a class="yt-timestamp" data-t="31:03:00">[31:03:00]</a>. For example, moving from the belief that malaria is caused by "bad air" to understanding mosquitoes are the vector <a class="yt-timestamp" data-t="30:03:00">[30:03:00]</a>. Such systems would need to integrate concepts like metaphor and reasoning by analogy <a class="yt-timestamp" data-t="33:22:00">[33:22:00]</a>.
*   **Understanding Free Will**: The "illusion of free will" might have a computational advantage, and machines could be programmed to act as if they have it, improving user interaction and trust <a class="yt-timestamp" data-t="27:03:00">[27:03:00]</a>.

The current trend in AI is the [[integration_of_causal_reasoning_in_machine_learning | hybrid of causal inference and large language models]] <a class="yt-timestamp" data-t="25:56:00">[25:56:00]</a>, where LLMs serve as functional approximators that can be guided by [[causal_inference_and_decision_making | causal theory]] <a class="yt-timestamp" data-t="25:23:00">[25:23:00]</a>.

## Challenges in Adoption and Education

A significant "rift" exists in the [[causal_inference_and_decision_making | causal community]] <a class="yt-timestamp" data-t="21:42:00">[21:42:00]</a>, leading to communication breakdowns and duplicated work <a class="yt-timestamp" data-t="22:27:00">[22:27:00]</a>. Key challenges in applying [[causality_in_marketing_and_decisionmaking | causality]] more broadly in industry include:

*   **Funding and Language**: Barriers in terminology and financial support <a class="yt-timestamp" data-t="34:28:00">[34:28:00]</a>.
*   **Training and Lack of Platforms**: Insufficient education and tools <a class="yt-timestamp" data-t="34:32:00">[34:32:00]</a>.
*   **Attention and Paradigm Shift**: People in machine learning often focus solely on data fitting and interpolation, failing to recognize limitations predicted by [[causal_inference_and_decision_making | causality]] <a class="yt-timestamp" data-t="34:39:00">[34:39:00]</a>.

> [!quote] Judea Pearl on Paradigm Shift
> "As Thomas Kuhn so keenly said, you can't expect people to change paradigm every 10 years and now we have to change it every 10 years and people are paid and they are rewarded by continuing to work in the same paradigm and they are paid to continue that and not to change it." <a class="yt-timestamp" data-t="35:14:00">[35:14:00]</a>

### Limitations of Statistics and RCTs

Traditional statistics often treats [[causal_inference_and_decision_making | causal modeling]] (e.g., [[causal_reasoning_and_structural_causal_models | Structural Equation Models]]) merely as a "parsimonious representation of the covariance matrix," without explicitly addressing its causal meaning <a class="yt-timestamp" data-t="38:40:00">[38:40:00]</a>. Fitting models based solely on statistical fit (e.g., Bayesian Information Criteria) is a "terrible advice" because a non-causal fit will not generalize under distribution shifts <a class="yt-timestamp" data-t="37:18:00">[37:18:00]</a>.

Randomized Controlled Trials (RCTs), while considered the "golden standard" for establishing [[causal_inference_and_decision_making | causation]] <a class="yt-timestamp" data-t="40:41:00">[40:41:00]</a>, have limitations:

*   **Translational Challenge**: Results from RCTs may not directly apply to specific environments or individuals due to differences in populations or idiosyncratic characteristics <a class="yt-timestamp" data-t="40:13:00">[40:13:00]</a>. Tools for data fusion exist to combine results from various experiments and apply them to new environments, but this relies on causal assumptions (level two of the ladder of causality) that are not always verifiable by RCTs alone <a class="yt-timestamp" data-t="41:00:00">[41:00:00]</a>.
*   **Scope Limitation**: RCTs primarily address interventional questions (Level 2 of the ladder of [[causal_inference_and_decision_making | causality]]) <a class="yt-timestamp" data-t="43:32:00">[43:32:00]</a>. They cannot answer counterfactual questions (Level 3), such as finding causes of effects or distinguishing between a drug having no effect on any individual versus killing some and saving others <a class="yt-timestamp" data-t="44:15:00">[44:15:00]</a>.

## The Ladder of Causality

[[causal_inference_and_decision_making | Causal inference]] operates on a "ladder" with different levels:

*   **Level 1 (Association)**: Deals with observational data, correlation, and prediction.
*   **Level 2 (Intervention)**: Addresses "what if we do X?" questions, often handled by randomized experiments.
*   **Level 3 (Counterfactuals)**: Asks "what if X had not happened?" questions, concerning causes of effects, necessary and sufficient causes, and individualized decisions <a class="yt-timestamp" data-t="44:15:00">[44:15:00]</a>.

Many statisticians, focused on randomized experiments, are "blind to level three" questions <a class="yt-timestamp" data-t="45:32:00">[45:32:00]</a>. However, tools exist to combine observational and randomized studies to obtain bounds on the probability of harm or benefit for individuals, which are Level 3 queries <a class="yt-timestamp" data-t="45:13:00">[45:13:00]</a>.

## [[causal_discovery_and_analysis | Causal Discovery]]

Professor Pearl's work has focused on what can be done with a [[causal_inference_and_decision_making | causal model]] once it is assumed to exist, rather than how to discover it <a class="yt-timestamp" data-t="52:00:00">[52:00:00]</a>. He acknowledges the significant achievements and improvements in [[causal_discovery_and_analysis | causal discovery]] software, particularly in making assumptions less stringent <a class="yt-timestamp" data-t="52:25:00">[52:25:00]</a>.

When asked about the future of AGI learning [[causal_inference_and_decision_making | causality]], Professor Pearl suggests it will learn in the same way humans do, across all three levels of the ladder: association (Level 1), experimentation (Level 2), and hypothesizing and imagination (Level 3) <a class="yt-timestamp" data-t="53:23:00">[53:23:00]</a>. This process will likely be accelerated by greater access to data and computation <a class="yt-timestamp" data-t="54:02:00">[54:02:00]</a>.

> [!info] Data vs. Assumptions
> Having more data does not necessarily reduce the need for assumptions <a class="yt-timestamp" data-t="50:39:00">[50:39:00]</a>. Limitations in [[causal_inference_and_decision_making | causal inference]] often pertain to the asymptotic case with infinite data, where the *kind* of data (observational vs. interventional) matters more than its size <a class="yt-timestamp" data-t="51:07:00">[51:07:00]</a>.

## Advice for Learning Complex Topics

Professor Pearl advises those starting with complex subjects to "start small" with something they feel they can master at least partially <a class="yt-timestamp" data-t="01:00:46">[01:00:46]</a>. From this small area, one can expand and grow, rather than trying to tackle an overwhelmingly complex field all at once <a class="yt-timestamp" data-t="01:00:58">[01:00:58]</a>.