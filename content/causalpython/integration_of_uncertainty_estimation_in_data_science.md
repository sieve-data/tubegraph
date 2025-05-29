---
title: Integration of uncertainty estimation in data science
videoId: QAzAFess1AA
---

From: [[causalpython]] <br/> 

[[uncertainty_quantification_in_machine_learning | Uncertainty quantification]] is a critical aspect of data science, particularly when models are used for decision-making rather than just prediction. Understanding and communicating model uncertainty is crucial for effective action and building trust with stakeholders <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.

## Importance of Uncertainty in Decision Making
The primary purpose of data science is to facilitate better actions and decisions <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. To achieve this, it's essential to understand how actions affect outcomes, which is fundamentally a causal question <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. Predictive models alone, without considering causation, can lead to losses if they don't capture the underlying causal structure of a system <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

While some problems only require black-box machine learning for forecasting <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>, many business problems demand a deeper understanding of the system's causal structure <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>. In these scenarios, [[uncertainty_quantification_in_machine_learning | uncertainty estimation]] becomes vital <a class="yt-timestamp" data-t="00:44:18">[00:44:18]</a>.

## [[probabilistic_modeling_and_bayesian_frameworks | Bayesian Frameworks]] and Uncertainty
[[probabilistic_modeling_and_bayesian_frameworks | Bayesian modeling]] offers a natural and organic way to estimate uncertainty <a class="yt-timestamp" data-t="00:42:29">[00:42:29]</a>. Unlike frequentist approaches that often rely on point estimates, Bayesian methods provide full posterior distributions for parameters, inherently quantifying uncertainty <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>.

### Challenges in Communicating Uncertainty
Historically, explaining concepts like priors and uncertainty to non-technical stakeholders has been challenging <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. However, framing discussions around "causality" resonates more widely, as people intuitively grasp the need to understand what causes what to take effective action <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### Generative Models and Structural Discovery
[[probabilistic_modeling_and_bayesian_frameworks | Bayesian models]] are often generative, meaning they define the data-generating process <a class="yt-timestamp" data-t="00:37:32">[00:37:32]</a>. This allows practitioners to build a causal structure before fitting data, then generate synthetic data to immediately see if the model behaves as expected <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>. This iterative process aids in "structural discovery" by allowing exploration of different hypotheses and their implications on data patterns <a class="yt-timestamp" data-t="00:38:49">[00:38:49]</a>.

## Comparison with Other Approaches
### Frequentist vs. Bayesian
Traditional causal inference, often expressed in a frequentist framework, commonly uses structural causal graphs to identify variables to include or exclude for subsequent estimation (e.g., in a linear regression) <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>. If the wrong variables are included (e.g., a collider) or confounders are omitted, biases can occur <a class="yt-timestamp" data-t="00:34:19">[00:34:19]</a>.

In contrast, within a [[probabilistic_modeling_and_bayesian_frameworks | Bayesian framework]], the entire structural model is estimated directly; there's no need for a separate variable selection logic based on paths <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a>. Including a collider, for instance, is naturally handled by the inference process <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>.

### Conformal Prediction
Conformal prediction is another popular method for [[uncertainty_quantification_in_machine_learning | uncertainty estimation]] coming from a frequentist tradition <a class="yt-timestamp" data-t="00:44:46">[00:44:46]</a>. While useful, it typically provides total uncertainty in a more black-box manner <a class="yt-timestamp" data-t="00:47:36">[00:47:36]</a>. [[probabilistic_modeling_and_bayesian_frameworks | Bayesian frameworks]], however, can easily distinguish between aleatoric (inherent randomness in the data) and epistemic (uncertainty due to limited data or knowledge) uncertainty <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.

### Challenges with Uncertainty from Black-Box Models
The type and behavior of uncertainty estimates from complex models like [[Bayesian deep learning]] can be problematic. For example, Bayesian deep learning might show decreasing uncertainty further from a hyperplane, even where data is sparse, which is not the desired behavior for out-of-distribution detection <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>. This highlights that uncertainty estimates need careful validation against reality to be believed <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>.

## [[applications_of_bayesian_modeling_in_industry | Applications of Uncertainty Estimation in Industry]]
The true value of [[uncertainty_quantification_in_machine_learning | uncertainty estimation]] lies in its actionability <a class="yt-timestamp" data-t="00:51:25">[00:51:25]</a>. Rather than just providing posterior estimates with error bars, uncertainty can be integrated into optimization processes. For instance, in a marketing mix model, uncertainty bounds can be fed into an optimizer to maximize sales based on budget allocation <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>.

Consider a marketing channel with limited data (e.g., two months) that shows high effectiveness based on a point estimate, versus a channel with three years of solid but not "amazing" data <a class="yt-timestamp" data-t="00:53:20">[00:53:20]</a>. An optimizer using only point estimates might heavily favor the short-term, high-performing channel. However, by incorporating uncertainty, the optimizer naturally behaves like a risk-averse human, preferring the more certain, long-term channel while still exploring the new one <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>. This reflects how humans make decisions, incorporating risk <a class="yt-timestamp" data-t="00:54:24">[00:54:24]</a>.

This integration provides actionable solutions that directly address business problems, such as suggesting the best budget allocation for marketing spend, and allows for simulations to explore different scenarios <a class="yt-timestamp" data-t="00:55:01">[00:55:01]</a>.