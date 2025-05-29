---
title: difference between regular and differential equations
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

This article serves as an [[introduction to differential equations | introduction to differential equations]], outlining their fundamental nature and distinguishing them from conventional equations. [[introduction to differential equations | Differential equations]] are widely applicable and appear in diverse fields such as economics, physics, and engineering <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## What is a Differential Equation?
A [[differential_versus_algebraic_equations | differential equation]] is defined as an equation that involves an unknown function and one or more of its derivatives <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The primary goal when dealing with a [[differential_versus_algebraic_equations | differential equation]] is to determine the specific function that satisfies the given relationship <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

<br>

> [!EXAMPLE] Examples of [[differential_versus_algebraic_equations | Differential Equations]]
>
> An unknown function, often denoted as *y* or *f(x)*, and its derivatives are central to [[differential_versus_algebraic_equations | differential equations]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
>
> ```
> y' + y = x + 3
> ```
> <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
>
> This can also be written using Leibniz notation or as a function of *x*:
>
> ```
> dy/dx + y = x + 3
> ```
> <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
>
> ```
> f'(x) + f(x) = x + 3
> ```
> <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>

## Regular Equations vs. Differential Equations

The key distinction between "regular equations" (often referred to as [[differential_versus_algebraic_equations | algebraic equations]]) and [[differential_versus_algebraic_equations | differential equations]] lies in the nature of their solutions <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Regular Equations
For a regular equation, the solution is typically a number or a set of numbers <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

<br>

> [!EXAMPLE] Example of a Regular Equation
>
> Consider an equation with one variable:
>
> ```
> x^2 + cos(x) = sqrt(x)
> ```
> <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>
>
> The solution to this equation would be a specific numerical value (or values) for *x* that satisfies the equality <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Differential Equations
In contrast, the solution to a [[differential_versus_algebraic_equations | differential equation]] is a *function*, or a class/set of functions <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>, <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. The aim is to find which function, when substituted along with its derivatives, makes the equation true <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

<br>

> [!INFO] [[understanding_solutions_of_differential_equations | Verifying Solutions to Differential Equations]]
>
> To [[verifying_solutions_to_differential_equations | verify if a function is a solution to a differential equation]], you substitute the proposed function and its derivatives into the equation. If the equation holds true, the function is a solution <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
>
> Consider the [[differential_versus_algebraic_equations | differential equation]]:
>
> ```
> y'' + 2y' - 3y = 0
> ```
> <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>
>
> #### Verification of `y1(x) = e^(-3x)`
>
> Proposed solution: `y1(x) = e^(-3x)` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
>
> 1.  First derivative: `y1' = -3e^(-3x)` <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>
> 2.  Second derivative: `y1'' = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
>
> Substitute into the equation:
>
> ```
> (9e^(-3x)) + 2(-3e^(-3x)) - 3(e^(-3x))
> = 9e^(-3x) - 6e^(-3x) - 3e^(-3x)
> = (9 - 6 - 3)e^(-3x)
> = 0e^(-3x)
> = 0
> ```
> <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
>
> Since the equation equals 0, `y1(x) = e^(-3x)` is a valid solution <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
>
> #### Verification of `y2(x) = e^x`
>
> Proposed solution: `y2(x) = e^x` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>
>
> 1.  First derivative: `y2' = e^x` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
> 2.  Second derivative: `y2'' = e^x` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
>
> Substitute into the equation:
>
> ```
> (e^x) + 2(e^x) - 3(e^x)
> = (1 + 2 - 3)e^x
> = 0e^x
> = 0
> ```
> <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
>
> As the equation equals 0, `y2(x) = e^x` is also a valid solution <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. This example demonstrates that a [[differential_versus_algebraic_equations | differential equation]] can have multiple solutions <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Terminology of [[differential_versus_algebraic_equations | Differential Equations]]
Once the basic understanding of what a [[differential_versus_algebraic_equations | differential equation]] is and what its solution means is established, it is useful to learn some terminology <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Ordinary vs. Partial Differential Equations
A key classification divides [[differential_versus_algebraic_equations | differential equations]] into [[ordinary_vs_partial_differential_equations | ordinary and partial differential equations]] <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

*   **[[ordinary_vs_partial_differential_equations | Ordinary Differential Equation (ODE)]]**: An ODE involves functions and their derivatives with respect to only *one* independent variable <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. The examples shown above are all ODEs <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This playlist focuses on [[ordinary_vs_partial_differential_equations | ordinary differential equations]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **[[ordinary_vs_partial_differential_equations | Partial Differential Equation (PDE)]]**: A PDE involves functions of *more than one* independent variable and their partial derivatives (e.g., with respect to *x*, *y*, or *z*) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. PDEs are more complex and are not the focus of this particular series <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### Order of a Differential Equation
The *order* of a [[differential_versus_algebraic_equations | differential equation]] is determined by the highest derivative present in the equation <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

<br>

> [!EXAMPLE] Identifying the Order
>
> Consider the equation:
>
> ```
> x^2 (d^2y/dx^2) + x (dy/dx) + 2y = sin(x)
> ```
> <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
>
> The highest derivative here is the second derivative (`d^2y/dx^2`) <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. Therefore, this is a [[linear_vs_nonlinear_differential_equations | second-order ordinary differential equation]] <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Linear vs. Nonlinear Differential Equations
[[linear_vs_nonlinear_differential_equations | Differential equations]] can also be classified as [[linear_vs_nonlinear_differential_equations | linear or nonlinear]] <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

*   **[[linear_vs_nonlinear_differential_equations | Linear Differential Equation]]**: A [[linear_vs_nonlinear_differential_equations | differential equation]] is [[linear_vs_nonlinear_differential_equations | linear]] if all terms involving the unknown function and its derivatives are "linear" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This means there are no terms like `y^2`, `(dy/dx)^2`, or products of the function and its derivatives (e.g., `y * y''`) <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
    *   Example: `x^2 (d^2y/dx^2) + x (dy/dx) + 2y = sin(x)` is [[linear_vs_nonlinear_differential_equations | linear]] because `y`, `y'`, and `y''` are not multiplied by themselves or each other <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Even though *x* is multiplied by derivatives, *x* is the independent variable, not the function *y* or its derivatives <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

*   **[[linear_vs_nonlinear_differential_equations | Nonlinear Differential Equation]]**: A [[linear_vs_nonlinear_differential_equations | differential equation]] is [[linear_vs_nonlinear_differential_equations | nonlinear]] if it contains any terms that violate the linearity condition <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   Example 1: If the equation `x^2 (d^2y/dx^2) + x (dy/dx) + 2y = sin(x)` were modified to `x^2 (d^2y/dx^2)^2 = sin(x)`, it would become [[linear_vs_nonlinear_differential_equations | nonlinear]] due to the `(d^2y/dx^2)^2` term <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
    *   Example 2: If the equation were `y * (d^2y/dx^2) = sin(x)`, it would also be [[linear_vs_nonlinear_differential_equations | nonlinear]] because the function `y` is multiplied by its second derivative <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.