---
title: Challenges in identifying causal relationships
videoId: rHM0mBXubig
---

From: [[causalpython]] <br/> 

Current approaches to autonomous driving face significant challenges, notably the impracticality of driving millions of kilometers to encounter every possible natural event <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. While simulation can help, it introduces complexity issues and difficulties in proper setup <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This "gaping gap" suggests a need for a new framework <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Causal Models as a Solution
Causal models are proposed as a suitable framework to address these challenges <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. They allow for modeling and manipulating distributions of natural events to answer queries efficiently <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

Key advantages include:
*   **Efficiency in Parameter Space**: Causal models are more efficient in describing the parameter space <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Time Integration**: While time can be incorporated, often it can be removed from the equation for greater efficiency, especially when its impact is not always critical <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. For example, in an autonomous car entering a tunnel, the light-dark-light sequence is time-dependent, but many other events are not <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Combinatorial Power**: They allow for combining distributions of natural events using functions, complex functions, machine learning, and neural networks, without requiring real-time processing or even speed-up <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Journey into Causality
Many, including Daniel Evenha, became interested in causality through the work of Judea Pearl <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Pearl's framework resonated due to its ability to address unsolved problems in various industries and its testable implications <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Inspiring Aspects of Pearl's Framework
*   **Testable Implications**: Provides a "safe ground" for research <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   **Counterfactual Reasoning**: Allows for asking "what if" questions beyond observed factual data, such as what would have happened if it rained while driving on a sunny day <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This broadens the toolset for tackling complex problems <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

## Counterfactuals vs. Interventions
The **Causal Ladder** distinguishes between associative, interventional, and counterfactual reasoning <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Counterfactuals incorporate both interventional and associative aspects <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

*   **Interventions**: The user acts as the manipulator, fixing values to specific parameters in a causal model to calculate an outcome <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This is useful in some scenarios, but in complex contexts like autonomous driving, it's hard to fix all parameters <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Counterfactuals**: Incorporate knowledge from already observed data through an **abduction step** <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This means propagating observed knowledge "up" to background or exogenous variables to understand how distributions shift <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Only then is the causal model forwarded to predict outcomes in this new state <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This process is considered more powerful and usable <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

> [!definition] Abduction
> Abduction is the upward propagation of knowledge in a causal network <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. If an observation is made on a variable low in a tree (e.g., a grandchild has blonde hair), abduction updates the distributions of its ancestors (grandparents, great-grandparents) to reflect the likelihood of certain phenotypes, without necessarily setting them to a single value <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. This shifts the likelihood towards certain phenotypes <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

## [[challenges_in_causal_inference_and_statistical_analysis | Challenges in Practice]]
[[challenges_in_causal_inference_and_statistical_analysis | Identifying causal relationships]] in practice, especially for industrial applications, presents several [[papers_on_practical_challenges_in_causal_research | challenges]]:

### Rich System Description & Effort
Counterfactual queries often require a very rich description of the system and a lot of information <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Fully Specified Structural Causal Models (SCMs)**: Using frameworks like SCMs (which incorporate any functional relationship) demands significant engineering time and resources to fully specify mechanisms and distributions <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. While this allows answering any counterfactual query, it requires substantial upfront investment <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

### Dealing with Unobserved Variables
It is the likely case that systems will have unobserved variables, hidden confounding, and mechanisms that cannot be easily defined or for which data is hard to collect <a class="yt-timestamp" data-t="00:40:37">[00:40:37]</a>.

### Data Collection for Mechanisms
Collecting data to find mechanisms is not easy <a class="yt-timestamp" data-t="00:33:49">[00:33:49]</a>.
*   Publicly available datasets and expert guidance can help inform the form of relationships (e.g., quadratic) <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>.
*   Gathering plausible and causally appropriate data from test runs or in-car "black boxes" is crucial but complex <a class="yt-timestamp" data-t="00:34:27">[00:34:27]</a>.
*   Simulation and synthetic data can also serve as data gatherers to learn mechanisms <a class="yt-timestamp" data-t="00:34:58">[00:34:58]</a>.

## Solutions and Methodologies
### Iterative Workflow and Prototyping
An iterative mindset is crucial for working with causal models <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   **Benchmark Models**: Start with understandable benchmark examples, perhaps slightly more complex than simple X-Y graphs, to communicate findings <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.
*   **Simplification**: Initially, efforts might lead to very large and complex models (e.g., a Lane Changing Assistant model with 100+ nodes) <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. The iterative process helps to identify what truly needs to be modeled and to simplify the structure <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
*   **"Frankenstein Structure"**: Build substructures or "Frankenstein structures" by piecing together components that might not be perfect but bring the solution a step closer <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.
*   **Prioritize Target Variables**: Clearly define the target variables first (e.g., "does a collision happen?" or "how strong was the impact?") <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
*   **Neglect Less Impactful Variables**: Through iteration, identify environmental variables or visual sensor data that have minimal impact on target variables and can be neglected for easier initial models <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

### Asking the Right Questions and Price Tags
It is essential to know what one wants to know and the "price" (effort, data collection) for each question <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.
*   **[[causal_inference_and_identification | Identification Algorithms]]**: Algorithms like ID, IDC, and ID* (IDC*) can provide a direct answer: can the question be answered given the causal structure, and if so, what is the recipe for calculation and what data is needed <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This allows evaluating the effort and cost of data collection <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **Question Refinement**: If a question requires too much data or effort, consider asking an easier, smaller question. If the answer to the simpler question is negative, the more difficult one might not be necessary <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This optimizes the effort-outcome ratio <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

### Balancing Accuracy and Practicality
A dilemma exists between achieving high accuracy and making something practical <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>. It's often better to lean towards practicality, especially in initial stages, to avoid getting lost in perfectionism or investing effort in dead ends <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>. Causal models offer a playing ground for low-effort experiments <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.

## Corner Cases and Long Tails
Existing autonomous driving frameworks face [[challenges_in_causal_analysis_in_different_settings | challenges]] with "long tails" in complex distributions, which can lead to unexpected events <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>.

*   **Corner Cases**: These are test cases where at least two parameters coincide in a problematic way, even if individually they are not extreme values <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. An example is slight rain and -1 degree Celsius temperature leading to sudden ice <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Using Causal Models for Long Tails**: The SCM framework can reverse the question: What structures, mechanisms, and distributions, when combined, will produce a long tail in the target variable (e.g., car accident impact)? <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a> This guides the search more efficiently and allows pre-filtering <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. Experts can provide implicit knowledge about structural information, mechanisms, and coincidences that can be incorporated to narrow down the search space for these difficult-to-handle long tail phenomena <a class="yt-timestamp" data-t="00:37:12">[00:37:12]</a>.

## Addressing the Fear of "Wrong DAGs"
Many people are intimidated by the idea of drawing an incorrect Directed Acyclic Graph (DAG) <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. However, a DAG simply makes implicit assumptions explicit <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. Assumptions are always present in decision-making and science; writing them down allows for clarity, revisitation, and correction <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>. Explicit assumptions are a win, as even one corrected wrong assumption is a huge step forward <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.

## Biggest Discoveries and Lessons Learned
### Abduction is Central and Difficult
The abduction step is at the heart of working with defined SCMs, especially for propagating observations upward to calculate the posterior of background variable distributions <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a>. While simple examples can be done on paper, complex models with many nodes, non-linear mechanisms, and varied noise incorporation make abduction challenging <a class="yt-timestamp" data-t="00:30:36">[00:30:36]</a>. Numerous methods (MCMC sampling, numerical, closed-form integral) were explored, with many failing to achieve the necessary efficiency and precision <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>. Finding a method that is time-efficient, precise, and works for diverse mechanisms and distributions remains an area of ongoing research <a class="yt-timestamp" data-t="00:31:43">[00:31:43]</a>.

### Moving from Bayesian Models to SCMs
Early attempts in Daniel's project started with Bayesian models, which were comprehensible and inferable <a class="yt-timestamp" data-t="00:27:25">[00:27:25]</a>. However, Bayesian models often have restrictions, such as being more prone to discrete variables <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>. The team sought a more general framework and transitioned to Structural Causal Models (SCMs), which allow for discrete, continuous, or mixed variables and any type of mechanism <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>. Attempts to bridge the gap between Bayesian models (with conditional probability tables) and SCMs (using reparameterization tricks) proved to be a dead end, leading to a full commitment to the general SCM framework <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.

## Team and Mindset
Working with a diverse team, including PhD physicists and mathematicians, as well as UX/UI designers, is a pleasure <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.
*   **Physicists**: Bring critical and open-minded thinking, challenging assumptions and exploring "uncharted territory" <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>. They embody the principle that a theory is only true if it cannot be falsified <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
*   **Mathematicians**: Demand solid mathematical frameworks, proofs, and a clear theoretical background, translating ideas into algorithms <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   This combination fosters fruitful exploration and grounded implementation <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

### Key Characteristics for Causal Work
*   **Resilience and Frustration Tolerance**: [[challenges_of_causal_inference_and_counterfactual_thinking | Causal inference]] is not an easy exercise; it requires persistence through difficulties <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.
*   **Experimental Mindset**: Willingness to experiment and play around with models <a class="yt-timestamp" data-t="00:45:29">[00:45:29]</a>.
*   **Playfulness**: Approaching the problem with curiosity and a willingness to start small and iterate <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>.

## Industry Need and Transportability
There is a definite need for more people with causal expertise in industry <a class="yt-timestamp" data-t="00:49:04">[00:49:04]</a>. Without causality, industries can hit dead ends, make wrong decisions based on implicit assumptions, and fail to fully understand their data <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>. The "Simpson's Paradox reverse" example, where Google mistakenly raised men's wages due to a non-causal analysis of the gender pay gap, highlights this risk <a class="yt-timestamp" data-t="00:50:04">[00:50:04]</a>.

### Transportability
A common [[challenges_in_deploying_causal_models_in_industry | challenge in industry]] that causal models address is **transportability** <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>.
*   **Definition**: Transportability involves taking conclusions from one context (e.g., a surfboard shop in Los Angeles) and applying them to another different context (e.g., New York) <a class="yt-timestamp" data-t="00:48:10">[00:48:10]</a>.
*   **Problem**: While some parameters might be identical, others are diverse (e.g., clients, beach access) <a class="yt-timestamp" data-t="00:48:30">[00:48:30]</a>. Without a causal approach, one might "compare apples with peas," leading to problematic conclusions <a class="yt-timestamp" data-t="00:48:45">[00:48:45]</a>. Causal methods help recognize what's comparable and what's different to still extract valid insights <a class="yt-timestamp" data-t="00:48:54">[00:48:54]</a>.

## Resources and Advice for Newcomers
Key resources that influenced Daniel Evenha's [[challenges_and_methodologies_in_causal_inference | causal journey]] include:
*   *The Book of Why* by Judea Pearl <a class="yt-timestamp" data-t="00:51:09">[00:51:09]</a>
*   *Causality* by Judea Pearl <a class="yt-timestamp" data-t="00:51:13">[00:51:13]</a>
*   *Causal Inference in Statistics: A Primer* by Pearl, Glymour, and Jewell <a class="yt-timestamp" data-t="00:51:16">[00:51:16]</a>
*   *Elements of Causal Inference* by Jonas Peters, Dominik Janzing, and Bernhard Schölkopf (especially chapters on interventional and counterfactual queries) <a class="yt-timestamp" data-t="00:51:22">[00:51:22]</a>
*   Causal toolboxes like `Pgm` <a class="yt-timestamp" data-t="00:51:38">[00:51:38]</a>

### Advice for Aspiring Causal Practitioners
*   Stay curious and experimental <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>.
*   Embrace the causal mindset; once "infected," it can lead to a lifelong journey of seeking high standards in making sense of things, answering difficult questions, and improving understanding <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.