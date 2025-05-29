---
title: Causal inference and its applications
videoId: OvmpcL1CKqM
---

From: [[causalpython]] <br/> 

The Causal Bandits podcast welcomed ILY, a statistician passionate about solving real-world problems. His journey into [[causal_inference_concepts_and_applications | causal inference]] stemmed from a realization that traditional statistics often fall short in answering complex business questions <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

## Limitations of Traditional Statistics
ILY observed early in his career at VSAT, an internet satellite company, that standard statistical measurements like T-tests often didn't make sense <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. While results might be "statistically significant," there was a deeper "dimension to analyzing data that isn't about the uncertainty related with just measurement error but rather about the data generating process that underlies it" <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. He realized that statistics alone were not enough to answer the most interesting business questions <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

## First Encounter with Causal Thinking: The Churn Problem
At VSAT, ILY worked on email campaigns aimed at retaining customers by offering discounts <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. The prevailing approach was to predict which customers were likely to churn and then send discounts to them <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.

However, ILY realized that the core interest wasn't just predicting churn, as many of those customers would churn anyway <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. The crucial question was: "who's going to respond best to our discount?" <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a> This shifted the focus from prediction to understanding the causal effect of the discount <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

Examples of counterintuitive scenarios included:
*   Customers too upset for a small voucher to matter <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   Satisfied customers starting to question their bills upon receiving a discount, potentially leading them to check competitors <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.

This highlighted that "statistical associations is not what we are after most of the time" in [[causal_inference_and_decision_making | decision making]]; instead, it's "that layer of how would variables in the system react" <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

## The Journey to Causal Inference
ILY recognized the complexity of [[causal_inference_methods_and_applications | causal inference methods]] and the lack of readily available expertise or consultants <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>. To gain a deeper understanding and be able to utilize these methods in real-world scenarios, he started writing a blog <a class="yt-timestamp" data-t="06:39:00">[06:39:00]</a>. This forced him to understand topics well enough to explain them clearly and develop code examples and simulations, revealing gaps in his understanding <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>, <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.

This initiative unexpectedly led to a job offer where he could apply [[causal_inference_methods_and_applications | causal inference]] for real <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>. He views working in the field as the next crucial step in mastering it <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>.

### Academic Gap
Despite having a statistics degree, ILY noted that "zero" attention was given to [[causal_inference_concepts_and_applications | causal thinking]] in his studies <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. He finds this surprising in retrospect, as [[causal_inference_concepts_and_applications | causal inference]] is a sub-branch of statistics, working with assumptions and models of the world <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>. Much of the literature, including Rubin's work from the 70s and Pearl's from the 80s, has existed for a while <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>.

While statistical tools were useful, they were "constrained to the statistical associations field and never really touched about the data generating process and how things actually work under the hood in in the real word" <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>.

## Applications and Challenges: Debiasing with Time Domain
ILY works on a product analytics platform helping product managers make decisions, such as understanding which features drive conversions to paid users <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>.

A common problem is comparing conversion rates between users who adopted a feature and those who didn't <a class="yt-timestamp" data-t="13:56:00">[13:56:00]</a>. The challenge is that users who adopt features are often more engaged or had higher initial intent, confounding the results <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>. Differences in conversion might be due to this pre-existing intent rather than the feature itself <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>.

### Leveraging Time-Varying Confounders
To address this, ILY's team measures users' activity within the app as a proxy for their initial intent or personality <a class="yt-timestamp" data-t="16:08:00">[16:08:00]</a>. For example, comparing users who have interacted with at least five features, then observing the difference in conversion rates for those who additionally adopted a specific feature <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>. This makes the comparison more "believable" and less confounded, as all users in this group are already highly engaged <a class="yt-timestamp" data-t="17:07:00">[17:07:00]</a>. User behavior acts as an "equivalent of a personality test" <a class="yt-timestamp" data-t="17:43:00">[17:43:00]</a>.

### The Problem with Collapsing Time and the Solution: Survival Analysis
A significant challenge in measuring the effect of time-varying treatments (feature adoption) and outcomes (conversions) is how to organize the data <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>. If, for instance, both adoption and conversion frequently happen on the first day, a simple classification approach would require discarding a large amount of data to ensure the adoption precedes the conversion <a class="yt-timestamp" data-t="18:31:00">[18:31:00]</a>. This discarding is not only about quantity but also introduces bias, potentially making a strong feature appear ineffective <a class="yt-timestamp" data-t="20:06:00">[20:06:00]</a>, <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>.

The solution is using **Survival Analysis**, an "underrated" third branch of supervised learning alongside classification and regression <a class="yt-timestamp" data-t="21:02:00">[21:02:00]</a>. Survival analysis allows the use of "time-varying covariates" to encode instances where users adopted a feature but haven't converted, or haven't adopted it yet <a class="yt-timestamp" data-t="21:43:00">[21:43:00]</a>. This method preserves the time dimension, avoids discarding information, and provides an equal footing for comparing groups <a class="yt-timestamp" data-t="22:12:00">[22:12:00]</a>. It ensures that the treatment actually happened *before* the outcome and that confounders (user profiles) always precede the treatment <a class="yt-timestamp" data-t="23:51:00">[23:51:00]</a>.

> "When you squash your data and you eliminate the time Dimension then you can get all these backwards relationships that can really bias your your analysis." <a class="yt-timestamp" data-t="26:08:00">[26:08:00]</a>

Specifically, collapsing the time dimension can lead to controlling for "mediators" (actions that are *caused by* the treatment, not preceding it), which biases the effect estimates downwards by blocking the flow of information from treatment to outcome <a class="yt-timestamp" data-t="26:50:00">[26:50:00]</a>, <a class="yt-timestamp" data-t="27:09:00">[27:09:00]</a>. [[Causal inference and identification | Pearl's framework]] highlights how controlling for a mediator removes the "mediation effect," leaving only the "direct effect," while often, the "total effect" is what matters for [[causal_inference_and_decision_making | decision-making]] <a class="yt-timestamp" data-t="27:58:00">[27:58:00]</a>. Keeping the time dimension naturally overcomes this issue <a class="yt-timestamp" data-t="28:30:00">[28:30:00]</a>.

### Limitations: Hidden Confounding
While preserving the time dimension resolves biases like those from mediators, it doesn't necessarily address all issues, such as "hidden confounding" or certain collider biases (e.g., M-bias) <a class="yt-timestamp" data-t="29:15:00">[29:15:00]</a>. If there are no hidden confounders, sorting by time should solve everything, as it prevents controlling for blockers or mediators <a class="yt-timestamp" data-t="30:35:00">[30:35:00]</a>.

## Costs and Risks in Causal Inference
Jacob Zeitler's perspective suggests that [[causal_inference_concepts_and_applications | causal assumptions]] come with a cost <a class="yt-timestamp" data-t="31:49:00">[31:49:00]</a>. For instance, Randomized Controlled Trials (RCTs) offer guarantees against hidden confounding but are costly <a class="yt-timestamp" data-t="31:55:00">[31:55:00]</a>. Consulting subject matter experts to build a complete causal graph is also very costly <a class="yt-timestamp" data-t="32:16:00">[32:16:00]</a>. Conversely, making assumptions about the data-generating process can be risky <a class="yt-timestamp" data-t="32:36:00">[32:36:00]</a>.

ILY views these costs primarily as "man hours" of highly trained individuals or experts <a class="yt-timestamp" data-t="33:40:00">[33:40:00]</a>. His approach is to develop [[causal_inference_methods_and_applications | methods]] that can be utilized in "low resource environments," which means accepting "lower guarantees about what you can say from the data" <a class="yt-timestamp" data-t="34:46:00">[34:46:00]</a>.

> "I always think about causality not as a binary state but rather as a spectrum and as long as you are able to make some estimates somewhat more causal then that's always better than using you know play plain correlations for that matter." <a class="yt-timestamp" data-t="35:34:00">[35:34:00]</a>

He seeks methods that yield the "highest guarantees with the lowest costs" <a class="yt-timestamp" data-t="35:56:00">[35:56:00]</a>.

## Real-World Success: The Golfing App Example
ILY and his team helped a customer with a golfing app that had an underperforming feature <a class="yt-timestamp" data-t="36:13:00">[36:13:00]</a>. Intuitively, one might assume the feature wasn't good <a class="yt-timestamp" data-t="36:30:00">[36:30:00]</a>. However, confounding factors existed, such as the feature's inaccessibility within the product <a class="yt-timestamp" data-t="36:40:00">[36:40:00]</a>.

Using the methodology described (leveraging time and user activity as confounders), they were able to "disentangle all these biases and uncover the reality that that feature had a great potential to drive that users's kpis" <a class="yt-timestamp" data-t="36:57:00">[36:57:00]</a>. Based on their recommendations, the customer moved the feature to a more prominent place and made it part of the onboarding process, leading to significant increases in top-line KPIs <a class="yt-timestamp" data-t="37:13:00">[37:13:00]</a>.

## Main Challenges in Applying Causal Inference
The biggest challenge is not the technical application but convincing stakeholders of the value of [[causal_inference_methods_and_applications | causal inference]] <a class="yt-timestamp" data-t="38:44:00">[38:44:00]</a>. Organizations already collect and use data, so one must persuade them that aggregating data differently will generate significant value <a class="yt-timestamp" data-t="39:02:00">[39:02:00]</a>. This requires setting clear expectations: not claiming absolute truth, but rather demonstrating a "higher probability that it's true or that it's more correct than what they are seeing in their regular data" <a class="yt-timestamp" data-t="39:56:00">[39:56:00]</a>.

### Communication and Transparency
A key driver of trust is the ability to clearly connect the results back to the raw data <a class="yt-timestamp" data-t="41:02:00">[41:02:00]</a>. This is especially vital when delivering counterintuitive results or recommendations that might challenge existing beliefs <a class="yt-timestamp" data-t="41:54:00">[41:54:00]</a>. No matter how rigorous or sophisticated the method, if it cannot be tied back to the data in a transparent way, convincing stakeholders is difficult <a class="yt-timestamp" data-t="42:07:00">[42:07:00]</a>.

ILY emphasizes that every method he develops is "completely transparent," allowing users to see how calculations are derived from their data and even reproduce them <a class="yt-timestamp" data-t="42:41:00">[42:41:00]</a>. This empowers them and gives them ownership of the results <a class="yt-timestamp" data-t="43:05:00">[43:05:00]</a>.

## The Future of Causality
The future of [[causal_inference_methods_and_applications | causal inference]] is seen as increasingly causal, viewed as a spectrum rather than a binary state <a class="yt-timestamp" data-t="43:24:00">[43:24:00]</a>. Adoption will depend on resources: larger organizations will use state-of-the-art methods for high guarantees, while smaller players might use automation or Software-as-a-Service (SaaS) solutions with lower guarantees, but still deriving more causal conclusions <a class="yt-timestamp" data-t="43:41:00">[43:41:00]</a>.

[[Causal inference concepts and applications | Causal inference]] started gaining traction around 2017 with conferences and hackathons <a class="yt-timestamp" data-t="44:40:00">[44:40:00]</a>. The rise of Large Language Models (LLMs) and their human-like behavior has further opened the door for people to believe in complex concepts like causality, accelerating its pickup in the industry beyond academia <a class="yt-timestamp" data-t="45:00:00">[45:00:00]</a>. More business leaders are feeling the need to invest in [[industrial_applications_of_causal_inference | causal inference]] <a class="yt-timestamp" data-t="45:44:00">[45:44:00]</a>.

## Advice for Beginners
For those starting with [[causal_inference_concepts_and_applications | causality]]:
*   **Avoid shortcuts:** Especially in the age of LLMs, [[causal_inference_concepts_and_applications | causal inference]] requires a "very deep level of understanding" through meticulous study <a class="yt-timestamp" data-t="46:43:00">[46:43:00]</a>.
*   **Deep study through explanation:** Reading papers only provides a shallow understanding <a class="yt-timestamp" data-t="47:46:00">[47:46:00]</a>. To truly internalize concepts and see how they behave in different settings, one must try to explain them, for example, by writing a blog, giving lectures, or doing simulation analysis and specific examples <a class="yt-timestamp" data-t="48:51:00">[48:51:00]</a>.
*   **Seek practical application:** The best way to get into any domain is by working in it <a class="yt-timestamp" data-t="50:00:00">[50:00:00]</a>. If a job offers the opportunity to perform such analyses, it's worth pursuing <a class="yt-timestamp" data-t="50:05:00">[50:05:00]</a>.

## Recommended Resources
*   Alex Molak's book (for beginners) <a class="yt-timestamp" data-t="57:47:00">[57:47:00]</a>.
*   [[Causal Inference and Identification | Judah Pearl's]] "Causal Inference Primer for Statistics" <a class="yt-timestamp" data-t="58:13:00">[58:13:00]</a>.
*   "A Tale of Two Cultures" paper (discusses statistics vs. computer science communities, different mindsets) <a class="yt-timestamp" data-t="58:37:00">[58:37:00]</a>.

## Message to the Causal Python Community
It is challenging to justify the use of [[causal_inference_methods_and_applications | causal inference methods]] over simpler ones <a class="yt-timestamp" data-t="59:24:00">[59:24:00]</a>. However, it's "very important to do science correctly" <a class="yt-timestamp" data-t="59:43:00">[59:43:00]</a>. If data is used to drive recommendations without properly handling confounding or accounting for the time dimension, it can "end up hurting the business instead of helping it" <a class="yt-timestamp" data-t="59:56:00">[59:56:00]</a>.

Persistence in becoming better practitioners matters, not just for formality, but because it "will help you drive better [[importance_of_understanding_causal_inference_for_decision_making | decision making]] and ultimately help your business or whatever entity you work for thrive" <a class="yt-timestamp" data-t="01:00:37">[01:00:37]</a>.

## Where to Find ILY
*   **LinkedIn:** Feel free to reach out to connect and chat <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>.
*   **Blog:** erin.io <a class="yt-timestamp" data-t="01:01:22">[01:01:22]</a>.