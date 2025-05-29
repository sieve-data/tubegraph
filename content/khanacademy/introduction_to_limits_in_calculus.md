---
title: Introduction to limits in calculus
videoId: riXcZT2ICjA
---

From: [[khanacademy]] <br/> 

The [[introduction_to_limits|idea of a limit]] is a fundamental concept upon which all of [[calculus]] is based <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Despite its critical importance, it is a relatively simple idea <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

The core concept of a limit revolves around what a function is *approaching* as its input variable gets closer and closer to a particular value, rather than what the function actually *equals* at that exact point <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. This is distinct from standard function evaluation <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Defining Limits Through Examples

### Example 1: A Function with a Hole

Consider the function `f(x)` defined as:
`f(x) = (x - 1) / (x - 1)` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

One might assume this simplifies to `f(x) = 1` because the numerator and denominator are the same <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. However, this simplification is only true with the crucial constraint that `x` cannot be equal to 1 <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

#### Why `f(x)` is Undefined at x = 1

If `x` is set to 1, the function becomes:
`f(1) = (1 - 1) / (1 - 1) = 0 / 0` <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>

Division by zero, including `0/0`, results in an undefined value <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Therefore, `f(1)` is undefined <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

#### [[graphical_representation_of_limits | Graphical Representation]]

When graphed, `f(x)` looks like the horizontal line `y = 1` for all `x` values except `x = 1` <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. At `x = 1`, there is a "gap" or a "hole" in the graph, signified by an open circle, indicating that the function is not defined at that point <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

#### Function Evaluation vs. Limit Evaluation

*   **Function Evaluation:** If asked "What is `f(1)`?", the answer is "Undefined" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. The graph shows a gap at `x=1` <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Limit Evaluation:** If asked "What is the function *approaching* as `x` approaches 1?", this refers to the [[concept_of_approaching_values_in_calculus|idea of a limit]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. As `x` gets infinitely close to 1 (from either the left or the right side), the `f(x)` value consistently approaches 1 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

This is formally written as:
`lim (x→1) f(x) = 1` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>

The notation `lim` is short for "limit" <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This means that even though `f(1)` is undefined, the function's value gets arbitrarily close to 1 as `x` gets arbitrarily close to 1 <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Example 2: A Piecewise Function with Discontinuity

Consider a function `g(x)` defined as:
`g(x) = x²` when `x ≠ 2` <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>
`g(x) = 1` when `x = 2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

This function demonstrates a discontinuity <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

#### [[graphical_representation_of_limits | Graphical Representation]]

The graph of `g(x)` largely follows the parabola `y = x²` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. However, at `x = 2`, there is a gap or hole at `y = 4` (because `2² = 4`) <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. Instead, the function is explicitly defined as `g(2) = 1`, so a single point exists at `(2, 1)` <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

#### Function Evaluation vs. Limit Evaluation

*   **Function Evaluation:** If asked "What is `g(2)`?", by definition, `g(2) = 1` <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Limit Evaluation:** If asked "What is the limit as `x` approaches 2 of `g(x)`?", we look at what `g(x)` is approaching as `x` gets closer to 2 from either side <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
    *   As `x` approaches 2 from the left (e.g., 1.9, 1.99, 1.999), `g(x)` follows `x²` and approaches 4 <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
    *   As `x` approaches 2 from the right (e.g., 2.1, 2.01, 2.001), `g(x)` also follows `x²` and approaches 4 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

Even though `g(2)` is 1, the function is *approaching* 4 as `x` gets closer to 2 <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

This is written as:
`lim (x→2) g(x) = 4` <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>

#### [[evaluating_limits_using_numerical_methods | Numerical Evaluation]]

Using a calculator, we can observe the numerical approach to the limit <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>:

| `x` (Approaching from left) | `g(x) = x²`            |
| :-------------------------- | :--------------------- |
| 1.9                         | 1.9² = 3.61            |
| 1.99                        | 1.99² = 3.9601         |
| 1.999                       | 1.999² = 3.996001      |
| 1.9999999999                | ≈ 4 (calculator rounds) <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a> |

| `x` (Approaching from right) | `g(x) = x²`            |
| :--------------------------- | :--------------------- |
| 2.1                          | 2.1² = 4.41            |
| 2.01                         | 2.01² = 4.0401         |
| 2.001                        | 2.001² = 4.004001      |

As `x` gets closer to 2 from either direction, `g(x)` gets closer and closer to 4, demonstrating that the limit is 4 <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This illustrates the key distinction: the function's value *at* the point might be different from its [[concept_of_approaching_values_in_calculus|approaching value]] <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.