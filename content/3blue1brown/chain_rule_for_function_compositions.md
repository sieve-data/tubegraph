---
title: Chain rule for function compositions
videoId: YG15m2VwSjA
---

From: [[3blue1brown]] <br/> 

Most real-world functions involve mixing, combining, or tweaking simpler functions <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. To accurately model these, it's crucial to understand how to take [[understanding_derivatives_of_combined_functions | derivatives of more complicated combinations]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The goal is to develop a clear intuition for where derivative formulas come from, rather than just memorizing them <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

Functions are typically combined in three fundamental ways <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>:
1.  **Adding them together**: This gives rise to the [[sum_rule_for_derivatives | sum rule]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Subtraction is a variation of this, treated as multiplying by negative one and then adding <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
2.  **Multiplying them**: This leads to the [[product_rule_in_calculus | product rule]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Division can be seen as a form of function composition and multiplication <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
3.  **Composing them**: Throwing one function inside another, which is addressed by the [[chain_rule_in_differentiation | chain rule]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

By understanding how derivatives interact with these three combination types, one can systematically analyze even very complex expressions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This article focuses on the third method: function composition and its derivative, the [[chain_rule_in_differentiation | chain rule]].

## Understanding Function Composition

[[Complex functions and transformations | Function composition]] involves "shoving one function inside the other" <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. For example, taking `x²` and inserting it into `sin(x)` results in `sin(x²)`. The question is, what is the derivative of such a new function? <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### Visualizing Function Composition with Number Lines

To visualize the derivative of a composite function like `f(x) = sin(x²)`, a three-number-line setup can be helpful <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>:
*   **Top line**: Represents the input value `x` <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Second line**: Represents the value of the inner function, `x²` (or `h = x²`) <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Third line**: Represents the final output, `sin(x²)`, which is `sin(h)` <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

The function `x²` maps from line 1 to line 2, and `sin` maps from line 2 to line 3 <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. As `x` is adjusted, say from `1.5` to `1.5 + dx`, the value `x²` on the second line also nudges by `dx²` <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. This `dx²` can be renamed `dh` for clarity <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This `dh` then causes a nudge `d sin(h)` on the third line <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

## The Chain Rule Derivation

The derivative of the sine function is cosine <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>, meaning `d sin(h)` is approximately `cos(h) * dh` <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
Since `h = x²`, we can substitute `h` back with `x²`, so the bottom nudge is `cos(x²) * dx²` <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
The derivative of `x²` is `2x` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, so `dx²` is approximately `2x * dx` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

Combining these:
The total change in `f(x)` (or `df`) is `cos(x²) * (2x * dx)` <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
To find the derivative `df/dx`, we divide by `dx`:
`df/dx = cos(x²) * 2x` <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

This pattern reveals that the derivative of a composite function is the derivative of the outside function (evaluated at the unaltered inside function) multiplied by the derivative of the inside function <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

### The Chain Rule Formula

For any two functions `g(x)` and `h(x)`, the derivative of their composition, `g(h(x))`, is:
`d/dx [g(h(x))] = dg/dh * dh/dx` <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

In this formula:
*   `dg/dh`: Represents the derivative of the outer function `g`, evaluated with respect to the intermediate variable `h` (which is `h(x)`) <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   `dh/dx`: Represents the derivative of the inner function `h` with respect to `x` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

This symbolic representation `dg/dh * dh/dx` is a powerful reminder that the intermediate change `dh` effectively "cancels out" notationally, resulting in the desired `dg/dx` <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This cancellation is a genuine reflection of how tiny nudges propagate through the chain of functions <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

The [[chain_rule_in_backpropagation | chain rule]] is a fundamental tool for handling derivatives of functions that combine multiple smaller parts, alongside the [[sum_rule_for_derivatives | sum rule]] and [[product_rule_in_calculus | product rule]] <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Understanding the intuition behind these rules, rather than just memorizing them, allows one to naturally discover these patterns through careful thought about what a derivative truly means <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.