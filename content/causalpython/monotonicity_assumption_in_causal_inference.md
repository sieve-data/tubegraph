---
title: Monotonicity assumption in causal inference
videoId: zTJFUaLjxfE
---

From: [[causalpython]] <br/> 

The monotonicity assumption is a key concept in [[causal_inference_concepts_and_applications | causal inference]], particularly when dealing with [[understanding_partial_identification_in_causal_analysis | counterfactual probabilities]] and making informed decisions based on data <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. It addresses the fundamental problem of [[causal_inference_concepts_and_applications | causal inference]], which is the inability to observe outcomes for two different treatments on the same individual at the same time <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Definition and Concept
Monotonicity, in the context of [[causal_inference_concepts_and_applications | causal inference]], essentially states that there is no possibility of "harm" in a counterfactual sense <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

Consider a medical example:
*   A patient takes a medicine to treat an illness <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   "Harm" would occur if taking the medicine *prevented* the patient from getting better, but if they had *not* taken the medicine, their own immune system *would have* taken care of the illness <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. This represents a negative counterfactual effect at an individual level <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   If the probability of this specific scenario (negative counterfactual effect) is zero, then the monotonicity assumption holds <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This can be the case if it's definitionally impossible in certain scenarios, or if the underlying biological mechanisms of a medicine are understood to preclude such an outcome <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Benefits of the Monotonicity Assumption
When monotonicity can be assumed, it allows for significant advancements in [[causal_inference_concepts_and_applications | causal analysis]]:
*   **Narrowing Bounds:** While initial bounds on probabilities of causation (e.g., probability of necessity, probability of sufficiency, probability of necessity and sufficiency), developed by Jin Tian and [[Judea_Pearl | Judea Pearl]], are mathematically proven to be tight, they are often "too loose to be useful" for decision-making <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Monotonicity helps to narrow these bounds <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Point Identification:** Ideally, the bounds can be narrowed so much that they become "identified" or "point identified" <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. With monotonicity, it becomes possible to point identify various counterfactual probabilities, such as the probability of benefit, or confirm that the probability of harm is zero <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. This helps in understanding data-generating processes and making better decisions <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Challenges in Application
The main challenge in broadly applying methods that rely on monotonicity is determining if the assumption holds in a given scenario <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **Knowing if it Holds:** It's often difficult to definitively know if monotonicity is present <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Assuming it when it doesn't hold can lead to skewed results <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Disproving vs. Proving:** It is relatively rare to be able to show monotonicity from data alone <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. However, it is much more feasible to show from the data that monotonicity *definitely does not* hold <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. This aligns with the general scientific principle that disproving theories is easier than proving them <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Quantifying Violation:** Even if monotonicity is violated, it's possible to assess the extent of the violation <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. By understanding the limits of the violation, researchers can still narrow the bounds on counterfactual probabilities, even if point identification isn't possible <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This is likened to "putting a bound on the bound" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

## Application in Unit Selection Framework
The monotonicity assumption is relevant to the unit selection framework, which was created by Angley and [[Judea_Pearl | Judea Pearl]] <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. This framework is particularly valuable in marketing contexts, where the goal is to make better advertising decisions beyond traditional A/B testing <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

In a marketing example:
*   **Treatment:** Showing someone an ad <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.
*   **Response:** The person buys the product <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

The unit selection framework identifies four types of responders:
1.  **Complier:** Buys the product if shown the ad, but not if not shown <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. These are the desired targets for advertising <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
2.  **Always Taker:** Buys the product regardless of whether they see the ad <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
3.  **Never Taker:** Does not buy the product regardless of whether they see the ad <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
4.  **Defier:** Buys the product if *not* shown the ad, but *does not* buy if shown the ad <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>. This is the type one wants to avoid advertising to, as the ad actively *harms* the chance of a sale <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. The existence of defiers directly implies a violation of monotonicity (as showing the ad leads to a negative counterfactual effect).

The framework allows marketers to assign a value (positive or negative) to each responder type and make optimal decisions about whom to advertise to <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>. Standard A/B testing, which focuses on average performance, can be "severely suboptimal" compared to strategies that account for these individual response types and their associated values <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>. Even without identifying individual counterfactual probabilities, the framework can provide bounds on the overall value of advertising to certain subpopulations, leading to better decision-making <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.