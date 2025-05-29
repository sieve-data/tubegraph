---
title: Understanding significant figures
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

Significant figures, sometimes referred to as significant digits, are used to ensure that when large computations are performed, the result does not over-represent the precision of the initial measurements <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The idea is that the final result should not be more precise than the measurements that were used to obtain it <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. They indicate which digits truly provide information about the precision of a measurement <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Identifying Significant Figures

Here are examples demonstrating how to identify significant figures:

### Example 1: Leading Zeros and Trailing Zeros After Decimal

Consider the number `0.00700` <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

*   The significant figures are 7, 0, and 0 <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   This number has three significant figures <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   The leading zeros (e.g., `0.00`) are not included because they indicate the magnitude of the number rather than the precision of the measurement <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For instance, `0.00700` kilometers is equivalent to `7.00` meters <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. In `7.00` meters, it's clear there are three significant figures <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   The trailing zeros (the two '0's after the '7') are significant because the person who wrote the number chose to include them, explicitly stating the measurement's precision <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. If they had not measured to that level of precision, they would have omitted these zeros <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Example 2: More on Leading Zeros

For the number `0.052` <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>:

*   The significant figures are 5 and 2 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   This number has two significant figures.
*   Similar to the first example, the leading zeros (e.g., `0.0`) are not significant <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. `0.052` kilometers is the same as `52` meters, which clearly has two significant figures <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Example 3: Trailing Zeros with an Explicit Decimal Point

For the number `370.` (with a decimal point) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>:

*   The significant figures are 3, 7, and 0 <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   This number has three significant figures <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   The decimal point explicitly indicates that the measurement was made to the ones place, meaning the trailing zero is significant <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Example 4: Trailing Zeros After a Decimal Point

For the number `3.70` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>:

*   The significant figures are 3, 7, and 0 <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   This number has three significant figures <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   The trailing zero after the decimal point indicates precision to the nearest tenth <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Example 5: Zeros Between Non-Zero Digits

For the number `700.008` <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>:

*   All digits are significant: 7, 0, 0, 0, 0, and 8 <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   This number has six significant figures <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   Zeros that fall between non-zero digits are always considered part of the measurement and are therefore significant <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Example 6: Ambiguous Trailing Zeros

For the number `37,000` (without a decimal point) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>:

*   This representation is ambiguous <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. It's unclear if the measurement was precisely 37,000 or if it was rounded to the nearest thousand <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   Without additional information, one would typically assume there are two significant figures (3 and 7) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   To clarify that all five digits are significant, a decimal point would be added: `37,000.` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This explicitly states the measurement's precision <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Rules of Thumb for Identifying Significant Figures

While the examples provide a good understanding, these general [[rules_for_identifying_significant_figures | rules]] can be applied:

*   **Non-zero digits**: All non-zero digits are always significant <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Leading zeros**: Zeros that precede all non-zero digits (e.g., `0.00` in `0.00700`) are *not* significant <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. They are merely placeholders for the decimal point.
*   **Trailing zeros**:
    *   Trailing zeros are significant if the number contains a decimal point (e.g., `7.00`, `370.`, `3.70`) <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
    *   Trailing zeros in numbers without a decimal point are ambiguous and generally considered non-significant unless otherwise specified (e.g., `37,000`) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Contained zeros**: Zeros located between non-zero digits are always significant (e.g., `700.008`) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

The purpose of significant figures is to accurately represent the [[importance_in_computations | precision]] of measurements and computations <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.