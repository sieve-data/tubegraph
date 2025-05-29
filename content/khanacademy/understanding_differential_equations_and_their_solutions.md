---
title: Understanding differential equations and their solutions
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

## Introduction
[[introduction_to_differential_equations | Differential equations]] are a widely applicable area of study, showing up in various fields such as economics, physics, and engineering <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This article provides an [[introduction_to_differential_equations | introduction]] to what [[introduction_to_differential_equations | differential equations]] are and how their [[functionbased_solutions_to_differential_equations | solutions]] differ from traditional algebraic [[comparing_algebraic_and_differential_equations | equations]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## What is a Differential Equation?
A [[introduction_to_differential_equations | differential equation]] is an [[comparing_algebraic_and_differential_equations | equation]] that involves an unknown [[functionbased_solutions_to_differential_equations | function]] and its [[differential_calculus_and_its_applications | derivatives]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

For example, `y' + y = x + 3` is a [[introduction_to_differential_equations | differential equation]] where `y` is the unknown [[functionbased_solutions_to_differential_equations | function]] <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This can also be written as `dy/dx + y = x + 3` or `f'(x) + f(x) = x + 3` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Differential vs. Algebraic Equations
Unlike a regular [[comparing_algebraic_and_differential_equations | equation]] (e.g., `x^2 + cos(x) = sqrt(x)`) where the [[functionbased_solutions_to_differential_equations | solution]] is a number or a set of numbers <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, the [[functionbased_solutions_to_differential_equations | solution]] for a [[introduction_to_differential_equations | differential equation]] is a [[functionbased_solutions_for_differential_equations | function]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. The goal is to find what [[functionbased_solutions_for_differential_equations | function]] satisfies the given relationship <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Verifying Solutions for Differential Equations
To verify if a given [[functionbased_solutions_for_differential_equations | function]] is a [[verification_of_solutions_for_differential_equations | solution]] to a [[introduction_to_differential_equations | differential equation]], you substitute the [[functionbased_solutions_for_differential_equations | function]] and its [[differential_calculus_and_its_applications | derivatives]] back into the [[comparing_algebraic_and_differential_equations | equation]] to see if it holds true <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Example Verification
Consider the [[introduction_to_differential_equations | differential equation]]:
`y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>

Let's test `y1(x) = e^(-3x)` as a proposed [[functionbased_solutions_for_differential_equations | solution]] <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
1.  Find the first derivative: `y1' = -3e^(-3x)` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>
2.  Find the second derivative: `y1'' = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
3.  Substitute into the original [[introduction_to_differential_equations | differential equation]]:
    `9e^(-3x) + 2(-3e^(-3x)) - 3(e^(-3x))` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
    `= 9e^(-3x) - 6e^(-3x) - 3e^(-3x)` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
    `= (9 - 6 - 3)e^(-3x) = 0e^(-3x) = 0` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
This verifies that `y1(x) = e^(-3x)` is a [[verification_of_solutions_for_differential_equations | solution]] <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

It's important to note that there might be more than one [[functionbased_solutions_for_differential_equations | solution]] to a [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. For the same example, `y2(x) = e^x` is also a [[verification_of_solutions_for_differential_equations | solution]] <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>:
1.  `y2' = e^x` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
2.  `y2'' = e^x` <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>
3.  Substitute: `e^x + 2(e^x) - 3(e^x) = (1 + 2 - 3)e^x = 0` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
Thus, `y2(x) = e^x` is also a [[verification_of_solutions_for_differential_equations | solution]] <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. The [[functionbased_solutions_for_differential_equations | solution]] can often be a class of [[functionbased_solutions_for_differential_equations | functions]] <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## Terminology and Classification of Differential Equations

### Ordinary vs. Partial Differential Equations
[[types_of_differential_equations_ordinary_vs_partial | Differential equations]] are broadly classified into two types <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>:
*   **[[types_of_differential_equations_ordinary_vs_partial | Ordinary Differential Equations (ODEs)]]**: These involve a [[functionbased_solutions_for_differential_equations | function]] of only one variable and its [[differential_calculus_and_its_applications | derivatives]] with respect to that variable (e.g., `y` with respect to `x`) <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. This playlist focuses on [[types_of_differential_equations_ordinary_vs_partial | ODEs]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **[[types_of_differential_equations_ordinary_vs_partial | Partial Differential Equations (PDEs)]]**: These are more complex, involving a [[functionbased_solutions_for_differential_equations | function]] of more than one variable and its partial [[differential_calculus_and_its_applications | derivatives]] (e.g., with respect to x, y, or z) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### Order of a Differential Equation
The [[order_of_a_differential_equation | order]] of a [[introduction_to_differential_equations | differential equation]] refers to the highest [[differential_calculus_and_its_applications | derivative]] that exists in the [[comparing_algebraic_and_differential_equations | equation]] <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

For example, in the [[introduction_to_differential_equations | differential equation]]:
`x^2 * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
The highest [[differential_calculus_and_its_applications | derivative]] is the second derivative (`y''`). Therefore, this is a [[first_order_vs_higher_order_differential_equations | second-order]] [[types_of_differential_equations_ordinary_vs_partial | ordinary differential equation]] <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Linear vs. Non-linear Differential Equations
A [[introduction_to_differential_equations | differential equation]] is [[classification_of_differential_equations_linear_vs_nonlinear | linear]] if all of the [[functionbased_solutions_for_differential_equations | functions]] and their [[differential_calculus_and_its_applications | derivatives]] are essentially [[classification_of_differential_equations_linear_vs_nonlinear | linear]] <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This means there are no terms like `y^2`, `(dy/dx)^2`, or `y * y''` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

*   **[[classification_of_differential_equations_linear_vs_nonlinear | Linear Equation]]**:
    `x^2 * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
    This is [[classification_of_differential_equations_linear_vs_nonlinear | linear]] because the [[differential_calculus_and_its_applications | derivatives]] (`y''`, `y'`) and the [[functionbased_solutions_for_differential_equations | function]] (`y`) are not multiplied by themselves or each other. They are only multiplied by terms of the independent variable `x` (e.g., `x^2`, `x`) <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

*   **[[classification_of_differential_equations_linear_vs_nonlinear | Non-linear Equation]]** (Examples):
    *   If the [[introduction_to_differential_equations | equation]] has a squared [[differential_calculus_and_its_applications | derivative]]: `x^2 * (y'')^2 = sin(x)` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. This is [[classification_of_differential_equations_linear_vs_nonlinear | non-linear]] because the second [[differential_calculus_and_its_applications | derivative]] is squared <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   If the [[functionbased_solutions_for_differential_equations | function]] is multiplied by its [[differential_calculus_and_its_applications | derivative]]: `y * y'' = sin(x)` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This is also [[classification_of_differential_equations_linear_vs_nonlinear | non-linear]] <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.