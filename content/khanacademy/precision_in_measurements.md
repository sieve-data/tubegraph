---
title: precision in measurements
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

The concept of significant figures, sometimes called significant digits, is used to ensure that when a computation is performed, the result does not over-represent the amount of [[importance_of_decimal_points_in_precision | precision]] available from the initial measurements [00:00:10], [00:00:14], [00:00:16]. The outcome of a calculation should not be more precise than the values used to obtain it [00:00:17], [00:00:20]. The general idea is to identify which digits in a number provide meaningful information about how precise a measurement actually is [00:00:32], [00:00:34], [00:00:38].

## Rules for Identifying Significant Figures

The [[rules for identifying significant figures | rules for identifying significant figures]] help determine which digits convey precision.

### Leading Zeros

Leading zeros (zeros appearing before the first non-zero digit) are generally not considered significant figures because they primarily indicate the magnitude of the number rather than the precision of the measurement [00:00:53], [00:00:57], [00:01:02], [00:01:05].

*   **Example**: In the measurement **0.00700 kilometers** <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>:
    *   The `7`, `0`, and `0` at the end are significant figures <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, resulting in three significant figures <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
    *   The leading `0.00` are not significant <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
    *   This is clearer when converting units; 0.00700 kilometers is equivalent to 7.00 meters <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. In "7.00 meters," it becomes evident that only the 7 and the two trailing zeros contribute to the precision <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, indicating measurement to the nearest centimeter <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
    *   Similarly, **0.052 kilometers** would be 52 meters, clearly showing only two significant figures (5 and 2) <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, [00:02:28], [00:02:33].
*   **Rule of Thumb**: Do not count leading zeros before the first non-zero digit <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Trailing Zeros with a Decimal Point

Trailing zeros (zeros at the end of a number) are considered significant figures if a decimal point is present <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. The presence of these zeros explicitly indicates that the measurement was carried out to that level of precision <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, [00:02:03], [00:02:05]. If the measurement did not achieve that level of precision, these zeros would typically be omitted <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, [00:02:08].

*   **Example 1**: **370.** <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>
    *   The decimal point after 370 indicates that the measurement was exactly 370 <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, [00:03:14], [00:03:16]. This means all three digits (`3`, `7`, `0`) are significant, giving three significant figures <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, [00:03:29].
*   **Example 2**: **8.50** <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>
    *   The decimal and the trailing zero indicate measurement to the nearest tenth place <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, [00:03:40], [00:03:41]. This number has three significant figures (`8`, `5`, `0`) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, [00:03:45].

### Zeros Between Non-Zero Digits

Zeros located between non-zero digits are always considered significant because they are part of the measured value and contribute to its precision <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, [00:03:57], [00:03:59], [00:04:02].

*   **Example**: **700.040** <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>
    *   The measurement extends from the hundreds place (`7`) all the way to the thousandths place (`0` at the end) <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>, [00:03:54]. All digits (`7`, `0`, `0`, `.`, `0`, `4`, `0`) are significant, resulting in six significant digits <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>, [00:04:08].

### Ambiguity with Trailing Zeros (No Decimal Point)

When a number ends in zeros but has no decimal point, the number of significant figures can be ambiguous <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, [00:04:14].

*   **Example**: **37,000** <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>
    *   It is unclear if the measurement was exactly 37,000 (meaning all digits are significant) or if it was only measured to the nearest thousand (meaning only '3' and '7' are significant) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>, [00:04:19], [00:04:21], [00:04:25], [00:04:29].
    *   Without further information, one would typically assume only the non-zero digits are significant, leading to two significant figures (`3` and `7`) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>, [00:04:41], [00:04:46].
    *   To remove ambiguity and indicate that all zeros are significant, a decimal point should be added: **37,000.** <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>, [00:04:49]. This would imply five significant figures <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, [00:04:55], [00:04:57].

These [[examples of significant digits | examples of significant digits]] illustrate the various scenarios for determining the precision of a measurement through its written representation.