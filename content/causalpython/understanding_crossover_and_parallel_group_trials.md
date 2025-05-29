---
title: Understanding crossover and parallel group trials
videoId: nT_yCwXSz54
---

From: [[causalpython]] <br/> 

Dr. Stephen Senn, author of "Statistical Issues in Drug Development" and "Dicing with Death," discusses the complexities of clinical trial design, emphasizing the practical and theoretical challenges faced by statisticians [00:00:38]. He highlights the importance of understanding different trial methodologies, particularly [[optimal_experimentation_in_causal_analysis | optimal experimental design]] and the distinction between crossover and parallel group trials [00:00:08].

## Randomization in Clinical Trials
Randomization, while seemingly straightforward, is a topic of ongoing discussion among statisticians and scientists [00:01:48]. Critics often misunderstand its purpose, believing its goal is "perfect estimation" or perfectly balanced groups [00:02:10]. However, the original intent of randomization, as proposed by R.A. Fisher, was to enable the estimation of how *imperfect* any estimate is [00:02:17].

Statisticians acknowledge that factors affecting outcomes in a clinical trial will not be perfectly balanced after randomization, leading to some bias in estimates [00:02:38]. The standard analysis accounts for this inherent imbalance, contributing to the estimate of error [00:03:00]. This is analogous to an engineer designing a bridge with expansion joints to account for thermal expansion, rather than expecting no expansion at all [00:04:27]. Ignoring this leads to "endless tedious conversations" [00:03:21].

## Types of Clinical Trials
The podcast discusses two primary types of clinical trial designs:

### Parallel Group Trial
A [[nf1_trials_and_their_design | parallel group trial]] is arguably the most common type of clinical trial [00:05:57]. In this design, patients are randomized to receive either a new treatment or a standard treatment, with each patient receiving only one of the interventions [00:06:01]. These trials are generally easier to implement [00:06:09]. An example given is a stroke prevention trial where half the subjects receive a new treatment and the other half receive standard care [00:06:51].

### Crossover Trial
In contrast, [[challenges_in_identifying_causal_effects_in_single_subject_studies | crossover trials]] aim to have each patient serve as their own control [00:06:13]. This design is feasible for chronic diseases where treatments are essentially reversible [00:06:18]. For example, in asthma, patients might be treated with one beta-agonist for a period, and then with another beta-agonist for a different period, with the order of treatments randomized [00:06:25].

### Comparison: Confidence Intervals
The design choice significantly impacts the confidence interval of the treatment effect:
*   **Crossover Trials**: Lead to much narrower confidence intervals because each subject acts as their own control, balancing for numerous factors like 20,000 genes and entire life histories [00:05:17].
*   **Parallel Group Trials**: Result in much wider confidence intervals because different patients receive different treatments, and this direct patient-as-own-control balancing is not possible [00:05:13].

## What Can Randomized Trials Answer?
Dr. Senn highlights five questions, initially outlined in his paper "Added Values," that randomized trials might attempt to answer, noting they become progressively more difficult [00:07:46]:

1.  **Was there a difference between treatments in the trial?** (Was there an effect of treatment?) [00:07:53]
2.  **What was the average effect for the patients actually treated?** (What difference did it make to them?) [00:08:02]
3.  **Was the effect the same for all patients in the trial?** [00:08:13]
4.  **If not, is it different for particular subgroups (e.g., men vs. women, elderly vs. young)?** [00:08:24]
5.  **What will it be like in future patients not in the trial?** (Can we say anything about patients outside the trial?) [00:08:34]

Most statistical work in trials focuses on questions one and two [00:09:05]. Answering questions three and four, especially regarding subgroups, often requires more power than available [00:09:13]. Question five, about generalizability to future patients, involves a degree of uncertainty not fully captured by formal statistical analysis [00:09:21]. For instance, streptomycin, once highly effective for tuberculosis, is no longer so due to the mutation of the disease [00:09:58].

This fifth question is not merely about counterfactuals in the traditional sense, but about the unpredictability of the future and changing environments beyond genetics [00:11:07]. Our theories, even in physics and especially in biology, are fallible [00:12:40].

## Practical Considerations in Trial Design
Clinical trial design involves significant practical, financial, and ethical limitations [00:16:11]. Statisticians must aim to answer questions one and two precisely, acknowledging the "missing element" of counterfactuals in parallel group trials, or changing circumstances in crossover trials [00:15:22].

A key challenge is the recruitment of diverse patient populations. For example, if a lung cancer trial predominantly includes males due to disease prevalence, it may be difficult to say something definitive for females, even if the drug is plausible for them [00:16:40]. Industry professionals often cannot afford the time or resources to answer all subgroup questions, as this competes with developing new, potentially better molecules [00:17:50].

This reality isn't unique to clinical trials; it applies to experimentation in general. The automobile industry, for example, uses accelerated life testing to predict a car's longevity without waiting years, extrapolating from stress conditions [00:19:36].

## History and Evolution of Experimental Design
The formal theory of experimentation has a long history, dating back over 100 years [00:20:27].
*   **R.A. Fisher** at Rothamsted in 1919 revolutionized experimental design, dealing with complex field experiments involving fertility gradients and correlation structures [00:20:58]. He developed methods to ensure that the estimate of error correctly reflected the variation contributing to treatment differences, leading to valid standard errors [00:22:09].
*   This led to the development of incomplete block designs and fractional factorial designs [00:22:32].
*   Industrial applications expanded in the 1940s, with clinical trials adopting these principles relatively later [00:23:01].
*   **John Nelder's** work in 1965, developing a "front-end machine" for linear models, was a key milestone [00:23:21]. This approach dictates how to analyze experiments to ensure correct standard errors based on blocking structure, experimental variation, and treatment structure [00:23:42].

## Role of Covariates in Clinical Trials
Incorporating covariates in models is crucial for efficiency, especially in larger trials.
*   For a typical Phase III [[nf1_trials_and_their_design | parallel group trial]] with hundreds of patients, including half a dozen or even up to 15 covariates is generally not problematic [00:44:42].
*   **Benefits of fitting a covariate (Normal Linear Model):**
    1.  **Reduced Mean Square Error:** Predictive covariates lower the mean square error, leading to narrower confidence intervals and greater power [00:45:19].
    2.  **Increased Variance (Small Effect):** Non-orthogonal covariates (not perfectly balanced) cause some variance inflation, but this is usually small, akin to losing one patient per covariate [00:45:41].
    3.  **Second Order Precision Loss:** Each covariate fitted reduces degrees of freedom, affecting the variance of the T-distribution, though this is less significant in larger trials [00:46:10].
*   **Non-linear models (e.g., logistic regression, survival analysis):** Covariates do not reduce mean square error in the same way, but their inclusion prevents attenuation of the treatment estimate, providing a more accurate signal [00:48:51].
*   Many trials "underuse the ability to fit covariates" [00:48:08]. A common mistake is dichotomizing data (e.g., responders/non-responders), which can lead to a 60% increase in required sample size and is misleading [01:15:05].

## Communication and Understanding in Statistics
Effective communication involves finding simple stories and graphical methods to explain complex statistical concepts [01:05:12]. For instance, explaining why an ANOVA might show a difference between treatments without pinpointing specific pairwise differences can be done with an analogy of a mother knowing her children were fighting without knowing who started it [01:05:50].

Statisticians themselves need to understand statistics in at least two ways: mathematically and intuitively [01:10:10]. Understanding that statistical solutions often reduce to linear combinations, even through iterative processes, can provide crucial insight [01:09:54].

There is a need to bridge communication gaps between different "ghettos" within statistics and between statisticians and other fields [00:56:59]. Practical constraints and real-world application details are crucial for effective theoretical development and application [01:00:16].

### Underappreciated Statisticians
Dr. Senn considers R.A. Fisher as a scientist to be underappreciated, despite his high reputation among statisticians [00:24:26]. Fisher's mathematical ability was often underestimated due to his use of older forms of mathematics and geometric intuition rather than the formal algebraic proofs that became standard [00:24:52]. Other underappreciated figures include Pitman, and earlier forerunners like Edgeworth [00:26:03].

## Career and Advice
Dr. Senn's career path in statistics was somewhat accidental but led to a fulfilling role solving difficult problems [01:10:53]. He learned much from teaching a broad range of topics in academia [00:38:38] and from hands-on, collaborative project work in industry, where early failure detection is valued [00:39:40]. His time in the Health Service taught him to be critical of data, even official statistics, due to underlying complexities like recalibration after censuses [00:40:00].

He highlights the profound responsibility felt when serving on a data safety monitoring board, deciding whether a trial continues, especially in cancer where toxicities often appear before efficacy [00:35:07]. Stopping a trial early due to efficacy is a positive experience, while stopping due to unexpected toxicity of a marketed drug is shocking but ultimately beneficial [00:37:02].

For those starting in an advanced field like statistics or causal inference, Dr. Senn advises:
*   Find concrete problems to work on to develop practical skills [01:12:27].
*   Look wider beyond your specific area of expertise to discover new methods or applications, like how n-of-1 trials in medicine were inspired by psychologists [01:12:53].
*   Be grateful for the opportunity to solve challenging problems [01:10:53].
*   Acknowledge that much of life is influenced by luck [01:11:46].

## Future Directions
The most impactful change for clinical trials would be to efficiently analyze them using existing knowledge [01:14:50]. This means avoiding dichotomization of data and consistently using covariate information, simple modeling steps which are often resisted despite being based on 100-year-old theory [01:15:07]. There's a contradiction in practice where covariates might be balanced in randomization (e.g., using minimization) but not then included in the model [01:16:36].

He also suggests that combining observational and clinical trial data sets could lead to more power, though this area still needs development [01:56:06].