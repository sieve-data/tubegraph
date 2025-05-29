---
title: Implicit differentiation
videoId: qb40J4N1fa4
---

From: [[3blue1brown]] <br/> 

## Introduction
[[Implicit differentiation]] is a technique used in calculus to find the slope of a tangent line to curves that are not easily expressed as explicit functions, where one variable is isolated in terms of the other <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. This method is particularly useful for "implicit curves" <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

## Understanding Implicit Curves
An implicit curve is defined by an equation relating two or more variables, such as `x^2 + y^2 = 5^2` for a circle with radius 5 centered at the origin <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. In such equations, `x` is not explicitly an input and `y` is not explicitly an output; they are interdependent values related by the equation <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. For these curves, standard [[computing_derivatives_of_functions | derivative]] techniques, which involve finding the size of a tiny nudge to an output caused by a tiny nudge to an input, are not directly applicable <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

The slope of a tangent line to a curve can be found by zooming in close enough that the curve resembles its tangent line, then considering a tiny step along the curve <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. If the y-component of this step is `dy` and the x-component is `dx`, the slope is `dy/dx` <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

### Example: Circle Equation
For a circle defined by `x^2 + y^2 = 5^2` (or 25), to find the slope at a point like (3,4):
1.  Take the [[computing_derivatives_of_functions | derivative]] of both sides of the equation <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.
    *   The derivative of `x^2` becomes `2x dx` <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
    *   The derivative of `y^2` becomes `2y dy` <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.
    *   The derivative of the constant `5^2` (or 25) is `0` <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.
    *   This results in the equation: `2x dx + 2y dy = 0` <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.
2.  Rearrange the equation to solve for `dy/dx` <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.
    *   `2y dy = -2x dx`
    *   `dy/dx = -2x / 2y`
    *   `dy/dx = -x / y` <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
3.  At the point (3,4), the slope would be `-3/4` <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

## Connection to Related Rates Problems
[[Implicit differentiation]] shares a conceptual link with [[calculating_derivatives_and_their_applications | related rates problems]] <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.

### Example: Ladder Problem
Consider a 5-meter ladder against a wall, where the top is 4 meters above ground and the bottom is 3 meters from the wall (by Pythagorean theorem) <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. If the top of the ladder is dropping at 1 meter per second, the question is the rate at which the bottom is moving away from the wall <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.

1.  Define variables: `y(t)` for the height of the ladder's top from the ground, and `x(t)` for the distance of the ladder's bottom from the wall <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.
2.  The relationship is given by the Pythagorean theorem: `x(t)^2 + y(t)^2 = 5^2` <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. This equation holds true at all points in time <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
3.  Take the [[computing_derivatives_of_functions | derivative]] of both sides with respect to time (`t`) <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.
    *   The left side is a function of time, and its [[computing_derivatives_of_functions | derivative]] represents how much the expression changes over a small `dt` <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.
    *   Using the [[chain_rule_in_differentiation | chain rule]]:
        *   `d/dt (x(t)^2)` becomes `2 * x(t) * dx/dt` <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>.
        *   `d/dt (y(t)^2)` becomes `2 * y(t) * dy/dt` <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.
    *   The right side (constant `5^2`) has a derivative of `0` <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.
    *   Resulting equation: `2x(t) dx/dt + 2y(t) dy/dt = 0` <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.
4.  Substitute known values at `t=0`: `y(t)=4`, `x(t)=3`, and `dy/dt = -1` (since it's dropping) <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>.
5.  Solve for `dx/dt`:
    *   `2(3) dx/dt + 2(4)(-1) = 0`
    *   `6 dx/dt - 8 = 0`
    *   `6 dx/dt = 8`
    *   `dx/dt = 8/6 = 4/3` meters per second <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

In the ladder problem, the expressions were functions of time, so taking the [[computing_derivatives_of_functions | derivative]] with respect to time had a clear meaning <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>. In the circle problem, `dx` and `dy` are "floating free," not tied to a common variable like time <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>.

## Interpretation of `dx` and `dy`
To understand `dx` and `dy` in [[implicit differentiation]], consider the expression `s = x^2 + y^2` as a function `s(x,y)` of two variables <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. Taking the derivative of `s` means considering tiny changes `dx` to `x` and `dy` to `y` <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>. The resulting change in `s`, denoted `ds`, is approximately `2x dx + 2y dy` <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>. This expression is a "recipe" for how `x^2 + y^2` changes based on the starting point `(x,y)` and the tiny step `(dx, dy)` <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.

When restricting steps to stay *on the circle*, it means ensuring that the value of `s` (which is 25 for the circle) does not change; `ds` must be `0` <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>. Therefore, setting `2x dx + 2y dy = 0` is the condition for a tiny step to stay on the circle's tangent line <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>. For tiny enough steps, the tangent line and the curve are essentially the same <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>.

## More Complex Examples
[[Implicit differentiation]] can be applied to any equation relating `x` and `y`.
For `sin(x) * y^2 = x` <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>:
1.  Take the [[computing_derivatives_of_functions | derivative]] of each side.
2.  For the left side, `sin(x) * y^2`, use the [[chain_rule_in_differentiation | product rule]] (left d right + right d left):
    *   `sin(x) * (2y dy)` (derivative of `y^2` using [[chain_rule_in_differentiation | chain rule]]) <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>
    *   `+ y^2 * (cos(x) dx)` (derivative of `sin(x)`) <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>
3.  For the right side, `x`, the derivative is `dx` <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.
4.  Equate the changes: `sin(x) (2y dy) + y^2 cos(x) dx = dx` <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.
This equation ensures that the left and right sides change by the same amount if a step stays on the curve <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>. From here, one can algebraically solve for `dy/dx` <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.

## Deriving New Derivative Formulas
[[Implicit differentiation]] is useful for deriving new [[computing_derivatives_of_functions | derivative]] formulas, especially for inverse functions.

### Example: Derivative of Natural Log of x
To find the derivative of `ln(x)`:
1.  Start with `y = ln(x)` <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>.
2.  Rearrange this equation into its equivalent exponential form: `e^y = x` <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.
3.  Take the [[computing_derivatives_of_functions | derivative]] of both sides with respect to `x`:
    *   Left side (`e^y`): using the [[chain_rule_in_differentiation | chain rule]], the derivative is `e^y dy` <a class="yt-timestamp" data-t="13:44:00">[13:44:00]</a>.
    *   Right side (`x`): the derivative is `dx` <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>.
    *   This gives: `e^y dy = dx` <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
4.  Rearrange to solve for `dy/dx`: `dy/dx = 1 / e^y` <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.
5.  Since `e^y = x` (from the original rearrangement), substitute `x` back into the expression: `dy/dx = 1 / x` <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>.
Therefore, the [[computing_derivatives_of_functions | derivative]] of `ln(x)` is `1/x` <a class="yt-timestamp" data-t="14:15:00">[14:15:00]</a>.

## Conclusion
[[Implicit differentiation]] provides a powerful method for [[calculating_derivatives_and_their_applications | calculating derivatives]] for implicitly defined curves. This technique provides a glimpse into [[ordinary_derivatives_versus_partial_derivatives | multivariable calculus]], which involves functions with multiple inputs and how they change when those inputs are tweaked <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. The key is to visualize the tiny nudges and their interdependencies <a class="yt-timestamp" data-t="14:44:00">[14:44:00]</a>.