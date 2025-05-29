---
title: order of operations
videoId: ClYdw4d4OmA
---

From: [[khanacademy]] <br/> 

Order of operations is a fundamental concept in mathematics, providing a consistent way to interpret mathematical statements <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. A solid understanding of the order of operations is crucial as nearly all other mathematical concepts build upon it <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## The Problem Without a Standard Order

Without an agreed-upon [[order_of_operations | order of operations]], a single mathematical statement could be interpreted in multiple ways, leading to different results <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This ambiguity is unacceptable in mathematics, especially for critical applications like space missions, where misinterpretation could lead to significant errors <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

Consider the statement `7 + 3 * 5`:

*   **Interpretation 1: [[left_to_right_rule_in_operations | Left to Right]]**
    If read from left to right, one might perform the addition first, then the multiplication <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>:
    `(7 + 3) * 5`
    `10 * 5`
    `50` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>
*   **Interpretation 2: [[priority_of_multiplication_and_division | Multiplication Before Addition]]**
    Alternatively, one might prioritize multiplication over addition <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
    `7 + (3 * 5)`
    `7 + 15`
    `22` <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

As shown, these two interpretations yield different answers (50 versus 22) for the same statement <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## The Agreed-Upon Order of Operations

To ensure a single interpretation for every mathematical statement, an agreed-upon hierarchy of operations is followed <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This hierarchy dictates the sequence in which operations should be performed:

1.  **[[parentheses_and_exponents_in_arithmetic | Parentheses]]** <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>: Operations inside parentheses (or other grouping symbols like brackets) are always performed first.
2.  **[[parentheses_and_exponents_in_arithmetic | Exponents]]** <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>: After parentheses, evaluate any exponents.
3.  **Multiplication and Division** <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>: These operations have the same level of priority <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. When both are present, perform them from [[left_to_right_rule_in_operations | left to right]] <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
4.  **Addition and Subtraction** <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>: These operations also have the same level of priority <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. When both are present, perform them from [[left_to_right_rule_in_operations | left to right]] <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

```
Priority Level:
1. Parentheses
2. Exponents
3. Multiplication / Division (from left to right)
4. Addition / Subtraction (from left to right)
```

## Applying the Order of Operations

### Example 1: `7 + 3 * 5`

Using the agreed-upon order of operations:

1.  **Parentheses**: None.
2.  **Exponents**: None.
3.  **Multiplication/Division**: Perform `3 * 5` first <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    `7 + (3 * 5)`
    `7 + 15` <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>
4.  **Addition/Subtraction**: Perform `7 + 15`.
    `22` <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>

Therefore, `22` is the correct interpretation of the statement <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Example 2: `7 + 3 * 4 / 2 - 5 * 6`

Let's apply the order of operations step-by-step:

1.  **[[parentheses_and_exponents_in_arithmetic | Parentheses]]**: Perform the operation inside the parentheses first <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    `(7 + 3) * 4 / 2 - 5 * 6`
    `10 * 4 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>
2.  **[[parentheses_and_exponents_in_arithmetic | Exponents]]**: None.
3.  **Multiplication/Division**: Perform these from [[left_to_right_rule_in_operations | left to right]] <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
    *   First, `10 * 4`:
        `40 / 2 - 5 * 6` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
    *   Next, `40 / 2`:
        `20 - 5 * 6` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>
    *   Finally, `5 * 6` (before subtraction, as multiplication has priority):
        `20 - 30` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>
4.  **Addition/Subtraction**: Perform the final subtraction.
    `-10` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>

## Important Considerations

*   **Same Level Operations (e.g., Addition/Subtraction or Multiplication/Division)**: When operations are at the same level in the hierarchy, such as addition and subtraction, or multiplication and division, they should be performed strictly from [[left_to_right_rule_in_operations | left to right]] <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>, <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
    *   Example: `1 + 2 - 3 + 4 - 1`
        *   ` (1 + 2) - 3 + 4 - 1 = 3 - 3 + 4 - 1` <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>
        *   ` (3 - 3) + 4 - 1 = 0 + 4 - 1` <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>
        *   ` (0 + 4) - 1 = 4 - 1` <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>
        *   ` 3` <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>

*   **All Addition or All Multiplication**: If an expression contains *only* addition operations (e.g., `1 + 5 + 7 + 3 + 2`) or *only* multiplication operations (e.g., `1 * 5 * 7 * 3 * 2`), the order in which they are performed does not affect the outcome <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. However, this flexibility does not apply if other operations like division or subtraction are present <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.