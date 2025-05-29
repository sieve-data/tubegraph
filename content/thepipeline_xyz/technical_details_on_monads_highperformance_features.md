---
title: Technical Details on Monads HighPerformance Features
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

Monad is a blockchain designed as a "full scratch redesign" of an EVM L1 equivalent blockchain that looks similar to Ethereum in shape <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It aims to provide a high-performance system for Ethereum applications <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, while maintaining full EVM RPC compatibility <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This means developers can port over existing contracts and tap into the EVM ecosystem <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## High-Performance Metrics

Monad targets significant [[performance_improvements_with_monads_technology | performance improvements]] over existing EVM chains:
*   **Transactions Per Second (TPS)**: 10,000 real historical Ethereum transactions per second (not just transfers) <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Block Times**: Single block times <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Finality**: Single slot finality <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Transaction Costs**: Hundreds of a cent for a Uniswap V2 transaction <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Decentralization**: Achieved by supporting hundreds of nodes globally with reasonable hardware requirements <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Addressing Blockchain Bottlenecks

Monad's design addresses four fundamental constraints in distributed blockchain systems <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>:
1.  **Network Bandwidth**: The internet overhead for nodes <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Monad targets 100 megabits per second for a consumer full node, compared to 1 GB or 10 GB connections used by other blockchains <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
2.  **CPU Throughput**: How fast the computer cores can run <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
3.  **State Access**: The speed of accessing the database and historical state of the chain <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
4.  **State Growth**: The ability to quickly pull up current accounts and their balances <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

Many existing blockchains take shortcuts by increasing bandwidth requirements, placing nodes close together, or increasing RAM requirements, which makes nodes expensive and reduces decentralization <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Monad's goal is to maximize performance from commodity hardware while preserving decentralization through a new software architecture <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## New Software Architecture

Monad features a full redesign of its architecture, keeping only the EVM bytecode instructions <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Key components of this architecture include:
*   Rebuilt Consensus (not detailed in this discussion) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>
*   Rebuilt Execution Engine <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>
*   [[Parallel Processing and Pipelining in Monad | Parallel Execution]] <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>
*   Custom State Database ([[Monad and its Technical Innovations | Monad DB]]) <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>

### Asynchronous Execution (Pipelining)

Traditional blockchains often use "interleaved execution," where execution and consensus happen in tandem within a single block time <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For example, in Ethereum, execution might take 1% of the 12-second block time, with consensus taking significantly longer due to global network latency <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

Monad's "asynchronous execution" stems from the realization that execution can be decoupled from consensus <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Because the EVM is a deterministic state machine, if the ordering and data of transactions are known, the results will always be the same <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This allows Monad to pull execution out of the current block and perform it in tandem with the next block <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Essentially, Monad orders the current block while executing the previous block <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

This approach means that consensus and execution operate on different sides of the block production process <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. Monad comes to consensus on the data and its order, and then executes it afterward, in parallel with coming to consensus on the next block's ordering <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. This allows Monad to expand the execution budget, leading to higher throughput and lower fees <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

Nodes come to consensus on transaction ordering prior to execution <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. While nodes have a delayed view of the state, finality is achieved at consensus time because the deterministic nature of the EVM ensures that if the order and data are known, the outcome is final <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### [[Parallel Processing and Pipelining in Monad | Parallel Execution]]

[[Parallel Processing and Pipelining in Monad | Parallel execution]] transforms a single processing lane into multiple lanes, leveraging modern computers' multi-core CPUs <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. While transactions are linearly ordered by consensus, Monad executes them in parallel and commits the results in their original order <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

Monad uses "optimistic parallel execution," also known as Software Transactional Memory or Optimistic Concurrency Control (OCC) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. The process is as follows:
1.  Start with a synced view of the world and assume all transactions can run in parallel <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
2.  Generate a batch of pending results <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
3.  Walk through the pending results in order, attempting to commit them <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
4.  If a pending result relied on a previous one that was modified (a conflict), re-execute that transaction with the new state <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

Due to the serial commitment process, no transaction needs to be re-executed more than once <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. The overhead of re-execution is low because the most time-consuming part of a transaction is calling up the state from the database, not the execution itself <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. State is cached, making re-execution light <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

A benefit of this model is that developers do not need to deal with access lists, which simplifies development and reduces bandwidth overhead <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. This provides a familiar EVM interface while maintaining backend performance <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

### [[Monad and its Technical Innovations | Monad DB]]

[[Monad and its Technical Innovations | Monad DB]] is Monad's custom state database that enables [[Parallel Processing and Pipelining in Monad | parallel execution]] by providing parallel state access <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. It ensures that the parallel execution engine remains saturated by providing asynchronous I/O, allowing many requests to the database in parallel <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

Modern hard drives (SSDs) offer high bandwidth and millions of I/O operations per second, making it crucial to saturate this memory bandwidth <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

Ethereum stores its state in a Merkle Patricia Trie (MPT), which enables succinct verification of transactions and state <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>. This allows checking a root hash to verify all data under it, without downloading and re-executing entire blocks <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. However, most Ethereum clients use off-the-shelf databases (like B-trees or LSM trees) to store this MPT structure <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>. This creates a "tree traversal within a tree traversal" problem: logically traversing the MPT requires multiple lookups within the backend database, incurring 16 to 32 times more overhead <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

[[Monad and its Technical Innovations | Monad DB]] is a full rebuild of a database where the Merkle Patricia Trie is the native way data is stored on disk <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. This removes the indirection, leading to 16 to 32 times fewer lookups per traversal of the state tree <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. Combined with asynchronous I/O using kernel technology like IOU_ring, Monad DB can spawn many parallel lookups to feed the [[Parallel Processing and Pipelining in Monad | parallel execution]] engine efficiently <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. This parallel state access, alongside [[Parallel Processing and Pipelining in Monad | parallel execution]], is the "secret sauce" behind Monad's performance <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.