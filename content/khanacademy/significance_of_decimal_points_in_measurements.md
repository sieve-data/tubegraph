---
title: Significance of decimal points in measurements
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

The idea behind [[significant_figures_concept | significant figures]], sometimes called [[identifying_significant_digits | significant digits]], is to ensure that computations do not over-represent the amount of precision of the original measurements <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The result of a computation should not be more precise than the measurements used to obtain it <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The general way to think about [[significant_figures_concept | significant figures]] is to identify which digits truly convey information about the precision of a measurement <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## How Decimal Points Affect Precision

Decimal points play a crucial role in determining the [[rules_for_significant_figures | rules for significant figures]], especially concerning trailing zeros. They indicate the explicit precision to which a measurement was made.

### Trailing Zeros and Decimal Points

Trailing zeros are counted as significant if a decimal point is involved <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. The inclusion of trailing zeros after a decimal point signifies that the person taking the measurement intended to convey that level of precision <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. If they did not measure to that precision, they would have omitted those zeros <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

For example:
*   In `0.00700` kilometers, the digits `7`, `0`, and `0` after the first non-zero digit are considered significant <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This means there are three [[identifying_significant_digits | significant figures]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
    *   The leading zeros (`0.00`) are not included because they only define the number's magnitude, not its precision <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This can be understood by converting units: `0.00700` kilometers is the same as `7.00` meters <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. When expressed as `7.00` meters, it's clear that the measurement was taken to the nearest centimeter <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, and the `7`, `0`, and `0` are the digits giving precision <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Similarly, `0.052` kilometers would be equivalent to `52` meters, which clearly has two [[identifying_significant_digits | significant figures]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Leading zeros before the first non-zero digit are not counted <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   For `5.00`, the presence of the decimal point and the trailing zeros indicates that the measurement was precise to the nearest tenth <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>, resulting in three [[identifying_significant_digits | significant figures]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Decimal Points and Ambiguity

The presence or absence of a decimal point can resolve [[ambiguity_in_significant_digits | ambiguity in significant digits]] for whole numbers ending in zeros:

*   **`370.` (with decimal point):** If a decimal point is explicitly written after a whole number ending in zeros, it signifies that all digits, including the trailing zeros, are significant <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This means the measurement was exactly `370` <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>, not just rounded to the nearest tens place <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. In this case, there are three [[identifying_significant_digits | significant figures]] <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

*   **`37,000` (without decimal point):** This number is ambiguous <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. It's unclear if the measurement was exactly `37,000` to the nearest one, or if it was only measured to the nearest thousand <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Without further information, it's generally assumed to have only two [[identifying_significant_digits | significant figures]] (the `3` and the `7`) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. To make it unambiguous and indicate five [[identifying_significant_digits | significant figures]], a decimal point would be added: `37,000.` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Zeros Between Non-Zero Digits

Zeros located between non-zero digits are always considered significant, regardless of a decimal point's presence (though these examples all include one) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. For example, in `700.005`, all digits are significant, resulting in six [[identifying_significant_digits | significant digits]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.