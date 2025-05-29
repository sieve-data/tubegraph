---
title: Derivative of logarithmic functions
videoId: qb40J4N1fa4
---

From: [[3blue1brown]] <br/> 

The derivative of the natural logarithm function, `ln(x)`, can be found using a technique called implicit differentiation <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. This method is particularly useful for finding the derivative of inverse functions or functions where `x` and `y` are interdependent values related by an equation, rather than `y` being an explicit function of `x` <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>, <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

## Deriving the Derivative of `ln(x)`

To find the derivative of `ln(x)`, we start with the function `y = ln(x)` <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>, <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. This graph can be viewed as an implicit curve <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. The goal is to find `dy/dx`, which represents the slope of this graph and, thus, the derivative of `ln(x)` <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

1.  **Rearrange the Equation**: First, rewrite the equation `y = ln(x)` in its exponential form, which is `e^y = x` <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>, <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. This transformation reflects the definition of the natural logarithm: `e` to the power of "what" equals `x` <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

2.  **Apply Implicit Differentiation**: Take the derivative of both sides of the rearranged equation (`e^y = x`) with respect to `x` <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. This involves asking how a tiny step with components `dx` (change in `x`) and `dy` (change in `y`) alters the value of each side of the equation <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
    *   The derivative of the left side, `e^y`, with respect to `x` (using the chain rule and knowing the [[derivatives_of_exponential_functions|derivative of e^y is e^y]]) becomes `e^y * dy` <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
    *   The derivative of the right side, `x`, with respect to `x` is `dx` <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

    To ensure that a tiny step `dx` and `dy` remains on the curve, the change to the left side must equal the change to the right side <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. This yields the equation:
    `e^y * dy = dx` <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>, <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>

3.  **Solve for `dy/dx`**: Rearrange the equation to isolate `dy/dx`, which represents the slope of the graph:
    `dy / dx = 1 / e^y` <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>, <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>

4.  **Substitute Back**: Since `e^y` is defined as `x` when on the curve `y = ln(x)`, substitute `x` back into the expression:
    `dy / dx = 1 / x` <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>, <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>

Therefore, the derivative of `ln(x)` is `1/x` <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

## Interpretation

This process demonstrates how the concept of implicit differentiation allows us to determine the rate of change of one variable with respect to another, even when their relationship isn't explicitly defined as a function of one variable in terms of the other. It extends the idea of derivatives to curves that are not simply graphs of functions <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

This approach offers a glimpse into [[multivariable_calculus|multivariable calculus]], where functions with multiple inputs are considered, and their changes are analyzed as individual inputs are tweaked <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>, <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. The core principle remains a clear understanding of the "tiny nudges" at play and their interdependencies <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>, <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The formalization of these "tiny nudges" into the idea of a derivative relies on the concept of [[derivative_definitions_and_their_relation_to_limits|limits]] <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>, <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.