---
title: Handling parentheses and exponents in calculations
videoId: ClYdw4d4OmA
---

From: [[khanacademy]] <br/> 

Understanding the [[order of operations]] is fundamental to all subsequent work in [[mathematics]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Its primary purpose is to ensure that there is only one way to interpret a [[mathematical_expressions | mathematical statement]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Without an agreed-upon order, a simple expression like `7 + 3 * 5` could be interpreted in two different ways, yielding either 50 or 22 <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Such ambiguity is "completely unacceptable" in mathematics, especially for critical applications like space missions <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Agreed-Upon Order of Operations

The established [[order of operations]] dictates the sequence in which operations should be performed within a [[mathematical_expressions | mathematical expression]] to arrive at a consistent and correct answer <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. The hierarchy is as follows:

1.  **Parentheses**: Operations enclosed within parentheses are performed first <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
2.  **Exponents**: Next, any operations involving [[understanding_exponents | exponents]] are calculated <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
3.  **Multiplication and Division**: These operations have the same level of priority and are performed next, from left to right <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>, <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
4.  **Addition and Subtraction**: These operations also share the same level of priority and are performed last, from left to right <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>, <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

## Handling Parentheses

Parentheses, often referred to as "curly things around numbers," delineate parts of an expression that must be computed before other operations outside them <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Example with Parentheses

Consider the expression: `7 + 3 * 5` <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
Without parentheses, the multiplication `3 * 5` is done first (yielding 15), then added to 7, resulting in 22 <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

Now, if we introduce parentheses: `(7 + 3) * 5` <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
Following the [[order of operations]], the `7 + 3` inside the parentheses is evaluated first, resulting in 10 <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Then, this result (10) is multiplied by 5, giving an answer of 50 <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### Complex Example Walkthrough

Let's look at a more complex example: `(7 + 3) * 4 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

1.  **Parentheses First**: Evaluate `(7 + 3)`, which simplifies to 10 <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    The expression becomes: `10 * 4 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
2.  **Exponents**: There are no [[exponents and radical notation | exponents]] in this expression <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
3.  **Multiplication and Division (Left to Right)**:
    *   First, `10 * 4` (leftmost multiplication) equals 40 <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
        The expression is now: `40 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
    *   Next, `40 / 2` (leftmost division) equals 20 <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   Simultaneously, `5 * 6` (the remaining multiplication) equals 30 <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
        The expression is now: `20 - 30` <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
4.  **Addition and Subtraction**:
    *   Finally, `20 - 30` equals -10 <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## Understanding Exponents

After addressing parentheses, the next priority in the [[order of operations]] is [[understanding_exponents | exponents]] <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. An exponent is represented by a small number written at the top right of a base number, indicating how many times the base number is multiplied by itself <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For example, "7 squared" would be written as `7²` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Although no examples in this discussion include exponents, it is important to remember their position in the hierarchy <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Operations at the Same Level

When multiple operations exist at the same level of priority (e.g., only multiplication and division, or only addition and subtraction), they should generally be performed from left to right <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

For instance, with addition and subtraction: `1 + 2 - 3 + 4 - 1` <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   `1 + 2 = 3` <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>
*   `3 - 3 = 0` <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>
*   `0 + 4 = 4` <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>
*   `4 - 1 = 3` <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>

However, if an expression consists *only* of addition or *only* of multiplication, the order of operations does not matter <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>, <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. For example, `1 + 5 + 7 + 3 + 2` or `1 * 5 * 7 * 3 * 2` can be calculated in any order <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>, <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. If other operations like division or subtraction are present, adhering to the left-to-right rule at the same priority level is recommended <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.