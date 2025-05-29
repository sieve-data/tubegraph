---
title: examples of significant digits
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

[[significant figures | Significant figures]], also known as significant digits, are used to ensure that computations do not over-represent the amount of [[precision in measurements | precision]] present in the original measurements <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The goal is to determine which digits genuinely provide information about how precise a measurement is <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Identifying Significant Figures

Here are several examples demonstrating how to identify [[significant figures | significant figures]]:

### Example 1: 0.00700 kilometers

In this number, the significant figures are the 7, 0, and 0 <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This means there are three [[significant figures | significant figures]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

*   **Leading zeros (0.00):** These zeros are not counted as significant <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. While they define the number's magnitude, they do not indicate the measurement's [[precision in measurements | precision]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
    *   For instance, 0.00700 kilometers is equivalent to 7.00 meters <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. When expressed as 7.00 meters, it becomes clearer that only the 7, 0, and 0 convey the [[precision in measurements | precision]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The leading zeros simply shift the decimal based on the unit of measurement <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   **Trailing zeros (after the 7):** These zeros *are* significant because their inclusion implies a deliberate measurement to that level of [[precision in measurements | precision]] <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. If the measurement wasn't precise to these digits, they would typically be omitted (e.g., writing "7 meters" instead of "7.00 meters") <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Example 2: 0.052 kilometers

Following the same logic, only the 5 and 2 are significant <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. The leading zeros (0.0) are not included <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Similar to the previous example, 0.052 kilometers is the same as 52 meters <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>, which clearly has two [[significant figures | significant figures]] <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

### Example 3: 370.

This number has three [[significant figures | significant figures]] <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. The presence of the decimal point at the end is crucial here <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   The decimal point explicitly indicates that the measurement was taken precisely to 370, rather than being rounded <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This demonstrates the [[importance of decimal points in precision | importance of decimal points]] in clarifying [[precision in measurements | precision]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Example 4: 43.0

This number also has three [[significant figures | significant figures]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   The decimal point and the trailing zero indicate that the measurement was taken to the nearest tenth, not just the nearest whole number <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Example 5: 700.005

All digits in this number are significant, totaling six [[significant figures | significant figures]] <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   The measurement extends all the way down to the thousandths place <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   Zeros located between non-zero digits are always considered part of the measurement and are thus significant <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Example 6: 37,000

This number is ambiguous regarding its [[significant figures | significant figures]] <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   It's unclear if the measurement was precisely 37,000 (measured to the nearest one) or if it was only measured to the nearest thousand (meaning the trailing zeros are placeholders) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   Without additional information, one would typically assume only two [[significant figures | significant figures]] (the 3 and the 7) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   To remove ambiguity and indicate that all five digits are significant, a decimal point would be added at the end: `37,000.` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This explicitly states that the [[precision in measurements | precision]] extends to the ones place <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

## Rules of Thumb for Identifying Significant Figures

Based on these examples, general [[rules for identifying significant figures | rules of thumb]] can be formed:

*   **Non-zero digits:** All non-zero digits are always significant <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Leading zeros:** Zeros that appear before the first non-zero digit are not significant <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. They serve to position the decimal point.
*   **Captive zeros:** Zeros located between non-zero digits are always significant <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Trailing zeros:**
    *   If a decimal point is present, trailing zeros (zeros at the end of the number) are significant <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This shows the explicit [[precision in measurements | precision]] of the measurement <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
    *   If no decimal point is present, trailing zeros may or may not be significant, leading to ambiguity <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. It is generally assumed that only the non-zero digits and any captive zeros are significant in such cases, unless specified otherwise (e.g., by adding a decimal point at the end) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.