---
title: Basics of error correction schemes
videoId: X8jsijhllIA
---

From: [[3blue1brown]] <br/> 

[[concepts_in_information_theory_and_coding_theory | Error correction codes]] are a set of mathematical techniques that enable data to be stored and transmitted resiliently to errors <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This means that even if the underlying 1s and 0s are altered during storage or transmission, the original data can often be recovered precisely <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## The Problem: Data Corruption

When data is stored on mediums like CDs or DVDs, physical scratches can affect the 1s and 0s on the disk, causing different data to be read than what was originally stored <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Despite these errors, the data can often be decoded into the exact original file, thanks to [[error_correction_in_digital_data_storage | error correction techniques]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Similarly, data transmission can also be prone to errors <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Simple (Inefficient) Error Correction

Any digital file, whether video, sound, text, code, or an image, is fundamentally a sequence of 1s and 0s <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. A basic strategy to correct a flipped bit is to store three copies of each bit <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. A machine reading the file could then compare these three copies and use a "2 out of 3" majority rule whenever a discrepancy occurs <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

However, this method is highly inefficient, using two-thirds of the storage space for redundancy <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Furthermore, it offers no strong guarantee if more than one bit gets flipped <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## The Goal: Efficient Error Correction

The more interesting challenge is to correct errors while minimizing the amount of space given up for redundancy <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. For instance, advanced methods allow storing data in 256-bit blocks where only 9 bits act as redundancy, leaving 247 bits for meaningful data <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. With such a scheme, a single flipped bit within the block can be precisely identified and corrected just by examining that block <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. If two bits are flipped, the system can detect that two errors occurred, although it might not be able to fix them <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

Such methods are generally known as [[error_correction_and_hamming_codes | error correction codes]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This field has been a rich source of deep mathematics, integrated into everyday devices <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Core Principle

The basic principle of [[error_correction_and_hamming_codes | error correction]] is that within a vast space of all possible messages, only a specific subset is considered valid <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. When a valid message is altered, the receiver's role is to correct what they observe back to the "nearest" valid neighbor, similar to correcting a typo <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Developing concrete algorithms for this categorization requires cleverness <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Introducing Hamming Codes

The goal of this discussion is to provide a thorough understanding of one of the earliest [[error_correction_and_hamming_codes | error correction codes]], known as a [[history_and_significance_of_hamming_codes | Hamming code]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. While not as widely used today as modern codes like the Reed-Solomon algorithm, [[history_and_significance_of_hamming_codes | Hamming codes]] beautifully illustrate the principles of error correction <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Historical Context

The story of [[history_and_significance_of_hamming_codes | Hamming codes]] begins in the 1940s with Richard Hamming at Bell Labs <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Frustrated by programs failing due to misread bits on a large punch card computer, Hamming invented the world's first error correction code <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### The Setup

Error correction algorithms involve two main roles:
1.  **Sender**: Responsible for encoding special redundant bits into the data <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
2.  **Receiver**: Responsible for performing checks and correcting errors <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

These "sender" and "receiver" roles refer to machines or software, and "message" broadly includes data storage, which can be thought of as sending a message from the past to the future <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

### [[understanding_parity_checks | Parity Checks]]

A [[understanding_parity_checks | parity check]] is a method that allows for the detection of single bit errors, but not their correction <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   One bit is designated as a special "parity bit," controlled by the sender, while the rest carry the message <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   The job of this bit is to ensure the total number of 1s in the message is an even number <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. If the count of 1s is odd, the sender flips the parity bit to make it even; if already even, it remains 0 <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   If any bit in the message flips (0 to 1 or 1 to 0), the total count of 1s changes from even to odd <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   Upon receiving an odd number of 1s (odd parity), the receiver knows an error has occurred, but not where <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   The term "parity" refers to whether a group of bits has an even or odd number of 1s (often represented as 0 for even, 1 for odd) <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. The special bit controlling this is the "parity bit" <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   If an odd number of errors occur (e.g., 1, 3, 5), the parity will be odd <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. If an even number of errors occur (e.g., 2, 4), the parity will remain even, making detection impossible with a single parity check <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

While a single [[understanding_parity_checks | parity check]] is weak, it distills the idea of change across a message into a single bit, making it a powerful building block for more sophisticated schemes <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

## Hamming's Insight: Localizing Errors with Multiple Parity Checks

Hamming's key insight was that applying [[understanding_parity_checks | parity checks]] not to the full message, but to carefully selected subsets, could pinpoint the location of any single bit error <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. This is analogous to a game of 20 questions, where "yes" or "no" answers cut the possibilities in half <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### The [[history_and_significance_of_hamming_codes | Hamming Code]] Structure (16-bit block example)

In a 16-bit block (positions 0-15), 12 bits constitute the actual data, and 4 positions are reserved for redundancy <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. These 4 redundant bits are placed in positions that are powers of 2 (positions 1, 2, 4, 8) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This arrangement is crucial for the elegance and scalability of the system <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

To locate an error, a series of [[understanding_parity_checks | parity checks]] are performed on specific subsets of bits. For a 16-bit block (excluding position 0 for now), four [[understanding_parity_checks | parity checks]] are used:

1.  **Parity Check 1 (Position 1)**: Covers bits in odd-numbered positions (e.g., columns) <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. If an error is detected here, it means the error is in an odd position <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
2.  **Parity Check 2 (Position 2)**: Covers bits in the right half of the block <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. If an error is detected here, it's in the right half <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
3.  **Parity Check 3 (Position 4)**: Covers bits in odd-numbered rows <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
4.  **Parity Check 4 (Position 8)**: Covers bits in the bottom two rows <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

By combining the results of these four [[understanding_parity_checks | parity checks]], the receiver can pinpoint the exact column and row, and thus the specific bit location, of any single error <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. This system allows for identifying and fixing single bit errors regardless of whether they occur in data bits or the parity bits themselves <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

For a block of 256 bits, only eight "yes" or "no" questions (and thus 8 parity bits) are needed to binary search and pinpoint an error location <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

### Handling the "No Error" Case

With four "yes" or "no" questions, there are 16 possible outcomes, which perfectly map to pinpointing 1 out of 16 positions <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. However, an additional outcome is needed to signify "no error" <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. The simplest solution is to discard position 0, working with a 15-bit block where 11 bits are data and 4 are for redundancy. If all four [[understanding_parity_checks | parity checks]] indicate no error, it unambiguously means no error occurred <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This is known as a 15-11 [[error_correction_and_hamming_codes | Hamming code]] <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

### [[error_correction_and_hamming_codes | Extended Hamming Codes]]: Detecting Two Errors

To maintain a block size that is a clean power of 2 (like 16 bits) and add capabilities, the 0th bit can be utilized <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. If position 0 is used as an additional [[understanding_parity_checks | parity bit]] for the *entire* block, it allows for the detection (though not correction) of 2-bit errors <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

Here's how it works:
*   After setting the four error-correcting parity bits, the 0th bit is set so that the parity of the *full* 16-bit block is even <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   If a single bit error occurs, the overall block parity will become odd, and the four error-correcting checks will pinpoint the error <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
*   If two errors occur, the overall block parity will *revert* to even, but the four error-correcting checks will still indicate a non-zero error (as they will pinpoint a single incorrect location or conflict) <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   Therefore, if the receiver sees an even overall parity but the other four checks show errors, they know at least two errors occurred <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>. This is a standard feature of [[error_correction_and_hamming_codes | extended Hamming codes]] <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

It's important to note that no [[error_correction_and_hamming_codes | error detection or correction]] method can guarantee 100% confidence, as enough random noise could always transform one valid message into another <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. The goal is to create schemes robust up to a certain number of errors or to reduce the probability of false positives <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Practical Example

To construct an error-resistant 16-bit block from an 11-bit chunk of data:
1.  Place the 11 message bits into the 16-bit block, skipping positions 0, 1, 2, 4, and 8 (which are reserved for parity bits) <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.
2.  Calculate and set the parity bits at positions 1, 2, 4, and 8 according to their respective subsets to ensure even parity <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
3.  Finally, set the parity bit at position 0 to ensure the *entire* 16-bit block has an even parity <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

When a receiver checks the block:
1.  They perform the four [[understanding_parity_checks | parity checks]] for positions 1, 2, 4, and 8 <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. The combination of "even" or "odd" results from these checks points to a specific bit position if an error occurred <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
2.  They also check the overall parity of the block <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. If the overall parity is odd, and the four sub-checks pinpoint an error, it indicates a single bit flip. If the overall parity is even but the sub-checks indicate an error, it suggests two errors <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
3.  Once the error location is identified (and if it's a single error), the bit is flipped back to its original state <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
4.  The 11 original message bits are then extracted from their designated positions <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

## Looking Ahead

The true elegance of this algorithm lies in how simply a machine can identify an error's position, how it systematically scales, and how all these [[understanding_parity_checks | parity checks]] can be framed as a single operation <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. For a [[practical_implementation_of_error_correction_algorithms | hardware-level understanding]] of [[error_correction_and_hamming_codes | Hamming codes]], practical implementations on breadboards exist <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.