---
title: Significant figures concept
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

Significant figures, sometimes called [[identifying_significant_digits | significant digits]], are used to ensure that when a computation is performed, the result does not over-represent the amount of precision present in the initial measurements <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The goal is to ensure the result is not more precise than the measurements used to obtain it <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. They indicate which digits truly provide information about the precision of a measurement <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Identifying Significant Figures

To [[identifying_significant_digits | identify significant figures]], consider which digits contribute to the precision of the measurement <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Non-Zero Digits
All non-zero digits are always significant <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Leading Zeros
Leading zeros (zeros before the first non-zero digit) are **not** significant <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. They serve only to define the number's magnitude or shift it based on units, but they do not convey precision <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a> <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

> [!example] Example 1: 0.00700 km
> This number has three significant figures: 7, 0, and 0 <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a> <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
>
> To understand why leading zeros are not significant, consider converting units:
> * 0.00700 kilometers <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
> * This is equivalent to 7.00 meters <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
>
> In "7.00 meters", it is clear there are three significant figures, indicating measurement to the nearest centimeter <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a> <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. The leading zeros in 0.00700 kilometers simply shift the decimal based on the unit <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

> [!example] Example 2: 0.052
> This number has two significant figures: 5 and 2 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a> <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. The leading zero is not included <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Similarly, 0.052 kilometers is equivalent to 52 meters, which clearly has two significant figures <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a> <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Trailing Zeros and [[significance_of_decimal_points_in_measurements | Decimal Points]]
Trailing zeros (zeros at the end of a number) are significant **if** a decimal point is present <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a> <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This is because writing these zeros explicitly states that the measurement was taken to that level of precision <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. If they were not measured to that precision, they would typically be omitted <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

> [!example] Example 1: 370.
> The presence of the decimal point after 370 indicates that all three digits, including the trailing zero, are significant <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a> <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This signifies that the measurement was exactly 370, rather than a rounded number <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Thus, it has three significant figures <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

> [!example] Example 2: 7.00
> The decimal point and the trailing zeros indicate precision to the hundredths place. This number has three significant figures <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a> <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a> <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Zeros Between Non-Zero Digits
Zeros located between non-zero digits are always significant because they are part of the measured value <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

> [!example] Example: 700.005
> In this number, every digit is significant because the zeros are either trailing zeros with a decimal point or are between non-zero digits <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a> <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Thus, it has six significant digits <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Ambiguity
When a number has trailing zeros but no decimal point, its number of significant figures can be [[ambiguity_in_significant_digits | ambiguous]] <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

> [!example] Example: 37,000
> It is unclear whether this number was measured exactly to 37,000 (meaning all zeros are significant) or if it was rounded to the nearest thousand (meaning only 3 and 7 are significant) <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a> <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
>
> In the absence of more information, it is generally assumed that only the non-zero digits are significant, giving two significant figures for 37,000 <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a> <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
>
> To remove this [[ambiguity_in_significant_digits | ambiguity]], a decimal point can be added to indicate precision to the ones place, making all trailing zeros significant <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. For example, 37,000. clearly indicates five significant figures <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a> <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

For a summary of these concepts, refer to [[rules_for_significant_figures | rules for significant figures]].