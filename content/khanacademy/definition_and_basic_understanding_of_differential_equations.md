---
title: Definition and Basic Understanding of Differential Equations
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

[[introduction_to_differential_equations | Differential equations]] are a widely applicable area of study that appear in various fields <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. They are fundamental in fields like economics <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, physics <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>, and engineering <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This article serves as an [[introduction_to_differential_equations | introduction to differential equations]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## What is a Differential Equation?

A [[introduction_to_differential_equations | differential equation]] is defined as an equation that involves an unknown function and its [[understanding_derivatives_in_differential_equations | derivatives]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

For example, `y' + y = x + 3` is a differential equation <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. In this example, `y` is the unknown function <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This can also be written as `dy/dx + y = x + 3` or `f'(x) + f(x) = x + 3` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Differential Equations vs. Regular Equations

Unlike a regular algebraic equation, where the [[solutions_to_differential_equations | solution]] is a number or a set of numbers <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, the [[solutions_to_differential_equations | solution]] to a [[introduction_to_differential_equations | differential equation]] is a function <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal is to find the function (e.g., `y(x)` or `f(x)`) that satisfies the given relationship or equation <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Verifying a Solution

To understand what a [[solutions_to_differential_equations | solution]] to a [[introduction_to_differential_equations | differential equation]] means, consider the equation:
`y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>

#### Example Solution 1: `y1(x) = e^(-3x)`
To verify if `y1(x) = e^(-3x)` is a [[solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>:
1.  Find the first derivative `y1'`:
    `y1' = -3e^(-3x)` <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>
2.  Find the second derivative `y1''`:
    `y1'' = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
3.  Substitute `y1`, `y1'`, and `y1''` into the original equation:
    `9e^(-3x) + 2(-3e^(-3x)) - 3(e^(-3x))` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
    `= 9e^(-3x) - 6e^(-3x) - 3e^(-3x)` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
    `= (9 - 6 - 3)e^(-3x)` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
    `= 0` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

Since the equation holds true, `y1(x) = e^(-3x)` satisfies the [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

#### Example Solution 2: `y2(x) = e^x`
Another [[solutions_to_differential_equations | solution]] to the same differential equation is `y2(x) = e^x` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>:
1.  Find the first derivative `y2'`:
    `y2' = e^x` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>
2.  Find the second derivative `y2''`:
    `y2'' = e^x` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
3.  Substitute `y2`, `y2'`, and `y2''` into the original equation:
    `e^x + 2(e^x) - 3(e^x)` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
    `= (1 + 2 - 3)e^x` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
    `= 0` <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>

This shows that `y2(x) = e^x` is also a [[solutions_to_differential_equations | solution]] to the [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. A [[solutions_to_differential_equations | solution]] to a [[introduction_to_differential_equations | differential equation]] can be a single function, a set of functions, or a class of functions <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

## Terminology and Classification of Differential Equations

[[classification_of_differential_equations | Differential equations]] are classified in several ways <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>:

### Ordinary vs. Partial Differential Equations
*   **Ordinary [[introduction_to_differential_equations | Differential Equation]] (ODE)**: Involves a function of only one independent variable and its [[understanding_derivatives_in_differential_equations | derivatives]] <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. This playlist focuses on ODEs <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Partial [[introduction_to_differential_equations | Differential Equation]] (PDE)**: Involves a function of more than one variable and its partial [[understanding_derivatives_in_differential_equations | derivatives]] (e.g., with respect to x, y, or z) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. These are more complex and are discussed later <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### Order of a Differential Equation
The **order** of a [[introduction_to_differential_equations | differential equation]] is the highest [[understanding_derivatives_in_differential_equations | derivative]] that exists in the equation <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

Consider the example:
`x^2 * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
The highest derivative in this equation is the second derivative (`y''`) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Therefore, this is a **second-order** ordinary [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Linear vs. Non-linear Differential Equations
A [[introduction_to_differential_equations | differential equation]] is [[linear_and_nonlinear_differential_equations | linear]] if all of the functions and their [[understanding_derivatives_in_differential_equations | derivatives]] are linear <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This means there are no terms like `y^2`, `(dy/dx)^2`, or `y * y''` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

*   **[[linear_and_nonlinear_differential_equations | Linear]] Equation Example**:
    `x^2 * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>
    This is a [[linear_and_nonlinear_differential_equations | linear]] equation because the second derivative, first derivative, and `y` are not multiplied by the function or its derivatives <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. The terms multiplied are the independent variable `x` <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

*   **[[linear_and_nonlinear_differential_equations | Non-linear]] Equation Examples**:
    *   `x^2 * (y'')^2 = sin(x)` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
        This is [[linear_and_nonlinear_differential_equations | non-linear]] because the second [[understanding_derivatives_in_differential_equations | derivative]] (`y''`) is squared <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   `y * y'' = sin(x)` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>
        This is also [[linear_and_nonlinear_differential_equations | non-linear]] because the function `y` is multiplied by its second [[understanding_derivatives_in_differential_equations | derivative]] <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

This introduction provides a basic survey of what a [[introduction_to_differential_equations | differential equation]] is <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>, its characteristics, and how to verify its [[solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. The next step is to begin solving these equations <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.