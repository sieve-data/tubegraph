---
title: History and significance of Hamming codes
videoId: X8jsijhllIA
---

From: [[3blue1brown]] <br/> 

Hamming codes represent a significant early advancement in [[error_correction_and_hamming_codes | error correction codes]], enabling data resilience against errors during storage or transmission <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This mathematical ingenuity allows for scenarios such as a scratched CD or DVD still playing back its stored content accurately, despite affected 1s and 0s <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## The Problem: Resilient Data Storage and Transmission

Any digital file, whether video, sound, text, or an image, is fundamentally a sequence of 1s and 0s <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. A simple, but inefficient, strategy for error correction would be to store three copies of each bit, allowing a machine to compare them and take the "best 2 out of 3" if there's a discrepancy <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. However, this method uses two-thirds of storage space for redundancy and offers no strong guarantee if more than one bit is flipped <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The more intriguing challenge is to correct errors while minimizing space usage <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

For instance, a Hamming code can store data in 256-bit blocks, using only 9 bits for redundancy and 247 bits for meaningful data <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. If any single bit is flipped within such a block, a machine can identify the error and its precise location for correction <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. If two bits are flipped, the machine can detect that two errors occurred, though it won't know how to fix them <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Historical Genesis: Richard Hamming at Bell Labs

The story of Hamming codes begins in the 1940s with Richard Hamming at Bell Labs <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Frustrated by program failures due to misread bits on an expensive punch card computer, Hamming invented the world's first [[error_correction_and_hamming_codes | error correction code]] <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Core Principle: Parity Checks

The basic principle of [[basics_of_error_correction_schemes | error correction schemes]] is that in a vast space of all possible messages, only a subset are considered valid <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. When a valid message is altered, the receiver corrects it back to the nearest valid neighbor, similar to correcting a typo <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

A fundamental building block for this is the **parity check** <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Mechanism**: A single bit (the parity bit) is designated to ensure that the total number of 1s in a message (or a subset thereof) is an even number <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. If the count of 1s is odd, the sender flips the parity bit to make it even; otherwise, it remains 0 <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **Detection**: If any bit in the message (or parity bit itself) is flipped, the total count of 1s changes from even to odd, signaling an error to the receiver <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   **Limitations**: While a parity check detects an odd number of errors (1, 3, 5, etc.), it cannot detect an even number of errors (2, 4, etc.), nor can it pinpoint the location of the error <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### Hamming's Key Insight: Pinpointing Errors with Multiple Parity Checks

Hamming's breakthrough insight was to apply parity checks not to the full message, but to *certain carefully selected subsets* of bits <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This allows for a series of questions that can pinpoint the location of any single bit error <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This process resembles a "20 questions" game, where each yes/no answer halves the possibilities <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Example: A 16-bit Block Hamming Code

In a 16-bit block (positions 0-15), 12 bits carry data, and 4 positions are reserved for redundancy <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. These 4 special bits are placed at positions that are powers of 2 (1, 2, 4, 8, etc.), which allows for elegant scaling <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

A standard Hamming code involves a sender setting these parity bits and a receiver performing checks and corrections <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Storing data is analogous to sending a message from the past to the future <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

For a 16-bit block, four parity checks can be set up:
1.  **Parity Check 1 (Position 1):** Checks the parity of bits in all odd-numbered positions (1, 3, 5, 7, 9, 11, 13, 15) <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
2.  **Parity Check 2 (Position 2):** Checks the parity of bits in the right half of the grid (or specific positions, e.g., 2, 3, 6, 7, 10, 11, 14, 15) <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
3.  **Parity Check 3 (Position 4):** Checks the parity of bits in the odd rows (or specific positions, e.g., 4, 5, 6, 7, 12, 13, 14, 15) <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
4.  **Parity Check 4 (Position 8):** Checks the parity of bits in the bottom two rows (or specific positions, e.g., 8, 9, 10, 11, 12, 13, 14, 15) <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

By combining the results of these four checks, a single bit error can be precisely located <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. For example, if an error affects the first and second parity groups but not the third and fourth, it necessarily points to a specific bit (e.g., position 3) <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. The connection between these questions and binary counting is key <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

### The 15-11 Hamming Code and Extended Hamming Code

Initially, four yes/no parity checks yield 16 possible outcomes, which could pinpoint 1 out of 16 positions <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. However, a 17th outcome is needed to indicate "no error" <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. The solution is to disregard position 0, working with a 15-bit block where 11 bits are data and 4 are for redundancy <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. This is known as a **15-11 Hamming code** <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

To achieve a clean power-of-2 block size and enhance error detection, the 0th bit can be utilized as an overall parity bit for the entire block <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. This creates an **extended Hamming code** <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   **Single-bit error**: The full block parity toggles to odd, and the four error-correcting checks also catch it <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
*   **Two-bit errors**: The overall parity toggles back to even, but the four individual parity checks will still show non-zero results, indicating at least two errors have occurred, even if they cannot be corrected <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

## Significance and Legacy

[[error_correction_and_hamming_codes | Hamming codes]] are a foundational example within [[concepts_in_information_theory_and_coding_theory | information theory and coding theory]], demonstrating how surprisingly deep mathematics can be integrated into everyday devices <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. While more modern codes like the Reed-Solomon algorithm are now more widely used, Hamming codes illustrate a "magic" contrast between the initial impossibility of the task and its utter reasonableness once understood <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

The goal of any error detection or correction scheme is not 100% confidence, but to be robust up to a certain maximum number of errors or to reduce the probability of false positives <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This method efficiently protects message bits by naturally extending protection to the error correction bits as a byproduct <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. For example, a 256-bit block needs only eight yes/no questions (parity bits) to binary search and pinpoint an error location <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

For a hardware-level understanding, Ben Eater has created a video demonstrating the implementation of Hamming codes on breadboards <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.