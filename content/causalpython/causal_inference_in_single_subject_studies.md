---
title: Causal Inference in Single Subject Studies
videoId: gN-6DfhCguA
---

From: [[causalpython]] <br/> 

N-of-1 trials, also known as single-subject studies, represent a specialized study design focused on a single individual, often employing randomization [00:00:00]. This approach contrasts with traditional group-based trials by primarily aiming for personalization rather than broad generalizability to large populations [00:00:12].

## What is an N-of-1 Trial?

An N-of-1 trial is a study of one person [00:00:00]. In the trial sense, it is randomized, typically using a crossover design [00:02:42]. For example, one might experiment on themselves to see if drinking coffee affects sleep, randomizing coffee consumption (coffee vs. no coffee) on different days and comparing average sleep amounts [00:02:47]. These designs are also known as time series designs [00:03:16].

### Purpose and Generalizability
While N-of-1 trials are not generally meant to generalize to other people, they are designed to generalize to the individual being studied [00:00:12]. The primary goal is to understand a consistent pattern within that specific person [00:00:19]. The question of broader generalizability to other individuals is considered a secondary objective in the context of N-of-1 studies [00:21:18]. When seeking to generalize findings across individuals, methods that borrow information across people, such as mixed-effects models, are often employed [00:21:26]. However, a key difference in N-of-1 is that models per person can differ, unlike mixed-effects models where they are often constrained to be mostly the same [00:21:50].

## Challenges in N-of-1 Trials

The main challenges in single-subject time series settings include:
*   **Carryover Effects** The treatment received at one point in time can impact outcomes in the future [00:07:31]. This is a form of serial interference, where the effect "carries over" [00:07:45].
*   **Autocorrelation** An individual's outcome at one point in time might be influenced by their own past outcomes (e.g., migraine chances tomorrow affected by migraine chances today) [00:07:54].
*   **Exogenous Factors** External factors not affected by treatment or outcome (e.g., weather) can still influence the outcome [00:08:14].

In controlled N-of-1 trials, these challenges are often managed through careful design:
*   Clinicians and patients collaboratively design the trial, being aware of exposures and their duration in the body [00:41:47].
*   Washout periods can be built in before re-randomization [00:42:07].
*   The time series involved are often kept short to maintain stationarity by design [00:42:18].
*   Clinicians communicate with patients to be aware of other factors that might impact outcomes [00:42:30].

In real-world, less controlled scenarios, dealing with non-stationarity is tougher [00:42:43]. While methods like stationarization (e.g., taking first differences) can be applied, they change the study question from looking at the direct outcome to its derivative or difference [00:43:39]. Diagnostic tests for stationarity on residuals can also be performed, and if assumptions don't hold, techniques like changepoint detection might be used to segment the time series into stationary periods [00:44:24].

## Causal Inference in N-of-1 Trials

The application of [[causal_inference_and_its_applications | causal inference]] in N-of-1 trials aims to identify individual-level triggers and recurring patterns [00:09:00]. This is particularly useful for outcomes with highly heterogeneous triggers across individuals [00:09:31]. For instance, coffee might worsen migraines for one person but prevent them for another; a standard group-based trial would show no average effect, highlighting the value of N-of-1 trials for personalized insights [00:09:40].

### Average Period Treatment Effect (APTE)
The Average Period Treatment Effect (APTE) is an estimate used in N-of-1 trials [00:10:31]. Similar to the Average Treatment Effect (ATE) in traditional trials, the APTE is an average effect between two or more treatment levels [00:10:54]. The "period" in APTE signifies that it's an average effect measured across different time periods for the *same* person, rather than between different people [00:11:28]. It involves comparing the same person under different conditions (e.g., coffee vs. no coffee periods) [00:11:55].

### Serial Interference
Interference in the standard [[causal_inference_concepts_and_applications | causal inference]] context means one person's treatment affects another's outcomes [00:05:57]. **Serial interference** is when the "treatment" at one time point affects the potential outcomes of the *same* person at a future time point [00:06:35]. For example, being vaccinated at time point one affects potential outcomes at time point two for the same individual [00:06:44]. A unique aspect of serial interference is that future treatments cannot interfere with past outcomes [00:07:02].

## Statistical Machinery and Assumptions
The largest difference in the statistical analysis of N-of-1 trials compared to group-based studies is the time series setting [00:12:33].
*   **Independence Assumption**: In group-based trials, there's usually an independence assumption between participants [00:12:44]. In N-of-1 trials, this is replaced by assumptions related to time series [00:12:52].
*   **Stationarity**: A key assumption is stationarity, meaning that over time, certain averages (like the mean) remain constant over a specific span [00:12:56].
*   **Error Dependence**: While lagged outcomes can be correlated with present outcomes, the independence assumption for errors can still be achieved after controlling for factors like lag and autocorrelation [00:13:20].

### Frameworks for Causal Identification
When it comes to [[causal_inference_and_identification | causal identification]], the potential outcomes framework is often used [00:18:19]. The Directed Acyclic Graph (DAG) framework, as developed by Pearl and others, is considered very useful due to its visual nature [00:18:31]. DAGs help in understanding the flow of arrows from the past to the present in a time series, which is crucial for identifying effects and constructing models for estimation [00:19:13]. The DAG framework assists in determining if an effect is identifiable and in specifying necessary model components and underlying assumptions [00:18:47].

## Designing and Running an N-of-1 Study
For individuals interested in running N-of-1 experiments on themselves, key aspects at the design, implementation, and analysis stages are crucial for trustworthy conclusions [00:20:21]:
1.  **Define the Study Question**: Most importantly, clearly define the specific question you want to answer [00:22:37]. This guides the entire study.
2.  **Specify Variables and Measurement**: Decide what variables to collect, how to measure them (e.g., passive sensors like Fitbit, daily diaries, lab values), and ensure feasibility [00:22:15].
3.  **Resource Management**: Be mindful of limited time, money, resources, and patience, especially if others are involved in data collection [00:22:47].
4.  **Design Trumps Analysis**: Echoing Rubin's quote, the design stage is paramount [00:10:01]. A well-designed study, considering the question, variables, timeline, and data collection methods, prevents "garbage in, garbage out" scenarios [00:23:13].

## Resources and Future Directions
*   **Stats of One**: A newsletter focused on statistical methods, data collection, and software related to N-of-1 trials and single-case designs [00:14:10]. It aims to bridge knowledge from various fields like psychology, education, time series, functional data analysis, econometrics, and finance [00:14:34]. In finance, N-of-1 trials are sometimes called "switchback experiments" [00:15:17].
*   **N-of-1 Collaborative Network**: An Australian-based group that popularizes the design and implementation of N-of-1 trials and offers consulting services [00:17:08].
*   **Software Ecosystem**:
    *   *Tummy Trials*: An early app for irritable bowel syndrome patients [00:24:17].
    *   *Migraine Buddy*: More on the self-tracking side [00:24:39].
    *   *StudyMe*: A newer package by Stefan Konorski for self-collection and experimentation [00:24:50].

Future directions for N-of-1 trials include:
*   Further work in **functional data analysis**, looking at entire curves of data (e.g., step counts over a day, blood glucose, athletic performance) rather than just means, to see how these curves differ under various conditions [00:45:59].
*   Connecting [[causal_inference_and_its_applications | causal inference]] to **control theory and system identification**, utilizing engineering techniques to optimize human behavior or bring an individual to a stable point [00:46:57]. This area is particularly relevant for understanding agentic systems and learning reliable world models [00:47:50].

## Personal Journey into Statistics and Causal Inference
Dr. Eric Daza, a trained concert pianist and creator of Stats of One, initially pursued neurobiology in college [01:32:00]. His interest shifted towards statistics after a cognitive studies course lab component where he designed and analyzed an experiment [00:27:06]. A one-year master's program in applied statistics at his school became a "statistically significant moment" that set him on his path [00:28:11].

After working in pharma as a biostatistician, he sought a doctoral degree to understand the underlying statistical concepts [00:29:05]. He serendipitously took a [[causal_inference_and_its_applications | causal inference]] course taught by Mark van der Laan, whom he initially did not know was a leading figure in the field [00:03:56]. His interest in N-of-1 trials was sparked by Professor Susan Murphy's work on dynamic treatment regimes (a branch of [[causal_inference_and_its_applications | causal inference]]) and the personal experience of a loved one with irritable bowel syndrome, a chronic condition treatable with N-of-1 trials [00:05:01].

Dr. Daza's journey highlights that a background in mathematics is not a prerequisite for success in statistics, as he himself found math and statistics very challenging initially [00:28:31]. His eventual diagnosis with ADHD explained his early struggles with concentration and his later ability to break down daunting tasks into smaller, manageable steps [00:32:57]. He emphasizes the satisfaction derived from mastering difficult concepts and finding personal application for statistical reasoning in everyday life [00:59:02].

## Advice for Aspiring Scientists
For those starting in advanced fields like statistics, machine learning, or [[causal_inference_and_its_applications | causality]], the advice is to:
*   **Start Doing the Work**: Get into the data, start coding, and work through the math [00:50:22].
*   **Break Down Tasks**: Break large, daunting steps into smaller, manageable ones, which makes the process less overwhelming [00:51:06].
*   **Define the Study Question**: Always begin by clearly defining the question you want to answer, as this is the "root of really good science" [01:00:05]. From this question, the specifics of variables and data collection can be determined [01:00:16].
*   **Be Aware of Assumptions**: Understand the assumptions made when specifying a model or analysis [01:01:00].
*   **Embrace Challenges**: Be prepared for real-world data issues such as messy data or unexpected collection problems; these insights come from hands-on experience [01:51:57].