---
title: Integration of Causal Thinking in Machine Learning
videoId: w9Dy4xqn7mA
---

From: [[causalpython]] <br/> 

The "Causal Bandits" podcast frequently explores the intersection of [[causal_inference_and_machine_learning | causality and machine learning]] <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. One key focus is on understanding *why* machine learning models work, rather than just *that* they work <a class="yt-timestamp" data-t="02:27:03">[02:27:03]</a>. This approach aims to move the field forward by stress-testing existing methods and gathering comprehensive knowledge <a class="yt-timestamp" data-t="01:36:39">[01:36:39]</a>.

## A "Why" Approach to Machine Learning Research

A central theme in research is the emphasis on understanding *why* certain methods work and *when* they are effective <a class="yt-timestamp" data-t="02:27:03">[02:27:03]</a>. While the [[causal_ai_and_machine_learning_intersection | machine learning literature]] often excels at building solutions and demonstrating performance, it less frequently delves into the underlying reasons or specific conditions for success <a class="yt-timestamp" data-t="02:37:34">[02:37:34]</a>. This contrasts with fields like statistics and econometrics, which traditionally focus on understanding the mechanisms behind observed phenomena <a class="yt-timestamp" data-t="02:50:52">[02:50:52]</a>.

### The Double Descent Phenomenon: A Case Study
An example of this "why" research is the analysis of the Double Descent phenomenon in machine learning <a class="yt-timestamp" data-t="03:40:48">[03:40:48]</a>. This counterintuitive finding shows that as model complexity increases, performance initially follows a U-shaped curve, but then experiences a *second descent* when the number of parameters exceeds the training examples <a class="yt-timestamp" data-t="04:02:45">[04:02:45]</a>.

Instead of merely observing this, the research sought the root cause <a class="yt-timestamp" data-t="04:39:13">[04:39:13]</a>. The insight gained was that this phenomenon often arises not from a single 2D complexity curve, but from two separate, orthogonal complexity axes in a 3D plot <a class="yt-timestamp" data-t="06:04:47">[06:04:47]</a>. The apparent "double descent" occurs because these axes are traversed sequentially, often due to a mechanism shift in how parameters are added once a limit is reached on one axis (e.g., adding more trees instead of more leaves to a single tree) <a class="yt-timestamp" data-t="06:25:05">[06:25:05]</a>. This analysis reveals that the statistical intuition typically taught in courses still holds, making the phenomenon more understandable, even "trivial" once the 3D perspective is adopted <a class="yt-timestamp" data-t="06:48:47">[06:48:47]</a>.

## Causal Machine Learning: Heterogeneous Treatment Effect Estimation

Much of the early work in [[machine_learning_and_causal_inference_methodologies | causal machine learning]] focused on Heterogeneous Treatment Effect (HTE) estimation, specifically Conditional Average Treatment Effect (CATE) estimators <a class="yt-timestamp" data-t="09:56:06">[09:56:06]</a>.

### Strategies for Treatment Effect Estimation
A treatment effect is the expected difference in an individual's outcome given treatment versus no treatment <a class="yt-timestamp" data-t="10:43:08">[10:43:08]</a>. Two main strategies exist for its estimation:
1.  **Indirect Estimation**: Separately estimate the expected outcome under treatment and no treatment, then take the difference <a class="yt-timestamp" data-t="10:54:19">[10:54:19]</a>.
2.  **Direct Targeting**: Directly estimate the treatment effect without separately estimating the potential outcomes <a class="yt-timestamp" data-t="11:07:05">[11:07:05]</a>.

The choice of strategy often depends on whether learning the treatment effect directly is structurally simpler than learning the two potential outcome functions separately <a class="yt-timestamp" data-t="11:21:40">[11:21:40]</a>. Direct targeting is more efficient when the treatment effect function is simpler <a class="yt-timestamp" data-t="11:37:37">[11:37:37]</a>.

### Shaping Perspectives
A background in econometrics and policy economics, particularly in treatment effect estimation, significantly shapes the approach to [[causal_ai_and_machine_learning_intersection | machine learning]] <a class="yt-timestamp" data-t="12:26:07">[12:26:07]</a>. This includes a strong emphasis on understanding the necessary assumptions for methods to work and the scenarios under which they perform well <a class="yt-timestamp" data-t="13:10:48">[13:10:48]</a>. This rigor is crucial in safety-critical applications like policy-making or medical decisions, where accurate estimation is paramount <a class="yt-timestamp" data-t="13:21:05">[13:21:05]</a>. This desire for statistical intuition and understanding *when* and *why* things work extends to non-causal machine learning research as well <a class="yt-timestamp" data-t="14:14:48">[14:14:48]</a>.

## Challenges in Causal Machine Learning with CATE Models

### Technical Challenges
In CATE estimation, two primary technical challenges arise <a class="yt-timestamp" data-t="16:47:35">[16:47:35]</a>:
*   **Covariate Shift**: When the treated group looks significantly different from the untreated group, models can suffer from the effects of covariate shift <a class="yt-timestamp" data-t="17:00:27">[17:00:27]</a>.
*   **Unobserved Labels**: The true label of interest, the individual treatment effect (difference between potential outcomes), is fundamentally unobservable in reality <a class="yt-timestamp" data-t="17:27:06">[17:27:06]</a>. This makes learning particularly challenging <a class="yt-timestamp" data-t="17:49:15">[17:49:15]</a>.

### The Evaluation Problem
The biggest practical hurdle for deploying these models, especially in safety-critical applications like [[application_of_causal_machine_learning_in_medicine | medicine]], is the evaluation problem <a class="yt-timestamp" data-t="18:06:17">[18:06:17]</a>. Since the true potential outcomes are unobserved and necessary assumptions are untestable, it's very difficult to validate whether an HTE system works correctly in practice <a class="yt-timestamp" data-t="18:17:51">[18:17:51]</a>.

### Issues with Benchmarking and Synthetic Data
Similar to issues in causal discovery, benchmarking practices in HTE estimation often rely on simulated datasets <a class="yt-timestamp" data-t="19:50:52">[19:50:52]</a>. However, the problem characteristics embedded in these simulated datasets may disproportionately favor specific types of estimators <a class="yt-timestamp" data-t="20:19:15">[20:19:15]</a>. These characteristics are not always rooted in realistic data-generating processes, leading to an inaccurate reflection of real-world performance <a class="yt-timestamp" data-t="20:30:46">[20:30:46]</a>. There is a need for more authoritative statements on likely real-world data-generating processes to create better benchmarking testbeds <a class="yt-timestamp" data-t="21:00:44">[21:00:44]</a>.

### Model Evaluation and Testable Implications
While some parts of treatment effect estimators can be evaluated (e.g., potential outcome predictions against factual observations), there's a caveat <a class="yt-timestamp" data-t="22:30:17">[22:30:17]</a>. Models that predict outcomes best are not necessarily the best at predicting treatment effects <a class="yt-timestamp" data-t="23:09:47">[23:09:47]</a>. This is because errors in potential outcome predictions might cancel out or add up when the difference (the treatment effect) is calculated, which doesn't have clear testable implications <a class="yt-timestamp" data-t="23:37:05">[23:37:05]</a>. Nevertheless, checking testable implications as a first step is good practice to ensure predictions are at least in the "right ballpark" <a class="yt-timestamp" data-t="24:00:23">[24:00:23]</a>.

## Frameworks in Causality: Potential Outcomes vs. Causal Graphs

Both the Potential Outcomes framework and Causal Graphs (DAGs) are valuable tools in [[causal_reasoning_in_ai | causal reasoning]].
*   **Causal Graphs (DAGs)** are incredibly useful for:
    *   Representing assumptions clearly <a class="yt-timestamp" data-t="25:28:16">[25:28:16]</a>.
    *   Communicating with non-expert stakeholders, such as doctors, about confounders <a class="yt-timestamp" data-t="25:35:10">[25:35:10]</a>.
    *   Depicting problems with complex structures, like biases from causal structures beyond a simple three-variable setup, or problems involving time <a class="yt-timestamp" data-t="25:56:07">[25:56:07]</a>. For instance, in analyzing cancer survival with competing risks, a causal graph is essential for understanding different paths of effect <a class="yt-timestamp" data-t="26:28:13">[26:28:13]</a>.
*   **Potential Outcomes Framework** is preferred for reasoning about the estimators themselves, as it naturally depicts a treatment effect as the difference between two potential outcomes <a class="yt-timestamp" data-t="26:59:17">[26:59:17]</a>.

These two frameworks are not in contrast; they are equivalent, and choosing between them often comes down to personal preference for writing and thinking <a class="yt-timestamp" data-t="27:31:01">[27:31:01]</a>.

## Broader Context and the Future of Causal Machine Learning

The application of statistical skills transcends specific domains, with many parallels between fields like economics and medicine <a class="yt-timestamp" data-t="31:13:00">[31:13:00]</a>. While assumptions may differ, requiring domain experts, the underlying statistical problems remain similar <a class="yt-timestamp" data-t="31:16:03">[31:16:03]</a>.

[[advances_in_causal_machine_learning_research | Causality]] is increasingly gaining traction in mainstream machine learning <a class="yt-timestamp" data-t="32:01:06">[32:01:06]</a>. This is because concepts like generalization and building autonomous systems that take actions inherently involve causal thinking (an action is an intervention) <a class="yt-timestamp" data-t="32:19:14">[32:19:14]</a>.

The biggest challenge in [[causal_reasoning_in_artificial_intelligence | causality]] is developing better ways to evaluate if models work in practice <a class="yt-timestamp" data-t="33:02:12">[33:02:12]</a>. This requires validating untestable assumptions, which ideally involves mapping domain expertise to a system that can confirm the likelihood of assumptions holding <a class="yt-timestamp" data-t="33:30:19">[33:30:19]</a>.

### Sensitivity Analysis
Sensitivity analyses are a promising tool to quantify how wrong estimates might be by perturbing assumptions <a class="yt-timestamp" data-t="34:49:03">[34:49:03]</a>. This allows for placing bounds on treatment effects, for example, by modeling the impact of unobserved confounding <a class="yt-timestamp" data-t="35:06:05">[35:06:05]</a>. Recent work integrates modern machine learning ideas, such as conformal prediction intervals, to bound the effects of unobserved confounding <a class="yt-timestamp" data-t="35:31:39">[35:31:39]</a>.

### Missing Data as a Unifying Perspective
Many complexities in real-world problems, such as survival analysis, competing risks, censoring, and informative sampling, ultimately boil down to a missingness problem <a class="yt-timestamp" data-t="50:50:56">[50:50:56]</a>. The more layers of complexity are added, the more data becomes unobserved, leading to a sparsity problem compounded by covariate shifts induced by these missingness mechanisms <a class="yt-timestamp" data-t="51:03:00">[51:03:00]</a>. This unifying perspective aligns with the work of statisticians like Donald Rubin, who also explored both causality and missingness as interconnected problems <a class="yt-timestamp" data-t="52:09:59">[52:09:59]</a>.

### Contrasting ML Publication Culture
A notable contrast exists between the culture of machine learning publishing and the "why" approach of statistics/econometrics <a class="yt-timestamp" data-t="54:23:42">[54:23:42]</a>. Machine learning often prioritizes achieving state-of-the-art results and demonstrating methodological novelty (e.g., "my attention horse is running faster") <a class="yt-timestamp" data-t="54:43:08">[54:43:08]</a>. In contrast, fields like statistics focus more on understanding the problem structure and the necessary solutions, which can lead to novel insights into existing methods rather than just new architectures <a class="yt-timestamp" data-t="55:09:47">[55:09:47]</a>. This difference often leads to challenges in getting "understanding"-focused papers published in ML venues due to perceived lack of methodological novelty <a class="yt-timestamp" data-t="55:34:03">[55:34:03]</a>.

This focus on novelty over understanding can be problematic, as it leads to an accumulation of methods with the same failure modes because the underlying problem aspects are not fully analyzed <a class="yt-timestamp" data-t="56:11:13">[56:11:13]</a>. There's a need to ask "what are we actually doing here?" <a class="yt-timestamp" data-t="56:22:45">[56:26:00]</a>. The future of machine learning is hopefully at least partially "causality-inspired," leading to more robust and stable models that leverage ideas like the invariance of causal mechanisms <a class="yt-timestamp" data-t="57:37:34">[57:37:34]</a>.

Ultimately, the message to the causal community, particularly the "Causal Python Community," is to "keep asking why" <a class="yt-timestamp" data-t="59:17:39">[59:17:39]</a>. This innate curiosity to distill causation from mere correlation is a strength that sets [[causal_reasoning_in_artificial_intelligence | causal machine learning]] apart <a class="yt-timestamp" data-t="59:58:39">[59:58:39]</a>.