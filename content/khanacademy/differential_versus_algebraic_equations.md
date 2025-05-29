---
title: Differential versus algebraic equations
videoId: 6o7b9yyhH7k
---

From: [[khanacademy]] <br/> 

[[introduction_to_differential_equations | Differential equations]] are mathematical expressions that are highly useful for modeling and simulating phenomena, aiding in the understanding of how things operate <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## What is a Differential Equation?
A differential equation involves a relationship between a function and its derivatives <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
An example of a differential equation is:
*   `y'' + 2y' = 3y` <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>

This can also be written in function notation, assuming `y` is a function of `x`:
*   `y''(x) + 2y'(x) = 3y(x)` <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>

Using Leibniz notation, it appears as:
*   `d²y/dx² + 2(dy/dx) = 3y` <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>

All these forms represent the same fundamental question: can functions be found where the second derivative plus two times the first derivative equals three times the function itself? <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>

## Solutions to Differential Equations
The [[understanding_solutions_of_differential_equations | solution]] to a differential equation is a function, or a class of functions, rather than a single value or set of values <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. A single differential equation can have more than one solution, often encompassing a whole class of functions <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

For the differential equation `y'' + 2y' = 3y`, two examples of solutions are:
*   `y₁(x) = e^(-3x)` <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>
*   `y₂(x) = e^x` <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>

### [[verifying_solutions_to_differential_equations | Verifying solutions]]
To [[verifying_solutions_to_differential_equations | verify]] `y₁(x) = e^(-3x)` as a solution:
1.  First derivative: `y'₁(x) = -3e^(-3x)` <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>
2.  Second derivative: `y''₁(x) = 9e^(-3x)` <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>
3.  Substitute into the equation: `9e^(-3x) + 2(-3e^(-3x)) = 3e^(-3x)` <a class="yt-timestamp" data-t="05:05:00">[05:05:05]</a>
4.  Simplify: `9e^(-3x) - 6e^(-3x) = 3e^(-3x)` <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>
5.  Result: `3e^(-3x) = 3e^(-3x)`, which is true <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. Therefore, `y₁(x) = e^(-3x)` is a solution <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>.

To [[verifying_solutions_to_differential_equations | verify]] `y₂(x) = e^x` as a solution:
1.  First derivative: `y'₂(x) = e^x` <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>
2.  Second derivative: `y''₂(x) = e^x` <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>
3.  Substitute into the equation: `e^x + 2(e^x) = 3e^x` <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>
4.  Simplify: `3e^x = 3e^x`, which is true <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>. Therefore, `y₂(x) = e^x` is a solution <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.

## Contrast with Algebraic Equations
In contrast to differential equations, an algebraic [[understanding_equality_in_algebra | equation]] is one typically encountered in algebra that does not involve derivatives <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.

An example of an algebraic [[understanding_equality_in_algebra | equation]] is a simple quadratic equation:
*   `x² + 3x + 2 = 0` <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>

The [[understanding_solutions_of_differential_equations | solutions]] to this algebraic equation are numbers, or a set of numbers <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.
*   Factoring the equation: `(x + 2)(x + 1) = 0` <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>
*   The solutions are `x = -2` or `x = -1` <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

The key distinction is that algebraic equations yield numerical solutions, while differential equations yield functional solutions <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.