---
title: Understanding the Sum Rule for derivatives
videoId: YG15m2VwSjA
---

From: [[3blue1brown]] <br/> 

When dealing with [[calculating_derivatives_and_algebraic_simplification_in_calculus | calculating derivatives]] for functions that combine simpler forms, understanding how [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] interact with these combinations is crucial <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Most functions used in modeling involve mixing, combining, or tweaking simple functions <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The foundational rules for these combinations are addition, multiplication, and composition <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. While subtraction and division can be considered, they are fundamentally variations of addition and multiplication with [[understanding_the_chain_rule_for_function_composition_in_derivatives | function composition]] (e.g., division by `x` is `1/x` composed with the function and then multiplied) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

Knowing how [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] apply to these three basic combination types allows one to systematically approach even the most complex expressions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## The Sum Rule

The Sum Rule is the most straightforward of the derivative combination rules <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
Simply put:

> The derivative of a sum of two functions is the sum of their [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

This means if you have a function `f(x) = g(x) + h(x)`, then `f'(x) = g'(x) + h'(x)`.

### Visualizing the Sum Rule with Tiny Nudges

To grasp the intuition behind the Sum Rule, especially before delving into the more complex [[applying_the_product_rule_in_derivatives | product rule]] and [[understanding_the_chain_rule_for_function_composition_in_derivatives | chain rule]], consider what it means to take the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of a sum of two functions <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

Let's use the example: `f(x) = sin(x) + x^2` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
This function's value at any input `x` is the sum of `sin(x)` and `x^2` at that point <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

1.  **Representing the Sum:** Imagine at a specific `x` (e.g., `x = 0.5`), `sin(x)` is a vertical bar of a certain height, and `x^2` is another vertical bar <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. The sum `f(x)` is the total length obtained by stacking these two bars <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

2.  **Introducing a Nudge (dx):** To find the [[understanding_the_meaning_and_computation_of_derivatives | derivative]], we ask what happens to `f(x)` as you nudge the input `x` slightly to `x + dx` <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. The resulting difference in `f`'s value, `df`, represents the change in the total stacked height <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

3.  **Components of Change:** When visualizing this, it becomes clear that the total change in height (`df`) is simply the sum of the change in the sine graph's height (`d sin(x)`) and the change in the `x^2` graph's height (`d x^2`) <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

    *   We know the [[understanding_the_meaning_and_computation_of_derivatives | derivative of sin(x)]] is `cos(x)` <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This means `d sin(x)` is approximately `cos(x) * dx` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   Similarly, the [[understanding_the_meaning_and_computation_of_derivatives | derivative of x^2]] is `2x` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. So, `d x^2` is approximately `2x * dx` <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

4.  **Deriving the Sum Rule:**
    Since `df = d sin(x) + d x^2` <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, we can substitute the expressions for the tiny changes:
    `df ≈ cos(x) * dx + 2x * dx` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>

    Dividing by `dx` to find the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] (`df/dx`):
    `df/dx ≈ cos(x) + 2x` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>

    This result, `cos(x) + 2x`, is indeed the sum of the [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] of `sin(x)` and `x^2` <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

This intuitive visualization reinforces that the change in a sum of functions is simply the sum of the individual changes in each component function. This direct relationship is why the Sum Rule is relatively straightforward compared to the [[applying_the_product_rule_in_derivatives | Product Rule]] or [[understanding_the_chain_rule_for_function_composition_in_derivatives | Chain Rule]].

---

### Constant Multiplier Rule

If a function is multiplied by a constant, e.g., `2 * sin(x)`, its [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is simply the constant multiplied by the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of the function <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. For `2 * sin(x)`, the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is `2 * cos(x)` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This rule can be seen as a simpler case of the [[applying_the_product_rule_in_derivatives | product rule]] where one of the functions is a constant.

---

Ultimately, the Sum Rule, along with the [[applying_the_product_rule_in_derivatives | Product Rule]] and [[understanding_the_chain_rule_for_function_composition_in_derivatives | Chain Rule]], are essential tools for [[taking_derivatives_of_complex_combinations_of_functions | handling derivatives of complex combinations of functions]] <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Understanding their derivation provides a deeper intuition beyond mere memorization <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.