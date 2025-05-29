---
title: Communication between statisticians and industry professionals
videoId: nT_yCwXSz54
---

From: [[causalpython]] <br/> 

Effective communication between statisticians and professionals in industry, particularly in fields like clinical trials and engineering, is crucial for successful project outcomes and mutual understanding of limitations and possibilities <a class="yt-timestamp" data-t="01:00:38">[01:00:38]</a>. This dialogue often faces challenges due to differing perspectives and backgrounds <a class="yt-timestamp" data-t="00:56:49">[00:56:49]</a>.

## Challenges in Communication

One significant challenge is the "ghettos" that exist within statistics itself and between statisticians and other fields <a class="yt-timestamp" data-t="00:56:59">[00:56:59]</a>.

### Misunderstanding of Randomization
A common point of contention arises from a misunderstanding of randomization, particularly among critics who expect perfect estimation <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Statisticians understand that perfect balance of factors is impossible post-randomization, but the method allows for estimating how imperfect any estimate is <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Critics often fail to grasp that the standard analysis for randomized trials already accounts for the fact that factors will not be perfectly balanced <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

For instance, in a Parallel Group trial, perfect balance between treatment groups is not guaranteed, but the statistical analysis is designed to account for this variation, leading to wider confidence intervals compared to crossover trials where subjects act as their own controls <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. The failure to understand this leads to "endless tedious conversations" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Bridging Theory and Practice in [[role_of_mathematics_and_statistics_in_experimental_design | Experimental Design]]
While there are "deep wonderful and complex theories of optimal experimental design," medical statisticians often do not know them well enough <a class="yt-timestamp" data-t="00:52:31">[00:52:31]</a>. Conversely, some experts in optimal [[role_of_mathematics_and_statistics_in_experimental_design | experimental design]] may not fully grasp the practical constraints of real experiments <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>. For example, they might not realize that patients are not treated simultaneously, or that certain optimality criteria might require lengthening the trial duration, which is impractical for diseases with imbalanced patient demographics <a class="yt-timestamp" data-t="00:53:21">[00:53:21]</a>. This disconnect can lead to proposed designs that are theoretically optimal but impossible to implement in practice <a class="yt-timestamp" data-t="00:53:18">[00:53:18]</a>.

### Practical Considerations in Clinical Trials
Statisticians may sometimes overstate the capabilities of their methods to clients, particularly regarding the five levels of questions that randomized trials can answer <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>:
1.  Was there a difference between treatments in the trial (effect of treatment)? <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>
2.  What was the average effect for the patients actually treated? <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>
3.  Was the effect the same for all patients? <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>
4.  Is the effect different for particular subgroups (e.g., men vs. women)? <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>
5.  What will the effect be like in future patients not in the trial? <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>

Most statistical work primarily addresses questions one and two <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Questions three and four are often beyond the power of a typical trial <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. Question five, concerning future patients, introduces uncertainty not fully captured by formal statistical analysis, as real-world factors (like disease mutation or environmental changes) can alter outcomes <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. This involves making "leaps of faith" in areas like drug registration for specific demographics when full data isn't available <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

### [[challenges_of_implementing_causality_in_research_and_industry | Challenges of Implementing Causality]]
The assumption that genetics is the sole determinant, or that classifying patients based on genetics will predict everything about future patients, is misleading <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. Other environmental factors constantly change and may affect humans <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. Predicting the future requires understanding mechanisms of change, which are complex and often unknown <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

## Learning from Different Sectors

### [[transition_from_academia_to_industry | Academic and Industry Learning Processes]]
Different environments offer distinct learning opportunities <a class="yt-timestamp" data-t="00:38:28">[00:38:28]</a>:
*   **Academia**: Often involves teaching a broad range of subjects, leading to wide but not always deep knowledge <a class="yt-timestamp" data-t="00:38:59">[00:38:59]</a>.
*   **Industry**: Emphasizes learning by doing, working on projects where success or failure matters <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>. This intense collaborative work is very useful <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>. It also teaches critical evaluation of data, even official statistics, as there may be underlying "stories" (e.g., population recalibration after a census) <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.

### Lessons from Industrial Experimentation
The automobile industry's use of accelerated life testing for car parts is an example where waiting for real-world data (e.g., a 10-year warranty period) is impractical <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. This necessitates extrapolation from stress testing, a common challenge in many experimental fields <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. Clinical trials, relatively late to formal experimental design, can learn from this long history <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>. Early work in experimental design, pioneered by R.A. Fisher at Rothamsted starting in 1919, dealt with complex agricultural experiments, which evolved into theories for incomplete block designs and fractional factorial designs <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. This was further developed in industry from the 1940s onwards <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>.

## Improving Communication with Stakeholders

### Simple Stories and Visualizations
When [[communicating_and_justifying_causal_methods_to_stakeholders | communicating and justifying causal methods to stakeholders]], it's essential to find simple stories and analogies that everyone can understand <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>. For example, to explain how an analysis of variance can show a treatment effect without identifying specific pairwise differences, one can use the analogy of a mother knowing her children are fighting but not who the aggressor is <a class="yt-timestamp" data-t="01:05:50">[01:05:50]</a>. Simple graphical methods can also illustrate complex concepts like regression to the mean without relying on advanced mathematics <a class="yt-timestamp" data-t="01:06:38">[01:06:38]</a>. Resorting to algebra should be a last resort <a class="yt-timestamp" data-t="01:07:18">[01:07:18]</a>.

### Understanding Model Behavior
Statisticians should strive to understand statistical concepts in at least two ways: mathematically and intuitively <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>. Understanding the weights in linear combinations, for instance, can provide a deeper grasp of how a design operates beyond just the matrix algebra <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>.

One major challenge in [[applications_and_limitations_of_statistical_models_in_clinical_trials | statistical models in clinical trials]] that needs better communication is the underuse of covariate information <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>. Dichotomizing continuous data, for example, is wasteful and misleading, significantly reducing statistical power <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>. Incorporating covariates can increase precision and understanding <a class="yt-timestamp" data-t="01:15:39">[01:15:39]</a>. Despite the theory being over 100 years old, these simple improvements are often resisted, possibly due to ingrained habits or a perceived complexity <a class="yt-timestamp" data-t="01:15:47">[01:15:47]</a>.

Ultimately, bridging communication gaps requires both sides to engage in dialogue and understand each other's constraints and theoretical underpinnings <a class="yt-timestamp" data-t="00:55:59">[00:55:59]</a>.