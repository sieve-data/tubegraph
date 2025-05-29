---
title: Digital signatures and cryptography
videoId: S9JGmA5_unY
---

From: [[3blue1brown]] <br/> 

In the context of [[the_role_of_ledgers_digital_signatures_and_hash_functions_in_bitcoin | cryptocurrencies]], breaking certain security measures, such as those related to [[the_role_of_ledgers_digital_signatures_and_hash_functions_in_bitcoin | digital signatures]] or [[hash_functions_and_sha256 | cryptographic hash functions]], often requires guessing a specific string of [[256_bit_security_concept | 256 bits]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. For instance, to find a message whose [[hash_functions_and_sha256 | SHA-256]] hash matches a specific 256-bit string, the most effective method is to guess and check random messages, which would, on average, necessitate 2^256 guesses <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## The Impossibility of Guessing 256-bit Strings

The number 2^256 is astronomically large, making its scale difficult to comprehend <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. To illustrate its magnitude, 2^256 can be expressed as 2^32 multiplied by itself eight times <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Since 2^32 equals 4 billion, this means envisioning 4 billion multiplied by itself eight successive times <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

Consider the following thought experiment to grasp the scale:

*   **Computing Power:** A high-performance [[gpu_and_asics_in_cryptographic_computations | GPU]], specifically programmed for cryptographic hashing, could perform nearly a billion hashes per second <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Imagine a computer packed with enough [[gpu_and_asics_in_cryptographic_computations | GPUs]] to execute 4 billion hashes per second <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Kilo-Google:** Next, picture 4 billion of these [[gpu_and_asics_in_cryptographic_computations | GPU]]-packed computers <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For context, estimates place Google's server count in the single-digit millions <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This hypothetical setup would be equivalent to approximately 1,000 copies of a "souped-up Google," a concept termed a "kilo-Google" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Planetary Scale:** With 7.3 billion people on Earth, imagine giving a little over half of every individual their own personal kilo-Google <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Intergalactic Scale:** Now, envision 4 billion copies of this Earth <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Given that the Milky Way galaxy contains between 100 and 400 billion stars, this would be akin to 1% of every star in the galaxy having a copy of Earth, where half its population owns a personal kilo-Google <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Time Scale:** This "giga-galactic supercomputer" would be performing 2^160 guesses every second <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   4 billion seconds is roughly 126.8 years <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    *   4 billion of *those* spans 507 billion years, which is about 37 times the age of the universe <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

Even with this unimaginable computational power guessing for 37 times the age of the universe, there would still only be a 1 in 4 billion chance of finding the correct guess <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Real-world Hashing in Cryptocurrencies

The collective [[blockchain_technology_and_its_application_in_cryptocurrency_transactions | Bitcoin]] mining network currently performs guesses at a rate of approximately 5 billion billion hashes per second <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This immense power is not achieved through billions of [[gpu_and_asics_in_cryptographic_computations | GPU]]-packed machines, but by the use of [[gpu_and_asics_in_cryptographic_computations | Application-Specific Integrated Circuits (ASICs)]] <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. [[gpu_and_asics_in_cryptographic_computations | ASICs]] are hardware specifically designed for [[blockchain_technology_and_its_application_in_cryptocurrency_transactions | Bitcoin]] mining, optimized solely for executing [[hash_functions_and_sha256 | SHA-256]] hashes <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. By eliminating the need for general computation, [[gpu_and_asics_in_cryptographic_computations | ASICs]] achieve significant efficiency gains, making them roughly 1,000 times more efficient than [[gpu_and_asics_in_cryptographic_computations | GPUs]] for this specific task <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.