---
title: rules for identifying significant figures
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

[[significant_figures | Significant figures]], sometimes called [[examples_of_significant_digits | significant digits]], are used to ensure that when performing computations, the result does not over-represent the [[precision in measurements | precision]] of the initial measurements <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The general idea is to identify which digits provide information about the [[precision in measurements | precision]] of a measurement <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Identifying Significant Figures: Examples and Rules

### 1. Non-Zero Digits and Trailing Zeros After a Decimal

**Example:** 0.00700 <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   **Significant Figures:** 7, 0, 0 <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   **Count:** 3 significant figures <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   **Reasoning:**
    *   Leading zeros (e.g., 0.00) are not significant because they define the number's magnitude but not its measurement [[precision in measurements | precision]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
    *   For instance, 0.00700 kilometers is equivalent to 7.00 meters <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. In "7.00 meters," it's clear there are three significant figures <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
    *   Trailing zeros (the ones after the '7' and after the decimal point) are significant because the person who recorded the measurement explicitly wrote them down to indicate the level of [[precision in measurements | precision]] achieved <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. If they hadn't measured to that precision, they would have omitted these zeros <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### 2. Leading Zeros Before Non-Zero Digits

**Example:** 0.052 <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>
*   **Significant Figures:** 5, 2 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>
*   **Count:** 2 significant figures <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
*   **Rule:** Leading zeros (zeros before the first non-zero digit) are not significant <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Reasoning:** Similar to the first example, 0.052 kilometers is the same as 52 meters, which clearly has two significant figures <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### 3. Presence of a Decimal Point for Trailing Zeros (Whole Numbers)

**Example:** 370. <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>
*   **Significant Figures:** 3, 7, 0 <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>
*   **Count:** 3 significant figures <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>
*   **Rule:** If a decimal point is explicitly written after a whole number, all trailing zeros are significant <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Reasoning:** The decimal point indicates that the measurement is exactly 370, not just rounded to the nearest tens place <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

**Example:** 370.0 <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>
*   **Significant Figures:** 3, 7, 0, 0 <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>
*   **Count:** 4 significant figures <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>
*   **Reasoning:** The trailing zero after the decimal point indicates measurement to the nearest tenth <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### 4. Zeros Between Non-Zero Digits

**Example:** 700.007 <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>
*   **Significant Figures:** All digits (7, 0, 0, 0, 0, 7) <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>
*   **Count:** 6 significant figures <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
*   **Rule:** Zeros located between non-zero digits are always significant <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Reasoning:** These zeros are part of the direct measurement and indicate [[precision in measurements | precision]] down to the thousandths place in this example <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### 5. Ambiguous Cases (Whole Numbers Without a Decimal Point)

**Example:** 37,000 <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>
*   **Ambiguity:** It's unclear whether this number was measured exactly to 37,000 or only to the nearest thousand <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Default Rule (if no additional information):** Assume only the non-zero digits are significant.
*   **Count (default):** 2 significant figures (the 3 and the 7) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **How to remove ambiguity:** To clearly indicate that all digits are significant, a decimal point should be added at the end (e.g., 37,000.) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This would then indicate five significant figures <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

---

### Summary of Rules for Identifying Significant Figures

*   All non-zero digits are significant <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   Zeros between non-zero digits are significant <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   Leading zeros (before the first non-zero digit) are NOT significant <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Trailing zeros are significant ONLY if the number contains a decimal point <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   For whole numbers ending in zeros without an explicit decimal point, the trailing zeros are generally considered non-significant unless more information is provided, making the number ambiguous <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.