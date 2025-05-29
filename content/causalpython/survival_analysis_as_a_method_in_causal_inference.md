---
title: survival analysis as a method in causal inference
videoId: OvmpcL1CKqM
---

From: [[causalpython]] <br/> 

Ido Lazar, a guest on the Causal Bandits podcast, discusses his journey into causal inference and how it addresses limitations of traditional statistics <a class="yt-timestamp" data-t="01:23:23">[01:23:23]</a>. He shares insights from his work in product analytics, where he applies methods like survival analysis to derive more accurate causal conclusions from complex, time-varying data <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>.

## The Path to Causal Inference

Ido Lazar's career began at ViaSat, a satellite internet company, where he observed that while statisticians ran [[statistics | T-tests]] and identified statistically significant results, these findings often lacked true business meaning <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. He realized that statistics alone was insufficient to answer the most interesting business questions, leading him to seek a "whole parallel kind of dimension to analyzing data" focused on the underlying data generating process rather than just measurement error <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

His first encounter with causal thinking occurred while working on email campaigns to retain customers <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. Initially, the approach was to predict which customers were likely to churn and offer them discounts <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. However, Lazar realized the more pertinent question was not "who will churn?" but "who will respond best to our discount?" <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. Some high-probability churners might be too upset to respond to a small voucher, while satisfied customers might be prompted to consider competitors after receiving one <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>. This highlighted that [[statistical_associations | statistical associations]] are often not what's truly desired for decision-making; rather, understanding how variables in the system would react is key <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

### The Learning Journey

Lazar found that his statistics degree devoted "zero" attention to causal thinking <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. To overcome the complexity and lack of immediate mentorship in the field, he adopted a unique learning strategy <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>. He started writing a blog about causal inference, not for audience engagement, but to force himself to deeply understand the topics <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. This involved:
*   Explaining concepts clearly to others <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>.
*   Creating code examples and real-life simulations to grasp specific models and their practical application <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.
This disciplined approach led to a job offer from Tom Laer, who discovered his blog and hired him to apply causal inference methods in practice <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>.

## Survival Analysis in Product Analytics

Lazar's current work involves providing an analytics platform for product and growth teams, helping them make decisions like optimizing menu ordering or identifying features that drive conversions <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>.

### The Challenge of Confounding in Product Data

A common problem is determining which product features genuinely drive conversions to paid users versus those that are merely adopted by already engaged users <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>. Users who adopt certain features are often more engaged and have higher initial intent, leading to a confound where observed differences in conversion rates might be due to this pre-existing intent rather than the feature itself <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.

Traditional methods of controlling for baseline attributes like country or device are often too coarse, as significant user variations exist even within these categories <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.

### Leveraging Time with Survival Analysis

To address this, Lazar's team uses a method that measures user activity within the app as a [[assumptions_in_causal_inference | proxy]] for initial intent or user personality <a class="yt-timestamp" data-t="16:08:00">[16:08:00]</a>. This allows for a more believable comparison, for example, comparing conversion rates among users who *already* adopted five features and then *additionally* adopted a sixth <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>.

However, dealing with time-varying treatments (feature adoption), time-varying outcomes (conversions), and time-varying confounders (in-app activity) presents [[data_preparation_for_causal_analysis | data organization challenges]] <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>. For instance, if feature adoption and conversion often happen on the same day, traditional classification approaches might discard significant amounts of data, especially cases where the feature was highly effective and led to immediate conversion <a class="yt-timestamp" data-t="19:45:00">[19:45:00]</a>. This discarding is not just about quantity but can also introduce bias <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>.

Lazar highlights **survival analysis** as an underrated and powerful method to overcome these challenges <a class="yt-timestamp" data-t="21:02:00">[21:02:00]</a>. It's a third branch of supervised learning, distinct from classification and regression, that handles both continuous and binary components <a class="yt-timestamp" data-t="21:18:00">[21:18:00]</a>.

```ad-note
"Using survival lets you... solve the problem I was mentioning earlier. You'd go about and use what is called time-varying covariates to encode those instances where users have adopted the feature but haven't converted yet and those instances where users haven't adopted the feature and you would build a survival curve for both groups." <a class="yt-timestamp" data-t="21:36:00">[21:36:00]</a>
```

This approach allows for:
*   An equal footing for both groups in terms of time to convert <a class="yt-timestamp" data-t="22:09:00">[22:09:00]</a>.
*   No need to discard information <a class="yt-timestamp" data-t="22:18:00">[22:18:00]</a>.
*   Modeling behavioral confounders similarly by treating feature adoption as a censored time-to-event target <a class="yt-timestamp" data-t="22:31:00">[22:31:00]</a>.

By preserving the temporal dimension, survival analysis ensures that treatments and confounders are correctly ordered relative to the outcome <a class="yt-timestamp" data-t="23:24:00">[23:24:00]</a>. Collapsing data and eliminating the time dimension can lead to "backwards relationships," where actions that are a *result* of the treatment (mediators) are mistakenly controlled for, thereby biasing the causal estimate downwards <a class="yt-timestamp" data-t="25:38:00">[25:38:00]</a>.

## Cost and Risk in Causal Inference

When considering the [[assumptions_in_causal_inference | assumptions in causal inference]], Lazar views costs (e.g., running Randomized Controlled Trials, consulting subject matter experts) as ultimately boiling down to "man hours" or the time and salary of highly trained individuals <a class="yt-timestamp" data-t="33:40:00">[33:40:00]</a>.

His work focuses on applying causal inference in "low resource environments," which means accepting lower guarantees about what can be definitively concluded from the data <a class="yt-timestamp" data-t="34:48:00">[34:48:00]</a>. He sees causality not as a binary state but as a spectrum, where any improvement towards a more causal estimate is better than relying on plain correlations <a class="yt-timestamp" data-t="35:34:00">[35:34:00]</a>. The goal is to find methods that yield the highest guarantees with the lowest costs <a class="yt-timestamp" data-t="35:56:00">[35:56:00]</a>.

## Practical Applications and [[communication_challenges_in_causal_inference | Communication Challenges]]

Using these methodologies, Lazar's team has helped companies significantly improve operations <a class="yt-timestamp" data-t="36:04:00">[36:04:00]</a>. For example, they helped a golfing app realize the hidden potential of an underused feature by disentangling [[challenges_in_implementing_causal_analysis_in_practice | confounding factors]] like its inaccessible location. This led to the feature being promoted within the product and integrated into the onboarding process, resulting in substantial increases in key performance indicators (KPIs) <a class="yt-timestamp" data-t="36:13:00">[36:13:00]</a>.

The biggest [[challenges_in_implementing_causal_analysis_in_practice | challenge in implementing causal analysis]] is often convincing stakeholders of its value <a class="yt-timestamp" data-t="38:44:00">[38:44:00]</a>. Organizations already collect and use data, so presenting a new way of aggregating it that promises greater value requires careful expectation setting <a class="yt-timestamp" data-t="39:02:00">[39:02:00]</a>. Instead of claiming absolute truth, the aim is to show a higher probability of correctness compared to existing methods <a class="yt-timestamp" data-t="39:56:00">[39:56:00]</a>.

Building trust with stakeholders, especially when results are counterintuitive, is paramount <a class="yt-timestamp" data-t="41:02:00">[41:02:00]</a>. Lazar emphasizes that transparency is a core pillar of his methods:
```ad-tip
"One of the main pillars of every method I develop is that it's completely transparent in the sense that you can see how every calculation that gives you the final answer is derived from your data." <a class="yt-timestamp" data-t="42:35:00">[42:35:00]</a>
```
This transparency allows decision-makers to reproduce results and gain ownership, fostering belief even in difficult situations <a class="yt-timestamp" data-t="42:58:00">[42:58:00]</a>.

## The Future of Causal Inference

Lazar firmly believes the future is "more causal," viewing causality as a spectrum rather than a binary state <a class="yt-timestamp" data-t="43:24:00">[43:24:00]</a>. Adoption rates will vary based on organizational resources; larger entities will utilize state-of-the-art methods for high guarantees, while smaller players might opt for automated services or SaaS solutions with lower guarantees but still more causal conclusions than traditional approaches <a class="yt-timestamp" data-t="43:47:00">[43:47:00]</a>.

The field has been gaining steam since around 2017 with conferences like AIC hosting data hackathons <a class="yt-timestamp" data-t="44:40:00">[44:44:00]</a>. More recently, the rise of [[machine_learning_and_causal_inference_methodologies | Large Language Models (LLMs)]] and their human-like behavior has "opened the door for people believing in things that they might find hard to understand initially," fostering an environment where causal inference is gaining traction beyond academia into industry <a class="yt-timestamp" data-t="45:00:00">[45:00:00]</a>.

## Advice for Aspiring Practitioners

Lazar advises against shortcuts, especially in the age of LLMs, as causal inference demands a deep, meticulous understanding <a class="yt-timestamp" data-t="46:43:00">[46:43:00]</a>. His personal recommendation, based on his own experience, is to:
*   **Start a blog or give lectures/presentations**: This forces a deeper understanding to explain concepts clearly, create simulations, and apply specific examples <a class="yt-timestamp" data-t="48:28:00">[48:28:00]</a>.
*   **Seek work applying causal inference**: Finding a job where these skills are sought after is the "next step in the ladder of getting into the field" <a class="yt-timestamp" data-t="49:49:00">[49:49:00]</a>.

Lazar encourages the causal Python community to persist in their journey, emphasizing that doing science correctly by handling confounding and preserving the time dimension is crucial <a class="yt-timestamp" data-t="59:43:00">[59:43:00]</a>. This is not just a formal exercise but a means to drive better decision-making and help businesses thrive <a class="yt-timestamp" data-t="01:00:37">[01:00:37]</a>.

### Recommended Resources
*   **"Causal Inference Primer for Statistics"** by Judea Pearl: A small, to-the-point booklet for quick understanding of DAGs (Directed Acyclic Graphs) <a class="yt-timestamp" data-t="58:13:00">[58:13:00]</a>.
*   **"A Tale of Two Cultures"**: A paper discussing the differences between the statistics and computer science communities, promoting a hybrid mindset <a class="yt-timestamp" data-t="58:37:00">[58:37:00]</a>.

### Connect with Ido Lazar
*   **LinkedIn**: Connect for discussions and updates <a class="yt-timestamp" data-t="01:00:58">[01:00:58]</a>.
*   **Blog**: erin.io – Features a series of blog posts written over the years <a class="yt-timestamp" data-t="01:01:22">[01:01:22]</a>.