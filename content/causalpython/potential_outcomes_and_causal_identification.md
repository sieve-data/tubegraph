---
title: Potential Outcomes and Causal Identification
videoId: gN-6DfhCguA
---

From: [[causalpython]] <br/> 

## What is an N-of-1 Trial?
An N-of-1 trial is a randomized study conducted on a single individual, essentially functioning as a crossover design [00:00:00, 02:35:00]. The core idea is to experiment on oneself to understand specific effects, such as how coffee consumption impacts sleep [02:47:00]. This involves randomizing exposures (e.g., coffee vs. no coffee on different days) and then comparing average outcomes under each condition [02:55:00]. These designs are also known as time series designs in some contexts [03:16:00].

### Generalizability
While N-of-1 trials are not typically meant to generalize across different people, they are designed to generalize to the individual being studied, helping to identify patterns specific to that person [00:12:00, 02:09:00, 02:56:00]. The question of whether a pattern is more general to other people is a secondary consideration in the N-of-1 study framework [02:15:00]. Connecting these individual findings to broader populations often involves methods like mixed-effects models that borrow information across people [02:24:00, 02:29:00].

## Challenges in N-of-1 Trials and Time Series Analysis
Analyzing data from a single individual over time, especially in [[causal_discovery_and_analysis | causal analysis]], presents specific challenges:
*   **Carryover Effects (Serial Interference)**: The treatment received at one point in time can impact outcomes at a later point [07:31:00]. This is a form of interference where the effect "carries over" into the future [07:48:00]. Serial interference specifically refers to interference over time, where a person's treatment at time point one affects their potential outcomes at time point two [06:57:00].
*   **Autocorrelation**: An individual's outcome at one time point might be naturally correlated with their outcome at another time point (e.g., migraine chances today affecting chances tomorrow) [07:54:00].
*   **Exogenous Factors**: External factors not influenced by the treatment or outcome (like weather) can affect outcomes over time [08:14:00].
*   **Non-Stationarity**: This is a major challenge where the underlying statistical properties of the time series change over time [04:09:00]. In classic N-of-1 trials, stationarity is often assumed or controlled by design (e.g., short study periods, wash-out periods between treatments) [04:20:00]. However, in real-world settings, non-stationarity requires advanced methods like Markov chain processes to analyze latent states and transitions, or techniques to stationarize the data (e.g., taking first differences), though these can alter the study question [04:29:00, 04:39:00]. Diagnosing and potentially segmenting time series to find stationary periods are also strategies [04:44:00].

## Causal Concepts in N-of-1 Trials
### Average Period Treatment Effect (APTE)
Given the availability of personal-level measurements (e.g., Fitbit data), N-of-1 trials can estimate the Average Period Treatment Effect (APTE) [10:14:00]. The APTE is an average effect similar to the traditional Average Treatment Effect (ATE) but applied to different time periods within the same person [10:52:00]. It compares an individual's outcomes under different treatment conditions across different periods of time [11:28:00].

### Statistical Machinery and Assumptions
The primary difference in the statistical methods used for N-of-1 trials compared to group-based trials is the time series setting [12:33:00]. The standard independence assumption between study participants is replaced by assumptions like stationarity, which means that averages remain consistent over a given time span [12:56:00]. While independence of errors can still be achieved, it requires controlling for factors like lag and autocorrelation [13:20:00].

### Heterogeneous Treatment Effects
N-of-1 trials are particularly useful when dealing with outcomes that have highly heterogeneous triggers or effects across individuals [09:31:00]. For example, coffee might worsen migraines for one person but prevent them for another [09:42:00]. In such cases, a traditional randomized control trial might show no average treatment effect because individual effects cancel out [09:50:00]. N-of-1 designs allow for understanding these personalized effects.

### Potential Outcomes Framework
The speaker, Eric Daza, primarily operates within the [[causal_inference_and_identification | potential outcomes framework]] for [[causal_inference_and_identification | causal identification]] [18:19:00]. This framework, when applied to N-of-1 trials, acknowledges the fundamental problem of [[causal_inference_and_identification | causal inference]]: at any given point in time, only one treatment was administered, so the counterfactual outcome for the other treatment is unobserved [0:41:15]. This problem persists, but it is applied over time for a single individual.

### Directed Acyclic Graphs (DAGs)
[[Causality_and_Causal_Models | Directed Acyclic Graphs (DAGs)]], as championed by Pearl, are found to be very useful for [[causal_inference_and_identification | causal identification]] [18:31:00]. DAGs provide a visual way to represent causal relationships and help in formulating the equations needed to determine if an effect is identifiable and how to construct a model to estimate it [18:40:00, 19:39:00]. For time series data, DAGs are particularly insightful because they force a recursive representation, showing arrows from the past to the present, which helps in understanding model assumptions and what variables need to be included [19:07:00, 19:15:00].

## Designing Trustworthy N-of-1 Studies
When designing a self-experiment or N-of-1 trial, several aspects are crucial for ensuring trustworthy and reliable conclusions:
1.  **Define the Study Question**: The most important step is clearly defining the question you aim to answer [22:37:00, 00:14:00]. This forms the "roots of really good science" [01:19:00].
2.  **Specify Variables and Measurement**: Clearly define what variables will be collected and how they will be measured (e.g., passive sensors, daily diaries, lab values) [22:15:00]. Consider the feasibility of these measurements given limited time, money, and patience [22:47:00].
3.  **"Design Trumps Analysis"**: Quoting Don Rubin, the design stage is more important than the analysis stage [23:13:00, 00:10:00, 00:59:00]. A poorly designed study will yield meaningless results ("garbage in, garbage out") [23:37:00]. This emphasizes the importance of carefully considering the study question, variables, timeline, and data collection methods [23:17:00].

## Evolution of the Field and Future Directions
The field of N-of-1 trials has roots in psychology and education [14:34:00] and intersects with areas like time series analysis, functional data analysis, econometrics, and finance (where they are sometimes called switchback experiments) [14:41:00, 15:10:00]. There's a push to bring these diverse literatures together to advance the field [15:36:00].

Future directions and challenges in N-of-1 trials include:
*   **Functional Data Analysis**: Moving beyond simple means and medians to analyze entire curves of data (e.g., step counts over a day, blood glucose levels) under different conditions [14:50:00, 04:59:00].
*   **Connection to Control Theory and System Identification**: Exploring how engineering techniques, such as impulse response and system identification, can be used to understand human behavior and optimize interventions to reach stable points [04:57:00, 04:50:00]. This is particularly relevant for [[causal_inference_and_identification | causal inference]] and [[understanding_and_applying_systematic_processes_in_causal_analysis | understanding and applying systematic processes in causal analysis]].
*   **Clarifying Nomenclature**: The term "individual treatment effect" is often a misnomer, as it frequently refers to a "small group treatment effect" or "individualized treatment effect," which is an average effect within a subgroup [38:48:00, 39:40:00]. A purely individual treatment effect is a counterfactual quantity that cannot be observed [39:54:00]. Making this distinction clearer is crucial for precise communication in the field.

## Personal Journey into Statistics and Causality
Eric Daza's journey into statistics and [[causality_and_causal_models | causality]] was influenced by diverse interests and a drive for deeper understanding [02:50:00, 03:27:00]. Initially studying neurobiology, he developed an interest in designing and analyzing experiments during his undergraduate studies [02:09:00, 02:72:00]. A pivotal moment was discovering an applied statistics master's program [02:81:00].

After working in pharma as a biostatistician, a desire to understand the underlying statistical concepts, rather than just programming, led him back to graduate school for a doctoral degree [02:91:00, 03:39:00]. A chance encounter with a [[causal_inference_and_identification | causal inference]] course taught by Mark Vanderland profoundly influenced him [03:56:00]. Later, Professor Susan Murphy's work on dynamic treatment regimes, a branch of [[causal_inference_and_identification | causal inference]] focused on personalized approaches, sparked his interest in N-of-1 trials [04:50:00]. A personal connection, with a loved one suffering from irritable bowel syndrome (a condition treatable with N-of-1 trials), further motivated his focus [05:20:00]. His journey highlights that success in quantitative fields doesn't always require a natural inclination for math, but often perseverance and a willingness to tackle challenges step-by-step [05:92:00].

The broader message to the [[causal_community | causal community]] is to prioritize defining the study question and thoroughly considering the design, as "design trumps analysis" [00:10:00, 00:59:00, 00:10:00, 01:00:00]. This foundational thinking extends beyond research into personal life, fostering a deeper understanding of various phenomena through statistical reasoning [01:01:22].

## Resources
*   **Stats of One Newsletter**: A resource for statistical methods, data collection, and software related to N-of-1 trials and single-case designs [14:10:00]. It covers aspects from time series literature, functional data analysis, econometrics, and finance (switchback experiments) [14:41:00, 15:10:00].
*   **NF1 Collaborative Network**: An Australian-based group offering foundational concepts, popularizing design and implementation, and providing consulting services for N-of-1 trials [17:08:00, 04:57:00].
*   **Software**: Platforms for self-data collection and experimentation exist, such as "Tummy Trials" (for IBS) and "Migraine Buddy" (for self-tracking) [24:17:00]. A promising package is "Study Me," developed by Stefan Konorski [24:50:00].