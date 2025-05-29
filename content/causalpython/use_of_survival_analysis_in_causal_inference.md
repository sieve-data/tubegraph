---
title: Use of survival analysis in causal inference
videoId: OvmpcL1CKqM
---

From: [[causalpython]] <br/> 

Ialy, a guest on the Causal Bandits podcast, emphasizes the limitations of traditional statistical approaches for answering complex business questions and highlights the importance of [[causal_inference_concepts_and_applications | causal thinking]] to understand the underlying data generating process <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. His early career experiences revealed that statistical significance alone often doesn't adequately explain real-world phenomena <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.

## Limitations of Traditional Statistical Approaches

Ialy recounts how at Viasat, a satellite internet company, initial efforts to model customer churn focused on predicting *who* would churn <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. However, it was realized that many customers would churn regardless, leading to the key insight: the goal should be to identify *who would respond best* to a discount, not just who was likely to churn <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. This distinction between prediction and intervention highlights the need for [[causal_inference_and_its_applications | causal thinking]] <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

Traditional statistical associations are often insufficient for decision-making because they don't explain how variables in a system will react to interventions <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>. A significant [[challenges_in_causal_inference_and_statistical_analysis | challenge in causal inference]] is controlling for all possible confounders, which is particularly difficult in "open" systems like marketing campaigns or political science research, compared to more isolated systems like manufacturing processes <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>.

### The Freemium Product Conversion Problem

Ialy details a common business problem: understanding which product features drive conversions in a freemium model <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>. Companies often compare conversion rates between users who adopted a feature and those who didn't <a class="yt-timestamp" data-t="13:58:00">[13:58:00]</a>. The problem is that users who adopt features are often more engaged or had higher initial intent, creating a strong confounder <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>. Basic baseline attributes like country or device are too coarse to control for this inherent user personality or preference <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>.

## Debiasing with the Time Domain and Survival Analysis

To address the confounding issue, Ialy's work utilizes users' activity within the app as a proxy for their initial intent or personality <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>. This allows for stronger debiasing of results <a class="yt-timestamp" data-t="16:34:00">[16:34:00]</a>. For example, comparing conversion rates among users who *already* adopted at least five features makes the causal effect of an *additional* feature more believable, as both groups have demonstrated high initial intent <a class="yt-timestamp" data-t="17:07:00">[17:07:00]</a>.

A key methodology employed is **Survival Analysis** <a class="yt-timestamp" data-t="21:02:00">[21:02:00]</a>. This technique is particularly useful for measuring the effect of time-varying treatments (feature adoption), time-varying outcomes (conversions), and time-varying confounders (in-app activity) <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>.

### Challenges with Traditional Classification for Time-Varying Data

In standard classification problems, one might attempt to define time frames (e.g., first-day adoptions vs. conversions after the first day) to ensure the treatment precedes the outcome <a class="yt-timestamp" data-t="19:07:00">[19:07:00]</a>. However, this approach leads to significant data loss <a class="yt-timestamp" data-t="19:45:00">[19:45:00]</a>. For instance, if a feature is very effective and conversion happens quickly after adoption (e.g., both on the first day), these cases might be discarded because they don't fit the predefined time windows <a class="yt-timestamp" data-t="20:10:00">[20:10:00]</a>. This biased discarding of information can lead to misinterpretations, making a strong feature appear ineffective <a class="yt-timestamp" data-t="20:34:00">[20:34:00]</a>.

### Survival Analysis as a Solution

Survival analysis is described as an "underrated" third branch of supervised learning (alongside classification and regression) that handles both continuous and binary parts of data <a class="yt-timestamp" data-t="21:02:00">[21:02:00]</a>. It solves the data discarding problem by using **time-varying covariates** to encode instances where users have adopted a feature but haven't yet converted, or haven't adopted it at all <a class="yt-timestamp" data-t="21:43:00">[21:43:00]</a>. By building survival curves for different groups and comparing their conversion rates at the end of a period, both groups are put on an equal footing in terms of time to convert, without discarding any information <a class="yt-timestamp" data-t="22:09:00">[22:09:00]</a>.

This method also allows for modeling behavioral confounders, such as user activity, in the same manner. By treating feature adoption as a censored time-to-event target and using app usages as covariates, one can identify user profiles that quickly adopt features versus those that don't <a class="yt-timestamp" data-t="22:34:00">[22:34:00]</a>.

## Preserving the Time Dimension for Causal Validity

The core idea is to preserve as much temporal information as possible to gain more accurate estimates and avoid controlling for irrelevant variables <a class="yt-timestamp" data-t="23:24:00">[23:24:00]</a>. The data structure ensures that the treatment always precedes the outcome, and confounders always precede the treatment adoption <a class="yt-timestamp" data-t="23:51:00">[23:51:00]</a>. This allows for a millisecond-precise description of a user's journey, encoding the timeline itself rather than collapsing it <a class="yt-timestamp" data-t="24:28:00">[24:28:00]</a>.

Collapsing data and eliminating the time dimension can lead to "backwards relationships" and biased analysis <a class="yt-timestamp" data-t="26:08:00">[26:08:00]</a>. For instance, controlling for user actions that are *a result of* the treatment (e.g., increased app usage due to a good feature) would incorrectly bias the treatment effect estimate downwards <a class="yt-timestamp" data-t="26:21:00">[26:21:00]</a>. This is known as controlling for a "mediator" or "blocker" in Pearl's language, which incorrectly blocks the flow of information from the treatment to the outcome and removes the mediation effect <a class="yt-timestamp" data-t="27:01:00">[27:01:00]</a>. From a decision-making standpoint, the total effect (direct + mediated) is usually what matters <a class="yt-timestamp" data-t="28:16:00">[28:16:00]</a>.

### Limitations: Hidden Confounding

While preserving the time dimension resolves many biases like those caused by mediators, it does not fully address issues like hidden confounding <a class="yt-timestamp" data-t="30:05:00">[30:05:00]</a>. For example, in an M-bias scenario (where two variables connected through a collider node confound a relationship), simply knowing the time order isn't always enough <a class="yt-timestamp" data-t="29:02:00">[29:02:00]</a>. If there are unobserved confounders, further framework development is needed <a class="yt-timestamp" data-t="30:18:00">[30:18:00]</a>. However, assuming no hidden confounders (a common practical assumption), sorting by time can resolve most issues related to blockers <a class="yt-timestamp" data-t="30:35:00">[30:35:00]</a>.

## Practical [[Industrial applications of causal inference | Applications]] and Challenges

Ialy works on projects that help companies make better decisions, often in low-resource environments <a class="yt-timestamp" data-t="34:46:00">[34:46:00]</a>. He views [[causal_inference_concepts_and_applications | causality]] not as a binary state but as a spectrum, aiming to make estimates "somewhat more causal" than plain correlations <a class="yt-timestamp" data-t="35:34:00">[35:34:00]</a>.

### Case Study: Golfing App

His team applied these methods to a golfing app with a feature that had low user adoption <a class="yt-timestamp" data-t="36:13:00">[36:13:00]</a>. Intuitively, it seemed like a poor feature. However, using the time-domain debiasing methodology, they disentangled the biases (e.g., inaccessibility of the feature) and uncovered that the feature had great potential to drive user KPIs <a class="yt-timestamp" data-t="36:57:00">[36:57:00]</a>. By recommending pushing the feature into the onboarding process, the company saw significant increases in their top-line KPIs <a class="yt-timestamp" data-t="37:13:00">[37:13:00]</a>.

### Main Challenges

The biggest [[challenges_and_methodologies_in_causal_inference | challenge in applying causal inference methods]] is not technical, but rather convincing organizations of their value <a class="yt-timestamp" data-t="38:44:00">[38:44:00]</a>. Companies already use data for decision-making, and introducing a new, complex way of aggregating it requires demonstrating tangible value <a class="yt-timestamp" data-t="39:09:00">[39:09:00]</a>. This involves setting expectations correctly, comparing the work to existing association-based methods rather than an ideal truth, and emphasizing transparency <a class="yt-timestamp" data-t="39:56:00">[39:56:00]</a>. Ialy ensures his methods are transparent, allowing stakeholders to see how every calculation is derived from their data and reproduce the results, fostering trust and ownership <a class="yt-timestamp" data-t="42:41:00">[42:41:00]</a>.

## The Future of Causal Inference

Ialy sees the future as definitely more causal, operating on a spectrum <a class="yt-timestamp" data-t="43:24:00">[43:24:00]</a>. Larger organizations with more resources will use state-of-the-art methods for high guarantees, while smaller players might rely on automation or SaaS solutions that provide lower guarantees but still more [[causal_inference_methods_and_applications | causal conclusions]] than traditional correlations <a class="yt-timestamp" data-t="43:47:00">[43:47:00]</a>. He notes that [[causal_inference_concepts_and_applications | causal inference]] started gaining traction around 2017 with AIC conferences and hackathons, and the rise of LLMs (large language models) has further opened the door for people to believe in complex, intelligent machine behaviors, boosting awareness and investment in the field <a class="yt-timestamp" data-t="44:40:00">[44:40:00]</a>.

## Advice for Aspiring Causal Practitioners

Ialy advises against shortcuts, especially in the age of LLMs, as [[causal_inference_concepts_and_applications | causal inference]] requires a deep, meticulous understanding <a class="yt-timestamp" data-t="46:43:00">[46:43:00]</a>. His personal strategy was to start a blog in 2019, where he was forced to understand topics well enough to explain them clearly, often through code examples and simulations <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. Writing and teaching (like giving lectures or blogging) forces a deeper engagement with the material, helping to identify gaps in understanding and explore how methods behave in different settings <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>. The next step, he suggests, is to find a job where one is expected to apply these skills, as practical application is crucial for mastering the field <a class="yt-timestamp" data-t="49:49:00">[49:49:00]</a>.

For resources, he recommends:
*   Alex's book, which is good for beginners <a class="yt-timestamp" data-t="57:47:00">[57:47:00]</a>.
*   Judea Pearl's "Causal Inference Primer for Statistics," a small booklet for understanding DAGs (Directed Acyclic Graphs) <a class="yt-timestamp" data-t="58:13:00">[58:13:00]</a>.
*   The paper "A Tale of Two Cultures," which discusses the differences between the statistics and computer science communities <a class="yt-timestamp" data-t="58:37:00">[58:37:00]</a>.

His core message to the causal Python community is to persist in doing "science correctly." This means handling confounding and preserving the time dimension to avoid hurting the business with biased recommendations <a class="yt-timestamp" data-t="59:43:00">[59:43:00]</a>. Applying [[causal_inference_methods_and_applications | causal inference methods]] is not just about formality but about driving better, ultimately more valuable decision-making for businesses <a class="yt-timestamp" data-t="01:00:34">[01:00:34]</a>.

## Personal Philosophy

Ialy's background in cello (instilling focus and concentration) and political science (cultivating a desire for positive change) influences his work <a class="yt-timestamp" data-t="52:12:00">[52:12:00]</a>. He believes that by helping companies make better data-driven decisions, he contributes to shaping the reality around us and advancing societal progress <a class="yt-timestamp" data-t="53:40:00">[53:40:00]</a>. His mentor, Elad Cohen, taught him the paramount importance of producing measurable business value, prioritizing it over "shiny algorithms" or job titles <a class="yt-timestamp" data-t="00:50:49">[00:50:49]</a>.