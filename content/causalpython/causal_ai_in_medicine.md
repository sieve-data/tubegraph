---
title: Causal AI in Medicine
videoId: w9Dy4xqn7mA
---

From: [[causalpython]] <br/> 

Alicia Curth, a researcher at the University of Cambridge, emphasizes the importance of understanding *why* machine learning methods work and when they fail, rather than merely observing *that* they work <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This approach stems from her background in econometrics and statistics, which heavily focuses on the assumptions and scenarios under which methods are effective <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. This critical perspective is particularly crucial in fields such as [[application_of_causal_machine_learning_in_medicine | medicine]] and policy economics, where decisions are often made in safety-critical environments <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

## Approach to Machine Learning and Causality

Curth began her journey in machine learning by seeking tools to infer treatment effects, reversing the usual path of applying general machine learning methods to specific causal problems <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Her initial exposure to machine learning was through a [[causal_ai_and_machine_learning_intersection | causal machine learning]] paper on causal trees <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. She advocates for looking at existing solutions from more perspectives and stress-testing them against different cases to move the field forward <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>, <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

Curth expresses a dislike for the modern machine learning tendency to view models as "magic bullets" that defy statistical intuition, stressing the value of understanding failure modes <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>, <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. She believes [[causal_reasoning_in_ai | causal thinking]] is increasingly relevant for [[causal_ai_and_its_application_in_different_sciences | generalization]] and building systems that take actions, as actions are interventions on the environment <a class="yt-timestamp" data-t="00:32:19">[00:32:19]</a>, <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>.

## Causal Models and Decision Systems in Health

In the context of health, particularly for building reliable automated decision systems, some form of knowledge about how a system behaves under intervention is necessary <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>, <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. This directly relates to [[causality_in_ai | causality]].

### Challenges in Kate Models

Curth identifies unique challenges in Conditional Average Treatment Effect (CATE) models compared to standard prediction problems:
*   **Covariate Shift**: Treatment assignment biases can lead to a covariate shift where the treated group looks very different from the untreated group <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
*   **Unobserved Labels**: The true label of interest—the individual treatment effect (difference between potential outcomes)—is never fully observed in reality <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>, <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. This makes learning challenging <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.

### Evaluation and Untestable Assumptions

The primary hurdle for deploying CATE models in practice is the evaluation problem <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. Since the true individual treatment effect is unobserved and identification assumptions are untestable, it's hard to validate whether a heterogeneous treatment effect system works well <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>, <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>, <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>.

While some parts of treatment effect estimators can be evaluated (e.g., potential outcome predictions against factual data), models that predict outcomes best are not necessarily the ones that predict treatment effects best <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. Errors in potential outcome predictions can either cancel out or add up when calculating the difference for the treatment effect, which is not directly testable <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>, <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.

### Benchmarking Practices

Curth's research, including the NeurIPS 2021 paper "Really Doing Great at Estimating Kate," critically examines benchmarking practices in treatment effect estimation <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>. Due to the missing data problem, researchers often rely on simulated datasets for benchmarking <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. However, these simulated datasets often encode problem characteristics that heavily favor specific types of estimators, and these characteristics may not be rooted in realistic data-generating processes <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>, <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. There is a need for more authoritative statements on likely real-world data-generating processes to improve benchmarking <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

### Sensitivity Analysis and Missing Data

Sensitivity analyses are crucial for perturbing assumptions and understanding the impact if they are not perfectly met <a class="yt-timestamp" data-t="00:47:04">[00:47:04]</a>. This includes using [[causal_ai_and_its_role_in_experiments | sensitivity models]] to bound the effects of unobserved confounding <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>.

Many complexities in real-world problems, such as survival analysis, competing risks, missingness, censoring, and informative sampling, ultimately reduce to a missingness problem <a class="yt-timestamp" data-t="00:50:43">[00:50:43]</a>, <a class="yt-timestamp" data-t="00:50:58">[00:50:58]</a>. The more layers of complexity added, the more unobserved information there is, leading to a sparsity problem <a class="yt-timestamp" data-t="00:51:04">[00:51:04]</a>. These missingness mechanisms can also induce covariate shifts <a class="yt-timestamp" data-t="00:51:28">[00:51:28]</a>. Curth suggests that there is value in tackling these missingness problems jointly, as they are fundamentally similar, albeit with slight differences in assumed causal structures or target parameters <a class="yt-timestamp" data-t="00:51:34">[00:51:34]</a>, <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>.

## Frameworks and Future Directions

Curth finds both [[causal_reasoning_in_ai | causal graphs (DAGs)]] and the potential outcomes framework highly useful <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>, <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. [[applications_of_causal_models_in_biology_and_ai | Causal graphs]] are excellent for representing and communicating assumptions, especially with non-technical stakeholders like doctors, and for depicting complex problem structures, such as those involving time or multiple biases <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>, <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. The potential outcomes framework is preferred for reasoning about the estimators themselves <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. She notes that the two frameworks are not in contrast and are equivalent <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>.

Curth highlights the impact of semi-parametric statistics, particularly from the "Targeted Learning" book, on her thinking, as it offers a more flexible way to reason about [[causal_ai_and_machine_learning_intersection | causal quantities]] as functionals of statistical models, detaching them from restrictive parametric linear models <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>, <a class="yt-timestamp" data-t="00:40:09">[00:40:09]</a>.

The future of machine learning and [[causal_ai_and_its_application_in_different_sciences | causal machine learning]] is seen as increasingly intertwined <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>. Curth sees great potential for [[advancements_in_causal_modeling_and_ai | causal ideas]] to improve autonomous systems and address questions of generalization and robustness <a class="yt-timestamp" data-t="00:32:19">[00:32:19]</a>, <a class="yt-timestamp" data-t="00:57:49">[00:57:49]</a>.

### Key Challenges for the Future

For Curth, the biggest challenge to solve in [[causality_in_ai | causality]] is developing better methods for evaluating whether models work in practice <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>. This requires ways to validate untestable assumptions, potentially by mapping domain expertise into mechanisms that can confirm if assumptions are likely to hold <a class="yt-timestamp" data-t="00:33:39">[00:33:39]</a>, <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>.
She criticizes the current machine learning research culture's focus on methodological novelty and "horse races" (showing one method beats another) rather than understanding the *sources of gain* or why a method performs better <a class="yt-timestamp" data-t="00:54:37">[00:54:37]</a>, <a class="yt-timestamp" data-t="00:55:50">[00:55:50]</a>, <a class="yt-timestamp" data-t="00:56:55">[00:56:55]</a>. She asserts that the field doesn't need "more and more and more methods" if they all share the same failure mode and don't address broader problem aspects <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a>. She concludes by encouraging the causal community to "keep asking why" <a class="yt-timestamp" data-t="00:59:17">[00:59:17]</a>.