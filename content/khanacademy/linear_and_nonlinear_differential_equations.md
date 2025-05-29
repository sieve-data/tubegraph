---
title: Linear and Nonlinear Differential Equations
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

This article explores the [[classification_of_differential_equations | classification of differential equations]] based on their order and linearity.

## What is a Differential Equation?

A [[definition_and_basic_understanding_of_differential_equations | differential equation]] is an equation that involves an unknown function and its derivatives <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, `y' + y = x + 3` is a differential equation where `y` is the unknown function <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This can also be written as `dy/dx + y = x + 3` or `f'(x) + f(x) = x + 3` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Solutions to Differential Equations

Unlike [[understanding_linear_equations | regular equations]] where the solution is a number or a set of numbers, the [[solutions_to_differential_equations | solution to a differential equation]] is a function <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal is to find the function that satisfies the given relationship <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

For instance, consider the differential equation `y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
It can be shown that `y1(x) = e^(-3x)` is a solution:
*   `y1'(x) = -3e^(-3x)` <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>
*   `y1''(x) = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>
Substituting these into the equation:
`9e^(-3x) + 2(-3e^(-3x)) - 3(e^(-3x))` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
`= 9e^(-3x) - 6e^(-3x) - 3e^(-3x) = 0` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
This confirms `y1(x)` is a solution <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

Another solution for the same equation is `y2(x) = e^x` <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>:
*   `y2'(x) = e^x` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>
*   `y2''(x) = e^x` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>
Substituting these:
`e^x + 2(e^x) - 3(e^x)` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
`= e^x + 2e^x - 3e^x = 0` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
Thus, `y2(x)` is also a solution <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## Classification of Differential Equations

Differential equations are broadly classified into two types <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>:
*   **Ordinary Differential Equations (ODEs)**: Involve functions and their derivatives with respect to only one independent variable <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. This playlist primarily focuses on ODEs <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Partial Differential Equations (PDEs)**: Involve functions of more than one variable and their partial derivatives (e.g., with respect to x, y, or z) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

Within ordinary differential equations, there are further classifications based on their **order** and **linearity** <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

### Order of a Differential Equation

The **order** of a [[classification_of_differential_equations | differential equation]] is defined by the highest derivative present in the equation <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
**Example:**
`x^2 (d^2y/dx^2) + x (dy/dx) + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
In this equation, the highest derivative is the second derivative (`d^2y/dx^2`) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Therefore, this is a **second-order** ordinary [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### Linear vs. Nonlinear Differential Equations

A [[understanding_linear_equations | differential equation]] is considered **linear** if all of the unknown functions and their derivatives appear in a linear fashion <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This means:
*   There are no terms where the function (e.g., `y`) or its derivatives (e.g., `dy/dx`, `d^2y/dx^2`) are raised to a power (e.g., `y^2`, `(dy/dx)^2`) <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   There are no terms where the function is multiplied by one of its derivatives (e.g., `y * (d^2y/dx^2)`) <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   The coefficients of the function and its derivatives can be functions of the independent variable (e.g., `x^2` or `x`), but not the dependent variable or its derivatives <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

**Example of a Linear Differential Equation:**
`x^2 (d^2y/dx^2) + x (dy/dx) + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
This is a **linear** equation because `y`, `dy/dx`, and `d^2y/dx^2` are not squared, nor are they multiplied by each other or `y` <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. The coefficients `x^2` and `x` are functions of the independent variable `x` <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

**Examples of Nonlinear Differential Equations:**
*   `x^2 (d^2y/dx^2)^2 = sin(x)` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
    This is **nonlinear** because the second derivative (`d^2y/dx^2`) is squared <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   `y (d^2y/dx^2) = sin(x)` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>
    This is also **nonlinear** because the function `y` is multiplied by its second derivative <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

Understanding these [[classification_of_differential_equations | classifications]] is essential for approaching [[examples_of_differential_equation_solutions | solutions to differential equations]], which will be covered in subsequent videos <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.