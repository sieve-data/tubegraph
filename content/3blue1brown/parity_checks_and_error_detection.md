---
title: Parity Checks and Error Detection
videoId: X8jsijhllIA
---

From: [[3blue1brown]] <br/> 
Even with scratches on a CD or DVD, data can often still be played back correctly <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This is because a scratch affects the underlying 1s and 0s, causing different data to be read than what was originally stored <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The ability to recover the original file despite these alterations is due to mathematical techniques that make data storage and transmission [[Error Correction and Data Redundancy | resilient to errors]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### The Problem of Errors

Any digital file, whether it's video, sound, text, or an image, is fundamentally a sequence of 1s and 0s <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. A simple, but inefficient, strategy to correct a flipped bit would be to store three copies of each bit <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. A machine could then compare these copies and take the "best 2 out of 3" if there's a discrepancy <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. However, this method uses two-thirds of the storage space for redundancy and offers no strong guarantee against more than one bit being flipped <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

The more significant challenge lies in designing methods that allow errors to be corrected while minimizing the amount of space given up for redundancy <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Methods for correcting errors are known as "error correction codes" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Historical Context

The field of error correction codes has been a rich source of deep mathematics, integrated into everyday devices, for the better part of the last century <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. A key development came in the 1940s when [[Historical Background of Hamming Codes | Richard Hamming]], working at Bell Labs, grew frustrated by computer programs failing due to occasional misread bits <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This frustration led him to invent the world's first error correction code, the [[Introduction to Hamming Codes | Hamming code]] <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### The Basic Principle

The fundamental principle of error correction involves defining a subset of "valid" messages within the vast space of all possible messages <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. When a valid message is altered (e.g., by an error), the receiver attempts to correct it back to the nearest valid message <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Parity Checks

A foundational idea in error detection is the "parity check" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This method uses a single, dedicated bit (called the "parity bit") that the sender is responsible for setting <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

#### How a Parity Check Works
The parity bit's sole purpose is to ensure that the total number of 1s in a given block of data (including the parity bit itself) is an even number <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   If the current number of 1s is odd, the sender flips the parity bit to a 1 to make the total count even <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   If the count is already even, the parity bit remains a 0 <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

The "parity" of a group of bits refers to whether it has an even (0) or odd (1) number of 1s <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

#### Error Detection with Parity Checks
If any single bit in the message is flipped (from 0 to 1 or 1 to 0), it changes the total count of 1s from even to odd <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Therefore, if a receiver examines the message and finds an odd number of 1s, they know for certain that an error has occurred <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

#### Limitations of Parity Checks
While a parity check can detect that an error has occurred, it cannot pinpoint *where* the error is <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   If the receiver sees an odd parity, it means there was an odd number of errors (e.g., 1, 3, 5) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   If there were an even number of errors (e.g., 2, 4), the final count of 1s would still be even, meaning the parity check would not detect the error <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

This means a single parity check is "pretty weak" <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>, as it cannot provide 100% confidence in the message or correct errors <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. The goal of error detection and correction schemes is typically to be robust up to a certain maximum number of errors, or to reduce the probability of false positives <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Parity Checks as Building Blocks for Error Correction

Despite their limitations, parity checks are powerful building blocks for more sophisticated schemes <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. [[Relation between the puzzle and error correction | Hamming's key insight]] was that by applying multiple parity checks to carefully selected *subsets* of the message, it becomes possible to ask a refined series of questions that can pinpoint the location of any single-bit error <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This process is akin to a game of "20 questions," where yes or no queries narrow down possibilities <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

For instance, by setting up multiple parity bits that check different, overlapping groups of bits (e.g., specific columns and rows in a grid representation of data), a single error will cause a unique combination of parity check failures, revealing its exact position <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This concept leads directly to the design of [[Introduction to Hamming Codes | Hamming codes]], which can not only detect but also correct single-bit errors efficiently <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

Furthermore, a specific "overarching parity bit" (like the 0th bit in a 16-bit block) can be used to provide an [[Extending Hamming Codes for Improved Error Detection | extended Hamming code]] that allows for the detection of two-bit errors, even if they cannot be corrected <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. This occurs if the overall parity remains even (indicating two errors) while the more specific internal parity checks indicate a problem <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.