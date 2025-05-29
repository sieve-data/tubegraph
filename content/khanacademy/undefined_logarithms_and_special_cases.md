---
title: Undefined logarithms and special cases
videoId: mQTWzLpCcW0
---

From: [[khanacademy]] <br/> 

A [[logarithm_notation_and_conversion | logarithm]] is essentially the inverse of exponentiation <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. When evaluating a logarithm, you are determining the exponent to which a base must be raised to get a certain number <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This [[inverse_relationship_between_logarithms_and_expone nts | inverse relationship]] means there are specific cases where a logarithm might be undefined or result in special values like zero or negative numbers.

## Special Cases

### Logarithm of One
Any number raised to the power of 0 equals 1 <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. This principle applies to logarithms:
*   **Example:** To find `log base 100 of 1` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>, ask "100 to what power is equal to 1?" <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
    *   The answer is 0, because `100^0 = 1` <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
    *   Therefore, `log base 100 of 1 = 0` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

> [!INFO] Key Takeaway
> For any valid base `b` (where `b > 0` and `b ≠ 1`), `log base b of 1 = 0`.

### Logarithms Resulting in Negative Numbers
Logarithms can result in negative numbers, particularly when dealing with fractions. This relates to [[logarithms_with_fractions_and_negative_exponents | negative exponents]].
*   **Example:** To find `log base 8 of 1/64` <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>:
    *   We know `8^2 = 64` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
    *   The question becomes "8 to what power equals 1/64?" <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
    *   Using the rule for negative exponents, `8^-2` is the same as `1/(8^2)` or `1/64` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
    *   Therefore, `log base 8 of 1/64 = -2` <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
    *   Taking the inverse of the number you're finding the logarithm of will make the answer negative <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

## Undefined Logarithms

Not all logarithmic expressions can be [[evaluating_logarithmic_expressions | evaluated]] within the set of real numbers.

### Logarithm of Zero
A logarithm with an argument (the number inside the log) of zero is undefined.
*   **Example:** To find `log base 2 of 0` <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>:
    *   This asks "2 to what power `x` is equal to 0?" <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   There is no real number `x` that can satisfy `2^x = 0` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
    *   Therefore, `log base 2 of 0` is undefined or has no solution <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

### Logarithm of a Negative Number
A logarithm with a negative argument (the number inside the log) is also undefined in the real number system.
*   **Example:** To find `log base 3 of -1` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>:
    *   This asks "3 to what power `x` is equal to -1?"
    *   Assuming you are dealing with real numbers, there is no real number `x` that can make `3^x` a negative number <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   Therefore, `log base 3 of -1` is undefined <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### General Rule for Logarithm Arguments
As long as the base of the logarithm is positive, the number (argument) inside the logarithm must be greater than 0 <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. It cannot be 0 and it cannot be negative <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.