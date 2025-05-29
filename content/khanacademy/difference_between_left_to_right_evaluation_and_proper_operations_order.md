---
title: Difference between left to right evaluation and proper operations order
videoId: ClYdw4d4OmA
---

From: [[khanacademy]] <br/> 

Mathematics requires a standard way to interpret statements to ensure consistent results <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Without an agreed-upon [[order_of_operations_introduction | order of operations]], a single mathematical statement could lead to multiple interpretations and different answers, which is unacceptable in mathematics <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## The Problem with Left-to-Right Interpretation

Consider the mathematical statement: `7 + 3 * 5` <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

If this statement were interpreted simply by reading it from left to right, one might perform the addition first:
*   `(7 + 3)` equals `10` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   Then, `10` multiplied by `5` equals `50` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
This is a natural way to interpret it if no specific order is agreed upon <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

However, another interpretation might prioritize multiplication before addition:
*   `3` multiplied by `5` equals `15` <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   Then, `7` plus `15` equals `22` <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

The same mathematical statement yields two different answers (`50` vs. `22`) based on the order of operations <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This ambiguity is "completely unacceptable" as it could lead to critical errors, such as a satellite missing its target if computers interpreted calculations differently <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This highlights the [[importance_of_a_standardized_order_of_operations | importance of a standardized order of operations]] <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## The Agreed-Upon Order of Operations

To ensure consistent interpretation and results, a standardized [[order_of_operations_introduction | order of operations]] has been established <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Following this order guarantees that everyone arrives at the same answer for a given statement <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

The hierarchy of operations is as follows:
1.  **Parentheses** (or Brackets) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
2.  **Exponents** <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a> (Though not featured in this video's examples <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>)
3.  **Multiplication and Division** (same level of priority, performed left to right) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
4.  **Addition and Subtraction** (same level of priority, performed left to right) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>

### Applying the Proper Order

Let's re-evaluate `7 + 3 * 5` using the agreed-upon [[order_of_operations_introduction | order of operations]] <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>:

1.  **Parentheses**: There are none <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
2.  **Exponents**: There are none <a class="yt>timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  **Multiplication and Division**: There is a multiplication (`3 * 5`) <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   `3 * 5 = 15` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
4.  **Addition and Subtraction**: There is an addition (`7 + 15`) <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
    *   `7 + 15 = 22` <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

Therefore, `22` is the correct interpretation of the statement <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Example with Multiple Operations

Consider a more complex expression: `(7 + 3) * 4 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

Applying the [[order_of_operations_introduction | order of operations]]:

1.  **Parentheses**: Perform the operation inside the parentheses first <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    *   `(7 + 3) = 10` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   The expression becomes: `10 * 4 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
2.  **Exponents**: There are no exponents <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
3.  **Multiplication and Division**: These operations are at the same level of priority and are performed from left to right <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   `10 * 4 = 40` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
    *   The expression is now: `40 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
    *   Next, perform the division: `40 / 2 = 20` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>, and simultaneously, the multiplication: `5 * 6 = 30` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   The expression becomes: `20 - 30` <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
4.  **Addition and Subtraction**: These operations are at the same level and are performed from left to right <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   `20 - 30 = -10` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

Thus, `-10` is the correct interpretation of the statement <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Left-to-Right for Same-Level Operations

When operations are at the same level of priority (e.g., all [[arithmetic_operations | addition]] and [[arithmetic_operations | subtraction]], or all [[arithmetic_operations | multiplication]] and [[arithmetic_operations | division]]), you should evaluate them from left to right <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

*   **Example (Addition/Subtraction)**: `1 + 2 - 3 + 4 - 1` <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>
    *   `1 + 2 = 3` <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>
    *   `3 - 3 = 0` <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>
    *   `0 + 4 = 4` <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>
    *   `4 - 1 = 3` <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>

*   **Example (Multiplication/Division)**: `4 * 2 / 3 * 2` <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>
    *   `4 * 2 = 8` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>
    *   `8 / 3 = 8/3` <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>
    *   `8/3 * 2 = 16/3` <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>

### When Order Doesn't Matter

The only time you can be flexible with the [[order_of_operations_introduction | order of operations]] is when an expression consists *only* of [[arithmetic_operations | addition]] or *only* of [[arithmetic_operations | multiplication]] <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. In such cases, the order in which you perform the operations does not affect the final result <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

*   **All Addition**: `1 + 5 + 7 + 3 + 2` <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>
*   **All Multiplication**: `1 * 5 * 7 * 3 * 2` <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>

However, if there is any mix of [[arithmetic_operations | division]] or [[arithmetic_operations | subtraction]] within a series of same-level operations, it is best to stick to the left-to-right rule <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.