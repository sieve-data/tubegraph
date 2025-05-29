---
title: Bitcoin mining and applicationspecific integrated circuits
videoId: S9JGmA5_unY
---

From: [[3blue1brown]] <br/> 

In the context of [[understanding_the_basics_of_bitcoin_and_cryptocurrency | cryptocurrencies]], breaking certain security measures, such as finding a message whose [[cryptographic_hash_functions_with_256_bit_security | SHA-256 hash]] matches a specific 256-bit string, requires guessing and checking random messages <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This process demands, on average, 2 to the 256 guesses <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This immense number highlights the challenge of brute-forcing cryptographic security based on [[256_bit_security and its implications | 256-bit security]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Hardware for Hashing

Initially, the power of Graphics Processing Units (GPUs) was considered for these computational tasks <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. A well-programmed GPU could perform nearly a billion [[cryptographic_hash_functions_with_256_bit_security | hashes]] per second <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. A computer packed with multiple GPUs might achieve 4 billion hashes per second <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Application-Specific Integrated Circuits (ASICs)

However, the landscape of [[bitcoin_mining_and_block_creation | Bitcoin hashing]] has evolved beyond general-purpose GPUs <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. While all [[bitcoin_mining_and_block_creation | Bitcoin miners]] collectively process approximately 5 billion billion hashes per second <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, this immense rate is not achieved through vast numbers of GPU-equipped machines <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Instead, miners utilize [[applications_in_computer_graphics_and_robotics | Application-Specific Integrated Circuits]] (ASICs) <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

ASICs are specialized hardware designed for a single purpose <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. For [[bitcoin_mining_and_block_creation | Bitcoin mining]], they are built specifically to run [[cryptographic_hash_functions_with_256_bit_security | SHA-256 hashes]] with high efficiency <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. These devices offer substantial efficiency gains—approximately 1000 times better than a GPU for this specific task <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. This improvement comes from discarding the need for general computation and optimizing the integrated circuits for one singular function <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.