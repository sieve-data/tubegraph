---
title: Functionbased solutions to differential equations
videoId: 6o7b9yyhH7k
---

From: [[khanacademy]] <br/> 

A [[introduction_to_differential_equations | differential equation]] is a mathematical expression that relates a function to its derivatives <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. These equations are highly valuable for modeling and simulating various phenomena, helping to understand how they operate <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## What is a Differential Equation?

Consider the following example of a [[introduction_to_differential_equations | differential equation]]:

```
y'' + 2y' = 3y
```
This equation can be expressed in various notations, all representing the same relationship:
*   `y'' + 2y' = 3y` <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>
*   `f''(x) + 2f'(x) = 3f(x)` (when `y` is a function of `x`) <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>
*   `d²y/dx² + 2(dy/dx) = 3y` (Leibniz notation) <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>

These equations all pose the question: Can we find functions where the second derivative plus two times the first derivative equals three times the function itself? <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>

## Solutions: Functions, Not Numbers

Unlike [[comparing_algebraic_and_differential_equations | algebraic equations]] (e.g., `x² + 3x + 2 = 0`), whose solutions are specific numbers or sets of values (like `x = -2` or `x = -1`) <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>, the solution to a [[introduction_to_differential_equations | differential equation]] is a function, or often a class of functions <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. The solution defines a relationship between the function and its derivatives that holds true <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

## Verifying Function-Based Solutions

To [[verification_of_solutions_for_differential_equations | verify]] if a function is a solution to a [[introduction_to_differential_equations | differential equation]], you substitute the function and its derivatives into the equation <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

### Example Solution 1: `y₁(x) = e⁻³ˣ`

Let's [[verification_of_solutions_for_differential_equations | verify]] if `y₁(x) = e⁻³ˣ` is a solution to `y'' + 2y' = 3y` <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.

1.  **Find the first derivative**:
    `y₁'(x) = -3e⁻³ˣ` <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>

2.  **Find the second derivative**:
    `y₁''(x) = 9e⁻³ˣ` <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>

3.  **Substitute into the differential equation**:
    `y₁'' + 2y₁' = 3y₁`
    `(9e⁻³ˣ) + 2(-3e⁻³ˣ) = 3(e⁻³ˣ)` <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>
    `9e⁻³ˣ - 6e⁻³ˣ = 3e⁻³ˣ` <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>
    `3e⁻³ˣ = 3e⁻³ˣ` <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>

Since the equation holds true, `y₁(x) = e⁻³ˣ` is indeed a solution <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>.

### Example Solution 2: `y₂(x) = eˣ`

Let's [[verification_of_solutions_for_differential_equations | verify]] if `y₂(x) = eˣ` is also a solution to `y'' + 2y' = 3y` <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.

1.  **Find the first derivative**:
    `y₂'(x) = eˣ` <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>

2.  **Find the second derivative**:
    `y₂''(x) = eˣ` <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>

3.  **Substitute into the differential equation**:
    `y₂'' + 2y₂' = 3y₂`
    `eˣ + 2(eˣ) = 3(eˣ)` <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>
    `3eˣ = 3eˣ` <a class="yt-timestamp" data-t="07:24:00">[07:24:00]</a>

This also holds true, confirming that `y₂(x) = eˣ` is another solution <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.

## Classes of Solutions

As demonstrated, a single [[introduction_to_differential_equations | differential equation]] can have multiple solutions <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>. Often, there is a "whole class of functions" that can satisfy a [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. Future explorations will delve into techniques for [[understanding_differential_equations_and_their_solutions | understanding differential equations and their solutions]], visualizing them, and developing a toolkit for deeper analysis <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.