---
title: Impact of interventions on data distributions
videoId: eCtLAt-6yps
---

From: [[causalpython]] <br/> 

Interventions, or deliberate actions within a system, fundamentally change the underlying data generating process, shifting it from an observational distribution to an interventional distribution <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. Understanding this shift is crucial for accurate modeling and decision-making, especially in high-stakes scenarios <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## The Fundamental Distinction: Prediction vs. Intervention

A key difference between associative and causal models lies in their application to blind prediction versus decision-making <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Associative models can perform well when passively observing a system and assuming its dynamics are stationary over time <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. However, as soon as an intervention occurs—such as rebalancing a marketing budget, updating a manufacturing pipeline, or changing a global supply chain—the system moves away from its observational distribution <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This means the underlying data generating process has changed <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

## Why Associative Models Fail with Interventions

Associative models, like deep learning algorithms, are often chosen to minimize an in-sample error term, leading to potential overfitting <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. If the chosen covariates do not actually drive how the data is generated, the model may perform well in the training domain but fall apart when encountering out-of-sample data or interventions <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. When an intervention occurs, the model ends up representing a "completely wrong distribution" <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

For instance, if a multi-million dollar marketing campaign is launched based on an associative model that incorrectly identifies how a target audience is influenced, it could have zero effect, leading to a loss of trust in the model <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## Causal Models for Interventional Data

Causality, in essence, involves figuring out the correct way to factor the joint distribution to capture the true data generating process <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This means understanding the "information flow" between variables <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Structural Causal Models (SCMs) at Causal Lens

At Calin, the approach to causality follows the Pearl School, working extensively with Structural Causal Models (SCMs) <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. These models allow for prediction even when intervening in a system, as they explicitly represent the underlying data generating process <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

The development of an SCM typically involves an iterative process:
1.  **Graph Iteration with Customers:** Incorporating domain knowledge, especially regarding variable hierarchies, helps to reduce the search space for possible graphs <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. For example, age is a source node (nothing drives it), while an advertising channel is an intervenable variable <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
2.  **Causal Discovery Algorithms:** A suite of algorithms (constraint-based, score-based, continuous optimization, model-based like LinGAM) is used <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. The choice of algorithm depends on data types (e.g., score-based for continuous, constraint-based for mixed categorical and continuous) <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
3.  **Functional Dependencies:** After settling on a Directed Acyclic Graph (DAG), the next step is to define the functional dependencies of each node given its parents <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. Various backends like PyTorch, CVXPy, or Pyro are used to learn these functional forms, allowing for different types of relationships (e.g., linear, polynomial, monotonic) <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### [[Machine Learning and Treatment Effect Estimation | Debiased Machine Learning]] (Double ML) Inspired Training

A key improvement is training the SCM using a methodology inspired by [[Machine Learning and Treatment Effect Estimation | debiased machine learning]] (Double ML) <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. While Double ML is often specific to a known treatment and outcome, this extended approach aims to learn functional dependencies across the entire SCM, enabling unbiased estimation of treatment effects between *any* pair of variables when an intervention occurs <a class="yt-timestamp" data-t="00:30:45">[00:30:45]</a>. This might lead to some loss in predictive accuracy for individual nodes or targets but ensures unbiased treatment effect estimation <a class="yt-timestamp" data-t="00:31:17">[00:31:17]</a>.

### Uncertainty Quantification in Interventional Settings

For uncertainty quantification in interventional settings, methods like conformal prediction can be integrated <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. For example, in a causal impact package (which handles time series data with mixed interventional and observational periods), after training an SCM pre-intervention, the "do operator" is applied to simulate the intervention and predict post-intervention outcomes <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>. Uncertainty estimations can then be obtained through quantile regression, bootstrapping, and conformal prediction <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.

## Real-World Implications of Interventions

### Safety-Critical Domains

In domains where decisions are high-value or safety-critical, such as healthcare, it is imperative to identify what truly drives a target of interest to generalize to unseen data, rather than merely minimizing in-sample error <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. For example, using generative AI for legal documentation that "hallucinates" non-existent cases can have severe consequences, unlike creative or low-risk applications <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

### Business Decisions

Similarly, in manufacturing, modeling underlying physical systems can be quite effective because the information flow is highly constrained, making it easier to identify root causes of anomalous outcomes like poor yield rates <a class="yt-timestamp" data-t="00:57:36">[00:57:36]</a>. In contrast, complex systems like supply chains, which are non-stationary and lack sufficiency (meaning not all variables are measurable), require advanced preprocessing techniques to apply standard causal discovery methods <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.

## The Future is Causal

The future of data science is undoubtedly causal, especially in contexts where decisions involve high value, safety-critical systems, or where errors could be detrimental to life or revenue <a class="yt-timestamp" data-t="01:26:04">[01:26:04]</a>. Understanding and modeling the impact of interventions allows for informed decision-making and optimal treatment selection, moving beyond implicit assumptions to explicit representations of the data generating process <a class="yt-timestamp" data-t="01:17:36">[01:17:36]</a>.