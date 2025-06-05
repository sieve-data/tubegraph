---
title: Implementing cryptographic concepts in blockchain development
videoId: qF7dkrce-mQ
---

From: [[fireship]] <br/> 

Blockchain technology, as exemplified by Bitcoin, fundamentally relies on [[cryptographic_proof_and_blockchain_technology | cryptographic proof]] to enable reliable, peer-to-peer transactions without the need for a central authority <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. This approach eliminates the weakness of trust in centralized financial systems, which often requires intervention by lawyers and government <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

The core purpose of software like blockchain is to arrange ones and zeros in a meaningful way <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The protocol that makes it meaningful is blockchain itself, which allows parties to engage in transactions denominated in cryptocurrencies like Bitcoin <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Foundational Cryptographic Concepts

Developers should understand various [[introduction_to_computer_science_concepts | concepts in cryptography]], such as [[implementing_security_rules_and_user_authentication | encryption]], [[implementing_security_rules_and_user_authentication | signing]], hashing functions, and algorithms like SHA, RSA, and MD5 <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. These concepts are essential for the [[security_measures_in_frontend_and_backend | security]] and integrity of blockchain systems <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Hashing Functions

A hashing function takes a value of an arbitrary size and maps it to a fixed-length value, typically a hexadecimal string <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. The output is called a hash or hash digest <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. A key property of a hash is that it cannot be reversed to reconstruct the original content <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. However, hashes can be used to validate if two values are identical by comparing their hashes <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This is crucial for a blockchain because it ensures that blocks can be linked without manipulation <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

*   **SHA-256**: Stands for Secure Hash Algorithm with a length of 256 bits <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Developed by the NSA in 2001, it is a one-way cryptographic function, meaning it can encrypt data but not decrypt it back to its original form <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. It is used in blockchain to create a hash of a block <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **MD5**: A hashing algorithm that is 128 bits long and faster to compute than SHA-256 <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### Public and Private Key Cryptography (RSA)

A wallet in a blockchain system is essentially a wrapper for a public key and a private key <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
*   The **public key** is used for receiving money <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. It's like a username <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   The **private key** is used for spending money <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. It's like a password <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

**RSA**, named after its creators, is a full [[implementing_security_rules_and_user_authentication | encryption]] algorithm that can encrypt data and decrypt it if the proper key is available <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. While RSA can encrypt and decrypt, its primary interest for blockchain is in creating digital signatures <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

#### Digital Signatures

Digital signatures are crucial for ensuring the authenticity and integrity of transactions <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
1.  Instead of encrypting the message, a hash of the message is created <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
2.  This hash is then signed with the sender's private key <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
3.  The message can then be verified later using the public key <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
If the message is changed, it would produce a different hash, causing the verification to fail <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This prevents tampering with transaction details like the amount or payee <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

### Mining and Proof of Work

To prevent issues like double-spending (where a user attempts to pay two different people at the same time) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, blockchain implements a [[mining_and_proof_of_work_in_bitcoin | proof of work]] system <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   This system allows multiple computers (nodes) worldwide to agree on the appropriate state of the entire system or ledger <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Each new block must undergo a process called [[mining_and_proof_of_work_in_bitcoin | mining]], which involves solving a difficult computational problem to confirm the block <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   The work is difficult to solve but very easy for other nodes to verify <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   The first miner to solve the proof (which occurs via luck) receives a portion of Bitcoin as a reward, incentivizing participation in the network <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   A **nonce** (number used once) is a one-time use random number added to a block <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. Miners will attempt to find a nonce that, when added to the block's data, produces a hash with a specific pattern (e.g., starting with four zeros) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. This requires brute-force computation <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

## Implementing a Blockchain with Node.js and TypeScript

A simplified blockchain can be built using Node.js and TypeScript, incorporating these cryptographic principles <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Node.js `crypto` Library

The built-in Node.js `crypto` library provides modular functionality for [[cryptographic_proof_and_blockchain_technology | cryptography]] <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Transaction Class

A `Transaction` object typically has properties for the amount, the sender, and the receiver <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. For cryptographic operations, the transaction object is often serialized to a string <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Block Class

A `Block` acts as a container for transactions, and in a simple implementation, it might hold a single transaction <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. Blocks are structured like a linked list, with each block containing a `previousHash` property that references the hash of the preceding block <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
The hash of a block is generated by stringifying the block's content and then applying a hashing algorithm like SHA-256 using `createHash` from `node:crypto` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. The hash is then returned as a hexadecimal string <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Each block also includes a timestamp to ensure chronological order <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

### Chain Class

The `Chain` class represents the blockchain itself, functioning as a linked list of blocks <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. It's often implemented as a singleton to ensure only one instance exists <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. The chain starts with a "genesis block" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

To add a block to the chain, a method like `addBlock` verifies the transaction's legitimacy <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. This verification involves:
1.  Creating a signature verification object using `node:crypto` <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
2.  Validating that the transaction data has not been tampered with, using the sender's public key and the provided digital signature <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

### Wallet Class

A `Wallet` class manages the generation and use of public and private keys <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. Key pairs are generated using the RSA algorithm, typically formatted as PEM strings that can be saved to a user's system <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

To send money, a user's wallet:
1.  Creates a transaction object with the amount and the recipient's public key <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
2.  Uses `node:crypto` to create a SHA-256 signature of the transaction data <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
3.  Signs the transaction hash with the sender's private key <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This signature serves as a one-time password to verify identity without exposing the private key <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

### Mining Implementation

A basic [[mining_and_proof_of_work_in_bitcoin | proof of work]] system can be implemented by adding a `nonce` value to the block class <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. A `mine` method iteratively computes hashes, incrementing the `nonce`, until it finds a hash that meets a specific criterion (e.g., starting with four zeros) <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. This brute-force process simulates the computational difficulty of [[mining_and_proof_of_work_in_bitcoin | mining]] <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. Once found, the solution is returned and can be verified by other nodes, allowing the block to be confirmed on the blockchain <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.