---
title: Understanding the concept of limits in calculus
videoId: riXcZT2ICjA
---

From: [[khanacademy]] <br/> 
The concept of a [[the_concept_of_a_limit_in_finding_derivatives | limit]] is a fundamental idea upon which all of [[derivatives_and_calculus_terminology | calculus]] is based <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Despite its importance, it is a relatively simple idea <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. A limit describes what a function is "approaching" as the input approaches a certain value <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Understanding Limits Through Examples

### Example 1: Function with a Hole

Consider the function defined as:
`f(x) = (x - 1) / (x - 1)` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

While it might seem like this simplifies to `f(x) = 1`, there's a crucial difference <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This function is undefined when `x = 1`, because substituting `x = 1` results in `0/0`, which is an undefined expression <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

Therefore, `f(x)` can be written as `f(x) = 1` with the constraint that `x` cannot be equal to `1` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

[[Graphing limits | Graphing this function]] shows a horizontal line at `y = 1`, but with a "gap" or a hole at the point where `x = 1` <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>, <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

#### Function Value vs. Limit
*   **Function Value:** If asked for `f(1)`, the answer is "undefined" because the function is explicitly not defined at that point <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Limit:** However, if asked, "What is the function approaching as `x` equals `1`?" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, the concept of a limit comes into play <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. As `x` gets infinitely close to `1` (from both the left and right sides) but is not exactly `1`, the value of `f(x)` is `1` <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

This is expressed using [[understanding_limit_notation | limit notation]]:
`lim (x->1) f(x) = 1` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>, <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>

This notation simply asks what value the function is approaching as `x` gets closer and closer to `1` <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Example 2: Function with a Discontinuity

Consider another function, `g(x)`, defined as:
`g(x) = x^2` when `x != 2` <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>
`g(x) = 1` when `x = 2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

This function represents a [[limits_approaching_a_point_of_discontinuity | discontinuity]] <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. [[Graphing limits | Graphically]], it looks like a parabola `y = x^2`, but at `x = 2`, the function "jumps" down to `y = 1` (a filled-in point) while there's a hole at `y = 4` on the parabola where `x = 2` <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

#### Function Value vs. Limit
*   **Function Value:** `g(2) = 1` based on the definition <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Limit:** The question for the limit is: "What is the limit as `x` approaches `2` of `g(x)`?" <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, asking what `g(x)` is approaching as `x` gets closer and closer to `2` <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

[[Calculating limits numerically and graphically | Graphically]], as `x` approaches `2` from either direction along the `x^2` part of the function, the function's value approaches `4` <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>, <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Even though `g(2)` is `1`, the limit is `4`.

This is written as:
`lim (x->2) g(x) = 4` <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>

#### Calculating Limits Numerically
To confirm this, one can [[calculating_limits_numerically_and_graphically | calculate the function's values numerically]] as `x` gets closer to `2` <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>:

*   **Approaching from below:**
    *   `g(1.9) = 1.9^2 = 3.61` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>, <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>
    *   `g(1.99) = 1.99^2 = 3.9601` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
    *   `g(1.999) = 1.999^2 = 3.996001` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>, <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>
    As `x` gets closer to `2`, `g(x)` gets closer to `4` <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

*   **Approaching from above:**
    *   `g(2.1) = 2.1^2 = 4.41` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>, <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>
    *   `g(2.01) = 2.01^2 = 4.0401` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>
    Again, as `x` gets closer to `2`, `g(x)` approaches `4` <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

In summary, the [[introduction_to_limits | concept of a limit]] focuses on the value a function approaches as its input gets arbitrarily close to a certain point, irrespective of the function's actual value at that point, or even if it's defined at that point <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.