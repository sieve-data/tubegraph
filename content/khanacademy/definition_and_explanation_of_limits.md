---
title: Definition and explanation of limits
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

A [[introduction_to_limits | limit]] describes the value an expression or [[definition_of_a_function | function]] approaches as its input approaches a certain number <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Basic Concept with x-squared

Consider the expression `x squared` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The notation `limit as x approaches 2 of x squared` asks what value `x squared` approaches as `x` gets closer and closer to 2 <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

[[graphical_representation_of_limits | Graphically]], the [[definition_of_a_function | function]] `x squared` looks like a parabola <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. As `x` approaches 2 from both sides (numbers less than 2 and numbers greater than 2), the value of `x squared` approaches 4 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. In this simple case, direct [[definition_of_a_function | function evaluation]] where `f(2) = 2^2 = 4` yields the same result as the [[introduction_to_limits | limit]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Differentiating Limits from Function Evaluation

The utility of a [[introduction_to_limits | limit]] becomes clear with [[definition_of_a_function | functions]] that are not continuously defined at a specific point <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

Consider a [[definition_of_a_function | function]] `f(x)` defined as:
*   `f(x) = x squared` when `x` does not equal 2 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   `f(x) = 3` when `x` equals 2 <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

[[graphical_representation_of_limits | Graphing]] this [[definition_of_a_function | function]] shows it behaves like `x squared` everywhere except at `x = 2`. At `x = 2`, there is a "hole" in the graph at `(2, 4)` because the [[definition_of_a_function | function]] is not defined as `x squared` there <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Instead, at `x = 2`, the [[definition_of_a_function | function]]'s value "drops down" to 3, meaning `f(2) = 3` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

To find the [[introduction_to_limits | limit]] as `x` approaches 2 for this `f(x)`:
1.  As `x` approaches 2 from the left-hand side (numbers less than 2), `f(x)` approaches values closer and closer to 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
2.  Similarly, as `x` approaches 2 from the right-hand side, `f(x)` also slowly approaches 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

Therefore, the [[introduction_to_limits | limit]] as `x` approaches 2 of `f(x)` is 4 <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Key [[differences_between_limits_and_function_evaluation | Difference]]
In this example, the [[introduction_to_limits | limit]] as `x` approaches 2 of `f(x)` (which is 4) does not equal `f(2)` (which is 3) <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This illustrates the key [[differences_between_limits_and_function_evaluation | difference between a limit]] and simply [[definition_of_a_function | evaluating the function]] at that point <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. Limits are crucial when a [[definition_of_a_function | function]] might be undefined or jump at a specific point, but still approaches a particular value from either side <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Further Exploration

While this provides an intuitive understanding of limits <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, a more formal definition, such as the delta-epsilon definition, exists <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. Solving various problems can further build intuition for limits <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. Limits are foundational concepts that lead to understanding [[definition_and_application_of_derivatives | derivatives]] and integrals <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.