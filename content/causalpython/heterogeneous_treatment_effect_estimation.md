---
title: Heterogeneous treatment effect estimation
videoId: w9Dy4xqn7mA
---

From: [[causalpython]] <br/> 

Heterogeneous Treatment Effect (HTE) estimation, also known as Conditional Average Treatment Effect (CATE) estimation, is a core area of focus in causal machine learning. It seeks to understand how the effect of a treatment or intervention varies across different individuals or subgroups within a population <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Alicia's research, for example, has centered on understanding *why* machine learning methods work well for [[individual_treatment_effects | individual treatment effect estimation]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Defining Treatment Effects

A treatment effect is defined as the expected value of the difference between an individual's outcome if they received a treatment versus if they did not receive it <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

## Estimation Strategies

There are two primary strategies for estimating treatment effects <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>:

1.  **Two-Step Estimation:**
    *   First, estimate the expected outcome under one treatment condition.
    *   Second, estimate the expected outcome under the alternative treatment condition.
    *   Finally, calculate the difference between these two estimates <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
2.  **Direct Targeting:**
    *   Estimate the treatment effect directly without necessarily having the two separate expected outcome values as byproducts <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
    *   Direct targeting tends to be a more efficient and effective strategy when the problem of learning the treatment effect itself is structurally simpler than learning the two potential outcome functions separately <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

## Challenges in HTE Estimation

Estimating heterogeneous treatment effects presents unique challenges compared to standard prediction problems <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>:

*   **Covariate Shift:** When the group receiving treatment differs significantly from the group not receiving treatment, models can suffer from the effects of covariate shift <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This is a major theme in the literature <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   **Unobserved Label:** The true label of interest, the difference between potential outcomes for an individual, is inherently unobserved. In reality, only one of the two potential outcomes can be observed for any given individual <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. This missingness makes the learning process quite challenging <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.
*   **Evaluation Problem:** Due to the unobservable nature of potential outcomes and the untestable nature of necessary assumptions, it is difficult to reliably validate whether HTE models work effectively in practice <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. This poses a significant hurdle for deploying these models, especially in safety-critical applications like health or policymaking <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
    *   While some testable implications, like checking potential outcome predictions against factual observations, can provide a first step in evaluation, models that perform best at predicting outcomes are not necessarily the best at predicting treatment effects <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. Errors in potential outcome predictions can either cancel out or be magnified when calculating the difference for the treatment effect, making evaluation complex, especially in low-data regimes <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.
*   **Benchmarking Practices:** A NeurIPS 2021 paper, "Really Doing Great at Estimating CATE," highlighted that simulated datasets used for benchmarking often contain problem characteristics that unfairly favor specific types of estimators <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>. These characteristics are not always rooted in realistic data generating processes, leading to a need for more authoritative statements on expected real-world data generating processes to create better benchmarking testbeds <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.

## HTE in Broader Contexts

### Machine Learning and Causality

The field of HTE estimation exists at the intersection of machine learning and causality. Machine learning literature often prioritizes showing that something works ("what") rather than understanding *why* or *when* it works <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Conversely, fields like statistics and econometrics emphasize understanding assumptions and scenarios where methods perform well, which is crucial in safety-critical environments <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

The "why" question is central to Alicia's research approach, even in non-causal machine learning contexts like "double descent" <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. She advocates for integrating statistical intuition, which helps determine when methods will and will not work, into machine learning <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

### Causality and Automated Decision Systems

For building reliable automated decision systems, particularly in safety-critical applications like health, some form of knowledge about how a system behaves under intervention is necessary <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. If a perfect model of the underlying Structural Causal Model (SCM) of the world could be obtained, it would theoretically allow for decisions on any intervention <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

### Frameworks: Potential Outcomes vs. Causal Graphs

*   **Causal Graphs (DAGs):** These are incredibly useful for representing assumptions, especially for communicating with non-machine learning or non-statistical stakeholders (e.g., doctors) <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>. They excel at depicting complex problem structures, such as biases arising from non-simple variable setups, and are invaluable when dealing with higher-dimensional problems, including [[timevarying_treatments_in_machine_learning | time]] <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.
*   **Potential Outcomes:** This framework is preferred for reasoning about the estimators themselves, as it allows for thinking about treatment effects as the difference between two potential outcomes <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.
    *   The potential outcomes framework and the causal graph (DAG) framework are not contradictory; there are papers showing their equivalence <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>.

## Future Directions and Opportunities

There is a significant opportunity to explore more realistic and wider classes of problems in HTE estimation, moving beyond single-treatment, simple outcome, static data scenarios <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>. Real-world problems often involve multiple complexities, including <a class="yt-timestamp" data-t="00:50:03">[00:50:03]</a>:
*   Time-varying treatments <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>
*   Different types of outcomes <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>
*   Multiple treatments and treatment combinations <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>
*   Missingness and informative sampling <a class="yt-timestamp" data-t="00:50:13">[00:50:13]</a>

### Missing Data as a Unifying Perspective

Many additional complexities in HTE, such as survival analysis, competing risks, censoring, and informative sampling, can ultimately be framed as problems of missing data <a class="yt-timestamp" data-t="00:50:45">[00:50:45]</a>. As more layers of complexity are added, the data becomes sparser, and more covariate shifts are induced by various missingness mechanisms <a class="yt-timestamp" data-t="00:51:04">[00:51:04]</a>. There is significant potential in jointly tackling these missingness problems, viewing them as different manifestations of the same underlying challenge <a class="yt-timestamp" data-t="00:51:37">[00:51:37]</a>. This perspective aligns with the work of researchers like Donald Rubin, who explored both causality and missingness <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>.

### Sensitivity Analysis

Sensitivity analyses are interesting tools to perturb assumptions and observe the impact on estimates <a class="yt-timestamp" data-t="00:47:04">[00:47:04]</a>. For example, in treatment effect estimation, a sensitivity model can be placed on the amount of hidden confounding to understand its impact on estimates, including potentially flipping their sign <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>. Modern machine learning ideas, such as conformal prediction intervals, are being used to bound the effects of unobserved confounding <a class="yt-timestamp" data-t="00:35:31">[00:35:31]</a>. Beyond confounding, sensitivity models can be applied to other aspects of real problems, such as censoring in survival data or missingness in observed data <a class="yt-timestamp" data-t="00:48:08">[00:48:08]</a>.

### Future of Machine Learning and Causality

Causality is increasingly making its way into mainstream machine learning, especially as researchers realize the importance of causal thinking for generalization to new settings and for building systems that take actions <a class="yt-timestamp" data-t="00:32:19">[00:32:19]</a>. Taking an action is, in essence, performing an intervention on the environment <a class="yt-timestamp" data-t="00:32:36">[00:32:36]</a>. Ideas from causality, such as the invariance of causal mechanisms, can lead to more robust and stable models <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>. The near-term future is likely to be "causality-inspired," potentially becoming fully causal at some point <a class="yt-timestamp" data-t="00:57:41">[00:57:41]</a>.

The biggest challenge in causality that Alicia would like to see solved is developing better ways to evaluate if models work in practice <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>. This would involve methods to validate untestable assumptions, perhaps by mapping domain expertise into mechanisms that can confirm if assumptions are likely to hold <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>.