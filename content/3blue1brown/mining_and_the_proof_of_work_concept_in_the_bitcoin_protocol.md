---
title: Mining and the proof of work concept in the bitcoin protocol
videoId: bBC-nXj3Ng4
---

From: [[3blue1brown]] <br/> 

[[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] is a fully digital currency without a central government or banks managing accounts and verifying transactions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Its underlying technology, the [[blockchain_technology_and_its_application_in_cryptocurrency_transactions|blockchain]], relies on a clever system of [[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies|decentralized trustless verification]] based on cryptographic principles <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Understanding [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] means understanding what computers do when sending, receiving, and creating cryptocurrencies <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## The Decentralized Ledger Problem

At its core, [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] is a [[the_role_of_ledgers_digital_signatures_and_hash_functions_in_bitcoin|ledger]] <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. In a decentralized system where everyone keeps their own copy of the [[the_role_of_ledgers_digital_signatures_and_hash_functions_in_bitcoin|ledger]], a key challenge arises: how do participants agree on what the correct [[the_role_of_ledgers_digital_signatures_and_hash_functions_in_bitcoin|ledger]] is? <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a> How can one be sure that everyone else is recording the same transactions and in the same order? <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a> This is the fundamental problem [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] addresses <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## Proof of Work: The Solution

The solution offered by [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] is to trust the [[the_role_of_ledgers_digital_signatures_and_hash_functions_in_bitcoin|ledger]] that has the most computational work put into it <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. This concept, known as [[proof_of_work_concept_in_the_bitcoin_protocol|Proof of Work]], makes fraudulent transactions and conflicting ledgers infeasible to create due to the immense computation required <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

### Cryptographic Hash Functions

Central to [[proof_of_work_concept_in_the_bitcoin_protocol|Proof of Work]] is the [[hash_functions_and_sha256|cryptographic hash function]], specifically [[hash_functions_and_sha256|SHA256]] in [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Input and Output**: A hash function takes any message or file as input and produces a fixed-length string of bits (e.g., [[256_bit_security_concept|256 bits]]) as output, called a hash or digest <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Unpredictability**: Even a slight change in the input completely changes the resulting hash in an unpredictable way <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   **One-Way Function**: It is computationally infeasible to compute the hash in the reverse direction; meaning, given a hash, there's no better method than guessing and checking to find the input that produces that specific hash <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. This infeasibility is crucial for modern security <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. The number of possible [[256_bit_security_concept|256-bit]] hashes is 2 to the power of 256, an astronomically large number <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Demonstrating Work with Hashes

The concept of [[proof_of_work_concept_in_the_bitcoin_protocol|Proof of Work]] uses hash functions to prove that a significant amount of computational effort has been expended <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. Imagine someone shows a list of transactions and a "special number" such that when the number is appended to the list and [[hash_functions_and_sha256|SHA256]] is applied, the output hash starts with a specific number of zeros (e.g., 30 zeros) <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

Since [[hash_functions_and_sha256|SHA256]] is a [[hash_functions_and_sha256|cryptographic hash function]], the only way to find such a special number is by guessing and checking <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. The probability of a random hash starting with 30 zeros is 1 in 2^30 (about 1 in a billion) <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. Therefore, finding such a number almost certainly required about a billion guesses <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. Once found, verifying it is quick: simply run the hash and check the zeros <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. This process allows verification of a large amount of work without having to perform it yourself <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

Crucially, this work is intrinsically tied to the list of transactions. If even one transaction is slightly changed, the hash would change completely, requiring a new billion guesses to find a new [[proof_of_work_concept_in_the_bitcoin_protocol|Proof of Work]] <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

### Blocks and the Blockchain

In [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]], the [[the_role_of_ledgers_digital_signatures_and_hash_functions_in_bitcoin|ledger]] is organized into "blocks" <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Each block contains:
1.  A list of transactions <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
2.  A [[proof_of_work_concept_in_the_bitcoin_protocol|Proof of Work]] (a special number causing the block's hash to start with many zeros, e.g., 60 zeros) <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
3.  The hash of the previous block in its header <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

This chaining mechanism means that if any block is altered, or if the order of blocks is changed, it invalidates all subsequent blocks, requiring all their [[proof_of_work_concept_in_the_bitcoin_protocol|Proof of Work]] to be redone <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This is why the structure is called a [[blockchain_technology_and_its_application_in_cryptocurrency_transactions|blockchain]] <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

## Bitcoin Mining

[[bitcoin_mining_efficiency_and_technology|Mining]] is the process of creating blocks <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. [[bitcoin_mining_efficiency_and_technology|Block creators]] (miners) listen for broadcasted transactions, collect them into a block, and then perform the intensive work of finding the special number that yields a hash with the required number of leading zeros <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. Once found, they broadcast the valid block <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

### Block Reward and New Currency

To incentivize this work, miners are rewarded with new currency (Ledger Dollars in the example, [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] in the actual protocol) for successfully creating a block <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. This "block reward" is a special transaction where the miner creates money out of thin air, increasing the total currency supply <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. This is how new [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] enters the system <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

[[bitcoin_mining_efficiency_and_technology|Mining]] is analogous to a miniature lottery: miners guess numbers as fast as they can until one finds the special number that satisfies the hash requirement <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

### Decentralized Consensus

For users, the core principle is: if you hear two distinct [[blockchain_technology_and_its_application_in_cryptocurrency_transactions|blockchains]] with conflicting transaction histories, you defer to the longest one—the one with the most work put into it <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. If there's a tie, wait for an additional block to determine which chain is longer <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. This agreement to prefer the longest chain allows for [[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies|decentralized consensus]] without a central authority <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

### Security and Trusting Transactions

The [[proof_of_work_concept_in_the_bitcoin_protocol|Proof of Work]] system makes fraudulent activity extremely difficult. To fool someone with a fraudulent block (e.g., double-spending), an attacker would need to find valid [[proof_of_work_concept_in_the_bitcoin_protocol|Proof of Work]] for their fraudulent chain faster than all other honest miners combined <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>. Unless the attacker possesses close to 50% of the network's total computing resources, the legitimate [[blockchain_technology_and_its_application_in_cryptocurrency_transactions|blockchain]] will almost certainly grow faster, causing their fraudulent chain to be rejected <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.

Therefore, you shouldn't immediately trust a new block <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. Instead, wait for several new blocks to be added on top of it. If no longer, conflicting chains emerge, you can be confident that the block is part of the chain everyone else is using <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>.

## Bitcoin Protocol Details

*   **Difficulty Adjustment**: The [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] protocol periodically adjusts the difficulty (the required number of leading zeros in the hash) to ensure that a new block is found, on average, every 10 minutes, regardless of the number of miners <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
*   **Block Reward Halving**: The initial block reward was 50 [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] per block <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. This reward is halved approximately every four years (every 210,000 blocks) <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. This geometric decrease ensures there will never be more than 21 million [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] in existence <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **Transaction Fees**: In addition to the block reward, miners earn money through optional transaction fees <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>. Users can include a fee with their payment to incentivize miners to include their transaction in the next block <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>. This is particularly relevant because [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency|Bitcoin]] blocks have a limited capacity (about 2400 transactions) <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>, making fees a determinant for transaction inclusion <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>.