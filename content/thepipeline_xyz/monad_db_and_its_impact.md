---
title: Monad DB and its impact
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

[[monad_blockchain_development | Monad]] features a fully custom state database called Monad DB, which is crucial for its high-performance capabilities <a class="yt-timestamp" data-t="04:51:30">[04:51:30]</a>. This database is a fundamental component that enables Monad's parallel execution and overall efficiency <a class="yt-timestamp" data-t="04:51:30">[04:51:30]</a>.

## The Problem: Traditional State Storage in EVM Blockchains

Traditional blockchain designs often face fundamental constraints including network bandwidth, CPU throughput, state access, and state growth <a class="yt-timestamp" data-t="02:21:26">[02:21:26]</a>. When it comes to state access, a significant bottleneck arises from how Ethereum-like blockchains store their historical state <a class="yt-timestamp" data-t="02:33:04">[02:33:04]</a>.

### Merkle Patricia Trie and Off-the-Shelf Databases
Ethereum stores its state in a Merkel Patricia Trie (MPT), a tree structure designed to allow for succinct verification of transactions and state <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>, <a class="yt-timestamp" data-t="01:32:46">[01:32:46]</a>. This means you can check the root of something to determine if all data under that root is as expected <a class="yt-timestamp" data-t="01:26:22">[01:26:22]</a>. For example, to verify if a transaction is included, with an MPT you don't need to download and re-execute the entire block <a class="yt-timestamp" data-t="01:37:05">[01:37:05]</a>.

However, most Ethereum clients like Go Ethereum and Aragon use off-the-shelf databases (e.g., B-trees or LSM trees) to store this MPT <a class="yt-timestamp" data-t="01:47:30">[01:47:30]</a>. These standard databases are not natively built as a Merkle Patricia Trie <a class="yt-timestamp" data-t="01:48:47">[01:48:47]</a>. This creates an inefficiency: when logically traversing the MPT, the system performs a "tree traversal within a tree traversal" because it has to look up nodes in the non-MPT backend database <a class="yt-timestamp" data-t="01:50:52">[01:50:52]</a>, resulting in 16 to 32 times more overhead per lookup <a class="yt-timestamp" data-t="01:50:52">[01:50:52]</a>.

Furthermore, execution is incredibly cheap, but the time-consuming part is calling up the state for a transaction from the database, which involves going to the hard disk, reading into RAM, and then executing <a class="yt-timestamp" data-t="01:27:08">[01:27:08]</a>. If the computer is waiting for the database to pull dependencies every time a transaction is executed, parallel execution becomes irrelevant <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>.

## What Monad DB Is

Monad DB is a complete rebuild of a database where the Merkle Patricia Trie is the *actual* way data is stored on disk <a class="yt-timestamp" data-t="01:41:40">[01:41:40]</a>, <a class="yt-timestamp" data-t="01:44:48">[01:44:48]</a>. This design natively structures the Merkle Patricia Trie on disk, removing the "tree in direction" problem present in other implementations <a class="yt-timestamp" data-t="01:49:18">[01:49:18]</a>, <a class="yt-timestamp" data-t="01:50:52">[01:50:52]</a>.

### Key Technologies
*   **Native MPT Structure:** Monad DB makes Ethereum state native to how Ethereum works logically, directly storing the Merkle Patricia Trie on disk <a class="yt-timestamp" data-t="01:47:50">[01:47:50]</a>, <a class="yt-timestamp" data-t="02:02:16">[02:02:16]</a>.
*   **Asynchronous IO:** It utilizes a kernel technology called `IO_Uring` to enable asynchronous I/O <a class="yt-timestamp" data-t="02:07:34">[02:07:34]</a>, <a class="yt-timestamp" data-t="02:09:07">[02:09:07]</a>. This allows Monad DB to issue many requests to the database in parallel and immediately execute transactions as the results come back <a class="yt-timestamp" data-t="01:25:01">[01:25:01]</a>.

## Impact of Monad DB

Monad DB serves as the "secret sauce" that allows parallel execution to truly work <a class="yt-timestamp" data-t="02:18:55">[02:18:55]</a>. Its impact is seen in several areas:

*   **Saturates Parallel Execution:** By enabling parallel state access, Monad DB ensures that the parallel execution engine is continuously fed with the necessary data, preventing bottlenecks where the system would otherwise wait for database lookups <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>, <a class="yt-timestamp" data-t="01:59:44">[01:59:44]</a>.
*   **Reduced Lookups:** The native MPT structure drastically reduces the number of database lookups per tree traversal (16 to 32 times less) compared to off-the-shelf databases <a class="yt-timestamp" data-t="02:10:20">[02:10:20]</a>.
*   **Efficient State Access:** The combination of native MPT storage and asynchronous I/O makes state access very efficient, keeping the compute saturated <a class="yt-timestamp" data-t="02:14:46">[02:14:46]</a>.
*   **High Performance:** This efficiency contributes to [[monad_blockchain_development | Monad's]] ability to achieve high throughput, handling 10,000 real Ethereum transactions per second <a class="yt-timestamp" data-t="00:39:10">[00:39:10]</a>.