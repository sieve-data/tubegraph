---
title: ordinary vs partial differential equations
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

This article serves as an [[introduction_to_differential_equations | introduction to differential equations]], a topic useful across various fields such as economics, physics, and engineering <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## What is a Differential Equation?
A [[introduction_to_differential_equations | differential equation]] is defined as an equation that involves an unknown function and its derivatives <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

For example, `y' + y = x + 3` is a differential equation where `y` is the unknown function <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This can also be written as `dy/dx + y = x + 3` or `f'(x) + f(x) = x + 3` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Differential vs. Regular Equations
Unlike [[difference_between_regular_and_differential_equations | regular equations]] (e.g., `x² + cos(x) = √x`) where the solution is a number or a set of numbers <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, for a [[introduction_to_differential_equations | differential equation]], the [[understanding_solutions_of_differential_equations | solution is a function]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal is to find the function that satisfies the given relationship <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Verifying Solutions
To [[verifying_solutions_to_differential_equations | verify a solution]] to a [[introduction_to_differential_equations | differential equation]], you substitute the proposed function and its derivatives back into the equation to see if it holds true <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

**Example:**
Consider the differential equation: `y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
1.  **Proposed Solution 1:** `y1(x) = e^(-3x)` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
    *   `y1' = -3e^(-3x)` <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>
    *   `y1'' = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
    *   Substituting: `9e^(-3x) + 2(-3e^(-3x)) - 3(e^(-3x)) = 9e^(-3x) - 6e^(-3x) - 3e^(-3x) = 0` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
    *   This confirms `y1(x)` is a solution <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

2.  **Proposed Solution 2:** `y2(x) = e^x` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>
    *   `y2' = e^x` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>
    *   `y2'' = e^x` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
    *   Substituting: `e^x + 2(e^x) - 3(e^x) = e^x + 2e^x - 3e^x = 0` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   This confirms `y2(x)` is also a solution <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

The [[understanding_solutions_of_differential_equations | solution to a differential equation]] can be a single function, a set of functions, or a class of functions <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## Classification of Differential Equations

### Ordinary Differential Equations (ODEs)
An ordinary differential equation (ODE) involves a function and its derivatives with respect to only **one variable** <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. The unknown function and its derivatives are functions of only one independent variable <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This playlist focuses on ordinary differential equations <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Partial Differential Equations (PDEs)
Partial differential equations (PDEs) are more complex, as they involve functions that can be functions of **more than one variable** <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. This means derivatives can be taken with respect to multiple independent variables (e.g., x, y, and z) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. PDEs will be discussed later <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## Further Classifications of Ordinary Differential Equations
Within ordinary differential equations, there are two main overlapping classifications:

### Order of the Differential Equation
The **order** of a [[introduction_to_differential_equations | differential equation]] is determined by the highest derivative that exists within the equation <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

**Example:**
`x² * (d²y/dx²) + x * (dy/dx) + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
The highest derivative here is the second derivative (`d²y/dx²`), so this is a second-order ordinary differential equation <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Linear vs. Nonlinear Differential Equations
A [[linear_vs_nonlinear_differential_equations | differential equation is linear]] if all of the functions and their derivatives are "linear" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This means:
*   You don't have terms like `y²` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   You don't have derivatives squared, e.g., `(dy/dx)²` <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   You don't have the function multiplied by its derivative, e.g., `y * (d²y/dx²)` <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

**Examples:**
*   **Linear:** `x² * (d²y/dx²) + x * (dy/dx) + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
    *   This is linear because the second derivative, first derivative, and `y` are not multiplied by the function or its derivatives <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. The coefficients (`x²`, `x`, `2`) are independent variables and do not affect linearity in this context <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Nonlinear:** `x² * (d²y/dx²)² = sin(x)` <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>
    *   This is nonlinear because the second derivative is squared <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   **Nonlinear:** `y * (d²y/dx²) = sin(x)` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>
    *   This is nonlinear because the function `y` is multiplied by its second derivative <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.