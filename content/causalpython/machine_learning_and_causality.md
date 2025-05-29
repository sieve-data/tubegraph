---
title: Machine learning and causality
videoId: w9Dy4xqn7mA
---

From: [[causalpython]] <br/> 

The Causal Bandits podcast focuses on [[causality_and_machine_learning | causality and machine learning]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Dr. Alicia Curth, a researcher at the University of Cambridge, emphasizes the importance of understanding *why* [[causal_ai_and_machine_learning | machine learning]] methods work, rather than just showing that they do <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. She advocates for moving beyond simply building more methods to critically examining existing ones, testing them from multiple perspectives, and gathering knowledge to advance the field <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Alicia Curth's Research Philosophy

Alicia Curth's research is driven by a curiosity about "why machine learning works" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. While the literature on treatment effect estimation in [[causality_and_machine_learning | machine learning]] has excelled at building solutions and demonstrating functionality, it often lacks focus on the underlying reasons or conditions for success <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Her background in statistics and econometrics has instilled a focus on understanding *why* and *when* specific methods operate effectively <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

She initially encountered [[causality_and_machine_learning | machine learning]] methods as tools to infer treatment effects from a policy economics background, which is the reverse of the usual path of learning ML then applying it to [[causality_and_machine_learning | causality]] <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This perspective influenced her to prioritize understanding assumptions and scenarios where methods work, especially in safety-critical applications like policy-making or biostatistics <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. Curth expresses concern about the modern [[causal_ai_and_machine_learning | machine learning]] trend that dismisses statistical intuition, preferring to uphold established statistical principles and understand the failure modes of [[causal_ai_and_machine_learning | machine learning]] methods <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

## Double Descent Phenomenon

Curth's paper, "A U-turn on Double Descent," investigates the counterintuitive phenomenon of double descent in [[causal_ai_and_machine_learning | machine learning]] <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. This phenomenon shows that model performance, instead of following the traditional U-shaped trade-off with increasing model complexity, experiences a second decline in error as the number of parameters exceeds the number of training examples <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

Her research aimed to uncover the root cause of this observation, finding that it arises from a "mechanism shift" in how parameters are increased, rather than the interpolation threshold itself being the cause <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. The team found that double descent is often a misrepresentation of a 3D plot with two orthogonal complexity axes presented as a 2D curve <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. The "peak" in the double descent curve appears because one complexity axis has a limited number of parameters (e.g., leaves in a tree, limited by the number of examples), forcing a switch to a different parameter-adding mechanism (e.g., adding more trees) <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

This work highlights a common issue in contemporary [[causal_ai_and_machine_learning | machine learning]]: models often perform well empirically, but the underlying reasons for their success are not well understood <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Conditional Average Treatment Effect (CATE) Estimation

In her work on conditional average treatment effect (CATE) estimators, Curth's main insight was that the best strategy for estimating treatment effects depends on the assumed underlying problem structure <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. Treatment effects can be estimated in two ways:
1.  By estimating expected outcomes under treatment and control separately, then taking the difference <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
2.  By directly estimating the treatment effect <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

Direct targeting is often superior when learning the treatment effect itself is simpler than learning the potential outcomes separately <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

### Challenges in CATE Estimation

Two technical challenges make CATE estimation unique compared to standard prediction problems:
1.  **Covariate Shift:** Treatment assignment biases can lead to a covariate shift between treated and control groups, making it difficult to fit models <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
2.  **Missing Label:** The true label of interest, the difference between potential outcomes for an individual (e.g., treated vs. untreated), is never fully observed for any single individual <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

Beyond technical challenges, the biggest hurdle for deploying CATE models in practice is the **evaluation problem** <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. Since the true potential outcomes are unobservable in practice and key assumptions are untestable, validating whether a heterogeneous treatment effect system works effectively is challenging <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.

### Benchmarking and Problem Characteristics

Similar to findings in [[Causality and Causal Models | causal discovery]], Curth's work on CATE estimation highlighted issues with current benchmarking practices <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. Because of the missing data problem, researchers often rely on simulated datasets to evaluate models <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. However, the problem characteristics embedded in these simulated datasets frequently favor specific types of estimators that may not reflect real-world data generating processes <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. This underscores a need for more authoritative statements on likely real-world data generating processes to create better benchmarking test beds <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

### Model Evaluation and Testable Implications

While it is possible to evaluate parts of treatment effect estimators (e.g., checking potential outcome predictions against factual observations), models that predict outcomes best are not necessarily the ones that predict treatment effects best <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. This is because errors in potential outcome predictions can either cancel out or add up when calculating the difference for the treatment effect, making evaluation complex <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. Nonetheless, examining testable implications remains a crucial first step to ensure predictions are within a reasonable range <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.

## Integration of Causal Frameworks

Curth finds both the potential outcomes framework and [[structural_causal_models_and_machine_learning | causal graphs (DAGs)]] highly useful <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>. DAGs are particularly effective for:
*   Representing assumptions <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.
*   Communicating with non-experts, such as doctors or policymakers <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>.
*   Depicting complex problem structures and biases, especially with multiple dimensions or time-dependent data <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>. For example, in modeling cancer survival with competing risks like cardiovascular disease, DAGs help in understanding the different causal paths <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.

The potential outcomes framework is preferred for reasoning about the estimators themselves, as it conceptualizes a treatment effect as the difference between two potential outcomes <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. Curth doesn't see these two frameworks as contrasting, noting existing papers that demonstrate their equivalence <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>.

## Challenges and Future of [[causality_in_artificial_intelligence | Causality in Artificial Intelligence]]

A major challenge in [[causality_in_artificial_intelligence | causal models]] is dealing with untestable assumptions, especially in complex, open real-world systems where validating the causal graph's correspondence to reality is difficult <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.

### The Need for Reliability in Automated Decision Systems

Curth believes that some form of knowledge about how a system behaves under intervention is necessary for building reliable automated decision systems <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. If a perfect [[causality_and_causal_models | Structural Causal Model (SCM)]] of the world existed, it would be sufficient for making decisions on any intervention <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

### Sensitivity Analysis and Missingness

Sensitivity analyses are vital tools for perturbing assumptions and understanding how varying assumptions might impact estimates <a class="yt-timestamp" data-t="00:47:19">[00:47:19]</a>. This includes modeling the effects of unobserved confounding to determine potential bounds on treatment effects <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>. Recent work uses methods like conformal prediction intervals to bound the effects of unobserved confounding <a class="yt-timestamp" data-t="00:35:31">[00:35:31]</a>.

Many additional complexities in real-world problems, such as survival analysis, competing risks, censoring, and informative sampling, ultimately reduce to a "missingness problem" <a class="yt-timestamp" data-t="00:50:43">[00:50:43]</a>. As more layers of complexity are added, less of the potential outcomes are observed, leading to sparsity and covariate shifts induced by various missingness mechanisms <a class="yt-timestamp" data-t="00:51:04">[00:51:04]</a>. Treating these challenges jointly as a unified missing data problem, in the spirit of Donald Rubin's work, could be a valuable direction <a class="yt-timestamp" data-t="00:51:57">[00:51:57]</a>.

### Machine Learning Culture vs. Causal Inference

Curth observes a contrast between the cultures of [[causal_ai_and_machine_learning | machine learning]] and statistics/econometrics <a class="yt-timestamp" data-t="00:54:27">[00:54:27]</a>. [[causal_ai_and_machine_learning | Machine learning]] research often focuses on achieving "state-of-the-art" results and demonstrating methodological novelty (e.g., "my attention horse is running faster") <a class="yt-timestamp" data-t="00:54:47">[00:54:47]</a>. In contrast, statistics and econometrics emphasize understanding the problem structure and the types of solutions needed <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>.

Curth finds it challenging to publish research focused on understanding existing methods and problem insights within the [[causal_ai_and_machine_learning | machine learning]] community, which often prioritizes novelty in architecture or methods <a class="yt-timestamp" data-t="00:55:27">[00:55:27]</a>. She argues against a proliferation of new methods that share the same failure modes and advocates for stepping back to examine what is actually being done <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a>. She cites "Troubling Trends in Machine Learning Scholarship" as a paper that addresses issues like showing improvements without identifying the sources of gain <a class="yt-timestamp" data-t="00:56:31">[00:56:31]</a>.

### The Future of [[Causality and Machine Learning | Causal Machine Learning]]

[[causality_and_machine_learning | Causality]] is gaining traction in mainstream [[causality_and_machine_learning | machine learning]], as researchers realize that concepts like generalization and building systems that take actions (interventions) involve causal thinking <a class="yt-timestamp" data-t="00:32:11">[00:32:11]</a>. There is significant potential to use causal ideas, such as the invariance of causal mechanisms, to build more robust and stable models <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>.

For Curth, the biggest challenge to be solved in [[causality_and_machine_learning | causality]] is developing better ways to evaluate if things work in practice, especially the validation of untestable assumptions by domain experts <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>. The ultimate goal is to have a mechanism that can validate assumptions, ensuring the reliability of [[causality_and_machine_learning | causal models]] in real-world applications <a class="yt-timestamp" data-t="00:33:39">[00:33:39]</a>.

## Recommended Readings

Alicia Curth recommends the following books:
*   *The Book of Why* by Judea Pearl: A good "gateway drug" to [[causality_and_machine_learning | causality]] for its philosophical depth, including counterfactuals, and its accessible popular science approach <a class="yt-timestamp" data-t="00:43:06">[00:43:06]</a>.
*   *Targeted Learning* by Mark van der Laan and Sherri Rose: Revolutionary in its approach to thinking about target parameters and causal quantities <a class="yt-timestamp" data-t="00:41:49">[00:41:49]</a>.
*   *The Elements of Statistical Learning* by Hastie, Tibshirani, and Friedman: A highly intuitive and well-structured textbook on statistical learning <a class="yt-timestamp" data-t="00:42:15">[00:42:15]</a>.

Her advice for those starting in [[causality_and_machine_learning | causality]] is to focus on getting the intuition right first, suggesting *The Book of Why* as a good starting point <a class="yt-timestamp" data-t="00:43:01">[00:43:01]</a>.