---
title: significant figures
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

[[Significant figures]], sometimes referred to as [[examples_of_significant_digits | significant digits]], are used to ensure that computations accurately represent the [[precision_in_measurements | precision]] of the original measurements involved <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The concept prevents over-representing the amount of precision, ensuring that a result is not more precise than the measurements used to obtain it <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The goal is to identify which digits truly provide information about the measurement's precision <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Identifying Significant Figures: Examples

Here are [[examples_of_significant_digits | examples]] demonstrating how to identify significant figures:

### Example 1: Leading Zeros
Consider the number `0.00700` <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
In this case, the significant figures are `7`, `0`, and `0`, resulting in three significant figures <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The leading zeros (those after the decimal point but before the first non-zero digit) are not considered significant <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. While they define the number's magnitude, they do not indicate the measurement's [[precision_in_measurements | precision]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

For instance, `0.00700 kilometers` is equivalent to `7.00 meters` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. If the original measurement was `7.00 meters` (measured to the nearest centimeter), the three significant figures (`7`, `0`, `0`) clearly indicate this precision <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The leading zeros in the kilometer conversion merely shift the decimal based on units, not indicating greater precision <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### Example 2: Non-Zero Digits and Leading Zeros
For `0.052`, the significant figures are `5` and `2`, totaling two significant figures <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Non-zero digits are always significant <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. Similar to the previous example, leading zeros before the first non-zero digit are not counted <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. For example, `0.052 kilometers` is the same as `52 meters`, which clearly has two significant figures <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Example 3: Trailing Zeros with a Decimal Point
In the number `370.`, the presence of the decimal point makes all three digits significant <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. If the decimal point were omitted, the precision would be unclear <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. The explicit decimal point indicates that the measurement was taken exactly to `370`, rather than being a rounded number or approximate to the tens place <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

Similarly, `3.70` has three significant figures <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. The trailing zero after the decimal point indicates that the measurement was taken to the nearest tenth, confirming its significance <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Trailing zeros after a decimal point are considered significant because they explicitly show the level of precision to which a measurement was made <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Example 4: Zeros Between Non-Zero Digits
For `700.005`, all six digits are significant <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The zeros between the non-zero digits (`7` and `5`) are part of the measurement and contribute to its precision <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Example 5: Ambiguity Without a Decimal Point
The number `37,000` is ambiguous <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. It's unclear if the measurement was precisely `37,000` (implying measurement to the nearest one) or if it was only measured to the nearest thousand <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Without further information, it's generally assumed to have only two significant figures (the `3` and `7`) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. To clarify, adding a decimal point, e.g., `37,000.`, would indicate five significant figures of precision <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## [[rules_for_identifying_significant_figures | Rules for Identifying Significant Figures]]

Based on the examples, here are general [[rules for identifying significant figures | rules of thumb]]:
*   **Non-zero digits:** All non-zero digits are significant <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Leading zeros:** Zeros that appear before the first non-zero digit are *not* significant <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. They serve as placeholders for magnitude.
*   **Trailing zeros:** Zeros at the end of a number are significant *if* a decimal point is present <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a> <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. If no decimal point is present, trailing zeros may be ambiguous and are typically not counted as significant unless specified <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Captured (or Sandwiched) zeros:** Zeros located between two non-zero digits are always significant <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **The [[importance of decimal points in precision | importance of decimal points]]:** A decimal point explicitly indicates that all digits, including any trailing zeros, are significant, signifying a higher level of [[precision_in_measurements | precision]] <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.