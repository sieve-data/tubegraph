---
title: Causality and Causal Models
videoId: yqKJ9pUQ6Q8
---

From: [[causalpython]] <br/> 

## Introduction to Modern Causality

Professor Judea Pearl is widely regarded as the "Godfather of modern causality" <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. His work has significantly influenced the field, with his book *The Book of Why* being a starting point for many in their [[causal_reasoning_and_structural_causal_models | adventure with modern causality]] <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.

## The Genesis of Causal Inquiry

Professor Pearl's interest in causality was sparked during a junior high school logic class <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. The teacher presented a paradox from 1840s France concerning smallpox vaccination: the number of people who died *from* vaccination appeared larger than those who died *from* smallpox, leading to protests against vaccination <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. This data, however, actually proved the vaccination's effectiveness, as the low number of smallpox deaths was due to successful vaccination <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. The teacher could not formally rectify the paradox with available logic tools <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

Pearl later found that traditional logic lacked a language to express concepts like "died from" <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. It took a long time to develop the correct solutions for such problems, which involve understanding the effectiveness of interventions like vaccination <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.

## Evolution from Probabilistic Reasoning to Structural Causal Models

The challenge of causality became prominent in artificial intelligence in the 1980s <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>. While Bayesian Networks were initially seen as the best way to manage uncertainty, their success largely stemmed from being constructed in the causal direction <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>. By 1988, Pearl realized that Bayesian Networks were not enough and a different direction was needed <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.

This led to the formalization of [[causal_reasoning_and_structural_causal_models | structural causal models]] (SCMs) around 1991, in collaboration with Thomas Verma <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. A significant shift occurred in formulating counterfactuals with deterministic functions, where uncertainty only arises from uncertain boundary conditions (e.g., error variables) <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>. This was a "trauma" for researchers who had worked for two decades on purely probabilistic reasoning <a class="yt-timestamp" data-t="06:48:00">[06:48:48]</a>.

### The Ladder of Causation

The concept of the "ladder of causation" highlights different levels of causal inquiry:
*   **Level 1: Association (Seeing)** <a class="yt-timestamp" data-t="38:15:00">[38:15:00]</a>
*   **Level 2: Intervention (Doing)** <a class="yt-timestamp" data-t="38:15:00">[38:15:00]</a> - Questions about the effect of an action (e.g., what if we do X?) <a class="yt-timestamp" data-t="43:32:00">[43:32:00]</a>. Randomized control trials (RCTs) are a golden standard for establishing causation at this level <a class="yt-timestamp" data-t="40:15:00">[40:15:00]</a>.
*   **Level 3: Counterfactuals (Imagining)** <a class="yt-timestamp" data-t="38:15:00">[38:15:00]</a> - Questions about causes of effects (e.g., what if X had not happened?) <a class="yt-timestamp" data-t="43:37:00">[43:37:00]</a>. These include distinctions like necessary and sufficient causes, which are beyond the reach of statisticians only interested in randomized experiments <a class="yt-timestamp" data-t="44:15:00">[44:15:00]</a>.

It is problematic that some people do not distinguish between ranks two and three, missing areas where level three insights are needed, such as finding causes of effects <a class="yt-timestamp" data-t="43:42:00">[43:42:00]</a>.

## Causality and Artificial Intelligence

### Human vs. Artificial Intelligence Biases
Daniel Kahneman's work focused on systematic errors and biases in human reasoning <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>. Humans are constrained by resources, leading to shortcuts and errors in decision-making <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>. Large machines, however, do not have these resource limitations and might not possess the same biases, as they can afford to search deeper for more reasoned conclusions <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>. Their limitations might stem from the samples they can access in their training data <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>.

### [[Generative AI and Causal Models | Generative AI and Causal Models]]: Large Language Models (LLMs)
LLMs have a new kind of data in their training sets: text produced by people who inherently possess causal models of the world <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>. These models can "copy" human causal models from text <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>. However, this means they learn from a "salad of associations" among human-authored causal models, rather than truly learning the world model from raw data <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. This "salad of rumors" about causal models can lead to inconsistent performance on [[causal_model_evaluation_and_selection | causal benchmarks]] <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.

While LLMs can perform well on some [[causal_model_evaluation_and_selection | causal benchmarks]], they struggle with others <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>. Complex benchmarks like COVID-19 data are challenging because they lack a clear ground truth <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>. Pearl prefers working with simple, controllable problems like the "firing squad problem" for [[causal_model_evaluation_and_selection | evaluating causal models]] <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>.

> "If you're telling me that the Rifleman listens only to the captain and if you tell me keep on all repeating the assumption even though the assumption were derivable already from the story it he said if this is this is this is is true then then you're right if Riflemen when refrain from shooting the prisoner will still be dead if you prompt it more and more and tell but you have already the answer why do you have to repeat eventually it get it right so it's really an exercise and prompting you're dealing with a black box and you're asking what kind of prompt will give you the answer that you expect here we know what answer we expect in big problem we don't know the answer we expect so I like to experiment with the firing squad" <a class="yt-timestamp" data-t="16:41:00">[16:41:00]</a>

LLMs perform significantly poorer when asked to reason with abstract variables compared to concrete objects that relate to human everyday life ("baby world") <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.

### Future of AI: Automated Scientists and Free Will
The concept of an "automated scientist" is a promising area of research <a class="yt-timestamp" data-t="26:20:00">[26:20:00]</a>. Such a system could decide the best experiment to conduct next, moving beyond brute-force experimentation <a class="yt-timestamp" data-t="28:16:00">[28:16:00]</a>. The challenge lies in encoding the entire possible space of starting points and making the model understand the optimal direction for scientific inquiry <a class="yt-timestamp" data-t="28:51:00">[28:51:00]</a>.

One approach is through local perturbation of existing models <a class="yt-timestamp" data-t="31:00:00">[31:00:00]</a>. For example, if malaria is linked to swamps, one could hypothesize an intermediate variable (like mosquitoes) and experiment with interventions related to it <a class="yt-timestamp" data-t="31:07:00">[31:07:07]</a>. The ability to use metaphors and reason by analogy, incorporating "affordances" (what objects can do), is a powerful mode of reasoning not yet fully tackled in AI <a class="yt-timestamp" data-t="33:43:00">[33:43:00]</a>.

Pearl also believes the "scandal of science," the problem of free will, will be solved <a class="yt-timestamp" data-t="26:56:00">[26:56:00]</a>. The illusion of free will likely has survival value, and understanding its computational advantage will allow it to be programmed into AI systems, enabling them to act *as though* they have free will <a class="yt-timestamp" data-t="27:03:00">[27:03:00]</a>.

## Challenges and Future Directions in Causal Research

### Bridging Divides in the Causal Community
There is a "rift" in the causal community between different traditions, such as the graphical tradition and the potential outcome framework <a class="yt-timestamp" data-t="21:44:00">[21:44:00]</a>. However, the potential outcome framework is logically equivalent to [[causal_reasoning_and_structural_causal_models | structural causal models]] <a class="yt-timestamp" data-t="22:55:00">[22:55:00]</a>. The difference lies in comfort with articulating assumptions in one language versus another <a class="yt-timestamp" data-t="23:20:00">[23:20:00]</a>. Many who use potential outcomes implicitly think in terms of graphs <a class="yt-timestamp" data-t="23:44:00">[23:44:00]</a>. It is difficult for any "mortal" to defend assumptions like conditional ignorability without understanding the underlying causal structure <a class="yt-timestamp" data-t="24:22:00">[24:22:00]</a>.

### Personalized Medicine and Individualized Decision Making
A key future direction for the causal community is [[applications_of_causal_models_in_business_and_marketing | personalized medicine]] and individualized decision-making <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>. Recent work suggests the feasibility of answering questions about the probability of harm and quantifying harm or benefit for specific situations, not just populations <a class="yt-timestamp" data-t="19:08:00">[19:08:00]</a>. This requires being able to combine both experimental and observational data, often derived from the same population or mathematical object <a class="yt-timestamp" data-t="20:56:00">[20:56:00]</a>.

### Barriers to Broader Application
Several factors hinder the broader application of causality in industry:
*   **Funding** <a class="yt-timestamp" data-t="34:28:00">[34:28:00]</a>
*   **Language differences** <a class="yt-timestamp" data-t="34:32:00">[34:32:00]</a>
*   **Training** <a class="yt-timestamp" data-t="34:32:00">[34:32:00]</a>
*   **Lack of platforms** <a class="yt-timestamp" data-t="34:37:00">[34:37:00]</a>
*   **Attention** <a class="yt-timestamp" data-t="34:39:00">[34:39:00]</a>: Many in [[causality_and_machine_learning | machine learning]] are focused solely on "sampling, interpolations, curve fitting," and assume everything is "in the data" <a class="yt-timestamp" data-t="34:54:00">[34:54:00]</a>.
*   **Paradigm Shift Resistance**: People are often rewarded for working within existing paradigms, making it difficult to adopt new approaches <a class="yt-timestamp" data-t="35:10:00">[35:10:00]</a>.

### Education and the Role of Statistics
There is a need for a shift in education regarding causality <a class="yt-timestamp" data-t="43:43:00">[43:43:00]</a>. Statistics departments should view statistics as a "special branch of causal inference" dealing with the lower levels of the ladder of causation <a class="yt-timestamp" data-t="38:08:00">[38:08:00]</a>. Traditional statistics books often do not even have "cause" in their index <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>. For example, structural equation models (SEMs) are taught as parsimonious representations of covariance matrices, not as representations of causal models <a class="yt-timestamp" data-t="38:40:00">[38:40:00]</a>. Fitting a model with a better statistical fit (e.g., using BIC) is terrible advice for causal inference, as a non-causal fit will not generalize under distribution shifts <a class="yt-timestamp" data-t="37:18:00">[37:18:00]</a>.

Even randomized control trials (RCTs), while the golden standard for [[interventions_and_causal_models | interventional questions]], have limitations; they cannot answer counterfactual questions <a class="yt-timestamp" data-t="43:20:00">[43:20:00]</a>. There are tools available today for combining data from multiple experiments and observational studies to get informative bounds on individual behavior and answers to level three questions <a class="yt-timestamp" data-t="45:10:00">[45:10:00]</a>.

### Causal Discovery
Regarding [[causal_reasoning_and_structural_causal_models | causal discovery]] software, Pearl's work has focused on what can be done with a causal model once it is assumed, rather than how to discover it <a class="yt-timestamp" data-t="52:00:00">[52:00:00]</a>. While improvements in discovery have been made (e.g., less stringent assumptions), it remains a distinct area of research <a class="yt-timestamp" data-t="52:22:00">[52:22:00]</a>. The choice to focus on Directed Acyclic Graphs (DAGs) as an [[abstractions_and_causal_models | abstraction]] of SCMs is a division of labor, concentrating on identification in level two <a class="yt-timestamp" data-t="54:40:00">[54:40:00]</a>.

## Conclusion

The future of [[causality_and_machine_learning | causal influence]] lies in a hybrid approach, combining causal theory with [[generative_ai_and_causal_models | large language models]] as functional approximators <a class="yt-timestamp" data-t="25:56:00">[25:56:00]</a>. This will allow for the composition of expressions from different levels of the causal hierarchy <a class="yt-timestamp" data-t="25:41:00">[25:41:00]</a>. Ultimately, causality is the foundation of knowledge, and understanding human knowledge structure is crucial for designing machine interfaces <a class="yt-timestamp" data-t="48:46:00">[48:46:00]</a>. There is optimism that the advent of LLMs will expose and amplify the importance of [[causal_reasoning_in_language_models | causal inference]], rather than burying it <a class="yt-timestamp" data-t="48:21:00">[48:21:00]</a>.