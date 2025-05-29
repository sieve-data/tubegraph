---
title: Excluding values for undefined rational expressions
videoId: 7Uos1ED3KHI
---

From: [[khanacademy]] <br/> 

When working with [[rational_expressions_with_variables | rational expressions]], it's important to understand the concept of excluding values to ensure the expression remains defined. This process is similar to simplifying traditional [[representation_of_rational_numbers_as_fractions | fractions]] to their lowest terms <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, but with an added condition for variables.

## Simplifying Rational Expressions

Just as [[definition_of_rational_numbers | rational numbers]] (fractions) can be put into lowest terms by canceling common factors in the numerator and denominator <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, the same applies to [[rational_expressions_with_variables | rational expressions]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The key difference is that [[rational_expressions_with_variables | rational expressions]] involve variables in their numerators and/or denominators <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Example 1: Factoring out a constant
Consider the expression `(9x + 3) / (12x + 4)` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
1.  Factor the numerator: `3(3x + 1)` <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
2.  Factor the denominator: `4(3x + 1)` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  The expression becomes `(3(3x + 1)) / (4(3x + 1))` <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
4.  Since `(3x + 1)` is a common factor, it can be canceled out <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    This simplifies to `3/4` <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Example 2: Factoring algebraic expressions
Consider the expression `(x^2 - 9) / (5x + 15)` <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
1.  Factor the numerator as a difference of squares: `(x + 3)(x - 3)` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
2.  Factor the denominator: `5(x + 3)` <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
3.  The expression becomes `((x + 3)(x - 3)) / (5(x + 3))` <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
4.  The common factor `(x + 3)` cancels out <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    This simplifies to `(x - 3) / 5` <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Excluding Values for Undefined Expressions

When [[simplifying_expressions | simplifying]] [[rational_expressions_with_variables | rational expressions]], it is crucial to identify and exclude values of the variable that would make the original expression [[understanding_undefined_values_in_functions | undefined]] <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. An expression becomes [[understanding_undefined_values_in_functions | undefined]] if its denominator is zero <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Consider the example `(x^2 - 9) / (5x + 15)` <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>, which simplifies to `(x - 3) / 5`.
*   The original denominator was `5x + 15`. This becomes zero if `x = -3` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   Therefore, even though the simplified expression `(x - 3) / 5` is defined at `x = -3`, the original expression is not <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   To make the simplified expression truly equivalent to the original, we must state the condition that `x ≠ -3` <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    > <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a> `(x^2 - 9) / (5x + 15) = (x - 3) / 5`, where `x ≠ -3`.

Similarly, for `(9x + 3) / (12x + 4)`, which simplifies to `3/4`:
*   The original denominator `12x + 4` is zero if `x = -1/3` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   Thus, the equivalence holds only if `x ≠ -1/3` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Example 3: Factoring quadratic expressions
Let's look at `(x^2 + 6x + 5) / (x^2 - x - 2)` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
1.  Factor the numerator: `(x + 5)(x + 1)` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
2.  Factor the denominator: `(x - 2)(x + 1)` <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
3.  The common factor `(x + 1)` cancels out <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    This simplifies to `(x + 5) / (x - 2)` <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
4.  The original denominator `(x - 2)(x + 1)` would be zero if `x = 2` or `x = -1`.
5.  Therefore, the condition `x ≠ -1` must be added to ensure equivalence <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. (Note: `x ≠ 2` is still implied by the simplified denominator).
    > <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a> `(x^2 + 6x + 5) / (x^2 - x - 2) = (x + 5) / (x - 2)`, where `x ≠ -1`.

### Example 4: Factoring by grouping
Consider the more complex expression `(3x^2 + 3x - 18) / (2x^2 + 5x - 3)` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

#### Factoring the numerator `3x^2 + 3x - 18` <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>:
1.  Find two numbers that multiply to `3 * (-18) = -54` and add to `3` <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. These numbers are `9` and `-6` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
2.  Rewrite the middle term: `3x^2 + 9x - 6x - 18` <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
3.  Factor by grouping:
    *   `3x(x + 3)` from the first two terms <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
    *   `-6(x + 3)` from the last two terms <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
4.  Combine: `(3x - 6)(x + 3)` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

#### Factoring the denominator `2x^2 + 5x - 3` <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>:
1.  Find two numbers that multiply to `2 * (-3) = -6` and add to `5` <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. These numbers are `6` and `-1` <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
2.  Rewrite the middle term: `2x^2 + 6x - x - 3` <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
3.  Factor by grouping:
    *   `2x(x + 3)` from the first two terms <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
    *   `-1(x + 3)` from the last two terms <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
4.  Combine: `(2x - 1)(x + 3)` <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

#### Simplification and Excluded Value:
The original expression becomes `((3x - 6)(x + 3)) / ((2x - 1)(x + 3))` <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
1.  The common factor `(x + 3)` cancels out <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
2.  The simplified expression is `(3x - 6) / (2x - 1)` <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
3.  Since `x + 3` was a factor of the original denominator, `x` cannot be `-3` <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.
    > <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a> `(3x^2 + 3x - 18) / (2x^2 + 5x - 3) = (3x - 6) / (2x - 1)`, where `x ≠ -3`.

Understanding and correctly stating excluded values is fundamental for accurate [[understanding_algebraic_expressions | algebraic expressions]] and their equivalence.