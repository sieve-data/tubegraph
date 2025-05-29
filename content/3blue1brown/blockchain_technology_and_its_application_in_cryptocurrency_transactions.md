---
title: Blockchain technology and its application in cryptocurrency transactions
videoId: bBC-nXj3Ng4
---

From: [[3blue1brown]] <br/> 

## What is a Cryptocurrency?
Many people have heard of [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]], a fully digital currency not issued by any government, managed by banks, or with a known inventor <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]] was the first implemented example of a [[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies | cryptocurrency]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>, and there are now thousands more <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Understanding the underlying technical details helps to grasp its nature <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

At its core, a [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]] or any other [[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies | cryptocurrency]] is fundamentally a ledger <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. The history of transactions recorded on this ledger *is* the currency <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

## From Communal Ledgers to Digital Currencies

### The Communal Ledger
Initially, one might imagine keeping track of payments among friends using a communal ledger, accessible publicly like a website where anyone could add new lines <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. At the end of a period, participants would settle up based on the recorded transactions <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Incorporating Digital Signatures
A key problem with a public ledger is preventing unauthorized additions, such as someone falsely recording a payment from another person <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This is where [[Digital signatures and cryptography | digital signatures]] come in <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

*   **Purpose:** To prove that a transaction was seen and approved by the sender, making forgery infeasible <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Mechanism:** Everyone generates a public key-private key pair <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The private (or secret) key (SK) is kept secret, while the public key (PK) is shared <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Signature Properties:**
    *   A digital signature is a string of bits, commonly [[256_bit_security_concept | 256 bits]] <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   It changes for different messages; even a slight alteration to the message completely changes the signature <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
    *   Producing a signature involves a function depending on both the message and your private key, ensuring only you can produce it <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   A separate function uses the public key to verify if a signature is valid for a given message <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Security:** It is computationally infeasible to find a valid signature without knowing the secret key <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. With [[256_bit_security_concept | 256-bit]] signatures, the number of possibilities (2^256) is astronomically large, making guessing and checking impractical <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Preventing Duplication:** To prevent someone from copying a valid message-signature combination multiple times, messages must include a unique ID associated with that transaction <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Introducing "Ledger Dollars"
The next step is to remove the need for cash settlement <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. By initially assigning everyone an amount (e.g., $100 Ledger Dollars, or LD) and only accepting transactions where someone spends no more than they have on the ledger, the system can function independently of physical currency <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. This means verifying a transaction requires knowing the full history of transactions up to that point <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

## Decentralized Consensus: The Heart of Blockchain

### The Problem of Distributed Ledgers
If everyone keeps their own copy of the ledger and transactions are broadcast, how can everyone agree on what the *right* ledger is, especially regarding the order and validity of transactions <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>? This is a core problem addressed by [[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies | Bitcoin]] <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

### Proof of Work as a Solution
[[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies | Bitcoin]]'s solution is to trust the ledger that has the most computational work put into it <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. This makes fraudulent transactions and conflicting ledgers computationally infeasible to maintain <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

#### Cryptographic Hash Functions
A crucial component is the [[Hash functions and SHA256 | cryptographic hash function]], like [[Hash functions and SHA256 | SHA256]] <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   **Inputs and Outputs:** Takes any message or file as input and produces a fixed-length string of bits (e.g., [[256_bit_security_concept | 256 bits]]) called a hash or digest <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Sensitivity:** Even a slight change in the input completely alters the resulting hash in an unpredictable way <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   **One-Way Property:** It is infeasible to compute the input from a given output; the only known method is guessing and checking <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. This property underpins modern security <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

#### What is [[Mining and the proof of work concept in the bitcoin protocol | Proof of Work]]?
A [[Mining and the proof of work concept in the bitcoin protocol | proof of work]] demonstrates that a significant amount of computational effort has been expended <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. For example, finding a "special number" which, when appended to a list of transactions, makes the [[Hash functions and SHA256 | SHA256]] hash of the entire thing start with a certain number of zeros (e.g., 30 zeros). This would require about 2^30 (1 billion) guesses <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. This work is intrinsically tied to the list of transactions; altering them would require redoing all the work <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

### The Blockchain Structure
The ledger is organized into "blocks" <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.
*   **Block Composition:** Each block consists of a list of transactions and a [[Mining and the proof of work concept in the bitcoin protocol | proof of work]] (a special number causing the hash to start with many zeros) <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
*   **Chaining:** To maintain order, each block's header contains the hash of the *previous* block <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. This means changing any block or its order would necessitate redoing all the work for subsequent blocks <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This chained structure is why it's called a blockchain <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

### Block Creators (Miners)
Anyone can be a "block creator" or "miner" <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
*   **Role:** Miners listen for broadcast transactions, collect them into a block, and then perform the [[Mining and the proof of work concept in the bitcoin protocol | proof of work]] by finding the special number <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. Once found, they broadcast the new block <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   **Block Reward:** To incentivize this work, a miner can include a special transaction in their block, creating new "ledger dollars" (e.g., 10 LD) for themselves <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. This "block reward" is how new currency enters the economy <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   **Mining Analogy:** Mining is likened to a miniature lottery where individuals guess numbers rapidly until one finds the correct hash, earning the reward <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

### Achieving Decentralized Consensus
For users, the protocol dictates that if two distinct blockchains with conflicting histories are heard, preference is given to the *longest one* – the one with the most work put into it <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. If tied, one waits for an additional block to extend one chain <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. This mechanism allows for decentralized consensus without a central authority <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

#### Trust and Security
*   **Fraud Prevention:** To maintain a fraudulent chain, an attacker would need to consistently find blocks faster than all other miners combined <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. Unless an attacker controls nearly 50% of the network's computing resources, the legitimate chain will almost certainly grow faster <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
*   **Confirmation:** Due to this, a new block should not be immediately trusted. Instead, one should wait for several new blocks to be added on top of it, confirming its place in the longest chain <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>.

## Bitcoin Specifics

### Dynamic Difficulty
The [[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies | Bitcoin]] protocol periodically adjusts the difficulty (number of leading zeros required for the hash) to ensure that, on average, a new block is found every 10 minutes <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

### Money Supply and Transaction Fees
*   **Block Reward Halving:** [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]] block rewards, initially 50 [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]] per block, are cut in half approximately every four years (every 210,000 blocks) <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. Currently, the reward is 12.5 [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]] per block <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
*   **Limited Supply:** Due to this geometric decrease, the total number of [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]] in existence will never exceed 21 million <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **Transaction Fees:** Miners also earn money through transaction fees <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>. Users can optionally include a fee with their payment, which goes to the miner who includes that payment in their block <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>. This incentivizes miners, especially since [[what_bitcoin_is_and_how_it_functions_as_a_digital_currency | Bitcoin]] blocks have a limited capacity (around 2400 transactions) <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. This limited capacity can lead to higher transaction fees <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>.