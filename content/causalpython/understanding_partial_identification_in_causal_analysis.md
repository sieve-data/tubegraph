---
title: Understanding partial identification in causal analysis
videoId: Hc3rIGmX59k
---

From: [[causalpython]] <br/> 

## Assumptions in Causal Inference: A Spectrum
Assumptions in [[Causal Inference and Identification]] are not binary (true or false); rather, they exist on a range, like a slider that can be pulled up and down <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This perspective emerged from PhD work led by Ricardo Silva on partial identification <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. [[Causal Inference and Identification]] fundamentally relies on assumptions <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a> <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### The Cost of Assumptions
Assumptions in [[Causal Inference and Identification]] are necessary, but they come with a "cost" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a> <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Randomization** is considered the best assumption for establishing causality, but it is often expensive, costing millions or billions for clinical trials in the pharmaceutical industry <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a> <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Observational studies** may offer "free" assumptions, such as "no unmeasured confounding" <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. However, there's a question of whether money can be spent to reduce the risk that such assumptions are wrong <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   Heavier assumptions often entail a larger risk of being incorrect <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a> <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. The notion of risk is crucial in this framework <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   Spending money to discuss assumptions for observational studies, even if they are empirically unverifiable, can reduce the risk of making wrong assumptions <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a> <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This aligns with the "no free lunch" idea in statistics and machine learning <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Partial Identification vs. Point Identification
Traditionally, [[Causal Inference and Identification]] often focuses on [[Differences between identification and estimation in causal methods | point identification]], where making specific assumptions (e.g., A, B, and C) leads to a single causal effect number <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

However, partial identification offers an alternative where, with some assumptions, one obtains a [[Causal Inference and Identification | causal statement]] or result <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. Instead of a single number, partial identification yields a lower and upper bound on the true causal effect <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. As more assumptions are added, these bounds become tighter and eventually collapse to a single point, representing point identification <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a> <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This flexibility avoids a limiting, binary "all or nothing" approach to causality <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Benefits
This approach offers more flexibility by allowing the exploration of the [[Causal Inference and Identification | causal question]] from different "zoom levels" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. It allows for discussion of more and different assumptions, particularly weaker ones, which are easier to justify when discussing policy or strategies with decision-makers <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a> <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Historical Overview
Partial identification gained traction starting around 1989 with early papers by Robins, and Judea Pearl also discussed similar concepts using a DAG approach <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a> <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Charles Mansky from economics wrote a book on it around 2003, though it didn't immediately gain widespread adoption <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. The field is currently in a "third generation," driven by the frustration with the binary nature of full causal effect estimation versus no estimation <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

## Partial Identification and Sensitivity Analysis
While partial identification can be seen as a form of sensitivity analysis, it is more strictly a rephrasing of a causal model, on which sensitivity analysis can then be performed <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Sensitivity analysis** involves introducing a subjective parameter that is dialed up and down to observe how results change, requiring calibration of that parameter <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a> <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Partial identification** is not inherently subjective by design, although the assumed causal graph might be <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

### Challenges in Adoption
Both partial identification and sensitivity analysis are not widely known or applied in the community despite their power to broaden the action space in [[Causal Inference and Identification]] <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a> <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This lack of adoption is partly due to:
*   **Limited Bandwidth**: People often lack the resources and time to implement these more complex methods after already investing in basic causal effect estimation <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a> <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **Complexity**: Partial identification adds another layer of complexity, not only to understanding but also to running the methods <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a> <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
*   **Informative Bounds**: The bounds generated by partial identification can sometimes be uninformative <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>, though scientists should still report them to provide a comprehensive perspective <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Scalability Issues**: Exact methods for partial identification do not scale well, becoming computationally prohibitive beyond a few nodes or discrete states in a graph <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a> <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. Approximate methods, however, show more practical promise <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

## Practical Application: Synthetic Control at Spotify
Partial identification was applied in a project at Spotify to estimate the [[Causal Inference and Identification | causal effect]] on time series data, such as promoting a song <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a> <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>. The team characterized synthetic control methods using DAGs (directed acyclic graphs), which helped frame the [[Differences between identification and estimation in causal methods | identification]] problem more clearly <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a> <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. They also provided sensitivity analysis by introducing additional parameters into the causal model <a class="yt-timestamp" data-t="00:35:42">[00:35:42]</a>.

## Visualizing Causal Bounds with Polytopes
A "polytope" is a geometric object that can visualize causal bounds <a class="yt-timestamp" data-t="00:47:39">[00:47:39]</a>.
*   Imagine a cube representing a causal problem with its associated assumptions <a class="yt-timestamp" data-t="00:48:30">[00:48:30]</a>.
*   Causal assumptions "slice through" the cube, cutting off parts and lowering the upper bound or raising the lower bound <a class="yt-timestamp" data-t="00:48:38">[00:48:38]</a>.
*   The upper and lower bounds are the maximum and minimum points on the polytope <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a>.
*   When enough assumptions are made, the polytope is "sliced down" so much that the lowest and highest points converge, leading to [[Differences between identification and estimation in causal methods | causal identification]] (a single point) <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a> <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>.
*   The "causal marginal polytope" involves combining different convex "boxes" (polytopes) <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>. Convexity is important for optimization, ensuring that the calculated minimum and maximum bounds are the true bounds <a class="yt-timestamp" data-t="00:49:21">[00:49:21]</a>.

## Importance of Questioning Assumptions
A key takeaway is the importance of questioning every assumption one makes <a class="yt-timestamp" data-t="00:59:35">[00:59:35]</a>. This act of questioning is "cheap" and allows for informed investment in verifying those assumptions <a class="yt-timestamp" data-t="00:59:37">[00:59:37]</a>. One wrong assumption can cause significant damage, while ten well-justified assumptions can be highly beneficial <a class="yt-timestamp" data-t="01:09:44">[01:09:44]</a>. The cost of assumptions is essential for making causal analysis more justifiable and practical <a class="yt-timestamp" data-t="01:12:57">[01:12:57]</a>.