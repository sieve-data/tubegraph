---
title: Optimal experimentation in causal analysis
videoId: Hc3rIGmX59k
---

From: [[causalpython]] <br/> 

Optimal experimentation is a field focused on strategically designing experiments to gain the most informative data, particularly within the context of [[causal_ai_and_its_role_in_experiments | causal analysis]] <a class="yt-timestamp" data-t="00:50:43">[00:50:43]</a>. It addresses the question of "which experiment should I run next?" <a class="yt-timestamp" data-t="00:51:13">[00:51:13]</a> to efficiently gather data that can "cut the causal space" or refine causal estimates <a class="yt-timestamp" data-t="00:51:05">[00:51:05]</a>.

## Core Idea

The fundamental concept behind optimal experimentation is to move beyond random or brute-force approaches to data acquisition <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>. Instead of drilling randomly for gold or making an expensive grid of measurements, optimal experimentation aims to be "smart about the drilling" <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a>. This approach is applicable to both correlational data analysis and [[causal_ai_and_its_role_in_experiments | causal analysis]] <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>.

## Methods and Techniques

One prominent method used in optimal experimentation is **Bayesian optimization** <a class="yt-timestamp" data-t="00:52:07">[00:52:07]</a>. This technique utilizes a predictor model with uncertainty (often a Gaussian process) to determine where the next data point should be acquired <a class="yt-timestamp" data-t="00:52:11">[00:52:11]</a>. It's a highly effective method for designing experiments <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a>.

The idea of strategic exploration has roots in other fields, such as "kriging" in mining, which uses statistical methods to predict values across a spatial area based on a limited number of samples <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.

## Challenges

The primary challenge in optimal experimentation is the **integration of [[data_preparation_for_causal_analysis | expert knowledge]]** <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>. While boilerplate methods can operate solely on data, the predictive models used in Bayesian optimization have parameters that can be tuned to incorporate this knowledge <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>.

[[data_preparation_for_causal_analysis | Expert knowledge]] can help "steer" the surrogate model, for instance, by guiding the search towards areas where gold pockets are more likely to be found (e.g., at the bottom of a hill) <a class="yt-timestamp" data-t="00:53:41">[00:53:41]</a>. This can involve incorporating physical knowledge, such as established formulas in physics, to exclude nonsensical or inconclusive parts of the parameter space <a class="yt-timestamp" data-t="00:53:48">[00:53:48]</a>.

This integration of [[data_preparation_for_causal_analysis | expert knowledge]] is also referred to as "preference elicitation" <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>. While valuable, there's a "cost of [[data_preparation_for_causal_analysis | expert knowledge]]" <a class="yt-timestamp" data-t="00:56:53">[00:56:53]</a>: good experts can be expensive, and incorrect [[data_preparation_for_causal_analysis | expert knowledge]] can lead to wrong assumptions <a class="yt-timestamp" data-t="00:57:01">[00:57:01]</a>. However, in a Bayesian approach, collecting more true data can eventually overrule incorrect [[data_preparation_for_causal_analysis | expert knowledge]] <a class="yt-timestamp" data-t="00:58:26">[00:58:26]</a>.

## Relation to Other Causal Concepts

Optimal experimentation is closely tied to the idea of the "cost of [[assumptions_in_causal_inference | causal assumptions]]" <a class="yt-timestamp" data-t="00:51:03">[00:51:03]</a>. Experiments, such as Randomized Control Trials (RCTs), offer high certainty about causal effects but are often very expensive <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Optimal experimentation seeks to make these expensive interventions more efficient.

It can also help in navigating the causal hierarchy, particularly when moving from observational data to interventional statements <a class="yt-timestamp" data-t="02:22:22">[02:22:22]</a>. While observational data is cheap, interventional data is much more expensive <a class="yt-timestamp" data-t="02:33:31">[02:33:31]</a>. Strategic experimentation can help justify the costs associated with strengthening causal claims <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>.

In the context of [[synthetic_control_methods_in_causal_analysis | synthetic control methods in causal analysis]], optimal experimentation can be used to inform how to collect additional data to refine [[evaluation_and_systematic_testing_of_causal_models | causal model]]s <a class="yt-timestamp" data-t="01:12:52">[01:12:52]</a>.

## Applications

[[practical_applications_of_causal_methods | Practical applications of causal methods]] are broad, and optimal experimentation plays a role in various fields. For instance, in Material Science, it is crucial for optimizing materials, such as microcomputer chips, by strategically conducting experiments to improve efficiency and reduce costs <a class="yt-timestamp" data-t="00:54:16">[00:54:16]</a>. It's about being smart in how resources are spent to achieve better results <a class="yt-timestamp" data-t="00:58:39">[00:58:39]</a>.