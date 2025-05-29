---
title: Understanding the basics of Bitcoin and cryptocurrency
videoId: bBC-nXj3Ng4
---

From: [[3blue1brown]] <br/> 

## What is Bitcoin?

Bitcoin is a fully digital currency that operates without government issuance or the need for banks to manage accounts and verify transactions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Its inventor remains unknown <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Bitcoin was the first implemented example of a cryptocurrency <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>, with thousands more now existing on exchanges alongside traditional currencies <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

While user-friendly applications allow individuals to send and receive cryptocurrencies without needing to understand the underlying mechanics <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>, the backbone of Bitcoin is a decentralized, trustless verification system based on [[role_of_cryptography_and_digital_signatures_in_bitcoin | cryptographic]] mathematics, rather than a bank <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## From Communal Ledger to Cryptocurrency

The concept of Bitcoin can be understood by imagining the invention of your own digital currency, starting with a simple communal ledger among friends <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This ledger would be a public website where anyone could add lines, such as "Alice pays Bob $20" <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. At the end of each month, participants would settle up based on recorded transactions <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Incorporating Digital Signatures

A key challenge with a public ledger is preventing unauthorized transactions, such as Bob adding "Alice pays Bob $100" without Alice's consent <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This is where [[role_of_cryptography_and_digital_signatures_in_bitcoin | digital signatures]] come into play <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

*   **Public Key-Private Key Pair**: Everyone generates a public key (PK) and a private key (SK) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The private key must be kept secret <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Signing a Transaction**: A [[role_of_cryptography_and_digital_signatures_in_bitcoin | digital signature]] is a string of bits (e.g., 256 bits) that is produced by a function dependent on both the message (transaction) and the sender's private key <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Any slight alteration to the message completely changes the signature <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This ensures only the private key holder can create the signature and prevents copying signatures to new messages <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Verifying a Signature**: A separate verification function, using the public key, can determine if a signature is valid for a given message <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. It is infeasible to find a valid signature without knowing the secret key <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. The number of possible 256-bit signatures (2^256) is astronomically large, making guessing practically impossible <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Preventing Double Spending**: To prevent copying and re-using past valid transactions (e.g., Bob repeatedly copying "Alice pays Bob $100") <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>, each transaction signed must include a unique ID <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Ledger Dollars: Detaching from Physical Currency

To avoid having to settle up in cash, the system can evolve to prevent individuals from spending more than they have on the ledger <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. This requires verifying a transaction against the full history of transactions up to that point <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

This step removes the direct connection between the ledger and physical US dollars, turning the quantities on the ledger into "ledger dollars" (LD) <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. People can exchange LD for real US dollars, but such exchanges are not guaranteed by the protocol <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

The fundamental nature of Bitcoin, or any other cryptocurrency, is that it *is* a ledger, and the history of transactions *is* the currency <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## Decentralized Consensus: The Blockchain and Proof of Work

The ledger system, if centrally hosted, would still require trust in a single entity <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. To remove this trust, everyone keeps their own copy of the ledger <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. When a transaction is made, it's broadcast for everyone to record on their ledgers <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. The challenge then becomes how to ensure everyone agrees on the same ledger and transaction order <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

Bitcoin's solution is to trust whichever ledger has the most computational [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | work]] put into it <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. This is achieved using [[role_of_cryptography_and_digital_signatures_in_bitcoin | cryptographic hash functions]] like SHA256 <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

### Cryptographic Hash Functions

*   **Functionality**: A hash function takes any message or file as input and produces a fixed-length string of bits (e.g., 256 bits) called a hash or digest <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Properties**:
    *   The output appears random <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
    *   Slight changes to the input completely change the resulting hash <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
    *   For a *cryptographic* hash function, it is infeasible to compute in reverse; finding an input that produces a specific hash output requires guessing and checking <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

### Proof of Work

A [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | proof of work]] demonstrates that a significant amount of computational effort has been expended <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. For example, finding a "special number" that, when added to a list of transactions and hashed with SHA256, results in a hash starting with 30 zeros <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Since the probability of this occurring randomly is about 1 in a billion (2^30) <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>, finding such a number implies approximately a billion guesses and checks <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. This work is quick to verify, but difficult to produce <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

Crucially, this [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | work]] is tied to the list of transactions; altering any transaction invalidates the hash and requires redoing the entire [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | proof of work]] <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

### The Blockchain

The ledger is organized into "blocks," where each block contains a list of transactions and a [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | proof of work]] <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. To maintain a standard order, each block's header must include the hash of the previous block <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. This chaining mechanism means that changing any block or its order would invalidate all subsequent blocks, requiring immense computational effort to re-calculate all proofs of work <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This structure is why it's called a [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | blockchain]] <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

### Bitcoin Mining

Anyone can be a [[bitcoin_mining_and_block_creation | block creator]] (miner) <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. Miners listen for broadcast transactions, collect them into a block, and then perform the [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | proof of work]] to find the special number that makes the block's hash start with many zeros <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. Once found, they broadcast the valid block <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

*   **Block Reward**: To incentivize [[bitcoin_mining_and_block_creation | block creation]], miners are allowed to include a special transaction in their block that grants them new ledger dollars "out of thin air" <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. This "block reward" increases the total money supply with each new block <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   **Mining as a Lottery**: [[bitcoin_mining_and_block_creation | Mining]] is like a lottery where miners guess numbers as fast as possible until one finds a valid hash, earning the reward <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

### Decentralized Consensus through Longest Chain

The core rule for all participants is: if you hear two conflicting [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | blockchains]], you defer to the longest one – the one with the most [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | work]] put into it <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. This protocol allows for decentralized consensus without a central authority <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

To deceive someone with a fraudulent block, an attacker would need to consistently out-compete all other miners on the network in finding new blocks to maintain a longer fraudulent chain <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. Unless an attacker controls nearly 50% of the network's computing resources, the legitimate [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | blockchain]] will almost certainly grow faster <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. Therefore, payments aren't fully trusted until several new blocks have been added on top of the block containing the payment, confirming its inclusion in the longest chain <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>.

## Key Aspects of the Bitcoin Protocol

*   **Target Block Time**: The Bitcoin protocol periodically adjusts the difficulty of the [[blockchain_and_proof_of_work_in_the_Bitcoin_protocol | proof of work]] (e.g., the number of leading zeros required in the hash) to ensure that a new [[bitcoin_mining_and_block_creation | block]] is found, on average, every 10 minutes <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
*   **Block Reward Halving**: Initially, [[bitcoin_mining_and_block_creation | block rewards]] were 50 Bitcoin per block <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. This reward is cut in half every 210,000 blocks (approximately every 4 years) <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. As of the transcript's recording, it was 12.5 Bitcoin per block <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
*   **Limited Supply**: Due to the geometrically decreasing block reward, the total number of Bitcoin will never exceed 21 million <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **[[transaction_fees_and_scalability_issues_in_bitcoin | Transaction Fees]]**: Miners also earn money from [[transaction_fees_and_scalability_issues_in_bitcoin | transaction fees]] <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>. Senders can optionally include a fee with their payment, which incentivizes miners to include that transaction in the next block <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.
*   **[[transaction_fees_and_scalability_issues_in_bitcoin | Scalability Issues]]**: Bitcoin blocks are limited to about 2400 transactions <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. This limit contributes to higher [[transaction_fees_and_scalability_issues_in_bitcoin | transaction fees]] because miners prioritize transactions with higher fees <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>. For comparison, Visa processes an average of about 1700 transactions per second, with a capacity of over 24,000 per second <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>.