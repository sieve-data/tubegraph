---
title: Understanding parity checks
videoId: X8jsijhllIA
---

From: [[3blue1brown]] <br/> 

[[error_correction_in_digital_data_storage | Storing]] and [[error_correction_in_digital_data_storage | transmitting digital data]] reliably, even when errors occur, relies on mathematical cleverness <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. For instance, a scratched CD or DVD can still play back its content accurately because of techniques that make data resilient to errors <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Any digital file, whether video, sound, text, or an image, is fundamentally a sequence of 1s and 0s <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

A simple, though inefficient, strategy to correct a flipped bit would be to store three copies of each bit <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. A machine could then compare these copies and take the "best 2 out of 3" when a discrepancy arises <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. However, this uses two-thirds of the storage space for redundancy and offers no strong guarantee against more than one bit flipping <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The more interesting challenge is to correct errors while minimizing redundant space <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This is where [[basics_of_error_correction_schemes | error correction schemes]], like [[error_correction_and_hamming_codes | Hamming codes]], come into play <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

For example, using methods like [[error_correction_and_hamming_codes | Hamming codes]], data can be stored in 256-bit blocks where only 9 bits act as redundancy, leaving 247 bits for meaningful data <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. If any single bit flips in such a block, a machine can identify and precisely correct the error <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. If two bits flip, the machine can at least detect that two errors occurred, though it won't know how to fix them <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

The basic principle behind [[basics_of_error_correction_schemes | error correction]] is that within the vast space of all possible messages, only a specific subset is considered valid <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

> As an analogy, think about correctly spelled words vs incorrectly spelled words <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Whenever a valid message gets altered, the receiver is responsible for correcting what they see back to the nearest valid neighbor, as you might do with a typo <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## The Parity Check

A fundamental concept in [[basics_of_error_correction_schemes | error detection]] is the parity check <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. A simple parity check involves separating out one single bit, controlled by the sender, whose sole job is to ensure that the total number of 1s in the message is an even number <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### How it Works
*   **Sender's Role**: If the total count of 1s in the message (excluding the parity bit) is odd, the sender sets the special bit (the parity bit) to a 1, making the overall count even <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. If the count is already even, the parity bit is kept at 0 <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **Receiver's Role**: If any bit in the message flips (0 to 1 or 1 to 0), it changes the total count of 1s from even to odd <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. If the receiver observes an odd number of 1s, they know for sure that an error has occurred <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

The property of having an even or odd number of 1s in a group of bits is known as its parity <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>, which can be represented as 0 or 1 respectively <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Limitations
While elegant, a single parity check has limitations:
*   **Detection, Not Correction**: It can detect that an error occurred, but it cannot identify *where* the error is <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   **Odd Errors Only**: If there are two errors, or any even number of errors, the total count of 1s would still be even, so the receiver would not detect an issue <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **No 100% Confidence**: No [[basics_of_error_correction_schemes | error detection or correction method]] can provide 100% confidence, as random noise could always transform one valid message into another <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. The goal is to be robust up to a certain maximum number of errors or to reduce the probability of false positives <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Parity Checks in [[error_correction_and_hamming_codes | Hamming Codes]]

Richard Hamming invented the world's first [[error_correction_and_hamming_codes | error correction code]] in the 1940s while working at Bell Labs <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. His key insight was that applying multiple parity checks, not to the full message but to *carefully selected subsets*, allows for a refined series of questions that can pinpoint the location of any single-bit error <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. This process feels like a game of 20 questions, narrowing down possibilities <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Example: 16-Bit Block
Consider a block of 16 bits, positions 0 to 15 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   12 bits are for actual data, and 4 positions are reserved for redundancy <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   These 4 special bits are placed at positions that are powers of 2 (1, 2, 4, 8, etc.) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Position 0 has a mild nuance <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   A "sender" sets these special bits, and a "receiver" checks and corrects errors <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

By performing multiple, overlapping parity checks on subsets of the data, the location of an error can be deduced:
1.  **Parity Check 1 (e.g., odd-numbered positions)**: Uses position 1 as its parity bit. If an error is detected here, it's known to be in an odd position <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
2.  **Parity Check 2 (e.g., right half of grid)**: Uses position 2 as its parity bit. If an error is detected here, it's known to be in the right half <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

When combined, these two checks can pinpoint a specific column where the error lies <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. Similarly, two more checks focusing on rows (e.g., parity check on odd rows using position 4, and on bottom two rows using position 8) can pinpoint the row <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. The intersection of these column and row identifications reveals the exact location of the single-bit error <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. Even if a parity bit itself is flipped, the same four questions will track it down <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

This method is efficient; for a 256-bit block, only eight "yes or no" questions (requiring 8 parity bits) are needed to binary search for a specific error location <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

### The Nuance of Position 0

Initially, with four parity checks, there are 16 possible outcomes, which seems perfect for pinpointing 1 out of 16 positions <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. However, a 17th outcome is needed to indicate "no error" <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **15-11 Hamming Code**: One solution is to simply exclude the 0th bit, working with a 15-bit block where 11 bits carry the message and 4 are for redundancy <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. If all four parity checks are even, it unambiguously means no error <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   **Extended Hamming Code**: A cleverer approach is to keep the 0th bit and use it as an overarching parity bit for the *entire* block <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. After setting the four error-correcting bits, the 0th bit is set to ensure the full block has an even parity <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
    *   If a single bit error occurs, the full block's parity becomes odd (detected by the 0th bit) <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
    *   If two errors occur, the overall parity toggles back to even, but the receiver would still detect issues with the other four parity checks <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. This allows the detection of two-bit errors, even if they cannot be corrected <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.

This combination of multiple parity checks, especially as seen in [[error_correction_and_hamming_codes | Hamming codes]], transforms basic error detection into powerful error correction <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. The underlying mathematical elegance allows for a systematic way to scale these methods and perform the logic efficiently <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.

For a [[practical_implementation_of_error_correction_algorithms | practical implementation]] of [[error_correction_and_hamming_codes | Hamming codes]], Ben Eater created a video demonstrating how to build them on breadboards <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. While more modern codes like Reed-Solomon are now widely used, [[error_correction_and_hamming_codes | Hamming codes]] offer a magical simplicity in understanding how seemingly impossible error correction can be achieved <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.