---
title: Implicit differentiation
videoId: qb40J4N1fa4
---

From: [[3blue1brown]] <br/> 

Implicit differentiation is a technique used in [[calculating_derivatives_and_algebraic_simplification_in_calculus | calculus]] to find the slope of a tangent line to a curve or the rate of change of variables in an equation where one variable is not explicitly defined as a function of the other <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. This method is particularly useful for "implicit curves," which are sets of points (x, y) that satisfy a property written in terms of two variables, x and y <a class="yt-timestamp" data-t="01:52:04">[01:52:04]</a>.

## Finding the Slope of a Tangent Line to a Circle

Consider a circle with radius 5 centered at the origin, defined by the equation x² + y² = 5² <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. To find the slope of a tangent line to this circle, for instance at the point (3,4) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, a direct application of [[calculating_derivatives_and_algebraic_simplification_in_calculus | simple derivatives]] is not possible because the curve is not the graph of a single function <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. X is not an input, and y is not an output; they are interdependent values <a class="yt-timestamp" data-t="01:44:26">[01:44:26]</a>.

The key idea for finding tangent line slopes is to "zoom in" until the curve looks like its tangent line, then consider a tiny step along the curve <a class="yt-timestamp" data-t="01:07:11">[01:07:11]</a>. The y-component of this step is `dy`, and the x-component is `dx`, making the desired slope `dy/dx` <a class="yt-timestamp" data-t="01:17:21">[01:17:21]</a>.

To apply implicit differentiation:
1.  Take the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of both sides of the equation x² + y² = 5² <a class="yt-timestamp" data-t="02:12:12">[02:12:12]</a>.
    *   For x², the derivative is `2x * dx` <a class="yt-timestamp" data-t="02:16:32">[02:16:32]</a>.
    *   For y², the derivative is `2y * dy` <a class="yt-timestamp" data-t="02:19:50">[02:19:50]</a>.
    *   The derivative of the constant 5² is 0 <a class="yt-timestamp" data-t="02:24:25">[02:24:25]</a>.
    *   This yields the equation: `2x dx + 2y dy = 0` <a class="yt-timestamp" data-t="02:46:17">[02:46:17]</a>.
2.  Rearrange the equation to find an expression for `dy/dx` <a class="yt-timestamp" data-t="02:46:17">[02:46:17]</a>.
    *   `2y dy = -2x dx`
    *   `dy / dx = -x / y` <a class="yt-timestamp" data-t="02:51:24">[02:51:24]</a>.

At the point (x, y) = (3, 4), the slope `dy/dx` is -3/4 <a class="yt-timestamp" data-t="02:56:56">[02:56:56]</a>.

## Connection to Related Rates Problems

Implicit differentiation is conceptually linked to "related rates" problems <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.

### Example: The Ladder Problem

Imagine a 5-meter ladder leaning against a wall <a class="yt-timestamp" data-t="03:26:34">[03:26:34]</a>. If the top of the ladder is 4 meters above the ground and is slipping down at 1 meter per second, the bottom is initially 3 meters from the wall <a class="yt-timestamp" data-t="03:30:19">[03:30:19]</a>. The question is, at what rate is the bottom of the ladder moving away from the wall at that moment <a class="yt-timestamp" data-t="03:46:42">[03:46:42]</a>?

1.  Define variables: Let `y(t)` be the distance from the top of the ladder to the ground, and `x(t)` be the distance from the bottom of the ladder to the wall <a class="yt-timestamp" data-t="04:21:49">[04:21:49]</a>.
2.  The relationship is given by the Pythagorean theorem: `x(t)² + y(t)² = 5²` <a class="yt-timestamp" data-t="04:34:01">[04:34:01]</a>. This equation holds true at all times <a class="yt-timestamp" data-t="04:43:40">[04:43:40]</a>.
3.  Take the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of both sides with respect to time (`t`) <a class="yt-timestamp" data-t="05:36:58">[05:36:58]</a>.
    *   The left side `x(t)² + y(t)²` is a function of time <a class="yt-timestamp" data-t="05:17:09">[05:17:09]</a>.
    *   Using the [[taking_derivatives_of_complex_combinations_of_functions | chain rule]]:
        *   `d/dt (x(t)²) = 2 * x(t) * (dx/dt)` <a class="yt-timestamp" data-t="06:08:42">[06:08:42]</a>
        *   `d/dt (y(t)²) = 2 * y(t) * (dy/dt)` <a class="yt-timestamp" data-t="06:27:06">[06:27:06]</a>
    *   The right side, `5²` (a constant), has a [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of 0 <a class="yt-timestamp" data-t="05:53:57">[05:53:57]</a>.
    *   This results in: `2x (dx/dt) + 2y (dy/dt) = 0` <a class="yt-timestamp" data-t="06:35:54">[06:35:54]</a>.
4.  Substitute known values at `t=0`: `y(t) = 4m`, `x(t) = 3m`, and `dy/dt = -1 m/s` (negative because it's dropping) <a class="yt-timestamp" data-t="06:45:51">[06:45:51]</a>.
    *   `2(3) (dx/dt) + 2(4) (-1) = 0`
    *   `6 (dx/dt) - 8 = 0`
    *   `dx/dt = 8/6 = 4/3 meters per second` <a class="yt-timestamp" data-t="07:04:15">[07:04:15]</a>.

In the ladder problem, taking the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] has a clear meaning: it's the rate at which the expression changes as time changes <a class="yt-timestamp" data-t="07:32:04">[07:32:04]</a>. For the circle, the "tiny nudges `dx` and `dy`" are not tied to an external variable like time <a class="yt-timestamp" data-t="07:52:16">[07:52:16]</a>, which initially feels strange <a class="yt-timestamp" data-t="07:43:08">[07:43:08]</a>.

## Interpretation of Implicit Differentiation

To understand the meaning of taking a [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of an expression with multiple variables:

1.  Let `s = x² + y²` <a class="yt-timestamp" data-t="08:03:07">[08:03:07]</a>. This `s` is a function of two variables, `x` and `y` <a class="yt-timestamp" data-t="08:08:11">[08:08:11]</a>. For points on the circle, `s` equals 25 <a class="yt-timestamp" data-t="08:16:38">[08:16:38]</a>.
2.  Taking a [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of this expression means considering a tiny change `dx` to `x` and a tiny change `dy` to `y` <a class="yt-timestamp" data-t="08:34:03">[08:34:03]</a>.
3.  The change in `s`, denoted `ds`, is approximately `2x dx + 2y dy` <a class="yt-timestamp" data-t="09:21:40">[09:21:40]</a>. This formula tells you how much the value of `x² + y²` changes based on your starting point (x,y) and the tiny step (dx, dy) <a class="yt-timestamp" data-t="09:41:43">[09:41:43]</a>.
4.  When you restrict yourself to steps *along the circle*, you are ensuring that the value of `s` does not change; it remains 25 <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.
5.  Therefore, `ds` must be 0 <a class="yt-timestamp" data-t="10:17:34">[10:17:34]</a>.
6.  Setting the expression `2x dx + 2y dy` equal to 0 is the condition for a tiny step to stay on the tangent line of the circle <a class="yt-timestamp" data-t="10:20:23">[10:20:23]</a>. For tiny enough steps, the tangent line and the circle are essentially the same <a class="yt-timestamp" data-t="10:40:02">[10:40:02]</a>.

## Generalizing Implicit Differentiation

Implicit differentiation can be applied to any equation relating `x` and `y`.

### Example: `sin(x)y² = x`

Consider the equation `sin(x)y² = x`, which represents a set of u-shaped curves <a class="yt-timestamp" data-t="10:53:23">[10:53:23]</a>.

1.  Take the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of each side with respect to `x` (implicitly) <a class="yt-timestamp" data-t="11:23:42">[11:23:42]</a>.
    *   For the left side, `sin(x)y²`, apply the [[applying_the_product_rule_in_derivatives | product rule]]: "left d right plus right d left" <a class="yt-timestamp" data-t="11:32:06">[11:32:06]</a>.
        *   `sin(x) * (change to y²)`, which is `sin(x) * 2y dy` <a class="yt-timestamp" data-t="11:39:10">[11:39:10]</a>.
        *   `y² * (change to sin(x))`, which is `y² * cos(x) dx` <a class="yt-timestamp" data-t="11:44:03">[11:44:03]</a>.
    *   For the right side, `x`, the change is simply `dx` <a class="yt-timestamp" data-t="11:52:16">[11:52:16]</a>.
2.  Set the changes of both sides equal to each other to ensure the step stays on the curve <a class="yt-timestamp" data-t="11:59:04">[11:59:04]</a>.
    *   `sin(x) (2y dy) + y² cos(x) dx = dx` <a class="yt-timestamp" data-t="11:59:04">[11:59:04]</a>.
3.  From here, you can algebraically rearrange to find `dy/dx` <a class="yt-timestamp" data-t="12:26:17">[12:26:17]</a>.

## Deriving New Derivative Formulas

Implicit differentiation can also be used to derive new [[calculating_derivatives_and_algebraic_simplification_in_calculus | derivative formulas]].

### Example: Derivative of Natural Logarithm `ln(x)`

To find the [[calculating_derivatives_and_algebraic_simplification_in_calculus | derivative]] of `ln(x)`:
1.  Let `y = ln(x)` <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>. This implicitly defines the curve.
2.  Rearrange the equation using the definition of natural logarithm: `e^y = x` <a class="yt-timestamp" data-t="13:16:16">[13:16:16]</a>.
3.  Take the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of both sides, considering how a tiny step (`dx`, `dy`) changes the value of each side <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.
    *   `d/dx (e^y)` using the [[taking_derivatives_of_complex_combinations_of_functions | chain rule]] is `e^y dy` <a class="yt-timestamp" data-t="13:44:16">[13:44:16]</a>.
    *   `d/dx (x)` is `dx` <a class="yt-timestamp" data-t="13:50:20">[13:50:20]</a>.
4.  Equate the changes to ensure the step stays on the curve: `e^y dy = dx` <a class="yt-timestamp" data-t="13:50:20">[13:50:20]</a>.
5.  Rearrange to solve for `dy/dx`: `dy/dx = 1 / e^y` <a class="yt-timestamp" data-t="13:57:38">[13:57:38]</a>.
6.  Since `e^y` is equal to `x` when on the curve, substitute `x` for `e^y`: `dy/dx = 1 / x` <a class="yt-timestamp" data-t="14:06:17">[14:06:17]</a>.

This demonstrates that the [[calculating_derivatives_and_algebraic_simplification_in_calculus | derivative]] of `ln(x)` is `1/x` <a class="yt-timestamp" data-t="14:24:20">[14:24:20]</a>.

Implicit differentiation is a fundamental concept in [[derivatives_and_integrals | multivariable calculus]] that helps understand how functions with multiple inputs change when those inputs are tweaked <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.