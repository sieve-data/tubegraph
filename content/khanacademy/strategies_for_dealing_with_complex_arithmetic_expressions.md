---
title: Strategies for dealing with complex arithmetic expressions
videoId: ClYdw4d4OmA
---

From: [[khanacademy]] <br/> 

[[Mathematical expressions | Mathematical expressions]] must be interpreted in a consistent way to ensure a single, correct answer <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Without an agreed-upon method, a statement like "7 + 3 * 5" could yield different results depending on the order of [[arithmetic_operations | arithmetic operations]] performed <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. To avoid such ambiguity and maintain consistency in mathematics, an established **order of operations** is followed <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## The Agreed-Upon Order of Operations

The standard hierarchy for evaluating [[mathematical_expressions | mathematical expressions]] is as follows:

1.  **Parentheses** <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>: Operations enclosed within parentheses are always performed first <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
2.  **Exponents** <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>: After parentheses, evaluate any exponents <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. (e.g., 7² <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>).
3.  **Multiplication and Division** <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>: These operations have the same level of priority <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. When both are present, they are performed from left to right <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
4.  **Addition and Subtraction** <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>: These operations also have the same level of priority <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. When both are present, they are performed from left to right <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

Following this order ensures that for any given statement, a consistent answer is always reached <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Left-to-Right Rule for Same-Level Operations

When an expression contains multiple operations at the same priority level (e.g., only multiplication and division, or only addition and subtraction), these operations should be evaluated from left to right <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

For example:
*   `4 * 2 / 3 * 2` should be calculated as `(4 * 2) / 3 * 2` then `(8 / 3) * 2`, resulting in `16/3` <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   `1 + 2 - 3 + 4 - 1` should be calculated as `(1 + 2) - 3 + 4 - 1` then `(3 - 3) + 4 - 1` then `(0 + 4) - 1`, resulting in `3` <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

### Exception: All Addition or All Multiplication

If an expression contains *only* addition operations or *only* multiplication operations, the order in which they are performed does not affect the final result <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>, <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. For instance, `1 + 5 + 7 + 3 + 2` can be added in any order, and `1 * 5 * 7 * 3 * 2` can be multiplied in any order <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>, <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. However, if there is any division or subtraction mixed in, it is best to stick to the left-to-right rule for same-level operations <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Examples

### Example 1: Resolving Ambiguity

Consider the [[mathematical_expressions | mathematical expression]]: `7 + 3 * 5` <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

*   **Without Order of Operations (Incorrect)**:
    *   Reading left to right: `(7 + 3) * 5` = `10 * 5` = `50` <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **With Order of Operations (Correct)**:
    *   Multiplication takes priority over addition <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   First, `3 * 5 = 15` <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
    *   Then, `7 + 15 = 22` <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
    *   Therefore, `22` is the correct answer <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Example 2: Complex Expression Evaluation

Evaluate the expression: `(7 + 3) * 4 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

1.  **Parentheses**: Evaluate `(7 + 3)` first <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    *   `7 + 3 = 10` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   Expression becomes: `10 * 4 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
2.  **Exponents**: No exponents are present <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
3.  **Multiplication and Division** (left to right) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>:
    *   `10 * 4 = 40` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
    *   Expression becomes: `40 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
    *   `40 / 2 = 20` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   Expression becomes: `20 - 5 * 6` <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
    *   `5 * 6 = 30` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
    *   Expression becomes: `20 - 30` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
4.  **Addition and Subtraction**:
    *   `20 - 30 = -10` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

The correct interpretation of the expression is `-10` <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

Understanding and correctly applying the order of operations is fundamental to all further mathematical studies <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This concept is crucial for [[simplifying_expressions | simplifying expressions]] and working with [[understanding_mathematical_equations | equations]].