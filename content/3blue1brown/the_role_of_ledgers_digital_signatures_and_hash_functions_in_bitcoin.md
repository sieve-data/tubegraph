---
title: The role of ledgers digital signatures and hash functions in bitcoin
videoId: bBC-nXj3Ng4
---

From: [[3blue1brown]] <br/> 

[[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]] is a fully digital currency without a central government or banks to manage accounts and verify transactions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Understanding "what it means to have a Bitcoin" involves delving into the technical details of how it operates <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The foundational concepts include ledgers, [[digital_signatures_and_cryptography | digital signatures]], and [[hash_functions_and_sha256 | hash functions]], which together enable a [[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies | decentralized, trustless verification system]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## The Ledger Concept

Initially, a digital currency can be thought of as a communal ledger, a public and accessible record where anyone can add new lines to record payments <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. For example, "Alice pays Bob $20" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Traditionally, users would "settle up" physically at the end of a period based on these entries <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

A critical problem with a simple public ledger is preventing unauthorized entries, such as Bob writing "Alice pays Bob $100" without Alice's approval <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This problem leads to the integration of [[digital_signatures_and_cryptography | cryptography]].

### From Physical Settlement to Digital Currency

By preventing users from spending more than they have recorded on the ledger, the need to "settle up" with physical cash is removed <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. For instance, if everyone starts with 100 "ledger dollars" (LD), transactions are only valid if the sender has sufficient balance <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This means verifying a transaction requires knowing the full history of transactions <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This effectively detaches the ledger's currency from physical money, making it an independent digital currency <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

> "What it is, is a ledger. The history of transactions is the currency." <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>

## [[digital_signatures_and_cryptography | Digital Signatures]]

To ensure transactions are approved by the sender, [[digital_signatures_and_cryptography | digital signatures]] are employed <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### How They Work
Everyone generates a **public key-private key pair**, each appearing as a string of bits <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Private Key (SK)**: This key must be kept secret <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Public Key (PK)**: This key is shared publicly <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

A digital signature is a string of 1s and 0s, commonly 256 bits long <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. It is generated using a function that depends on both the message (transaction) and the sender's private key <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

Key properties of [[digital_signatures_and_cryptography | digital signatures]]:
*   **Uniqueness**: The signature changes completely if the message is altered even slightly <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This prevents copying a signature for use on another message <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Authenticity**: Only the private key holder can produce a valid signature <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Forging a signature without the private key is computationally infeasible <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>, requiring guessing from `2^256` possibilities <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Verifiability**: A second function uses the public key to verify if a signature is valid for a given message <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

To prevent replay attacks (copying valid signed transactions), each transaction message must include a unique ID <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This ensures that even identical transactions (e.g., Alice paying Bob $100 multiple times) require a completely new signature <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Decentralized Consensus and [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Proof of Work]]

Instead of a single public ledger, [[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies | cryptocurrencies]] require everyone to keep their own copy <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. When a transaction is made, it's broadcast to the world for individuals to record <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. The challenge then becomes how to ensure everyone agrees on the same ledger, particularly on the order and validity of transactions <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

[[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]]'s solution is to trust whichever ledger has the most computational work put into it <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. This relies on [[digital_signatures_and_cryptography | cryptographic hash functions]].

### [[hash_functions_and_sha256 | Cryptographic Hash Functions]] (e.g., SHA256)

A [[hash_functions_and_sha256 | hash function]] takes any message or file as input and produces a fixed-length string of bits as output, called a hash or digest <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. For example, [[hash_functions_and_sha256 | SHA256]] produces a 256-bit output <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

Key properties of [[hash_functions_and_sha256 | cryptographic hash functions]]:
*   **Determinism**: The same input always yields the same output <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Avalanche Effect**: A slight change in the input completely changes the resulting hash in an unpredictable way <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   **One-way property**: It is computationally infeasible to compute the input message given only its hash. The only known method is guessing and checking <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. This property is fundamental to modern security <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

### [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Proof of Work]]

[[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Proof of work]] leverages [[hash_functions_and_sha256 | cryptographic hash functions]] to demonstrate that a significant amount of computational effort has been expended <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

For instance, finding a "special number" that, when appended to a list of transactions, results in an [[hash_functions_and_sha256 | SHA256]] hash starting with 30 zeros <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Since the probability of a random hash starting with 30 zeros is 1 in `2^30` (about 1 billion), finding such a number almost certainly required about a billion guesses <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. While hard to find, it's quick to verify <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

This work is intrinsically linked to the data: changing even one transaction in the list would completely alter the hash, requiring a new [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | proof of work]] to be found <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

## The [[blockchain_technology_and_its_application_in_cryptocurrency_transactions | Blockchain]]

The ledger is organized into **blocks**, where each block contains a list of transactions and its own [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | proof of work]] (a special number that makes its hash start with a certain number of zeros) <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. For order, each block must also contain the hash of the **previous block** at its header <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

This chaining mechanism means:
*   Altering a past block, or changing the order of blocks, invalidates all subsequent blocks because their hashes would no longer match the previous block's hash <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
*   This would require redoing all the [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | proof of work]] for every subsequent block <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
Because blocks are chained together, the entire structure is called a [[blockchain_technology_and_its_application_in_cryptocurrency_transactions | blockchain]] <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

## [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Mining]] and Rewards

Anyone can become a "block creator" or **[[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | miner]]** <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Miners]] listen for broadcast transactions, gather them into a block, and then perform intense computational work (guessing special numbers) to find a valid [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | proof of work]] for that block <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.

When a [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | miner]] successfully finds a [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | proof of work]], they broadcast the new block <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>. As a reward, they are allowed to include a special transaction at the top of their block, granting themselves new currency (e.g., 10 ledger dollars) <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. This is known as the **block reward**, which introduces new money into the economy and is an exception to the usual transaction rules (it doesn't need to be signed) <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.

The act of creating blocks is called [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | mining]], reflecting the hard work and the introduction of new currency <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Miners]] essentially participate in a "miniature lottery" by guessing numbers until one finds a valid hash <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

### Consensus and Trust in the Longest Chain
For users, the protocol dictates that if two distinct [[blockchain_technology_and_its_application_in_cryptocurrency_transactions | blockchains]] with conflicting transaction histories are encountered, the one with the most computational work (the **longest chain**) should be trusted <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. This mechanism enables [[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies | decentralized consensus]] without a central authority <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.

For a transaction to be considered truly legitimate, one should wait for several new blocks to be added on top of it <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>. This is because a fraudulent block, even if initially accepted by one person, would likely be outpaced by the legitimate chain worked on by the majority of miners <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. Unless a malicious actor controls close to 50% of the network's computing resources, their fraudulent chain will quickly fall behind <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.

### Bitcoin Specifics
*   **Difficulty Adjustment**: The [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin protocol]] periodically adjusts the difficulty (number of leading zeros required in a hash) to ensure a new block is found, on average, every 10 minutes <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
*   **Block Reward Halving**: The initial block reward for [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin]] was 50 Bitcoin <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. This reward is halved every 210,000 blocks (approximately every 4 years) <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. This geometric decrease limits the total supply of [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]] to a maximum of 21 million <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **Transaction Fees**: In addition to block rewards, [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | miners]] also earn transaction fees <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>. Users can optionally include a fee with their payment to incentivize [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | miners]] to include their transaction in the next block, especially given [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]]'s block size limit of approximately 2400 transactions <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.