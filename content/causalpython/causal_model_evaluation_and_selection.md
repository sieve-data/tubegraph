---
title: Causal model evaluation and selection
videoId: y59_XLOnmgI
---

From: [[causalpython]] <br/> 

[[Causality and Causal Models | Causal inference]] is a collection of concepts from multiple fields, including reinforcement learning, that focuses on identifying optimal actions and decisions rather than solely making predictions <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. At its heart, the problem often revolves around evaluating and selecting the best [[Causality and Causal Models | causal models]] to guide these decisions <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.

## Challenges in Causal Model Evaluation

Evaluating [[Causality and Causal Models | causal models]] presents unique challenges compared to traditional predictive machine learning models:

*   **Unobservable Causal Quantities**
    [[Causality and Causal Models | Causal quantities]] are often "non-observables," making it difficult to define direct performance metrics <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. Unlike predictive models where metrics like AUC or cross-entropy can be directly calculated on observable outcomes, evaluating a [[Causality and Causal Models | causal model]] requires inferring effects that cannot be directly seen <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>.

*   **Non-linearity**
    Relationships between interventions (like credit lines) and outcomes (like defaulting on a loan) are often non-linear <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. For example, increasing a credit line might initially increase the probability of default, but then saturate and become flat after a certain point <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. Capturing and evaluating these complex, non-linear responses is a significant challenge <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

*   **Confounding and Bias**
    A primary concern in [[Causality and Causal Models | causal inference]] is confounding bias, where factors not accounted for influence both the "treatment" and the outcome <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. For instance, if people who drink wine tend to live longer, it's crucial to adjust for other factors like socioeconomic status or healthcare access to determine if it's the wine or other variables <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. While some industry settings allow for [[Interventions and causal models | interventions]] and randomization, mitigating confounding remains a core concern <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

    Other types of bias, such as selection bias or collider bias, can also arise <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>. This happens when conditioning on a variable that is a collider (an outcome of two independent causes), which can inadvertently open a spurious path and lose the benefits of randomization <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>. An example is filtering a dataset to only include customers who "converted" (e.g., took a loan), which can bias the estimation of interest rates on loan amounts <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>.

## Approaches to Causal Model Evaluation and Selection

### The "Meat Grinder" Framework
To overcome the difficulty of evaluating [[Causality and Causal Models | causal models]], a "meat grinder" framework, inspired by traditional machine learning, is proposed <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. This involves:
1.  **Trying a Bunch of Things**: Experimenting with various [[Causality and Causal Models | causal inference]] models and configurations <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>.
2.  **Performance Metric**: Identifying a reliable performance metric for [[Causality and Causal Models | causal models]] (a major challenge in itself <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>).
3.  **Selection**: Picking the model that performs best based on this metric and deploying it <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.

This approach aims to enable practices like cross-validation and feature selection for [[Causality and Causal Models | causal models]] <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>.

### The Role of Randomized Data
The most important lesson in [[Evaluating causal models in practice | evaluating causal models in practice]] is the necessity of reliable, randomized data <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.
*   **Trustworthy Validation Set**: Having a dataset where treatments are randomized and thus free from biases allows for a trustworthy validation set <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. This set can be used to compute [[Causality and Causal Models | causal metrics]] with confidence <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.
*   **Simplified Decision-Making**: Randomizing simplifies the evaluation process and ensures the analysis is not overly complicated by confounding <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. If a model doesn't perform well on randomized data, it's unlikely to perform well in production <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.

### Lessons from Reinforcement Learning
[[Causal inference]] is closely related to reinforcement learning (RL), often seen as a "flavor" of it <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>. Both involve optimizing an action to maximize a metric given an environment (or covariates) <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.
*   **Offline Policy Evaluation**: RL provides techniques like offline policy evaluation, which allows assessing how alternative policies (decisions) would have performed on historical data, even if those policies were never explicitly implemented <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>.
*   **Human in the Loop**: While RL models can self-update, it's crucial to have a human in the loop to debias data <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>. Without careful intervention, RL agents can learn correlations instead of causation, leading to suboptimal decisions <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>. Techniques like making actions probabilistic instead of deterministic and using propensity scores can correct for these biases <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

### Tackling Complex Problem Decomposition
In cases where direct causal estimation is difficult due to data distribution (e.g., many zero outcomes), complex problems can be broken down into simpler parts <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>. For example, estimating the impact of interest rates on loan amount (where many customers have zero loans) can be decomposed into:
1.  The probability of conversion given the price.
2.  The expected value of the loan amount given the price, *conditioned on conversion*.
While the second term might appear biased due to conditioning, multiplying it by the first (causal) term can make the overall bias disappear, yielding a valid causal prediction <a class="yt-timestamp" data-t="00:37:26">[00:37:26]</a>. This mathematical truth holds even in non-linear cases <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.

## CausalOps: Deploying Causal Models at Scale
Deploying [[Causality and Causal Models | causal models]] at scale, or "CausalOps," can largely leverage existing MLOps practices <a class="yt-timestamp" data-t="00:30:33">[00:30:33]</a>.
*   **Predicting Impact**: For [[Causality and Causal Models | causal models]] focused on heterogeneous treatment effects, the goal is to predict the incremental impact of a treatment for each individual <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>. From a production standpoint, this is still a predictive task, even if the predicted quantity (treatment effect) is unobservable <a class="yt-timestamp" data-t="00:31:12">[00:31:12]</a>.
*   **Standard Practices**: Using standard libraries and tools that are easy to deploy is recommended <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>. Pure Python implementations of [[Causality and Causal Models | causal models]] can be too slow for large-scale deployment, favoring models implemented in more efficient languages like C++ with Python wrappers <a class="yt-timestamp" data-t="00:31:50">[00:31:50]</a>. For example, while [[Causal reasoning and structural causal models | causal trees]] are fascinating, their pure Python implementation can make them 39 times slower than alternatives, hindering production use <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.

## Why Causal Inference is the Future
The speaker believes that [[Causality and Causal Models | causal inference]] is not just the future, but already the present, for companies <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>.
*   **Beyond Prediction**: Companies don't primarily care about predictions; they care about making better decisions that lead to tangible business outcomes, such as increasing customers, conversion rates, or profitability, or cutting costs <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>, <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Formalized Decision-Making**: While traditional machine learning models are excellent for prediction (e.g., fraud detection), they often fall short in providing a formalized framework for decision-making <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. [[Causal inference]] offers a natural and seamless way to integrate machine learning with decision-making, ensuring that decisions are optimal and improve over time <a class="yt-timestamp" data-t="00:48:58">[00:48:58]</a>.
*   **Personalization**: Framing [[Causality and Causal Models | causal inference]] problems as personalization (or "treatment effect heterogeneity") makes it an easier sell to managers, as they are often keen on tailoring experiences for different users <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This focus shifts from whether an action is good on average to whether it's better for a specific customer <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.