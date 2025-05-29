---
title: Optimal experimentation in causal studies
videoId: Hc3rIGmX59k
---

From: [[causalpython]] <br/> 

Optimal experimentation is a crucial concept in causal inference, driven by the realization that experimental data can significantly refine causal models. It addresses the question of "which experiment should I run next?" <a class="yt-timestamp" data-t="00:51:11">[00:51:11]</a>, aiming to efficiently acquire data that maximizes information gain for causal understanding.

## Core Idea

The fundamental idea behind optimal experimentation is to intelligently decide where to collect new data points or run experiments, rather than relying on random or brute-force approaches <a class="yt-timestamp" data-t="00:52:36">[00:52:36]</a>. This approach is likened to efficient gold or oil exploration, where instead of randomly drilling or drilling on a rigid grid, smart methods are used to pinpoint promising areas <a class="yt-timestamp" data-t="00:51:23">[00:51:23]</a>. This concept, known as kriging in geological exploration <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>, can be applied to navigate a statistical parameter space <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>.

## Methodology: Bayesian Optimization

The primary method used for optimal experimentation is **Bayesian optimization** <a class="yt-timestamp" data-t="00:52:07">[00:52:07]</a>. This technique utilizes a predictor model that accounts for uncertainty, most commonly a Gaussian process, to determine where the next data point should be acquired <a class="yt-timestamp" data-t="00:52:11">[00:52:11]</a>. It's an inspiring and effective approach that applies to both correlational and [[causal_discovery_and_analysis | causal analysis]] <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>.

### Surrogate Models

In Bayesian optimization, "surrogate models" are used to make predictions and identify the next best experiment to run <a class="yt-timestamp" data-t="00:53:14">[00:53:14]</a>. These models have parameters that can be tuned, ideally linked to expert knowledge, to accelerate the discovery process <a class="yt-timestamp" data-t="00:53:21">[00:53:21]</a>.

## Main Challenges

The primary challenge in optimal experimentation is the effective **integration of expert knowledge** <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>. While "vanilla" Bayesian optimization methods only rely on data, incorporating expert insights can significantly enhance the process <a class="yt-timestamp" data-t="00:53:06">[00:53:06]</a>.

## Role of Expert Knowledge

Expert knowledge, also known as "preference elicitation," is crucial because it leverages existing information to make the data acquisition process smarter <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>. It can help in several ways:
*   **Steering the Search**: Expert knowledge can guide the surrogate model to focus on areas more likely to yield valuable results (e.g., knowing that gold pockets are at the bottom of a hill) <a class="yt-timestamp" data-t="00:53:35">[00:53:35]</a>.
*   **Excluding Non-Sensical Areas**: Physics knowledge, for example, can be integrated to exclude parts of the parameter space that are physically impossible or nonsensical <a class="yt-timestamp" data-t="00:53:48">[00:53:48]</a>.
*   **Constraining the Search Space**: Similar to [[causal_discovery_and_analysis | causal discovery]], expert knowledge can help limit the search space, reducing computational complexity <a class="yt-timestamp" data-t="00:55:37">[00:55:37]</a>. This effectively "slices" the [[causal_model_evaluation_and_selection | causal marginal polytope]], making the search space smaller and constraining the bounds closer to the true causal effect <a class="yt-timestamp" data-t="00:58:07">[00:58:07]</a>.

However, acquiring expert knowledge comes at a cost <a class="yt-timestamp" data-t="00:56:53">[00:56:53]</a>. A high-quality expert might be expensive, and incorrect expert knowledge can lead to wrong assumptions <a class="yt-timestamp" data-t="00:57:01">[00:57:01]</a>. Fortunately, in a Bayesian approach, collecting more true data can eventually overrule incorrect expert knowledge, though this process also incurs costs <a class="yt-timestamp" data-t="00:58:26">[00:58:26]</a>.

## Practical Importance and Application

The importance of optimal experimentation is evident in fields like Material Science <a class="yt-timestamp" data-t="00:54:16">[00:54:16]</a>. Given the widespread use and high dependency on materials, optimizing their design and production (e.g., microcomputer chips) can lead to significant cost reductions and technological advancements <a class="yt-timestamp" data-t="00:54:24">[00:54:24]</a>. Integrating the knowledge of material scientists into these models is crucial for effective optimization <a class="yt-timestamp" data-t="00:54:19">[00:54:19]</a>.

The ability to "cut the [[causal_model_evaluation_and_selection | marginal polytope]]" or the causal space with experimental data is a powerful tool <a class="yt-timestamp" data-t="00:51:03">[00:51:03]</a>. This approach aims to move away from relying solely on cheap, observational data towards smarter, more targeted experiments that yield more robust [[evaluating_causal_models_in_practice | causal findings]] <a class="yt-timestamp" data-t="01:12:35">[01:12:35]</a>. It supports the broader shift from simply predicting and explaining everything with big data to integrating valuable, precise expert knowledge into models <a class="yt-timestamp" data-t="00:57:21">[00:57:21]</a>.