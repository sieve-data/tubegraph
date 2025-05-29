---
title: Evaluating causal models in practice
videoId: w9Dy4xqn7mA
---

From: [[causalpython]] <br/> 

Evaluating [[causality_and_causal_models | causal models]] in real-world applications presents significant challenges, particularly when considering their deployment in critical systems like healthcare or policy-making <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. Unlike traditional predictive models, [[causality_and_causal_models | causal models]] aim to understand "why" something works or fails, which requires a deeper scrutiny of assumptions and underlying mechanisms <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Key Challenges in Practice

### Untestable Assumptions and Unobserved Labels

A primary hurdle in evaluating [[causality_and_causal_models | causal models]] is the presence of untestable assumptions <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>. For instance, in heterogeneous treatment effect (HTE) estimation, the true "label" of interest—the difference between potential outcomes for an individual (e.g., if they were treated versus not treated)—is inherently unobserved <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. This makes it much harder to validate whether an HTE system works correctly when deployed in practice <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. The problem is compounded by issues like covariate shift, where the group receiving treatment differs significantly from the control group <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

### Benchmarking and Simulated Data Issues

Benchmarking practices in [[causality_and_causal_models | causal machine learning]] often rely on simulated datasets to provide a ground truth for evaluation <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. However, this approach can be problematic. Research has shown that problem characteristics encoded in these simulated datasets can heavily favor specific types of estimators <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. These characteristics may not reflect realistic data-generating processes seen in the real world, leading to a lack of authoritative benchmarking testbeds <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. This phenomenon is similar to issues found in causal discovery literature, where simulation processes might introduce clues that models exploit but are absent in reality <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.

### The Missingness Problem as a Unifying Challenge

Many complexities in real-world [[causality_and_causal_models | causal problems]], such as survival analysis, competing risks, censoring, and informative sampling, can ultimately be framed as "missingness problems" <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>. The more layers of complexity added, the more unobserved data points there are, leading to sparsity issues and covariate shifts induced by these missingness mechanisms <a class="yt-timestamp" data-t="00:51:04">[00:51:04]</a>. Treating these diverse challenges jointly under a unified missing data framework, as historically explored by statisticians like Donald Rubin, could offer a powerful approach <a class="yt-timestamp" data-t="00:51:57">[00:51:57]</a>.

## Approaches to Evaluation

### Leveraging Testable Implications

While the ultimate causal effect may be unobserved, parts of [[causality_and_causal_models | causal models]] can be evaluated using "testable implications" <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. For instance, if a model outputs potential outcome predictions, these can be checked against factual observations as a first step to ensure they resemble the observed data <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>. However, models that are best at predicting outcomes are not necessarily best at predicting treatment effects <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. Errors in potential outcome predictions might cancel out or magnify when calculating the difference for the treatment effect, especially in low-data regimes <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.

### Sensitivity Analysis and Quantifying Uncertainty

To address untestable assumptions and provide more robust evaluations, sensitivity analyses can be employed <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>. This involves perturbing the assumptions being made and observing how estimates change if, for example, unobserved confounding was of a certain strength <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>. Recent work integrates modern machine learning ideas, such as conformal prediction intervals, to bound the effects of unobserved confounding <a class="yt-timestamp" data-t="00:35:31">[00:35:31]</a>. This moves beyond single point predictions to provide a set of plausible outcomes given certain assumptions <a class="yt-timestamp" data-t="00:47:37">[00:47:37]</a>.

## The Importance of "Why" and Understanding Failure Modes

A significant gap in current machine learning research, including [[causality_and_causal_models | causal machine learning]], is the overemphasis on methodological novelty and achieving state-of-the-art results, often at the expense of understanding *why* models work or fail <a class="yt-timestamp" data-t="00:54:45">[00:54:45]</a>. There is a need to shift focus from "horse races" where new methods simply aim to "beat the benchmark" to a more in-depth understanding of the problem structure and the sources of gain or failure <a class="yt-timestamp" data-t="00:54:37">[00:54:37]</a>. This means dissecting models to understand which components contribute to performance, rather than just showing that a new architecture with five changes works better <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>. Understanding failure modes is crucial for building reliable systems <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Future Outlook

The future of [[causality_and_causal_models | causal machine learning]] lies in moving towards more realistic and complex problems that go beyond simple, static data settings <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>. This includes incorporating additional complexities like time, multiple outcomes, various treatments, and informative missingness <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>. The field is gaining traction as researchers realize that [[causality_and_causal_models | causal thinking]] is essential for generalization to new settings and for building autonomous systems that take actions (interventions) in an environment <a class="yt-timestamp" data-t="00:32:19">[00:32:19]</a>. The biggest challenge that needs to be solved is developing better ways to evaluate that [[causality_and_causal_models | causal models]] work in practice, ideally by bridging domain expertise with assumption validation <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>.