---
title: Myths and controversies of randomization in clinical trials
videoId: nT_yCwXSz54
---

From: [[causalpython]] <br/> 

Randomization is a fundamental concept in experimental design, particularly in clinical trials, yet it remains a subject of controversy and misunderstanding among statisticians and scientists <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Core Misunderstanding of Randomization

A central misunderstanding about randomization is the belief that its goal is to achieve perfect balance or estimation between treatment groups <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a> <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Critics argue that once randomized, factors affecting an outcome will not be perfectly balanced, leading to bias in the estimate <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

However, as R.A. Fisher, who proposed randomization, realized, perfect estimation is impossible <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The true purpose of randomization is to allow for the estimation of how imperfect any estimate is, providing a measure of error <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The standard analysis for randomized trials accounts for the fact that factors will not be perfectly balanced <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

This concept can be illustrated with an analogy:
> "The mathematician says to the engineer, 'well actually the problem with the bridge that you've built is that in the hot weather the bridge will expand and then in that case you're going to have trouble because you've calculated the bridge in such a way that it fits over the river but uh thermal expansion will lead to lead to problems' and the engineer says 'yes I know that that's why we have Expansion Joints'" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
Similarly, statisticians using randomization have already accounted for the imbalance by allowing for it in the error estimation <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Comparing Trial Designs

The impact of balancing on confidence intervals can be seen by comparing [[understanding_crossover_and_parallel_group_trials | crossover and parallel group trials]] <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

*   **Parallel Group Trial**: Patients are randomized to receive either a new treatment or a standard treatment, with each patient receiving only one. This is the most common trial type and is relatively easy to implement <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. In a parallel group trial, groups are not perfectly balanced, leading to wider confidence intervals <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Crossover Trial**: Applicable to chronic, reversible conditions (e.g., asthma), where each patient can receive multiple treatments in a randomized order <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. In a crossover trial, each subject acts as their own control, implicitly balancing for numerous genetic and life history factors, resulting in much narrower confidence intervals <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a> <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Five Questions in Randomized Trials

A key presentation by Dr. Stephen Senn, "Seven Myths of Randomization," outlines five questions that randomized trials attempt to answer <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a> <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. These questions progressively increase in difficulty and scope, highlighting the [[applications_and_limitations_of_statistical_models_in_clinical_trials | applications and limitations of statistical models in clinical trials]] in real-world settings:

1.  **Was there a difference between treatments in the trial?** (Was there an effect of treatment?) <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>
2.  **What was the average effect for the patients actually treated?** (What difference did it make to them?) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>
3.  **Was the effect the same for all patients in the trial?** <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>
4.  **Is the effect different for particular subgroups?** (e.g., men vs. women, elderly vs. young) <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>
5.  **What will it be like in future patients not in the trial?** (Can we say anything about patients outside the trial?) <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>

Most of what statisticians do is confined to answering questions one and two, with occasional forays into question three, and rarely question four <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Question five, concerning future patients, introduces a level of uncertainty not fully captured by formal statistical analysis <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. The future is inherently unpredictable due to changing circumstances and unknown factors, as seen with streptomycin for tuberculosis becoming ineffective due to bacterial mutation <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This relates to [[causal_inference_and_individual_treatment_effects | causal inference and individual treatment effects]] and the challenge of understanding mechanisms of change <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

## Practical Considerations and Limitations

In practice, clinical trials prioritize answering questions one and two to establish treatment effectiveness, often due to financial and ethical resource constraints <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. It's often impossible to gain enough statistical power to make meaningful statements about subgroups (question four) <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. Decisions sometimes have to be made based on incomplete information, as exemplified by a lung cancer drug being effective for males but lacking sufficient data for females <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

This highlights the [[challenges_of_implementing_causality_in_research_and_industry | challenges of implementing causality in research and industry]] in real-world settings. Similar limitations are found in other industries, such as accelerated life testing in the automobile industry, where full experimental conditions (e.g., waiting 10 years for a car warranty test) are impractical <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

## Historical Context and Evolution of Experimental Design

The formal theory of experimentation has a long history <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. It began significantly with R.A. Fisher at Rothamsted in 1919, where he developed complex experimental designs for agriculture, accounting for factors like fertility gradients and correlation structures in fields <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. Fisher's work led to the development of incomplete block designs and fractional factorial designs, which aimed to compare many treatment combinations with limited experimental material <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.

This area of experimental design was further developed in industry starting in the 1940s, and clinical trials adopted these principles relatively later <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>. John Nelder's development in 1965 of a "front-end machine" for linear models provided a framework to analyze experiments correctly, ensuring valid standard errors based on blocking structure, treatment structure, and design matrix <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>. This historical perspective is crucial for understanding the [[role_of_mathematics_and_statistics_in_experimental_design | role of mathematics and statistics in experimental design]].

## Communication Challenges and Underuse of Covariates

There's a significant gap in [[communication_challenges_in_causal_inference | communication challenges in causal inference]] between theoretical optimal experimental design and practical application <a class="yt-timestamp" data-t="00:55:19">[00:55:19]</a>. Experts in [[optimal_experimentation_in_causal_analysis | optimal experimentation in causal analysis]] may propose designs without understanding real-world constraints, such as patients not being treated simultaneously or the feasibility of recruiting specific demographics <a class="yt-timestamp" data-t="00:53:18">[00:53:18]</a> <a class="yt-timestamp" data-t="00:54:08">[00:54:08]</a>.

A major practical improvement in clinical trials would be to efficiently use existing knowledge, particularly by avoiding dichotomization of data and extensively using covariates <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>. Dichotomizing data, like classifying patients as "responders" or "non-responders," can lead to significant loss of statistical power <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>. Including covariates, which are predictive variables, can lead to smaller confidence intervals, greater power, and a better understanding of treatment effects, especially in trials with hundreds of patients <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>.

### Impact of Interventions on Data Distributions
Using covariates appropriately allows for a more accurate understanding of the [[impact_of_interventions_on_data_distributions | impact of interventions on data distributions]]. While there are considerations for how many covariates to include (losing a degree of freedom per covariate and potential variance inflation if not orthogonal), the benefits often outweigh these minor penalties in larger trials <a class="yt-timestamp" data-t="00:45:02">[00:45:02]</a>. For nonlinear models, missing predictive covariates can lead to misspecified models and attenuation of the signal <a class="yt-timestamp" data-t="00:48:41">[00:48:41]</a>.

Despite these known benefits and the fact that the underlying theory is over 100 years old, these simple modeling steps are often resisted in practice due to perceived complexity or ingrained habits <a class="yt-timestamp" data-t="01:15:47">[01:15:47]</a>. There's a contradiction in balancing covariates in design (e.g., using minimization) but then not including them in the final model <a class="yt-timestamp" data-t="01:16:37">[01:16:37]</a>.