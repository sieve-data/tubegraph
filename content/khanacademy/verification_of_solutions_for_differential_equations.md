---
title: Verification of solutions for differential equations
videoId: 6o7b9yyhH7k
---

From: [[khanacademy]] <br/> 

[[introduction_to_differential_equations | Differential equations]] are mathematical constructs used for modeling and simulating phenomena, helping to understand their operation <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Unlike [[comparing_algebraic_and_differential_equations | algebraic equations]] which yield numerical solutions, the [[functionbased_solutions_to_differential_equations | solutions to a differential equation]] are functions or a class of functions <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## What is a Differential Equation?

A [[introduction_to_differential_equations | differential equation]] expresses a relationship between a function and its derivatives <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

An example of a [[introduction_to_differential_equations | differential equation]] is:
`y'' + 2y' = 3y` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

This can also be written in [[Differential Calculus and Its Applications | function notation]] if `y` is a function of `x`:
`f''(x) + 2f'(x) = 3f(x)` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>

Or using Leibniz notation:
`d²y/dx² + 2(dy/dx) = 3y` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

All these notations represent the same inquiry: finding functions where the second derivative plus two times the first derivative equals three times the function itself <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Contrasting with Algebraic Equations

Traditional [[comparing_algebraic_and_differential_equations | algebraic equations]] typically yield numbers or a set of numbers as solutions <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

For instance, consider the algebraic equation:
`x² + 3x + 2 = 0` <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>

Factoring this equation gives `(x + 2)(x + 1) = 0` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, resulting in solutions `x = -2` or `x = -1` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Here, the solutions are specific numerical values that satisfy the equation <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

In contrast, the [[functionbased_solutions_to_differential_equations | solution to a differential equation]] is a function or a set of functions <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Verifying Solutions for a Differential Equation

To verify if a proposed function is a [[functionbased_solutions_to_differential_equations | solution to a differential equation]], one must substitute the function and its derivatives into the equation and check if it holds true <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Let's use the example [[introduction_to_differential_equations | differential equation]]: `y'' + 2y' = 3y` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

### Verification of `y₁(x) = e^(-3x)`

Consider `y₁(x) = e^(-3x)` as a potential solution <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

1.  **First Derivative**:
    `y₁'(x) = -3e^(-3x)` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>

2.  **Second Derivative**:
    `y₁''(x) = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>

3.  **Substitute into the equation**:
    Substitute these derivatives back into `y'' + 2y' = 3y`:
    `9e^(-3x) + 2(-3e^(-3x)) = 3(e^(-3x))` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>
    `9e^(-3x) - 6e^(-3x) = 3e^(-3x)` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
    `3e^(-3x) = 3e^(-3x)` <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>

Since both sides of the equation are equal, `y₁(x) = e^(-3x)` is indeed a [[functionbased_solutions_to_differential_equations | solution to this differential equation]] <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Verification of `y₂(x) = e^x`

Consider `y₂(x) = e^x` as another potential solution <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

1.  **First Derivative**:
    `y₂'(x) = e^x` <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>

2.  **Second Derivative**:
    `y₂''(x) = e^x` <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>

3.  **Substitute into the equation**:
    Substitute these derivatives back into `y'' + 2y' = 3y`:
    `e^x + 2(e^x) = 3(e^x)` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
    `3e^x = 3e^x` <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>

As both sides are equal, `y₂(x) = e^x` is also a [[functionbased_solutions_to_differential_equations | solution to this differential equation]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This demonstrates that a [[introduction_to_differential_equations | differential equation]] can have more than one solution; often, there's a whole class of functions that can satisfy it <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.