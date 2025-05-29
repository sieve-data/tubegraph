---
title: History and influence of statisticians in clinical trials
videoId: nT_yCwXSz54
---

From: [[causalpython]] <br/> 

The history of experimental design and the influence of statisticians, particularly in [[clinical_trial_design_and_optimization | clinical trials]], is a long and complex one, spanning over a century of formal theory and practical application <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. Statisticians play a critical role in designing, analyzing, and interpreting trials, navigating both theoretical ideals and real-world constraints <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Early Development of Experimental Design

Formal theory of experimentation dates back at least 100 years <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. A key milestone was the arrival of R.A. Fisher at Rothamsted in 1919, where he began working on complex agricultural experiments <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. These experiments involved factors like fertility gradients in fields and correlation structures between soil plots, requiring sophisticated methods to compare treatments <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. Fisher recognized the need to ensure that the estimation of error accurately reflected contributions to treatment differences, leading to the development of valid standard errors <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.

This work led to the development of various experimental designs:
*   **Incomplete Block Designs:** Used when not all treatments could be compared in the same block <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>.
*   **Fractional Factorial Designs:** Employed when comparing many treatment combinations with limited experimental material, often by assuming higher-order interactions were negligible <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>.

This theoretical development gained significant impetus in [[industrial_applications_of_causal_inference | industry]] starting around the 1940s, with [[clinical_trial_design_and_optimization | clinical trials]] adopting these methods relatively later <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

A significant development was John Nelder's front-end machine in 1965, which provided a way of thinking for linear models to dictate how an experiment should be analyzed based on blocking, treatment structure, and the design matrix, ensuring correct standard errors <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.

## Randomization in Clinical Trials

Randomization is a core concept in [[clinical_trial_design_and_optimization | clinical trial design]] and is foundational to assessing treatment effects <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>. However, its understanding can be a source of controversy among statisticians and scientists <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Misunderstanding of Randomization
Critics often misunderstand randomization's purpose, believing its goal is "perfect estimation" or that it will perfectly balance groups <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>, <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. R.A. Fisher, who proposed randomization, recognized that perfect estimation was impossible <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Instead, randomization allows statisticians to estimate how imperfect any estimate is, and to account for the fact that factors influencing outcomes will not be perfectly balanced across groups <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

> "The standard analysis allows for the fact that they will not be perfectly balanced and it's failure to understand this which leads to endless tedious conversations in which people don't really know what's going on." <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>

This concept is likened to an engineer designing a bridge with expansion joints to account for thermal expansion, rather than expecting no expansion at all <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

### Types of Clinical Trials
Different [[clinical_trial_design_and_optimization | clinical trial designs]] have different implications for balance and precision:
*   **Parallel Group Trial:** The most common type, where patients are randomized to receive either a new treatment or a standard treatment. Each patient receives only one, making it relatively easy to implement <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. For example, in stroke prevention, half of the subjects receive a new treatment and half receive standard care <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. These trials typically have broader confidence intervals compared to crossover trials <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Crossover Trial:** In this design, each patient serves as their own control, receiving both treatments sequentially (e.g., Treatment A then B, or B then A) <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This design is suitable for chronic, reversible conditions like asthma, allowing for balancing of numerous individual factors (e.g., 20,000 genes, full life history), leading to much narrower confidence intervals <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Questions Answered by Randomized Trials

Randomized trials primarily aim to answer five key questions, which become progressively more difficult:
1.  **Was there a difference between treatments in the trial?** (Was there an effect of treatment?) <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>
2.  **What was the average effect for the patients that were actually treated?** (What difference did it make to them if they were given treatment B rather than treatment A?) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>
3.  **Was the effect the same for all the patients in the trial?** <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>
4.  **Is the effect different for particular subgroups?** (e.g., men vs. women, elderly vs. young) <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>
5.  **What will it be like in future patients not in the trial?** (Can we say anything about patients outside the trial?) <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>

Statisticians often focus on questions 1 and 2, with occasional ability to address question 3 and, less frequently, question 4 <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Question 5, predicting future outcomes, involves a degree of uncertainty not fully captured by formal statistical analysis, as the world and diseases (e.g., tuberculosis resistance to streptomycin) can change <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. This challenge is more about predicting how the world will change rather than a direct [[challenges_in_causal_inference_and_statistical_analysis | counterfactual analysis]] of what might have happened differently in the past <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

## Practical Challenges in Clinical Trials

Statisticians face significant practical, ethical, and financial constraints when designing [[clinical_trial_design_and_optimization | clinical trials]] <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

### Resource and Ethical Limitations
*   **Precise Answers are Hard:** It is incredibly difficult to produce precise answers about what happened on average to patients in a trial, partly due to the "missing counterfactual" in parallel group trials, or changing circumstances in crossover trials <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
*   **Subgroup Analysis Limitations:** Often, there isn't enough power or time to make meaningful statements about subgroups (Question 4), such as ensuring an equally precise statement for women in a lung cancer trial where males are predominant <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   **Ethical Dilemmas:** Statisticians on data safety monitoring boards face difficult decisions, especially in cancer trials where effective drugs often show toxicities before efficacy <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>. Decisions to continue or stop a trial carry profound impact on patients' lives <a class="yt-timestamp" data-t="00:34:41">[00:34:41]</a>.

### Data Quality and Covariates
A crucial lesson is to be very careful about data quality, even when collected for official purposes, as underlying stories and biases can exist (e.g., population figures recalibrated after a census) <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>.

Using covariates effectively is essential for efficiency:
*   **Benefits of Covariates:** In a normal linear model, fitting predictive covariates reduces mean square error, leading to narrower confidence intervals and greater power <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.
*   **Trade-offs:** Covariates can inflate variance if not perfectly balanced, equivalent to losing about one patient per covariate <a class="yt-timestamp" data-t="00:45:41">[00:45:41]</a>. They also lead to a loss of degrees of freedom <a class="yt-timestamp" data-t="00:46:34">[00:46:34]</a>.
*   **Practical Guidelines:** For large Phase III trials with hundreds of patients, fitting half a dozen to 15 covariates is generally not a problem. However, for very small trials (e.g., 12 patients), fitting too many covariates should be avoided <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.
*   **Non-linear Models:** In models like logistic regression, missing predictive covariates can lead to misspecification and attenuation of the signal itself <a class="yt-timestamp" data-t="00:48:41">[00:48:41]</a>.

### Communication and Bridging Gaps
There are "ghettos" within statistics and between statisticians and other fields <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>. [[Clinical trial design and optimization | Optimal experimental design theory]] can be highly abstract and beautiful, but its application requires understanding practical constraints and real-world conditions (e.g., patients not being treated simultaneously, recruitment challenges) <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>.

Statisticians can improve communication by:
*   **Using Simple Stories:** Employing relatable analogies to explain complex statistical concepts, such as why a global ANOVA might be significant while pairwise comparisons are not (the "children fighting" analogy) <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.
*   **Simple Graphical Methods:** Visualizing concepts like regression to the mean without relying on complex mathematics <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>.
*   **Understanding Underlying Structure:** Grasping that statistical solutions are often linear combinations of cells, which can be understood by finding the weights, rather than just relying on matrix algebra <a class="yt-timestamp" data-t="01:07:56">[01:07:56]</a>.

## Underappreciated Figures and Core Principles

While R.A. Fisher's reputation among statisticians is high, his mathematical ability can sometimes be underestimated due to his use of older, geometrical forms of mathematics <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>. Other important, possibly underappreciated figures include Pitman and Edgeworth <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.

The idea of [[causal_inference_and_its_applications | causal data fusion]] (combining observational and experimental data) holds promise for increasing power, though challenges related to random sampling need to be addressed <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>.

At its core, statistics often involves adding things up and occasionally squaring them, particularly through linear combinations, even in iteratively re-weighted processes <a class="yt-timestamp" data-t="01:09:46">[01:09:46]</a>. A deep understanding of statistics requires both mathematical rigor and intuitive grasp <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>.

## Advice for Aspiring Statisticians

*   **Find Concrete Problems:** Work on specific, tangible problems to gain experience and ownership <a class="yt-timestamp" data-t="01:12:28">[01:12:28]</a>.
*   **Look Wider:** Explore different fields and applications to borrow insights and methods, as seen in the unexpected collaboration between an agricultural scientist and an astronomer on applying standard errors <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>, and the development of n-of-1 trials in medicine influenced by psychologists <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>.
*   **Embrace Luck:** Acknowledge the role of chance and luck in career paths and outcomes <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.

A major, yet simple, improvement in [[clinical_trial_design_and_optimization | clinical trials]] would be to analyze them more efficiently using existing knowledge <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>. This includes avoiding dichotomization of data, which causes significant loss of power, and consistently using covariate information, practices that are often resisted despite being based on century-old theory <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>. Understanding the structure of variables and potential biases (e.g., in observational studies where samples might be processed in different labs) is crucial for good design <a class="yt-timestamp" data-t="01:18:23">[01:18:23]</a>.