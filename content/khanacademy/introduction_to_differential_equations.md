---
title: introduction to differential equations
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

[[introduction_to_differential_equations | Differential equations]] are a widely applicable area of study that appear in various fields, including economics, physics, and engineering <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This playlist will focus on [[introduction_to_differential_equations | differential equations]] due to their usefulness in many disciplines <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## What is a Differential Equation?
A [[introduction_to_differential_equations | differential equation]] is an equation that involves an unknown function and its [[introduction_to_derivatives | derivatives]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Examples
*   `y' + y = x + 3` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   `dy/dx + y = x + 3` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   `f'(x) + f(x) = x + 3` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>

In these examples, the unknown function is `y` (or `y(x)`, or `f(x)`) <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Solutions to Differential Equations
A key [[difference_between_regular_and_differential_equations | difference between regular equations and differential equations]] lies in their solutions <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Regular equations**: The solution is typically a number or a set of numbers (e.g., `x^2 + cos(x) = sqrt(x)` where `x` is a number) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **[[understanding_solutions_of_differential_equations | Differential equations]]**: The solution is a function or a class of functions <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal is to find the function that satisfies the given equation <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### [[verifying_solutions_to_differential_equations | Verifying solutions to differential equations]]
To understand what a solution means, consider the [[introduction_to_differential_equations | differential equation]]:
`y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>

Let's [[verifying_solutions_to_differential_equations | verify]] that `y1(x) = e^(-3x)` is a solution <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>:
1.  **Find the first derivative `y1'`**:
    `y1' = -3e^(-3x)` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>
2.  **Find the second derivative `y1''`**:
    `y1'' = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
3.  **Substitute into the original equation**:
    `9e^(-3x) + 2(-3e^(-3x)) - 3(e^(-3x))` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
    `= 9e^(-3x) - 6e^(-3x) - 3e^(-3x)` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
    `= (9 - 6 - 3)e^(-3x)` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
    `= 0e^(-3x) = 0` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

Since the substitution yields `0`, `y1(x) = e^(-3x)` is indeed a solution <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

Another function, `y2(x) = e^x`, is also a solution to the same [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>:
1.  **Find the first derivative `y2'`**:
    `y2' = e^x` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
2.  **Find the second derivative `y2''`**:
    `y2'' = e^x` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>
3.  **Substitute into the original equation**:
    `e^x + 2(e^x) - 3(e^x)` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
    `= (1 + 2 - 3)e^x` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
    `= 0e^x = 0` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>

This demonstrates that a [[introduction_to_differential_equations | differential equation]] can have multiple solutions, or a class of functions as its solution <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Terminology and Classifications
[[introduction_to_differential_equations | Differential equations]] can be classified in several ways <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### [[ordinary_vs_partial_differential_equations | Ordinary vs. Partial Differential Equations]]
*   **Ordinary Differential Equation (ODE)**: An equation where the functions and their [[introduction_to_derivatives | derivatives]] depend on only one independent variable <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. This playlist will primarily deal with [[ordinary_vs_partial_differential_equations | ordinary differential equations]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Partial Differential Equation (PDE)**: A more complex equation where a function can depend on more than one variable, involving partial [[introduction_to_derivatives | derivatives]] with respect to different variables (e.g., `x`, `y`, and `z`) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### Order of a Differential Equation
The order of a [[introduction_to_differential_equations | differential equation]] is determined by the highest [[introduction_to_derivatives | derivative]] present in the equation <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   **Example**: `x^2 * (d^2y/dx^2) + x * (dy/dx) + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
    *   The highest [[introduction_to_derivatives | derivative]] here is the second [[introduction_to_derivatives | derivative]] (`d^2y/dx^2`) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
    *   Therefore, this is a **second-order** [[introduction_to_differential_equations | ordinary differential equation]] <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### [[linear_vs_nonlinear_differential_equations | Linear vs. Nonlinear Differential Equations]]
A [[introduction_to_differential_equations | differential equation]] is considered [[linear_vs_nonlinear_differential_equations | linear]] if all of the unknown functions and their [[introduction_to_derivatives | derivatives]] are, essentially, linear <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This means:
*   You don't have the function or its [[introduction_to_derivatives | derivatives]] squared (e.g., `y^2` or `(dy/dx)^2`) <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   You don't have the function multiplied by its [[introduction_to_derivatives | derivatives]] (e.g., `y * (d^2y/dx^2)`) <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

*   **Example of a [[linear_vs_nonlinear_differential_equations | linear]] equation**: `x^2 * (d^2y/dx^2) + x * (dy/dx) + 2y = sin(x)` <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>
    *   Here, `d^2y/dx^2`, `dy/dx`, and `y` are not multiplied by themselves or by other [[introduction_to_derivatives | derivatives]] of `y` <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. Coefficients like `x^2` or `x` are allowed because they are independent variables, not the unknown function `y` or its [[introduction_to_derivatives | derivatives]] <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

*   **Example of a [[linear_vs_nonlinear_differential_equations | non-linear]] equation**:
    *   `x^2 * (d^2y/dx^2)^2 = sin(x)` (non-linear due to the squared [[introduction_to_derivatives | derivative]]) <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>
    *   `y * (d^2y/dx^2) = sin(x)` (non-linear due to the function `y` multiplied by its [[introduction_to_derivatives | derivative]]) <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>