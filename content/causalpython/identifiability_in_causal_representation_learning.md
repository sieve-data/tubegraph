---
title: Identifiability in causal representation learning
videoId: vW2vB6e-Mm8
---

From: [[causalpython]] <br/> 

Simon Bing, affiliated with TU Berlin in Germany, presented work on an identifiability result for [[causal_representation_learning | causal representation learning]] at Clear 2024 <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

## Work Overview
The main contribution of the presented work is to soften a ubiquitous assumption made by previous research in [[causal_representation_learning | causal representation learning]] <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>. Prior studies often assume that in each environment, intervention can only occur on a single variable, leading to "atomic" or "single-node" interventions <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>. This new work presents one of the first results allowing for multi-node interventions with unknown intervention targets, meaning multiple nodes can be intervened on simultaneously in a single environment while still achieving identifiability <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.

## Key Results
The research characterizes a specific notion of sparsity to operationalize the "sparse mechanism shift hypothesis" <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. This hypothesis posits that when transitioning between environments within an underlying [[causal_inference_and_machine_learning | causal model]], the changes in the mechanisms affected by interventions are sparse <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

The key assumptions made in this setting are:
*   A linear mixing function from latent variables to observed variables <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>.
*   Sufficiently diverse and sparse coverage of interventions across environments <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.

By regularizing for this notion of sparsity, the underlying [[causal_inference_and_machine_learning | causal variables]] can be recovered up to the indeterminacy of permutation and element-wise rescaling <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.

## Real-world Impact
The long-term goal for Bing's group is to apply [[causal_inference_and_machine_learning | causal inference]] and [[causal_representation_learning | causal representation learning]] to large-scale climate data <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>. Climate data often involves very high-dimensional measurements, and the aim is to extract [[causal_inference_and_machine_learning | causal information]] or formulate [[causal_inference_and_machine_learning | causal models]] about macroclimate phenomena <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>.

This work is particularly relevant because:
*   Climate data is heterogeneous <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.
*   It is collected from different environments <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>.
*   Active interventions on the climate are not possible <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.

Therefore, moving away from single-node to multi-node interventional environment settings could be an important first step for such applications <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.

## How to Find the Work
To find this work, one can search for "multinode Interventional [[causal_representation_learning | Causal representation learning]]" <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>.

## Recommended Paper
Simon Bing's favorite [[causal_inference_and_machine_learning | causal paper]] read recently is "Identifying representations for intervention extrapolation" by Soren S. from ET Dererk <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>. He finds it exciting because it presents a real use case for [[causal_representation_learning | causal representation learning]] <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.