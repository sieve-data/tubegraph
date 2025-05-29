---
title: Bitcoin mining efficiency and technology
videoId: S9JGmA5_unY
---

From: [[3blue1brown]] <br/> 

In the context of cryptocurrencies, breaking security often involves guessing a specific string of 256 bits <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This applies to [[the_role_of_ledgers_digital_signatures_and_hash_functions_in_bitcoin | digital signatures]] and [[hash_functions_and_sha256 | cryptographic hash functions]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. For instance, to find a message whose [[hash_functions_and_sha256 | SHA-256 hash]] is a specific 256-bit string, the most effective method is random guessing, which would, on average, require 2 to the 256 guesses <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This number is astronomically large, making such brute-force attacks practically impossible.

## Computational Power Required

To grasp the scale of 2^256, consider that it's equivalent to 2^32 multiplied by itself 8 times <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Since 2^32 is 4 billion <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>, this means appreciating what multiplying 4 billion by itself eight successive times feels like <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Evolution of Mining Technology

### GPUs

A [[GPU and ASICs in cryptographic computations | GPU]] (Graphics Processing Unit) can perform many computations in parallel at an incredibly fast rate <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. A high-performance [[GPU and ASICs in cryptographic computations | GPU]], specially programmed for running cryptographic hash functions, can achieve nearly a billion hashes per second <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. If a computer were packed with multiple [[GPU and ASICs in cryptographic computations | GPUs]], it could potentially run 4 billion hashes per second <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### ASICs

The current state of [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin hashing]] involves miners collectively performing approximately 5 billion billion hashes per second <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This immense computational power is not achieved by an abundance of [[GPU and ASICs in cryptographic computations | GPU-packed machines]] <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Instead, [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin miners]] utilize [[GPU and ASICs in cryptographic computations | Application-Specific Integrated Circuits (ASICs)]], which are about 1000 times more efficient than a [[GPU and ASICs in cryptographic computations | GPU]] for this specific task <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

[[GPU and ASICs in cryptographic computations | ASICs]] are hardware components specifically engineered for [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin mining]] and running [[hash_functions_and_sha256 | SHA-256 hashes]] <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. They achieve significant efficiency gains by being designed for one particular task, unlike general-purpose computing devices <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.