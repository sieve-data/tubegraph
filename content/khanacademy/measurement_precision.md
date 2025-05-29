---
title: Measurement precision
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

[[understanding_significant_figures | Significant figures]], sometimes called significant digits, are used to prevent over-representing the amount of precision in a computation <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The idea is that the result of a calculation should not be more precise than the initial measurements used to obtain it <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Essentially, [[rules_for_identifying_significant_figures | significant figures]] indicate which digits truly provide information about how precise a measurement is <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Identifying Significant Figures

The general approach to identifying significant figures focuses on which digits convey precision, rather than just defining the number's magnitude <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Examples and Rules

*   **Non-Zero Digits**: All non-zero digits are significant <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Leading Zeros**: Zeros that appear before the first non-zero digit are *not* significant <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
    *   **Example**: In `0.00700`, the leading zeros (`0.00`) are not significant <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Only the `7`, `0`, and `0` are significant, resulting in three significant figures <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
    *   **Reasoning**: These zeros merely shift the decimal point based on the unit of measurement and do not reflect measurement precision <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. For instance, `0.00700 kilometers` is equivalent to `7.00 meters` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. In `7.00 meters`, it's clearer that there are three significant figures because the measurement was made to the nearest centimeter <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Similarly, `0.052 kilometers` is equivalent to `52 meters`, which clearly has only two significant figures <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Zeros Between Non-Zero Digits**: Zeros located between non-zero digits *are* significant <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    *   **Example**: In `700.001`, all six digits (`7`, `0`, `0`, `0`, `0`, `1`) are significant <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. These zeros are integral to the measurement <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Trailing Zeros**:
    *   **With a Decimal Point**: Trailing zeros are significant if a decimal point is present <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
        *   **Example 1**: In `370.`, the decimal point indicates that the measurement was taken exactly to `370`, making all three digits significant <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
        *   **Example 2**: In `7.00`, the trailing zeros are significant, indicating the measurement was taken to the nearest hundredth (e.g., centimeter if units are meters) <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. The person writing the number explicitly included them to show the extent of their measurement <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. If they hadn't measured that precisely, they would have omitted these zeros <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   **Without a Decimal Point (Ambiguous)**: Trailing zeros in a whole number without an explicit decimal point are ambiguous regarding their significance <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
        *   **Example**: In `37,000`, it's unclear if the measurement was precisely `37,000` (meaning all five digits are significant) or if it was only measured to the nearest thousand (meaning only `3` and `7` are significant) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
        *   **Resolution**: If no other information is provided, typically only the non-zero digits would be considered significant <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. To remove ambiguity and indicate that all digits are significant, a decimal point should be added, e.g., `37,000.` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This explicitly states that there are five significant figures <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

### Summary of Rules

When identifying significant figures:
*   Count all non-zero digits <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   Count zeros that are located between non-zero digits <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   Count trailing zeros *only if* a decimal point is involved <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   Do *not* count leading zeros before the first non-zero digit <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.