---
title: Importance in computations
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

Significant figures, sometimes referred to as significant digits, are crucial in computations to ensure that the reported result does not over-represent the amount of precision available from the initial measurements <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The core idea is to identify which digits truly convey information about the precision of a measurement <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This prevents a computed value from appearing more precise than the raw data used to derive it <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Understanding Precision through Examples

The number of significant figures directly relates to the precision of a measurement, rather than simply defining the number's magnitude <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

Consider the following:
*   A measurement of 0.00700 kilometers has three [[understanding_significant_figures | significant figures]] (the 7, 0, and 0) <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The leading zeros (0.00) are not significant because they merely shift the decimal point based on the unit of measurement <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This is evident when converting 0.00700 kilometers to 7.00 meters, which clearly shows three significant figures <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   Similarly, 0.052 kilometers would be equivalent to 52 meters, indicating two [[understanding_significant_figures | significant figures]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>, <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. Leading zeros before the first non-zero digit are generally not counted as significant <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Rules of Thumb for Identifying Significant Figures

The following general guidelines help determine [[understanding_significant_figures | significant figures]] in a given number:

*   **Non-zero digits:** All non-zero digits are significant <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Leading zeros:** Zeros before the first non-zero digit (e.g., 0.007) are not significant as they only serve to place the decimal point <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Captive zeros:** Zeros located between non-zero digits are always significant (e.g., 700.002) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Trailing zeros:**
    *   Trailing zeros *with* a decimal point are significant. For example, 7.00 meters indicates measurement to the nearest hundredth (centimeter) <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. If these zeros were not part of the measurement precision, they would typically be omitted (e.g., 7 meters instead of 7.00) <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
    *   If a number ends with zeros and includes a decimal point (e.g., 370.), all digits are significant, indicating the measurement was exact to that place value <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   Trailing zeros *without* a decimal point (e.g., 37,000) are ambiguous <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Without further information, they are typically considered non-significant, implying only the non-zero digits are precise (e.g., 37,000 would have two [[understanding_significant_figures | significant figures]] if ambiguity is present) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>, <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. To clarify precision in such cases, a decimal point is added (e.g., 37,000.) to indicate all zeros are significant <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>, <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>, <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

In summary, correctly identifying and applying [[understanding_significant_figures | significant figures]] is essential to accurately reflect the precision of measurements and computations, preventing misleading results by maintaining appropriate levels of precision throughout calculations.