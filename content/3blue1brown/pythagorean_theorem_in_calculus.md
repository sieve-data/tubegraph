---
title: Pythagorean theorem in calculus
videoId: qb40J4N1fa4
---

From: [[3blue1brown]] <br/> 

The [[proof_and_demonstration_of_the_pythagorean_theorem | Pythagorean theorem]], traditionally stating that the sum of the squares of two legs on a right triangle equals the square of the hypotenuse, finds significant application in calculus, particularly when dealing with implicit curves and related rates problems <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. It often provides the foundational equation that relates interdependent variables.

## Defining Implicit Curves

A common example demonstrating the theorem's role is a circle <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. A circle with radius 5 centered at the origin of the xy-plane is defined by the equation `x^2 + y^2 = 5^2` <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This equation represents all points `(x, y)` on the circle that are a distance of 5 from the origin <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Unlike functions where `y` is explicitly defined as `f(x)`, here `x` and `y` are interdependent values related by an equation <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This is known as an implicit curve <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

## Implicit Differentiation with the Pythagorean Theorem

One application is to find the slope of a tangent line to such a curve, for instance, a circle <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. For an implicit curve, [[calculating_derivatives_and_algebraic_simplification_in_calculus | simple derivative]] rules don't directly apply because `y` is not an output of `x` <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The technique used is called [[calculating_derivatives_and_algebraic_simplification_in_calculus | implicit differentiation]] <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

To find `dy/dx` for `x^2 + y^2 = 5^2`:
1.  Take the derivative of both sides of the equation <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
2.  `x^2` becomes `2x * dx` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
3.  `y^2` becomes `2y * dy` <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
4.  The constant `5^2` (25) becomes `0` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
5.  This results in the differential equation: `2x dx + 2y dy = 0` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
6.  Rearranging to solve for `dy/dx`: `dy/dx = -x/y` <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

For example, at the point `(3, 4)` on the circle, the slope `dy/dx` would be `-3/4` <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### Interpretation of `dx` and `dy`

The presence of `dx` and `dy` floating freely might seem unusual <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Consider `s = x^2 + y^2` as a function of two variables <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. Taking a derivative of `s` means considering a tiny change `dx` to `x` and a tiny change `dy` to `y`, and then asking how much the value of `s` changes (denoted `ds`) <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

The expression `2x dx + 2y dy` is a recipe for how much `x^2 + y^2` changes based on the starting point `(x, y)` and the tiny step `(dx, dy)` <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. When restricting steps to stay *on* the circle, it implies that the value of `s` (which is 25 for the circle) should not change, meaning `ds` must be `0` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Therefore, setting `2x dx + 2y dy = 0` is the condition for a tiny step to stay on the circle's tangent line <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. For infinitesimally small steps, the tangent line and the curve are essentially the same <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

## Related Rates Problems

The Pythagorean theorem is also central to solving [[role_of_linear_algebra_and_calculus_in_geometry | related rates problems]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Consider a 5-meter ladder sliding down a wall, with its top initially 4 meters above the ground and dropping at 1 meter per second <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. By the [[proof_and_demonstration_of_the_pythagorean_theorem | Pythagorean theorem]], the bottom is initially 3 meters from the wall <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

*   Let `y(t)` be the distance from the top of the ladder to the ground (a function of time) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Let `x(t)` be the distance between the bottom of the ladder and the wall (a function of time) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

The key equation relating these terms at any point in time is the [[proof_and_demonstration_of_the_pythagorean_theorem | Pythagorean theorem]]: `x(t)^2 + y(t)^2 = 5^2` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

To find the rate at which `x` is changing (`dx/dt`):
1.  Take the derivative of both sides of `x(t)^2 + y(t)^2 = 5^2` with respect to time `t` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
2.  Using the [[calculating_derivatives_and_algebraic_simplification_in_calculus | chain rule]], `x(t)^2` becomes `2 * x(t) * dx/dt` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
3.  Similarly, `y(t)^2` becomes `2 * y(t) * dy/dt` <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
4.  The derivative of the constant `5^2` is `0` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
5.  This gives the equation: `2x dx/dt + 2y dy/dt = 0` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
6.  At `t=0`, `y(0) = 4` and `x(0) = 3` <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
7.  Given `dy/dt = -1` m/s (dropping) <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
8.  Substitute values: `2(3) dx/dt + 2(4)(-1) = 0` <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
9.  Solve for `dx/dt`: `6 dx/dt - 8 = 0` => `dx/dt = 8/6 = 4/3` m/s <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Connection Between Implicit Differentiation and Related Rates

The structure of the derivatives obtained from the Pythagorean theorem for implicit differentiation (`2x dx + 2y dy = 0`) and related rates (`2x dx/dt + 2y dy/dt = 0`) is remarkably similar <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. In related rates, the derivatives are explicitly with respect to a common variable like time `t` <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. In implicit differentiation, the `dx` and `dy` terms represent tiny nudges in the `x` and `y` directions respectively, not necessarily tied to an external variable like time <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. Both approaches leverage the underlying relationship provided by the Pythagorean theorem to describe how changes in one variable affect the others.