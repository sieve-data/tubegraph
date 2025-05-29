---
title: Introduction to Hamming Codes
videoId: X8jsijhllIA
---

From: [[3blue1brown]] <br/> 

[[Introduction to Hamming Codes]] are a class of error correction codes that allow data to be stored or transmitted in a way that is resilient to errors <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. They enable the recovery of the original data even if some bits are flipped due to scratches on a CD or DVD, or noise during transmission <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## The Problem of Data Corruption

When data, such as a video, sound, text, or an image, is stored or transmitted, it exists as a sequence of 1s and 0s <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>, <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. A physical scratch on a CD or DVD, for instance, can affect these 1s and 0s, causing the system to read different data than what was originally stored <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

A simple, but inefficient, strategy to correct a flipped bit would be to store three copies of each bit <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. A machine could then compare these copies and take the best two out of three in case of a discrepancy <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. However, this method uses two-thirds of the storage space for redundancy and offers no strong guarantee if more than one bit gets flipped <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

The more interesting challenge is to correct errors while minimizing the amount of space given up for redundancy <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Efficiency of Hamming Codes

[[Introduction to Hamming Codes]] are remarkably efficient. For example, using methods like those described in the video, a 256-bit block of data could use only 9 bits for redundancy, leaving 247 bits for the meaningful message <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>, <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. If any single bit in this block is flipped, a machine can identify the error and its precise location to correct it <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

Furthermore, if two bits are flipped, the system can detect that two errors occurred, though it won't be able to fix them in this basic configuration <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

Methods for correcting errors are broadly known as "error correction codes" <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, and [[Introduction to Hamming Codes]] are one of the earliest examples <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. While more modern codes like the Reed-Solomon algorithm are now more widely used, [[Introduction to Hamming Codes]] offer a fundamental and elegant understanding of the concept <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>, <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Basic Principle of Error Correction

The fundamental principle of error correction is that in a vast space of all possible messages, only a specific subset is considered "valid messages" <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. When a valid message is altered, the receiver's role is to correct what they observe back to the "nearest valid neighbor," similar to correcting a typo <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>, <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## [[historical_background_of_hamming_codes | Historical Background]]

[[historical_background_of_hamming_codes | Richard Hamming]] invented the world's first error correction code in the 1940s while working at Bell Labs <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. He became frustrated when his programs, run on a large punch card computer, frequently failed due to misread bits <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Parity Checks: A Building Block

Before [[Introduction to Hamming Codes]] can be fully understood, it's important to grasp the concept of a parity check <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. A parity check uses a single dedicated bit, called a "parity bit," whose sole purpose is to ensure that the total number of 1s in a given message block is an even number <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. If the initial count of 1s is odd, the sender flips the parity bit to a 1; if it's already even, the parity bit remains 0 <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>, <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

If any bit in the message is flipped (0 to 1 or 1 to 0), the total count of 1s changes from even to odd <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>, <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. The receiver can then detect an error by observing an odd number of 1s <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>, <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

> [!NOTE] Parity
> The term "parity" refers to whether a group of bits has an even or odd number of 1s <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>, <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This can also be expressed numerically as 0 for even and 1 for odd <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### Limitations of Simple Parity Checks

While parity checks are elegant, they have limitations:
*   An odd parity only indicates that *some* error has occurred, not *where* it was <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   An odd parity means there could have been 1, 3, 5, or any other odd number of errors <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>, <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   If an even number of errors (e.g., 2) occurs, the total count of 1s would still be even, and the receiver wouldn't detect any error <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>, <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

No error detection or correction method can guarantee 100% confidence, as enough random noise could always transform one valid message into another <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>, <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. The goal is robustness up to a certain maximum number of errors or to reduce the probability of false positives <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Hamming's Key Insight: Pinpointing Errors

Hamming's breakthrough was realizing that by applying parity checks not to the entire message, but to **carefully selected subsets** of bits, the location of a single bit error could be pinpointed <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>, <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>, <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This process is akin to playing a game of 20 questions, where each "yes" or "no" answer (from a parity check) halves the space of possibilities <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>, <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Example: 16-Bit Block Hamming Code

Let's consider a 16-bit block, with positions numbered 0 to 15 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>, <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. In this setup, 12 bits are for actual data, and 4 positions are reserved for redundancy <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>, <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. These 4 special "parity bits" are placed at positions that are powers of 2 (positions 1, 2, 4, 8, etc.), which facilitates an elegant error detection mechanism <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>, <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

A "sender" is responsible for setting these parity bits, and a "receiver" performs checks and corrects errors <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>, <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

The specific parity checks are performed on overlapping subsets of bits:

1.  **Check 1 (Position 1):** Covers all odd-numbered positions <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>, <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. If an error is detected here, it means the error is in an odd position <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
2.  **Check 2 (Position 2):** Covers the right half of the 16-bit block (positions 2-3, 6-7, 10-11, 14-15) <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>, <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. If this parity check is odd, the error is within this group <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
3.  **Check 3 (Position 4):** Covers the bottom two rows (positions 4-7, 12-15) <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
4.  **Check 4 (Position 8):** Covers the bottom two rows of the right half (positions 8-15) <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>, <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

By combining the results of these four parity checks, the receiver can uniquely pinpoint the location of any single bit error <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>, <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This works because each bit's position can be represented in binary, and each parity check corresponds to one of the binary digits of the error's position <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>, <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. For example, if a bit at position 3 (binary 0011) is flipped, it will affect the parity checks associated with the 1st and 2nd binary place values (positions 1 and 2), but not the 4th and 8th (positions 4 and 8) <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>, <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>, <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

> [!NOTE] Parity Bit Errors
> If a parity bit itself is flipped, the same group of four questions will track down its location just like any other bit <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>, <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>, <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. Protecting these parity bits is a natural byproduct of the scheme <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.

For a larger block of 256 bits, only eight yes/no questions (eight parity bits) are needed to binary search for a specific error location <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>, <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>, <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. Each question requires only one bit for the parity check <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

### The "No Error" Condition (15-11 Hamming Code)

With four yes/no questions, there are 16 possible outcomes <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>, <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. While this is perfect for pinpointing 1 out of 16 positions, it doesn't account for the 17th outcome: *no error* <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>, <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. If all four parity checks show no error, it could either mean no error occurred or that the error was at position 0 (if position 0 were part of the checks) <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>, <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>, <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

The initial solution is to simply ignore position 0 <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. If all four parity checks are even, it unambiguously signifies "no error" <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>, <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. This configuration uses a 15-bit block, with 11 data bits and 4 redundancy bits, known as a **15-11 Hamming code** <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>, <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>, <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>, <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

## [[extending_hamming_codes_for_improved_error_detection | Extended Hamming Codes]]

While the 15-11 Hamming code can correct single bit errors, it cannot detect two-bit errors. A clever way to detect (though not correct) two-bit errors is to use position 0 as an overarching parity bit for the entire block <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>, <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. This is known as an [[extending_hamming_codes_for_improved_error_detection | extended Hamming code]] <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

Here's how it works:
1.  After setting the four error-correcting parity bits (positions 1, 2, 4, 8), position 0 is set so that the parity of the *entire 16-bit block* is even <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>, <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>, <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
2.  If a single bit error occurs, the overall block parity will toggle to odd, and the four error-correcting checks will also catch it, allowing correction <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>, <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
3.  If two errors occur, the overall block parity will toggle *back* to being even <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>, <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. However, the receiver will still notice that at least some error has occurred because the four specific parity checks (for positions 1, 2, 4, 8) will show a non-zero pattern, even if they don't pinpoint a single error <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>, <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>, <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>. This allows the detection of two-bit errors <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>, <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

This sophisticated approach, utilizing the 0th bit, makes it possible to detect two-bit errors, even if they cannot be corrected <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.