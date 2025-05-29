---
title: First order vs higher order differential equations
videoId: 6o7b9yyhH7k
---

From: [[khanacademy]] <br/> 

[[introduction_to_differential_equations | Differential equations]] are mathematical constructs used for [[understanding_differential_equations_and_their_solutions | modeling and simulating phenomena]] and understanding their operation <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. At its core, a [[introduction_to_differential_equations | differential equation]] expresses a relationship involving a function and its derivatives <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## What is a Differential Equation?

A [[introduction_to_differential_equations | differential equation]] is an equation that involves derivatives of an unknown function <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

For example, the following is a [[introduction_to_differential_equations | differential equation]]:
y'' + 2y' = 3y <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

### Notation Examples

This same [[introduction_to_differential_equations | differential equation]] can be expressed in various notations:

*   **Function Notation**: If `y` is a function of `x`, it can be written as y''(x) + 2y'(x) = 3y(x) <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This asks to find functions where the second derivative plus two times the first derivative equals three times the function itself <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Leibniz Notation**: Using Leibniz notation, it can be written as d²y/dx² + 2(dy/dx) = 3y <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

All three forms represent the same underlying relationship <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## [[functionbased_solutions_to_differential_equations | Solutions to Differential Equations]]

### Functions as Solutions

A key characteristic of a [[introduction_to_differential_equations | differential equation]] is that its [[functionbased_solutions_to_differential_equations | solution is a function]], or a class of functions, rather than a single value or set of values <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This means the goal is to find functions that satisfy the given relationship between the function and its derivatives <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Often, there is more than one [[functionbased_solutions_to_differential_equations | solution]], forming a whole class of functions <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### [[comparing_algebraic_and_differential_equations | Contrast with Algebraic Equations]]

It's important to [[comparing_algebraic_and_differential_equations | contrast differential equations]] with traditional [[comparing_algebraic_and_differential_equations | algebraic equations]] <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

For instance, an [[comparing_algebraic_and_differential_equations | algebraic equation]] like x² + 3x + 2 = 0 has solutions that are numbers <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. In this case, the solutions are x = -2 or x = -1 <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. These are specific numerical values that satisfy the equation <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

In contrast, the [[functionbased_solutions_to_differential_equations | solution to a differential equation]] is a function or a set of functions <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

## [[verification_of_solutions_for_differential_equations | Verifying Solutions]]

To [[verification_of_solutions_for_differential_equations | verify if a function is a solution]] to a [[introduction_to_differential_equations | differential equation]], one must substitute the function and its derivatives into the equation to see if the equality holds true <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Example [[verification_of_solutions_for_differential_equations | Verification]]

Consider the [[introduction_to_differential_equations | differential equation]]: y'' + 2y' = 3y <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

**Solution 1: y₁(x) = e^(-3x)** <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>
1.  First derivative: y₁'(x) = -3e^(-3x) <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>
2.  Second derivative: y₁''(x) = 9e^(-3x) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>

Substituting these into the equation:
9e^(-3x) + 2(-3e^(-3x)) = 3(e^(-3x)) <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>
9e^(-3x) - 6e^(-3x) = 3e^(-3x) <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
3e^(-3x) = 3e^(-3x) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>
Since both sides are equal, y₁(x) = e^(-3x) is a [[functionbased_solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

**Solution 2: y₂(x) = e^x** <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>
1.  First derivative: y₂'(x) = e^x <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>
2.  Second derivative: y₂''(x) = e^x <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>

Substituting these into the equation:
e^x + 2(e^x) = 3(e^x) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
3e^x = 3e^x <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>
Since both sides are equal, y₂(x) = e^x is also a [[functionbased_solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.