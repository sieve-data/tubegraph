---
title: Rules for identifying significant figures
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

[[understanding_significant_figures | Significant figures]], sometimes called significant digits, are used to ensure that a computation's result does not over-represent the [[measurement_precision | precision]] of the original measurements <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. They indicate which digits truly provide information about how precise a measurement is <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Identifying Significant Figures through Examples

Let's explore several examples to derive the rules for identifying significant figures.

### Example 1: 0.00700

In the number 0.00700, the significant figures are 7, 0, and 0 <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, resulting in three significant figures <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

*   **Leading Zeros (before non-zero digits) are NOT significant**: The zeros after the decimal point and before the 7 (0.00) are not counted <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. While they help define the number, they do not indicate the [[measurement_precision | precision]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. For instance, 0.00700 kilometers is equivalent to 7.00 meters <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. These leading zeros merely shift the decimal based on the units of measurement <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

*   **Trailing Zeros (after non-zero digits and with a decimal) ARE significant**: The trailing zeros (the two 0s after the 7) are counted <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. If the person writing the number had not measured to that level of [[measurement_precision | precision]], they would have omitted these zeros <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Their presence indicates that the measurement was taken to that specific degree of [[measurement_precision | precision]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### Example 2: 0.052

This number has two significant figures: 5 and 2 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

*   **Non-zero digits are always significant**: The 5 and 2 are non-zero digits <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Leading Zeros are NOT significant**: Similar to the previous example, the leading zero (0.0) is not included <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. 0.052 kilometers is equivalent to 52 meters, which clearly has two significant figures <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Example 3: 370.

This number has three significant figures <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

*   **Explicit Decimal Point Makes Trailing Zeros Significant**: The presence of a decimal point after 370 indicates that the measurement was precisely 370, implying that all three digits are significant <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It means the measurement was taken exactly to the ones place, not rounded <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Example 4: 7.00

This number also has three significant figures <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

*   **Trailing Zeros after a Decimal Point are Significant**: The decimal point and the trailing zeros (00) explicitly show that the measurement was taken to the nearest tenth, making them significant <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Example 5: 700.005

This number has six significant digits <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

*   **Zeros between Non-Zero Digits are Significant**: All digits, including the zeros between the 7 and 5, are significant because they are part of the measurement and fall between non-zero digits <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The measurement extends from the hundreds place (7) down to the thousandths place (5) <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Example 6: 37,000

This number is ambiguous <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

*   **Ambiguity without a Decimal Point**: It's unclear whether 37,000 was measured precisely to the ones place or only to the nearest thousand <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Typical Interpretation (without more info)**: If no further information is provided, it is generally assumed to have two significant figures (the 3 and the 7) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Resolving Ambiguity**: To indicate that all five digits are significant (e.g., that it was measured exactly as 37,000), a decimal point should be added: 37,000. <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## General Rules of Thumb for Identifying Significant Figures

Based on these examples, here are the general rules:

*   **Non-zero digits**: All non-zero digits are significant <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Leading zeros**: Zeros that come before the first non-zero digit are not significant <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Captive zeros**: Zeros that are between two non-zero digits are significant <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Trailing zeros**:
    *   If a decimal point is present, all trailing zeros (at the end of the number) are significant <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
    *   If no decimal point is present, trailing zeros are usually considered non-significant unless more information clarifies the measurement's [[measurement_precision | precision]] <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. To explicitly show they are significant, a decimal point should be added <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

> [!tip] Purpose
> The core idea behind significant figures is to accurately represent the [[measurement_precision | precision]] of a measurement, preventing overstatement of how well something was measured <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.