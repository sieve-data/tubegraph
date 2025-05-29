---
title: Classification of differential equations linear vs nonlinear
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

## What is a Differential Equation?
A [[introduction_to_differential equations | differential equation]] is defined as an equation that involves an unknown function and its derivatives <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, `y' + y = x + 3` or `dy/dx + y = x + 3` are ways to write a [[introduction_to_differential equations | differential equation]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Solutions to Differential Equations
Unlike [[comparing_algebraic_and_differential_equations | regular equations]] where the [[understanding_differential_equations_and_their_solutions | solution]] is typically a number or a set of numbers <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, the [[understanding_differential_equations_and_their_solutions | solution]] to a [[introduction_to_differential equations | differential equation]] is a function, or sometimes a class of functions <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>, <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. The goal is to find the function that satisfies the given equation <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

For instance, given the [[introduction_to_differential equations | differential equation]] `y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>:
*   `y1(x) = e^(-3x)` is a [[understanding_differential_equations_and_their_solutions | solution]] because substituting it and its derivatives into the equation yields `0` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   `y2(x) = e^x` is also a [[understanding_differential_equations_and_their_solutions | solution]], as it also satisfies the equation <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>, <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## General Classifications
[[introduction_to_differential equations | Differential equations]] can be broadly classified into two main types:
*   **[[types_of_differential_equations_ordinary_vs_partial | Ordinary Differential Equations (ODEs)]]**: These involve derivatives of a function with respect to only one independent variable <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This playlist focuses on [[types_of_differential_equations_ordinary_vs_partial | ordinary differential equations]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **[[types_of_differential_equations_ordinary_vs_partial | Partial Differential Equations (PDEs)]]**: These are more complex and involve functions of more than one variable, with derivatives taken with respect to multiple independent variables (e.g., x, y, z) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>, <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

## [[order_of_a_differential_equation | Order of a Differential Equation]]
Within [[types_of_differential_equations_ordinary_vs_partial | ordinary differential equations]], one classification is by their [[order_of_a_differential_equation | order]] <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. The [[order_of_a_differential_equation | order]] refers to the highest derivative present in the equation <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   **Example**: `x^2 * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
    *   The highest derivative here is `y''` (the second derivative) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
    *   Therefore, this is a **second [[order_of_a_differential_equation | order]]** [[types_of_differential_equations_ordinary_vs_partial | ordinary differential equation]] <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## Linear vs. Nonlinear Differential Equations
Another key classification is whether a [[introduction_to_differential equations | differential equation]] is linear or nonlinear <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Linear Differential Equations
A [[introduction_to_differential equations | differential equation]] is **linear** if all the unknown functions and their derivatives within the equation are "linear" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This means:
*   You do not have the unknown function squared (`y^2`) <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   You do not have a derivative squared (`(dy/dx)^2`) <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   You do not have the unknown function multiplied by one of its derivatives (e.g., `y * y''`) <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   Coefficients multiplying the function or its derivatives can be functions of the independent variable (e.g., `x^2 * y''` is linear because `x^2` is a coefficient of the independent variable) <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

**Example of a Linear Differential Equation**:
`x^2 * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>
*   This equation is linear because `y''`, `y'`, and `y` are not squared or multiplied by each other <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. The terms `x^2` and `x` are coefficients based on the independent variable.

### Nonlinear Differential Equations
A [[introduction_to_differential equations | differential equation]] is **nonlinear** if it violates any of the conditions for linearity <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

**Examples of Nonlinear Differential Equations**:
*   `x^2 * (y'')^2 = sin(x)` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>, <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>
    *   This is nonlinear because the second derivative (`y''`) is squared <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   `y * y'' = sin(x)` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>, <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
    *   This is nonlinear because the unknown function `y` is multiplied by its second derivative `y''` <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.