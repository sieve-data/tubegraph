---
title: Practical implementation of error correction algorithms
videoId: X8jsijhllIA
---

From: [[3blue1brown]] <br/> 

Error correction algorithms are mathematical techniques that allow data to be stored or transmitted in a way that is resilient to errors <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This means that even if the underlying bits of data are affected by noise or physical damage, the original information can often be recovered perfectly <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

A common example of [[error_correction_in_digital_data_storage | error correction in digital data storage]] is a scratched CD or DVD <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Although a scratch physically alters the 1s and 0s on the disk, the stored file can still play back correctly unless the damage is severe <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Basic Principles

Any file, whether video, sound, text, or an image, is fundamentally a sequence of 1s and 0s <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. The core idea behind [[basics_of_error_correction_schemes | error correction schemes]] is that in the vast space of all possible messages, only a specific subset is considered valid <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. If an altered message is received, the system aims to correct it back to the nearest valid version <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Simple Redundancy

A straightforward, but inefficient, strategy for error correction is to store three copies of each bit <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. A machine reading the file could then compare these copies and apply a "best 2 out of 3" rule if there's a discrepancy <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. However, this method uses two-thirds of the storage space for redundancy and offers no strong guarantee against multiple bit flips <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Efficient Error Correction

The more interesting challenge is to correct errors while minimizing the amount of space given up for redundancy <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. For instance, some methods allow storing data in 256-bit blocks where only 9 bits are used for redundancy, leaving 247 bits for meaningful data <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. With this approach, if any single bit is flipped, a machine can identify the error's precise location and correct it <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. If two bits are flipped, the machine can detect that errors occurred, but it won't be able to fix them <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

Methods that enable such error correction are known as [[concepts_in_information_theory_and_coding_theory | error correction codes]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Hamming Codes

[[error_correction_and_hamming_codes | Hamming codes]] represent one of the earliest examples of efficient error correction <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. They were invented in the 1940s by Richard Hamming, who sought to overcome frequent program failures caused by misread bits on a punch card computer at Bell Labs <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. While not as widely used as modern codes like the Reed-Solomon algorithm, Hamming codes offer a foundational understanding of the principles involved <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Parity Checks as Building Blocks

A crucial concept leading to Hamming codes is the [[understanding_parity_checks | parity check]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. A parity check involves a single "parity bit" that a sender tunes to ensure the total number of 1s in a message (or a subset of bits) is an even number <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

*   **Detection**: If any bit in the message flips (0 to 1 or 1 to 0), the total count of 1s changes from even to odd <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. A receiver seeing an odd number of 1s can definitively know an error occurred, even without knowing its location <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Limitations**: While effective for detecting any odd number of errors (1, 3, 5, etc.), a parity check cannot detect an even number of errors (like 2 or 4), as the parity would remain even <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. Also, it doesn't pinpoint the error location <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### Locating Errors with Multiple Parity Checks

Hamming's key insight was that applying multiple [[understanding_parity_checks | parity checks]] to carefully selected subsets of bits can not only detect an error but also pinpoint its exact location <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This functions like a game of "20 questions," where yes/no queries halve the space of possibilities <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

For a 16-bit block (positions 0-15), 4 positions are reserved as redundancy bits, typically powers of 2 (1, 2, 4, 8) <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. These bits control the parity of specific subsets of data bits.

*   **Example (16-bit block)**:
    *   **Check 1**: Parity check on all odd-numbered positions (using position 1 as parity bit) <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
    *   **Check 2**: Parity check on the right half of the grid (using position 2 as parity bit) <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
    *   **Check 3**: Parity check on the odd rows (using position 4 as parity bit) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
    *   **Check 4**: Parity check on the bottom two rows (using position 8 as parity bit) <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

By combining the results of these checks, a single bit error can be precisely located within the block <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. For instance, if errors are detected in the odd columns and the right half, the error must be in the last column <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

### The "No Error" Condition and Extended Hamming Codes

Originally, four parity checks yield 16 possible outcomes, which could pinpoint 1 of 16 positions. However, a 17th outcome is needed to indicate "no error" <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

A simple solution is to discard position 0, making it a 15-bit block where 11 bits carry the message and 4 are for redundancy. If all four parity checks show even parities, it unambiguously means no error <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This is known as a 15-11 Hamming code <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

An **extended Hamming code** utilizes position 0 as an additional parity bit for the *entire block* <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. This allows for the detection of *two-bit errors*, even if they cannot be corrected <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. If a single bit error occurs, the overall block parity becomes odd (detected by bit 0), and the four error-correcting checks will also indicate an error. If two errors occur, the overall block parity might revert to even, but the four error-correcting checks would still show anomalies, signaling that at least two errors happened <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

### Implementation Overview

When implementing a Hamming code:
1.  **Sender**: Divides the message into chunks (e.g., 11-bit chunks for a 16-bit block) <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
2.  **Sender**: Places message bits into all positions not reserved for error correction (i.e., not powers of 2, plus position 0 for extended codes) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.
3.  **Sender**: Calculates and sets the parity bits (at positions 1, 2, 4, 8) for their respective subsets to ensure even parity <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
4.  **Sender**: For an extended Hamming code, calculates and sets the parity bit at position 0 to ensure the overall block has even parity <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
5.  **Receiver**: Checks the parity of the same subsets of bits that the sender used to set the parity bits (at positions 1, 2, 4, 8) <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
6.  **Receiver**: The combination of results from these checks (which ones are odd/even) precisely indicates the position of a single bit error, if any <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
7.  **Receiver**: Checks the overall parity of the block (using bit 0). If it's even but other parity checks indicate an error, it suggests multiple errors <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
8.  **Receiver**: Corrects the identified bit by flipping it <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
9.  **Receiver**: Extracts the original message bits, excluding the redundancy bits <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

The elegance of this algorithm allows for the core logic to be condensed into a single operation, making it efficient for machines to implement <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>. The systematic scaling of [[error_correction_and_hamming_codes | Hamming codes]] means that for a block of 256 bits, only eight yes/no questions (corresponding to eight parity bits) are needed to binary search for and pinpoint an error location <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.