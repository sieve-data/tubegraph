---
title: Identifiability in causal representation learning with multinode interventions
videoId: vW2vB6e-Mm8
---

From: [[causalpython]] <br/> 

Simon Bing from TU Berlin presented work on an identifiability result for causal representation learning <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. This research aims to soften a common assumption made in previous works regarding [[interventions_and_causal_models | interventions]] <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

## Addressing Previous Assumptions
Typically, in causal representation learning, multiple environments are considered <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. These environments are defined by different [[interventions_and_causal_models | interventions]] on latent variables <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. A widely-held assumption in prior research is that in each environment, intervention is restricted to a single variable, known as atomic or single-node [[interventions_and_causal_models | interventions]] <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

This work presents one of the first results where, for unknown intervention targets, multi-node [[interventions_and_causal_models | interventions]] are allowed <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>. This means that in a single environment, it is possible to intervene on multiple nodes simultaneously and still achieve identifiability <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.

## Key Results

The main results characterize a specific notion of sparsity, operationalizing the "sparse mechanism shift hypothesis" <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. This hypothesis suggests that when moving from one environment to the next within an underlying Causal Bayesian Network (CBN) model, the changes in affected mechanisms due to [[interventions_and_causal_models | interventions]] are sparse <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.

Key assumptions and principles applied in this setting include:
*   A linear mixing function from latent variables to observed variables <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.
*   Sufficiently diverse and sparse coverage of [[interventions_and_causal_models | interventions]] across environments <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.

By regularizing for this notion of sparsity, the underlying causal variables can be recovered, subject to the indeterminacy of permutation and element-wise rescaling <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.

## Real-World Impact
The long-term goal is to apply [[causal_inference_and_identification | causal inference]] and causal representation learning to large-scale climate data <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>. This involves extracting causal information and formulating causal models for macroclimate phenomena from high-dimensional measurements <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

> [!info] Addressing Real-World Challenges
> The transition from single-node to multi-node interventional environment settings is crucial for applications like climate modeling because data is heterogeneous, and active [[interventions_and_links | interventions]] on the climate are not possible <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.

## Finding the Work
To find this work, one can search for "multinode interventional causal representation learning" <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>.

## Recommended Reading
Simon Bing recommends "Identifying Representations for Intervention Extrapolation" by Sor S. et al. <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>, noting its real-world use case for causal representation which was previously missing <a class="yt-timestamp" data-t="00:21:58">[00:21:58]</a>.