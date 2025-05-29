---
title: Causal reasoning in artificial intelligence
videoId: yqKJ9pUQ6Q8
---

From: [[causalpython]] <br/> 

This article summarizes key discussions on [[causal_reasoning_in_ai | causal reasoning in Artificial Intelligence]] from a podcast episode featuring Professor Judea Pearl, widely recognized as the "Godfather of modern causality" <a class="yt-timestamp" data-t="01:17:59">[01:17:59]</a>.

## Judea Pearl's Journey to Causality

Professor Pearl's journey into causality was profoundly influenced by a high school logic paradox. The paradox involved a smallpox vaccination campaign in France in the 1840s, where initial data suggested more people died from the vaccination itself than from smallpox, leading to public protests <a class="yt-timestamp" data-t="02:51:24">[02:51:24]</a>. The teacher intended to demonstrate logic's power to rectify such paradoxes, but the formal tools available at the time lacked the language to express concepts like "died from," making it impossible to formulate the problem correctly <a class="yt-timestamp" data-t="04:00:27">[04:00:27]</a>.

The challenge of causality only became prominent in the field of Artificial Intelligence in the 1980s <a class="yt-timestamp" data-t="05:06:01">[05:06:01]</a>. After his book on Bayesian Networks was published in 1988, Pearl realized something was missing <a class="yt-timestamp" data-t="06:00:19">[06:00:19]</a>. While Bayesian Networks were effective for managing uncertainty, their success stemmed from being constructed in the [[causal_reasoning_in_ai | causal direction]] <a class="yt-timestamp" data-t="05:47:31">[05:47:31]</a>.

This realization led him to shift his focus towards [[structural_causal_models | structural causal models]] (SCMs) around 1991, in collaboration with Thomas Verma <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. This transition was initially "traumatic" as it involved formulating everything using deterministic functions, a departure from two decades of working primarily with probabilistic reasoning <a class="yt-timestamp" data-t="06:48:06">[06:48:06]</a>.

## AI and Human Biases in Reasoning

When discussing human reasoning, particularly in light of Daniel Kahneman's work on systematic errors and biases, the question arises whether a General [[causal_reasoning_in_ai | Artificial Intelligence]] system "should" always reason correctly in a formal sense <a class="yt-timestamp" data-t="09:46:12">[09:46:12]</a>.

Humans are constrained by limited resources, leading to quick decision-making and the development of cognitive shortcuts, which inherently come with errors and biases <a class="yt-timestamp" data-t="10:02:13">[10:02:13]</a>. Machines, however, do not share these computational limitations <a class="yt-timestamp" data-t="10:38:09">[10:38:09]</a>. They can potentially search deeper and arrive at more reasoned conclusions, avoiding human-like biases, unless limited by factors such as access to samples in their training data <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>.

## Large Language Models (LLMs) and Causal Reasoning

Pearl's work with Al Bareinboim previously demonstrated that certain [[causal_reasoning_in_ai | causal structures]] cannot be learned solely from observational data <a class="yt-timestamp" data-t="11:35:10">[11:35:10]</a>. With the advent of Large Language Models (LLMs), there's an ongoing debate about their ability to learn "World models" <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>. Andrew Lineman suggests that LLMs can learn active [[causal_reasoning_in_ai | causal strategies]] from "passive data," which he defines as a mix of observational data, interventional data (describing experiments), and interactions (like discussion forums) <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.

Pearl's perspective is that LLMs don't learn [[causal_reasoning_in_ai | causal models]] directly from environmental data. Instead, they access text produced by people who already possess [[causal_reasoning_in_ai | causal models]] of the world <a class="yt-timestamp" data-t="13:30:17">[13:30:17]</a>. Thus, LLMs essentially "copy" these models or "compose them together by building a salad of associations among the causal model that were authored by people" <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. This means LLMs are not necessarily constrained by the "ladder of causation" in the same way, as they are leveraging existing human-generated [[causal_reasoning_in_ai | causal understanding]] <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.

LLMs have shown varying performance on [[causal_reasoning_in_ai | causal benchmarks]], performing well on some but poorly on others <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>. Pearl prefers simple "toy problems" like the firing squad problem for testing, as they have a clear ground truth and allow for controlled experimentation <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>. LLMs often require extensive prompting to arrive at the correct [[causal_reasoning_in_ai | causal conclusion]] in such scenarios <a class="yt-timestamp" data-t="17:15:00">[17:15:00]</a>. Interestingly, LLMs perform much worse when presented with abstract variables instead of concrete objects, suggesting they rely on human-like contextual knowledge ("baby world" understanding) <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.

## Future Directions for Causal AI Research

Pearl advises the [[causal_reasoning_in_ai | causal community]] to focus research over the next 5-10 years on:

*   **Personalized medicine and individualized decision-making:** Recent work shows the feasibility of answering questions about the probability and quantification of harm or benefit for specific situations, not just populations. This has applications across medicine, political science (e.g., swing states), business, and marketing <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>.
*   **Automated scientists:** Developing AI systems that can decide on the best experiment to conduct next, moving beyond brute-force experimentation <a class="yt-timestamp" data-t="26:20:25">[26:20:25]</a>. This involves local perturbations on existing models and testing intermediate variables, similar to how the understanding of malaria shifted from "bad air" to mosquitoes <a class="yt-timestamp" data-t="31:03:00">[31:03:00]</a>.
*   **Free will:** Understanding the "computational advantage" of the illusion of free will, which Pearl believes has survival value <a class="yt-timestamp" data-t="27:03:00">[27:03:00]</a>. Once understood, this can be programmed into machines, creating systems that act as though they have free will <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>.
*   **Metaphors and reasoning by analogy:** A powerful mode of reasoning not yet adequately tackled in AI, crucial for generating hypotheses and understanding affordances of objects <a class="yt-timestamp" data-t="33:18:22">[33:18:22]</a>.

## Challenges in Broadly Applying Causality

The main blockers to applying [[causal_reasoning_in_ai | causality]] more broadly in industry include:
*   Funding <a class="yt-timestamp" data-t="34:28:06">[34:28:06]</a>
*   Language barriers <a class="yt-timestamp" data-t="34:32:00">[34:32:00]</a>
*   Lack of training <a class="yt-timestamp" data-t="34:37:00">[34:37:00]</a>
*   Insufficient platforms <a class="yt-timestamp" data-t="34:37:00">[34:37:00]</a>
*   The primary challenge: **attention** <a class="yt-timestamp" data-t="34:39:00">[34:39:00]</a>. Many machine learning practitioners, for example, are focused on "sampling, interpolations, curve fitting" and believe "everything is in the data," failing to recognize the limitations predicted by [[causal_reasoning_in_ai | causality]] <a class="yt-timestamp" data-t="34:51:00">[34:51:00]</a>. This represents a "Paradigm shift" which is difficult to achieve, especially when people are rewarded for working within existing paradigms <a class="yt-timestamp" data-t="35:10:00">[35:10:00]</a>.

Even within statistics, where some claim [[causal_reasoning_in_ai | causal modeling]] has always been a guideline, the word "cause" is often absent from textbooks <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>. While structural equation models (SEMs) can represent causality, they are often taught as mere "parsimonious representations of the covariance matrix" rather than as tools for expressing [[causal_reasoning_in_ai | causal knowledge]] <a class="yt-timestamp" data-t="38:47:00">[38:47:00]</a>. Pearl advocates for a shift in education, suggesting that statistics should be a special branch of [[causal_reasoning_in_ai | causal inference]], dealing with the lower levels of the ladder of causation while keeping the entire ladder in mind <a class="yt-timestamp" data-t="38:05:00">[38:05:00]</a>.

### Limitations of Randomized Control Trials (RCTs)
There is a common misconception that RCTs are the "golden standard for establishing causation" <a class="yt-timestamp" data-t="43:20:00">[43:20:00]</a>. However, RCTs have limitations:

*   **External Validity:** Results from an RCT may not translate directly to different environments because the populations in trials are often not representative of the broader population <a class="yt-timestamp" data-t="40:26:00">[40:26:00]</a>.
*   **Scope:** RCTs can answer interventional questions (Level 2 on the ladder of causation) but not counterfactual questions (Level 3) <a class="yt-timestamp" data-t="43:32:00">[43:32:00]</a>.
*   **Causes of Effect:** Statisticians focused solely on randomized experiments cannot answer questions about the causes of effect, such as distinguishing between a drug having no effect on any individual versus killing some and saving others <a class="yt-timestamp" data-t="44:42:00">[44:42:00]</a>. Tools exist to combine observational and randomized studies to derive bounds on individual harm or benefit <a class="yt-timestamp" data-t="45:06:00">[45:06:00]</a>.
*   **Legal Settings:** In legal contexts, questions about "but for" causality (e.g., "would the injury be okay but for the actions of the accused?") are constantly asked, and while [[causal_reasoning_in_ai | causal inference]] offers tools to formulate and identify these, lawyers are often unaware of them <a class="yt-timestamp" data-t="46:23:00">[46:23:00]</a>.

## Data and Assumptions in Causal AI

The growing access to data does not necessarily reduce the need for assumptions in establishing "true causality" <a class="yt-timestamp" data-t="50:39:00">[50:39:00]</a>. Pearl emphasizes that the limitations identified in [[causal_reasoning_in_ai | causal inference]] are often asymptotic, meaning they persist even with infinite data <a class="yt-timestamp" data-t="50:46:00">[50:46:00]</a>. The crucial factor is "what is the content of the data rather than the size" <a class="yt-timestamp" data-t="51:32:00">[51:32:00]</a>. For instance, infinite passive observation data cannot allow a jump from Level 1 (associational) to Level 2 (interventional) on the ladder of causation <a class="yt-timestamp" data-t="51:20:00">[51:20:00]</a>.

Regarding [[causal_discovery_and_inference_in_ai | causal discovery software]], Pearl acknowledges its advancements but highlights his personal focus on *what can be done with a causal model* once it's assumed to exist, rather than *how to discover it* <a class="yt-timestamp" data-t="51:57:00">[51:57:00]</a>.

Future [[generative_ai_and_causal_reasoning | AGI systems]] are expected to learn [[causal_reasoning_in_ai | causal models]] in a similar way to humans, through experiments (Level 2) and hypothesizing and imagination (Level 3) <a class="yt-timestamp" data-t="53:23:00">[53:23:00]</a>. This process will be accelerated by greater access to data and computational power <a class="yt-timestamp" data-t="54:02:00">[54:04:00]</a>.

On the question of focusing on DAG-based identification versus more accurate specification of SCMs, Pearl notes that DAGs are simply an [[abstractions_in_causal_reasoning | abstraction]] of SCMs <a class="yt-timestamp" data-t="54:27:00">[54:27:00]</a>. In Level 3 identification, the goal is to identify the functions themselves, and while a direct way of testing them is still developing, combining experimental and observational data provides informative bounds on Level 3 queries <a class="yt-timestamp" data-t="55:08:00">[55:08:00]</a>.

The rise of LLMs poses a dual risk: they might "cover" (bury) [[causal_reasoning_in_ai | causal inference]] by monopolizing attention, or they might "expose" and "amplify" it by inevitably leading researchers to [[causal_reasoning_in_ai | causal questions]] when seeking to improve their understanding of human knowledge <a class="yt-timestamp" data-t="47:50:00">[47:50:00]</a>. Pearl is optimistic that the latter will occur, as [[causal_reasoning_in_ai | causal inference]] provides the fundamental framework for understanding human knowledge <a class="yt-timestamp" data-t="48:36:00">[48:36:00]</a>. He also believes that methods to automatically learn user knowledge, rather than explicitly encoding it, will be discovered <a class="yt-timestamp" data-t="49:10:00">[49:10:00]</a>.