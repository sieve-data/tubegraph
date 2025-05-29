---
title: Assumptions in causal inference
videoId: Hc3rIGmX59k
---

From: [[causalpython]] <br/> 

Assumptions are fundamental to [[causal_inference_in_practical_applications | causal inference]] <a class="yt-timestamp" data-t="01:56:48">[01:56:48]</a>. They represent things that are believed in and built faith in for a model or conclusion to work <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

## The Nature of Assumptions
Assumptions are not binary—they are not simply true or false <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, but rather exist as a range, like a slider that can be pulled up and down <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This perspective views assumptions as a spectrum, not an all-or-nothing condition <a class="yt-timestamp" data-t="06:35:48">[06:35:48]</a>. This understanding is crucial because thinking in binary terms (either causality can be done or it cannot) can be very limiting and might lead to discarding potential gains that could be much cheaper than initially assumed <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>.

Instead of a single causal effect number derived from strict assumptions, one can make some assumptions to obtain a causal statement or result <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. This approach allows for discussing assumptions at different levels <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>.

## The Cost of Assumptions
While assumptions are necessary for [[causal_inference_in_practical_applications | causal inference]] <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>, they come with an associated cost that is often ignored <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

For example:
*   **Randomization (e.g., Clinical Trials):** This is considered the "best" assumption for certainty about causal effects <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>, but it is expensive. Clinical trials can cost millions or even billions for the pharmaceutical industry <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
*   **Observational Studies:** Assumptions like "no unmeasured confounding" come for free in observational studies, as they are simply stated and then assumed true <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. However, these assumptions are empirically unverifiable <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

The heavier the assumptions made, the larger the risk taken <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. For instance, assuming no hidden confounding in a purely observational study can be a "heavy" assumption with a higher risk of being wrong, even if the price of obtaining data is lower <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.

### Reducing Risk
Money can be spent to reduce the risk that an assumption is wrong <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. For observational studies, this might involve:
*   **Discussion among experts:** At institutions like Harvard's Public Health School, significant resources are dedicated to discussing assumptions for observational studies <a class="yt-timestamp" data-t="04:17:00">[04:17:19]</a>. This includes paying professors and staff to manage discussions and engage with the public <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. This reduces the risk of making incorrect assumptions <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

This concept aligns with the "no free lunch" idea in statistics and machine learning <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

## Partial Identification and Causal Bounds
The concept of "partial identification" provides a way to approach [[causal_inference_in_practical_applications | causal inference]] when strong assumptions are hard to justify <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. Instead of a single point estimate for a causal effect, partial identification provides a lower and upper bound on the true effect <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>.

As more assumptions are added, these bounds become tighter. They eventually collapse to a single point, which represents point identification <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>. This approach allows for greater flexibility and the use of weaker assumptions, which are easier to justify, especially when communicating with policymakers or companies about strategies <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

*   **History:** Partial identification began around 1989 with early papers by Robins and Pearl <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>. Pearl's DAG (Directed Acyclic Graph) approach is often more intuitive for explaining partial identification <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>. Charles Mansky from economics also wrote a book on it around 2003 <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. Currently, it's experiencing a "third generation" resurgence, driven by the desire for more flexibility and weaker assumptions <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.

*   **Causal Polytopes:** The concept of a "causal marginal polytope" helps visualize causal bounds <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. Imagine a cube representing the causal problem. Each causal assumption slices off parts of the cube, reducing the space. The lowest and highest points on the remaining polytope represent the lower and upper bounds of the causal effect <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. When enough assumptions are made, the polytope is "sliced down" so much that the lowest and highest points meet, resulting in causal identification <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

## Relationship with Sensitivity Analysis
Partial identification can be broadly seen as a form of sensitivity analysis <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>. However, strictly speaking, partial identification is a rephrasing of a causal model <a class="yt-timestamp" data-t="09:45:00">[09:45:00]</a>. Sensitivity analysis, introduced by G imens, typically involves introducing a subjective parameter that is dialed up and down to see how results change <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. Partial identification, by design, is not subjective, though a causal graph assumption might be <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.

### Challenges in Adoption
Despite their power, partial identification and sensitivity analysis are not widely known or applied <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>. This is partly due to:
*   **Lack of bandwidth/resources:** People often lack the time and investment needed to go beyond basic [[causal_inference_and_machine_learning | causal inference]] methods <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.
*   **Complexity:** Partial identification adds another layer of complexity, not just to understand but also to run the methods <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>. Exact methods often do not scale well beyond small graphs (e.g., five nodes) or discrete variable states <a class="yt-timestamp" data-t="13:55:00">[13:55:00]</a>.
*   **Informative Bounds:** The bounds produced by partial identification can sometimes be uninformative, though they should still be reported by scientists to provide the widest perspective <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>.

There is a growing movement towards creating simpler tools and packages (e.g., Tyler VanderWeele's E-value package for sensitivity analysis <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>) to make these methods more accessible <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>.

## Role of Expert Knowledge
Expert knowledge is crucial for refining [[causal_inference_in_practical_applications | causal inference]] models and optimizing experiments <a class="yt-timestamp" data-t="55:59:00">[55:59:00]</a>. It can help:
*   **Building graphs:** Informing structural Bayesian models <a class="yt-timestamp" data-t="55:25:00">[55:25:00]</a>.
*   **Limiting search space:** Reducing the super-exponential search space in causal discovery <a class="yt-timestamp" data-t="55:41:00">[55:41:00]</a>.
*   **Optimal experimentation:** Guiding surrogate models in Bayesian optimization by integrating "physics knowledge" or other domain-specific rules to exclude nonsensical areas in the parameter space <a class="yt-timestamp" data-t="53:03:00">[53:03:00]</a>.

Integrating expert knowledge into models (known as preference elicitation) makes the process smarter <a class="yt-timestamp" data-t="56:08:00">[56:08:00]</a>. However, expert knowledge also comes at a cost (e.g., expensive experts) and can be wrong <a class="yt-timestamp" data-t="56:53:00">[56:53:00]</a>. Bayesian approaches can help overcome incorrect expert knowledge by collecting more true data, but this data collection still incurs a cost <a class="yt-timestamp" data-t="58:26:00">[58:26:00]</a>.

Expert knowledge can continuously impact causal bounds, slicing the polytope and constraining the bounds closer to the true causal effect <a class="yt-timestamp" data-t="57:57:00">[57:57:00]</a>.

## The Causal Hierarchy
The causal hierarchy, or "causal ladder" as named by Pearl <a class="yt-timestamp" data-t="21:33:00">[21:33:00]</a>, is an essential concept that lays out the limitations of what can be done in science <a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>. It helps inquire what is theoretically possible and how assumptions relate to moving up the ladder:
*   **Level 1: Observation:** Purely observational data is cheap and underlies the success of [[causal_inference_and_machine_learning | machine learning]] and big data <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>. You cannot make statements about interventions solely from observational data without making assumptions <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>.
*   **Level 2: Intervention:** Interventional data, like from RCTs, is much more expensive than observational data <a class="yt-timestamp" data-t="23:40:00">[23:40:00]</a>. Even interventional data alone isn't enough to reach counterfactual conclusions <a class="yt-timestamp" data-t="22:43:00">[22:43:00]</a>.
*   **Level 3: Counterfactuals:** Counterfactual data "basically doesn't exist" unless in highly specific scenarios like twin studies, which are still expensive and require assumptions <a class="yt-timestamp" data-t="23:44:00">[23:44:00]</a>. Making statements at this level requires taking on additional, strong assumptions <a class="yt-timestamp" data-t="22:51:00">[22:51:00]</a>.

The cost of [[causal_inference_in_practical_applications | causal assumptions]] increases significantly as one moves up the causal ladder <a class="yt-timestamp" data-t="23:27:00">[23:27:00]</a>.

## Practical Advice on Assumptions
A key message for the [[communication_challenges_in_causal_inference | causal inference]] community is to:
1.  **Question your assumptions first.** <a class="yt-timestamp" data-t="00:1:15">[00:01:15]</a>
2.  **Consider the cost** or "dollar tag" associated with each assumption, as they are not free <a class="yt-timestamp" data-t="00:1:17">[00:01:17]</a>. Some assumptions are cheaper, others more expensive <a class="yt-timestamp" data-t="00:1:23">[00:01:23]</a>.
3.  **Think about when experimentation is a good choice.** This is the most realistic perspective, as it helps avoid a world solely relying on purely observational data sets <a class="yt-timestamp" data-t="00:1:28">[00:01:28]</a>. Observational studies can inform trials, but relying on them without considering how an experiment would verify results is problematic <a class="yt-timestamp" data-t="00:1:47">[00:01:47]</a>.

Focusing on the cost of assumptions and using them to "slice the polytope" to achieve more justifiable results will ultimately make [[causal_inference_in_practical_applications | causal inference]] more manageable and reliable <a class="yt-timestamp" data-t="00:1:57">[00:01:57]</a>. This means following the truth and continuously questioning assumptions <a class="yt-timestamp" data-t="00:1:08">[00:01:08]</a>.