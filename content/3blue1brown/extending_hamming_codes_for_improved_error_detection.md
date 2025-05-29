---
title: Extending Hamming Codes for Improved Error Detection
videoId: X8jsijhllIA
---

From: [[3blue1brown]] <br/> 

While a standard [[introduction_to_hamming_codes | Hamming code]] allows for the correction of any single bit error, it faces a challenge with larger blocks when differentiating between no error and an error occurring at a specific "null" position. This issue, initially handled by simply omitting the 0th bit and thus creating a 15-bit block from a 16-bit concept, can be cleverly resolved by using the 0th bit to enhance error detection capabilities <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

## The Problem with Position 0 <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>

In a 16-bit block using four [[parity_checks_and_error_detection | parity checks]], there are 16 possible outcomes for the checks, which seems perfect for pinpointing 1 out of 16 positions <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. However, an additional 17th outcome is needed to indicate that no error has occurred <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. If all four [[parity_checks_and_error_detection | parity checks]] indicate an even parity, it could mean either no error or that an error occurred specifically at position 0 <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. The initial simple solution was to discard the 0th bit entirely, resulting in a 15-bit block where 11 bits carry data and 4 bits are for redundancy—known as a 15-11 [[introduction_to_hamming_codes | Hamming code]] <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

## Introducing the Extended Hamming Code <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>

A more sophisticated approach, known as an **extended [[introduction_to_hamming_codes | Hamming code]]**, allows for keeping the 0th bit and utilizing it for enhanced error detection <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. This method leverages the 0th bit as an additional [[parity_checks_and_error_detection | parity bit]] for the *entire* block <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

### How it Works <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>

1.  **Sender's Role**: After the four main [[error_correction_and_data_redundancy | error-correcting]] bits are set, the 0th bit is set to ensure the [[parity_checks_and_error_detection | parity]] of the *full* 16-bit block is even <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
2.  **Single Bit Errors**: If a single bit error occurs, the overall [[parity_checks_and_error_detection | parity]] of the block will toggle to odd <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This change, combined with the non-zero result from the four standard [[parity_checks_and_error_detection | parity checks]], allows the receiver to precisely locate and correct the error <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
3.  **Two Bit Errors**: If two bits are flipped, the overall [[parity_checks_and_error_detection | parity]] of the block will toggle back to being even <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. However, the receiver will still observe a "non-zero" outcome from the four primary [[parity_checks_and_error_detection | parity checks]] (meaning at least one of them will indicate an error) <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. This combination (even overall [[parity_checks_and_error_detection | parity]] but active internal [[parity_checks_and_error_detection | parity checks]]) signals to the receiver that there were at least two errors, even though the specific locations cannot be corrected <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

This clever use of the 0th bit enables the detection of 2-bit errors, providing an improved level of resilience without significantly increasing redundancy <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. The inventor, [[historical_background_of_hamming_codes | Richard Hamming]], developed these concepts during his time at Bell Labs in the 1940s, driven by the frustration of frequent bit errors in punch card computers <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.