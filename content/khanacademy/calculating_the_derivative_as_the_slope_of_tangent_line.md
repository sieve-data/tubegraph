---
title: Calculating the derivative as the slope of tangent line
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

## Review of Slope for Straight Lines

The concept of [[understanding_slope_of_a_straight_line | slope of a line]] is first introduced early in algebra [00:00:00]. It's a fundamental idea that bears review [00:00:07].

To [[determining_slope | find the slope]] of a straight line, two points on the line are selected [00:00:36]. If a line is represented by the function `y = f(x)` or `f(x) = mx + b` [00:00:15], and two points are `(a, f(a))` and `(b, f(b))` [00:01:17], the slope can be determined [00:01:42].

The slope is defined as "rise over run" [00:01:56] or, equivalently, "change in y over change in x" [00:02:07].

Using the points `(a, f(a))` and `(b, f(b))`, where `b` has a larger x and y value:
*   The change in y (`Δy`) is `f(b) - f(a)` [00:02:47].
*   The change in x (`Δx`) is `b - a` [00:03:23].

Therefore, the slope is `(f(b) - f(a)) / (b - a)` [00:02:51]. This formula allows for [[finding the slope of a line | calculating the slope]] if the coordinates of two points are known [00:03:31]. This value corresponds to `m` in the equation `f(x) = mx + b` [00:01:50].

### Example of Slope Calculation for a Line
Consider two points on a line: `(2, 3)` and `(5, 7)` [00:03:46].
*   Change in y = `7 - 3 = 4` [00:04:00]
*   Change in x = `5 - 2 = 3` [00:04:10]
*   Slope = `4/3` [00:04:20]

This method comes directly from Algebra 1 [00:03:40].

## Generalizing Slope to Curves: Introduction to Derivatives

Unlike straight lines, the [[introduction_to_slope_of_a_curve | slope of a curve]] is constantly changing [00:05:22]. For instance, with a curve like `y = x^2` [00:05:01], the slope varies:
*   At negative x-values, the slope is negative (downward sloping) [00:05:34].
*   As x approaches zero, the slope becomes less negative [00:05:37].
*   At `x = 0`, the slope is flat (zero), as the horizontal line `y = 0` is [[slope of a curve and tangent lines | tangent to the curve]] at this point [00:05:56].
*   For positive x-values, the slope becomes increasingly positive (upward sloping) [00:06:05].

Since the slope changes at every point along a curve, simply asking "what is the slope for this curve?" is not meaningful; it's different at every point [00:06:37]. The [[slope_of_a_curve_and_tangent_lines | slope of a curve]] at a specific point is defined as the [[slope_of_tangent_line_on_a_curve | slope of the tangent line]] at that point [00:05:28].

## Calculating the Slope of a Curve Using Secant Lines

To [[graph interpretation for slope calculation | find the slope of a curve]] at a single point, we start by taking two points, similar to how we calculate the slope of a line [00:07:34].

Consider a general curve `y = f(x)`:
1.  **First Point:** Let the point of interest be `(x₀, f(x₀))` [00:08:45].
2.  **Second Point:** Choose a second point slightly displaced from the first, `(x₀ + h, f(x₀ + h))` [00:08:22]. Here, `h` represents the horizontal distance between the two points.

The line connecting these two points is called a **secant line** [00:09:27]. The slope of this secant line can be calculated using the familiar formula for the change in y over the change in x [00:10:10]:

**Slope of Secant Line**
$$ \text{Slope} = \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(x_0 + h) - f(x_0)}{(x_0 + h) - x_0} $$
Simplifying the denominator:
$$ \text{Slope of Secant Line} = \frac{f(x_0 + h) - f(x_0)}{h} $$
This expression represents the slope of the line connecting `(x₀, f(x₀))` and `(x₀ + h, f(x₀ + h))` [00:11:57].

## From Secant Line to Tangent Line: The Derivative

To find the [[slope_of_tangent_line_on_a_curve | slope of the tangent line]] at a single point (i.e., the slope of the curve at that point), we need to make the second point infinitesimally close to the first point [00:13:28]. This is achieved by taking the **limit as `h` approaches zero** [00:13:07].

As `h` gets smaller:
*   The second point moves closer to the first point [00:13:13].
*   The secant line connecting the two points more closely approximates the [[slope of a curve and tangent lines | tangent line]] at the original point [00:13:17].

When `h` becomes an "infinitesimally small number," the secant line's slope gets very close to the slope at the point in question [00:13:41].

This crucial step defines the **derivative** of a function, which is the [[definition_and_significance_of_the_derivative | definition and significance of the derivative]] in calculus [00:14:54].

**The Derivative (f'(x))**
The derivative of a function `f(x)` at a specific point `x₀`, denoted as `f'(x₀)`, is given by:
$$ f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} $$
This formula is equal to the [[slope_of_tangent_line_on_a_curve | slope of the tangent line]] at `x₀` [00:14:52]. Sometimes, `Δx` is used instead of `h` to represent the change in x [00:14:20].

The derivative `f'(x)` is itself a function [00:15:10], because the slope of a curve can be different at every x-value [00:15:12]. By applying this formula, one can calculate the slope of the tangent line at any given point on the curve [00:15:27]. This foundational concept is key to [[understanding derivatives in differential equations | understanding derivatives in differential equations]] and further calculus topics [00:15:31].