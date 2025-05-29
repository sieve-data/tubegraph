---
title: Exploring function behavior at specific points
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

## Introduction to Limits

A limit describes what value an expression or function approaches as its input approaches a certain value <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. The notation for a limit is written as "the limit as x approaches 2 of x squared" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This concept helps understand function behavior, especially where direct evaluation might be misleading or impossible <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Simple Case: f(x) = x²

Consider the limit as x approaches 2 of x squared:
$$ \lim_{x \to 2} x^2 $$
This question asks: [[understanding_limits_as_x_approaches_a_value | what value does the expression x squared approach as x approaches 2?]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

Visually, when [[graphing_quadratic_functions | x squared looks something like this]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
When x is 2, the value of x squared is 4 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
As x approaches 2 from both sides (from numbers less than 2 and from numbers greater than 2), the expression x squared approaches 4 <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
The value the expression approaches is 4 <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This is intuitive because if `f(x) = x²`, then `f(2) = 4` <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Complex Case: A Piecewise Function

Consider a slightly different function, defined piecewise:
$$ f(x) = \begin{cases} x^2 & \text{if } x \neq 2 \\ 3 & \text{if } x = 2 \end{cases} $$
Now, let's ask for the limit as x approaches 2 of this new [[function_notation and examples | f of x]] <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

Graphing this function reveals a key difference from the simple x² case:
The graph looks exactly like x squared, but at x equals 2, there is a "hole" at the point (2, 4) because the function is not defined as x² at that exact point <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Instead, at x equals 2, f(x) is equal to 3 <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
So, the graph has a gap at (2, 4) and a single point at (2, 3) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

To find the limit, we still observe the behavior as x *approaches* 2.
As x approaches 2 from the left-hand side (numbers less than 2), f(x) approaches values near 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. Similarly, as x approaches 2 from the right-hand side, f(x) also slowly approaches 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
Therefore, in this case, the limit as x approaches 2 is also equal to 4 <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Why Limits Matter

The second example highlights the [[differences_between_limits_and_evaluating_functions | difference between limits and evaluating functions]] at a specific point <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
In the simple `f(x) = x²` case, `f(2) = 4`, and the limit as x approaches 2 is also 4 <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
However, for the piecewise function, while `f(2) = 3`, the limit as x approaches 2 is still 4 <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

This demonstrates that a limit describes the value a function *approaches* as its input gets arbitrarily close to a point, regardless of the function's actual value *at* that point, or even if the function is defined at all at that point <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. This concept is foundational for understanding advanced calculus topics like derivatives and integrals <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.