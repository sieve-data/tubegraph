---
title: Machine Learning and Treatment Effect Estimation
videoId: w9Dy4xqn7mA
---

From: [[causalpython]] <br/> 

Alicia, a researcher at the University of Cambridge, focuses her work on understanding *why* machine learning methods work, rather than just showing that they work <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. This approach stems from her background in statistics and econometrics, where the emphasis is on understanding assumptions and scenarios where methods perform well <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. Her research specifically delves into [[causal_inference_and_individual_treatment_effects | treatment effect estimation]] in machine learning <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

## Core Research Focus: Understanding Machine Learning Methods

Alicia emphasizes the need to understand existing methods before building new ones, specifically understanding what they work well for and where they fail <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. Her research often involves stress-testing different strategies to identify promising avenues and their underlying reasons for success <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

> "Most of my research has just very much focused on the word why my machine learning is very good or the the literature on [[causal_inference_and_individual_treatment_effects | treatment effect estimation]] in machine learning specifically had been very good at Building Solutions and I think machine learning as a literature often focuses on the showing that something works but never so much on why or when" <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.

## Insights into Heterogeneous Treatment Effect Estimation

Alicia's early work on heterogeneous treatment effect estimation revealed that the best strategy depends on the assumed underlying problem structure <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.

### Estimation Strategies
There are two main ways to estimate a treatment effect (the expected difference between an outcome given treatment versus no treatment):
1.  **Indirect Estimation**: First estimate the expected outcome under one treatment, then under the other, and take the difference <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.
2.  **Direct Targeting**: Directly estimate the treatment effect without separately estimating the two expected values <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>.

Direct targeting is often a better strategy if the problem of learning the treatment effect itself is simpler than learning the two potential outcome functions separately <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.

### Unique Challenges in Treatment Effect Estimation
From a technical standpoint, two unique challenges arise in [[causal_inference_and_individual_treatment_effects | treatment effect estimation]]:
1.  **Covariate Shift**: When the group receiving treatment looks very different from the group not receiving treatment, models can suffer from covariate shift effects <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>.
2.  **Missing Label Problem**: The true label of interest, the difference between potential outcomes for an individual (e.g., if I were treated versus if I weren't), is unobserved because only one of the two can ever be observed in reality <a class="yt-timestamp" data-t="17:27:00">[17:27:00]</a>. This makes learning challenging <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>.

## Influence of Background on Machine Learning Approach

Alicia's entry into machine learning was through [[causal_inference_and_individual_treatment_effects | treatment effect estimation]], coming from a policy economics background <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>. This reversed pathway (using ML for causality rather than applying ML to causal problems) shaped her focus <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.

Her econometrics background emphasized:
*   Understanding the necessary assumptions for methods to work <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
*   Identifying scenarios where methods perform well <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>.

This perspective is crucial in "safety-critical environments" like policy economics and biostatistics, where decisions based on estimates must be correct <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>. She advocates for retaining "statistical intuition" and understanding failure modes of methods, rather than viewing machine learning as a "magic bullet" that defies statistical laws <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.

## Challenges in Model Evaluation for Causal Machine Learning

A significant hurdle for deploying [[causal_inference_and_individual_treatment_effects | treatment effect estimation]] models in practice is the evaluation problem <a class="yt-timestamp" data-t="18:04:00">[18:04:00]</a>.

### Untestable Assumptions and Simulated Data
It's difficult to validate whether a heterogeneous treatment effect system works when deployed because the underlying assumptions are untestable in practice, and access to both potential outcomes is impossible <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.

Research has shown that current benchmarking practices often rely on simulated datasets whose characteristics heavily favor specific types of estimators, not necessarily reflecting real-world data generating processes <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>. There's a need for more authoritative statements on likely real-world data generating processes to create better benchmarking test beds <a class="yt-timestamp" data-t="21:01:00">[21:01:00]</a>.

### Predicting Outcomes vs. Predicting Treatment Effects
While models can be evaluated by checking potential outcome predictions against factual observations, models that predict outcomes best are not necessarily the ones that predict treatment effects best <a class="yt-timestamp" data-t="23:09:00">[23:09:00]</a>. This is because a treatment effect is a difference between two predictions, and errors can either cancel out or add up <a class="yt-timestamp" data-t="23:37:00">[23:37:00]</a>. In low-data regimes, it's harder to judge treatment effect estimator performance based solely on potential outcome predictions <a class="yt-timestamp" data-t="24:50:00">[24:50:00]</a>.

## Causal Frameworks: Potential Outcomes vs. Causal Graphs

Alicia highlights the utility of both the potential outcomes framework and causal graphs (DAGs).

### Causal Graphs (DAGs)
[[machine_learning_and_causality | Causal graphs]] are "incredibly useful as a tool to represent your assumptions" <a class="yt-timestamp" data-t="25:28:00">[25:28:00]</a>. They facilitate communication with non-technical stakeholders (e.g., doctors) about confounders and problem structures <a class="yt-timestamp" data-t="25:35:00">[25:35:00]</a>. They are particularly helpful for problems with:
*   More complex causal structures <a class="yt-timestamp" data-t="25:56:00">[25:56:00]</a>.
*   Higher dimensionality, such as [[timevarying_treatments_in_machine_learning | time-varying treatments in machine learning]] or multiple outcomes (e.g., competing risks in survival analysis) <a class="yt-timestamp" data-t="26:11:00">[26:11:00]</a>.

### Potential Outcomes Framework
Alicia prefers using potential outcomes for reasoning about estimators themselves <a class="yt-timestamp" data-t="27:00:00">[27:00:00]</a>, finding the concept of a treatment effect as the difference between two potential outcomes to be a very useful way of depicting things <a class="yt-timestamp" data-t="27:20:00">[27:20:00]</a>. She doesn't see the two frameworks as contrasting, noting existing papers showing their equivalence <a class="yt-timestamp" data-t="27:31:00">[27:31:00]</a>.

## Broader Complexities and Future Directions

Alicia emphasizes the need to broaden the scope of [[causal_inference_and_machine_learning | causal machine learning]] to address more realistic problems, moving beyond simple static data with single treatments <a class="yt-timestamp" data-t="49:59:00">[49:59:00]</a>.

### Realistic Problem Characteristics
Real-world problems often involve:
*   Time <a class="yt-timestamp" data-t="50:06:00">[50:06:00]</a>
*   Different outcomes <a class="yt-timestamp" data-t="50:07:00">[50:52:00]</a>
*   Multiple treatments or treatment combinations <a class="yt-timestamp" data-t="50:07:00">[50:07:00]</a>
*   Missingness, informativeness, and how things are sampled <a class="yt-timestamp" data-t="50:13:00">[50:13:00]</a>.

Most of these additional complexities ultimately boil down to a "missingness problem" where not everything one wants to observe is observed <a class="yt-timestamp" data-t="50:57:00">[50:57:00]</a>. She suggests a unifying perspective that treats these challenges as aspects of a missing data problem, similar to how Donald Rubin approached both causality and missingness <a class="yt-timestamp" data-t="52:00:00">[52:00:00]</a>.

### Sensitivity Analysis
Sensitivity analyses are a promising tool to perturb assumptions and assess their impact on estimates, especially concerning unobserved confounding <a class="yt-timestamp" data-t="47:04:00">[47:04:00]</a>. This includes exploring how errors propagate over time if initial assumptions are not met <a class="yt-timestamp" data-t="49:03:00">[49:03:00]</a>.

### Future of Machine Learning and Causality
Causality is gaining traction in mainstream machine learning, especially in areas like generalization and building systems that take actions (performing interventions) <a class="yt-timestamp" data-t="32:11:00">[32:11:00]</a>. Alicia believes there is huge potential to incorporate causal ideas, such as the invariance of causal mechanisms, to build more robust and stable models <a class="yt-timestamp" data-t="57:52:00">[57:52:00]</a>.

The biggest challenge in causality, in her view, is developing better ways to evaluate that models work in practice and to validate untestable assumptions, potentially by mapping domain expertise to assumption validation <a class="yt-timestamp" data-t="33:02:00">[33:02:00]</a>.

## Critique of Machine Learning Publication Culture

Alicia observes a contrast between the cultures of statistics/econometrics and machine learning publications:
*   **Statistics/Econometrics**: Focuses on understanding the structure of a problem and the solutions needed <a class="yt-timestamp" data-t="55:06:00">[55:06:00]</a>.
*   **Machine Learning**: Often centered on "horse races" to achieve state-of-the-art results and demonstrating methodological novelty <a class="yt-timestamp" data-t="54:37:00">[54:37:00]</a>.

Alicia finds it challenging to publish research focused on understanding existing methods and gaining new insights into problems because the community primarily looks for novelty in architectures or methods themselves <a class="yt-timestamp" data-t="55:27:00">[55:27:00]</a>. This leads to a proliferation of methods with the same failure modes, as researchers don't step back to understand *why* things work <a class="yt-timestamp" data-t="56:11:00">[56:11:00]</a>.

> "We don't need more and more and more methods necessarily like if they all have the same failure mode for example if we keep on focusing on one aspect of the problem and ignoring another one because no one ever takes a step back and looks at what are we actually doing here" <a class="yt-timestamp" data-t="56:13:00">[56:13:00]</a>.

She cites the paper "Troubling Trends in Machine Learning Scholarship" which discusses the lack of focus on "sources of gain" (why a new method performs better) <a class="yt-timestamp" data-t="56:55:00">[56:55:00]</a>.

## Personal Philosophy and Advice

Alicia attributes her academic journey to curiosity, a love for statistics, and a passion for learning new things <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>. Her initial accidental foray into econometrics, despite disliking high school statistics, turned out to be a "very happy accident" <a class="yt-timestamp" data-t="29:12:00">[29:12:00]</a>.

Her advice for those starting in causality is to focus on finding a way to get the intuition right first <a class="yt-timestamp" data-t="43:03:00">[43:03:00]</a>. For the [[machine_learning_and_causality | causal machine learning]] community, her message is to "keep asking why" <a class="yt-timestamp" data-t="59:17:00">[59:17:00]</a>. She believes that the focus on distinguishing correlation from causation inherently trains [[machine_learning_and_causality | causal machine learning]] researchers to ask "why," a valuable trait <a class="yt-timestamp" data-t="59:51:00">[59:51:00]</a>.