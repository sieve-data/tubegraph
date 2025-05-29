---
title: causal inference in practical applications
videoId: OvmpcL1CKqM
---

From: [[causalpython]] <br/> 

## Introduction to Causal Inference
The Causal Bandits podcast focuses on [[causal_inference_and_machine_learning | causality and machine learning]] <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. This field is a sub-branch of statistics, requiring assumptions and model building to analyze results <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The speaker, who studied political science and statistics, realized early in his career that statistics alone was insufficient to answer complex business questions <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

## Limitations of Statistical Approaches
Traditional statistical measurements, such as T-tests, often fall short because they only highlight statistical significance without delving into the underlying data generating process <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. This realization led to the understanding that there's a parallel dimension to data analysis beyond mere measurement error <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

### Initial Encounter with Causal Thinking
An early experience at a satellite internet company highlighted the need for causal thinking <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. Working on email campaigns to retain customers, the initial approach was to predict which customers were likely to churn <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. However, it was observed that many of these customers would churn regardless of intervention <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. The critical shift in perspective was realizing that the goal was not to predict churn, but to identify which customers would respond best to a discount <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

This led to the understanding that:
*   Some customers are too upset to be swayed by a small discount <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   Others are perfectly satisfied and might even be prompted to reconsider their service by an unexpected discount <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.

This experience underscored that simple statistical associations are often insufficient for effective decision-making; understanding how variables in a system react is paramount <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

## Applying Causal Inference in Real-World Problems
Modern projects focus on helping companies make better decisions by utilizing [[causal_inference_and_decision_theory | causal inference and decision theory]] <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. The speaker's company provides an analytics platform for product and growth teams, addressing questions like which product features drive conversions to paid users or prevent churn <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.

A common challenge is that users who adopt a feature are often already more engaged or have higher initial intent <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>. This confounds the analysis, making it difficult to determine if conversion differences are due to feature adoption or pre-existing user intent <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>.

### Debiasing with the Time Domain
To address this confounding, a method was developed that uses users' activity within the app as a proxy for their initial intent or personality <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>. By comparing conversion rates among users with similar levels of prior engagement (e.g., those who interacted with at least five other features), the effect of the specific feature adoption becomes more discernible <a class="yt-timestamp" data-t="16:44:00">[16:44:40]</a>. This approach generates stronger confounders to debias results <a class="yt-timestamp" data-t="16:31:00">[16:31:00]</a>.

### The Role of Survival Analysis
Measuring the effect of time-varying treatments (like feature adoption) and outcomes (like conversions), while also using time-varying confounders (like in-app activity), presents significant data organization challenges <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>.

Traditional classification problems often require discarding large amounts of data to maintain the correct temporal order of events (treatment before outcome) <a class="yt-timestamp" data-t="19:28:00">[19:28:00]</a>. This can lead to biased discarding of information, especially for very effective features where conversion happens immediately after adoption <a class="yt-timestamp" data-t="20:06:00">[20:06:00]</a>.

Survival analysis is an underrated method that can solve these issues <a class="yt-timestamp" data-t="21:02:00">[21:02:00]</a>. It is a third branch of supervised learning (beyond classification and regression) that handles both continuous and binary data components <a class="yt-timestamp" data-t="21:18:00">[21:18:00]</a>.

> "Using survival lets you solve the problem I was mentioning earlier. You'd go about and use what is called time varying covariates to encode those instances where users have adopted the feature but haven't converted yet and those instances where users haven't adopted the feature, and you would build a survival curve for both groups and then compare the... conversion rate at the end of the period." <a class="yt-timestamp" data-t="21:36:00">[21:36:00]</a>

This approach provides equal footing for both groups in terms of time to convert and avoids discarding information <a class="yt-timestamp" data-t="22:12:00">[22:12:00]</a>. It also allows modeling behavioral confounders similarly, treating feature adoption as a censored time-to-event target <a class="yt-timestamp" data-t="22:34:00">[22:34:00]</a>.

### Preserving Temporal Information
The key is to preserve and leverage temporal information to gain more accurate estimates and avoid controlling for irrelevant variables <a class="yt-timestamp" data-t="23:24:00">[23:24:00]</a>. By structuring data to ensure treatments precede outcomes, and user profiles precede treatment adoption, biases are reduced <a class="yt-timestamp" data-t="23:49:00">[23:49:00]</a>. Collapsing the time dimension can lead to "backwards relationships" where variables that are *results* of a treatment are mistakenly treated as *preceding* it, leading to biased analysis <a class="yt-timestamp" data-t="25:32:00">[25:32:00]</a>. This means potentially controlling for a mediator, which blocks the flow of information from the treatment to the outcome <a class="yt-timestamp" data-t="27:01:00">[27:01:00]</a>.

> "If you are controlling for actions in the product that are a result of adopting a certain feature, you actually are biasing, you are making the estimate look lower than it should be." <a class="yt-timestamp" data-t="26:21:00">[26:21:00]</a>

This would remove the mediation effect, leaving only the direct effect, which is often not what is desired for decision-making purposes where the total effect (mediated or direct) is more relevant <a class="yt-timestamp" data-t="27:58:00">[27:58:00]</a>.

### Handling Hidden Confounders
While preserving the time dimension resolves biases like those from blockers or mediators, it doesn't entirely address issues like hidden confounding <a class="yt-timestamp" data-t="29:52:00">[29:52:00]</a>. If no hidden confounders are assumed, sorting variables by time can resolve most issues <a class="yt-timestamp" data-t="30:35:00">[30:35:00]</a>.

## Costs and Risks of [[assumptions_in_causal_inference | Assumptions in Causal Inference]]
Making causal assumptions or consulting domain experts involves costs, primarily in man-hours of highly trained individuals <a class="yt-timestamp" data-t="33:30:00">[33:30:00]</a>. Randomized Controlled Trials (RCTs) can help assume no hidden confounding but come with their own costs <a class="yt-timestamp" data-t="31:55:00">[31:55:00]</a>.

The speaker's work focuses on utilizing [[causal_inference_and_decision_theory | causal inference and decision theory]] in low-resource environments, which means accepting a lower degree of guarantees <a class="yt-timestamp" data-t="34:48:00">[34:48:00]</a>. Causality is viewed as a spectrum, and any method that makes estimates "somewhat more causal" is better than relying on plain correlations <a class="yt-timestamp" data-t="35:38:00">[35:38:00]</a>. The aim is to find methods that yield the highest guarantees with the lowest costs <a class="yt-timestamp" data-t="35:56:00">[35:56:00]</a>.

### Success Stories
Using these methodologies, companies have seen significant improvements. For example, a golfing app customer used the approach to identify a feature that, despite low initial traction, had great potential <a class="yt-timestamp" data-t="36:13:00">[36:13:00]</a>. By disentangling biases, it was found that the feature was valuable but inaccessible <a class="yt-timestamp" data-t="36:50:00">[36:50:00]</a>. Implementing recommendations (pushing the feature forward, making it part of onboarding) led to surprisingly high improvements in key performance indicators (KPIs) <a class="yt-timestamp" data-t="37:13:00">[37:13:00]</a>.

## [[challenges_in_implementing_causal_analysis_in_practice | Challenges in Implementing Causal Analysis in Practice]]
The biggest challenge is convincing stakeholders of the value of [[practical_applications_of_causal_methods | practical applications of causal methods]] <a class="yt-timestamp" data-t="38:44:00">[38:44:00]</a>. Organizations already collect and use data for decision-making, so persuading them to adopt different aggregation methods for causal analysis can be difficult <a class="yt-timestamp" data-t="39:02:00">[39:02:00]</a>.

### [[communication_challenges_in_causal_inference | Communication Challenges in Causal Inference]]
To overcome these [[communication_challenges_in_causal_inference | communication challenges in causal inference]]:
*   **Set Expectations Right:** Don't claim absolute truth, but emphasize a higher probability of correctness or better results compared to regular associations <a class="yt-timestamp" data-t="39:56:00">[39:56:00]</a>.
*   **Tie Results to Data:** The ability to clearly connect results to the underlying data is crucial for building trust, especially when delivering counterintuitive or challenging recommendations <a class="yt-timestamp" data-t="41:02:00">[41:02:00]</a>.
*   **Transparency:** Methods should be completely transparent, allowing stakeholders to see how every calculation is derived from their data and reproduce the results themselves <a class="yt-timestamp" data-t="42:41:00">[42:41:00]</a>. This empowers them and fosters ownership of the results <a class="yt-timestamp" data-t="43:05:00">[43:05:00]</a>.

## The Future of Causality
The future is definitely more causal, treating causality as a spectrum <a class="yt-timestamp" data-t="43:24:00">[43:24:00]</a>. Adoption will depend on resources:
*   Larger organizations with more resources will use state-of-the-art methods for high-guarantee answers to big questions <a class="yt-timestamp" data-t="43:50:00">[43:50:00]</a>.
*   Smaller players might use automation or Software as a Service (SaaS) solutions to tap into causal inference with lower guarantees, especially if lacking domain experts <a class="yt-timestamp" data-t="44:04:00">[44:04:00]</a>.

The field of [[causal_discovery_and_inference_in_AI | causal discovery and inference in AI]] began to gain momentum around 2017 with AIC conferences and data hackathons <a class="yt-timestamp" data-t="44:40:00">[44:40:00]</a>. The rise of Large Language Models (LLMs) and their human-like behavior has further opened the door for people to believe in complex concepts like [[causal_reasoning_in_AI | causal reasoning in AI]] <a class="yt-timestamp" data-t="45:00:00">[45:00:00]</a>. Both in academia and industry, there's growing awareness and investment in causal inference <a class="yt-timestamp" data-t="45:38:00">[45:38:00]</a>.

## Advice for Aspiring Practitioners
For those overwhelmed by the amount of information in [[causal_inference_and_machine_learning | causal inference and machine learning]]:
*   **Avoid Shortcuts:** A deep understanding of causal inference cannot be achieved through shortcuts, like relying solely on LLMs <a class="yt-timestamp" data-t="46:43:00">[46:43:00]</a>. It requires meticulous study <a class="yt-timestamp" data-t="47:03:00">[47:03:00]</a>.
*   **Engage Actively:** Just reading papers provides only a shallow understanding <a class="yt-timestamp" data-t="47:51:00">[47:51:00]</a>. To truly internalize methods and understand their behavior in different settings, engage in activities like:
    *   Writing a blog <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>
    *   Giving lectures or presentations <a class="yt-timestamp" data-t="48:35:00">[48:35:00]</a>
    *   Creating code examples and simulations <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>
    *   Being explicit in coding forces thinking through all specifics of how things work <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.
*   **Seek Practical Application:** After building a theoretical understanding, the next step is to work in the field and apply causal inference <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>. This is the best way to level up and gain real-world insights, even if it means taking a seemingly demotion <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.
*   **Focus on Business Value:** Always prioritize bringing value to the company over chasing the "shiniest algorithm" or job titles <a class="yt-timestamp" data-t="51:11:00">[51:11:00]</a>. Understanding the business impact of your work is crucial <a class="yt-timestamp" data-t="51:46:00">[51:46:00]</a>.
*   **Just Start:** The most important first step is to "just do it" and start today <a class="yt-timestamp" data-t="56:12:00">[56:12:00]</a>.

## Recommended Resources
*   **_Causal Inference Primer for Statistics_** by Judea Pearl: A small, to-the-point booklet excellent for understanding DAGs (Directed Acyclic Graphs) <a class="yt-timestamp" data-t="58:13:00">[58:13:00]</a>.
*   **_A Tale of Two Cultures_** paper: Discusses the differences between the statistics and computer science communities, fostering an understanding of different analytical mindsets <a class="yt-timestamp" data-t="58:37:00">[58:37:00]</a>.

## Message to the Causal Python Community
It is challenging to justify the use of causal inference methods over simpler alternatives <a class="yt-timestamp" data-t="59:24:00">[59:24:00]</a>. However, it is vital to persist in the journey to become better practitioners <a class="yt-timestamp" data-t="01:00:21">[01:00:21]</a>. Doing science correctly by handling confounding and preserving temporal dimensions is essential to help businesses, not hurt them <a class="yt-timestamp" data-t="00:59:47">[00:59:47]</a>. Causal inference is not just a formal exercise; it genuinely helps drive better decision-making and ultimately helps businesses thrive <a class="yt-timestamp" data-t="01:00:32">[01:00:32]</a>.

Further work from the speaker can be found on LinkedIn and his blog: `arin.io` <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>.