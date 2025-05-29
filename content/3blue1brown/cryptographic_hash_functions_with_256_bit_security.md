---
title: Cryptographic hash functions with 256 bit security
videoId: S9JGmA5_unY
---

From: [[3blue1brown]] <br/> 

Cryptographic hash functions, such as SHA-256, are fundamental to modern security. Breaking their security often involves guessing a specific string of 256 bits, a task requiring an immense number of attempts <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This concept also applies to [[Digital signatures and 256 bit security | digital signatures]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## The Challenge of Brute Force
To find a message whose SHA-256 hash matches a specific 256-bit string, the most effective method is to guess and check random messages <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This process would, on average, necessitate 2^256 guesses <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

### Understanding the Scale of 2^256
The number 2^256 is exceptionally large and difficult to comprehend <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. It can be expressed as 2^32 multiplied by itself 8 times <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Since 2^32 is approximately 4 billion <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, appreciating 2^256 means understanding what it feels like to multiply 4 billion by itself eight successive times <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

Consider the following thought experiment to grasp the magnitude:
*   **A Single Machine:** A highly optimized GPU, specially programmed for [[Role of cryptography and digital signatures in Bitcoin | cryptographic hash function]] computations, could perform nearly a billion hashes per second <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Imagine a computer packed with enough GPUs to execute 4 billion hashes per second <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This represents the first 4 billion in the 2^256 calculation <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Global Computing Power:** Now, picture 4 billion of these GPU-packed computers <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For context, Google's server estimates are in the single-digit millions, and most are less powerful than this imagined machine <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
    *   If Google replaced all its servers with these powerful machines, 4 billion such machines would be equivalent to about 1,000 copies of this "souped-up Google," termed a "kilo-Google" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Imagine giving over half of Earth's 7.3 billion people their own personal "kilo-Google" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Intergalactic Scale:** Next, envision 4 billion copies of this Earth <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
    *   With the Milky Way galaxy containing an estimated 100 to 400 billion stars <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, this would be akin to 1% of every star in the galaxy hosting a copy of Earth where half the population owns a "kilo-Google" <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Giga-Galactic Supercomputer:** Finally, imagine 4 billion copies of the Milky Way, forming a "giga-galactic supercomputer" capable of approximately 2^160 guesses per second <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   Even with this unimaginable power, guessing for 4 billion seconds (about 126.8 years) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, and then 4 billion *of those* timeframes (507 billion years) <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, which is about 37 times the age of the universe <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>, it would still only result in a 1 in 4 billion chance of finding the correct guess <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
<br>
This elaborate analogy demonstrates the near-impossibility of brute-forcing a 256-bit cryptographic hash. [[Computational limits in breaking 256 bit security | 256 bit security and its implications]] are profound, as even with immense computational resources and timeframes far exceeding the universe's age, the chance of success remains astronomically low.

## Bitcoin Mining and Specialized Hardware
The current state of [[Bitcoin mining and applicationspecific integrated circuits | Bitcoin mining]] provides a real-world example of intense hashing <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. All miners collectively perform about 5 quintillion hashes per second <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This remarkable rate is not due to billions of GPU-packed machines, but rather the use of [[Bitcoin mining and applicationspecific integrated circuits | application-specific integrated circuits]] (ASICs) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

ASICs are pieces of hardware specifically designed for [[Bitcoin mining and applicationspecific integrated circuits | Bitcoin mining]] and running SHA-256 hashes <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. They are about 1,000 times more efficient than general-purpose GPUs for this task <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. This efficiency comes from designing the integrated circuits for one specific task, eliminating the need for general computation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.