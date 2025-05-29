---
title: Understanding derivatives in differential equations
videoId: 6o7b9yyhH7k
---

From: [[khanacademy]] <br/> 

[[introduction_to_differential_equations | Differential equations]] are mathematical tools used for modeling and simulating various phenomena, helping to understand how they operate <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. At their core, these equations involve functions and their [[derivatives_and_calculus_terminology | derivatives]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## What is a Differential Equation?

A [[definition_and_basic_understanding_of_differential_equations | differential equation]] is an equation that expresses a relationship between a function and one or more of its [[introduction_to_derivatives | derivatives]] <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

Here's an example:
```
y'' + 2y' = 3y
```
This equation relates the second [[derivatives_and_calculus_terminology | derivative]] of `y` (`y''`) and the first [[derivatives_and_calculus_terminology | derivative]] of `y` (`y'`) to the function `y` itself <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

This same equation can be written in different notations:
*   **Function Notation**: If `y` is a function of `x`, denoted as `y(x)`:
    ```
    y''(x) + 2y'(x) = 3y(x)
    ```
    This states that the second [[derivatives_and_calculus_terminology | derivative]] of the function `y` with respect to `x`, plus two times its first [[derivatives_and_calculus_terminology | derivative]], is equal to three times the function itself <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Leibniz Notation**:
    ```
    (d²y/dx²) + 2(dy/dx) = 3y
    ```
    This expresses the second [[derivatives_and_calculus_terminology | derivative]] of `y` with respect to `x`, plus two times the first [[derivatives_and_calculus_terminology | derivative]] of `y` with respect to `x`, equaling three times `y` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

All three notations represent the same [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The core question posed by such an equation is: Can we find functions where the second [[derivatives_and_calculus_terminology | derivative]] plus two times the first [[derivatives_and_calculus_terminology | derivative]] equals three times the function itself? <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

## Solutions: Functions, Not Values

A critical distinction of [[solutions_to_differential_equations | differential equations]] is that their [[solutions_to_differential_equations | solutions]] are functions, or a class of functions, rather than specific numerical values <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

Contrast this with an **algebraic equation**, such as a simple quadratic equation:
```
x² + 3x + 2 = 0
```
The [[solutions_to_differential_equations | solutions]] to this equation are numbers (e.g., x = -2 or x = -1) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

For a [[definition_and_basic_understanding_of_differential_equations | differential equation]], the [[solutions_to_differential_equations | solution]] is a function or a set of functions that satisfy the relationship between the function and its [[derivatives_and_calculus_terminology | derivatives]] <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

## Examples of Solutions

Let's examine [[examples_of_differential_equation_solutions | solutions]] for the differential equation `y'' + 2y' = 3y` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. It is common for a [[definition_and_basic_understanding_of_differential_equations | differential equation]] to have more than one solution; often, a whole class of functions can be a solution <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Example Solution 1: `y₁(x) = e⁻³ˣ`

Let's verify if `y₁(x) = e⁻³ˣ` is a [[solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

1.  **First Derivative (`y₁'`)**: Using the chain rule for [[introduction_to_derivatives | derivatives]], `y₁'(x) = -3e⁻³ˣ` <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
2.  **Second Derivative (`y₁''`)**: `y₁''(x) = 9e⁻³ˣ` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

Now, substitute these into the [[introduction_to_differential_equations | differential equation]] `y'' + 2y' = 3y`:
```
(9e⁻³ˣ) + 2(-3e⁻³ˣ) = 3(e⁻³ˣ)
9e⁻³ˣ - 6e⁻³ˣ = 3e⁻³ˣ
3e⁻³ˣ = 3e⁻³ˣ
```
Since both sides are equal, `y₁(x) = e⁻³ˣ` is indeed a [[solutions_to_differential_equations | solution]] to the [[definition_and_basic_understanding_of_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Example Solution 2: `y₂(x) = eˣ`

Let's verify if `y₂(x) = eˣ` is another [[solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

1.  **First Derivative (`y₂'`)**: `y₂'(x) = eˣ` <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
2.  **Second Derivative (`y₂''`)**: `y₂''(x) = eˣ` <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

Substitute these into the [[introduction_to_differential_equations | differential equation]] `y'' + 2y' = 3y`:
```
(eˣ) + 2(eˣ) = 3(eˣ)
eˣ + 2eˣ = 3eˣ
3eˣ = 3eˣ
```
As both sides are equal, `y₂(x) = eˣ` is also a [[solutions_to_differential_equations | solution]] to the [[definition_and_basic_understanding_of_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

These examples highlight that [[solutions_to_differential_equations | solutions]] to [[definition_and_basic_understanding_of_differential_equations | differential equations]] involve finding functions whose [[derivatives_and_calculus_terminology | derivatives]] satisfy the given relationship within the equation. Future explorations will delve into techniques for solving these equations and visualizing their [[solutions_to_differential_equations | solutions]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.