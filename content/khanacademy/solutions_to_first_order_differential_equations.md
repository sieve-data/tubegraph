---
title: Solutions to first order differential equations
videoId: 6o7b9yyhH7k
---

From: [[khanacademy]] <br/> 
## [[understanding_solutions_of_differential_equations | Understanding Solutions of Differential Equations]]

An [[introduction to differential equations | introduction to differential equations]] reveals them to be extremely useful for modeling and simulating phenomena, and for [[understanding solutions of differential equations | understanding how they operate]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

### What is a Differential Equation?
A differential equation is an equation that involves a function and its derivatives <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Here is an example of a differential equation:

*   The second derivative of y plus two times the first derivative of y is equal to three times y <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

This can be written in several ways:
*   Using prime notation (assuming y is a function of x): `y'' + 2y' = 3y` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   Using function notation: `f''(x) + 2f'(x) = 3f(x)` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>
*   Using Leibniz notation: `(d²y)/(dx²) + 2(dy/dx) = 3y` <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>

All these notations ask the same question: Can functions be found where the second derivative plus two times the first derivative equals three times the function itself? <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>

### Solutions to Differential Equations
The distinguishing characteristic of a differential equation is that its solution is a function, or a class of functions, rather than a single value or set of values <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This is because differential equations describe relationships between a function and its derivatives <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### [[differential_versus_algebraic_equations | Differential Versus Algebraic Equations]]
It's important to contrast differential equations with [[differential_versus_algebraic_equations | algebraic equations]] <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. For example, an [[differential_versus_algebraic_equations | algebraic equation]] like `x² + 3x + 2 = 0` has solutions that are numbers <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. In this case, factoring it to `(x+2)(x+1) = 0` yields numerical solutions of `x = -2` or `x = -1` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. These are specific values that satisfy the equation <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. In contrast, the solution to a differential equation is a function or a set of functions <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### [[verifying_solutions_to_differential_equations | Verifying Solutions to Differential Equations]]
To [[verifying_solutions_to_differential_equations | verify a solution]] to a differential equation, one must substitute the proposed function and its derivatives into the equation and check if it holds true <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Often, there is more than one solution, and sometimes a whole class of functions can be a solution <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

Consider the differential equation: `y'' + 2y' = 3y` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

**Example Solution 1: `y₁(x) = e⁻³ˣ`** <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>
1.  **First Derivative:** `y₁'(x) = -3e⁻³ˣ` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>
2.  **Second Derivative:** `y₁''(x) = 9e⁻³ˣ` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>

Substitute these into the differential equation:
`9e⁻³ˣ + 2(-3e⁻³ˣ) = 3(e⁻³ˣ)` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>
`9e⁻³ˣ - 6e⁻³ˣ = 3e⁻³ˣ` <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>
`3e⁻³ˣ = 3e⁻³ˣ` <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>
Since both sides are equal, `y₁(x) = e⁻³ˣ` is indeed a solution <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

**Example Solution 2: `y₂(x) = eˣ`** <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>
1.  **First Derivative:** `y₂'(x) = eˣ` <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>
2.  **Second Derivative:** `y₂''(x) = eˣ` <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>

Substitute these into the differential equation:
`eˣ + 2(eˣ) = 3(eˣ)` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
`3eˣ = 3eˣ` <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>
Since both sides are equal, `y₂(x) = eˣ` is also a solution <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

These examples illustrate that a single differential equation can have multiple distinct solutions <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Further exploration involves understanding what these classes of solutions look like, techniques for [[solving_differential_equations_using_laplace_transform | solving differential equations]], and visualizing their behaviors <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.