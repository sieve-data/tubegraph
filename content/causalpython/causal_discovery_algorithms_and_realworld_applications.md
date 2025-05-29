---
title: Causal discovery algorithms and realworld applications
videoId: sljBU_HFnFs
---

From: [[causalpython]] <br/> 
This article compiles insights from researchers presenting at the Triple AI conference in Vancouver, Canada, and participants of a workshop on causality and large language models <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## [[Causal discovery algorithms and realworld applications | Causal Discovery Algorithms]]

Usman, a PhD student at CISPA Helmholtz Center for Information Security in Germany, is working on developing [[practical_applications_of_causal_methods | practical causal discovery algorithms]] that can be applied in real-world scenarios <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Adaptive Causal Discovery
One of his main goals is to create algorithms that can adapt to data as it arrives over time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This approach allows algorithms to learn continuously as new data becomes available, rather than requiring a fully specified dataset from the beginning <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

This concept, based on learning by compression, can be applied even when causal relationships in the incoming dataset change dynamically over time <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The compression-based strategy can separate different types of structures <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Challenges and Considerations
*   **Difficulty with General Settings**: The more general problem setting makes it harder to distinguish differences, especially when data is just starting to arrive <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Dynamic Networks**: If new data at each point comes from a different dynamical network, it becomes very challenging to distinguish them practically <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Poor early distinction can lead to suboptimal later results <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Computational Requirements
*   **Score-Based Causal Discovery**: Usman's work utilizes score-based [[causal_discovery_and_learning | causal discovery]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Scaling Challenges**: While the worst-case scenario still involves exponential computational cost, greedy search helps mitigate this <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   **Greedy Approach**: Building or discovering networks in a greedy fashion can work well in practice, assuming the evaluation score fits the data assumptions <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This approach has scaled to 500 variables in sparse networks for earlier algorithms <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Functional Assumptions**: The main assumption is nonlinear functions with additive Gaussian noise, which is considered less restrictive than assuming linearity <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Real-World Impact
The work aims to be applied to [[practical_applications_of_causal_methods | practical problems]] like healthcare, particularly in disease diagnosis <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This would allow algorithms to adapt and improve their knowledge as more data becomes available, rather than starting from scratch each time <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Causality in Large Language Models (LLMs)

### Sample Selection Bias in LLMs
Emily McMillan, an independent researcher, presented work at the intersection of LLMs and causality <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Her motivation stems from the hypothesis that while LLMs are trained on vast amounts of data (seemingly the whole world's data), this data is still a subsampled representation of the real world <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This subsampling introduces potential for sample selection bias <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

**Main Insights:**
*   Always consider the data generating process <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   Do not assume data is Independent and Identically Distributed (IID), no matter its size <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   There are parallels between LLMs and [[structural_causal_models_and_causal_discovery | causal dags]] (Directed Acyclic Graphs), particularly regarding conditional probabilities <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   It is encouraged to look at the log probabilities from LLMs, allowing for introspection deeper than just the token <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

**Real-World Impact:**
The work aims to highlight the missing data problem and sample selection bias in LLMs <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. It suggests that common sense reasoning, often considered obvious and therefore not explicitly written down, might be what LLMs are lacking due to these biases <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

**Interesting Paper**: Emily found "Causal Parrots" work, specifically a 2020 NeurIPS paper on mediation analysis, interesting <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. This paper introspected into LLMs, froze weights, drew parallels between causal dags and Transformer models, and validated hypotheses <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### Learning Causality from Passive Training
Andrew Linin, a researcher at Google DeepMind, discusses work focused on understanding what language models can learn about causality from passive training <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

**Motivation**: To resolve a puzzle in the literature: the notion that systems cannot learn [[causal_discovery_and_learning | causal structures]] from observational data, yet language models perform causal-seeming tasks <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

**Resolution**: A key distinction exists between observational data (from which causality cannot be learned) and passive data that *might contain interventions* <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. Internet data, on which LLMs are trained, is argued to be of the latter form <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. Systems trained on such data can learn generalizable causal strategies and other causal reasoning <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

**Main Insights:**
*   The distinction between "observational/interventional" and "passive/active" data dimensions is crucial for understanding how LLMs learn from internet text <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   Systems can learn strategies from passive training that allow them to experiment and generalize in new situations <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. This has implications for causality, LLMs, and philosophy of agency <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

**Impact**: The work contributes to the fundamental science of understanding what can be learned about causality from different data types, aiming to foster better, more robust learning systems that generalize well <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

**Interesting Paper**: Andrew found work studying human world models and their limitations particularly interesting, specifically research by cognitive scientist Todd Gureckis at NYU, which examines how human mental simulation fails to discriminate between physically possible and impossible situations, suggesting imperfect abstractions <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

### Workshop Discussions on LLMs and Causality
Participants Ali and Abd Rahman Zed both praised the workshop on causal inference, particularly the discussion on whether LLMs can learn causal relations <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

*   **Diverse Viewpoints**: The debate presented both sides, with groups arguing for and against LLMs' ability to learn causal relations <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **"Too Early to Decide"**: A notable point was made that given LLMs have only been around for about five years in their current large scale, it might be too early to definitively conclude if they can learn causal relationships <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
*   **Judea Pearl's Insights**: The talk by Judea Pearl, "the Godfather of [[causal_inference_in_practical_applications | causal inference]]", was highly appreciated <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. His key insight was that while a theorem states causal relationships cannot be found solely from observations, LLMs have access to an enormous amount of data that already contains interventions <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. This could potentially prove the theorem wrong for LLMs, as their data access is far beyond human capacity <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. Pearl tailored his theorem to consider LLMs not as human beings, but as systems trained on the entire internet, which offers a different perspective on their potential for causal understanding <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

Abd Rahman Zed is currently working on fairness in language models, specifically addressing how LLMs learn and exacerbate biases (gender, race, religion) and how to mitigate and measure them <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. He co-authored a paper on pruning LLMs, showing that removing specific parts responsible for bias can reduce the model's overall bias <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.

## Practical Causal Applications in Policy

Scott Muer, affiliated with UCLA and a PhD advisor to Judea Pearl, presented a paper on incentivizing electric vehicle (EV) procurement <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This work was done in collaboration with Toyota Research Institute <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

**Motivation**: Governments aim to incentivize EV purchases for environmental sustainability, which is generally positive <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. However, EV manufacturing has higher greenhouse gas emissions <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. If incentivized EVs are not driven much (e.g., as complimentary vehicles), they can have a negative environmental impact compared to not buying an EV at all <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. The core problem is identifying the "right people" to incentivize <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

**Approach**: This is a problem of [[causal_inference_in_practical_applications | counterfactual nature]], involving unit selection and probabilities of necessity (PN) and sufficiency (PNS) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Household Response**: Some households might respond negatively to incentives, especially if they dislike the source (e.g., opposite political party), potentially preventing them from ever buying an EV <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. Policy makers want to avoid this <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   **Desired Outcome**: The ideal scenario is when an incentive leads to a purchase and frequent driving, and without the incentive, the purchase would not have happened or the vehicle would not have been driven much <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This is the "probability of benefit" or PNS <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **Weighted Response Types**: The paper incorporates a weighting system for different response types <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. For example, a harmful consequence (incentive prevents purchase, while without incentive, they would have bought it) might have a negative weight (-10), while a beneficial outcome (incentive works and benefits environment) might have a positive weight (2) <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

**Main Insights**: The conclusions on which groups to incentivize and what types of incentives to give vary significantly depending on the preferences for these weights <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

**Learning**: The project applied existing [[machine_learning_and_causal_inference_methodologies | causal inference methodologies]] to understand the electric and internal combustion engine vehicle industries and how governments make policy decisions <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

**Impact**: The hope is that this work will enable governments and policymakers to make more informed decisions, incentivizing the right people in a way that truly benefits the environment <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

**Interesting Paper**: Scott mentioned a paper by his UCLA colleague Yu Chen and advisor Adon Darwich on [[causal_discovery_and_inference_in_ai | causal Bayesian networks]] and [[structural_causal_models_and_causal_discovery | structural causal models]] <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. This work shows that if variables are deterministic (e.g., 1s and 0s in a causal Bayesian network), point estimates for probabilities of causation or factual probabilities can be identified even without knowing the exact formulas or conditional probability tables for those deterministic variables <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.