---
title: Fundamental concepts of calculus
videoId: WUvTyaaNkzM
---

From: [[3blue1brown]] <br/> 

This article introduces the [[introduction_to_calculus_series | essence of calculus series]], aiming to convey the core of the subject in an accessible format over 10 days <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The goal is to explain where common calculus rules and formulas, like derivative formulas, the product rule, the chain rule, implicit differentiation, and Taylor series, originate, rather than just presenting them for memorization <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a><a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. The approach emphasizes [[visualization_in_calculus | visual understanding]] to make it feel as though one could have invented calculus concepts oneself <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a><a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Uncovering Calculus through Geometry: The Area of a Circle

The initial video explores how the core ideas of calculus can be discovered by deeply considering a specific geometry problem: the area of a circle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a><a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. While the formula (pi times radius squared) might be known, the focus is on understanding its derivation <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Contemplating this problem can lead to insights into three major calculus ideas: [[applications_and_interpretations_of_limits_in_calculus | integrals]], [[introduction_to_derivatives_and_calculus_concepts | derivatives]], and their inverse relationship <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a><a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Slicing a Circle into Rings

Consider a circle with a radius, say 3 <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. One way to find its area is to slice it into many concentric rings <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This approach respects the circle's symmetry, which is often rewarded in mathematics <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a><a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

*   Each ring has an inner radius `r` (between 0 and 3) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   By straightening out a ring, it can be approximated as a rectangle <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a><a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   The width of this approximate rectangle is the ring's circumference, `2 * pi * r` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a><a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   The thickness of the rectangle is denoted as `dr`, representing a tiny difference in radius from one ring to the next (e.g., 0.1) <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a><a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a><a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   The area of this thin rectangle is `2 * pi * r * dr` <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a><a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

This approximation becomes more accurate as `dr` gets smaller, making the top and bottom sides of the unwrapped ring closer in length <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a><a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Summing the Areas and its Visual Representation

To find the circle's total area, one needs to sum the areas of all these thin rings <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a><a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. The inner radius `r` ranges from 0 for the smallest ring to just under 3 for the largest <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

*   The rectangles approximating each ring's area can be visualized upright and side-by-side along an axis <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a><a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   Each rectangle has a thickness `dr` <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   The height of any rectangle above a specific value of `r` is `2 * pi * r`, the circumference of the corresponding ring <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a><a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   This setup naturally leads to visualizing the sum as the area under the graph of `y = 2 * pi * r`, which is a straight line with slope `2 * pi` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a><a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   As `dr` gets smaller, the sum of the rectangles' areas approaches the exact area under the graph <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a><a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

In this case, the area under the graph is a triangle with a base of 3 and a height of `2 * pi * 3` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a><a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. Calculating its area (`1/2 * base * height`) yields `pi * 3^2` <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. For a general radius `R`, the area is `pi * R^2` <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a><a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. This demonstrates how a problem can be solved by reframing it as finding the area under a graph <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a><a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## [[introduction_to_limits_in_calculus | Introduction to Limits]] and [[applications_and_interpretations_of_limits_in_calculus | Integrals]]

This transition from an approximate sum to a precise answer by considering smaller and smaller `dr` values is fundamental to calculus <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a><a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Many problems in math and science can be approximated by summing many small quantities, which then correspond to the area under a graph <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a><a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. An example is calculating the total distance a car travels given its velocity over time, by summing (velocity * tiny change in time) <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a><a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

This leads to a general question: how to find the area under any graph, not just a triangle? <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a><a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>
For instance, finding the area under the graph of `x^2` (a parabola) between `0` and `x` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a><a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. A function `a(x)` that gives this area is called an [[applications_and_interpretations_of_limits_in_calculus | integral]] of `x^2` <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a><a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a><a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. Finding this integral function can be challenging <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a><a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## [[introduction_to_derivatives_and_calculus_concepts | Derivatives]]: Measuring Sensitivity to Change

When faced with a difficult problem like finding an [[applications_and_interpretations_of_limits_in_calculus | integral]], a good strategy is to explore the relationship between the function defining the graph (e.g., `x^2`) and the function giving the area (`a(x)`) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a><a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a><a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

*   Consider a tiny increase in `x` by `dx` <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   The resulting change in area, `da`, can be approximated as a thin rectangle with height `x^2` and width `dx` <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a><a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a><a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   This approximation becomes more accurate as `dx` gets smaller <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   This implies `da` is approximately `x^2 * dx`, or `da / dx` is approximately `x^2` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a><a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a><a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

This ratio `da / dx` is called the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of `a` <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a><a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. More technically, the derivative is what this ratio approaches as `dx` becomes infinitesimally small <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a><a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. The derivative measures how sensitive a function's output is to small changes in its input <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.

## The [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]]

Derivatives are crucial for solving [[applications_and_interpretations_of_limits_in_calculus | integral]] problems <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a><a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. If one knows that the derivative of a mystery function `a(x)` is `x^2`, calculus provides tools to "reverse engineer" what `a(x)` must be <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a><a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a><a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

This reciprocal relationship, where the derivative of a function representing the area under a graph gives back the original function defining the graph, is known as the [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a><a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a><a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a><a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. It unifies [[applications_and_interpretations_of_limits_in_calculus | integrals]] and [[introduction_to_derivatives_and_calculus_concepts | derivatives]], showing them as inverse operations <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a><a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

## Conclusion

This exploration provides a high-level overview and a glimpse into the core ideas of calculus <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a><a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. The series aims to delve into the details of [[introduction_to_derivatives_and_calculus_concepts | derivatives]], [[applications_and_interpretations_of_limits_in_calculus | integrals]], and more, encouraging viewers to feel as if they could have developed these concepts through their own [[visualization_in_calculus | visual]] explorations <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a><a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a><a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.

## Acknowledgements

Special thanks are extended to the Patreon supporters who provide financial backing and offer suggestions during the series' development, often gaining early access to videos <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a><a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a><a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. New videos remain ad-free for their first month as a token of gratitude to the community <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a><a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.