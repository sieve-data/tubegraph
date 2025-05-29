---
title: Clinical trial design and optimization
videoId: nT_yCwXSz54
---

From: [[causalpython]] <br/> 

Dr. Stephen Senn, author of "Statistical Issues in Drug Development" and "Dicing with Death," is an expert in clinical trial design, particularly focused on randomization and the [[history_and_influence_of_statisticians_in_clinical_trials|history of statistics]] in clinical trials <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. He emphasizes the importance of understanding the practical and theoretical aspects of experimental design <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Randomization: Purpose and Misunderstandings

Randomization, though sometimes considered controversial, is not meant to achieve "perfect estimation" or perfectly balanced groups <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Instead, its primary goal, as realized by R.A. Fisher, is to allow for the estimation of how imperfect any estimate is <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Critics often misunderstand that imbalances in factors post-randomization are expected and accounted for in standard statistical analysis, contributing to the estimate of error <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

Dr. Senn uses the analogy of an engineer building a bridge with expansion joints to explain that statisticians already "allow for the fact that the factors will not be perfectly balanced" <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. The standard analysis permits for these imbalances, and a failure to grasp this leads to "endless tedious conversations" <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## [[crossover_trials_vs_parallel_group_trials | Crossover Trials vs. Parallel Group Trials]]

The choice of trial design significantly impacts confidence intervals:
*   **Parallel Group Trial**: The most common type, where patients are randomized to receive either a new treatment or a standard treatment, with each patient receiving only one <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. For example, in a stroke prevention trial, half subjects get the new treatment and half get the standard <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Crossover Trial**: Patients receive both treatments sequentially, with the order randomized <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. This design is suitable for chronic, reversible conditions like asthma <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. In a crossover trial, each subject acts as their own control, implicitly balancing for numerous factors like 20,000 genes and life history, leading to "much narrower confidence intervals" compared to parallel group trials <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

## Five Questions Randomized Trials Can (and Cannot) Answer

Dr. Senn outlined five questions that randomized trials attempt to answer, in increasing order of difficulty <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>:
1.  **Was there a difference between treatments in the trial?** (i.e., an effect of treatment) <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
2.  **What was the average effect for the patients actually treated?** <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>
3.  **Was the effect the same for all patients in the trial?** <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>
4.  **Is the effect different for particular subgroups?** (e.g., men vs. women, elderly vs. young) <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
5.  **What will it be like in future patients not in the trial?** This is the most ambitious question, involving uncertainty not fully captured by formal statistical analysis <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

Most statistical work remains focused on questions one and two <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Answering question five is challenging because the future holds surprises, and conditions can change (e.g., drug resistance, evolving patient populations) <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This involves making predictions with theories that can be fallible, much like in physics or biology <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. For example, a drug effective today might not be in the future due to disease mutation <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## Practical Considerations in Clinical Trial Design

Clinical trial design operates within financial and ethical constraints <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. It's often impossible to collect enough data to provide definitive answers for subgroups (questions three and four), especially for less prevalent patient populations <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. Statisticians must make "leaps of faith" and operate under the assumption that effects generalize, given that further research competes with developing new, potentially better molecules <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

This challenge is not unique to clinical trials; for instance, the automobile industry uses "accelerated life testing" to predict car part longevity without waiting years for natural wear and tear <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. This highlights the universal need to extrapolate from observed data under specific conditions to future, unobserved conditions <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.

## [[history_and_influence_of_statisticians_in_clinical_trials | History of Experimental Design]]

The formal theory of experimentation has a long history <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>:
*   **R.A. Fisher (early 20th century)**: Began with agricultural experiments at Rothamsted in 1919, dealing with fertility gradients and correlation structures in fields <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. He developed methods to ensure that the estimation of error reflected the way factors contributed to differences between treatments <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. This led to designs like incomplete block designs and fractional factorial designs <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>.
*   **Industrial Development (1940s onwards)**: Further developed experimental design, including by people like George Box, who worked in chemical production <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>.
*   **Clinical Trials**: Came relatively late to this formal theory <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.
*   **John Nelder (1965)**: Developed a "front-end way of thinking" for linear models, which could dictate how to analyze an experiment to ensure correct standard errors, given the blocking, treatment structure, and design matrix <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>. Dr. Senn believes this approach should guide the design of many experiments <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.
*   **Internet Experiments**: The "fourth age of experimental design" <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.

## Improving Clinical Trial Efficiency and Practice

### Current Inefficiencies
Current clinical trial practices often underuse available statistical techniques <a class="yt-timestamp" data-t="00:48:08">[00:48:08]</a>:
*   **Dichotomization**: Frequently, continuous data is dichotomized (e.g., "responders" vs. "non-responders"), which is "wasteful and misleading," leading to a significant loss in statistical power <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>.
*   **Underuse of Covariates**: Many trials do not fully utilize covariate information, even though including relevant covariates can significantly increase precision and power by reducing mean square error <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>. While adding covariates can lead to some variance inflation due to non-orthogonality (costing about one patient per covariate), this is negligible in large trials <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>. There is also a loss of degrees of freedom, affecting the variance of the T-distribution, but this effect diminishes with larger sample sizes <a class="yt-timestamp" data-t="00:46:32">[00:46:32]</a>.

### Bridging Gaps in Knowledge
There's a significant gap between theoretical statisticians (e.g., those studying [[optimal_experimentation_in_causal_studies|optimal experimental design]]) and practitioners (e.g., medical statisticians) <a class="yt-timestamp" data-t="00:52:31">[00:52:31]</a>. Theoretical designs might not account for practical constraints, like patients not being treated simultaneously, or the difficulty of recruiting specific demographic strata at an equal rate <a class="yt-timestamp" data-t="00:53:20">[00:53:20]</a>. Conversely, practitioners might not be aware of advanced theoretical designs that could offer benefits <a class="yt-timestamp" data-t="00:55:12">[00:55:12]</a>.

Dr. Senn advocates for better communication within statistics, not just between statisticians and other fields <a class="yt-timestamp" data-t="00:56:59">[00:56:59]</a>. He is open to the idea of [[optimal_experimentation_in_causal_studies|causal data fusion]], combining observational and experimental datasets, as a plausible way to increase power, though some current proposals have limitations <a class="yt-timestamp" data-t="00:56:04">[00:56:04]</a>.

## Career Insights and Advice

### Responsibility in Clinical Trials
Working on data safety monitoring boards (DSMBs) involves profound responsibility, as decisions impact patient lives <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>. Decisions to stop a trial early due to toxicity or efficacy carry immense weight <a class="yt-timestamp" data-t="00:36:20">[00:36:20]</a>. It's inherent to the process that there's a risk the treatment will not be positive; if efficacy was known, a trial wouldn't be necessary <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a>.

### Academia vs. Industry
*   **Academia**: Offers broad but not always deep knowledge across many topics, often requiring teaching subjects outside one's core expertise <a class="yt-timestamp" data-t="00:38:33">[00:38:33]</a>.
*   **Industry**: Provides learning through practical project work, where success or failure matters, and collaborative efforts are intense <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>. Dr. Senn's experience in the pharmaceutical industry taught him to scrutinize data given its often complex origins and calibrations <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>.

### Communication Lessons
*   **Simple Stories**: Use analogies to explain complex statistical concepts. For instance, the "mother and fighting children" anecdote illustrates how an overall effect can be detected without identifying specific pairwise differences <a class="yt-timestamp" data-t="01:05:50">[01:05:50]</a>.
*   **Graphical Methods**: Employ visual tools to convey ideas, such as teaching regression to the mean without relying on complex mathematical concepts <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>.
*   **Intuition with Math**: Statisticians need to understand concepts in at least two ways: mathematically and intuitively. The math provides the formal framework, but intuition explains *why* the math works and delivers the expected answer <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>.

### Advice for Newcomers
*   **Work on Concrete Problems**: Gain experience by solving specific, tangible problems to build a foundation <a class="yt-timestamp" data-t="01:12:28">[01:12:28]</a>.
*   **Look Wider**: Explore different fields and applications. For example, the concept of [[personalized_experimental_design|N-of-1 trials]] in medicine (where a patient acts as their own control through repeated treatments) was borrowed from psychology <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>.
*   **Embrace Luck**: Recognize that a significant portion of career progression and opportunities can be attributed to luck <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.