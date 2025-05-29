---
title: Comparison of limits and function values
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

The concept of a [[understanding_the_concept_of_limits_in_calculus | limit]] describes the value an expression [[calculating_limits_numerically_and_graphically | approaches]] as an input variable gets closer and closer to a certain point <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This differs from simply [[evaluating_expressions_with_different_variable_values | evaluating the function]] at that exact point, which is crucial when dealing with functions that have [[difference_between_undefined_points_and_values_in_a_function | undefined points]] or "jumps" <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Basic Example: Continuous Function

Consider the expression `x^2` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. To find the [[introduction_to_limits | limit]] as `x` [[understanding_limit_notation | approaches]] 2, written as `lim (x->2) x^2`, we determine what value `x^2` gets closer to as `x` approaches 2 from both sides (from numbers less than 2 and from numbers greater than 2) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

[[graphing_limits | Graphically]], the function `x^2` forms a parabola <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   As `x` approaches 2 from the left side, the value of `x^2` approaches 4 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   As `x` approaches 2 from the right side, the value of `x^2` also approaches 4 <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

Therefore, the limit as `x` approaches 2 of `x^2` is 4 <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. In this simple case, [[evaluating_expressions_with_different_variable_values | evaluating the function]] at `x=2` yields `f(2) = 2^2 = 4` <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Here, the limit is equal to the function's value at that point <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## Complex Example: Discontinuous Function

The utility of a [[understanding_the_concept_of_limits_in_calculus | limit]] becomes apparent when dealing with functions that are not continuous at a certain point <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Consider a function `f(x)` defined as:
*   `f(x) = x^2` if `x ≠ 2` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   `f(x) = 3` if `x = 2` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

[[graphing_limits | Graphically]], this function looks like the `x^2` parabola, but with a "hole" at `(2, 4)` and a defined point at `(2, 3)` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

To find the [[introduction_to_limits | limit]] as `x` [[understanding_limit_notation | approaches]] 2 for this `f(x)`:
*   As `x` approaches 2 from the left (numbers less than 2), `f(x)` follows the `x^2` curve, approaching 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   As `x` approaches 2 from the right (numbers greater than 2), `f(x)` also follows the `x^2` curve, approaching 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

Therefore, the limit as `x` approaches 2 of `f(x)` is 4 <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

However, the actual [[evaluating_expressions_with_different_variable_values | function value]] at `x=2` is explicitly defined as `f(2) = 3` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
In this case, the limit as `x` approaches 2 of `f(x)` (which is 4) does *not* equal `f(2)` (which is 3) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

## Key Distinction

The [[understanding_the_concept_of_limits_in_calculus | concept of a limit]] is distinct from merely [[evaluating_expressions_with_different_variable_values | evaluating a function]] at a point <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   A **limit** describes the value a function *approaches* as the input approaches a specific point <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. It looks at the behavior of the function *around* the point, not necessarily *at* the point itself.
*   A **function value** describes what the function *equals* at that exact point.

Limits are particularly useful in [[the_concept_of_a_limit_in_finding_derivatives | calculus]] when dealing with functions that might be [[limits_with_undefined_or_jump_function_points | undefined or jump]] at certain points, but still exhibit a clear approaching value <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. This fundamental understanding is critical for later concepts such as derivatives and integrals <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.