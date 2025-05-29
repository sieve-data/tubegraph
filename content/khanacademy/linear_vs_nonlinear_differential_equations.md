---
title: linear vs nonlinear differential equations
videoId: -_POEWfygmU
---

From: [[khanacademy]] <br/> 

## What is a Differential Equation?
A differential equation is an equation that involves an unknown function and its derivatives <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, `y' + y = x + 3` is a differential equation where `y` is the unknown function <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This can also be written as `dy/dx + y = x + 3` or `f'(x) + f(x) = x + 3` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Distinction from Regular Equations
Unlike [[difference_between_regular_and_differential_equations | regular equations]] (e.g., `x² + cos(x) = √x`), where the solution is a number or a set of numbers <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, the solution to a [[introduction_to_differential_equations | differential equation]] is a function <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal is to find the function that satisfies the given relationship or equation <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

For instance, given the differential equation `y'' + 2y' - 3y = 0` <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, a claimed solution `y1(x) = e^(-3x)` can be verified by substituting it and its derivatives back into the equation <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. If `y1 = e^(-3x)`, then `y1' = -3e^(-3x)` and `y1'' = 9e^(-3x)` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Substituting these into the equation results in `9e^(-3x) + 2(-3e^(-3x)) - 3(e^(-3x))` which simplifies to `9e^(-3x) - 6e^(-3x) - 3e^(-3x) = 0` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. This confirms that `e^(-3x)` is a solution <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Another potential solution to the same equation is `y2(x) = e^x` <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

The solution to a [[introduction_to_differential_equations | differential equation]] can be a single function, a set of functions, or a class of functions <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## Classifications of Differential Equations

### Ordinary vs. Partial Differential Equations
[[ordinary_vs_partial_differential_equations | Ordinary differential equations]] involve one variable with respect to another variable, or one function with respect to a single independent variable (e.g., `y` with respect to `x`) and its derivatives <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
Partial differential equations are more complex, involving functions of more than one variable and their partial derivatives (e.g., with respect to `x`, `y`, and `z`) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. This article, and its associated playlist, focuses on [[ordinary_vs_partial_differential_equations | ordinary differential equations]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Order of a Differential Equation
The "order" of a [[introduction_to_differential_equations | differential equation]] is determined by the highest derivative present in the equation <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
For example, in the equation `x² * y'' + x * y' + 2y = sin(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, the highest derivative is the second derivative (`y''`) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Therefore, this is a second-order ordinary differential equation <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### Linear vs. Non-linear Differential Equations
A [[understanding_linear_equations | differential equation]] is considered **[[understanding_linear_equations | linear]]** if all the functions and their derivatives are essentially [[understanding_linear_equations | linear]] <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This means there are no terms where:
*   The function `y` is squared (e.g., `y²`) <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   A derivative is squared (e.g., `(dy/dx)²) ` <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   The function `y` is multiplied by one of its derivatives (e.g., `y * y''`) <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

For example, `x² * y'' + x * y' + 2y = sin(x)` is a **[[understanding_linear_equations | linear]]** differential equation <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. Although `x²` and `x` are multiplied by the derivatives, these are independent variables, not the function `y` or its derivatives themselves <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

Conversely, a [[introduction_to_differential_equations | differential equation]] is **non-linear** if it contains any of the non-[[understanding_linear_equations | linear]] forms mentioned above.

```markdown
# Examples of Non-Linear Differential Equations
```
*   `x² * (y'')² = sin(x)` <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>
    *   This is non-[[understanding_linear_equations | linear]] because the second derivative (`y''`) is squared <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   `y * y'' = sin(x)` <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>
    *   This is non-[[understanding_linear_equations | linear]] because the function `y` is multiplied by its second derivative <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.