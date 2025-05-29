---
title: Challenges and strategies in credit decisionmaking
videoId: y59_XLOnmgI
---

From: [[causalpython]] <br/> 

Matheus Furi, a staff data scientist at one of Brazil's largest banks, discusses the application of [[causal_analysis_and_decision_making | causal inference]] in the context of credit decision-making, highlighting key challenges and solutions. <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>

## Transitioning from Prediction to Decision Making

Traditional predictive models, while good at forecasting outcomes (e.g., probability of debt repayment), often fall short in guiding direct business decisions <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>. Companies are primarily interested in making decisions that lead to tangible improvements, such as increasing customers, conversions, or profitability, or cutting costs <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.

In a debt collection scenario, a predictive model might accurately assess the probability of someone paying their debt <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>. However, it doesn't inherently tell the company *who* to target (e.g., those most likely to pay or those least likely) or how to transform this probability into an optimal business decision <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. This gap led to the realization of the value of [[causal_analysis_and_decision_making | causal inference]] in formalizing the decision-making process <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.

Pure prediction models are often not enough because businesses seek to optimize outcomes, where predictive models are merely a small part of a larger system <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. While predictive models might suffice for issues like fraud detection, most business cases require executing a decision, such as setting a price, targeting an ad, or initiating a call <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>. In such scenarios, [[causal_analysis_and_decision_making | causal inference]] offers a natural framework for decision-making and optimization <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.

## Key Challenges

*   **Translating Predictions into Decisions**
    *   The primary challenge is to convert a predictive model's output (e.g., a probability) into a concrete action or optimization for the company <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. Simply having better predictive metrics does not guarantee improved business outcomes like increased profit <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.
*   **Confounding vs. Interventions**
    *   In many business contexts, especially in banking, confounding is less of a concern because companies can intervene on variables they care about, such as sending an email, making a call, or changing a price <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>. If an intervention is controllable, it can often be randomized, like in setting prices to understand their impact on sales <a class="yt-timestamp" data-t="17:20:00">[17:20:00]</a>.
*   **Effect Heterogeneity (Personalization)**
    *   A significant challenge is understanding *who* will be most impacted by an action, rather than just the average effect <a class="yt-timestamp" data-t="17:58:00">[17:58:00]</a>. For example, in debt collection, deciding which type of customer to call first to maximize incremental impact on payment probability <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>. This is essentially a [[counterfactual_reasoning_in_decision_making | personalization]] problem <a class="yt-timestamp" data-t="19:23:00">[19:23:00]</a>.
*   **Non-linearity**
    *   Complex, non-linear relationships, such as the impact of credit lines on default probability, are difficult to model <a class="yt-timestamp" data-t="19:34:00">[19:34:00]</a>. Increasing a credit line might increase default probability, but only up to a certain saturation point where it flattens <a class="yt-timestamp" data-t="19:59:00">[19:59:00]</a>.
*   **[[Challenges in Evaluating Causal Models | Evaluation Metrics for Causal Models]]**
    *   It is difficult to devise metrics for [[challenges_in_evaluating_causal_models | evaluating causal models]], because causal quantities are inherently unobservable <a class="yt-timestamp" data-t="20:17:00">[20:17:00]</a>. Unlike traditional machine learning where cross-validation and AUC are standard, applying a "meat grinder framework" (trying many models and picking the best based on a performance metric) to causal models requires defining reliable causal evaluation metrics <a class="yt-timestamp" data-t="21:00:00">[21:00:00]</a>.
    *   Trusting evaluation metrics without randomized data is challenging, as biases can easily distort results <a class="yt-timestamp" data-t="21:59:00">[21:59:00]</a>.
*   **Delay in Outcomes**
    *   In credit, there's a significant delay between an action (e.g., giving a loan) and observing its full impact (e.g., default in two years) <a class="yt-timestamp" data-t="01:06:31">[01:06:31]</a>. This long feedback loop makes assessing immediate performance difficult <a class="yt-timestamp" data-t="01:06:39">[01:06:39]</a>.
*   **Conversion Issue (Zero-Inflated Outcomes)**
    *   When a large portion of customers do not "convert" (e.g., take a loan), the outcome variable (loan amount) is zero-inflated, leading to diluted effects if naively estimated <a class="yt-timestamp" data-t="34:48:00">[34:48:00]</a>. Filtering out these zeros introduces [[challenges_and_opportunities_in_structural_causal_models | selection bias]] because conversion is a collider in the causal path, thereby losing the benefits of randomization <a class="yt-timestamp" data-t="36:30:00">[36:30:00]</a>.

## Strategies and Solutions

*   **Leveraging [[causal_analysis_and_decision_making | Causal Inference]] for Decision Making**
    *   Instead of forcing predictive models into decision-making, [[causal_analysis_and_decision_making | causal inference]] provides a formalized framework to evaluate, decide, and optimize actions within a company <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.
*   **Focusing on Personalization (Treatment Effect Heterogeneity)**
    *   Frame problems around "personalization," which translates to "treatment effect heterogeneity" in [[causal_analysis_and_decision_making | causal inference]] <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>. Managers and product managers are highly interested in treating users differently based on their individual needs <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.
*   **Randomized Data for Evaluation**
    *   Ensure a trusted, bias-free dataset from randomized experiments for validation <a class="yt-timestamp" data-t="22:28:00">[22:28:00]</a>. This allows for reliable evaluation of causal models, even if the training data is noisy or observational <a class="yt-timestamp" data-t="22:52:00">[22:52:00]</a>. Simplfying the decision-making process through randomization simplifies the analysis <a class="yt-timestamp" data-t="23:33:00">[23:33:00]</a>.
*   **Insights from Reinforcement Learning**
    *   Reinforcement learning (RL) shares similarities with [[causal_analysis_and_decision_making | causal inference]], as both involve optimizing actions (treatments) to maximize an outcome in an environment (covariates) <a class="yt-timestamp" data-t="24:54:00">[24:54:00]</a>.
    *   **Offline Policy Evaluation (OPE):** Techniques from RL, such as OPE, allow evaluating how different policies (sequences of decisions) would have performed on past data, even if those policies were never implemented in production <a class="yt-timestamp" data-t="25:25:00">[25:25:00]</a>.
    *   **Human-in-the-Loop:** While RL models can self-update, a human in the loop can debias the data by using techniques like probabilistic actions and propensity scores <a class="yt-timestamp" data-t="27:50:00">[27:50:00]</a>. This prevents the model from learning mere correlations (e.g., calling only low-delinquency customers leads to high payment rates) rather than true causation <a class="yt-timestamp" data-t="28:51:00">[28:51:00]</a>.
*   **Decomposing Complex Problems**
    *   For problems like the conversion issue (interest rates on loan amount with many non-converting customers), the total effect can be broken down into two components: the effect of price on conversion and the effect of price on loan amount *given* conversion <a class="yt-timestamp" data-t="37:06:00">[37:06:00]</a>. Even if the second component is biased due to conditioning, multiplying the two terms mathematically eliminates the bias and yields the correct [[counterfactual_reasoning_in_decision_making | counterfactual]] prediction <a class="yt-timestamp" data-t="37:26:00">[37:26:00]</a>. This approach works for both linear and non-linear cases <a class="yt-timestamp" data-t="39:27:00">[39:27:00]</a>.
*   **CausalOps for Deployment**
    *   When deploying [[challenges_of_machine_learning_integration_in_business | causal models]] at scale, especially for heterogeneous treatment effects, they can largely be treated as standard predictive models from a production aspect <a class="yt-timestamp" data-t="30:43:00">[30:43:00]</a>.
    *   Recommendations include using standard libraries (e.g., scikit-learn), prioritizing efficiently implemented models (often C++ with Python wrappers) over pure Python implementations that might be too slow for production (e.g., Causal Forests vs. EconML) <a class="yt-timestamp" data-t="31:26:00">[31:26:00]</a>.

## Banking as a Suitable Environment for Causal Inference

The banking sector is an ideal environment for applying [[causal_inference_in_fintech | causal inference]] because it presents many interesting problems where [[causal_analysis_and_decision_making | causal analysis]] is highly relevant <a class="yt-timestamp" data-t="01:07:27">[01:07:27]</a>. Furthermore, banking already has a strong culture rooted in economics and econometrics, making it easier to find relevant literature and convince stakeholders of the value of a causal approach <a class="yt-timestamp" data-t="01:07:36">[01:07:36]</a>.