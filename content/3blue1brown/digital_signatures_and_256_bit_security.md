---
title: Digital signatures and 256 bit security
videoId: S9JGmA5_unY
---

From: [[3blue1brown]] <br/> 

The concept of [[256_bit_security_and_its_implications | 256-bit security]] is fundamental in modern [[role_of_cryptography_and_digital_signatures_in_bitcoin | cryptography]], particularly in the context of [[role_of_cryptography_and_digital_signatures_in_bitcoin | digital signatures]] and [[cryptographic_hash_functions_with_256_bit_security | cryptographic hash functions]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. To "break" a piece of security protected by a 256-bit string, one would hypothetically need to guess that specific string <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## The Challenge of Breaking 256-Bit Security

In scenarios involving [[cryptographic_hash_functions_with_256_bit_security | cryptographic hash functions]], such as finding a message that produces a specific SHA-256 hash, there is no more efficient method than randomly guessing and checking messages <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. On average, this brute-force approach would require 2^256 guesses <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

### Understanding the Magnitude of 2^256

The number 2^256 is unimaginably large, far removed from typical human scales <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. To grasp its scale, 2^256 can be broken down as (2^32)^8 <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, where 2^32 is approximately 4 billion <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

Consider the following analogy to illustrate the scale of 2^256 guesses <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>:

*   **Computational Power**: A highly optimized Graphics Processing Unit (GPU) can perform around a billion [[cryptographic_hash_functions_with_256_bit_security | cryptographic hash functions]] per second <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **A Hypothetical Machine**: Imagine a computer packed with enough GPUs to execute 4 billion hashes per second <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Global Computing Scale**:
    *   Next, envision 4 billion of these GPU-packed computers <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For context, Google's server estimates are in the single-digit millions, and most are less powerful than this imagined machine <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This would be equivalent to about 1,000 copies of a "souped-up Google" (referred to as 1 kilo-Google) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Now, imagine giving a little over half of Earth's 7.3 billion people their own personal kilo-Google <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Then, picture 4 billion copies of this Earth <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This would be like 1% of every star in the Milky Way (which has 100-400 billion stars) having such an Earth <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   Finally, imagine 4 billion copies of the Milky Way, forming a "giga-galactic supercomputer" capable of running 2^160 guesses every second <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Time Scale**: Even if this giga-galactic supercomputer were to run for 4 billion seconds (approximately 126.8 years) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, and then this entire process were repeated 4 billion times, it would take 507 billion years—roughly 37 times the age of the universe <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Even with this immense [[computational_limits_in_breaking_256_bit_security | computational power]] and time, it would still only have a 1 in 4 billion chance of finding the correct 256-bit guess <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Real-World Hashing Power (Bitcoin)

The collective hashing power of [[role_of_cryptography_and_digital_signatures_in_bitcoin | Bitcoin]] miners today is about 5 quintillion hashes per second <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, which is roughly one-third of the "kilo-Google" described in the analogy <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This immense power is not achieved through billions of GPUs, but through application-specific integrated circuits (ASICs) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. ASICs are hardware components designed specifically for tasks like running SHA-256 hashes, offering significant efficiency gains by sacrificing general computation capabilities <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This specialized design highlights the [[computational_limits_in_breaking_256_bit_security | computational limits]] and resources dedicated to maintaining [[256_bit_security_and_its_implications | 256-bit security]] in practice.