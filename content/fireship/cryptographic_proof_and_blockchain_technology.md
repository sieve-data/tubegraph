---
title: Cryptographic proof and blockchain technology
videoId: qF7dkrce-mQ
---

From: [[fireship]] <br/> 

[[Understanding Bitcoin and its origins | Bitcoin]], a peer-to-peer electronic cash system, was first described in a 2008 white paper authored by the mysterious Satoshi Nakamoto <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Unlike the modern financial system that relies on trust in centralized banks <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, [[Understanding Bitcoin and its origins | Bitcoin]] enables reliable transactions between two parties based on cryptographic proof, eliminating the need for a trustee middleman <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Its underlying protocol, [[Building a blockchain with Nodejs and TypeScript | blockchain]], allows parties to engage in transactions denominated in bitcoins or satoshis <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Understanding the Blockchain

From a financial perspective, the [[Building a blockchain with Nodejs and TypeScript | blockchain]] acts as a shared public ledger containing all transactions from all [[Understanding Bitcoin and its origins | Bitcoin]] users <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This ledger is distributed and synchronized globally, removing the need for a central authority to maintain and validate it <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

Technically, the [[Building a blockchain with Nodejs and TypeScript | blockchain]] is a database structured as a linked list <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Each record, or "block," represents a group of transactions that have been permanently committed to the database <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. It functions similarly to a Git repository that can never be rebased <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. A critical aspect is that each new block is cryptographically linked to the previous one in the chain, following a strict set of rules <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Cryptographic Principles

The [[Building a blockchain with Nodejs and TypeScript | blockchain]] relies heavily on cryptographic concepts to ensure security and integrity. Developers should be familiar with encryption, signing, hashing functions, and algorithms like SHA, RSA, and MD5 <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Wallets and Keys

Each user or "wallet" has a unique public key for receiving money (like a username) and a unique private key for spending money (like a password) <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. To spend money, a user must prove they own the public key to which funds were previously sent <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Hashing Functions

A hashing function takes a value of arbitrary size, like a transaction, and maps it to a fixed-length value, often a hexadecimal string, called a hash or hash digest <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. Hashes are one-way cryptographic functions, meaning they cannot be reversed to reconstruct the original content <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. However, they are crucial for validating that two values are identical by comparing their hashes <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This ensures that blocks can be linked without being manipulated <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

Algorithms like SHA-256 (Secure Hash Algorithm with 256 bits) are used to hash block data <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. MD5, a faster but less secure algorithm with 128 bits, can also be used <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

### Digital Signatures with RSA

RSA is a full encryption algorithm capable of both encrypting and decrypting data with the appropriate key <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. In the context of [[Implementing cryptographic concepts in blockchain development | blockchain]], it's used to create digital signatures <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

To create a digital signature:
1.  A hash of the message (e.g., transaction data) is generated <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
2.  This hash is then signed with the sender's private key <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
3.  The message can later be verified using the sender's public key <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

If the message is altered, it produces a different hash, causing the verification to fail <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. This prevents interception and tampering with transaction details like amount or payee <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

## [[Mining and proof of work in Bitcoin | Mining and Proof of Work]]

One major challenge in digital currency is the "double spend" issue, where a user attempts to spend the same funds multiple times simultaneously <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. [[Understanding Bitcoin and its origins | Bitcoin]] addresses this with a [[Mining and proof of work in Bitcoin | proof of work]] system <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

[[Mining and proof of work in Bitcoin | Mining]] involves solving a difficult computational problem to confirm each new block <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. While solving it is difficult, verifying the solution by other nodes in the system is very easy <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This process is distributed globally, with multiple nodes competing to confirm blocks in a lottery-like system <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. The first miner to solve the proof (often via "dumb luck") receives a portion of [[Understanding Bitcoin and its origins | Bitcoin]] as a reward <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>, incentivizing investment in computing resources <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Once confirmed, the block is broadcast and permanently added to the [[Building a blockchain with Nodejs and TypeScript | blockchain]] <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

A simple [[Mining and proof of work in Bitcoin | proof of work]] system involves finding a "nonce" (a one-time use random number) that, when combined with other block data, produces a hash with a specific prefix (e.g., four leading zeros) <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. This is typically found through brute force computation via a while loop <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

## [[Building a blockchain with Nodejs and TypeScript | Building a Blockchain from Scratch]]

To implement a basic [[Building a blockchain with Nodejs and TypeScript | blockchain]], developers can use Node.js and TypeScript <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. The `crypto` library in Node.js provides modular functionality for cryptography <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

A simple [[Building a blockchain with Nodejs and TypeScript | blockchain]] implementation typically involves four core classes:
*   **Transaction**: Defines the transfer of funds, including amount, sender's public key, and recipient's public key <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Block**: A container for one or more transactions, including a reference (hash) to the previous block, and a timestamp <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   **Chain**: A linked list of blocks, starting with a "genesis block" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. It should be a singleton instance to ensure only one [[Building a blockchain with Nodejs and TypeScript | blockchain]] exists <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. The `addBlock` method verifies transactions using signatures before adding them <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Wallet**: A wrapper for a public key and a private key, used for sending and receiving funds <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

This practical approach helps in understanding how cryptographic concepts apply to different areas of development beyond just cryptocurrency <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.