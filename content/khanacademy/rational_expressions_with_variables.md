---
title: Rational expressions with variables
videoId: 7Uos1ED3KHI
---

From: [[khanacademy]] <br/> 

When working with [[mathematical_expressions | mathematical expressions]] that involve variables, the same principles used for simplifying fractions apply. These are known as rational expressions.

## Review: Simplifying Rational Numbers
When first learning about [[representation_of_rational_numbers_as_fractions | fractions]] or [[representation_of_rational_numbers_as_fractions | rational numbers]], the concept of putting them in lowest terms is introduced <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This involves identifying common factors in the numerator and denominator and then dividing them out.

For example:
*   To simplify 3/6 <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>:
    *   3 can be written as 3.
    *   6 can be written as 2 times 3 <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
    *   Since both share a common factor of 3, you can divide the numerator and denominator by 3, resulting in 1/2 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   To simplify 8/24 <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>:
    *   8 can be written as 8.
    *   24 can be written as 3 times 8 <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
    *   The common factor is 8, so dividing both by 8 gives 1/3 <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Simplifying Rational Expressions
The same principle of [[simplifying_expressions | simplifying expressions]] applies to rational expressions <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The key difference is that instead of the numerator and denominator being actual numbers, they are [[understanding_algebraic_expressions | expressions involving variables]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

The process involves factoring the numerator and the denominator to find common factors that can be cancelled out <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Example 1: `(9x + 3) / (12x + 4)`
To simplify `(9x + 3) / (12x + 4)` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:
1.  **Factor the numerator**: `9x + 3` can be factored by taking out a 3, yielding `3 * (3x + 1)` <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
2.  **Factor the denominator**: `12x + 4` can be factored by taking out a 4, yielding `4 * (3x + 1)` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  **Identify common factors**: Both the numerator and denominator have a common factor of `(3x + 1)` <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
4.  **Cancel common factors**: The `(3x + 1)` terms cancel out, leaving `3/4` <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Excluding Values for Undefined Expressions
When simplifying rational expressions, it is crucial to consider values of the [[understanding_algebraic_expressions | variable]] that would make the original expression [[excluding_values_for_undefined_rational_expressions | undefined]] <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. An expression is [[excluding_values_for_undefined_rational_expressions | undefined]] if its denominator is zero.

Even after simplification, these values must be excluded from the domain of the simplified expression to ensure it remains equivalent to the original expression <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

#### Revisit Example 1 with Exclusion
For `(9x + 3) / (12x + 4)`, the simplified form is `3/4`.
*   However, the original denominator was `12x + 4`.
*   Set `12x + 4 = 0` to find excluded values: `12x = -4`, so `x = -4/12 = -1/3` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   Therefore, the simplified expression is `3/4`, but with the condition that `x` cannot be equal to `-1/3` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Example 2: `(x^2 - 9) / (5x + 15)`
To simplify `(x^2 - 9) / (5x + 15)` <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>:
1.  **Factor the numerator**: `x^2 - 9` is a difference of squares, factoring to `(x + 3) * (x - 3)` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
2.  **Factor the denominator**: `5x + 15` can be factored by taking out a 5, yielding `5 * (x + 3)` <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
3.  **Identify and cancel common factors**: Both have `(x + 3)`, so they cancel out <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
4.  **Simplified expression**: `(x - 3) / 5` <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
5.  **Exclude values**: The original denominator `5x + 15` would be zero if `x = -3` <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   So, `(x - 3) / 5`, where `x ≠ -3` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Example 3: `(x^2 + 6x + 5) / (x^2 - x - 2)`
To simplify `(x^2 + 6x + 5) / (x^2 - x - 2)` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>:
1.  **Factor the numerator**: `x^2 + 6x + 5` factors into `(x + 5) * (x + 1)` (two numbers that multiply to 5 and add to 6 are 5 and 1) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
2.  **Factor the denominator**: `x^2 - x - 2` factors into `(x - 2) * (x + 1)` (two numbers that multiply to -2 and add to -1 are -2 and 1) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
3.  **Identify and cancel common factors**: Both have `(x + 1)`, so they cancel out <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
4.  **Simplified expression**: `(x + 5) / (x - 2)` <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
5.  **Exclude values**: The original denominator `(x - 2) * (x + 1)` would be zero if `x = 2` or `x = -1`.
    *   Therefore, the simplified expression is `(x + 5) / (x - 2)`, where `x ≠ -1` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. (Note: `x ≠ 2` is already implied by the simplified denominator, but `x ≠ -1` must be explicitly stated).

### Example 4: `(3x^2 + 3x - 18) / (2x^2 + 5x - 3)`
This example requires factoring by grouping for both the numerator and the denominator <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

#### Factoring the Numerator: `3x^2 + 3x - 18`
1.  Find two numbers that multiply to `3 * -18 = -54` and add to `3` <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. These numbers are `9` and `-6` (`9 * -6 = -54`, `9 + -6 = 3`) <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
2.  Rewrite the middle term (`3x`) using these numbers: `3x^2 + 9x - 6x - 18` <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
3.  Group terms and factor out common factors:
    ```
    (3x^2 + 9x) + (-6x - 18)
    3x(x + 3) - 6(x + 3) <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>
    ```
4.  Factor out the common binomial `(x + 3)`: `(3x - 6)(x + 3)` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
    *   The numerator is `(3x - 6)(x + 3)` <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

#### Factoring the Denominator: `2x^2 + 5x - 3`
1.  Find two numbers that multiply to `2 * -3 = -6` and add to `5` <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. These numbers are `6` and `-1` (`6 * -1 = -6`, `6 + -1 = 5`) <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
2.  Rewrite the middle term (`5x`) using these numbers: `2x^2 + 6x - x - 3` <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
3.  Group terms and factor out common factors:
    ```
    (2x^2 + 6x) + (-x - 3)
    2x(x + 3) - 1(x + 3) <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>
    ```
4.  Factor out the common binomial `(x + 3)`: `(2x - 1)(x + 3)` <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   The denominator is `(2x - 1)(x + 3)` <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.

#### Simplifying the Full Expression
Now substitute the factored forms back into the rational expression:
`(3x - 6)(x + 3) / (2x - 1)(x + 3)` <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>

1.  **Identify and cancel common factors**: Both numerator and denominator have `(x + 3)`.
2.  **Simplified expression**: `(3x - 6) / (2x - 1)` <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
3.  **Exclude values**: The original denominator `(2x - 1)(x + 3)` would be zero if `x = 1/2` or `x = -3`.
    *   Therefore, the simplified expression is `(3x - 6) / (2x - 1)`, where `x ≠ -3` <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. (Note: `x ≠ 1/2` is already implied by the simplified denominator, but `x ≠ -3` must be explicitly stated).