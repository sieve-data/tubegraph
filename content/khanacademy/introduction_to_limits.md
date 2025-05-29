---
title: Introduction to limits
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

The concept of a [[understanding_the_concept_of_limits_in_calculus | limit]] is fundamental in calculus <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It describes what value an expression or function "approaches" as its [[introduction_to_variables | variable]] approaches a specific number <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## [[understanding_limit_notation | Understanding Limit Notation]]

The notation for a limit is written as "the limit as x approaches 2 of x squared" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. For example, `lim (x->2) x^2` asks what value the expression x^2 approaches as x gets closer and closer to 2 <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## [[calculating_limits_numerically_and_graphically | Calculating Limits Graphically]]

One way to understand limits is by [[graphing_limits | graphing]] the function.

### Example 1: Continuous Function

Consider the function f(x) = x^2 <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

*   When x is equal to 2, the expression x^2 is equal to 4 <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   To find the [[understanding_the_concept_of_limits_in_calculus | limit]] as x approaches 2, we consider what value the expression approaches as x gets closer to 2 from both sides (from numbers less than 2 and from numbers greater than 2) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   As x gets closer and closer to 2, the expression x^2 essentially approaches 4 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   Visually, as you move along the curve closer and closer to the point where x=2, the expression's y-value approaches 4 <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

In this simple case, the [[understanding_the_concept_of_limits_in_calculus | limit]] of x^2 as x approaches 2 is 4 <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This is the same value as evaluating the function directly at x=2 (f(2) = 4) <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Example 2: Function with a Discontinuity

The concept of a [[understanding_the_concept_of_limits_in_calculus | limit]] becomes more useful when dealing with functions that have [[limits_approaching_a_point_of_discontinuity | discontinuities]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

Consider a modified function f(x) defined as:
*   f(x) = x^2, if x does not equal 2 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   f(x) = 3, when x equals 2 <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

Graphically, this function looks like the x^2 curve, but at x=2, there is a "hole" at y=4, and the function's value "jumps" to y=3 at that specific point <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

To find the [[understanding_the_concept_of_limits_in_calculus | limit]] as x approaches 2 of this new f(x):
*   As x approaches 2 from the left side (numbers less than 2), f(x) approaches values near 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   Similarly, as x approaches 2 from the right side (numbers greater than 2), f(x) also approaches values near 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   Therefore, in this case, the [[understanding_the_concept_of_limits_in_calculus | limit]] as x approaches 2 is 4 <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## [[comparison_of_limits_and_function_values | Comparison of Limits and Function Values]]

This example highlights the key difference between a [[understanding_the_concept_of_limits_in_calculus | limit]] and a function's actual value at a point:

*   For the modified function, the [[understanding_the_concept_of_limits_in_calculus | limit]] as x approaches 2 is 4 <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   However, the function's value at x=2 (f(2)) is 3 <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   Thus, in this case, the limit as x approaches 2 of f(x) does *not* equal f(2) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

This demonstrates that a [[understanding_the_concept_of_limits_in_calculus | limit]] describes the *trend* of the function as it gets arbitrarily close to a point, even if the function itself is undefined or has a different value *at* that exact point <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## Purpose of Limits

The concept of a [[understanding_the_concept_of_limits_in_calculus | limit]] provides the intuition necessary for understanding more advanced calculus topics <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. It is crucial for defining [[introduction_to_derivatives | derivatives]] and integrals, explaining why this concept was developed <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. The formal mathematical definition of a limit (the delta-epsilon definition) will be explored in a later presentation <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.