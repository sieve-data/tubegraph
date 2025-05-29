---
title: Related rates problems
videoId: qb40J4N1fa4
---

From: [[3blue1brown]] <br/> 

Related rates problems involve scenarios where multiple quantities are interdependent and change over time, and the goal is to determine the rate of change of one quantity given the rates of change of others <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The relationship between these quantities is often expressed through an equation that holds true at all points in time <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Example: The Ladder Problem

Consider a 5-meter long ladder leaning against a wall <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Initially, the top of the ladder is 4 meters above the ground, meaning the bottom is 3 meters from the wall (by the Pythagorean theorem) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   Suppose the top of the ladder is slipping down at a rate of 1 meter per second <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   The question is: What is the rate at which the bottom of the ladder is moving away from the wall at that initial moment? <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>

### Setting up the Problem

1.  **Name the Quantities**:
    *   Let `y(t)` be the distance from the top of the ladder to the ground (a function of time) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   Let `x(t)` be the distance between the bottom of the ladder and the wall (also a function of time) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
    *   The ladder's length is constant at 5 meters <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

2.  **Relate the Quantities**: The key equation is derived from the Pythagorean theorem: `x(t)² + y(t)² = 5²` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This equation is true at all moments in time <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Solving the Problem

One approach to solving a related rates problem is to differentiate the relating equation with respect to time. Since `x(t)` and `y(t)` are functions of time, taking the [[calculating_derivatives_and_algebraic_simplification_in_calculus|derivative]] of both sides means considering how much each side changes as time changes <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

*   The right side of the equation (`5²`) is a constant, so its [[calculating_derivatives_and_algebraic_simplification_in_calculus|derivative]] with respect to time is 0 <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   For the left side, `x(t)² + y(t)²`, we apply the [[calculating_derivatives_and_algebraic_simplification_in_calculus|chain rule]]:
    *   The [[calculating_derivatives_and_algebraic_simplification_in_calculus|derivative]] of `x(t)²` with respect to time is `2 * x(t) * (dx/dt)` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. This represents the rate of change of `x²` caused by the rate of change of `x` <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
    *   Similarly, the [[calculating_derivatives_and_algebraic_simplification_in_calculus|derivative]] of `y(t)²` with respect to time is `2 * y(t) * (dy/dt)` <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

Setting the [[calculating_derivatives_and_algebraic_simplification_in_calculus|derivative]] of both sides equal:
`2x(t) * (dx/dt) + 2y(t) * (dy/dt) = 0` <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
This equation signifies that the overall expression `x² + y²` does not change as the ladder moves <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

### Plugging in Values

At the initial moment (t=0):
*   `y(t)` = 4 meters <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>
*   `x(t)` = 3 meters <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>
*   `dy/dt` = -1 meters/second (negative because the height is decreasing) <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>

Substitute these values into the differentiated equation:
`2(3) * (dx/dt) + 2(4) * (-1) = 0`
`6 * (dx/dt) - 8 = 0`
`6 * (dx/dt) = 8`
`dx/dt = 8/6 = 4/3` meters/second <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

So, the bottom of the ladder is moving away from the wall at a rate of 4/3 meters per second.

## Connection to Implicit Differentiation

The process used to solve related rates problems is closely related to [[calculating_derivatives_and_algebraic_simplification_in_calculus|implicit differentiation]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
In related rates, the variables (e.g., `x` and `y`) are explicitly treated as functions of a common variable (time, `t`), and the [[calculating_derivatives_and_algebraic_simplification_in_calculus|derivative]] is taken with respect to that common variable <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This gives a clear meaning to the resulting rates (e.g., `dx/dt`, `dy/dt`).

In contrast, when finding the slope of a tangent line to an implicit curve (like a circle defined by `x² + y² = 5²`), [[calculating_derivatives_and_algebraic_simplification_in_calculus|implicit differentiation]] involves `dx` and `dy` "floating free," not tied to an external variable like time <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. However, the underlying principle of differentiating both sides of an equation to capture tiny changes that maintain the equation's truth remains the same for both related rates and general [[calculating_derivatives_and_algebraic_simplification_in_calculus|implicit differentiation]] <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.