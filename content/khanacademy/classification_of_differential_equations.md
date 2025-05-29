---
title: Classification of Differential Equations
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

This article introduces [[introduction_to_differential_equations | differential equations]], a concept that appears in various fields <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Requests for this topic have come from those studying economics, physics, and engineering, highlighting its [[applications_of_differential_equations_in_various_fields | widely applicable area of study]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## What is a Differential Equation?

A [[definition_and_basic_understanding_of_differential_equations | differential equation]] is an equation that involves an unknown function and its [[understanding_derivatives_in_differential_equations | derivatives]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

For example, `y' + y = x + 3` is a differential equation where `y` is the unknown function <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This can also be written as `dy/dx + y = x + 3` or `f'(x) + f(x) = x + 3` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

Unlike a regular equation, where the [[solutions_to_differential_equations | solution]] is a number or a set of numbers (e.g., `x^2 + cos(x) = sqrt(x)` has numerical solutions) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, the [[solutions_to_differential_equations | solution]] to a [[introduction_to_differential_equations | differential equation]] is a function <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal is to find the function of `x` that satisfies the given equation <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Examples of Solutions

Consider the [[introduction_to_differential_equations | differential equation]]:
`y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>

One claimed [[examples_of_differential_equation_solutions | solution]] is `y1(x) = e^(-3x)` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   `y1' = -3e^(-3x)` <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>
*   `y1'' = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>

Substituting these into the equation:
`9e^(-3x) + 2(-3e^(-3x)) - 3(e^(-3x))` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
`= 9e^(-3x) - 6e^(-3x) - 3e^(-3x)` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
`= 0` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>
This confirms that `y1(x) = e^(-3x)` satisfies the [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

Another [[examples_of_differential_equation_solutions | solution]] is `y2(x) = e^x` <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   `y2' = e^x` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
*   `y2'' = e^x` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>

Substituting these into the equation:
`e^x + 2(e^x) - 3(e^x)` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
`= e^x + 2e^x - 3e^x` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
`= 0` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
This also confirms `y2(x) = e^x` as a [[solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

The [[solutions_to_differential_equations | solution]] to a [[introduction_to_differential_equations | differential equation]] can be a function, a set of functions, or a class of functions <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## Classification of Differential Equations

[[introduction_to_differential_equations | Differential equations]] can be classified in several ways:

### Ordinary vs. Partial Differential Equations

*   **Ordinary Differential Equation (ODE)**: An equation involving one variable and its [[understanding_derivatives_in_differential_equations | derivatives]] <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. The functions and their [[understanding_derivatives_in_differential_equations | derivatives]] are a function of only one variable <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This playlist focuses on ODEs <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Partial Differential Equation (PDE)**: A more complex equation where a function can be a function of more than one variable, involving [[understanding_derivatives_in_differential_equations | derivatives]] with respect to multiple variables (e.g., x, y, and z) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### Order of a Differential Equation

The order of a [[introduction_to_differential_equations | differential equation]] is determined by the highest [[understanding_derivatives_in_differential_equations | derivative]] present in the equation for the unknown function <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

**Example:**
`x^2 * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
In this equation, the highest [[understanding_derivatives_in_differential_equations | derivative]] is the second derivative (`y''`) <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. Therefore, this is a **second order ordinary [[introduction_to_differential_equations | differential equation]]** <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### [[linear_and_nonlinear_differential_equations | Linear and Nonlinear Differential Equations]]

A [[introduction_to_differential_equations | differential equation]] is considered **linear** if all of the unknown functions and their [[understanding_derivatives_in_differential_equations | derivatives]] are linear <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This means:
*   There are no terms like `y^2` or `(dy/dx)^2` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   The function or its [[understanding_derivatives_in_differential_equations | derivatives]] are not multiplied by themselves or by other functions/derivatives of the unknown function (e.g., no `y * y''`) <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   They *can* be multiplied by the independent variable (e.g., `x * y'`) <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

**Example of a Linear Differential Equation:**
`x^2 * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
This is a second-order linear equation because `y''`, `y'`, and `y` are not multiplied by the function or its [[understanding_derivatives_in_differential_equations | derivatives]] <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

**Examples of Nonlinear Differential Equations:**
*   `x^2 * (y'')^2 = sin(x)` <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>
    This is **nonlinear** because the second [[understanding_derivatives_in_differential_equations | derivative]] (`y''`) is squared <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   `y * y'' = sin(x)` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>
    This is also **nonlinear** because the function `y` is multiplied by its second [[understanding_derivatives_in_differential_equations | derivative]] `y''` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.