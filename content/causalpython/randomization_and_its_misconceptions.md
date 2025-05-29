---
title: Randomization and its misconceptions
videoId: nT_yCwXSz54
---

From: [[causalpython]] <br/> 

Randomization, while a cornerstone in statistical methodology, remains a controversial idea among some statisticians and scientists today <a class="yt-timestamp" data-t="01:48:48">[01:48:48]</a>. Dr. Stephen Senn, author of "Statistical Issues in Drug Development" and "Dicing with Death," discusses common misunderstandings surrounding randomization, particularly in the context of clinical trials <a class="yt-timestamp" data-t="01:39:35">[01:39:35]</a>.

## Core Misconception: Perfect Estimation

A primary source of criticism stems from the misunderstanding that randomization's goal is "perfect estimation" <a class="yt-timestamp" data-t="02:08:35">[02:08:35]</a>. However, R. A. Fisher, who proposed randomization, recognized that perfect estimation is impossible <a class="yt-timestamp" data-t="02:17:15">[02:17:15]</a>. Instead, randomization was introduced to allow for the estimation of "how imperfect any estimate was" <a class="yt-timestamp" data-t="02:22:20">[02:22:20]</a>.

Critics argue that since many factors can affect an outcome in a clinical trial, randomization will not perfectly balance all of them, leading to bias in the estimate <a class="yt-timestamp" data-t="02:33:34">[02:33:34]</a>. Dr. Senn emphasizes that this imperfection is acknowledged and accounted for in standard statistical analysis <a class="yt-timestamp" data-t="02:49:11">[02:49:11]</a>.

> "I sort of imagine the conversation between a mathematician and an engineer and the mathematician says to the engineer well actually the problem with the bridge that you've built is that in the hot weather the bridge will expand and then in that case you're going to have trouble because you've calculated the bridge in such a way that it fits over the river but thermal expansion will lead to lead to problems and the engineer says yes I know that that's why we have Expansion Joints and the ma policians say yes but you're ignoring the fact that the bridge expands he's not listening to what the engineer says what I've already told the philosophical critics is I've already allowed for the fact that the factors will not be perfectly balanced and I can demonstrate this by showing you how narrow the confidence interval would be for a crossover trial compared to how broad it will be for a Parallel Group trial" <a class="yt-timestamp" data-t="03:57:42">[03:57:42]</a>

## Trial Types and Confidence Intervals

Randomization's impact on confidence intervals illustrates its function.
*   **Parallel Group Trial**: This is the most common trial type, where patients are randomized to receive either a new treatment or a standard treatment, with each patient receiving only one <a class="yt-timestamp" data-t="05:55:20">[05:55:20]</a>. For example, in stroke prevention, half of the subjects might receive a new treatment and half the standard treatment <a class="yt-timestamp" data-t="06:51:24">[06:51:24]</a>.
*   **Crossover Trial**: In this design, which is suitable for chronic diseases with reversible treatments (e.g., asthma), each patient serves as their own control, receiving both treatments at different times in a randomized order <a class="yt-timestamp" data-t="06:12:47">[06:12:47]</a>. This balances for "20,000 genes [and] all life history to date" <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>, leading to much narrower confidence intervals compared to parallel group trials <a class="yt-timestamp" data-t="05:17:34">[05:17:34]</a>.

Even though parallel group trials do not balance for these factors, the statistical analysis accounts for this variability, allowing for wider, yet valid, confidence intervals <a class="yt-timestamp" data-t="05:28:44">[05:28:44]</a>.

## Five Questions of Randomized Trials

Dr. Senn outlined five questions that randomized trials might attempt to answer, noting their increasing difficulty <a class="yt-timestamp" data-t="07:46:58">[07:46:58]</a>:

1.  **Was there a difference between treatments in the trial?** (Was there an effect of treatment?) <a class="yt-timestamp" data-t="07:53:23">[07:53:23]</a>
2.  **What was the average effect for the patients that were actually treated?** (What difference did it make to them if they were given treatment B rather than treatment A?) <a class="yt-timestamp" data-t="08:00:27">[08:00:27]</a>
3.  **Was the effect the same for all the patients in the trial?** <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>
4.  **Is the effect different for particular subgroups?** (e.g., men vs. women, elderly vs. young) <a class="yt-timestamp" data-t="08:24:43">[08:24:43]</a>
5.  **What will it be like in future patients not in the trial?** (Can we say anything about patients outside the trial?) <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>

Most statistical work focuses on answering questions one and two <a class="yt-timestamp" data-t="09:03:50">[09:03:50]</a>. Answering questions three and four meaningfully requires significant power <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>. The fifth question, concerning generalization to future patients, involves an inherent degree of uncertainty not fully captured by formal statistical analysis <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>. For example, streptomycin was effective for tuberculosis at the time of its pioneering trial, but is no longer effective due to bacterial mutation, illustrating how future conditions can differ <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>. This highlights [[challenges_in_identifying_causal_relationships]] and the limitations of predicting based solely on trial data, as the world and populations change <a class="yt-timestamp" data-t="11:09:47">[11:09:47]</a>.

## Practical Considerations and Covariates

In practice, clinical trials must operate within financial and ethical constraints, often prioritizing answering questions one and two <a class="yt-timestamp" data-t="15:15:21">[15:15:21]</a>. It is often impossible to adequately answer questions three or four due to insufficient data for subgroups <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>.

Using covariates effectively is crucial for efficiency in trials <a class="yt-timestamp" data-t="42:44:00">[42:44:00]</a>.
*   **Benefits of Covariates**: Fitting predictive covariates reduces the mean square error, leading to narrower confidence intervals and greater power <a class="yt-timestamp" data-t="45:17:15">[45:17:15]</a>.
*   **Costs of Covariates**: If covariates are not perfectly balanced (orthogonal), there is a slight inflation of variance, typically equivalent to losing about one patient per covariate <a class="yt-timestamp" data-t="45:40:48">[45:40:48]</a>. Additionally, each covariate fitted reduces a degree of freedom, which can be significant in very small trials but less so in larger ones <a class="yt-timestamp" data-t="46:27:00">[46:27:00]</a>.

Dr. Senn suggests that for typical Phase III trials with hundreds of patients, using half a dozen to fifteen covariates is generally not a problem and is often "underused" <a class="yt-timestamp" data-t="44:42:00">[44:42:00]</a>. In non-linear models (e.g., logistic regression), missing predictive covariates can lead to an "attenuation of the estimate" rather than a direct effect on variance <a class="yt-timestamp" data-t="48:51:00">[48:51:00]</a>.

## Historical Context and Optimal Experimental Design

The formal theory of experimentation has a long history, starting significantly with R.A. Fisher at Rothamsted in 1919 <a class="yt-timestamp" data-t="20:56:00">[20:56:00]</a>. Fisher developed methods to account for inherent variability in experimental units (e.g., soil fertility gradients) to obtain valid standard errors <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>. This led to concepts like incomplete block designs and fractional factorial designs, which were further developed in industry from the 1940s onwards <a class="yt-timestamp" data-t="22:33:00">[22:33:00]</a>.

Dr. Senn points out a significant gap: there are "many deep wonderful and complicated complex theories of [[optimal_experimentation_in_causal_studies]] that we medical statisticians ought to know better and don't" <a class="yt-timestamp" data-t="52:31:00">[52:31:00]</a>. Conversely, some optimal experimental design experts lack understanding of practical constraints in real-world experiments <a class="yt-timestamp" data-t="52:52:00">[52:52:00]</a>. For example, optimal designs might require unrealistic patient recruitment numbers or durations <a class="yt-timestamp" data-t="53:50:00">[53:50:00]</a>, or may only outperform simpler designs if a dose escalation can be completed, which isn't guaranteed <a class="yt-timestamp" data-t="54:51:00">[54:51:00]</a>. This highlights a failure of communication between theoretical and applied statistical communities <a class="yt-timestamp" data-t="55:19:00">[55:19:00]</a>.

## Communication and Intuition

Effective communication in statistics, especially with non-experts, involves using simple stories and graphical methods to convey complex ideas <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>. For instance, explaining why an overall treatment effect can be significant while individual pairwise comparisons are not, using an analogy of children fighting <a class="yt-timestamp" data-t="01:05:17">[01:05:17]</a>. Dr. Senn advises that statisticians should understand their field in at least two ways: mathematically and intuitively <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>.

## Probability and Causality

The need for [[probabilistic_modeling_and_bayesian_frameworks]] is debated, with some, like Nassim Taleb, arguing that probability can be misleading, especially outside of well-structured systems like games <a class="yt-timestamp" data-t="01:20:51">[01:20:51]</a>. However, Dr. Senn believes that in some cases, thinking probabilistically is unavoidable <a class="yt-timestamp" data-t="01:21:22">[01:21:22]</a>.

## Advice for Aspiring Statisticians

For those starting in fields like statistics or causality, Dr. Senn advises:
*   **Find concrete problems**: Work on specific problems that you can "own" to build problem-solving habits <a class="yt-timestamp" data-t="01:25:27">[01:25:27]</a>.
*   **Look wider**: Explore other fields and be open to borrowing insights or methods, as unexpected cross-pollination can occur (e.g., n-of-1 trials in medicine influenced by psychologists) <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.
*   **Luck is a factor**: Acknowledge the role of chance in one's career trajectory <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.

A key practical improvement for clinical trials today would be to efficiently analyze them using existing knowledge <a class="yt-timestamp" data-t="01:14:48">[01:14:48]</a>. This includes avoiding dichotomization of continuous data, which leads to significant power loss <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>, and consistently using covariate information for greater precision <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>. These are "simple modeling steps...using theory which is 100 years old" <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>, yet are often resisted, pointing to ingrained habits or a lack of understanding of the underlying experimental structure <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.