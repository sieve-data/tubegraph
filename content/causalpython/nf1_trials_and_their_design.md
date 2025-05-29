---
title: NF1 trials and their design
videoId: gN-6DfhCguA
---

From: [[causalpython]] <br/> 

An N-of-1 (NF1) trial is a randomized study conducted on a single individual, often employing a [[understanding_crossover_and_parallel_group_trials | crossover design]] [00:00:00]. The core idea is to experiment on oneself, for instance, to determine if drinking coffee affects one's sleep patterns [00:02:47]. This involves randomizing behaviors—like drinking coffee one day and abstaining the next—and then comparing outcomes, such as average sleep duration under each condition [00:02:55]. These designs are also known as [[time_series_designs_and_causal_inference | time series designs]] [00:03:16] or "switchback experiments" in finance [00:15:17].

## Purpose and Generalizability
NF1 trials are primarily [[personalized_models_in_experimental_research | personalized models]] [00:00:14] and are not intended to generalize to broader populations [00:12:12]. Instead, their purpose is to generalize to the individual being studied, helping them understand patterns specific to themselves [00:00:21]. This approach is particularly useful for conditions with highly heterogeneous triggers across individuals, where an average treatment effect observed in a group study might cancel out due to varying individual responses [00:09:31]. For example, coffee might worsen migraines for one person but prevent them for another [00:09:42].

## Key Design Considerations
When designing an NF1 study, whether for oneself or for others, crucial aspects include the design, implementation, and analysis stages [00:00:31]. The most important step is to clearly define the study question—what specific question is the experiment trying to answer [00:01:14]?

### Importance of Design
The principle of "design trumps analysis" is paramount [00:01:01]. A well-thought-out design ensures the conclusions drawn are trustworthy and reliable [00:00:42]. This involves:
*   **Specifying Variables**: Identifying what variables will be collected and measured [00:22:15].
*   **Measurement Feasibility**: Determining how data will be measured (e.g., passive sensors, daily diaries, lab values) and ensuring it's feasible within limited time and resources [00:22:20].
*   **Defining the Study Question**: Focusing on a clear, answerable question to guide data collection and avoid gathering irrelevant information [00:22:56].

## Challenges in NF1 Trials
Several [[challenges_in_identifying_causal_effects_in_single_subject_studies | challenges in identifying causal effects in single subject studies]] are common in time series settings:

*   **Carryover Effects**: When a treatment given at one point in time impacts future outcomes [00:07:31]. This implies "serial interference," meaning an individual's treatment at time point one affects their potential outcomes at time point two [00:06:46]. However, this interference only works forward in time, as future treatments cannot affect past outcomes [00:07:09].
*   **Autocorrelation**: When an individual's outcomes at one time point are naturally affected by their outcomes at previous time points (e.g., a migraine today increasing the chance of a migraine tomorrow) [00:07:52].
*   **Exogenous Factors**: External variables not affected by the treatment or outcome that can still influence the outcome (e.g., weather affecting migraine probability) [00:08:14].

## Addressing Challenges
In a classic, highly controlled NF1 trial, clinicians and patients co-design the study, controlling key elements:
*   **Known Exposures**: Treatments are well-defined, and their duration in the body is understood, allowing for washout periods before re-randomization [00:41:52].
*   **Randomization**: Treatment assignment is randomized, controlling for potential biases [00:42:12].
*   **Stationarity**: Trials are often conducted over short periods (e.g., a few weeks) to ensure the time series is largely stationary by design [00:42:18].
*   **Patient Awareness**: Clinicians are aware of other factors impacting the patient's outcomes through direct interaction [00:42:30].

In real-world applications where such control is harder, strategies include:
*   **Stationarization**: Transforming non-stationary time series (e.g., taking the first difference), though this changes the study question to focus on the derivative [00:43:39].
*   **Diagnostics**: Using modeling diagnostics to check for shifts in the time series [00:44:09].
*   **Segmentation**: Identifying and segmenting periods of stationarity using methods like changepoint detection [00:44:42].

## Analysis and Statistical Machinery
The primary difference in statistical analysis for NF1 trials compared to standard group-based trials is the [[applications_and_limitations_of_statistical_models_in_clinical_trials | time series setting]] [00:13:35]. The assumption of independence between participants is replaced by an assumption of stationarity [00:12:48]. While independence of errors can still be achieved, it requires controlling for lagged outcomes and autocorrelation [00:13:16].

### Average Period Treatment Effect (APTE)
The Average Period Treatment Effect (APTE) is an estimate used in NF1 trials [00:10:31]. Similar to the Average Treatment Effect (ATE) in group studies, APTE calculates an average effect between two or more treatment levels [00:10:54]. However, the "period" in APTE signifies that the comparison is made across different time periods *for the same person* [00:11:32]. It compares "groups" of the same individual under different conditions at different times [00:11:55].

## Frameworks for Causal Identification
When it comes to [[causal_inference_and_individual_treatment_effects | causal inference]] and identification in NF1 trials, the **Potential Outcomes framework** is commonly used [00:18:19]. Additionally, **Directed Acyclic Graphs (DAGs)** are highly useful, especially for time series data. DAGs help visualize causal relationships, including recursive patterns where past events affect present outcomes, aiding in identifying and constructing identifiable models [00:19:11].

## Software Ecosystem
A growing software ecosystem supports NF1 trials and self-experimentation:
*   **Tummy Trials**: An early app for irritable bowel syndrome patients [00:24:17].
*   **Migraine Buddy**: More focused on self-tracking than experiment design [00:24:39].
*   **Study Me**: A promising newer package developed by Stefan Konorski [00:24:50].

## Resources for Learning More
*   **Stats of One Newsletter**: Focuses on statistical methods, data collection, and software related to NF1 trials, single-case designs (psychology/education), and time series analysis [00:14:10].
*   **NF1 Collaborative Network**: An Australia-based group that popularizes NF1 trial design and implementation, offering foundational concepts and consulting services [00:17:08].
*   **Functional Data Analysis (FDA)**: A field that analyzes entire curves of data over time (e.g., step counts, blood glucose curves) rather than just averages [00:14:50]. This is increasingly relevant with digital health technologies [00:46:07].

## Future Directions and [[Optimal experimentation in causal analysis | Optimal Experimentation]]
Future work in NF1 trials includes:
*   Connecting to **Functional Data Analysis** for studying changes in data curves over time [00:45:59].
*   Linking [[causal_inference_and_individual_treatment_effects | causal inference]] with **control theory and system identification**, using engineering techniques to optimize human behavior or bring an individual to a stable point [00:46:57]. This involves exploring concepts like impulse response [00:47:35].

## Advice for Starting an NF1 Study
For those interested in running self-experiments or designing NF1 trials:
*   **Start Doing the Work**: Engage with data, begin coding, and work through the mathematics [00:50:23].
*   **Take Small Steps**: Break down daunting tasks into manageable steps, as cumulative small efforts lead to significant progress [00:51:01].
*   **Embrace Challenges**: Be prepared for real-world issues like dirty data, data accessibility, and missing information, as these are part of the learning process [00:51:57].
*   **Prioritize the Study Question**: Clearly defining the question you want to answer is the root of good science and should guide all design decisions [01:00:02]. This helps specify variables and assumptions required for the study [01:00:21].

> "Design trumps analysis." <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>
> "What is the question you're trying to answer? That is the roots of really good science." <a class="yt-timestamp" data-t="01:01:14">[01:01:14]</a>