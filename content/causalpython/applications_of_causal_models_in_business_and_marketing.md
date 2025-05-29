---
title: Applications of causal models in business and marketing
videoId: zTJFUaLjxfE
---

From: [[causalpython]] <br/> 

[[causality_in_marketing_and_decisionmaking | Causal models]] and [[causality_in_marketing | causal inference]] are becoming increasingly vital for making effective decisions in business and marketing. Scott Muller's work focuses on enabling better decision-making, both at an individual level and for policies affecting large populations, primarily through counterfactual reasoning <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This approach aims to provide the necessary insights to optimize business strategies and outcomes.

## Core Challenges in Decision-Making

A fundamental problem in [[causality_and_causal_models | causal inference]] is that one cannot observe the outcomes for two different treatments on the same individual <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. For instance, it's impossible to observe someone taking medicine and then go back in time to see what would have happened if they hadn't taken it <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. While population-level averages can be estimated in a straightforward way, obtaining precise point estimates or identifying probabilities for counterfactuals at the individual level remains challenging <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

Researchers, including Jin Tian and Judea Pearl, have developed bounds on probabilities of causation, such as probability of necessity, probability of sufficiency, and probability of necessity and sufficiency <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. While these bounds are mathematically proven to be tight, they are often too loose to be useful for basing practical decisions upon <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. The key challenge for Scott Muller's research is to narrow these bounds, ideally to the point of identification, or at least sufficiently to improve the understanding of underlying data-generating processes and enable better decision-making <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. This requires making additional, reasonable assumptions that fit specific scenarios <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Monotonicity Assumption

One helpful assumption is monotonicity, which posits that there is no possibility of harm in a counterfactual sense <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. For example, if a medicine is taken, harm would mean that a toxic element of the medicine prevents recovery, whereas without it, the person would have recovered <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. If the probability of such a negative counterfactual effect is zero (i.e., it's not possible), then monotonicity holds <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

When monotonicity is present, it allows for the point identification of probabilities like the probability of benefit or the probability of necessity/sufficiency <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. However, a significant challenge in applying these methods in practice is knowing whether monotonicity truly exists in a given scenario <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. While it's rare to prove monotonicity from data alone, it is much more feasible to show from data when monotonicity *does not* hold <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Scott Muller, in collaboration with Judea Pearl, has worked on identifying the limits to monotonicity violation, which can further narrow the bounds on counterfactual probabilities even when full identification is not possible <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.

## Bridging the Gap: From Theory to Practice

To make these theoretical advancements more accessible to practitioners, Scott Muller plans to develop software applications and contribute to open-source projects like DoWhy <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. The goal is to translate complex theoretical work into user-friendly software packages with familiar APIs, similar to scikit-learn in general machine learning <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. This would include building graphical user interfaces (GUIs) or integrating solutions into existing popular software packages used by domain experts in fields like econometrics, biology, epidemiology, and marketing <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

## Causal Models in Marketing

Marketing is particularly interested in [[causality_in_marketing | causal inference]] <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. A common practice in internet marketing is A/B testing, where different ads are shown to a randomly split target audience to assess performance <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. However, this method can be "severely suboptimal" <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

### Unit Selection Framework

The unit selection framework, developed by Angley and Judea Pearl, offers a more advanced approach <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. It allows marketers to specify the value or weight placed on four different types of responders to an advertisement (treatment is showing an ad, response is buying the product):

1.  **Complier:** Buys the product if shown the ad, but not if they don't see it <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.
2.  **Always Taker:** Buys the product whether or not they see the ad <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
3.  **Never Taker:** Will not buy the product whether or not they see the ad <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
4.  **Defier:** Will buy the product if they *don't* see the ad, but will *not* buy it if they *do* see the ad (e.g., the ad is offensive or makes them reconsider) <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.

Marketers ideally want to advertise to compliers. While it's generally okay to advertise to always takers and never takers (though cost considerations apply), it's crucial to avoid advertising to defiers, who represent a negative value <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. The framework allows businesses to assign specific values to each responder type based on their strategy <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.

Even though these response types represent individual-level treatment effects that cannot be perfectly identified, the unit selection framework, by plugging in observational and/or experimental data, can provide bounds on the overall value of advertising to a particular subpopulation <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. For example, if advertising to one group yields a value between negative $20 and positive $20, but another group yields between $30 and $35 positive, the latter is clearly the better choice, allowing for a sufficiently better decision <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>.

## Personal Journey and Motivation

Scott Muller's personal journey, from computer science to business and then back to academia to study [[causality_and_causal_models | causality]], reveals a unifying theme: a desire to make better decisions <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. He realized after reading Judea Pearl's "Book of Why" that his previous understanding of business statistics and data interpretation was "novice," and that he had likely made poor decisions in the past despite thinking otherwise <a class="yt-timestamp" data-t="00:37:27">[00:37:27]</a>. This realization motivated him to delve deeply into [[causal_ai_applications_in_business_and_technology | causal inference]], recognizing it as fundamental to human reasoning and crucial for developing human-level AI <a class="yt-timestamp" data-t="00:37:55">[00:37:55]</a>.

His business experience, while not directly providing theorems, offered a practical sense of what constitutes a "reasonable assumption" when trying to narrow bounds or identify counterfactual probabilities <a class="yt-timestamp" data-t="00:44:32">[00:44:32]</a>. This real-world perspective helps him develop assumptions more useful to practitioners in business decision-making <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>.

## Advice for Navigating Challenges

When facing challenges, whether intellectual or business-related, it's crucial to discern when to persevere versus when to pivot or stop entirely <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a>. For decision-making in business, Scott Muller advises learning [[causal_machine_learning_applications_in_various_industries | counterfactual analysis]] <a class="yt-timestamp" data-t="00:53:03">[00:53:03]</a>. In academia, while struggling with ideas is common, recognizing when a path is unproductive is key <a class="yt-timestamp" data-t="00:53:33">[00:53:33]</a>. He notes that for himself, he feels confident in solving problems he believes are solvable, and he won't stop until he finds a solution or confirms it's not possible or within his capability <a class="yt-timestamp" data-t="00:55:11">[00:55:11]</a>.