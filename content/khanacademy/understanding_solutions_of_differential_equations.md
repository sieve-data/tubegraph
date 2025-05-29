---
title: understanding solutions of differential equations
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

This article provides an [[introduction to differential equations | introduction to differential equations]], detailing what they are, how their solutions differ from regular equations, and how to verify potential solutions. It also covers basic classifications of [[introduction to differential equations | differential equations]].

## What is a Differential Equation?

A differential equation is an equation that involves an unknown function and its derivatives <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, an equation like `y' + y = x + 3` is a differential equation <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. In this example, the unknown function is `y` <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This could also be written as `dy/dx + y = x + 3` or `f'(x) + f(x) = x + 3` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

[[introduction to differential equations | Differential equations]] are widely applicable and appear in various fields such as economics, physics, and engineering <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

### [[difference_between_regular_and_differential_equations | Differential versus Algebraic Equations]]

The key [[difference_between_regular_and_differential_equations | difference between regular and differential equations]] lies in their solutions. For a regular equation like `x^2 + cos(x) = sqrt(x)`, the solution is a number or a set of numbers <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. However, for a differential equation, the solution is a function <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal when working with a differential equation is to find what function satisfies the given relationship or equation <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## [[verifying_solutions_to_differential_equations | Verifying Solutions to Differential Equations]]

To understand what a solution to a differential equation means, consider the following example:

`y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>

Let's [[verifying_solutions_to_differential_equations | verify solutions]] to this equation.

### Example Solution 1: `y1(x) = e^(-3x)`

It is claimed that `y1(x) = e^(-3x)` is a solution to the equation <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
To verify this, we need its first and second derivatives:
*   `y1' = -3e^(-3x)` <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>
*   `y1'' = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>

Substitute these into the differential equation:
`9e^(-3x) + 2(-3e^(-3x)) - 3(e^(-3x))` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
`= 9e^(-3x) - 6e^(-3x) - 3e^(-3x)` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
`= (9 - 6 - 3)e^(-3x)` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
`= 0e^(-3x)` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>
`= 0` <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>

Since the substitution results in `0`, `y1(x) = e^(-3x)` satisfies the differential equation <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Example Solution 2: `y2(x) = e^(x)`

Another claimed solution is `y2(x) = e^(x)` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
Its first and second derivatives are:
*   `y2' = e^(x)` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
*   `y2'' = e^(x)` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>

Substitute these into the differential equation:
`e^(x) + 2(e^(x)) - 3(e^(x))` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
`= (1 + 2 - 3)e^(x)` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
`= 0e^(x)` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
`= 0` <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>

This also results in `0`, confirming that `y2(x) = e^(x)` is also a solution to this differential equation <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Nature of Solutions

Unlike regular equations which might have a single numerical solution, the [[solutions_to_first_order_differential_equations | solutions to differential equations]] can be a function, a set of functions, or a class of functions <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. Often, these functions are similar but differ by constants <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

## Classification of Differential Equations

[[introduction to differential equations | Differential equations]] can be classified in several ways:

### [[ordinary_vs_partial_differential_equations | Ordinary vs. Partial Differential Equations]]

*   **[[ordinary_vs_partial_differential_equations | Ordinary Differential Equation (ODE)]]**: This type involves one variable with respect to another variable, or a function with respect to a single independent variable (e.g., `y` with respect to `x`) and its derivatives <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. The unknown function and its derivatives are functions of only one variable <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This playlist focuses on [[ordinary_vs_partial_differential_equations | ordinary differential equations]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Partial Differential Equation (PDE)**: These are more complex, occurring when a function depends on more than one variable, and derivatives are taken with respect to multiple independent variables (e.g., `x`, `y`, and `z`) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

### Order of a Differential Equation

The **order** of a differential equation is defined by the highest derivative that exists within the equation <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

**Example**: `x^2 * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
In this equation, the highest derivative is the second derivative (`y''`) <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. Therefore, this is a **second-order** ordinary differential equation <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### [[linear_vs_nonlinear_differential_equations | Linear vs. Nonlinear Differential Equations]]

A differential equation is considered [[linear_vs_nonlinear_differential_equations | linear]] if all of the unknown functions and their derivatives are "linear" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This means:
*   You do not have terms like `y^2` or `(dy/dx)^2` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   You do not have products of the function and its derivatives, such as `y * y''` <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

**Example of a Linear Differential Equation**:
`x^2 * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
This is a [[linear_vs_nonlinear_differential_equations | linear equation]] because `y''`, `y'`, and `y` are not multiplied by the function itself or its derivatives <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Coefficients like `x^2` and `x` are acceptable because they are independent variables, not the unknown function or its derivatives <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

**Examples of Nonlinear Differential Equations**:
*   `x^2 * (y'')^2 = sin(x)` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
    This is [[linear_vs_nonlinear_differential_equations | nonlinear]] because the second derivative `y''` is squared <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   `y * y'' = sin(x)` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>
    This is [[linear_vs_nonlinear_differential_equations | nonlinear]] because the function `y` is multiplied by its second derivative `y''` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

Having grasped what a differential equation is and what its solution means, the next step is to learn [[solving_differential_equations_using_laplace_transform | how to solve them]] <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.