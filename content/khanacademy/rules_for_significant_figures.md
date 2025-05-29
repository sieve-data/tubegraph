---
title: Rules for significant figures
videoId: eCJ76hz7jPM
---

From: [[khanacademy]] <br/> 

The concept of [[significant_figures_concept | significant figures]], sometimes called significant digits, is used to ensure that computations do not over-represent the precision of measurements [00:00:00]. The result of a calculation should not be more precise than the initial measurements used to obtain it [00:00:16].

The general idea behind [[identifying_significant_digits | identifying significant digits]] is to determine which digits truly provide information about the precision of a measurement [00:00:32].

## Rules for Identifying Significant Figures

The following rules apply to determining the number of [[significant_figures_concept | significant figures]] in a given number:

### Non-Zero Digits
All non-zero digits are considered significant [00:02:18].

### Leading Zeros
Zeros that appear before the first non-zero digit are not considered significant [00:00:53]. These zeros primarily serve to indicate the magnitude of the number and do not convey information about measurement precision [00:01:02].

> "These 0's are just shifting it based on the units of measurement that you're using." <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>

*   **Example**: In `0.00700`, the leading zeros (`0.00`) are not significant [00:00:53]. If `0.00700` kilometers were converted to `7.00` meters, it becomes clear that the leading zeros only shift the decimal point for unit conversion, not precision [00:01:11].
*   **Example**: In `0.052`, the leading zero (`0.`) is not significant [00:02:21]. This number is equivalent to `52` meters, which clearly has only two [[significant_figures_concept | significant figures]] [00:02:28].

### Trailing Zeros

*   **Trailing Zeros with a Decimal Point**: Trailing zeros (zeros at the end of a number) are significant if a decimal point is present [00:02:57]. The presence of these zeros indicates that the measurement was taken to that specific degree of precision [00:02:00].
    *   **Example**: In `0.00700`, the trailing zeros (`7.00`) are significant because they were explicitly written, indicating measurement to that level of precision [00:01:58]. If they were not measured to that precision, they would have been omitted (e.g., `7` meters instead of `7.00`) [00:02:08].
    *   **Example**: In `370.`, the decimal point explicitly indicates that the measurement is precise to the ones place, making all three digits (3, 7, and the trailing 0) significant [00:03:08].
    *   **Example**: In `23.0`, the trailing zero is significant because the decimal point indicates measurement to the nearest tenth [00:03:34].

*   **Trailing Zeros without a Decimal Point**: Trailing zeros in a whole number without an explicit decimal point create [[ambiguity_in_significant_digits | ambiguity]] [00:04:12]. It is unclear whether these zeros are part of the measurement's precision or simply placeholders for magnitude [00:04:17].
    *   **Example**: For `37,000`, it's ambiguous if the measurement was precise to the nearest one or only to the nearest thousand [00:04:14]. Without further information, it is generally assumed that only the non-zero digits are significant [00:04:36].
    *   To remove this [[ambiguity_in_significant_digits | ambiguity]] and indicate that all digits are significant, a decimal point should be added (e.g., `37,000.`) [00:04:47]. This explicitly states that all five digits are precise [00:04:52].

### Zeros Between Non-Zero Digits
Zeros that are located between non-zero digits are always considered significant [00:03:55]. These zeros are an integral part of the measured value.

*   **Example**: In `700.005`, all digits, including the zeros, are significant because the zeros are either between non-zero digits or are trailing zeros following a decimal point [00:03:55]. This number has six [[significant_figures_concept | significant digits]] [00:04:08].