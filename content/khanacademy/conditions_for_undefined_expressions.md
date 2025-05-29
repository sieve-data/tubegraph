---
title: Conditions for undefined expressions
videoId: 7Uos1ED3KHI
---

From: [[khanacademy]] <br/> 

An expression becomes undefined primarily when its denominator evaluates to zero <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. This concept is crucial when working with [[rational_expressions | rational expressions]], which are expressions involving variables in both the numerator and denominator <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a> <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

## Maintaining Domain When Simplifying

When [[simplifying_expressions | simplifying]] [[rational_expressions | rational expressions]], it is essential to consider the values of variables that would have made the original expression undefined <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>. Even if a common factor cancels out, the values that made that factor zero in the original denominator must still be excluded from the domain of the simplified expression to ensure they are truly [[understanding_equivalent_expressions_in_algebra | equivalent expressions]] <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a> <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.

### Examples of Undefined Conditions

#### Example 1: Simple Linear Expression

Consider the expression:
```
9x + 3
-------
12x + 4
```
To simplify, factor both numerator and denominator <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>:
*   Numerator: `3(3x + 1)` <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>
*   Denominator: `4(3x + 1)` <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>

The expression becomes:
```
3(3x + 1)
---------
4(3x + 1)
```
The common factor `(3x + 1)` can be cancelled out <a class="yt-timestamp" data-t="02:07:00">[02:07:07]</a> <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>, resulting in `3/4` <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

However, for the original expression, the denominator `12x + 4` cannot be zero <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   If `12x + 4 = 0`
*   Then `12x = -4`
*   So `x = -4/12 = -1/3` <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>

Therefore, the simplified expression `3/4` is equivalent to the original `9x + 3 / 12x + 4` only if the condition `x ≠ -1/3` is added <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

#### Example 2: Quadratic Expression with Difference of Squares

Consider the expression:
```
x² - 9
-------
5x + 15
```
Factor the numerator (difference of squares) and the denominator <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>:
*   Numerator: `(x + 3)(x - 3)` <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>
*   Denominator: `5(x + 3)` <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>

The expression becomes:
```
(x + 3)(x - 3)
--------------
    5(x + 3)
```
The common factor `(x + 3)` can be cancelled out <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>, resulting in `(x - 3) / 5` <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

For the original expression, the denominator `5x + 15` cannot be zero <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
*   If `5x + 15 = 0`
*   Then `5x = -15`
*   So `x = -3` <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>

Thus, the simplified expression `(x - 3) / 5` is equivalent to the original `x² - 9 / 5x + 15` only if `x ≠ -3` <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.

#### Example 3: Factoring Quadratic Trinomials

Consider the expression:
```
x² + 6x + 5
------------
x² - x - 2
```
Factor both numerator and denominator <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>:
*   Numerator: `(x + 5)(x + 1)` <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>
*   Denominator: `(x - 2)(x + 1)` <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>

The expression becomes:
```
(x + 5)(x + 1)
--------------
(x - 2)(x + 1)
```
The common factor `(x + 1)` cancels out <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>, resulting in `(x + 5) / (x - 2)` <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.

For the original expression, the denominator `x² - x - 2` cannot be zero. This occurs if either `(x - 2) = 0` or `(x + 1) = 0`.
*   If `x - 2 = 0`, then `x = 2`.
*   If `x + 1 = 0`, then `x = -1` <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

To make the simplified expression `(x + 5) / (x - 2)` truly equivalent to the original, the condition `x ≠ -1` (and `x ≠ 2`) must be stated <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>. This is because the simplified expression `(x + 5) / (x - 2)` *is* defined at `x = -1`, whereas the original expression is not <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a> <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

#### Example 4: Factoring by Grouping

Consider the expression:
```
3x² + 3x - 18
-------------
2x² + 5x - 3
```
Factor both numerator and denominator using grouping <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a> <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>:
*   Numerator (`3x² + 3x - 18`): This factors into `(3x - 6)(x + 3)` <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.
*   Denominator (`2x² + 5x - 3`): This factors into `(2x - 1)(x + 3)` <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.

The expression becomes:
```
(3x - 6)(x + 3)
---------------
(2x - 1)(x + 3)
```
The common factor `(x + 3)` can be cancelled out <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>, resulting in `(3x - 6) / (2x - 1)` <a class="yt-timestamp" data-t="15:02:00">[15:02:00]</a>.

For the original expression, the denominator `(2x - 1)(x + 3)` cannot be zero <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>.
*   If `2x - 1 = 0`, then `x = 1/2`.
*   If `x + 3 = 0`, then `x = -3` <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>.

Thus, the simplified expression `(3x - 6) / (2x - 1)` is equivalent to the original `3x² + 3x - 18 / 2x² + 5x - 3` only if `x ≠ -3` (and `x ≠ 1/2`) <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.