---
title: Differences between limits and evaluating functions
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

## Introduction to Limits
A limit describes the value an [[difference_between_expressions_and_equations | expression]] approaches as its [[role_of_variables_in_expressions | variable]] gets closer and closer to a specific point <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. It's written in the form "the [[introduction_to_limits | limit]] as [[understanding_limits_as_x_approaches_a_value | x approaches]] a certain value" <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Case 1: Simple Function (No Discontinuity)
Consider the [[introduction_to_limits | limit]] as [[understanding_limits_as_x_approaches_a_value | x approaches 2]] of x squared <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
When [[graph_interpretation_in_the_context_of_limits | graphing]] the function `f(x) = x^2`, as [[understanding_limits_as_x_approaches_a_value | x approaches 2]] from both sides (numbers less than 2 and numbers greater than 2), the [[difference_between_expressions_and_equations | expression]] `x^2` approaches 4 <a class="yt-timestamp" data-t="01:27">[01:27]</a>, <a class="yt-timestamp" data-t="01:33">[01:33]</a>.

On the [[graph_interpretation_in_the_context_of_limits | graph]], as you [[graph_interpretation_in_the_context_of_limits | move on the curve]] closer to where `x` is 2, the `y` (or `f(x)`) value approaches 4 <a class="yt-timestamp" data-t="02:04">[02:04]</a>, <a class="yt-timestamp" data-t="02:08">[02:08]</a>.
In this scenario, evaluating the function at `x = 2` (i.e., `f(2)`) also yields 4 <a class="yt-timestamp" data-t="02:23">[02:23]</a>, <a class="yt-timestamp" data-t="02:27">[02:27]</a>. This might lead one to believe the concept of a limit is unnecessary <a class="yt-timestamp" data-t="02:14">[02:14]</a>, <a class="yt-timestamp" data-t="02:17">[02:17]</a>.

## Case 2: Function with a Discontinuity at a Specific Point
Consider a new function, `f(x)`, defined as:
*   `f(x) = x^2` when `x` does not equal 2 <a class="yt-timestamp" data-t="02:36">[02:36]</a>, <a class="yt-timestamp" data-t="02:51">[02:51]</a>
*   `f(x) = 3` when `x` equals 2 <a class="yt-timestamp" data-t="02:59">[02:59]</a>

### Graphing the Function
This function's [[graph_interpretation_in_the_context_of_limits | graph]] is similar to `x^2`, but with a "hole" at the point where `x = 2` and `f(x) = 4` <a class="yt-timestamp" data-t="03:50">[03:50]</a>, <a class="yt-timestamp" data-t="04:02">[04:02]</a>. The function is not defined at `x = 2` on the `x^2` curve <a class="yt-timestamp" data-t="04:04">[04:04]</a>, <a class="yt-timestamp" data-t="04:08">[04:08]</a>. Instead, when `x = 2`, `f(x)` is equal to 3, creating a single point at `(2, 3)` <a class="yt-timestamp" data-t="04:19">[04:19]</a>, <a class="yt-timestamp" data-t="04:23">[04:23]</a>.

### Calculating the Limit
To find the [[introduction_to_limits | limit]] as [[understanding_limits_as_x_approaches_a_value | x approaches 2]] for this new `f(x)` <a class="yt-timestamp" data-t="03:23">[03:23]</a>, <a class="yt-timestamp" data-t="05:12">[05:12]</a>:
*   As [[understanding_limits_as_x_approaches_a_value | x approaches 2]] from the left side (numbers less than 2), `f(x)` approaches 4 <a class="yt-timestamp" data-t="05:23">[05:23]</a>, <a class="yt-timestamp" data-t="05:35">[05:35]</a>.
*   Similarly, as [[understanding_limits_as_x_approaches_a_value | x approaches 2]] from the right side, `f(x)` also approaches 4 <a class="yt-timestamp" data-t="05:54">[05:54]</a>, <a class="yt-timestamp" data-t="05:57">[05:57]</a>.

Therefore, the [[introduction_to_limits | limit]] as [[understanding_limits_as_x_approaches_a_value | x approaches 2]] of `f(x)` is 4 <a class="yt-timestamp" data-t="06:13">[06:13]</a>, <a class="yt-timestamp" data-t="06:15">[06:15]</a>.

### The Key Difference
In this second case, the [[introduction_to_limits | limit]] as [[understanding_limits_as_x_approaches_a_value | x approaches 2]] of `f(x)` (which is 4) does **not** equal `f(2)` (which is 3) <a class="yt-timestamp" data-t="06:24">[06:24]</a>, <a class="yt-timestamp" data-t="06:35">[06:35]</a>.

This demonstrates the crucial difference:
*   **Evaluating a function at a point** gives the actual [[understanding_inputs_and_outputs_in_functions | output]] value of the function *at that exact point* <a class="yt-timestamp" data-t="06:41">[06:41]</a>.
*   A **limit** describes the value the function *approaches* as the [[role_of_variables_in_expressions | input]] approaches a specific point, regardless of what the function's actual value is at that point, or if it's even defined there <a class="yt-timestamp" data-t="06:51">[06:51]</a>, <a class="yt-timestamp" data-t="06:53">[06:53]</a>. This concept is particularly useful when [[exploring_function_behavior_at_specific_points | functions]] have discontinuities or undefined points <a class="yt-timestamp" data-t="06:57">[06:57]</a>, <a class="yt-timestamp" data-t="07:01">[07:01]</a>.

> [!NOTE]
> While a formal delta-epsilon definition of a limit exists, understanding limits often begins with this intuitive [[graph_interpretation_in_the_context_of_limits | graphical interpretation]] <a class="yt-timestamp" data-t="07:08">[07:08]</a>, <a class="yt-timestamp" data-t="07:12">[07:12]</a>. The practical application of limits becomes clearer when moving into calculus concepts like derivatives and integrals <a class="yt-timestamp" data-t="07:28">[07:28]</a>, <a class="yt-timestamp" data-t="07:30">[07:30]</a>.