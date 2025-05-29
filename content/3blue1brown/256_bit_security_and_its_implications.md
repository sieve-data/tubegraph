---
title: 256 bit security and its implications
videoId: S9JGmA5_unY
---

From: [[3blue1brown]] <br/> 

[[digital_signatures_and_256_bit_security | 256-bit security]] refers to a level of cryptographic strength where breaking the security requires guessing a specific string of 256 bits <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This concept is relevant in various cryptographic applications, including [[digital_signatures_and_256_bit_security | digital signatures]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a> and [[cryptographic_hash_functions_with_256_bit_security | cryptographic hash functions]] like SHA-256 <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Breaking 256-bit Security

To find a message whose SHA-256 hash matches a specific 256-bit string, the most effective method is to guess and check random messages <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This process would require, on average, 2 to the power of 256 guesses <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

### Understanding the Scale of 2^256

The number 2^256 is astronomically large and difficult to comprehend <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. It can be expressed as 2^32 multiplied by itself 8 times <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Since 2^32 is approximately 4 billion <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, appreciating 2^256 means understanding what it feels like to multiply 4 billion by itself 8 successive times <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

To illustrate the sheer scale of 2^256 guesses, consider the following thought experiment:

*   **Computational Unit**: Imagine a high-performance computer packed with GPUs, capable of performing 4 billion hashes per second <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. A single GPU might typically perform less than a billion hashes per second <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **1 Kilo-Google**: Picture 4 billion of these GPU-packed computers <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For context, estimates place Google's server count in the single-digit millions <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This collection of 4 billion machines would be equivalent to approximately 1,000 copies of a "souped-up Google," a unit referred to as "1 kilo-Google" <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>, <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Global Computing Power**: Envision giving a little over half of Earth's 7.3 billion people their own personal "kilo-Google" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Intergalactic Scale**: Now, imagine 4 billion copies of this "Earth" <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This scale is akin to 1% of every star in the Milky Way galaxy (which has an estimated 100 to 400 billion stars) having a copy of Earth, where half its population owns a personal kilo-Google <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Giga-Galactic Supercomputer**: Finally, consider 4 billion copies of the Milky Way galaxy itself <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>, forming a "giga-galactic supercomputer" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. This supercomputer would be capable of performing 2^160 guesses every second <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

Even with such an unfathomably powerful "giga-galactic" computer, the time required to make 2^256 guesses is immense:

*   4 billion seconds is approximately 126.8 years <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   4 billion of those 4-billion-second periods total 507 billion years <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, which is about 37 times the age of the universe <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

Even if this "GPU-packed kilo-Google-per-person multiplanetary giga-galactic computer" were guessing numbers for 37 times the age of the universe, it would still only have a 1 in 4 billion chance of finding the correct guess <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This demonstrates the near-impossibility of breaking 256-bit security through brute force within any conceivable timeframe, highlighting [[computational_limits_in_breaking_256_bit_security | computational limits in breaking 256-bit security]].

## Real-world Hashing Power

In the context of [[role_of_cryptography_and_digital_signatures_in_bitcoin | Bitcoin]], the collective hashing power of all miners is approximately 5 billion billion hashes per second <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This corresponds to about one-third of a "kilo-Google" as described in the thought experiment <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This immense hashing power is achieved not by using billions of GPU-packed machines, but by employing [[bitcoin_mining_and_applicationspecific_integrated_circuits | application-specific integrated circuits]] (ASICs) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

ASICs are hardware components specifically designed for [[bitcoin_mining_and_applicationspecific_integrated_circuits | Bitcoin mining]], optimized solely for running SHA-256 hashes <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>, <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. They offer significant efficiency gains by sacrificing general computation capabilities for specialized, single-task execution <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.