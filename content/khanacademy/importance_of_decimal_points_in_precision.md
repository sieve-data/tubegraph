---
title: importance of decimal points in precision
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

Significant figures, sometimes called [[rules_for_identifying_significant_figures | significant digits]], are used to ensure that when a computation is performed, the result does not over-represent the amount of [[precision_in_measurements | precision]] available from the initial measurements <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The general idea is to identify which digits truly convey information about the [[precision_in_measurements | precision]] of a measurement <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Decimal points play a crucial role in indicating this [[precision_in_measurements | precision]].

## How Decimal Points Indicate Precision

The presence or absence of a decimal point, especially with trailing zeros, can dramatically change the number of [[rules_for_identifying_significant_figures | significant figures]] and thus the implied [[precision_in_measurements | precision]] of a measurement.

### Leading Zeros After a Decimal Point
Leading zeros that appear after a decimal point but before any non-zero digits are *not* considered significant <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. These zeros primarily serve as place holders and do not contribute to the [[precision_in_measurements | precision]] of the measurement; they simply shift the number based on the units being used <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

*   **Example:** In 0.00700 kilometers, the leading zeros (0.00) are not significant <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This measurement is equivalent to 7.00 meters <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, which clearly shows three [[rules_for_identifying_significant_figures | significant figures]] (7, 0, 0) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. The leading zeros only indicate the magnitude, not the precision <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Another Example:** In 0.052 kilometers, the leading zeros (0.0) are not significant <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This is the same as 52 meters, which has two [[rules_for_identifying_significant_figures | significant figures]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Trailing Zeros After a Decimal Point
Trailing zeros that appear after a non-zero digit *and* after a decimal point *are* considered significant <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Their inclusion explicitly states that the measurement was taken to that specific level of [[precision_in_measurements | precision]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. If those zeros were not measured, they would simply be left off <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

*   **Example:** In 7.00 meters, the trailing zeros are significant, indicating the measurement was precise to the nearest centimeter <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Example:** In 37.0, the trailing zero indicates that the measurement reached the nearest tenth, making it significant <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This number has three [[rules_for_identifying_significant_figures | significant figures]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Trailing Zeros in Whole Numbers

#### Explicit Decimal Point
When a decimal point is explicitly written after a whole number, even if no digits follow it, it signifies that all preceding digits, including trailing zeros, are significant <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This indicates that the measurement was exact to that unit <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

*   **Example:** In 370., the decimal point confirms that all three digits (3, 7, 0) are significant. This means the measurement was precisely 370, not rounded from a rougher measurement <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>, <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

#### Ambiguity Without a Decimal Point
Without an explicit decimal point, numbers with trailing zeros can be ambiguous regarding their [[precision_in_measurements | precision]] <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

*   **Example:** For 37,000, it is unclear whether the measurement was exactly 37,000 (precise to the ones place) or merely to the nearest thousand <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. If no additional information is provided, it's typically assumed that only the non-zero digits are significant in such a case, meaning two [[rules_for_identifying_significant_figures | significant figures]] (3 and 7) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>, <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   To remove this ambiguity and indicate that all zeros are significant, a decimal point would be added: 37,000. <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>, <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This signifies five [[rules_for_identifying_significant_figures | significant figures]] <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>, <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Zeros Between Non-Zero Digits
Zeros that are between non-zero digits are always significant, regardless of the presence of a decimal point. They are an integral part of the measured value <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

*   **Example:** In 700.005, all digits, including the zeros, are significant, resulting in six [[rules_for_identifying_significant_figures | significant digits]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>, <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.