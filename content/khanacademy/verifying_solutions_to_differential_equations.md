---
title: Verifying solutions to differential equations
videoId: 6o7b9yyhH7k
---

From: [[khanacademy]] <br/> 

A [[introduction_to_differential_equations | differential equation]] is an equation that expresses a relationship between a function and its derivatives <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. These equations are useful for modeling and simulating various phenomena <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Solutions to Differential Equations

Unlike [[differential_versus_algebraic_equations | algebraic equations]], whose solutions are numbers or sets of numbers <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, the solution to a [[introduction_to_differential_equations | differential equation]] is a function, or a class of functions <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Often, there can be more than one function that satisfies a given [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## How to Verify a Solution

To verify if a particular function is a solution to a [[introduction_to_differential_equations | differential equation]], you must:
1.  Calculate the necessary derivatives of the proposed function.
2.  Substitute the function and its derivatives into the [[introduction_to_differential_equations | differential equation]].
3.  Simplify the equation to see if both sides are equal. If they are, the function is a solution.

### Example Verification

Consider the [[introduction_to_differential_equations | differential equation]]:
`y'' + 2y' = 3y` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

This can also be written in function notation `y''(x) + 2y'(x) = 3y(x)` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, or using Leibniz notation `d²y/dx² + 2dy/dx = 3y` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

#### Proposed Solution 1: `y₁(x) = e⁻³ˣ` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>

1.  **Find derivatives:**
    *   First derivative: `y₁'(x) = -3e⁻³ˣ` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>
    *   Second derivative: `y₁''(x) = 9e⁻³ˣ` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>

2.  **Substitute into the equation:**
    `9e⁻³ˣ + 2(-3e⁻³ˣ) = 3(e⁻³ˣ)` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>

3.  **Simplify and check:**
    `9e⁻³ˣ - 6e⁻³ˣ = 3e⁻³ˣ` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
    `3e⁻³ˣ = 3e⁻³ˣ` <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>
    Since both sides are equal, `y₁(x) = e⁻³ˣ` is indeed a solution to the [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

#### Proposed Solution 2: `y₂(x) = eˣ` <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>

1.  **Find derivatives:**
    *   First derivative: `y₂'(x) = eˣ` <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>
    *   Second derivative: `y₂''(x) = eˣ` <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>

2.  **Substitute into the equation:**
    `eˣ + 2(eˣ) = 3(eˣ)` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>

3.  **Simplify and check:**
    `3eˣ = 3eˣ` <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>
    Since both sides are equal, `y₂(x) = eˣ` is also a solution to the [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

The ability to verify solutions is a foundational step in [[understanding_solutions_of_differential_equations | understanding solutions of differential equations]] and exploring techniques for [[solving_differential_equations_using_laplace_transform | solving them]] <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.