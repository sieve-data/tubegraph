---
title: Applications and limitations of statistical models in clinical trials
videoId: nT_yCwXSz54
---

From: [[causalpython]] <br/> 

This article explores the applications and limitations of statistical models in clinical trials, drawing insights from Dr. Stephen Senn, author of "Statistical Issues in Drug Development" and "Dicing with Death" <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Dr. Senn emphasizes the practical realities and historical context of experimental design, particularly in medicine.

## The Role of Randomization in Clinical Trials

According to Dr. Senn, [[myths_and_controversies_of_randomization_in_clinical_trials | randomization]] is "not a controversial idea" but is "still controversial among statisticians and scientists even today" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This controversy stems from a misunderstanding of its goal <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

> [!INFO] Goal of Randomization
> R. A. Fisher, who proposed [[myths_and_controversies_of_randomization_in_clinical_trials | randomization]], understood that "perfect estimation was impossible" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Instead, the aim of [[myths_and_controversies_of_randomization_in_clinical_trials | randomization]] is to "estimate how imperfect any estimate was" <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

Critics often misunderstand this, assuming that [[myths_and_controversies_of_randomization_in_clinical_trials | randomization]] should perfectly balance all factors that could affect an outcome <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. However, it's known and accepted that groups will not be perfectly balanced <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The standard analysis accounts for this imbalance by contributing to the estimate of error <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. If factors *were* perfectly balanced, the standard analysis would be incorrect <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

This concept is likened to an engineer building a bridge with "Expansion Joints" to account for thermal expansion, rather than expecting no expansion at all <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Types of Clinical Trials

Dr. Senn defines two common types of clinical trials:

*   **Parallel Group Trial**: The most common type, where patients are randomized to receive either a new treatment or a standard treatment, with each patient receiving only one <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. An example is a stroke prevention trial where half receive a new treatment and half get standard care <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Crossover Trial**: A design where each patient serves as their own control, receiving both treatments at different times <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. This is suitable for "chronic diseases where the treatments are essentially reversible" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. For example, comparing two beta agonists for asthma by treating patients with one, then the other, randomizing the order <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. Crossover trials lead to "much narrower confidence intervals" because they inherently balance for many patient-specific factors like "20,000 genes [and] all life history to date" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Five Questions Clinical Trials Can Answer

Dr. Senn outlines five levels of questions that clinical trials can attempt to answer, noting that they become progressively more difficult <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>:

1.  **Was there a difference between treatments in the trial?** (Was there a treatment effect?) <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>
2.  **What was the average effect for the patients actually treated?** (What difference did it make to them?) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>
3.  **Was the effect the same for all patients in the trial?** <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>
4.  **Is the effect different for particular subgroups?** (e.g., men vs. women, elderly vs. young) <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>
5.  **What will it be like in future patients not in the trial?** (Can we say anything about patients outside the trial?) <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>

Statisticians are often "stuck in question one and question two" <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Answering question three is occasional, and meaningful statements about subgroups (question four) are rare due to insufficient statistical power <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

Question five, concerning future patients, introduces an "uncertainty which is not captured in the formal statistical analysis" <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The future is uncertain; for instance, the streptomycin trial for tuberculosis was highly effective when reported, but now it's less so due to bacterial mutation and resistance <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Predicting the future requires understanding mechanisms and acknowledging that environmental factors change, not just genetics <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

## Practical Considerations and Challenges in Trial Design

Clinical trials operate under "limits of what we think is possible in terms of resources both financially and ethically" <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. Statisticians must often make "leaps of faith" regarding questions three, four, and five, and proceed as if subgroup differences don't matter, because pursuing all questions would compete with developing new, potentially better, molecules <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

This problem is not unique to clinical trials; it extends to other fields like the automobile industry, where "accelerated life testing" is used to predict component longevity without waiting for 10 years for a warranty <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. This highlights that experimentation often cannot be performed on the exact material or conditions desired <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

Decisions in clinical trials carry immense responsibility due to their "profound impact on people's lives" <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>. Data Safety Monitoring Boards face tough choices, as effective drugs often present toxicities before efficacy is proven <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>. Statisticians aid by comparing numbers and averages, while medical colleagues focus on individual patient stories <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>.

## History and Evolution of Experimental Design

The formal theory of [[role_of_mathematics_and_statistics_in_experimental_design | experimental design]] has a long history, dating back over 100 years <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.

*   **R. A. Fisher**: Began working on complex agricultural experiments at Rothamsted in 1919 <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. His key insight was ensuring "the contribution to your estimative error reflected the way in which this would also contribute to the differences between the treatments" to achieve valid standard errors <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. This led to incomplete block designs and fractional factorial designs <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>. Fisher's mathematical ability is often underestimated because he used an "old-fashioned" form of mathematics, relying on geometrical intuition over algebraic proofs <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.
*   **Industrial Influence**: The theory of [[role_of_mathematics_and_statistics_in_experimental_design | experimental design]] saw a "large impetus of development in industry" starting in the 1940s <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
*   **John Nelder**: A key milestone was Nelder's 1965 development of a "front-end way of thinking for linear models" that dictated how to analyze experiments for correct standard errors based on blocking, variation, and treatment structure <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.

There is a historical "collaboration...between an agricultural scientist and an astronomer" in applying standard errors to agricultural experiments <a class="yt-timestamp" data-t="00:57:18">[00:57:18]</a>, demonstrating early interdisciplinary applications of statistical methods. This highlights the broad applicability of [[causal_modeling_in_healthcare_and_astronomy | causal modeling in healthcare and astronomy]].

## Role of Covariates in Models

Using covariates can significantly improve the precision of trial results:

*   **Linear Models (e.g., Normal Linear Model)**:
    *   **Mean Square Error Reduction**: Predictive covariates reduce the mean square error, leading to narrower confidence intervals and greater power <a class="yt-timestamp" data-t="00:45:21">[00:45:21]</a>.
    *   **Variance Inflation (Minor)**: Non-orthogonal (imbalanced) covariates cause slight variance inflation, typically equivalent to losing "about one patient per covariate" <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>. This is negligible in large trials but significant in small ones <a class="yt-timestamp" data-t="00:45:57">[00:45:57]</a>.
    *   **Degrees of Freedom Loss**: Each covariate fitted loses one degree of freedom, affecting the precision of the estimated variance <a class="yt-timestamp" data-t="00:46:32">[00:46:32]</a>.

*   **Non-Linear Models (e.g., Logistic Regression)**:
    *   **Model Misspecification**: Missing predictive covariates can lead to model misspecification, attenuating the signal directly rather than affecting variance in the same way as linear models <a class="yt-timestamp" data-t="00:48:41">[00:48:41]</a>.
    *   **Non-Collapsibility**: Some models exhibit non-collapsibility, where an effect (e.g., odds ratio) may be consistent within subgroups but change when pooled <a class="yt-timestamp" data-t="00:50:20">[00:50:20]</a>. Dr. Senn views parameters as "resting stone[s] on the road to prediction" <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>, implying that predictive power is often more critical than parameter interpretability.

Despite the benefits, the ability to fit covariates is often "underuse[d]" in clinical trials <a class="yt-timestamp" data-t="00:48:08">[00:48:08]</a>. Simple modeling steps that incorporate covariates and avoid dichotomizing continuous data (which causes "huge loss in...power") are resisted, even though they use "theory which is 100 years old" <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>.

## Optimizing Experimentation and Data Fusion

Dr. Senn acknowledges that there are "many deep wonderful and complex theories of optimal [[role_of_mathematics_and_statistics_in_experimental_design | experimental design]] that we medical statisticians ought to know better" <a class="yt-timestamp" data-t="00:52:31">[00:52:31]</a>. However, there's also a gap between theory and practice, as some optimal design proposals fail to consider practical constraints like patient recruitment rates or the impossibility of dose escalations reaching their final stages <a class="yt-timestamp" data-t="00:53:18">[00:53:18]</a>.

Regarding [[causal_data_fusion | causal data fusion]], combining observational and clinical trial data sets is "plausible that a way of getting putting observational data sets and clinical trial data sets together will yield more power" <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>. This area holds promise, but some proposals rely on unrealistic assumptions like random sampling that doesn't occur in practice <a class="yt-timestamp" data-t="00:56:29">[00:56:29]</a>.

## Communication and Teaching Statistics

Effective communication is crucial in statistics. Dr. Senn advises finding "simple stories that everybody can understand to communicate an idea" <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>, such as the analogy of a mother not knowing which child was the aggressor to explain why an overall treatment effect can be significant even if pairwise comparisons are not <a class="yt-timestamp" data-t="01:05:50">[01:05:50]</a>. He also advocates for simple graphical methods over algebra for teaching concepts like regression to the mean <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>.

For statisticians, understanding statistical solutions as "linear combination[s] of the cells" rather than just matrix algebra is key <a class="yt-timestamp" data-t="01:07:56">[01:07:56]</a>. Intuition must accompany mathematical understanding <a class="yt-timestamp" data-t="01:10:20">[01:10:20]</a>.

## Personal Reflections and Advice

Dr. Senn's career has spanned both academia and industry, each offering different learning experiences <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>. Academia provides broad but not necessarily deep knowledge <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>, while industry offers learning by "doing things and working on projects" where success or failure matters <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>. Experience in the Health Service taught him the importance of being "very careful about data that are given to you" <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>, even official statistics <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>.

His most proud professional achievement was establishing a standard approach to designing and analyzing trials in asthma during his time at Ciba-Geigy (now Novartis), particularly by avoiding data dichotomization and using covariates effectively <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.

For those starting in advanced fields like statistics or [[machine_learning_and_treatment_effect_estimation | machine learning]], Dr. Senn advises finding "concrete problems to work on" to gain practical experience <a class="yt-timestamp" data-t="01:12:25">[01:12:25]</a>, while also "look[ing] wider" and borrowing ideas from other fields <a class="yt-timestamp" data-t="01:12:53">[01:12:53]</a>. He highlights the "n of 1 trials" for personalizing medicine, an idea borrowed from psychologists <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>.

He notes that the most impactful immediate improvement in clinical trials would be to efficiently analyze them using existing knowledge, specifically by:
1.  Avoiding data dichotomization <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>.
2.  Using covariate information <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>.
These "simple modeling steps" are often resisted due to being perceived as too complex, despite being based on century-old theory <a class="yt-timestamp" data-t="01:15:47">[01:15:47]</a>.

Dr. Senn also touches on the nature of probability and determinism, suggesting that in some cases, "we have no choice but nevertheless to think probabilistically about things" <a class="yt-timestamp" data-t="01:21:22">[01:21:22]</a>. He challenges the "ludic fallacy" where games are used as an analogy for real-world probabilities, arguing that real-world probabilities are less structured <a class="yt-timestamp" data-t="01:20:57">[01:20:57]</a>.

He acknowledges significant contributions from prominent figures in [[causal_inference_and_individual_treatment_effects | causal inference]] like Judea Pearl (whose "do-see distinction is very very important" <a class="yt-timestamp" data-t="00:59:17">[00:59:17]</a>) and Don Rubin, recognizing their importance in the "wider world of inference" <a class="yt-timestamp" data-t="00:59:45">[00:59:45]</a>. However, he emphasizes the need for [[challenges_in_evaluating_causal_models | causal inference]] researchers to understand the "limitations of applying their theories in practice" <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a>.