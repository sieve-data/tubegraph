---
title: Historical Background of Hamming Codes
videoId: X8jsijhllIA
---

From: [[3blue1brown]] <br/> 

## Introduction to Error Correction
Data storage and transmission often face challenges from errors, such as a scratched CD or DVD, where the physical damage affects the underlying 1s and 0s of the data [00:00:10]. Despite these errors, devices can often decode the data into a precise, bit-for-bit copy of the original file [00:00:21]. This resilience is due to mathematical cleverness that allows data to be stored and transmitted in a way that is resistant to errors [00:00:27].

A simple, though inefficient, strategy for error correction might involve storing three copies of each bit, allowing a machine to compare them and take the best two out of three in case of discrepancy [00:00:53]. However, this method dedicates two-thirds of storage space to redundancy and offers no strong guarantee against multiple bit flips [00:01:07]. The more interesting challenge lies in correcting errors while minimizing the space given up for redundancy [00:01:17]. Methods that allow for such error correction are known as [[introduction_to_hamming_codes | error correction codes]] [00:02:07].

For the better part of the last century, this field has been a rich source of surprisingly deep mathematics, which has been incorporated into devices used every day [00:02:13]. The aim of understanding this topic is to provide a thorough grasp of one of the earliest examples: a [[introduction_to_hamming_codes | Hamming code]] [00:02:22].

## The Birth of Hamming Codes
The story of [[introduction_to_hamming_codes | Hamming codes]] begins in the 1940s with a young Richard Hamming, who was working for Bell Labs [00:03:46]. Hamming had limited access to a large, expensive punch card computer for his work [00:03:51]. His programs frequently failed because bits would occasionally be misread [00:03:57]. Out of this frustration, Hamming invented the world's first [[introduction_to_hamming_codes | error correction code]] [00:04:03].

Although [[introduction_to_hamming_codes | Hamming codes]] are not as widely used today as more modern codes like the Reed-Solomon algorithm, their foundational principles demonstrate a "magic" in how a seemingly impossible task becomes utterly reasonable once understood [00:02:59].

## Fundamental Concepts
The basic principle of error correction involves defining a subset of "valid" messages within the vast space of all possible messages [00:03:13]. When a valid message is altered, the receiver's role is to correct it back to the nearest valid neighbor, similar to correcting a typo [00:03:28]. Developing a concrete algorithm for this categorization requires significant ingenuity [00:03:38].

### Parity Checks
A precursor to [[introduction_to_hamming_codes | Hamming codes]], and an idea fresh on Hamming's mind, was the concept of a parity check [00:05:47]. A parity check allows for the detection of any single bit error, but not their correction [00:05:50]. In a parity check, a single bit is designated by the sender to ensure that the total number of 1s in a message is an even number [00:06:04]. If this special bit is set to 1 when the initial count of 1s is odd, it makes the total count even; if the initial count is even, the bit remains 0 [00:06:15].

This simple mechanism is an elegant way to distill the idea of change within a message down to a single bit of information [00:06:27]. If any bit in the message is flipped (0 to 1, or 1 to 0), the total count of 1s changes from even to odd [00:06:37]. Therefore, if a receiver observes an odd number of 1s, they know an error has occurred, even if they don't know its location [00:06:47]. The property of a group of bits having an even or odd number of 1s is known as its *parity* (often represented as 0 for even, 1 for odd) [00:06:58], and the special bit used to control it is the *parity bit* [00:07:11].

While a single parity check can detect any odd number of errors (1, 3, 5, etc.), it cannot detect an even number of errors (2, 4, etc.) [00:07:21]. This means that an even count of 1s does not guarantee an error-free message [00:07:34]. No method of error detection or correction can provide 100% confidence, as enough random noise could change one valid message into another [00:07:49]. The goal is to create schemes that are robust up to a certain maximum number of errors or to reduce the probability of false positives [00:08:06].

### The Insight of Multiple Parity Checks
Hamming's key insight for identifying *where* an error happened was to apply multiple parity checks not to the full message, but to carefully selected subsets of bits [00:08:27]. By asking a series of refined questions through these checks, the location of any single bit error can be pinpointed [00:08:37]. This process is akin to a game of 20 questions, where each yes/no query halves the space of possibilities [00:08:46].

For example, performing a parity check on only the odd-numbered positions provides information that an error, if detected, lies within an odd position [00:08:54]. When combined with other strategically chosen checks, this counter-intuitively makes the system much more powerful [00:09:21].

## Hamming Code Structure (Example: 16-bit block)
A common example of a [[introduction_to_hamming_codes | Hamming code]] uses a 16-bit block [00:04:16]. In such a block, 12 bits constitute the actual data, while 4 positions are reserved for redundancy [00:04:25]. These 4 redundant bits are not simple copies; instead, they provide a "nuanced and clever" resilience without adding new information [00:04:40]. These special bits are typically placed at positions that are powers of two (e.g., positions 1, 2, 4, 8) for an elegant design that scales for larger blocks [00:04:54].

*   **Sender's Role**: The sender is responsible for setting these special bits [00:05:17].
*   **Receiver's Role**: The receiver performs checks and corrects errors [00:05:20].

By using four well-chosen parity checks, a machine can identify if a single bit error occurred and precisely where it was, allowing for correction [00:01:40]. If two bits get flipped, the system can detect that two errors occurred, although it won't know how to fix them [00:01:55]. This particular [[introduction_to_hamming_codes | Hamming code]] is referred to as a 15-11 Hamming code, meaning it uses a 15-bit block with 11 bits for the message and 4 for redundancy [00:14:44].

### [[extending_hamming_codes_for_improved_error_detection | Extended Hamming Codes]]
A clever addition, known as an [[extending_hamming_codes_for_improved_error_detection | extended Hamming code]], uses position 0 as an additional parity bit across the entire block [00:15:03]. This allows for the detection (though not correction) of 2-bit errors [00:15:08]. If a single bit error occurs, the full block's parity toggles to odd (which is also caught by the four error-correcting checks) [00:15:25]. However, if two errors occur, the overall parity toggles back to even, but the receiver would still see abnormalities from the four error-correcting checks, signaling at least two errors [00:15:34]. This demonstrates how the bothersome 0th bit can be put to extra work [00:15:54].