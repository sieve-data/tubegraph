---
title: Examples and practice problems
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

Significant figures, sometimes referred to as significant digits, are used to ensure that a large computation's result does not over-represent the amount of precision of the initial measurements. The idea is that the final result should not be more precise than the things that were actually measured to obtain it <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The general way to think about significant figures is to identify which digits are truly providing information about the precision of a measurement <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Identifying Significant Figures through Examples

Let's explore several examples to understand how to identify significant figures and develop some general rules.

### Example 1: Leading Zeros and Trailing Zeros After a Decimal
Consider the number `0.00700` <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

*   **Significant figures:** The 7, 0, and 0 are significant <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Count:** This number has three significant figures <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Explanation for leading zeros:** The zeros `0.00` before the `7` are not counted as significant. They do define the number but do not indicate the precision of the measurement <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. For instance, if `0.00700` represented kilometers, it would be equivalent to `7.00` meters <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. When expressed as `7.00` meters, it's clearer that only the `7`, `0`, and `0` indicate precision, suggesting a measurement to the nearest centimeter <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These leading zeros merely shift the decimal based on the units of measurement <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   **Explanation for trailing zeros after a decimal:** The trailing zeros (`7.00`) are counted because the person who wrote the number chose to include them, explicitly stating the level of precision achieved in the measurement <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. If they hadn't measured to that precision, they would have omitted these zeros (e.g., just `7` meters) <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Example 2: More on Leading Zeros
Consider the number `0.052` <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

*   **Significant figures:** The 5 and the 2 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Non-zero digits are always significant <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Count:** This number has two significant figures <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Explanation:** Similar to the previous example, the leading zero is not included. If `0.052` kilometers, it would be equivalent to `52` meters, which clearly has two significant figures <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Therefore, leading zeros before the first non-zero digit are generally not counted <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Example 3: Trailing Zeros with an Explicit Decimal Point
Consider the number `370.` (with a decimal point) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

*   **Significant figures:** The 3, 7, and 0 <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Count:** This number has three significant figures <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Explanation:** The presence of the decimal point after `370` explicitly indicates that the measurement was taken to the nearest one, confirming that all three digits are significant <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Example 4: Trailing Zeros After a Decimal Point
Consider the number `37.0` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

*   **Significant figures:** The 3, 7, and 0 <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Count:** This number has three significant figures <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **Explanation:** The decimal point and the trailing zero indicate that the measurement was precise to the nearest tenth <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Example 5: Zeros Between Non-Zero Digits
Consider the number `700.009` <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

*   **Significant figures:** All digits: 7, 0, 0, 0, 0, 9 <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Count:** This number has six significant figures <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Explanation:** Even though there are zeros in between, these zeros are part of the measurement because they fall between non-zero digits. The measurement extends from the hundreds place (7) down to the thousandths place (9) <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Example 6: Ambiguous Numbers
Consider the number `37,000` (without a decimal point) <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

*   **Ambiguity:** It is unclear whether the measurement was exactly `37,000` or if it was only measured to the nearest thousand (e.g., `37,000` rounded from `37,123`) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Default interpretation:** If no further information is provided, one would typically assume that only the non-zero digits are significant <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Count (default):** Two significant figures (the 3 and the 7) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **How to remove ambiguity:** To explicitly indicate that all zeros are significant (meaning five significant figures), a decimal point should be added at the end: `37,000.` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This signifies that the measurement is precise to the ones place <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Rules of Thumb for Identifying Significant Figures

Based on these examples, here are general guidelines:

*   **Non-zero digits:** All non-zero digits are significant <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Leading zeros:** Zeros that precede (come before) the first non-zero digit are **not** significant <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. They act as placeholders.
*   **Confined zeros:** Zeros located between non-zero digits are always significant <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Trailing zeros (with a decimal point):** Zeros at the end of a number are significant if a decimal point is present, either explicitly (`370.`) or by being after the decimal point (`0.00700`, `37.0`) <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Trailing zeros (without a decimal point):** Zeros at the end of a whole number without an explicit decimal point (e.g., `37,000`) are generally **not** considered significant unless additional information is given <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.