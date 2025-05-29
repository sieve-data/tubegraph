---
title: Causal reasoning in language models
videoId: sljBU_HFnFs
---

From: [[causalpython]] <br/> 

This article synthesizes discussions and research presented at the Triple-AI conference in Vancouver, Canada, particularly focusing on the workshop concerning [[causality_and_large_language_models | causality and large language models]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Researchers explored what [[Large Language Models and Causal Reasoning | Large Language Models]] (LLMs) can learn about [[causality_and_causal_models | causality]] from various data types and the practical applications of [[causal_reasoning_and_structural_causal_models | causal reasoning]] algorithms.

## Adaptive Causal Discovery Algorithms

Usman, a PhD student at CISPA Health Center for Information Security in Germany, presented work on practical [[causal_reasoning_and_structural_causal_models | causal discovery algorithms]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
The main goal is to develop algorithms that can be applied in real-world scenarios, particularly those that adapt to data arriving over time, rather than requiring a fully specified dataset from the beginning <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This approach can also be applied when the underlying structure behind the data generating process is dynamic <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

> [!INFO] Learning by Compression
> The underlying concept for these algorithms is "learning by compression" <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This strategy can separate different types of structures, even when causal relationships change over time <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Challenges
A key challenge is distinguishing differences in data, especially when starting out and data arrives from different dynamical networks, making it difficult to achieve good results later on <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Computational Requirements
For score-based [[causal_reasoning_and_structural_causal_models | causal discovery]], there is no escaping exponential computational cost in the worst case <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. However, greedy search can save some cost by building or discovering networks in a greedy fashion, which can scale to hundreds of variables for sparse networks <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The effectiveness of the greedy approach depends on how well the chosen score fits the assumptions about the data <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Assumptions
The main functional assumption relied upon is nonlinear functions with additive Gaussian noise <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This is considered less restrictive than assuming linearity <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Real-world Impact
These algorithms could be applied in domains like healthcare for disease diagnosis, where initial data might be limited, but as more data becomes available, the algorithms can adapt and improve without starting from scratch <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## [[Causality in large language models | Causality in Large Language Models]]

Emily McMillan, an independent researcher, presented on the intersection of [[Large Language Models and Causal Reasoning | LLMs and causality]] <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### Motivation
The work is motivated by the hypothesis that even though LLMs are trained on vast amounts of data (seemingly the "whole world's data"), it is still a subsampled representation of the real world <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This sampling introduces potential for sample selection bias, which needs to be explored <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Main Insights
It is crucial to consider the data generating process and not assume that a dataset is independent and identically distributed (IID), no matter its size <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. There are many parallels between LLMs and the conditional probabilities hypothesized with a [[causal_reasoning_and_structural_causal_models | causal Directed Acyclic Graph (DAG)]] <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Researchers are encouraged to look at the log probabilities from LLMs for deeper introspection, beyond just the tokens <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

### Real-world Impact
Addressing the missing data problem and sample selection bias in LLMs could help them acquire the "common sense reasoning" that they currently lack, as this often involves mundane information not explicitly written down in training data <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## [[Causality and Large Language Models | Understanding Causal Learning in LLMs]]

Andrew Lampinen, a researcher at Google DeepMind, discussed work aimed at scientifically understanding what LLMs can learn about [[causality | causality]] from passive training <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### Motivation
The motivation stems from a puzzle in the literature: while systems are generally thought not to learn causal structures from observational data, LLMs have demonstrated abilities in various "causal-seeming tasks" <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. The resolution proposed is a distinction between observational data (from which [[causality | causal]] learning is difficult) and passive data that *might contain interventions* <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. Internet data, used for LLM training, is argued to be of the latter form <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.

### Main Insights
1.  **Observational vs. Interventional Data**: The crucial distinction between these data types and how LLMs fit into this space due to the nature of internet text <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
2.  **Learning Generalizable Strategies**: It is possible for systems to learn strategies for experimentation and generalization in new situations purely from passive training <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. This has implications not just for [[causality_and_large_language_models | causality in LLMs]] but also for the philosophy of agency <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

### Real-world Impact
This work primarily serves as a fundamental science contribution to understand the nature of learning [[causality | causality]] and what can be learned from different data types <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. The hope is that this understanding will lead to better, more robust learning systems in the future, capable of improved generalization <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

## Workshop Reflections on [[Causality and Large Language Models | LLMs and Causality]]

Abd Rahman Zed, a PhD candidate at Mila, shared insights from the workshop on [[causality_in_large_language_models | causal inference]] <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. He particularly appreciated the discussion on whether [[Large Language Models and Causal Reasoning | large language models]] can learn [[causal_reasoning_and_structural_causal_models | causal relations]] <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

### Key Insight from Judea Pearl
A significant insight came from Judea Pearl, often referred to as the "Godfather of causal inference" <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. He stated that if one only has access to observations, it's generally impossible to derive [[causal_reasoning_and_structural_causal_models | causal relationships]] <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. However, this rule might not apply to LLMs because they have access to a vast amount of data that already contains implicit "interventions" <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

> [!NOTE] The LLM Data Advantage
> LLMs process far more data than a human could (e.g., the entire internet), which often includes descriptions of actions and their outcomes. This implicit interventional data could allow LLMs to learn [[causal_reasoning_and_structural_causal_models | causal understanding]] in a way that traditional observational data cannot <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. It suggests that LLMs should not be compared directly to human learning processes because their data environment is fundamentally different <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

The discussion highlighted that it might be too early to definitively conclude whether [[Large language models and causality | LLMs can learn causal relationships]], given their relatively recent emergence and rapid evolution <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

### Bias in LLMs
Abd Rahman Zed's current work focuses on fairness in language models, specifically how LLMs can learn and even exacerbate societal biases (gender, race, religion) and how to measure and mitigate these biases <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. His research suggests that specific parts of an LLM are responsible for bias, and removing these parts can reduce the model's biased output <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.