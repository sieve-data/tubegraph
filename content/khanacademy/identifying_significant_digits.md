---
title: Identifying significant digits
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

[[significant_figures_concept | Significant figures]], also known as significant digits, are used in computations to ensure that the final result does not over-represent the precision of the initial measurements <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The idea is that the outcome should not be more precise than the least precise input used to obtain it <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. When identifying [[significant_figures_concept | significant figures]], the goal is to determine which digits convey information about the precision of a measurement <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Examples and Rules

Let's examine several examples to understand the [[rules_for_significant_figures | rules for significant figures]].

### Leading Zeros

Leading zeros (zeros before the first non-zero digit) are **not** considered significant because they do not indicate precision; they merely serve as placeholders for the decimal point based on the unit of measurement <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

*   **0.00700**
    *   This number has three [[significant_figures_concept | significant figures]]: the 7, and the two trailing zeros <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
    *   The leading zeros (0.00) are not counted because they only position the decimal point and do not contribute to the measurement's precision <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
    *   For instance, 0.00700 kilometers is equivalent to 7.00 meters <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. In "7.00 meters," it becomes clearer that there are three [[significant_figures_concept | significant figures]], implying measurement to the nearest centimeter <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. The trailing zeros in "7.00" indicate that the measurement was made to that level of precision; otherwise, they would have been omitted (e.g., "7 meters") <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **0.052**
    *   This number has two [[significant_figures_concept | significant figures]]: the 5 and the 2 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   The leading zeros (0.0) are not counted <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
    *   Similarly, 0.052 kilometers is the same as 52 meters, which clearly has two [[significant_figures_concept | significant figures]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Trailing Zeros and Decimal Points

Trailing zeros (zeros at the end of a number) are significant if a decimal point is present. The presence of a decimal point signals that the measurement was taken to that specific degree of precision <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

*   **370.**
    *   The explicit decimal point after the 0 indicates that all three digits are significant <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   This means the measurement was precisely 370, not rounded from a rougher measurement <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   Therefore, it has three [[significant_figures_concept | significant figures]] <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **370.0**
    *   Similar to the above, the decimal point and the trailing zero indicate that the measurement was precise to the nearest tenth <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    *   This number also has four [[significant_figures_concept | significant figures]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Zeros Between Non-Zero Digits

Zeros located between non-zero digits are always significant, as they are an integral part of the measured value <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

*   **700.050**
    *   All digits, including the zeros, are significant in this case because the measurement extends from the hundreds place (7) down to the thousandths place (last 0), and all intermediate zeros are part of that measurement <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   This number has six [[significant_figures_concept | significant figures]] <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### [[ambiguity_in_significant_digits | Ambiguity in Significant Digits]]

Numbers without an explicit decimal point can be ambiguous regarding their precision.

*   **37,000**
    *   When written simply as 37,000, it's unclear if the measurement was exactly 37,000 (meaning all zeros are significant) or if it was rounded to the nearest thousand (meaning only 37 is significant) <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
    *   Without further information, it is typically assumed to have only two [[significant_figures_concept | significant figures]] (the 3 and the 7) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
    *   To resolve this [[ambiguity_in_significant_digits | ambiguity]], a decimal point should be added if all digits are significant. For example, "37,000." (with a decimal point) would indicate five [[significant_figures_concept | significant figures]] <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This highlights the [[significance_of_decimal_points_in_measurements | significance of decimal points in measurements]].