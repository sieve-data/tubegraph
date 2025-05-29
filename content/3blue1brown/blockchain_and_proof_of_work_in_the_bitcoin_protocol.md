---
title: Blockchain and proof of work in the Bitcoin protocol
videoId: bBC-nXj3Ng4
---

From: [[3blue1brown]] <br/> 

## Understanding Bitcoin: A Ledger-Based Currency

[[understanding_the_basics_of_bitcoin_and_cryptocurrency | Bitcoin]] is a fully digital currency not issued by any government, nor managed by banks for accounts or transactions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. It operates on a system of decentralized, trustless verification rooted in cryptography <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. To grasp "what it means to have a Bitcoin," one must understand its underlying technical details <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### From Communal Ledgers to Digital Currencies

The foundational concept of Bitcoin can be understood by imagining a communal ledger used by friends to track payments <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Initially, this ledger is public, like a website where anyone can add new lines, and settlements occur monthly <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

A key challenge with such a public ledger is preventing unauthorized entries, such as Bob falsely recording "Alice pays Bob $100" without Alice's approval <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Role of Cryptography and Digital Signatures

This is where [[role_of_cryptography_and_digital_signatures_in_bitcoin | digital signatures]] come into play <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The concept is that Alice can add something to a transaction that proves her approval, making forgery infeasible <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

A digital signature system involves:
*   **Public Key-Private Key Pair**: Everyone generates a unique pair, each being a string of bits <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The private (or secret) key (SK) is kept secret, while the public key (PK) is shared <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Message-Dependent Signatures**: Unlike handwritten signatures, a digital signature changes for different messages <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. It's a string of ones and zeros, often [[cryptographic_hash_functions_with_256_bit_security | 256 bits]] long <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Even a slight alteration to the message completely changes the signature <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Signing and Verification**: A signature is produced by a function depending on both the message and the private key <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. A separate function, using the public key, verifies if a signature is valid <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. It is infeasible to find a valid signature without knowing the secret key, as it would require guessing and checking 2 to the power of [[256_bit_security_and_its_implications | 256 possible signatures]] <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

To prevent replay attacks (where a valid signed transaction is copied multiple times), each signed transaction must include a unique ID <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### From IOUs to "Ledger Dollars"

Initially, the ledger still relies on an honor system for settling up in cash <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. To eliminate this need for trust, the system evolves:
1.  Everyone contributes initial funds to a virtual "pot" recorded on the ledger <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
2.  Transactions are only accepted if the sender has sufficient funds already recorded on the ledger <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. This means verifying a transaction requires knowing the full history of transactions <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

This crucial step disconnects the ledger from physical currency, allowing the quantities on the ledger to become their own independent currency, termed "ledger dollars" (LD) <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This is the first fundamental point about Bitcoin: it *is* a ledger, and the history of transactions *is* the currency <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## The Decentralization Challenge: Consensus in a Trustless System

The next challenge is decentralizing the ledger itself, as relying on a central website or authority introduces a point of trust <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. The solution is for everyone to keep their own copy of the ledger <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. Transactions are then broadcast globally <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

The core problem becomes: How can everyone agree on the correct ledger, ensuring that all participants are recording the same transactions in the same order, without a central authority <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>? This is the problem addressed in the original Bitcoin paper <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## Bitcoin's Solution: Proof of Work and Cryptographic Hash Functions

Bitcoin's high-level solution is to trust whichever ledger has the most computational work put into it <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. This is achieved using [[cryptographic_hash_functions_with_256_bit_security | cryptographic hash functions]] <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

### Cryptographic Hash Functions

A hash function takes any message or file as input and produces a fixed-length string of bits (e.g., 256 bits) as output, called the hash or digest <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Key properties:
*   **Deterministic but Random-Looking**: Always gives the same output for a given input, but the output appears random <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Sensitive to Input Changes**: Even a slight change in the input completely alters the resulting hash <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   **One-Way (Infeasible to Reverse)**: For a cryptographic hash function like SHA256, it's infeasible to find an input that produces a specific output without guessing and checking <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. The amount of computation needed to reverse a 256-bit hash is astronomical (2 to the power of 256) <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. While there's no [[role_of_rigor_in_mathematical_proofs | rigorous proof]] that it's hard to compute in reverse, modern security relies on this property <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

### Proof of Work

A "proof of work" demonstrates that significant computational effort has been expended <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. For example, if someone finds a "special number" that, when appended to a list of transactions, makes the SHA256 hash of the entire thing start with 30 zeros, it's highly probable they went through about a billion guesses (1 in 2^30 chance) <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Once found, this proof is quick to verify <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. Crucially, altering any part of the original data invalidates the proof, requiring new extensive computation <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

## Building the Blockchain

The distributed ledger is organized into "blocks" <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Each block contains:
1.  A list of transactions <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
2.  A proof of work (a special number causing the block's hash to start with a certain number of zeros) <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
3.  The hash of the previous block in its header, linking them together <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. This chaining means any alteration to a past block requires redoing all subsequent proofs of work <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This structure is why it's called a **blockchain** <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

### Bitcoin Mining and Block Creation

[[bitcoin_mining_and_block_creation | Block creators]], also known as "miners," listen for broadcasted transactions, collect them into a block, and perform "work" to find the special number for the proof of work <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. Once found, they broadcast the new block <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

Miners are incentivized by a "block reward," a special transaction at the top of the block where they create new "ledger dollars" out of thin air <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. This process is called "mining" because it requires significant work and introduces new currency into the economy <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. From a miner's perspective, each block is a lottery where they guess numbers rapidly until one finds the correct hash <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

## Decentralized Consensus and Security

The core protocol addition is: if you hear two distinct blockchains with conflicting transaction histories, you *defer to the longest one* – the one with the most work put into it <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. This mechanism allows for decentralized consensus without a central authority <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

> [!NOTE] Trusting a Payment
> You shouldn't immediately trust a new block <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. Instead, wait for several more blocks to be added on top of it. If no longer, conflicting chains appear, you can then be confident that the block is part of the chain everyone else is using <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>.

To fool someone with a fraudulent block, an attacker would need to consistently find proofs of work faster than all other miners combined to maintain a longer chain <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>. Unless they control close to 50% of the network's computing resources, the probability of the legitimate chain growing faster is overwhelming <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. This ensures the integrity of the system.

## Bitcoin Specifics and Transaction Fees

The Bitcoin protocol dynamically adjusts the difficulty of finding a proof of work (the number of leading zeros required in the hash) so that a new block is found, on average, every 10 minutes <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

All Bitcoin currency originates from block rewards <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. Initially, the reward was 50 Bitcoin per block. This reward is halved approximately every four years (or every 210,000 blocks) <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. Currently, the reward is 12.5 Bitcoin per block <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>. Due to this geometric decrease, there will never be more than 21 million Bitcoin in existence <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.

Miners also earn money from [[transaction_fees_and_scalability_issues_in_bitcoin | transaction fees]] <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>. Users can optionally include a fee with their payment, which goes to the miner who includes that transaction in a block <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>. This incentivizes miners to include transactions, especially given that each Bitcoin block is limited to about 2400 transactions <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. This block size limit contributes to higher transaction fees and slower processing compared to traditional payment systems like Visa <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>.