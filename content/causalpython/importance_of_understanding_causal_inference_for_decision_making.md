---
title: Importance of understanding causal inference for decision making
videoId: OvmpcL1CKqM
---

From: [[causalpython]] <br/> 

Understanding [[causal_analysis_and_its_importance | causal analysis]] and [[causal_inference_and_decision_making | causal inference]] is paramount for making informed decisions, particularly in business settings where traditional statistical methods often fall short <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. While statistics focuses on associations and measurement error, [[causal_inference_and_its_applications | causal inference]] delves into the underlying data generating process, revealing how variables in a system truly react to interventions <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Limitations of Traditional Statistics

Early career experiences highlight the inadequacy of statistics alone for answering complex business questions <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Simply running T-tests or identifying statistical significance doesn't always lead to meaningful results <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The core issue is that statistical significance only addresses uncertainty related to measurement error, not the causal mechanisms of the data generating process <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

For instance, in customer retention campaigns, the goal should not be merely predicting which users are likely to churn, as they might churn regardless of intervention <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Instead, the focus should be on identifying which customers will respond best to a discount <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Statistical associations alone cannot answer this; it requires understanding how variables in the system would react to a decision <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

Furthermore, academic statistics often dedicates "zero attention" to [[causal_reasoning_in_decisionmaking | causal thinking]] or [[causal_inference_concepts and applications | causal inference]], despite it being a sub-branch of statistics that requires working with assumptions and building models of the world <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

## Leveraging Time in Causal Inference

A significant challenge in [[causal_analysis_and_its_importance | causal analysis]] is controlling for all possible confounders, especially in open systems like marketing campaigns <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. However, the time domain can be leveraged to debias problems to a certain extent <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

### The Problem of Confounding
In product analytics, a common problem involves determining if feature adoption drives conversions to paid users, or if users adopting features are already more engaged and have a higher initial intent <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. Users might adopt features due to their personality, preferences, or perceived product value, which confounds the relationship between feature adoption and conversion <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. Traditional methods of controlling for baseline attributes like country or device are often too coarse to capture this "initial intent" or user personality <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

### Survival Analysis and Time-Varying Covariates
A method to address this is using [[applications_of_causal_inference_in_science_and_medicine | survival analysis]], which measures user activity within the app as a proxy for initial intent or user personality <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. This allows for a more believable comparison, such as comparing conversion rates among highly engaged users (e.g., those who interacted with five features) who additionally adopted a specific feature, versus those who didn't <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. This behavioral proxy acts as a better "personality test" than direct questions <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

Challenges arise with time-varying treatments (feature adoption), time-varying outcomes (conversions), and time-varying confounders (in-app activity) <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. If feature adoption and conversion happen quickly, or on the same day, traditional classification problems may discard a significant amount of valuable data, leading to biased conclusions <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

Survival analysis, a third branch of supervised learning (after classification and regression), addresses this by allowing the use of time-varying covariates <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. It allows for an "equal footing" in terms of conversion time for both groups and prevents data discarding <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.

### Preserving Temporal Information
The key benefit of using these methods is the preservation of the time dimension <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>. This ensures that the treatment (feature adoption) always precedes the outcome (conversion) and that confounders (user profile) precede the treatment adoption <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. Collapsing data and eliminating the time dimension can lead to "backwards relationships" where actions are mistaken for causes instead of results, biasing the analysis <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. This risk includes controlling for a mediator, which would block the flow of information from the treatment to the outcome, underestimating the total causal effect <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.

While preserving time can solve common biases like mediators, it doesn't always exclude spurious relations, particularly in the presence of hidden confounders, such as in "M-bias" scenarios <a class="yt-timestamp" data-t="00:29:10">[00:29:10]</a>. However, assuming no hidden confounders, sorting by time can resolve many issues <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

## Costs, Risks, and Value in Causal Assumptions
Making causal assumptions comes with costs and risks <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. These can include the "man hours" required for well-judged assumptions or consulting domain experts <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>. While randomized controlled trials (RCTs) can help assume no hidden confounding, they are costly <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. Conversely, making assumptions about the data generating process can be risky if incorrect <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>.

For organizations with limited resources, the goal is to find methods that yield the highest guarantees with the lowest costs <a class="yt-timestamp" data-t="00:35:59">[00:35:59]</a>. [[Causal inference and decision making | Causality]] should be viewed as a spectrum, not a binary state <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>. Making estimates "somewhat more causal" is always better than relying on plain correlations <a class="yt-timestamp" data-t="00:35:45">[00:35:45]</a>.

## Real-World Impact
Applying [[causal_inference_and_its_applications | causal inference]] can significantly improve business operations. For example, a golfing app discovered that a feature with low initial traction actually had great potential to drive user KPIs after disentangling confounding factors <a class="yt-timestamp" data-t="00:37:02">[00:37:02]</a>. By making the feature more accessible and part of the onboarding process, the company saw substantial increases in top-line KPIs <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a>. This demonstrates how causal methods can uncover hidden potential and lead to impactful decisions <a class="yt-timestamp" data-t="00:37:52">[00:37:52]</a>.

## Challenges in Adoption and Communication
The biggest challenge in applying [[causal_inference_concepts_and_applications | causal inference]] methods is convincing stakeholders of their value <a class="yt-timestamp" data-t="00:38:44">[00:38:44]</a>. Organizations already collect and use data for [[causal_inference_and_decision_making | decision-making]], so demonstrating that aggregating data differently will generate significant value can be difficult <a class="yt-timestamp" data-t="00:39:12">[00:39:12]</a>.

Key strategies for effective communication include:
*   **Setting expectations right**: Don't claim absolute truth, but rather a higher probability of correctness compared to regular associations <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>.
*   **Tying results back to data**: Transparency in how calculations are derived from the data is crucial for building trust <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>. Allowing stakeholders to reproduce results fosters ownership and belief, especially when findings are counterintuitive or challenge existing beliefs <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.

## The Future of Causal Inference
The future is definitely more causal, treating [[role_of_causality_and_bayesian_methods_in_decision_making | causality]] as a spectrum <a class="yt-timestamp" data-t="00:43:32">[00:43:32]</a>. Adoption will vary based on organizational resources; those with more resources will use state-of-the-art methods for high guarantees, while smaller players might use automation or Software-as-a-Service (SaaS) solutions for lower guarantees but still derive more causal conclusions <a class="yt-timestamp" data-t="00:43:44">[00:44:18]</a>. The rise of Large Language Models (LLMs) and their perceived intelligence might also open doors for people to believe in complex causal concepts <a class="yt-timestamp" data-t="00:45:02">[00:45:02]</a>. The field is gaining steam not only in academia but also in industry, with more leaders recognizing the need to invest in [[causal_inference_and_its_applications | causal inference]] <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>.

## Advice for Aspiring Practitioners
For those just starting with [[causal_inference_concepts_and_applications | causal inference]], the journey can feel overwhelming <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>. Key advice includes:
*   **Avoid shortcuts**: [[Causal inference and decision making | Causal inference]] requires a deep, meticulous understanding that cannot be achieved through quick answers from tools like ChatGPT <a class="yt-timestamp" data-t="00:46:47">[00:46:47]</a>.
*   **Engage in active learning**: Just reading papers provides a shallow understanding. To truly utilize methods in real-world scenarios, one must go deeper <a class="yt-timestamp" data-t="06:28:28">[06:28:28]</a>. Activities like writing a blog, giving lectures, or doing code examples (simulations) force a deeper understanding by requiring clear explanation and explicit coding of processes <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Seek practical application**: It's a "chicken and egg" problem: hard to get hired without experience, but hard to gain experience without a job <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>. Writing and simulating can be an intermediary step <a class="yt-timestamp" data-t="00:48:27">[00:48:27]</a>.
*   **Prioritize value over sophistication**: Always consider how your work impacts the business and strive to bring tangible value <a class="yt-timestamp" data-t="00:51:09">[00:51:09]</a>.

### Recommended Resources:
*   Alex's book on [[machine_learning_versus_causal_inference_for_decisionmaking | Machine Learning vs. Causal Inference for Decision-Making]] <a class="yt-timestamp" data-t="00:57:47">[00:57:47]</a>.
*   Judea Pearl's "Causal Inference Primer for Statistics" (a small booklet for understanding DAGs) <a class="yt-timestamp" data-t="00:58:18">[00:58:18]</a>.
*   "A Tale of Two Cultures" paper (discusses differences between statistics and computer science communities) <a class="yt-timestamp" data-t="00:58:37">[00:58:37]</a>.

The message to the [[role_of_assumptions_in_causal_inference | causal inference]] community is to persist in the journey to become better practitioners, as doing science correctly—handling confounding and preserving the time dimension—is crucial for driving better [[causal_inference_and_decision_making | decision-making]] and helping businesses thrive <a class="yt-timestamp" data-t="00:59:43">[00:59:43]</a>.