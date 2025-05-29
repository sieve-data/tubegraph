---
title: Application of causal AI in marketing and business
videoId: zTJFUaLjxfE
---

From: [[causalpython]] <br/> 

Scott Muller, a guest on the Causal Bandits podcast, discusses his journey from computer science and entrepreneurship to dedicating his full attention to studying [[causal_ai_and_its_application_in_different_sciences | causality]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. He emphasizes the importance of [[advancements_in_causal_modeling_and_ai | causal modeling]] for improving decision-making at both individual and population levels, particularly through counterfactual reasoning <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## Counterfactual Reasoning in Decision-Making

Muller's current research direction focuses on making better decisions based on counterfactual reasoning <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This hits upon a fundamental problem in [[causal_ai_in_business_applications | causal inference]]: it's impossible to observe the outcomes for two different treatments on the same individual simultaneously <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. For example, one cannot observe if a person gets better after taking medicine and also observe what would have happened if they hadn't taken the medicine <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. While this can be estimated at a population level through averages (e.g., randomized control trials) <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, obtaining point estimates for individual counterfactual probabilities is challenging <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

### Bounds on Probabilities of Causation
Jin Tian and Judea Pearl developed bounds on probabilities of causation, such as the probability of necessity (PN), probability of sufficiency (PS), and probability of necessity and sufficiency (PNS) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Although these bounds are mathematically proven to be "tight" (meaning no better bounds can be derived without further assumptions) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, they are often too broad to be useful for practical decision-making <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Muller's work aims to narrow these bounds, ideally to a point where they are "identified" or "point identified" <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. This requires making additional, reasonable assumptions that make sense for a specific scenario <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### The Monotonicity Assumption
One such helpful assumption is monotonicity <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>, which states that there is no possibility of harm in a counterfactual sense <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
For example, if a medicine is taken, it's assumed that it won't prevent recovery if the person would have recovered on their own without the medicine <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. If the probability of such a negative counterfactual effect at an individual level is zero, then monotonicity holds <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. In scenarios where monotonicity applies (either definitionally or due to known underlying mechanisms, as in [[causal_ai_in_medicine | medical applications]]) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, it becomes possible to point identify other counterfactual probabilities, such as the probability of benefit or necessity <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

A challenge for broad [[application_of_causal_methods_in_industry | application]] of these methods is knowing if monotonicity is present <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Muller, in collaboration with Judea Pearl, is working on a paper demonstrating that while confirming monotonicity from data alone is rare <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>, it is more feasible to show when it *definitely does not* exist <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. Even when monotonicity is violated, understanding the limits of that violation can still help narrow the counterfactual probability bounds <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

## Making Causal Methods Accessible

To make research findings more accessible to practitioners, Muller plans to leverage his background in software development <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. He intends to develop applications and software frameworks and contribute to open-source projects like DoWhy, adding his theorems and formulas to their library <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. The goal is to create convenient software packages with familiar APIs, similar to scikit-learn for machine learning, to make it easier for people to apply [[causal_ai_in_business_applications | causal methods]] in production without needing to implement everything from scratch <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

Ultimately, the vision is to build interfaces (e.g., graphical user interfaces or integrations into existing popular software packages) that are accessible to domain experts in fields like econometrics, biology, or marketing, who may not be software development or [[causal_ai_and_machine_learning_intersection | causal inference]] experts <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

## Causality in Marketing

[[causality_in_marketing_and_data_science | Marketing]] is a field with vivid interest in [[causal_ai_in_business_applications | causal inference]] <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. Muller highlights the limitations of traditional A/B testing in internet marketing, which is widely used but can be sub-optimal <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

### Unit Selection Framework
The **Unit Selection Framework**, developed by Angrist and Judea Pearl, offers a more valuable approach for marketers <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. It allows marketers to specify the weight or value they place on four different types of responders to an ad campaign, helping to optimize advertising decisions <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.

The four responder types, in the context of showing an ad (treatment) and a product purchase (response), are:
1.  **Complier**: Buys the product if shown the ad, but would not buy it if not shown the ad <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. (Desired target)
2.  **Always Taker**: Buys the product whether or not they see the ad <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. (Generally okay to advertise to, but ad cost might be a factor)
3.  **Never Taker**: Does not buy the product whether or not they see the ad <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>. (Generally okay to advertise to, but ad cost might be a factor)
4.  **Defier**: Would buy the product if they *don't* see the ad, but will *not* buy it if they *do* see the ad <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>. (Undesired target, potentially offensive ad)

While individual-level treatment effects (like these response types) cannot be identified directly <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>, the framework can provide bounds on the overall value of advertising to a particular subpopulation by plugging in observational and experimental data <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>. This allows marketers to make better decisions by choosing subpopulations with more favorable value bounds, even if the exact value is not identified <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>.

## Journey and Motivation

Scott Muller's career path includes:
*   **Computer Science**: Studied at UCLA, loved the mathematical nature and programming, and creating things through code <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>.
*   **Tech Industry and Entrepreneurship**: Entered the tech world as a software developer, then founded or co-founded several successful businesses <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>. He cherishes the experience of building something great with close colleagues, even through failures <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>.
*   **Return to Academia and Causality**: A lifelong desire to return to academia persisted <a class="yt-timestamp" data-t="00:31:17">[00:31:17]</a>. While running a computer science education company (Code I Loved It), he observed the rise of AI <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>. The dream of Artificial General Intelligence (AGI) and its potential to solve significant world problems (like cancer) was a strong motivator to pursue a PhD in AI <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.
*   **Discovery of Causality**: While preparing for graduate school, he read "The Book of Why" by Judea Pearl <a class="yt-timestamp" data-t="00:34:41">[00:34:41]</a>. This book was a turning point, making him realize his previous naive understanding of statistics and data interpretation <a class="yt-timestamp" data-t="00:37:15">[00:37:15]</a>. He recognized causality as fundamental to human reasoning and crucial for developing human-level AI <a class="yt-timestamp" data-t="00:37:58">[00:37:58]</a>.

Muller believes that the mathematics and science of [[causal_ai_and_its_application_in_different_sciences | causality]] must be "baked in" to machine learning architectures to achieve AGI <a class="yt-timestamp" data-t="00:40:33">[00:40:33]</a>. His current focus is developing expertise in [[causal_ai_in_business_applications | causal inference]] to later apply it to AI architectures <a class="yt-timestamp" data-t="00:41:10">[00:41:10]</a>.

## Business Experience and Causality

Muller's business experience, particularly making decisions based on data, significantly influenced his current work in [[causal_ai_in_business_applications | causality]] <a class="yt-timestamp" data-t="00:43:34">[00:43:34]</a>. Reading "The Book of Why" revealed how he had misinterpreted data and made sub-optimal decisions in the past <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>. This experience instilled in him a better sense of what constitutes a "reasonable assumption" when trying to narrow bounds on probabilities of causation <a class="yt-timestamp" data-t="00:44:32">[00:44:32]</a>. His business background motivates him to come up with assumptions that are more useful to others in practical scenarios <a class="yt-timestamp" data-t="00:45:04">[00:45:04]</a>.

## Advice for Navigating Challenges

For those starting in challenging fields like [[causality_in_marketing_and_data_science | causality]], [[machine_learning_versus_causal_models_in_business | machine learning]], or entrepreneurship, Muller acknowledges the difficulty in universally advising "to keep going" <a class="yt-timestamp" data-t="00:51:36">[00:51:36]</a>. Sometimes, stopping or pivoting is the correct decision if one is headed in a wrong direction <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a>.

His advice for decision-making in the face of obstacles, particularly in business, is to **learn counterfactual analysis** <a class="yt-timestamp" data-t="00:52:51">[00:52:51]</a>. He encourages reading works by other researchers in the field and hopes his contributions will also be valuable <a class="yt-timestamp" data-t="00:53:08">[00:53:08]</a>. For academic challenges, he finds "hard problems" that are high-impact to be very interesting puzzles <a class="yt-timestamp" data-t="00:53:56">[00:53:56]</a>. His personal approach is to pursue problems he feels confident he can solve <a class="yt-timestamp" data-t="00:55:47">[00:55:47]</a>.