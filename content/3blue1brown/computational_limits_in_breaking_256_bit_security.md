---
title: Computational limits in breaking 256 bit security
videoId: S9JGmA5_unY
---

From: [[3blue1brown]] <br/> 

In discussions about cryptocurrencies, references are often made to situations where breaking a piece of security requires guessing a specific string of [[256_bit_security_and_its_implications | 256 bits]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This applies to contexts like [[digital_signatures_and_256_bit_security | digital signatures]] and [[cryptographic_hash_functions_with_256_bit_security | cryptographic hash functions]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. For instance, to find a message whose [[cryptographic_hash_functions_with_256_bit_security | SHA-256 hash]] matches a specific [[256_bit_security_and_its_implications | 256-bit]] string, the most effective method is random guess and check <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Impossibility of 2^256 Guesses

Breaking [[256_bit_security_and_its_implications | 256-bit]] security would typically require, on average, 2 to the power of 256 guesses <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This number is astronomically large, making its scale difficult to comprehend <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

To put 2^256 into perspective:
*   2^256 can be broken down as (2^32)^8 <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   2^32 is approximately 4 billion <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   The challenge lies in appreciating what multiplying 4 billion by itself 8 successive times truly means <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### An Illustrative Analogy

Imagine a high-performance GPU specially programmed to run a [[cryptographic_hash_functions_with_256_bit_security | cryptographic hash function]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. A very efficient GPU could perform nearly a billion hashes per second <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

Let's scale up this computing power:
1.  **A single computer:** A computer packed with GPUs, running 4 billion hashes per second <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This represents the first "4 billion" in the 2^256 calculation <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
2.  **Kilo-Google:** Picture 4 billion of these GPU-packed computers <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For comparison, Google's server estimates are in the single-digit millions, with most being less powerful than our imagined machine <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This means 4 billion machines would be roughly 1,000 copies of a "souped-up Google," termed a "kilo-Google" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
3.  **Planetary Scale:** Imagine giving over half of Earth's 7.3 billion people their own personal kilo-Google <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
4.  **Multi-planetary Scale:** Now, envision 4 billion copies of this Earth <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. The Milky Way galaxy has between 100 and 400 billion stars <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This scenario would be akin to 1% of every star in the galaxy hosting a copy of Earth, where half the inhabitants have their own kilo-Google <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
5.  **Giga-galactic Supercomputer:** Finally, try to imagine 4 billion copies of the Milky Way <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. This is conceptualized as a "giga-galactic supercomputer," performing about 2 to the 160 guesses every second <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

Even with this incomprehensible computing power, the time required to make 2^256 guesses is immense:
*   4 billion seconds is approximately 126.8 years <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   Multiplying that by another 4 billion results in 507 billion years <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   This duration is about 37 times the age of the universe <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

<div class="callout is-warning">
Even if a "GPU-packed kilo-Google-per-person multiplanetary giga-galactic computer" were guessing numbers for 37 times the age of the universe, it would still only have a 1 in 4 billion chance of finding the correct guess <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This illustrates the robust nature of [[256_bit_security_and_its_implications | 256-bit security]].
</div>

## Real-World Hashing Power (Bitcoin)

The current state of Bitcoin hashing involves miners collectively performing approximately 5 billion billion hashes per second <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This incredible rate corresponds to about one-third of the "kilo-Google" described in the analogy <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

This computing power is not achieved through billions of GPU-packed machines, but by using Application-Specific Integrated Circuits (ASICs) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. ASICs are specialized hardware designed specifically for Bitcoin mining and executing [[cryptographic_hash_functions_with_256_bit_security | SHA-256 hashes]] <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. They are about 1,000 times more efficient than GPUs for this singular task, demonstrating significant efficiency gains when hardware is designed for a specific purpose rather than general computation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.