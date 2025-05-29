---
title: Role and Architecture of Monad DB in Optimizing Blockchain Efficiency
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

[[Monad Blockchain Technology | Monad DB]] is a fully custom state database, forming a crucial part of [[Monad Blockchain Technology | Monad's]] redesigned software architecture. It is designed to address the bottlenecks of traditional blockchain systems, particularly concerning state access and growth, thereby enabling high-performance features like [[optimizing_blockchain_performance | parallel execution]] <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

## Challenges in Traditional Blockchain Databases

Traditional blockchains, including Ethereum, store state using a logical structure called a Merkle Patricia Trie (MPT) <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>. This data structure is central to Ethereum's design philosophy, allowing for succinct verification of transactions and state. It enables users to check the root of something and verify that all data under that root is as expected <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>. Without an MPT, verifying a transaction would require downloading the entire block, re-executing it transaction by transaction, and then checking if the transaction is included <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>.

However, existing blockchain clients, such as Geth (Go Ethereum), LevelDB, or PebbleDB, typically use off-the-shelf databases like B-trees or LSM trees as their backend storage <a class="yt-timestamp" data-t="16:48:00">[16:48:00]</a>. These traditional database structures are not inherently Merkle Patricia Tries. This creates a "tree traversal within a tree traversal" problem <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>. When a node logically traverses the Merkle Patricia Trie, it translates into multiple lookups within the underlying non-MPT physical database, leading to 16 to 32 times more overhead per lookup <a class="yt-timestamp" data-t="19:36:00">[19:36:00]</a>.

Furthermore, accessing state from a database, especially from hard disk drives (HDDs) or Solid State Drives (SSDs), is significantly slower than CPU execution itself <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>. If the computer is constantly waiting for data to be pulled from the database for each transaction, the benefits of parallel execution are nullified <a class="yt-timestamp" data-t="15:16:00">[15:16:00]</a>.

## Architecture of [[Monad Blockchain Technology | Monad DB]]

[[Monad Blockchain Technology | Monad DB]] is a full redesign of a database where the Merkle Patricia Trie is the native way data is stored on disk <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>. This means that even if one were to store text or numbers in [[Monad Blockchain Technology | Monad DB]], it would inherently be structured as a Merkle Patricia Trie <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a>.

Key architectural features include:
*   **Native Merkle Patricia Trie Structure**: By directly structuring the Merkle Patricia Trie on disk, [[Monad Blockchain Technology | Monad DB]] eliminates the "tree in-direction" problem, vastly reducing the number of lookups required per traversal compared to traditional databases <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>. This results in 16 to 32 times fewer lookups <a class="yt-timestamp" data-t="20:10:00">[20:10:00]</a>.
*   **Asynchronous I/O**: [[Monad Blockchain Technology | Monad DB]] utilizes kernel technology called `IO_uring` to perform asynchronous I/O operations <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>. This allows the system to issue a multitude of requests to the database in parallel without waiting for each one to complete <a class="yt-timestamp" data-t="15:25:00">[15:25:00]</a>. As requests return, they are immediately fed into the execution engine <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>.

## Role in Optimizing Blockchain Efficiency

The primary role of [[Monad Blockchain Technology | Monad DB]] is to ensure the [[optimizing_blockchain_performance | parallel execution]] engine is continuously saturated with data <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>.

By providing [[optimizing_blockchain_performance | parallel state access]], [[Monad Blockchain Technology | Monad DB]] prevents the database from becoming a bottleneck:
*   **Feeds Parallel Execution**: It allows dependencies for many transactions to be pulled from the database simultaneously <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.
*   **Saturates Memory Bandwidth**: The design emphasizes saturating the memory bandwidth of modern hard drives, ensuring that data is always being pulled in parallel, preventing other parts of the system from being bottlenecked <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>. Modern SSDs, costing around $200, can offer about a million I/O operations per second, making it crucial to utilize their capabilities fully <a class="yt-timestamp" data-t="15:42:00">[15:42:00]</a>.

This combination of native MPT structuring and asynchronous I/O capability is the "secret sauce" that makes [[optimizing_blockchain_performance | parallel execution]] truly effective on [[Monad Blockchain Technology | Monad]], as it ensures that the compute resources are constantly fed with the necessary state data efficiently <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>.