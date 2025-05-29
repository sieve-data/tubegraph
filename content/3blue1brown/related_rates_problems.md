---
title: Related rates problems
videoId: qb40J4N1fa4
---

From: [[3blue1brown]] <br/> 

Related rates problems involve situations where several quantities are changing over time, and the goal is to determine the rate of change of one quantity based on the known rates of change of others <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. The key insight is that the quantities are related by some equation, and by taking the derivative of this equation with respect to time, the relationships between their rates of change can be found <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## The Ladder Problem Example

Consider a classic related rates scenario:
A 5-meter long ladder is leaning against a wall <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
Initially, the top of the ladder is 4 meters above the ground, meaning the bottom is 3 meters away from the wall, as determined by the Pythagorean theorem <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. If the top of the ladder is dropping at a rate of 1 meter per second, the problem asks for the rate at which the bottom of the ladder is moving away from the wall at that initial moment <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Setting Up the Problem
1.  **Define Variables**: Let `y(t)` be the distance from the top of the ladder to the ground (a function of time), and `x(t)` be the distance between the bottom of the ladder and the wall (also a function of time) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
2.  **Establish the Relationship**: The key equation connecting these variables is the Pythagorean theorem, which holds true at all points in time: `x(t)² + y(t)² = 5²` <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
3.  **Knowns and Unknowns (at t=0)**:
    *   `y(0) = 4` meters <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>
    *   `x(0) = 3` meters <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>
    *   `dy/dt = -1` meter per second (negative because the height is decreasing) <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>
    *   `dx/dt = ?` (the unknown rate) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>

### Solving with Derivatives
One approach is to isolate one variable and then take its derivative <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. However, a more direct method involves taking the derivative of the entire equation `x(t)² + y(t)² = 5²` with respect to time (`t`) <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

Since the right side (5²) is a constant, its derivative with respect to time is 0 <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. For the left side, apply the [[calculating_derivatives_and_their_applications | chain rule]]:
*   The derivative of `x(t)²` with respect to `t` is `2 * x(t) * (dx/dt)` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   The derivative of `y(t)²` with respect to `t` is `2 * y(t) * (dy/dt)` <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

So, the differentiated equation becomes:
`2x(t) (dx/dt) + 2y(t) (dy/dt) = 0` <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>

Now, substitute the known values at `t=0`:
`2(3) (dx/dt) + 2(4) (-1) = 0` <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>
`6 (dx/dt) - 8 = 0`
`6 (dx/dt) = 8`
`dx/dt = 8/6 = 4/3` meters per second <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

This means the bottom of the ladder is moving away from the wall at 4/3 meters per second at that instant <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

## Connection to Implicit Differentiation

Related rates problems share a conceptual similarity with [[calculating_derivatives_and_their_applications | implicit differentiation]] <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. In both cases, derivatives are taken on both sides of an equation that relates multiple variables <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

*   **Related Rates**: The variables (like `x` and `y`) are explicitly treated as [[relationship_between_velocity_and_distance_functions | functions]] of a common variable, typically time (`t`). Taking the derivative means finding how the expressions change as time passes <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Implicit Differentiation**: While not explicitly tied to an external variable like time, it asks how a tiny nudge `dx` to `x` and `dy` to `y` impacts an expression, often used to find `dy/dx` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. The core idea is that if an equation holds true, then tiny changes to its left side must equal tiny changes to its right side to maintain equality <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

Both techniques rely on understanding how "tiny nudges" in input variables affect the values of expressions containing those variables, emphasizing the interconnectedness of rates of change <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.