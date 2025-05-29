---
title: Understanding the Chain Rule for function composition in derivatives
videoId: YG15m2VwSjA
---

From: [[3blue1brown]] <br/> 

When dealing with [[taking_derivatives_of_complex_combinations_of_functions | complex combinations of functions]], there are three fundamental ways functions can be combined: addition, multiplication, and composition <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. While subtraction is a form of addition with a negative constant, and division can be seen as composition and multiplication, function composition, where one function is "shoved inside" another, is a crucial combination type <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. The [[understanding_the_chain_rule_for_function_composition_in_derivatives | Chain Rule]] provides a method for finding the derivative of such composite functions <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

## What is Function Composition?

Function composition occurs when the output of one function becomes the input of another <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. For example, if you have the function $x^2$ and the function $\sin(x)$, you can compose them to create a new function like $\sin(x^2)$ <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

## Visualizing the Chain Rule with Number Lines

To understand the derivative of a composite function like $\sin(x^2)$, a helpful visualization uses three number lines <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>:
1.  The top line represents the input value $x$ <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
2.  The second line represents the value of the inner function, $x^2$ <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
3.  The third line represents the value of the outer function applied to the inner function's result, $\sin(x^2)$ <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

As $x$ shifts, the value on the second line (e.g., $x^2$) adjusts, and consequently, the value on the third line (e.g., $\sin(x^2)$) also changes <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### The Role of Tiny Nudges

To find the derivative, consider how a tiny nudge to the input $x$ (denoted $dx$) propagates through the chain of functions <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>:

1.  **Nudge in x to nudge in inner function:** A nudge $dx$ in $x$ causes a resulting nudge in $x^2$, which can be called $dx^2$ (or $dh$, if we let $h = x^2$) <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. We know that the [[calculating_derivatives_and_algebraic_simplification_in_calculus | derivative of x squared is 2x]], meaning $dx^2 \approx 2x \cdot dx$ <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
2.  **Nudge in inner function to nudge in outer function:** This nudge $dh$ (or $dx^2$) then causes a change in the final output, $\sin(h)$, denoted $d\sin(h)$ <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. Since the [[derivatives_of_simple_functions_and_their_intuition | derivative of sine is cosine]], $d\sin(h) \approx \cos(h) \cdot dh$ <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

Combining these steps, the total change in $\sin(x^2)$ (which is $d\sin(h)$) can be expressed as:
$d\sin(h) \approx \cos(h) \cdot dh$ <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>
Substitute $h$ with $x^2$:
$d\sin(x^2) \approx \cos(x^2) \cdot dx^2$ <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>
Substitute $dx^2$ with $2x \cdot dx$:
$d\sin(x^2) \approx \cos(x^2) \cdot (2x \cdot dx)$ <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>

To find the derivative, we divide the tiny change in the function's output by the tiny change in the input $x$, $df/dx$:
$\frac{df}{dx} = \frac{d\sin(x^2)}{dx} = \cos(x^2) \cdot 2x$ <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>

## The General Chain Rule Formula

This reasoning applies to any two functions $g(x)$ and $h(x)$ <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. If you have a composite function $f(x) = g(h(x))$, its derivative is given by:

$\frac{df}{dx} = g'(h(x)) \cdot h'(x)$ <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>

In words, it's the derivative of the outside function ($g'$) evaluated on the unaltered inside function ($h(x)$), multiplied by the derivative of that inside function ($h'(x)$) <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

This pattern can also be written using Leibniz notation, which highlights the "cancellation" of intermediate variables:

$\frac{dg}{dx} = \frac{dg}{dh} \cdot \frac{dh}{dx}$ <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>

Here, $dh$ represents the change in the intermediate function $h$, and this notation serves as a reminder that the derivative of the outer function ($dg/dh$) is taken with respect to the intermediate variable $h$ (which is $x^2$ in our example) <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>. This "cancellation" is not just a notational trick but a genuine reflection of how tiny changes propagate through the functions <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

## Importance of Intuition

Understanding the [[understanding_the_meaning_and_computation_of_derivatives | meaning and computation of derivatives]] and visualizing these rules helps to see them as "natural patterns" rather than mere formulas to be memorized <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. While the [[understanding_the_chain_rule_for_function_composition_in_derivatives | Chain Rule]] can become complex in hairy situations, the underlying intuition of how tiny nudges propagate remains the same <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. Fluency with this rule, like with the [[understanding_the_sum_rule_for_derivatives | Sum Rule]] and [[applying_the_product_rule_in_derivatives | Product Rule]], requires consistent practice <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.