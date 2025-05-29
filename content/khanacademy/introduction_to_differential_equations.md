---
title: Introduction to Differential Equations
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

This article serves as an [[introduction_to_differential_equations | introduction to differential equations]], setting the stage for a comprehensive playlist on the topic <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. [[applications_of_differential_equations_in_various_fields | Differential equations]] are widely applicable and appear in many different fields <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Requests for this topic have come from individuals studying economics, physics, and engineering <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## [[definition_and_basic_understanding_of_differential_equations | Definition and Basic Understanding of Differential Equations]]

A [[definition_and_basic_understanding_of_differential_equations | differential equation]] is an equation that involves an unknown function and its [[understanding_derivatives_in_differential_equations | derivatives]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

For example, the following are all valid ways of writing the same [[definition_and_basic_understanding_of_differential_equations | differential equation]]:
*   `y' + y = x + 3` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   `dy/dx + y = x + 3` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   `f'(x) + f(x) = x + 3` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>

In these examples, the unknown function is `y` (or `y(x)` or `f(x)`) <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Solutions to Differential Equations

Unlike regular equations where the solution is a number or a set of numbers <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, the [[solutions_to_differential_equations | solution]] to a [[definition_and_basic_understanding_of_differential_equations | differential equation]] is a *function* <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal is to find the function of `x` that explicitly satisfies the given equation <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Often, the solution may be a class of functions, typically differing by constants <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

#### [[examples_of_differential_equation_solutions | Examples of Differential Equation Solutions]]

Consider the [[definition_and_basic_understanding_of_differential_equations | differential equation]]:
`y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>

To verify if a function is a [[solutions_to_differential_equations | solution]], substitute the function and its [[understanding_derivatives_in_differential_equations | derivatives]] back into the equation.

**Example 1: `y1(x) = e^(-3x)`** <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
1.  First derivative: `y1' = -3e^(-3x)` <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>
2.  Second derivative: `y1'' = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
3.  Substitute into the equation:
    `9e^(-3x) + 2(-3e^(-3x)) - 3(e^(-3x)) = 0` <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>
    `9e^(-3x) - 6e^(-3x) - 3e^(-3x) = 0` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
    `(9 - 6 - 3)e^(-3x) = 0`
    `0 = 0` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>
    This confirms `y1(x) = e^(-3x)` is a [[solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

**Example 2: `y2(x) = e^x`** <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>
1.  First derivative: `y2' = e^x` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
2.  Second derivative: `y2'' = e^x` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>
3.  Substitute into the equation:
    `e^x + 2(e^x) - 3(e^x) = 0` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
    `(1 + 2 - 3)e^x = 0`
    `0 = 0` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
    This confirms `y2(x) = e^x` is also a [[solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

The fact that there can be multiple [[solutions_to_differential_equations | solutions]] highlights that the solution is a function, or a set/class of functions <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

## [[classification_of_differential_equations | Classification of Differential Equations]]

[[classification_of_differential_equations | Differential equations]] are primarily classified in two ways:
1.  **Ordinary vs. Partial** <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>
2.  **Order** <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a> and **Linear vs. Non-linear** <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>

### Ordinary and Partial Differential Equations

*   **Ordinary Differential Equation (ODE)**: An ODE involves a function of only *one* variable and its [[understanding_derivatives_in_differential_equations | derivatives]] with respect to that single variable <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. This playlist focuses on [[introduction_to_differential_equations | ordinary differential equations]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Partial Differential Equation (PDE)**: A PDE involves a function of *more than one* variable and its partial derivatives with respect to those variables (e.g., `x`, `y`, `z`) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. These are more complex and are typically addressed later in studies <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### Order of a Differential Equation

The **order** of a [[definition_and_basic_understanding_of_differential_equations | differential equation]] is defined by the highest [[understanding_derivatives_in_differential_equations | derivative]] present in the equation <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

**Example**:
`x² * (d²y/dx²) + x * (dy/dx) + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
The highest derivative in this equation is the second derivative (`d²y/dx²`) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Therefore, this is a **second-order** [[definition_and_basic_understanding_of_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### [[linear_and_nonlinear_differential_equations | Linear and Nonlinear Differential Equations]]

A [[definition_and_basic_understanding_of_differential_equations | differential equation]] is considered **linear** if all of its functions and their [[understanding_derivatives_in_differential_equations | derivatives]] are essentially "linear" <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This means:
*   There are no terms like `y²` or `(dy/dx)²` <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   There are no products of the function and its derivatives, e.g., `y * (d²y/dx²)` <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

**Examples:**

*   **Linear Differential Equation**:
    `x² * (d²y/dx²) + x * (dy/dx) + 2y = sin(x)` <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>
    This is a linear equation because `y`, `y'`, and `y''` are not squared or multiplied by each other <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Coefficients like `x²` or `x` (which are independent variables) multiplying the derivatives do not make it non-linear <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

*   **Non-linear Differential Equation**:
    `x² * (d²y/dx²)² = sin(x)` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
    This is non-linear because the second derivative term `(d²y/dx²)` is squared <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

*   **Another Non-linear Differential Equation**:
    `y * (d²y/dx²) = sin(x)` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>
    This is non-linear because the function `y` is multiplied by its second derivative `(d²y/dx²)` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

---
The next video will delve into actually solving straightforward [[definition_and_basic_understanding_of_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.