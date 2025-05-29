---
title: Tangent lines and their slopes on curves
videoId: qb40J4N1fa4
---

From: [[3blue1brown]] <br/> 

## Introduction

When first learning calculus, understanding how to find the slope of a tangent line to a curve can be a peculiar concept, especially when dealing with curves not easily defined as simple functions <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The fundamental idea for problems involving tangent line slopes is to [[visualizing_derivatives_using_graphs|zoom in close enough]] to the curve until it essentially appears as its own tangent line <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. At this microscopic scale, a tiny step along the curve has a y-component, `dy`, and an x-component, `dx`, making the desired slope `dy` divided by `dx` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Implicit Curves and Tangent Slopes

Consider a circle with a radius of 5, centered at the origin of the xy-plane, defined by the equation `x² + y² = 5²` <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This equation encapsulates all points on the circle as being a distance of 5 from the origin, based on the Pythagorean theorem <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. If one wants to find the slope of a tangent line to this circle, for example, at the point (3,4) <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### The Problem with Explicit Functions

Unlike many tangent slope problems in calculus, a circle is not the graph of a single function <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This means `x` is not simply an input, and `y` is not merely an output; instead, they are interdependent values related by an equation <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Such a curve is called an *implicit curve*, representing the set of all points (x,y) that satisfy a property written in terms of both variables <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Introducing Implicit Differentiation

To find `dy/dx` for implicit curves, the procedure is to take the derivative of both sides of the equation <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. For `x² + y² = 5²`:
*   The derivative of `x²` becomes `2x * dx` <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   The derivative of `y²` becomes `2y * dy` <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   The derivative of the constant `5²` (which is 25) is `0` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

This results in the equation `2x dx + 2y dy = 0` <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

> [!NOTE] Initial Peculiarity
> This process, known as implicit differentiation, can initially feel strange, particularly the idea of taking a derivative of an expression with multiple variables and the "tacking on" of `dy` and `dx` <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

By rearranging the equation `2x dx + 2y dy = 0`, one can find an expression for `dy/dx` <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. In this case, `dy/dx = -x/y` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. For the point (3,4) on the circle, the slope would be -3/4 <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Related Rates: A Parallel Concept

Implicit differentiation is closely connected to "related rates" problems <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Consider a 5-meter ladder against a wall, with its top initially 4 meters above the ground, making the bottom 3 meters from the wall (by Pythagorean theorem) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. If the top of the ladder is dropping at 1 meter per second, the question is the rate at which the bottom of the ladder moves away from the wall <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

Let `y(t)` be the distance from the top of the ladder to the ground and `x(t)` be the distance from the bottom of the ladder to the wall <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The Pythagorean theorem `x(t)² + y(t)² = 5²` relates these terms and holds true at all points in time <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

By taking the derivative of both sides with respect to time (`t`):
*   The left-hand side `x(t)² + y(t)²` is a function of time, and its derivative with respect to time represents how much the expression changes when a small `dt` of time passes <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   Using the chain rule, the derivative of `x(t)²` is `2 * x(t) * (dx/dt)` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   Similarly, the derivative of `y(t)²` is `2 * y(t) * (dy/dt)` <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   Since `x(t)² + y(t)²` always equals `5²` (a constant), its derivative with respect to time must be `0` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

This leads to the equation `2x (dx/dt) + 2y (dy/dt) = 0` <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. At the start (t=0), `y(t)=4` meters, `x(t)=3` meters, and `dy/dt = -1` m/s (negative because it's dropping) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Plugging these values allows isolating `dx/dt`, which comes out to be 4/3 meters per second <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

The similarity between the ladder problem and the circle tangent problem is striking: both started with `x² + y² = 5²` and involved taking the derivative of each side <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The key difference is that in the ladder problem, `x` and `y` were functions of time, so `dx/dt` and `dy/dt` clearly represented rates of change with respect to time <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. In the circle problem, `dx` and `dy` are "floating free," not tied to an external variable like time <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## Understanding Implicit Differentiation

To interpret `dx` and `dy` in implicit differentiation, consider the expression `s = x² + y²` as a function of two variables <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. It assigns a number `s` to every point (x,y) in the plane <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. For points on the circle, `s` equals 25 <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

Taking a derivative of this expression (`ds`) means considering a tiny change (`dx` to `x` and `dy` to `y`) from a starting point, and asking how much the value of `s` changes <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This change `ds` is approximately `2x dx + 2y dy` <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. This expression serves as a recipe to determine how much `x² + y²` changes based on the starting point (x,y) and the tiny step (dx, dy) taken <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Like all derivatives, this is an approximation that becomes increasingly accurate for smaller `dx` and `dy` <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

The key insight for implicit differentiation is that when you restrict tiny steps to stay *on the circle*, you are essentially stating that the value of `s` (which is `x² + y²`) should not change; it must remain 25 <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Therefore, `ds` must be `0` <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Setting the expression `2x dx + 2y dy = 0` is the condition under which a tiny step remains on the tangent line of the circle, which for tiny steps is essentially the same as staying on the circle itself <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

## Applications of Implicit Differentiation

### Example: Sine and Y-squared Curve

Implicit differentiation applies to any implicitly defined curve, not just circles <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. Consider the equation `sin(x)y² = x` <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. This equation defines a set of u-shaped curves where the value of `sin(x)y²` equals `x` <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.

To find `dy/dx`, take the derivative of both sides.
*   **Left Side (product rule):** The derivative of `sin(x)y²` is `sin(x) * (2y dy) + y² * (cos(x) dx)` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   **Right Side:** The derivative of `x` is `dx` <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

Setting these equal: `sin(x) (2y dy) + y² (cos(x) dx) = dx` <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. This means that for a tiny step (dx, dy) to stay on the curve, the changes to both sides of the equation must be equal <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. From this algebraic expression, one can then solve for `dy/dx` <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

### Deriving New Derivative Formulas (Natural Log)

Implicit differentiation can also be used to derive new derivative formulas <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>. For example, to find the derivative of the natural logarithm `ln(x)`, first define it as an implicit curve: `y = ln(x)` <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. This equation can be rearranged into its exponential form: `e^y = x` <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

Take the derivative of both sides of `e^y = x`, considering how a tiny step (dx, dy) changes each side to stay on the curve:
*   **Left Side:** The derivative of `e^y` is `e^y dy` <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   **Right Side:** The derivative of `x` is `dx` <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

Setting them equal: `e^y dy = dx` <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. Rearranging for `dy/dx` gives `dy/dx = 1 / e^y` <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. Since `e^y` is defined as `x` when on the curve, the slope `dy/dx` is `1/x` <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. This demonstrates that the derivative of `ln(x)` is `1/x` <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

## Conclusion

Implicit differentiation provides a powerful technique for [[finding_intersections_of_tangents|finding tangent line slopes]] on curves that are not easily expressed as explicit functions. This concept offers a sneak peek into multivariable calculus, which deals with functions having multiple inputs and how they change <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. The key remains a clear understanding of the "tiny nudges" at play and their interdependencies <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.