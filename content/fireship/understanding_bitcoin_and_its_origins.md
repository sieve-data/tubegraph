---
title: Understanding Bitcoin and its origins
videoId: qF7dkrce-mQ
---

From: [[fireship]] <br/> 

Bitcoin is described as a peer-to-peer electronic cash system <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It was first detailed in a 2008 white paper authored by the pseudonymous Satoshi Nakamoto <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Why Bitcoin? Challenging Centralized Trust
The traditional financial system relies on trust in large, centralized banks to manage fiat currencies and process transactions <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. However, this reliance on trust can become a weakness, sometimes necessitating intervention from lawyers and governments <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

Bitcoin offers an alternative, enabling two parties to conduct reliable transactions based on [[cryptographic_proof_and_blockchain_technology | cryptographic proof]], thereby removing the need for a trusted middleman <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While some view it as "digital gold" and others as "fool's gold," Bitcoin is fundamentally software designed to meaningfully arrange ones and zeros <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## The Blockchain Protocol
The underlying protocol that gives Bitcoin meaning is blockchain <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This technology facilitates transactions denominated in bitcoins or satoshis, which hold value because users believe they do <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Blockchain as a Public Ledger
From a financial perspective, the blockchain operates as a shared, public ledger that records all transactions from all Bitcoin users <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This ledger is distributed and synchronized globally, eliminating the need for a central authority to maintain and validate it <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### Blockchain as a Database
Technically, the blockchain can be conceptualized as a database structured like a linked list <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Each record, or "block," represents a group of transactions that have been permanently committed to the database <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. It functions similarly to a [[introduction_to_git_and_github | Git]] repository that can never be rebased <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Each new block is cryptographically linked to the previous one in the chain, adhering to a strict set of rules for its creation <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

The very first block in a blockchain is known as the "genesis block" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. For the genesis block, there is no previous hash to link to, and it might instantiate an initial transaction, such as transferring 100 coins to Satoshi <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## Bitcoin Transactions and Wallets
In Bitcoin, users interact through "wallets," which are essentially wrappers for a public key and a private key <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

*   **Public Key**: Acts like a username and is used for receiving money <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Private Key**: Acts like a password and is used for spending money <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

To spend money, a user must prove ownership of a public key that has previously received funds <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Transaction Structure
Each transaction includes:
*   A hash (encrypted representation) of the previous transaction <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   The new owner's public key <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   The transaction hash is signed with the previous owner's private key <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This process validates the chain of ownership without revealing the private key and makes it virtually impossible to alter the transaction after it's issued <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## [[implementing_cryptographic_concepts_in_blockchain_development | Cryptographic Concepts]] in Bitcoin

### Hashing Functions
A hashing function takes an arbitrary-sized value (like a transaction) and maps it to a fixed-length value, often a hexadecimal string, called a hash or hash digest <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. Hashes are one-way; they cannot be reversed to reconstruct the original content <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. However, they are used to validate that two values are identical by comparing their hashes <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>, which is crucial for linking blockchain blocks without manipulation <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

*   **SHA-256 (Secure Hash Algorithm 256-bit)**: Developed by the NSA in 2001, it's a one-way cryptographic function used to hash transaction data <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **MD5 (Message-Digest Algorithm 5)**: A faster, 128-bit hashing algorithm, sometimes used in proof-of-work examples <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

### Digital Signatures with RSA
To generate public and private keys, Bitcoin uses algorithms like RSA (Rivest–Shamir–Adleman) <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. Unlike SHA, RSA is a full encryption algorithm that can encrypt and decrypt data with the appropriate key <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

Digital signatures are crucial:
1.  A hash of the message (transaction data) is created <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
2.  This hash is then signed with the sender's private key <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
3.  The message can later be verified using the public key <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
If the message is altered, the verification will fail, preventing interception and modification of transaction details like amount or payee <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This is like creating a one-time password to verify identity without exposing the private key <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

## [[mining_and_proof_of_work_in_bitcoin | Mining and Proof of Work]]
A significant challenge in digital cash systems is the "double-spend issue," where a user might try to pay two different people with the same Bitcoin simultaneously <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Bitcoin addresses this with a [[mining_and_proof_of_work_in_bitcoin | proof-of-work system]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### How Mining Works
Mining is a system that enables multiple computers globally to agree on the appropriate state of the entire system or ledger <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

1.  New transactions are broadcast to all nodes (computers) in the network <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  These transactions are then packaged into a block <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
3.  Miners expend computing power to validate a "proof of work" <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. They solve a random computational problem that is very difficult to find but very easy to verify <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
4.  The first miner to solve this proof (often by dumb luck) receives a portion of Bitcoin as a reward <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
5.  This newly confirmed block is then broadcast back to all other nodes, where it is permanently added to the blockchain <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

The proof-of-work system requires each new block to go through a computationally difficult process to confirm it, which is easy for other nodes to verify <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. When mining is distributed worldwide, multiple nodes compete in a "lottery" to confirm a block <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. The winner earns a portion of the coin, incentivizing investment in computing resources and driving the coin's price <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This process can be thought of as converting cloud computing resources into money <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

To implement a basic proof of work system, a `nonce` (a one-time use random number) value is added to the block <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Miners then attempt to find a number that, when combined with the `nonce`, produces a hash starting with a specific pattern (e.g., four zeros) <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. This is typically achieved through brute force by repeatedly hashing values until the desired pattern is found <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. Once found, the solution is broadcast and verified, and the block is confirmed <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.