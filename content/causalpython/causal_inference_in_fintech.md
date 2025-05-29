---
title: Causal inference in fintech
videoId: y59_XLOnmgI
---

From: [[causalpython]] <br/> 

[[Causal inference and its applications | Causal inference]], often referred to as a collection of concepts from multiple fields, is increasingly relevant in industries like fintech, where the goal extends beyond mere prediction to optimized decision-making and personalization <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Matos Fakri's Perspective

Matos Fakri, an author and staff data scientist at one of Brazil's largest banks, highlights the critical role of [[causal_inference_and_its_applications | causal inference]] in the financial sector <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

He observed the value of [[causal_inference_concepts_and_applications | causal inference]] when working with traditional predictive models <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. While predictive models can forecast outcomes (e.g., a number), companies primarily seek to transform these predictions into actionable decisions <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## The Limitation of Predictive Models

Businesses, including financial institutions, are generally less interested in pure prediction and more concerned with making decisions that yield concrete results, such as acquiring more customers, increasing conversion rates, boosting profitability, or reducing costs <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. A predictive model serves only as a small part of a larger decision-making system <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

Matos explains that companies often ask why they should invest in [[causal_inference_methods_and_applications | causal models]] if they already use machine learning <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. His answer emphasizes that while [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]] models are good for predictions, they often fall short in guiding optimal actions. For example, a fraud detection model predicting a fraudulent transaction is directly actionable <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. However, for tasks like determining pricing, targeting advertisements, or deciding who to call, [[causal_inference_and_decision_making | causal inference]] offers a more natural framework for decision-making <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

## Applications of Causal Inference in Finance

### Debt Collection
In a debt collection scenario, a highly accurate predictive model could forecast the probability of someone paying their debts <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The challenge then becomes how to utilize this information effectively: should the company target individuals most likely to pay, or those least likely? <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a> Matos realized that [[causal_inference_in_finance | causal inference]] provides the necessary framework to translate such probabilities into an optimized strategy for the company <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Personalization and Cross-Selling
[[Causal inference concepts and applications | Causal inference]] can be used to personalize strategies, treating users differently based on their specific needs and predicted responses to interventions <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This is known as "treatment effect heterogeneity" <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

For instance, in cross-selling, a bank might want to upgrade a credit card user to a prime credit card <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. The question is: who would benefit most from this cross-sell? <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a> [[Causal inference and decision making | Causal inference]] helps identify customers for whom the cross-selling action would have the highest incremental impact on their probability of converting <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.

### Credit Lines and Default Probability
Another complex problem involves understanding the non-linear impact of credit lines on the probability of someone defaulting on their loan <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. Initially, increasing a credit line might increase default probability, but at some point, it may saturate and flatten <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. This non-linearity makes it a challenging problem to model and evaluate <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.

## Challenges in Applying Causal Inference in Finance

### Non-linearity
Dealing with non-linear relationships, such as the impact of credit lines on default probability, poses a significant challenge <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

### Evaluation Metrics for Causal Models
Developing robust evaluation metrics for [[causal_inference_concepts_and_applications | causal models]] is difficult because causal quantities (like treatment effects) are often unobservable <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. Unlike traditional machine learning, where metrics like AUC or cross-entropy are straightforward for model selection, evaluating [[causal_inference_methods_and_applications | causal models]] requires different approaches <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>. The "meat grinder" framework, which involves trying many models and selecting the best based on performance metrics, is being adapted for [[causal inference]] <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. The core challenge here is finding a good evaluation metric for the causal model <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.

### Data Trust and Randomization
Matos emphasizes that it's difficult to trust any evaluation metric without randomized data <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. Having a trusted dataset, ideally from experiments where treatments are randomized, is crucial for validation, even if the training data is imperfect <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. This ensures the evaluation is free from biases like confounding <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.

### Confounding and Selection Bias
While Matos primarily works in settings where confounding is less of an issue due to the ability to intervene and randomize, other forms of bias, such as selection bias, remain challenging <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>.

#### Conversion Bias Example
A common challenge arises in scenarios like estimating the impact of interest rates on loan size <a class="yt-timestamp" data-t="00:34:54">[00:34:54]</a>. If only customers who took a loan are considered, it introduces a "collider bias" because conversion (taking a loan) is an outcome influenced by the interest rate <a class="yt-timestamp" data-t="00:36:30">[00:36:30]</a>. This effectively negates the benefits of randomization <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>. However, it's possible to break down the problem into two parts: the effect of price on conversion, and the effect of price on loan amount given conversion. When multiplied, the biases can disappear <a class="yt-timestamp" data-t="00:37:10">[00:37:10]</a>. This "simple mathematical truth" holds even in non-linear cases <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.

## Integration with Reinforcement Learning

Matos believes that [[causal_ai_applications_in_business_and_technology | reinforcement learning]] is a form of [[causal_inference_and_its_applications | causal inference]] or vice versa, given their similar goals: optimizing actions based on environment information to maximize a metric <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>. The "action" in [[causal_inference_in_healthcare_and_astronomy | causal inference]] is called a "treatment" <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. This connection allows for the application of reinforcement learning techniques, such as offline policy evaluation, to [[causal inference]] problems <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

Offline policy evaluation allows assessing how a different policy (set of decisions) would have performed on past data, even if it was never implemented in production <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>. While reinforcement learning models are often perceived as self-updating, Matos advocates for a human-in-the-loop approach to debias data and prevent models from learning mere correlations instead of causation <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>. Techniques like making actions probabilistic instead of deterministic, combined with propensity scores, can help correct for biases <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

## CausalOps

For deploying [[industrial_applications_of_causal_inference | causal models]] at scale, Matos suggests treating them as much as possible like standard machine learning models, leveraging existing MLOps practices <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>. Although [[causal_inference_in_finance | causal treatment effect heterogeneity]] involves predicting an unobservable impact of a treatment on an individual, the production aspect is still akin to a predictive model <a class="yt-timestamp" data-t="00:30:43">[00:30:43]</a>. Challenges include the efficiency of implementations, as many [[causal inference]] models are still pure Python rather than optimized C++ with Python wrappers <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.

## The Future of Causal Inference in Industry

Matos believes that [[causal_ai_applications_in_business_and_technology | causal inference]] is already the "present" for companies <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>. As businesses realize that their ultimate goal is to make better decisions, not just better predictions, they will increasingly adopt [[causal_inference_and_decision_making | causal inference]] to integrate decision-making seamlessly with machine learning <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>. This evolution will allow companies to supercharge their data science capabilities to output improved and more optimal decisions over time <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>.

The banking sector, with its established culture of economics and econometrics, is particularly well-suited for adopting [[causal_inference_in_finance | causal inference]] due to its complex problems and existing literature <a class="yt-timestamp" data-t="01:07:27">[01:07:27]</a>.