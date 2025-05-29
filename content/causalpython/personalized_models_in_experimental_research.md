---
title: Personalized models in experimental research
videoId: gN-6DfhCguA
---

From: [[causalpython]] <br/> 

Personalized models in experimental research primarily refer to **N-of-1 trials**, which are studies of a single person or subject <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. These trials are designed not to generalize to a broader population, but rather to the individual themselves, to understand patterns specific to that person <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. They aim to determine what works for an individual, even if it might not apply to others <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

The concept of N-of-1 trials has roots in psychology and education, and the term "switchback experiment" is used in finance for the same idea <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

## What is an N-of-1 Trial?

An N-of-1 trial is a randomized study involving a single individual, typically employing a crossover design <a class="yt-timestamp" data-t="02:35:38">[02:35:38]</a>. In this design, the individual is randomized to different treatments over time, such as drinking coffee on one day and no coffee on another, to observe the effect on a specific outcome like sleep duration <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. The average outcome under each condition is then compared <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.

These trials can also be referred to as time series designs <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>. Dr. Eric Daza, a principal clinical data scientist, creator of Stats of One, and researcher, became interested in N-of-1 trials due to his background in [[Causal inference and individual treatment effects | causal inference]], particularly dynamic treatment regimes, and a loved one's experience with irritable bowel syndrome, an idiosyncratic chronic condition treatable with N-of-1 trials <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

## Challenges in N-of-1 Trials

[[Challenges in identifying causal effects in single subject studies | Identifying causal effects in single subject studies]] presents unique challenges:
*   **Carryover Effects:** When a treatment administered at one point in time affects outcomes in the future <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. This implies "serial interference" over time, where a treatment at time point one affects one's own potential outcomes at time point two <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>.
*   **Autocorrelation:** The current outcome is naturally affected by past outcomes (e.g., migraine chances tomorrow influenced by migraine chances today) <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>.
*   **Exogenous Factors:** External factors not influenced by the treatment or outcome (e.g., weather) can affect outcomes over time <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
*   **Non-stationarity:** When the underlying distribution of the outcome changes over time, which can be an upfront challenge in real-world scenarios <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>. In classic N-of-1 trials, this is mitigated by controlling exposures and the study duration <a class="yt-timestamp" data-t="00:41:47">[00:41:47]</a>. Remedial strategies include stationarization by taking first differences (though this changes the study question) or segmenting time series into stationary periods using changepoint detection <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>.

## Statistical Considerations

The primary difference in the statistical analysis of N-of-1 trials compared to standard group-based trials is the time series setting <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
*   **Independence Assumption:** The typical independence assumption between participants is replaced by assumptions like stationarity <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. This means that averages stay consistent over a certain time span <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
*   **Correlated Outcomes:** Lagged outcomes can be correlated with present outcomes, requiring control for lag and autocorrelation to achieve effective independence of errors <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

### Average Period Treatment Effect (APTE)
The Average Period Treatment Effect (APTE) is an estimand similar to the Average Treatment Effect (ATE) but applied to different periods of time for the same individual <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. It compares the average outcome of an individual during periods under one treatment level (e.g., coffee) versus another (e.g., no coffee) <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

### Causal Identification and Frameworks
For [[Causal inference and individual treatment effects | causal identification]] in N-of-1 trials, the Directed Acyclic Graph (DAG) framework, as developed by Pearl and others, is particularly useful <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. DAGs help visualize the flow of arrows from the past to the present in time series, aiding in understanding what to include or exclude from a model and the implicit assumptions being made <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

## Applications

N-of-1 trials are especially useful when outcomes have very heterogeneous triggers across people <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. For example, coffee might worsen migraines for one person but prevent them for another <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. In such cases, a standard [[Experiments and AB testing in machine learning | randomized controlled trial]] or observational study between people would show no average treatment effect, as individual effects would cancel out <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. Conditions like migraines and irritable bowel syndrome, which are chronic and idiosyncratic, are well-suited for N-of-1 trials <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

They are ideal for recurring conditions; irreversible events like death cannot be studied this way because they only happen once <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>.

## Designing an N-of-1 Study

When designing an N-of-1 study, it is crucial to focus on the study question <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. As Rubin's quote emphasizes, "design trumps analysis" <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
Key aspects at the design, implementation, and analysis stages include:
*   **Specify Variables:** Clearly define what variables will be collected and how they will be measured (e.g., passive sensors, daily diaries, lab values) <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   **Feasibility:** Consider if the data collection methods are practical given limited time, money, and patience <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>.
*   **Clear Question:** Prioritize the specific question to be answered, as this guides which variables are necessary <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.
*   **Timeline:** Think about the timeline for data collection and analysis <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.
*   **Assumptions:** Be aware of the assumptions being made in the model, such as stationarity for time series data <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

## Software Ecosystem

Several software tools and platforms can assist with N-of-1 trials:
*   **Self-collection and experimentation platforms:** Examples include "Tummy Trials" (for irritable bowel syndrome) and "Migraine Buddy" (more for self-tracking) <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>.
*   **Study Me:** A promising package for designing and analyzing self-experiments <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

## Future Directions

The field of N-of-1 trials is expanding, with key areas of focus including:
*   **Popularizing the design:** Efforts are underway to make the design and implementation more widespread, for instance, through consulting services <a class="yt-timestamp" data-t="00:45:25">[00:45:25]</a>.
*   **Connecting different fields:** Integrating insights from diverse fields like single-case designs (psychology, education), time series analysis, functional data analysis, econometrics, and finance (where N-of-1 trials are known as switchback experiments) <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **Functional Data Analysis:** Analyzing entire curves of data (e.g., step counts over a day, blood glucose levels) rather than just means or medians to see how patterns differ under various conditions <a class="yt-timestamp" data-t="00:45:59">[00:45:59]</a>.
*   **Connection to Control Theory and System Identification:** Exploring how engineering techniques from control theory, such as impulse response system identification, can be applied to human behavior to optimize for stable states <a class="yt-timestamp" data-t="00:46:57">[00:46:57]</a>.

## Resources

*   **Stats of One Newsletter:** A newsletter focusing on statistical methods, data collection, and software related to N-of-1 trials and single-case designs <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   **N-of-1 Collaborative Network:** An Australian-based group that has been instrumental in popularizing N-of-1 trials for decades <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. They offer a consulting service <a class="yt-timestamp" data-t="00:45:29">[00:45:29]</a>.