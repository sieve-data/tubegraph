---
title: Causal AI in medicine
videoId: w9Dy4xqn7mA
---

From: [[causalpython]] <br/> 

Alicia, a researcher at the University of Cambridge, focuses on understanding "why" machine learning methods work, particularly in the domain of [[causal_ai_and_machine_learning | causality and machine learning]] <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. Her work often involves analyzing existing methods and stress-testing them to identify their strengths and failure points <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.

## The "Why" in Causal Machine Learning
Her research is driven by a curiosity to understand *why* machine learning works, rather than just demonstrating *that* it works <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. This approach is rooted in her background in statistics and econometrics, which emphasizes understanding assumptions and scenarios where methods perform well <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

Her paper, "A U-turn on Double Descent," although not focused on [[Causal AI and its connection to machine learning | causality]], exemplifies this "why" question <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. It investigates the "double descent" phenomenon in contemporary machine learning, where model loss decreases, then increases, and then decreases again as model complexity grows <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. The paper revealed that this seemingly counterintuitive behavior arises from presenting a 3D plot with two complexity axes as a 2D plot, indicating a mechanism shift rather than a true anomaly <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. This work highlights the importance of understanding underlying mechanisms in machine learning <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.

## Application in Safety-Critical Fields
Alicia's introduction to machine learning was through treatment effect estimation, stemming from her policy economics background <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>. Her research on conditional average treatment effect (CATE) estimators and heterogeneous treatment effect estimators specifically explores the underlying mechanisms influencing their performance <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>.

She emphasizes that in fields like policy economics, biostatistics, and medicine, where decisions based on estimations can have significant safety-critical implications, it is crucial to be certain that estimations are correct <a class="yt-timestamp" data-t="13:20:00">[13:20:00]</a>. For building reliable automated decision systems, some knowledge of how a system behaves under intervention—a core aspect of [[causal_ai_and_machine_learning | causality]]—is necessary <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.

## Challenges in Causal Medical AI
Working with CATE models, especially in health, presents unique challenges:
*   **Covariate Shift** <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>: If the treated group looks significantly different from the untreated group, models can suffer from the effects of covariate shift <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>.
*   **Unobserved Labels** <a class="yt-timestamp" data-t="17:27:00">[17:27:00]</a>: The true outcome of interest, the difference between potential outcomes (e.g., if a patient were treated vs. not treated), can never be fully observed for a single individual <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>. This fundamental missing data problem makes learning challenging <a class="yt-timestamp" data-t="17:47:00">[17:47:47]</a>.
*   **Evaluation Problem** <a class="yt-timestamp" data-t="18:06:00">[18:06:00]</a>: It is difficult to validate whether a heterogeneous treatment effect system works in practice because the true counterfactual outcomes are unobserved, and the necessary assumptions are untestable <a class="yt-timestamp" data-t="18:17:00">[18:17:00]</a>.

### Benchmarking Issues
A specific challenge is related to benchmarking practices in treatment effect estimation. Because of the missing data problem, researchers often rely on simulated datasets for evaluation <a class="yt-timestamp" data-t="20:03:00">[20:03:00]</a>. However, these simulated datasets often encode problem characteristics that unfairly favor specific estimators, and these characteristics may not be rooted in realistic data-generating processes <a class="yt-timestamp" data-t="20:19:00">[20:19:00]</a>. This highlights a need for more authoritative statements on likely real-world data-generating processes to improve benchmarking <a class="yt-timestamp" data-t="21:01:00">[21:01:00]</a>.

## Evaluating and Validating Causal Models
While untestable assumptions are inherent to causal models, some aspects can be evaluated. If a model provides potential outcome predictions, these can be checked against factual observations as a first step <a class="yt-timestamp" data-t="22:39:00">[22:39:00]</a>. However, models that are best at predicting outcomes are not necessarily best at predicting treatment effects, especially in low-data regimes <a class="yt-timestamp" data-t="23:09:00">[23:09:09]</a>. Errors in potential outcome predictions might cancel out or be magnified when calculating the treatment effect <a class="yt-timestamp" data-t="24:26:00">[24:26:00]</a>.

### Sensitivity Analysis
Sensitivity analysis is seen as a useful tool for quantifying uncertainty and exploring how estimates might change if underlying assumptions were slightly different <a class="yt-timestamp" data-t="35:03:00">[35:03:00]</a>. Modern [[causal_ai_and_machine_learning | machine learning]] ideas, such as conformal prediction intervals, are being used to bound the effects of unobserved confounding <a class="yt-timestamp" data-t="35:31:00">[35:31:00]</a>.

## Unifying Perspective: Missing Data Problems
Many additional complexities in real-world problems, such as:
*   Survival analysis <a class="yt-timestamp" data-t="48:10:00">[48:10:00]</a>
*   Competing risks <a class="yt-timestamp" data-t="48:10:00">[48:10:00]</a>
*   Censoring (e.g., in survival data) <a class="yt-timestamp" data-t="48:14:00">[48:14:00]</a>
*   Missingness (e.g., unrecorded data) <a class="yt-timestamp" data-t="48:27:00">[48:27:00]</a>
*   Informative sampling <a class="yt-timestamp" data-t="50:15:00">[50:15:00]</a>

can ultimately be viewed as "missingness problems" <a class="yt-timestamp" data-t="49:57:00">[49:57:00]</a>. As more layers of complexity are added, the data becomes sparser <a class="yt-timestamp" data-t="51:09:00">[51:09:00]</a>. Viewing these challenges through a unified missing data framework, similar to the work of Donald Rubin, could be highly beneficial <a class="yt-timestamp" data-t="52:06:00">[52:06:00]</a>.

## Future Directions and Broader Context
[[Trends in causal AI | Causality]] is increasingly gaining traction in mainstream machine learning, especially as researchers address questions of generalization and building systems that take actions (interventions) <a class="yt-timestamp" data-t="32:07:00">[32:07:00]</a>.

A major challenge for the field of [[causal_ai_and_machine_learning | causality]] is developing better ways to evaluate if models work in practice, especially validating untestable assumptions by mapping domain expertise into validation mechanisms <a class="yt-timestamp" data-t="33:07:00">[33:07:00]</a>.

Alicia advocates for focusing on understanding the structure of a problem rather than just achieving state-of-the-art empirical results or showing "methodological novelty" <a class="yt-timestamp" data-t="55:06:00">[55:06:00]</a>. This aligns with the "troubling [[Trends in causal AI | trends in machine learning scholarship]]" that highlight a lack of focus on understanding the *sources of gain* in new architectures <a class="yt-timestamp" data-t="56:31:00">[56:31:00]</a>.

The future of [[Causal AI applications in various industries | machine learning]], especially in health, is likely to be "causality-inspired," incorporating ideas like invariance of causal mechanisms for robustness and transfer learning <a class="yt-timestamp" data-t="57:48:00">[57:48:00]</a>.