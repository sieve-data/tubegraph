---
title: Hash functions and SHA256
videoId: S9JGmA5_unY
---

From: [[3blue1brown]] <br/> 

SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that produces a 256-bit (32-byte) hash value. This function is fundamental to security in various contexts, notably in [[the_role_of_ledgers_digital_signatures_and_hash_functions_in_bitcoin | cryptocurrencies]] like Bitcoin and in [[digital_signatures_and_cryptography | digital signatures]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Breaking SHA-256 Security

To break a piece of security related to SHA-256, such as finding a message that produces a specific 256-bit hash, there is no better method than to simply guess and check random messages <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. On average, this would require 2 to the power of 256 guesses <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## The Magnitude of 2^256

The number 2^256 is astronomically large, making it difficult to comprehend <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
It can be broken down as 2^32 multiplied by itself 8 times <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
Since 2^32 equals 4 billion <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, appreciating 2^256 means understanding what multiplying 4 billion by itself eight successive times feels like <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Illustrating the Scale of Computation

To grasp the scale of 2^256, consider the following hypothetical scenario:
*   **GPU Power**: A high-performance [[gpu_and_asics_in_cryptographic_computations | GPU]] specially programmed for cryptographic hashing might perform a little less than a billion hashes per second <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Super-Computer**: Imagine a computer packed with enough [[gpu_and_asics_in_cryptographic_computations | GPUs]] to perform 4 billion hashes per second <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This represents the first "4 billion" factor in the 2^256 calculation <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Kilo-Google**: Next, picture 4 billion of these [[gpu_and_asics_in_cryptographic_computations | GPU]]-packed computers <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For comparison, Google's server estimates are in the single-digit millions <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Four billion such machines would be equivalent to about 1,000 copies of a "souped-up Google," termed "1 kilo-Google" of computing power <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Personal Kilo-Google**: With roughly 7.3 billion people on Earth <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, imagine over half of every person on Earth owning their own personal kilo-Google <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Multi-Earths**: Then, imagine 4 billion copies of this Earth <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Considering the Milky Way galaxy has between 100 and 400 billion stars <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, this would be akin to 1% of every star in the galaxy having such an Earth <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Giga-Galactic Supercomputer**: Finally, envision 4 billion copies of the Milky Way, forming a "giga-galactic supercomputer" capable of running 2^160 guesses per second <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Time to Crack

If this giga-galactic supercomputer were to run for 4 billion seconds (approximately 126.8 years) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, and then this entire process was repeated 4 billion times, it would total 507 billion years <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This duration is about 37 times the age of the universe <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Even after such an immense computational effort, this multi-planetary giga-galactic computer would still only have a 1 in 4 billion chance of finding the correct guess for a 256-bit string <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Bitcoin Hashing and ASICs

The collective hashing power of all Bitcoin miners currently performs around 5 billion billion hashes per second <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This corresponds to about one-third of the "kilo-Google" computational power described in the analogy <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

This immense hashing rate is not achieved through billions of [[gpu_and_asics_in_cryptographic_computations | GPU]]-packed machines <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, but through the use of Application-Specific Integrated Circuits (ASICs) <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. ASICs are hardware specifically designed for Bitcoin mining, optimized solely for running SHA-256 hashes <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. By eliminating the need for general computation, ASICs achieve significant efficiency gains, making them about 1000 times more efficient than [[gpu_and_asics_in_cryptographic_computations | GPUs]] for this specific task <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.