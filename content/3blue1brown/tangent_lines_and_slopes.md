---
title: Tangent lines and slopes
videoId: qb40J4N1fa4
---

From: [[3blue1brown]] <br/> 

## Introduction to Tangent Lines and Slopes
When learning calculus, a common problem involves finding the slope of a tangent line to a curve <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. This requires zooming in close enough to the curve so it "basically looks just like its own tangent line" <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. A tiny step along the curve can be broken into an x-component, `dx`, and a y-component, `dy` <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. The desired slope is the "rise over run," `dy` divided by `dx` <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

### Implicit Curves
Unlike curves that are direct [[mathematical_functions_and_graphs | graphs]] of functions (e.g., `y = f(x)`), some curves, like a circle, are defined by an equation relating two interdependent variables, `x` and `y` <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. These are called implicit curves, representing "the set of all points `x`, `y` that satisfy some property written in terms of the two variables" <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

For instance, a circle with radius 5 centered at the origin is defined by the equation `x^2 + y^2 = 5^2` <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. This equation encapsulates the Pythagorean theorem, where the sum of the squares of the two legs equals the square of the hypotenuse <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>. If one wants to find the slope of a tangent line to this circle at a point like (3,4), a direct simple [[geometric_interpretation_of_derivatives | derivative]] isn't straightforward because `y` is not explicitly an output of `x` <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

## Implicit Differentiation
The procedure to find `dy/dx` for implicit curves is called implicit differentiation <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. It involves taking the derivative of both sides of the equation <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.

### Example: The Circle
For `x^2 + y^2 = 5^2`:
1.  Take the derivative of each term. `x^2` becomes `2x * dx` <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.
2.  Similarly, `y^2` becomes `2y * dy` <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.
3.  The derivative of the constant `5^2` (or 25) is 0 <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.
4.  This yields `2x dx + 2y dy = 0` <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.
5.  Rearranging the equation to solve for `dy/dx` results in `dy/dx = -x/y` <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.
6.  At the point (3,4), the slope would be -3/4 <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

### Connection to Related Rates Problems
Implicit differentiation is conceptually linked to [[related_rates_problems | related rates problems]] <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. Consider a 5-meter ladder against a wall, where its height `y(t)` and distance from the wall `x(t)` are both functions of time `t` <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>. The relationship is still `x(t)^2 + y(t)^2 = 5^2` <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.

To find how `x` changes with time (`dx/dt`) given how `y` changes (`dy/dt`), one can take the derivative of both sides of the equation with respect to time <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.
*   The derivative of `x(t)^2` is `2x(t) * dx/dt` (by the chain rule) <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>.
*   The derivative of `y(t)^2` is `2y(t) * dy/dt` <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.
*   The derivative of the constant `5^2` is 0.
*   So, `2x dx/dt + 2y dy/dt = 0` <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.

The key difference between related rates and implicit differentiation in the circle problem is that in related rates, `dx` and `dy` are explicitly tied to a common variable (time `dt`) <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>. In implicit differentiation for a curve's slope, `dx` and `dy` are "floating free, not tied to some other common variable" <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>.

### Interpretation of Implicit Differentiation
To understand `2x dx + 2y dy`, one can define the expression `x^2 + y^2` as `s`, which is a function of two variables (`s(x,y)`) <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. Taking a derivative of `s` (represented as `ds`) means considering how `s` changes due to tiny changes `dx` to `x` and `dy` to `y` <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.

The expression `2x dx + 2y dy` is a "recipe for telling you how much the value `x^2 + y^2` changes" based on the starting point `(x,y)` and the tiny step `(dx, dy)` <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>. This is an approximation that becomes increasingly accurate for smaller `dx` and `dy` <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>.

When restricting the step to stay *on the circle*, it means the value of `s` must not change; `ds` should be 0 <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>. Therefore, setting `2x dx + 2y dy = 0` is the condition for a tiny step to stay on the circle's tangent line <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>. For tiny steps, staying on the tangent line is essentially the same as staying on the curve itself <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>.

### Further Examples
1.  **Implicit Curve `sin(x)y^2 = x`**: To find the change, take the derivative of both sides <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.
    *   Left side (using the product rule): `sin(x) * (2y dy) + y^2 * (cos(x) dx)` <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>.
    *   Right side: `dx` <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.
    *   Setting them equal: `sin(x) (2y dy) + y^2 (cos(x) dx) = dx` <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>. This equation ensures that the values of both sides change by the same amount, keeping the step on the curve <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>. From here, `dy/dx` can be algebraically isolated <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.

2.  **Derivative of `ln(x)`**: Implicit differentiation can derive new [[derivative_of_polynomial_functions_using_geometric_visualization | derivative]] formulas <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>.
    *   Start with `y = ln(x)` <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>.
    *   Rearrange it using the definition of natural log: `e^y = x` <a class="yt-timestamp" data-t="13:20:00">[13:20:00]</a>.
    *   Take the derivative of both sides: `e^y dy = dx` <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.
    *   Rearrange for `dy/dx`: `dy/dx = 1 / e^y` <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.
    *   Since `e^y = x` on the curve, `dy/dx = 1/x` <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>. This shows that the derivative of `ln(x)` is `1/x` <a class="yt-timestamp" data-t="14:15:00">[14:15:00]</a>.

Implicit differentiation offers a sneak peek into multivariable calculus, which deals with functions having multiple inputs and how they change with tweaks to those inputs <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. The key is understanding the "tiny nudges" and their interdependencies <a class="yt-timestamp" data-t="14:44:00">[14:44:00]</a>.