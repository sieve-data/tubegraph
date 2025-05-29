---
title: Differences between limits and function evaluation
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

The concept of a limit in calculus is distinct from, though often related to, [[evaluating_functions | evaluating a function]] at a specific point <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. While in many simple cases the two might yield the same result, understanding their fundamental [[difference_between_expressions_and_equations | difference]] is crucial for grasping more complex functions.

## Understanding Limits

A limit, often written as "the limit as x approaches 2 of x squared" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, asks what value an [[expressions_and_their_evaluation | expression]] approaches as `x` gets closer and closer to a specific number <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This approach can be from numbers less than the target value (left side) or from numbers greater than the target value (right side) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Case 1: When the Limit Equals Function Evaluation

Consider the simple [[expressions_and_their_evaluation | expression]] `x²` <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Limit:** As `x` approaches 2, the [[expressions_and_their_evaluation | expression]] `x²` approaches 4 <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This can be visualized on a [[graphical_representation_of_limits | graph]] where, as you move along the curve of `x²` closer to `x=2` from either side, the `y` value (or the [[expressions_and_their_evaluation | expression]]'s value) gets closer to 4 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Function Evaluation:** If we define `f(x) = x²`, then [[evaluating_functions | evaluating]] `f(2)` directly gives `2² = 4` <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

In this scenario, the limit as `x` approaches 2 of `f(x)` is equal to `f(2)` <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. This might lead one to believe that [[introduction_to_limits | limits]] are a "useless concept" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a> since direct substitution yields the same answer.

## Case 2: When the Limit Differs from Function Evaluation

Consider a more complex function `f(x)` defined as:
*   `f(x) = x²` if `x ≠ 2` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   `f(x) = 3` if `x = 2` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

This function is almost identical to `x²`, but it has a "hole" at `x=2`, where its value "drops down to 3" instead of 4 <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

*   **Limit:** Even with this [[graphical_representation_of_limits | gap]] in the [[graphical_representation_of_limits | graph]] <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, as `x` approaches 2 from either the left or the right side, the value of `f(x)` still approaches 4 <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. The function's actual value at `x=2` does not affect what values the function is *approaching* <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. Therefore, the limit as `x` approaches 2 of `f(x)` is 4 <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **Function Evaluation:** [[evaluating_functions | Evaluating]] `f(2)` for this specific function yields 3, based on its definition <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

In this case, the limit as `x` approaches 2 of `f(x)` (which is 4) does *not* equal `f(2)` (which is 3) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

## Why the Distinction Matters

The ability to determine what a function *approaches* as `x` gets close to a point, even if the function is "not defined or...jumps up or down" at that exact point <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>, highlights the utility of [[introduction_to_limits | limits]]. It provides a way to analyze function behavior around specific points of interest, which is fundamental for understanding concepts like [[using_limits_to_find_the_derivative | derivatives]] and integrals in calculus <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

Further understanding of limits will involve exploring the more formal [[definition_and_explanation_of_limits | delta-epsilon definition of a limit]] <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a> and [[evaluating_limits_using_numerical_methods | solving various limit problems]] <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.