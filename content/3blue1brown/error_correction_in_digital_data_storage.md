---
title: Error correction in digital data storage
videoId: X8jsijhllIA
---

From: [[3blue1brown]] <br/> 

Digital data, whether stored on a CD/DVD or transmitted, is represented by sequences of 1s and 0s <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Even if a physical medium like a CD is scratched, affecting these 1s and 0s, the data can often still be played back accurately <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This resilience against errors is due to [[concepts_in_information_theory_and_coding_theory | mathematical cleverness]] that allows data to be stored and transmitted robustly <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## The Challenge of Redundancy

A naive approach to error correction involves storing multiple copies of each bit. For instance, storing three copies of every bit would allow a machine to compare them and take the best two out of three when a discrepancy occurs <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. However, this method is highly inefficient, using two-thirds of the storage space for redundancy, and offers no strong guarantee against multiple bit flips <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

The core challenge in [[basics_of_error_correction_schemes | error correction schemes]] is to enable error correction while minimizing the amount of space given up for redundancy <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. For example, a more advanced method can use 9 bits for redundancy within a 256-bit block, allowing 247 bits for meaningful data <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. With this approach, a single bit flip can be identified and precisely corrected within the block <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. If two bits are flipped, the system can detect that errors occurred but not pinpoint their location for correction <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

Methods that allow such error correction are known as [[error_correction_and_hamming_codes | error correction codes]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This field has been a rich source of deep mathematics applied in everyday devices <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## The Genesis of [[history_and_significance_of_hamming_codes | Hamming Codes]]

One of the earliest and foundational examples of [[error_correction_and_hamming_codes | error correction codes]] is the [[history_and_significance_of_hamming_codes | Hamming code]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The story begins in the 1940s with Richard Hamming at Bell Labs <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Frustrated by frequent program failures due to bit misreads on a punch card computer, Hamming invented the world's first [[error_correction_and_hamming_codes | error correction code]] <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

While [[history_and_significance_of_hamming_codes | Hamming codes]] are not as widely used as more modern codes like the Reed-Solomon algorithm, they offer a clear and elegant demonstration of the core principles of error correction <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. [[practical_implementation_of_error_correction_algorithms | Ben Eater]] has produced a video demonstrating the [[practical_implementation_of_error_correction_algorithms | practical implementation of Hamming codes]] on breadboards <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### The Basic Principle of Error Correction

The fundamental principle of [[error_correction_and_hamming_codes | error correction]] is that within the vast space of all possible messages, only a specific subset is considered valid <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. When a valid message is altered, the receiver's role is to correct the observed data back to the nearest valid message, much like correcting a typo <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. The challenge lies in creating an efficient algorithm to categorize messages and perform these corrections <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

It is important to note that no error detection or correction method can provide 100% confidence that a received message is identical to the sender's original, as random noise could coincidentally transform one valid message into another <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. The objective is to design schemes that are robust up to a certain maximum number of errors or to reduce the probability of false positives <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## [[basics_of_error_correction_schemes | Basics of Error Correction Schemes]]: Parity Checks

A foundational concept in [[error_correction_and_hamming_codes | error correction]] is the [[understanding_parity_checks | parity check]] <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. A [[understanding_parity_checks | parity check]] uses a single designated bit, called a parity bit, to ensure that the total number of 1s in a given block of data is either even or odd (depending on the system's design) <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. For example, if a block needs an even number of 1s and currently has an odd count, the sender flips the parity bit to make the total even <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

If any bit in the message (including the parity bit) is flipped, the total count of 1s will change from even to odd, or vice versa <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This allows the receiver to detect that an error has occurred <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. The property of a group of bits having an even or odd number of 1s is known as its parity <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

While a single [[understanding_parity_checks | parity check]] can detect any odd number of errors (1, 3, 5, etc.), it cannot determine the location of the error, nor can it detect an even number of errors (2, 4, etc.) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Despite this limitation, [[understanding_parity_checks | parity checks]] are powerful building blocks for more sophisticated schemes <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

## Pinpointing Errors with Multiple Parity Checks

Hamming's key insight was that by applying multiple [[understanding_parity_checks | parity checks]] to carefully selected subsets of a message, one could pinpoint the location of a single bit error <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This process resembles a "20 questions" game, where each check halves the possibilities <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

Consider a 16-bit block, with positions numbered 0 to 15 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Four positions are reserved for redundancy, specifically positions that are powers of 2 (1, 2, 4, 8) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. These "redundant" bits are not simple copies, but a nuanced form of redundancy that adds resilience <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

The process involves two main roles:
- **Sender:** Sets the special redundancy bits <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
- **Receiver:** Performs checks and corrects errors <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

### Example: A 16-bit Block (15-11 [[history_and_significance_of_hamming_codes | Hamming Code]])

For a 16-bit block (numbered 0-15), 12 bits carry data, and 4 positions (1, 2, 4, 8) are reserved for redundancy <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. (Initially, position 0 is not used for data, reducing data bits to 11 for a 15-bit block <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>).

To locate an error, a series of [[understanding_parity_checks | parity checks]] are performed on specific subsets of the block:

1.  **Check 1 (Position 1):** Covers the odd-numbered positions <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. If an error is detected here, it implies the error is in an odd position <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
2.  **Check 2 (Position 2):** Covers the right half of the block (e.g., positions 2, 3, 6, 7, 10, 11, 14, 15) <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. If this check reveals an error, it further narrows the location.
3.  **Check 3 (Position 4):** Covers the odd rows (e.g., positions 4-7, 12-15) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
4.  **Check 4 (Position 8):** Covers the bottom two rows (e.g., positions 8-15) <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

By combining the results of these four checks, the receiver can precisely locate any single bit error <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This works even if a parity bit itself is affected <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

For example, if an error occurs at position 3:
- It affects the first parity group (odd columns) <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
- It affects the second parity group (right half) <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
- It does not affect the third or fourth parity groups <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
Based on this combination of results, the receiver can pinpoint the error to position 3 and correct it <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

### The "No Error" Condition and Extended [[history_and_significance_of_hamming_codes | Hamming Codes]]

A potential issue arises if all four parity checks indicate no error: this could mean there's truly no error, or it could ambiguously point to position 0 <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. To resolve this, position 0 is typically set aside, making it a 15-bit block (a 15-11 [[history_and_significance_of_hamming_codes | Hamming code]], with 11 message bits and 4 redundancy bits) <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. In this setup, if all four parity checks are even, it unambiguously means no error occurred <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

However, position 0 can be cleverly utilized in an "extended [[history_and_significance_of_hamming_codes | Hamming code]]" to detect (but not correct) two-bit errors <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. After setting the four error-correcting parity bits, position 0 is set to ensure the parity of the *entire* block is even <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
- If a single bit error occurs, the overall block parity becomes odd, and the four internal checks pinpoint the error <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
- If two errors occur, the overall block parity might revert to even, but the four internal parity checks will still show an anomaly, indicating that at least two errors occurred <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

## Encoding and Decoding Example

To encode a message using a 16-bit extended [[history_and_significance_of_hamming_codes | Hamming code]] (11 message bits + 4 correction bits + 1 overall parity bit):

1.  **Divide Data:** Split the original data into 11-bit chunks <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
2.  **Place Message Bits:** Insert the 11 message bits into the non-parity positions (all positions except 0, 1, 2, 4, 8) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.
3.  **Set Parity Bits:**
    *   Set bit 1 to ensure even parity for its designated group of bits <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
    *   Set bit 2 to ensure even parity for its designated group <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
    *   Set bit 4 to ensure even parity for its designated group <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
    *   Set bit 8 to ensure even parity for its designated group <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>.
4.  **Set Overall Parity Bit:** Set bit 0 to ensure the parity of the entire 16-bit block is even <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

To decode and correct a received block:

1.  **Check Parity Groups:** Examine the four parity groups (related to positions 1, 2, 4, 8) <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.
2.  **Locate Error:** The pattern of odd/even parities from these four checks indicates the exact position of a single bit error. For instance, if the first check is even, second is odd, third is even, and fourth is odd, it points to position 10 <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
3.  **Check Overall Parity:** Examine the parity of the entire block (controlled by bit 0) <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
    *   If overall parity is odd and internal checks pinpoint an error, it's likely a single bit flip <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
    *   If overall parity is even but internal checks show an error, it indicates at least two errors <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
4.  **Correct Error:** Flip the bit at the identified error position <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
5.  **Extract Message:** Extract the 11 message bits from their non-parity positions to retrieve the original data <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

The elegance of [[history_and_significance_of_hamming_codes | Hamming codes]] lies in how these multiple [[understanding_parity_checks | parity checks]] can be systematically framed and executed, allowing for efficient error detection and correction with minimal overhead <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. This illustrates the underlying mathematical principles that form the basis of [[practical_implementation_of_error_correction_algorithms | practical implementation of error correction algorithms]] and [[concepts_in_information_theory_and_coding_theory | coding theory]].