---
title: Graphing rational expressions
videoId: 7Uos1ED3KHI
---

From: [[khanacademy]] <br/> 

When [[simplifying_rational_expressions | simplifying rational expressions]], the same principles apply as when reducing fractions to their lowest terms <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. Just as with [[representations_of_rational_numbers | rational numbers]], where you identify a [[common_factors_in_rational_expressions | common factor]] in the numerator and denominator to simplify (e.g., 3/6 becomes 1/2 by dividing by 3/3) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, [[simplifying_rational_expressions | rational expressions]] involve factoring variable expressions <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

## Simplifying for Graphing

Consider a rational expression that can be simplified, such as `(9x + 3) / (12x + 4)` <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
1.  Factor the numerator: `3(3x + 1)` <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>
2.  Factor the denominator: `4(3x + 1)` <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>
3.  The expression becomes `(3(3x + 1)) / (4(3x + 1))` <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.
4.  Since `(3x + 1)` is a [[common_factors_in_rational_expressions | common factor]] in both the numerator and denominator, they can cancel out <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
5.  This simplifies to `3/4` <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

### Impact on the Graph

If you were to [[graphing_equations | graph]] `y = (9x + 3) / (12x + 4)`, it might be tempting to assume its [[graphing_equations | graph]] is simply the horizontal line `y = 3/4` <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.

However, a crucial step must be taken:
*   You **must exclude** any x-values that would have made the original denominator equal to zero <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.
*   In the example `y = (9x + 3) / (12x + 4)`, the original denominator `(12x + 4)` would be zero if `x = -1/3` <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

> [!WARNING] Point Discontinuity
> When a [[common_factors_in_rational_expressions | common factor]] is cancelled out, the simplified expression's [[graphing_equations | graph]] is not entirely identical to the original expression's [[graphing_equations | graph]]. The original expression is undefined at the x-values that made the cancelled factor zero <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. This creates a "hole" or "point discontinuity" in the [[graphing_equations | graph]] at that specific x-value <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.
>
> Therefore, for the simplified expression to be truly equivalent to the original one, you must state the condition that excludes these specific x-values <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.

For the example above, `y = (9x + 3) / (12x + 4)` is equivalent to `y = 3/4` **only if** `x ≠ -1/3` <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

## More Examples

1.  **`x^2 - 9 / 5x + 15`** <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>
    *   Factor numerator (difference of squares): `(x + 3)(x - 3)` <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>
    *   Factor denominator: `5(x + 3)` <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>
    *   Simplified expression: `(x - 3) / 5` <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>
    *   **Condition:** `x ≠ -3` (because `x + 3` was a cancelled factor, and `-3` makes the original denominator zero) <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.

2.  **`x^2 + 6x + 5 / x^2 - x - 2`** <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>
    *   Factor numerator: `(x + 5)(x + 1)` <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>
    *   Factor denominator: `(x - 2)(x + 1)` <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>
    *   Simplified expression: `(x + 5) / (x - 2)` <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>
    *   **Condition:** `x ≠ -1` (because `x + 1` was a cancelled factor) <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>.

3.  **`3x^2 + 3x - 18 / 2x^2 + 5x - 3`** <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>
    *   Factor numerator (by grouping): `(3x - 6)(x + 3)` <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>
    *   Factor denominator (by grouping): `(2x - 1)(x + 3)` <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>
    *   Simplified expression: `(3x - 6) / (2x - 1)` <a class="yt-timestamp" data-t="15:02:00">[15:02:00]</a>
    *   **Condition:** `x ≠ -3` (because `x + 3` was a cancelled factor) <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>.

The process of [[simplifying_rational_expressions | simplifying rational expressions]] is essential for accurately [[graphing_equations | graphing]] them, as it reveals points of discontinuity that are not immediately obvious from the simplified form alone <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.