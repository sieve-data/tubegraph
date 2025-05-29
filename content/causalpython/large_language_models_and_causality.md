---
title: Large language models and causality
videoId: sljBU_HFnFs
---

From: [[causalpython]] <br/> 

The AAAI 2024 conference in Vancouver, Canada, featured a dedicated [[workshop_on_large_language_models_and_causality_at_aaai_2024 | workshop on causality and large language models]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Researchers presented their work on the intersection of [[large_language_models_and_causation | large language models and causality]] and the broader field of [[machine_learning_and_causality | machine learning and causality]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Causal Discovery with Adaptive Algorithms

Usman, a PhD student at CISPA Helmholtz Center for Information Security, presented work on practical causal discovery algorithms <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. His research focuses on adapting these algorithms to data as it arrives over time, rather than requiring a fully specified dataset from the beginning <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

### Key Aspects
*   **Dynamic Structures**: The underlying concept, based on learning by compression, can be applied even when causal relationships change over time <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This strategy helps separate different types of structures <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Challenges**: Distinguishing differences in data, especially when data arrives in small, varied batches from different dynamical networks, presents a significant practical challenge <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Computational Requirements**: The algorithms use a score-based causal discovery approach, which in the worst case, still involves exponential computational costs <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. However, a greedy search nature helps save computation in practice, enabling scaling to hundreds of variables for sparse networks under certain assumptions <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Assumptions**: The primary functional assumption is non-linear functions with additive Gaussian noise, which is considered less restrictive than assuming linearity <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Real-World Impact**: Such adaptive algorithms could be particularly powerful in domains like healthcare, where initial data for diagnosis might be limited, but algorithms could continuously adapt as more data becomes available <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Large Language Models and Data Bias

Emily McMillan, an independent researcher and research scientist, presented work at the [[integration_of_language_models_and_causality | intersection of LLMs and causality]] <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### Motivation and Insights
*   **Data Bias**: LLMs, despite being trained on vast amounts of data, are ultimately trained on a subsampled representation of the real world <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This sampling introduces potential for sample selection bias <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Key Learnings**: It is crucial to consider the data generating process and avoid assuming that a dataset, no matter how large, is independently and identically distributed (IID) <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **LLMs and Causal DAGs**: There are parallels between LLMs and causal directed acyclic graphs (DAGs), particularly concerning conditional probabilities <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Researchers can propose a DAG and measure the conditional probabilities it entails within an LLM <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Introspection into the log probabilities of LLMs, rather than just tokens, can provide deeper insights <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Real-World Impact**: Understanding sample selection bias and missing data in LLMs is important <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Common sense reasoning, often considered mundane or obvious, might be lacking in language models because it is rarely explicitly written down in training data <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   **Recommended Paper**: Emily found the "Causal Parrots" work interesting, specifically a 2020 NeurIPS paper on mediation analysis that introspected into LLMs by freezing weights and finding parallels between causal DAGs and the Transformer model <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## Causal Inference in Policy Making: Electric Vehicle Incentives

Scott Muer, affiliated with UCLA and a PhD advisor to Judea Pearl, presented a paper on the procurement of electric vehicles and how to effectively incentivize their purchase <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### Problem and Solution
*   **The Dilemma**: Governments incentivize electric vehicle (EV) purchases for environmental reasons <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. However, EV manufacturing has higher greenhouse gas emissions than internal combustion engine (ICE) vehicles <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. If an incentivized EV is not driven much (e.g., as a complimentary vehicle), it can have a negative environmental impact compared to not buying an EV at all <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Causal Approach**: The work frames this as a counterfactual problem involving unit selection, probabilities of necessity (PN), and probabilities of necessity and sufficiency (PNS) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Targeting Incentives**: It is crucial for policymakers to incentivize the *right* people <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Some households might react negatively to incentives (e.g., if from an opposing political party), potentially preventing EV adoption long-term <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   **Weighted Response Types**: The paper incorporates a formula to weigh different response types <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. For example, a harmful outcome (incentive leads to no EV purchase, but without incentive, they would have bought one) might have a significant negative weight, while a beneficial outcome (incentive leads to purchase and high usage) has a positive weight <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Main Insight**: Depending on the preferences for these weights, the conclusions on which groups to incentivize and what types of incentives to give can differ significantly <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Real-World Impact**: The hope is that this work will help governments and policymakers make more informed decisions to benefit the environment <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   **Recommended Paper**: Scott mentioned a paper by Yu Chin and Adnan Darwich on causal Bayesian networks and structural causal models, focusing on how deterministic variables can yield point estimates for probabilities of causation even without knowing their formulas <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

## Learning Causality from Passive Data in LLMs

Andrew Linzen, a researcher at Google DeepMind, discussed work aimed at scientifically understanding what [[large_language_models_and_causation | language models could learn about causality]] from passive training <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Resolving a Puzzle
*   **The Puzzle**: A recognized principle states that systems cannot learn causal structures solely from observational data <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. However, LLMs have demonstrated capabilities in causal-seeming tasks <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   **Resolution**: The paper resolves this by distinguishing between *observational data* (from which causality cannot be learned) and *passive data* that *might contain interventions* <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
*   **Internet Data**: Internet text data, on which LLMs are trained, is argued to be of the latter form, containing implicit interventions <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   **Main Insights**:
    1.  The crucial distinction between observational/interventional and passive/active dimensions <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
    2.  Systems trained on such data can learn generalizable causal strategies, enabling them to experiment and generalize in new situations just from passive training <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. This has implications beyond [[causality_and_large_language_models | causality and language models]], extending to philosophy of agency <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
*   **Real-World Impact**: The work contributes to a fundamental scientific understanding of the nature of learning causality and what can be learned from specific data types <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. This could help in building more robust learning systems that generalize better <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.
*   **Recommended Paper**: Andrew finds recent papers studying human world models and their limitations particularly interesting, especially work by Todd Gureckis at NYU on how human mental simulations sometimes fail to discriminate between physically possible and impossible situations <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

## Workshop on Causality and Large Language Models: Key Discussions

Attendees of the [[workshop_on_large_language_models_and_causality_at_aaai_2024 | Workshop on Large Language Models and Causality at AAAI 2024]] expressed great appreciation for the discussions <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.

### Can LLMs Learn Causal Relations?
*   **Debate**: Abd Rahman Zed, a PhD candidate at Mila, highlighted the engaging discussion on whether [[large_language_models_and_causation | large language models can learn causal relations]] <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. Both affirmative and dissenting viewpoints were presented with claims <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Judea Pearl's Insight**: A key insight from the workshop came from Judea Pearl, a prominent figure in causal inference <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. He stated that if one only has access to observations, it's impossible to derive causal relationships <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. However, this theorem might be challenged in the context of LLMs <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.
*   **LLMs' Unique Data Access**: [[Large Language Models and causation | LLMs]] have access to an enormous amount of data, including implicit interventions, which human beings typically do not <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. This unique access means that the traditional theorem regarding observational data might not fully apply to them, potentially allowing them to develop some form of causal understanding <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. Pearl emphasized the need to view LLMs as distinct from humans, given their unparalleled training data (e.g., the entire internet) <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
*   **Too Early to Decide**: One perspective from the workshop suggested it might be too early to definitively conclude whether [[large_language_models_and_causation | large language models can learn causal relationships]], given their relatively recent emergence in their current scale <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

### Bias in Language Models
Abd Rahman Zed's current work focuses on fairness and bias in language models <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. This includes understanding why LLMs learn biases, how they can exacerbate societal biases, and methods for mitigating and measuring these biases (gender, race, religion, etc.) <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.
*   **Recommended Paper**: His recent co-authored paper discusses pruning parts of [[large_language_models_and_causation | large language models]] that are responsible for bias to make the models less biased <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.