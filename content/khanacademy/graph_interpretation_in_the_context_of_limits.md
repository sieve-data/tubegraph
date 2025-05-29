---
title: Graph interpretation in the context of limits
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

Understanding [[introduction_to_limits | limits]] often involves interpreting a [[graphical_representation_of_solutions | graph]] to determine what value an expression approaches <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This method helps to visualize the behavior of a function as its input approaches a specific value.

## Understanding the Basics

To find the [[introduction_to_limits | limit]] of an expression like `x squared` as x approaches 2, one can use its [[graphical_representation_of_solutions | graphical representation of solutions]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The graph of `x squared` resembles a parabola <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. As x approaches 2 from both the left (numbers less than 2) and the right (numbers greater than 2), the value of the expression `x squared` approaches 4 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This means the expression essentially equals 4 at that point on the curve <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

In such a straightforward case, the [[introduction_to_limits | limit]] as x approaches 2 of `f(x)` (where `f(x) = x squared`) is equal to `f(2)`, which is 4 <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This might initially seem like an unnecessary concept, as simply [[differences_between_limits_and_evaluating_functions | evaluating functions]] at the point yields the same result <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## When Limits Differ from Function Values

The utility of [[introduction_to_limits | limits]] becomes clear when dealing with functions that have [[graphical_representation_of_solutions | graphical]] discontinuities or are not defined at a specific point <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

Consider a function `f(x)` defined as:
*   `f(x) = x squared` when `x` does not equal 2 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   `f(x) = 3` when `x` equals 2 <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

### Visualizing Discontinuity

The [[graphical_representation_of_solutions | graph]] of this function is similar to `x squared`, but with a key difference at `x = 2` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. At the point where `x = 2` and `f(x)` would normally be 4, there is a "hole" or gap in the graph because the function is not defined as `x squared` at that exact point <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Instead, when `x = 2`, `f(x)` is defined as 3 <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. So, the graph has a continuous curve except for a point at `(2,4)` which is empty, and a separate point at `(2,3)` <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### Interpreting the Limit with Discontinuity

To find the [[introduction_to_limits | limit]] as `x` approaches 2 of this new `f(x)`, one still observes the behavior of the curve <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   As `x` approaches 2 from the left-hand side (values less than 2), `f(x)` approaches values close to 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   Similarly, as `x` approaches 2 from the right-hand side (values greater than 2), `f(x)` also approaches values close to 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

Therefore, the [[introduction_to_limits | limit]] as [[understanding_limits_as_x_approaches_a_value | x approaches 2]] of `f(x)` is 4 <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Key Insights

This example highlights a crucial difference between [[introduction_to_limits | limits]] and [[differences_between_limits_and_evaluating_functions | evaluating functions]]:
*   The [[introduction_to_limits | limit]] as [[understanding_limits_as_x_approaches_a_value | x approaches 2]] of `f(x)` is 4.
*   However, `f(2)` (the actual value of the function at x=2) is 3 <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

This demonstrates that a [[introduction_to_limits | limit]] describes the value an expression "approaches" regardless of whether the function is defined at that specific point, or if its definition at that point is different from the surrounding trend <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This [[graphical_representation_of_solutions | visual representation of functions and circles]] provides intuition for understanding how functions behave near points where they might be undefined or discontinuous <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.