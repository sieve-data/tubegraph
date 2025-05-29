---
title: Error Correction and Data Redundancy
videoId: X8jsijhllIA
---

From: [[3blue1brown]] <br/> 

The ability to recover original information from corrupted data, such as a scratched CD or DVD, relies on sophisticated mathematical principles known as [[error_correction_codes | error correction codes]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. These methods allow data to be stored and transmitted in a way that is resilient to errors <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Even if a scratch affects the 1s and 0s on a disk, leading to different data being read, sophisticated decoding can often reconstruct the original file bit for bit <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Basic Redundancy

A straightforward, though inefficient, strategy for correcting flipped bits involves storing multiple copies of each bit <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. For example, storing three copies of each bit allows a machine to compare them and take the "best two out of three" when discrepancies arise <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

However, this method is highly inefficient, dedicating two-thirds of storage space to redundancy <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Furthermore, it offers no strong guarantee if more than one bit gets flipped <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The more interesting challenge is to correct errors while minimizing the space given up for redundancy <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

For instance, modern methods can store data in 256-bit blocks, using only 9 bits for redundancy and the remaining 247 for the actual message <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This allows a machine to identify and precisely locate a single flipped bit within the block, enabling its correction <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. If two bits are flipped, the system can detect the presence of two errors, though it cannot pinpoint their exact location for correction <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Error Correction Codes

Methods that enable error correction are broadly known as [[error_correction_codes | error correction codes]] <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This field has been a rich source of deep mathematics applied in everyday devices over the last century <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

The fundamental principle of error correction is that within the vast space of all possible messages, only a specific subset is considered "valid" <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Analogously, this is like distinguishing correctly spelled words from incorrectly spelled ones <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. If a valid message is altered, the receiver's role is to correct it back to the nearest valid message, similar to fixing a typo <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Developing efficient algorithms for this categorization requires significant ingenuity <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

While no method can guarantee 100% confidence that a received message is exactly what the sender intended (as random noise could coincidentally transform one valid message into another) <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>, the goal is to create schemes robust enough to handle a certain maximum number of errors or reduce the probability of false positives <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## [[hamming_code | Hamming Codes]]

The story of [[hamming_code | error correction codes]] begins in the 1940s with Richard Hamming at Bell Labs <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Frustrated by frequent bit errors in his punch card computer programs, Hamming invented the world's first error correction code <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. While more modern codes like the Reed-Solomon algorithm are now more widely used, [[hamming_code | Hamming codes]] remain a foundational example due to their elegant simplicity and effectiveness <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

For a deeper understanding of [[hamming_code | Hamming codes]] at the hardware level, accompanying resources exist that demonstrate their implementation on breadboards <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Parity Checks: The Building Block

Hamming's invention builds upon the concept of a [[parity_checks_and_error_detection | parity check]], a method to detect, but not correct, single bit errors <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. In a [[parity_checks_and_error_detection | parity check]], a single dedicated bit, called the [[parity_checks_and_error_detection | parity bit]], is set by the sender to ensure that the total number of '1's in the message (or a specific group of bits) is an even number <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

If any bit in the message flips (0 to 1 or 1 to 0), the total count of 1s changes from even to odd <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. The receiver, upon seeing an odd number of 1s (odd parity), can be sure an error has occurred, even if the location is unknown <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

*   **Parity:** Whether a group of bits has an even or odd number of '1's <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. It can be represented as 0 for even and 1 for odd <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **Limitations:** A [[parity_checks_and_error_detection | parity check]] only detects an *odd* number of errors (1, 3, 5, etc.) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. An even number of errors (2, 4, etc.) would result in an even count of 1s, making it appear error-free <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

While weak on their own, [[parity_checks_and_error_detection | parity checks]] are powerful building blocks for more sophisticated schemes <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

### Locating Errors with Multiple Parity Checks

Hamming's key insight was to apply multiple [[parity_checks_and_error_detection | parity checks]] not to the full message, but to carefully selected subsets of bits <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This allows for a series of questions that pinpoint the location of any single bit error, similar to a game of "20 Questions" <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

Consider a 16-bit block, with positions numbered 0 to 15 <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. In this example, 12 bits carry data, and 4 positions (specifically, those that are powers of 2: 1, 2, 4, 8) are reserved for "nuanced redundancy" <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>, <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

1.  **Parity Check 1 (Position 1):** Covers the 8 bits in odd-numbered positions (e.g., column-based check) <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. If an error is detected here, it's known to be in an odd position <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
2.  **Parity Check 2 (Position 2):** Covers the 8 bits on the right half of the block <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. If an error is detected, it's known to be in this half <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
    *   Combining these two checks allows pinpointing the specific column where an error occurred <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
3.  **Parity Check 3 (Position 4):** Covers the odd rows <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
4.  **Parity Check 4 (Position 8):** Covers the bottom two rows <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
    *   These two checks, combined, pinpoint the specific row <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

By combining the results of these four checks, any single bit error can be precisely located <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. This works even if one of the parity bits themselves is affected <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. The connection between these questions and binary counting is key to their systematic scaling <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

### The No-Error Condition and [[extending_hamming_codes_for_improved_error_detection | Extended Hamming Codes]]

A challenge arises because four "yes/no" parity checks yield 16 possible outcomes, which is perfect for pinpointing 1 out of 16 positions <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. However, a 17th outcome is needed: the "no error" condition <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

The basic solution is to disregard position 0, thus working with a 15-bit block where 11 bits carry data and 4 are for redundancy <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. This configuration is known as a 15-11 [[hamming_code | Hamming code]] <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

To achieve a 16-bit block and also detect two-bit errors, an [[extending_hamming_codes_for_improved_error_detection | extended Hamming code]] is used <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. Position 0 is used as an overarching parity bit for the entire block <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

*   **Single Bit Error:** If a single bit error occurs, the overall block parity becomes odd (from the original even), and the four internal parity checks will pinpoint the location <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
*   **Two Bit Errors:** If two errors occur, the overall parity of the block will return to even, but the four internal parity checks will still indicate discrepancies <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. By observing an even overall parity alongside non-zero results from the four internal checks, the receiver knows there were at least two errors, even if they cannot be corrected <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>. This sophisticated detection without correction is enabled by that single extra parity bit.

## Example: Encoding and Decoding a 16-Bit Block

To encode a message:
1.  Divide the message into 11-bit chunks <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
2.  For each 11-bit chunk, place the message bits into a 16-bit block, reserving positions 0, 1, 2, 4, and 8 for error correction <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.
3.  Set the parity bits at positions 1, 2, 4, and 8 according to their respective groups to ensure even parity <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
4.  Finally, set the bit at position 0 to ensure the parity of the entire 16-bit block is even <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

To decode and correct a message:
1.  Perform the four parity checks (for positions 1, 2, 4, and 8) on the received block <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
2.  The results of these checks (whether each group's parity is even or odd) will pinpoint the exact location of any single bit error <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
3.  Check the overall parity of the 16-bit block <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. If it's odd, and the other four checks pinpoint an error, it confirms a single bit flip <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>. If the overall parity is even but the other four checks show discrepancies, it indicates two (or more) errors <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
4.  Correct the identified bit by flipping its value <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
5.  Extract the 11 message bits from their non-parity positions to retrieve the original segment of data <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

This process demonstrates the efficiency of [[hamming_code | Hamming codes]], protecting messages with minimal redundancy while enabling robust error correction <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.