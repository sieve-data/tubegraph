---
title: Monotonicity assumption in causal models
videoId: zTJFUaLjxfE
---

From: [[causalpython]] <br/> 

The monotonicity assumption in causal inference states that there is no possibility of harm in a counterfactual sense <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. This means that an intervention or treatment cannot negatively impact an outcome that would have been positive had the intervention not occurred <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

## Definition and Example

In essence, monotonicity assumes the absence of a "negative counterfactual effect" at an individual level <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

A concrete example illustrates this:
If a person takes a medicine and recovers from an illness, harm would occur if a toxic element of the medicine prevented recovery, while the person would have recovered naturally if they had *not* taken the medicine <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. If the probability of this "harm" happening is zero, then monotonicity holds <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This assumption is applicable when certain scenarios definitionally preclude harm or when underlying biological mechanisms confirm its impossibility <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Benefits of Monotonicity

When monotonicity is assumed, it greatly aids in [[identifiability_in_causal_representation_learning | identifying]] counterfactual probabilities <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. Specifically, it allows for the point identification of probabilities such as:
*   Probability of benefit <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>
*   Probability of harm (which becomes zero under this assumption) <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>
*   Probability of necessity <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
*   Probability of sufficiency <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>

These specific probabilities are part of the broader category of counterfactual probabilities, for which Judea Pearl and Jin Tian developed bounds <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. While these bounds are mathematically tight, they can often be too loose for practical decision-making <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Making additional [[assumptions_in_causal_inference | assumptions]], like monotonicity, helps narrow these bounds, ideally leading to point identification or sufficient narrowing for better decisions <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Challenges and Scott Muller's Research

The main challenge in applying monotonicity in practice is determining if it holds true for a given scenario <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Assuming it incorrectly can lead to skewed results <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

Scott Muller, in collaboration with Judea Pearl, has explored ways to assess monotonicity from data <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. Their work indicates that while it's "pretty rare" to confirm monotonicity from data alone <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>, it is "much more feasible" to definitively show when monotonicity does *not* hold <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. There is a "relatively good test" to disprove monotonicity and a "weaker test" to indicate its presence, but only under "very particular situations" <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

Even when monotonicity is violated, Muller's research seeks to understand the limits of this violation, allowing for further narrowing of counterfactual probability bounds <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. This means "putting a bound on the bound" to improve decision-making based on available data <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

## Integration into Practice

To make these findings more accessible to practitioners, Scott Muller plans to contribute to open-source libraries like DoWhy <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. The goal is to integrate theorems and formulas, including those related to monotonicity, into user-friendly software packages with familiar APIs, similar to scikit-learn for general machine learning <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. This could enable non-coding domain experts (e.g., in marketing or econometrics) to leverage counterfactual reasoning through graphical user interfaces or integrations into existing popular software <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.

### Unit Selection Framework
One practical application where the concept of harm and its absence (monotonicity) is crucial is the Unit Selection Framework, developed by Angley and Judea Pearl <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. This framework categorizes individuals into four responder types based on their counterfactual responses to a treatment (e.g., seeing an ad):
1.  **Compliers:** Buy the product if shown the ad, but not if not shown the ad <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.
2.  **Always Takers:** Buy the product regardless of seeing the ad <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
3.  **Never Takers:** Do not buy the product regardless of seeing the ad <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.
4.  **Defiers:** Would buy the product if *not* shown the ad, but *not* if shown the ad <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.

The "defier" type represents a violation of monotonicity, as the treatment (showing the ad) leads to a negative outcome (not buying) where no treatment would have led to a positive one (buying) <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>. Knowing the probabilities of these response types and assigning values to them allows marketers to optimize advertising strategies beyond simple AB testing, which can be severely suboptimal <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>.