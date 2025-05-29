---
title: What bitcoin is and how it functions as a digital currency
videoId: bBC-nXj3Ng4
---

From: [[3blue1brown]] <br/> 

## Introduction to Bitcoin

Bitcoin is a fully digital currency that operates without a governing authority or the need for banks to manage accounts and verify transactions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Its inventor remains unknown <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Bitcoin was the first implemented example of a [[blockchain_technology_and_its_application_in_cryptocurrency_transactions | cryptocurrency]], and since its inception, thousands more have emerged, available on exchanges alongside traditional currencies <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

Understanding Bitcoin involves comprehending the actual processes computers perform when these currencies are sent, received, and created <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. While end-users don't need to know these intricate details to use Bitcoin, just as one doesn't need to understand credit card processing to swipe a card <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, grasping the underlying technology is crucial for those involved in the cryptocurrency space <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. The core difference from traditional digital payments is that its backbone is a clever system of [[the_principles_of_decentralized_trustless_verification_in_cryptocurrencies | decentralized trustless verification]] based on cryptography, rather than a bank <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## From Communal Ledgers to Digital Currencies

The concept of Bitcoin can be understood by imagining the evolution of a simple communal ledger used by friends to track payments <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This ledger, initially public and accessible for anyone to add lines to, would be settled periodically with cash <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Incorporating Digital Signatures

A key challenge with a public ledger is preventing unauthorized entries, such as someone adding a transaction claiming they were paid without approval <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This is where [[digital_signatures_and_cryptography | digital signatures]] come into play <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

*   **Public Key-Private Key Pair**: Each participant generates a public key (PK) and a private key (SK), both strings of bits <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The private key must be kept secret <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Signature Generation**: A digital signature is a string of 1s and 0s (commonly 256 bits) that is produced by a function dependent on both the message (transaction) and the sender's private key <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Even a slight alteration to the message completely changes the resulting signature <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This prevents anyone from copying a signature and forging it on a different message <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Signature Verification**: A second function, using the public key, verifies if a signature is valid for a given message, outputting true or false <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. It is computationally infeasible to find a valid signature without knowing the secret key, making forgery practically impossible <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. The number of possible 256-bit signatures is astronomically large (2^256), making random guessing futile <a class="yt-timestamp" data-t="00:05:58">[00:06:03]</a>.
*   **Unique Transaction IDs**: To prevent copying a valid message-signature combination multiple times, each transaction message must include a unique ID <a class="yt-timestamp" data-t="00:06:42">[00:07:01]</a>.

### From Cash Settlement to Ledger Dollars

The next step in removing trust is to eliminate the need for cash settlement. This is achieved by:
*   **Initial Pot**: Everyone contributes initial funds to the ledger, establishing a starting balance for each participant <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Balance Validation**: The protocol only accepts transactions where a sender has sufficient funds on the ledger <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. This requires knowing the full history of transactions <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   **Decoupling from Fiat**: This system removes the direct connection to physical currency. The quantities on the ledger become "ledger dollars" (LD), an independent digital currency <a class="yt-timestamp" data-t="00:08:51">[00:09:10]</a>. This is a fundamental aspect of Bitcoin: the history of transactions *is* the currency <a class="yt-timestamp" data-t="00:09:44">[00:09:53]</a>.

## Decentralized Verification and the Blockchain

Moving the ledger from a central website to a distributed system where everyone keeps their own copy introduces a new challenge: how to achieve consensus on the "correct" ledger when transactions are broadcast <a class="yt-timestamp" data-t="00:10:13">[00:10:19]</a>. The solution presented in the original Bitcoin paper is to trust the ledger that has the most computational work put into it <a class="yt-timestamp" data-t="00:11:38">[00:11:44]</a>.

### Cryptographic Hash Functions and Proof of Work

[[the_role_of_ledgers_digital_signatures_and_hash_functions_in_bitcoin | Cryptographic hash functions]], like SHA256, are central to this process <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Functionality**: A hash function takes any message or file as input and produces a fixed-length string of bits (e.g., 256 bits) called a hash or digest <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. The output appears random, and even a slight change in the input completely alters the hash <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **One-Way Property**: Cryptographic hash functions are "one-way"; it's infeasible to compute the input from a given hash output without guessing and checking <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
*   **Proof of Work**: This property allows for a "proof of work" <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. If someone finds a specific number that, when added to a list of transactions, results in a hash starting with a certain number of zeros (e.g., 30 zeros), it proves they undertook significant computational effort <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. This is because finding such a number requires, on average, a large number of guesses (e.g., 2^30 or 1 billion guesses for 30 zeros) <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. Once found, this proof of work is quick to verify <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. Any change to the transactions would invalidate the existing proof of work, requiring new computational effort <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

### The Blockchain Structure

To apply this, the ledger is organized into "blocks." Each block contains a list of transactions and its own [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | proof of work]] (a special number causing the block's hash to start with many zeros) <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. Blocks are chained together by including the hash of the previous block in the header of the current block <a class="yt-timestamp" data-t="00:16:50">[00:16:54]</a>. This chaining means that altering any past block would invalidate all subsequent blocks, requiring immense re-computation <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This structure is why it's called a [[blockchain_technology_and_its_application_in_cryptocurrency_transactions | blockchain]] <a class="yt-timestamp" data-t="00:17:22">[00:17:24]</a>.

### Mining and Block Rewards

"Block creators" (also known as [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | miners]]) listen for broadcast transactions, collect them into a block, and then perform the computationally intensive work of finding the special number (the proof of work) <a class="yt-timestamp" data-t="00:17:32">[00:17:35]</a>. Once found, they broadcast their completed block <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

To incentivize this work, miners are allowed to include a special transaction in their block, creating new "ledger dollars" out of thin air as a "block reward" <a class="yt-timestamp" data-t="00:17:50">[00:17:55]</a>. This process, known as [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | mining]], introduces new currency into the economy <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. For miners, finding a block is like winning a miniature lottery, where the fastest to find the correct number wins the reward <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

### Decentralized Consensus

Users of the system listen for broadcast blocks and update their own copies of the blockchain <a class="yt-timestamp" data-t="00:18:57">[00:19:01]</a>. The core protocol rule for achieving decentralized consensus is: if there are two distinct blockchains with conflicting transaction histories, trust the longest one—the one with the most work put into it <a class="yt-timestamp" data-t="00:19:10">[00:19:14]</a>.

To prevent fraud, such as Alice attempting to send Bob a fraudulent block without broadcasting it to the rest of the network, she would need to continue finding proofs of work faster than all other miners combined <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. Unless a fraudulent party controls nearly 50% of the total computing resources of all miners, the legitimate blockchain will almost certainly grow faster <a class="yt-timestamp" data-t="00:20:49">[00:21:03]</a>. Therefore, to truly trust a transaction, one should wait for several new blocks to be added on top of it, ensuring it's part of the widely accepted, longest chain <a class="yt-timestamp" data-t="00:21:23">[00:21:29]</a>.

## Bitcoin's Economic Design

Several specific details define Bitcoin's operation:
*   **Difficulty Adjustment**: The Bitcoin protocol periodically adjusts the difficulty of finding a proof of work (i.e., the required number of leading zeros in the hash) to ensure that, on average, a new block is found approximately every 10 minutes <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
*   **Block Reward Halving**: Initially, block rewards were 50 Bitcoin per block <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. This reward is halved approximately every four years (every 210,000 blocks) <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. Currently, the reward is 12.5 Bitcoin per block <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
*   **Supply Cap**: Due to this geometrical decrease in block rewards, the total number of Bitcoin will never exceed 21 million <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **Transaction Fees**: In addition to block rewards, miners earn money through optional transaction fees included by users <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>. These fees incentivize miners to include a user's transaction in the next block, especially since Bitcoin blocks have a limited capacity (around 2400 transactions) <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. This limited capacity can lead to higher transaction fees and slower processing compared to systems like Visa <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>.

This distributed ledger system, built on [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | proof of work]], forms the fundamental mechanism for Bitcoin and many other cryptocurrencies <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>.