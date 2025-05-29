---
title: 256 bit security concept
videoId: S9JGmA5_unY
---

From: [[3blue1brown]] <br/> 

The concept of "256-bit security" refers to the immense computational difficulty involved in breaking security measures that rely on guessing a specific string of 256 bits <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This principle is fundamental in areas such as [[digital_signatures_and_cryptography | digital signatures]] and [[hash_functions_and_sha256 | cryptographic hash functions]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## The Challenge of Guessing 256 Bits

To find a message whose [[hash_functions_and_sha256 | SHA-256]] hash matches a specific 256-bit string, there is no better method than random guessing and checking <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. On average, this would require 2 to the power of 256 guesses <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

### Understanding the Scale: 2^256

The number 2^256 is unfathomably large <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. It can be expressed as (2^32) multiplied by itself 8 times <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Since 2^32 is approximately 4 billion <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, 2^256 represents 4 billion multiplied by itself eight successive times <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

To illustrate the magnitude of 2^256, consider the following hypothetical scenario:

*   **Individual Computer Power:** A highly optimized [[GPU and ASICs in cryptographic computations | GPU]], specially programmed for [[hash_functions_and_sha256 | cryptographic hash functions]], might perform a little less than a billion hashes per second <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. A computer packed with extra [[GPU and ASICs in cryptographic computations | GPUs]] could potentially run 4 billion hashes per second <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Kilo-Google Computing Power:** Imagine 4 billion such GPU-packed computers <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This would be roughly equivalent to 1,000 copies of Google's estimated server infrastructure, referred to as 1 kilo-Google <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Planetary Scale:** Next, envision giving over half of the 7.3 billion people on Earth their own personal kilo-Google <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Interstellar Scale:** Then, picture 4 billion copies of this Earth <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, akin to 1% of every star in the Milky Way galaxy hosting such an Earth <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Giga-Galactic Supercomputer:** Finally, imagine 4 billion copies of the Milky Way galaxy, forming a "giga-galactic supercomputer" capable of making approximately 2^160 guesses every second <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Even with this unprecedented computational power, if this giga-galactic supercomputer were to guess numbers for 37 times the age of the universe (which is 507 billion years, derived from 4 billion periods of 4 billion seconds each) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, it would still only have a 1 in 4 billion chance of finding the correct 256-bit string <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Real-World Application: Bitcoin Mining

In the context of [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin mining]], all miners collectively perform [[hash_functions_and_sha256 | hash]] computations at a rate of about 5 billion billion hashes per second <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This remarkable speed, equivalent to one-third of a "kilo-Google" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, is not achieved by widespread use of [[GPU and ASICs in cryptographic computations | GPUs]] <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Instead, miners utilize [[GPU and ASICs in cryptographic computations | Application-Specific Integrated Circuits (ASICs)]] <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. These [[GPU and ASICs in cryptographic computations | ASICs]] are about 1,000 times more efficient than [[GPU and ASICs in cryptographic computations | GPUs]] for tasks like [[hash_functions_and_sha256 | SHA-256]] hashing <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Their efficiency stems from being specifically designed for one task, such as [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin mining]], rather than general computation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.