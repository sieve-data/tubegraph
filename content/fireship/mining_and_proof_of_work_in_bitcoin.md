---
title: Mining and proof of work in Bitcoin
videoId: qF7dkrce-mQ
---

From: [[fireship]] <br/> 

[[Understanding Bitcoin and its origins | Bitcoin]], first described in a 2008 white paper by the mysterious Satoshi Nakamoto, is a peer-to-peer electronic cash system designed to make reliable transactions based on [[cryptographic_proof_and_blockchain_technology | cryptographic proof]], eliminating the need for a trustee middleman <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The underlying protocol that makes this possible is blockchain <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

From a financial perspective, the blockchain acts as a shared public ledger containing all transactions from all [[Understanding Bitcoin and its origins | Bitcoin]] users <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This ledger is distributed and synchronized globally, removing the need for a central authority to maintain and validate it <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## The Double Spend Issue
A significant challenge in digital currency is the "double spend issue" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This occurs if a user attempts to send the same [[Understanding Bitcoin and its origins | Bitcoin]] to two different people simultaneously, potentially spending more money than they own before their transaction is confirmed on the blockchain <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a> <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

## Introduction to Mining
[[Understanding Bitcoin and its origins | Bitcoin]] addresses the double spend issue through a system called mining <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a> <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Mining is a process where multiple computers (nodes) around the world agree on the appropriate state of the entire system or ledger <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Process of Mining
1.  **Transaction Broadcast**: Each new transaction is broadcast to all nodes in the network <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  **Block Creation**: Transactions are packaged into a "block" <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
3.  **Proof of Work**: Miners expend computing power to validate "proof of work" for this block <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This involves computing a proof for a random computational problem that is very difficult to solve but very easy to verify <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
4.  **Solving the Proof**: The first miner to solve this problem (which occurs via "dumb luck") gets a portion of the [[Understanding Bitcoin and its origins | Bitcoin]] as a reward <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This system is likened to a "big lottery," with the winner earning coin as an incentive <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. It incentivizes people to invest in computing resources <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
5.  **Block Confirmation**: Once solved, the block is broadcast back to all other nodes where it is permanently confirmed on the blockchain <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a> <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

### Cryptographic Elements in Proof of Work
To implement a basic proof of work system, a "nonce" value is used <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. A nonce is a one-time use random number <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. The mining process attempts to find a number that, when added to the nonce, produces a hash that starts with a specific pattern (e.g., four zeros) <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. The only practical way to find this value is through brute force <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a> <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

Hashing algorithms like SHA-256 (Secure Hash Algorithm with 256 bits) and MD5 (128 bits) are used to create these hashes <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a> <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. [[Implementing cryptographic concepts in blockchain development | SHA-256]] is a one-way cryptographic function, meaning it can encrypt data but not decrypt it back to its original form <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Mining essentially converts cloud computing resources into money <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.