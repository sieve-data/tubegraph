---
title: Building a blockchain with Nodejs and TypeScript
videoId: qF7dkrce-mQ
---

From: [[fireship]] <br/> 

This article explores the fundamental concepts behind blockchain technology by demonstrating how to build a simplified blockchain from scratch using [[introduction_to_nodejs | Node.js]] and [[getting_started_with_typescript_and_its_installation | TypeScript]]. It covers core components like transactions, blocks, the chain itself, wallets, and the role of cryptography in securing these systems.

## What is a Blockchain?

A blockchain is the underlying protocol that makes cryptocurrencies like Bitcoin meaningful <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. From a financial perspective, it functions as a shared, public ledger that contains all transactions from all users, distributed and synchronized globally <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This decentralized nature eliminates the need for a central authority to maintain and validate transactions <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

Technically, a blockchain can be thought of as a database structured like a linked list, where each record (or block) represents a group of transactions permanently committed to the database <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. It operates similar to a Git repository that can never be rebased <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Each new block is cryptographically linked to the previous one and its creation follows strict rules <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Development Environment Setup

To begin building a blockchain, you will need [[introduction_to_nodejs | Node.js]] installed on your system <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. The project uses [[getting_started_with_typescript_and_its_installation | TypeScript]] due to its benefits for [[object_oriented_programming_with_typescript | Object Oriented Programming with TypeScript]] and improved code readability <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

### Initializing the Project
1.  Open VS Code in an empty directory <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
2.  Run `npm init -y` to create a new [[nodejs_runtime_and_basic_operations | Node.js]] project <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
3.  Install [[getting_started_with_typescript_and_its_installation | TypeScript]] using `npm install typescript` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  Create a `tsconfig.json` file and configure it <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
5.  Add a `dev` script in `package.json` to run the [[getting_started_with_typescript_and_its_installation | TypeScript]] compiler with the `--watch` flag, allowing it to constantly compile code into plain JavaScript in the background <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
6.  Run `npm run dev` from the command line <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
7.  All source code will be written in an `index.ts` file <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
8.  Import the `crypto` library, a built-in [[nodejs_runtime_and_basic_operations | Node.js]] module for cryptography functionality <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Core Blockchain Classes

A simple blockchain implementation typically consists of four main classes: `Transaction`, `Block`, `Chain`, and `Wallet` <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. The project uses [[object_oriented_programming_with_typescript | Object Oriented Programming with TypeScript]] principles and [[classes_and_inheritance_in_typescript | Classes and Inheritance in TypeScript]] for their implementation.

### Transaction Class
The fundamental purpose of any cryptocurrency is to transfer funds from one user to another <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   A `Transaction` object has three properties: `amount`, `payer`, and `payee` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   The `payer` and `payee` will eventually be set as public keys <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   A method is added to convert the transaction object to a string for cryptographic operations <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Block Class
A `Block` acts as a container for transactions, or a single transaction for simplicity <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   Blocks are like elements in a linked list, each referencing or linking to the previous block via a `prevHash` property <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   Each block also contains a timestamp, ensuring chronological order <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

#### Hashing Functions
A hashing function takes a value of arbitrary size (like a transaction) and maps it to a fixed-length value, often a hexadecimal string, called a hash or hash digest <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   Hashes cannot be reversed to reconstruct the original content <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   They are used to validate if two values are identical by comparing their hashes, ensuring blocks are linked without manipulation <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   The `createHash` function from `node:crypto` is used, specifying a hashing algorithm like SHA-256 <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

> [!NOTE] SHA-256 (Secure Hash Algorithm with a length of 256 bits) was developed by the NSA in 2001 <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. It's a one-way cryptographic function, meaning it can encrypt data but not decrypt it back to its original form <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Chain Class
The `Chain` class represents the blockchain itself, functioning as a linked list of blocks <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   It is implemented as a singleton instance to ensure only one blockchain exists <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   The chain is an array of `Block` objects <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   The constructor defines the first block, called the `genesis block`, which has a null `prevHash` and typically instantiates an initial transaction <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   A getter is created to easily retrieve the last block in the chain <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   The `addBlock` method takes a `Transaction`, the sender's `publicKey`, and a `signature` to verify the transaction before adding it <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### Wallet Class
A `Wallet` is a wrapper for a public key and a private key <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   The public key is for receiving money, while the private key is for spending money <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

#### RSA Algorithm and Digital Signatures
To generate public and private keys, the RSA algorithm is used <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   Unlike SHA, RSA is a full encryption algorithm that can encrypt data with a public key and decrypt it with a private key <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   More importantly for transactions, RSA is used to create a digital signature <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
    *   To sign, a hash of the message (transaction data) is created, then signed with the private key <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
    *   The message can then be verified later using the public key <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
    *   If the message is altered, it produces a different hash, causing verification to fail <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. This prevents tampering with transaction amounts or payees <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   Node's `crypto` module is used to generate key pairs, formatted as PEM strings for potential future reuse <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   To send money, a `sendMoney` method specifies an amount and the recipient's public key <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   A signature is created using SHA-256 format on the transaction data, then signed with the private key <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This allows identity verification without exposing the private key <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   The `addBlock` method in the `Chain` class uses `node:crypto` to verify the signature, ensuring the transaction data has not been tampered with using the sender's public key and signature <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## Proof of Work (Mining)

To address the "double-spend" issue (where a spender tries to send money to two different users simultaneously), Bitcoin uses a Proof of Work system <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   Proof of Work requires each new block to go through a process called "mining," where a difficult computational problem is solved to confirm the block <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   The work is difficult to solve but very easy for other nodes to verify <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   Mining is distributed globally, with multiple nodes competing in a "lottery" <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   The winner earns a portion of the coin as an incentive, motivating investment in computing resources <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

### Implementing Basic Proof of Work
*   In the `Block` class, a `nonce` value (a one-time use random number) is added <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   A `mine` method in the `Chain` class attempts to find a number that, when added to the `nonce`, produces a hash starting with a specific pattern (e.g., four zeros) <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
*   This value is found via brute force using a `while` loop that continuously creates hashes with the MD5 algorithm until the desired pattern is found <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

> [!NOTE] MD5 is similar to SHA-256 but is 128 bits and faster to compute <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

*   Once the solution is found, it's returned and broadcast to other nodes for verification, allowing the block to be confirmed on the blockchain <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.

This basic implementation demonstrates the core mechanics of a blockchain, including how transactions are linked, secured with cryptography, and validated through a proof-of-work system.