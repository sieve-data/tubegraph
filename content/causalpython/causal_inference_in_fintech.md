---
title: Causal inference in fintech
videoId: y59_XLOnmgI
---

From: [[causalpython]] <br/> 

Matheus Furi, a staff data scientist at one of Brazil's largest banks, discusses the application of [[causal_inference_in_practical_applications | causal inference]] in the financial industry. He defines [[causal_inference_in_practical_applications | causal inference]] as a collection of concepts from multiple fields, including [[machine_learning_and_causal_inference_methodologies | reinforcement learning]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## The Shift from Prediction to Decision-Making

Matheus initially worked with traditional predictive models, which provide a number but don't inherently tell a company what decision to make <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Companies are primarily interested in making decisions that lead to desired outcomes, such as acquiring more customers, increasing conversion rates, boosting profitability, or cutting costs <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. A predictive model is often just one small piece of a larger system aimed at optimization <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

For example, a model might predict the probability of a customer paying their debt <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. However, it doesn't answer whether the company should target those most likely to pay or those least likely <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. [[causal_inference_in_practical_applications | Causal inference]] provides a formalized framework to evaluate and determine the best actions and decisions, rather than simply forcing predictive models into a decision-making process <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This need for a formalized framework to optimize decisions led Matheus to [[causal_inference_in_practical_applications | causal inference]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

He emphasizes that businesses don't typically care about pure prediction; they care about making effective decisions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. While a [[causal_inference_and_machine_learning | machine learning]] predictive model might be sufficient for fraud detection, most business cases require executing a decision, like setting a price or targeting an ad <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. In such scenarios, [[causal_inference_and_decision_theory | causal inference]] offers a natural formalization for the decision-making process <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

## Real-world Applications in Finance

Matheus highlights several specific applications of [[causal_inference_in_finance | causal inference in finance]]:

### Debt Collection
In debt collection, a predictive model can estimate the probability of someone paying their debts <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The challenge is deciding who to target (those likely to pay or unlikely) to maximize recovery <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This requires understanding the incremental impact of actions like calling a customer <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.

### Cross-selling and Personalization
When considering cross-selling financial products, such as upgrading a customer to a prime credit card, [[causal_inference_in_practical_applications | causal inference]] helps identify who would benefit most from the action <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. This is framed as a "personalization" problem, or in technical terms, "treatment effect heterogeneity" <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Managers and product managers are very interested in treating users differently based on their specific needs and responses <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Credit Lines and Loan Amount
Understanding the nonlinear impact of credit lines on the probability of a loan defaulting is another complex application <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. As credit lines increase, the probability of default also increases, but it eventually saturates and flattens out <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. Similarly, estimating the impact of interest rates on the amount borrowed is crucial, especially when many customers don't take out a loan (resulting in a "huge spike on the zero" in the data) <a class="yt-timestamp" data-t="00:35:43">[00:35:43]</a>.

## Challenges in Applying Causal Inference in Fintech

### Evaluation Metrics and Model Selection
A significant challenge is developing good evaluation metrics for [[causal_inference_in_practical_applications | causal inference]] models <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. Unlike traditional [[causal_inference_and_machine_learning | machine learning]] where cross-validation and metrics like AUC are straightforward, causal quantities are often unobservable, making performance evaluation difficult <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>. Matheus suggests applying a "meat grinder framework" – trying many models and selecting based on the best performance metric – to [[causal_inference_in_practical_applications | causal inference]] <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

### Feature Selection
Feature selection for [[causal_inference_in_practical_applications | causal models]] is "incredibly hard" <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.

### Nonlinearity
Dealing with nonlinear relationships, such as the impact of credit lines on default probability, presents a "very tough problem" <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

### Conversion/Selection Bias Issues
Matheus describes the "conversion issue" where a vast majority of customers do not convert (e.g., don't take a loan) <a class="yt-timestamp" data-t="00:35:33">[00:35:33]</a>. Naively filtering out these zeros can introduce "spurious paths" and lead to selection bias, which negates the benefits of randomization <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>. However, he notes that by breaking down the problem into sub-problems (e.g., effect of price on conversion, and effect of price on loan amount *given* conversion) and multiplying them, the bias can surprisingly disappear <a class="yt-timestamp" data-t="00:37:26">[00:37:26]</a>. This counter-intuitive mathematical property holds even in nonlinear cases <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.

## [[causal_inference_and_machine_learning | Reinforcement Learning]] and [[Causal inference and machine learning | Causal Inference]]

Matheus believes [[machine_learning_and_causal_inference_methodologies | reinforcement learning]] is a "flavor of [[causal_inference_in_practical_applications | causal inference]]" or vice versa <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>. Both fields involve optimizing an outcome metric by performing actions based on environmental information <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>. The action in [[causal_inference_in_practical_applications | causal inference]] is called a "treatment" <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.

A key benefit of connecting these fields is "offline policy evaluation" from [[machine_learning_and_causal_inference_methodologies | reinforcement learning]] <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>. This allows evaluating how different policies or decisions would have performed on past data, even if those policies were never deployed in production <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

However, [[machine_learning_and_causal_inference_methodologies | reinforcement learning]] agents can still be susceptible to confounding and learn associational world models if not careful <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>. Matheus advocates for human oversight in retraining models to debias data, for example, by making actions probabilistic instead of deterministic to use techniques like propensity scoring <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.

## Deploying Causal Models at Scale (CausalOps)
For deploying [[causal_inference_in_practical_applications | causal models]] at scale (CausalOps), Matheus advises treating them as much as possible like standard [[causal_inference_and_machine_learning | machine learning]] models <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>. While [[causal_inference_in_practical_applications | causal inference]] models predict something unobservable (the treatment effect for an individual), they are still predictive models from a production standpoint <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>. He recommends using standard libraries and avoiding models that are too slow due to pure Python implementations, preferring those with efficient C++ backends <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.

## The Importance of Communication and Language
A significant challenge for Matheus was learning how to phrase [[causal_inference_in_practical_applications | causal problems]] so that data scientists could understand them <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. He notes the "language barrier" within causality itself, with different backgrounds (econometrics, epidemiology, graphical models) using different terminologies like potential outcomes versus Judea Pearl's graphical language <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

Matheus primarily gravitates towards the potential outcome framework from econometrics <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. He uses graphical models mainly to formalize problems and explain assumptions to technical colleagues at the beginning of a project, rather than for estimation or identification throughout the entire process <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

Being able to structure thoughts well and communicate effectively, translating technical difficulties without "dumbing it down," is a crucial non-technical skill <a class="yt-timestamp" data-t="01:08:15">[01:08:15]</a>.

## Future Outlook
Matheus believes [[causal_inference_in_practical_applications | causal inference]] is the **present** for companies <a class="yt-timestamp" data-t="00:48:01">[00:48:01]</a>. Companies are realizing that while they have many models and data scientists producing predictions, the ultimate goal is to make better decisions <a class="yt-timestamp" data-t="00:48:27">[00:48:27]</a>. [[causal_inference_in_practical_applications | Causal inference]] offers a natural and seamless way to integrate decision-making with [[causal_inference_and_machine_learning | machine learning]], moving beyond just outputting numbers to outputting decisions that improve over time <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>.