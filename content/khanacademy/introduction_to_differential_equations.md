---
title: Introduction to differential equations
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

[[understanding_differential_equations_and_their_solutions | Differential equations]] are equations that involve an unknown function and its derivatives <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. They are a widely applicable area of study, appearing in various fields such as economics, physics, and engineering <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a><a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## [[comparing_algebraic_and_differential_equations | Comparing Algebraic and Differential Equations]]

Unlike a regular algebraic equation, where the solution is typically a number or a set of numbers <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, the [[functionbased_solutions_to_differential_equations | solution to a differential equation]] is a function <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal when solving a differential equation is to find the function (e.g., `y(x)` or `f(x)`) that satisfies the given relationship or equation <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a><a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

For example:
*   **Regular Equation**: `x² + cos(x) = sqrt(x)` <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The solution is a number for `x`.
*   **Differential Equation**: `y' + y = x + 3` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Here, `y` is the unknown function. This can also be written as `dy/dx + y = x + 3` or `f'(x) + f(x) = x + 3` <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a><a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The solution is a function `y(x)` or `f(x)`.

A single differential equation might have more than one solution function <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Often, the solution is a "class of functions," which are variations of the same function with differing constants <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a><a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

## [[verification_of_solutions_for_differential_equations | Verification of Solutions]]

To verify if a proposed function is a solution to a differential equation, you substitute the function and its derivatives back into the equation to see if it holds true <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a><a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

### Example:
Consider the differential equation: `y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a><a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

**Proposed Solution 1:** `y₁(x) = e⁻³ˣ` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
1.  Find the first derivative: `y₁'(x) = -3e⁻³ˣ` (using the chain rule from [[introduction_to_derivatives_in_calculus | Differential Calculus]]) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a><a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
2.  Find the second derivative: `y₁''(x) = 9e⁻³ˣ` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a><a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
3.  Substitute into the equation:
    `9e⁻³ˣ + 2(-3e⁻³ˣ) - 3(e⁻³ˣ) = 0` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
    `9e⁻³ˣ - 6e⁻³ˣ - 3e⁻³ˣ = 0` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
    `(9 - 6 - 3)e⁻³ˣ = 0` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
    `0 = 0` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>
    Since the equation holds true, `y₁(x) = e⁻³ˣ` is a solution <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

**Proposed Solution 2:** `y₂(x) = eˣ` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a><a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>
1.  Find the first derivative: `y₂'(x) = eˣ` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a><a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
2.  Find the second derivative: `y₂''(x) = eˣ` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a><a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
3.  Substitute into the equation:
    `eˣ + 2(eˣ) - 3(eˣ) = 0` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
    `(1 + 2 - 3)eˣ = 0` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
    `0 = 0` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
    Since the equation holds true, `y₂(x) = eˣ` is also a solution <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## Terminology and Classification

[[types_of_differential_equations_ordinary_vs_partial | Differential equations]] are categorized in several ways:

### Ordinary vs. Partial Differential Equations
*   An **ordinary differential equation (ODE)** involves a function of only one variable and its derivatives with respect to that variable <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a><a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. The examples shown above are ODEs. This playlist primarily focuses on ODEs <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   A **partial differential equation (PDE)** involves a function of more than one variable, where derivatives can be taken with respect to multiple independent variables (e.g., x, y, z) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a><a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. These are more complex and are typically covered later <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### [[order_of_a_differential_equation | Order of a Differential Equation]]
The [[order_of_a_differential_equation | order]] of a differential equation is determined by the highest derivative of the unknown function present in the equation <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a><a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

*   **Example**: `x²(d²y/dx²) + x(dy/dx) + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
    *   The highest derivative is the second derivative (`d²y/dx²`) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a><a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
    *   Therefore, this is a [[first_order_vs_higher_order_differential_equations | second-order]] ordinary differential equation <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### Linear vs. Non-linear Differential Equations
A differential equation is **linear** if all the unknown functions and their derivatives within the equation appear in a "linear" fashion <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a><a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. This means:
*   There are no terms like `y²` or `(dy/dx)²` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a><a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   There are no products of the unknown function and its derivatives (e.g., `y * y''`) <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a><a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

*   **Example of a Linear Equation**: `x²(d²y/dx²) + x(dy/dx) + 2y = sin(x)` <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
    *   The `y`, `y'`, and `y''` terms are not multiplied by `y` or any of its derivatives <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. The coefficients are functions of the independent variable `x`, which is permissible <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a><a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

*   **Examples of Non-linear Equations**:
    *   `x²(d²y/dx²)² = sin(x)`: This is non-linear because the second derivative term is squared <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a><a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   `y(d²y/dx²) = sin(x)`: This is non-linear because the function `y` is multiplied by its second derivative <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a><a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

Understanding these foundational concepts is crucial before delving into methods for solving differential equations <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.