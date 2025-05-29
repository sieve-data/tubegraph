---
title: Secant lines and their slopes
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

## Understanding the Concept of Slope: A Review
The [[understanding_the_concept_of_slope | idea of slope]] is first introduced in algebra, representing the steepness of a line <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For a straight line, the [[slope_of_a_straight_line | slope]] remains consistent throughout <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Calculating the Slope of a Straight Line
To find the [[finding_the_slope_of_a_line | slope of a line]], two points on the line are selected <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The [[slope_of_a_line_in_algebra | slope in algebra]] is defined as "rise over run" or "change in y over change in x" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

If two points on a line are `(a, f(a))` and `(b, f(b))`, the [[slope_of_a_straight_line | slope]] is calculated as <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>:
*   Change in y: `f(b) - f(a)` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   Change in x: `b - a` <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>

Therefore, the [[slope_of_a_straight_line | slope]] `m` is:
`m = (f(b) - f(a)) / (b - a)` <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>

This formula provides the [[slope_of_a_straight_line | slope]] for the entire line because its [[consistency_in_calculating_slope | slope is consistent]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

#### Example Calculation
For points `(2, 3)` and `(5, 7)` on a line <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>:
*   Change in y: `7 - 3 = 4` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
*   Change in x: `5 - 2 = 3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
The [[slope_of_a_straight_line | slope]] is `4/3` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

## Transition to Curves
When dealing with a curve, the [[slope_of_a_curve | slope of a curve]] is not constant; it changes at every point <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For example, on the curve `y = x^2`:
*   The [[slope_of_a_curve | slope]] is negative on the left side <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   At the origin `(0,0)`, the [[slope_of_a_curve | slope]] is flat (zero) <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   The [[slope_of_a_curve | slope]] becomes positive and increasingly steeper on the right side <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

This changing [[slope_of_a_curve | slope]] means the traditional [[slope_of_a_line_in_algebra | algebraic definition]] needs to be adapted for curves <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. The "slope at a point" on a curve is represented by the [[tangent_line_and_secant_line | tangent line]] at that point <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

## Secant Lines and Their Slope
To find the [[slope_of_a_curve | slope]] of a curve at a single point, we start by using two points, similar to how we find the [[slope_of_a_straight_line | slope of a straight line]] <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

Consider a curve defined by `y = f(x)`:
1.  **First point:** Let's pick a specific point `(x_0, f(x_0))` on the curve <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
2.  **Second point:** We choose a second point that is a small distance `h` away from `x_0`. This point is `(x_0 + h, f(x_0 + h))` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

A line connecting these two points on the curve is called a [[tangent_line_and_secant_line | secant line]] <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. A [[tangent_line_and_secant_line | secant line]] intersects the curve at two points <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

The [[slope_of_a_curve | slope]] of this [[tangent_line_and_secant_line | secant line]] is calculated using the "change in y over change in x" formula <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>:
*   Change in y: `f(x_0 + h) - f(x_0)` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>
*   Change in x: `(x_0 + h) - x_0` <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>

Simplifying the change in x: `(x_0 + h) - x_0 = h` <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

So, the [[slope_of_a_curve | slope]] of the [[tangent_line_and_secant_line | secant line]] is:
`Slope_secant = (f(x_0 + h) - f(x_0)) / h` <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

### From Secant Lines to Tangent Lines (Introduction to Derivatives)
While the [[slope_of_a_curve | slope]] of the [[tangent_line_and_secant_line | secant line]] provides an average [[slope_of_a_curve | slope]] between two points, it does not represent the exact [[slope_of_a_curve | slope]] at a single point <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. To find the [[slope_of_a_curve | slope]] at a specific point `x_0`, we conceptually bring the second point `(x_0 + h, f(x_0 + h))` closer and closer to `(x_0, f(x_0))` <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This means letting `h` approach zero <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

As `h` gets arbitrarily small, the [[tangent_line_and_secant_line | secant line]] becomes a [[tangent_line_and_secant_line | tangent line]] to the curve at the point `x_0` <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. This process involves the concept of a limit in calculus <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

The [[slope_of_a_curve_using_tangent_lines | slope of the tangent line]] at a specific point `x_0` is defined as the limit of the [[slope_of_a_curve | slope]] of the [[tangent_line_and_secant_line | secant line]] as `h` approaches zero <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>:
`f'(x_0) = lim (h→0) [ (f(x_0 + h) - f(x_0)) / h ]` <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>

This expression is known as the **derivative of f** at `x_0`, denoted as `f'(x_0)` <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. The derivative `f'(x)` is itself a function that tells you the [[slope_of_a_curve | slope]] of the curve at any given x-value <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.