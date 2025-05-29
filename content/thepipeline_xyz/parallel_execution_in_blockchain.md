---
title: Parallel Execution in Blockchain
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

Monad is a blockchain designed as a "from scratch" redesign of the Ethereum Virtual Machine (EVM) architecture, offering a [[high_performance_blockchains | high performance]] system while maintaining full EVM compatibility <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a> <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. It aims to achieve 10,000 real Ethereum transactions per second and provide single block times with single-slot finality <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a> <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>. From a user perspective, Monad provides a low-cost system (hundreds of a cent for a Uniswap V2 transaction) and strives for decentralization with hundreds of globally distributed nodes maintaining reasonable hardware requirements <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a> <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a> <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a> <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

## Addressing Blockchain Bottlenecks

Traditional distributed systems and blockchains face four fundamental constraints <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>:
*   **Network Bandwidth:** Internet overhead <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. Some blockchains achieve performance by requiring high bandwidth (1 GB or 10 GB connections), unlike Monad which targets 100 megabits per second for consumer full nodes <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a> <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
*   **CPU Throughput:** Speed of processor cores <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.
*   **State Access:** Speed of retrieving data from the database and historical state <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.
*   **State Growth:** Managing current accounts and their balances <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

Many existing blockchains take shortcuts like increasing bandwidth requirements, placing nodes close together, or upping RAM requirements, which make nodes expensive and less decentralized <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a> <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a> <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a> <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. Monad's goal is to maximize performance from commodity hardware by designing software that saturates hardware through these bottlenecks while preserving decentralization <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a> <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.

## Monad's New Software Architecture

Monad's approach involves a full new architectural redesign, retaining only the EVM bytecode <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a> <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. Key components include:
*   A fully rebuilt consensus mechanism <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>.
*   A fully rebuilt execution engine <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.
*   Implemented [[optimistic_parallel_execution_algorithm | parallel execution]] <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
*   A custom state database called Monad DB <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

## [[asynchronous_execution_in_blockchain | Asynchronous Execution]]

Most blockchains today use "interleaved execution," where execution and consensus are performed in tandem within the same block time <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a> <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>. For example, in Ethereum's 12-second block time, execution might take 1% of the time, while consensus takes significantly longer due to global node communication <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a> <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.

[[asynchronous_execution_in_blockchain | Asynchronous execution]] stems from the realization that execution can be pulled out of consensus. Because the EVM is a deterministic state machine, knowing the transaction ordering and data means the execution results will always be the same <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a> <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. Monad leverages this by performing execution of the previous block in parallel with ordering (consensus) of the current block <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a> <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a> <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>.

This separation means:
*   Consensus and execution are on different sides of the timeline <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.
*   The execution budget can be greatly expanded to take up the entire block time, leading to higher throughput and lower fees <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a> <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.
*   Nodes come to consensus on transaction ordering prior to execution <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.
*   Finality is at consensus time, as a full node can immediately run transactions locally once consensus is reached <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a> <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>.

Many blockchains, including current proposals in Solana, are moving towards this model <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a> <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>.

## [[optimistic_parallel_execution_algorithm | Parallel Execution]]

[[optimistic_parallel_execution_algorithm | Parallel execution]] is the concept of taking a single lane of sequential processing and turning it into multiple lanes to fully utilize modern multi-core CPUs <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a> <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. Currently, transactions are typically linearly ordered and serially executed <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>. Monad aims to maintain this ordering provided by consensus but execute everything in parallel to get results much quicker <a class="yt-timestamp" data-t="10:59:00">[10:59:00]</a>.

Monad uses an [[optimistic_parallel_execution_algorithm | optimistic parallel execution algorithm]], also known as Software Transactional Memory (STM) or Optimistic Concurrency Control (OCC) <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a> <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>:
1.  Start with a synced view of the world <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.
2.  Assume everything can be run in parallel and generate a batch of pending results <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a> <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>.
3.  Walk through the pending results in order, attempting to commit them <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>.
4.  If a pending result relied on a previous one that changed, re-execute it with the new state <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a> <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>.

A key aspect of this algorithm is that, due to serial commitment, a transaction never needs to be re-executed more than once <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>. The overhead of re-execution is low because the most time-consuming part (calling up state from the database) is mitigated by caching <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a> <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>. This model also eliminates the need for developers to deal with access lists, reducing bandwidth overhead and simplifying the development interface <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a> <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a> <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>.

## Monad DB: Enabling [[parallel_execution_and_its_impact_on_performance | Parallel State Access]]

Monad DB is a custom state database crucial for saturating the [[optimistic_parallel_execution_algorithm | parallel execution]] engine by allowing [[parallel_execution_and_its_impact_on_performance | parallel state access]] <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a> <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>. If the computer has to wait for state dependencies to be pulled from the database for each transaction, [[optimistic_parallel_execution_algorithm | parallel execution]] is bottlenecked <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. Monad DB provides [[asynchronous_execution_in_blockchain | asynchronous I/O]], allowing multiple requests to the database in parallel, ensuring immediate execution as data returns <a class="yt-timestamp" data-t="15:25:00">[15:25:00]</a>.

Modern hard drives (SSDs) offer high bandwidth and millions of I/O operations per second, making it crucial to saturate this memory bandwidth by constantly pulling data from state in parallel <a class="yt-timestamp" data-t="15:42:00">[15:42:00]</a> <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>.

### Merkel Patricia Trie and Monad DB's Innovation

Ethereum stores its state in a Merkel Patricia Trie (MPT), a tree structure that enables succinct verification of transactions and state <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a> <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a> <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>. This allows checking the root hash to verify data integrity without downloading and re-executing an entire block <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a> <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>.

However, most EVM clients (like Go Ethereum) use off-the-shelf databases (e.g., B-trees or LSM trees) in the backend to store this MPT. These databases are not natively structured as MPTs <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a> <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a> <a class="yt-timestamp" data-t="16:56:00">[16:56:00]</a>. This leads to a "tree traversal within a tree traversal" where logical MPT traversals result in multiple inefficient lookups in the underlying non-MPT database (16 to 32 times more overhead) <a class="yt-timestamp" data-t="19:10:00">[19:10:00]</a> <a class="yt-timestamp" data-t="19:17:00">[19:17:00]</a> <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a> <a class="yt-timestamp" data-t="19:35:00">[19:35:00]</a>.

Monad DB is a full rebuild of a database where the Merkel Patricia Trie *is* the actual way data is stored on disk <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a> <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>. This removes the "tree in direction" and significantly reduces lookups per tree traversal (16 to 32 times less) <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a> <a class="yt-timestamp" data-t="20:10:00">[20:10:00]</a>. Combined with [[asynchronous_execution_in_blockchain | asynchronous I/O]] (using kernel technology like IOU_ring to spawn parallel lookups), Monad DB ensures that [[parallel_execution_and_its_impact_on_performance | parallel state access]] keeps the [[optimistic_parallel_execution_algorithm | parallel execution]] engine saturated and compute efficient <a class="yt-timestamp" data-t="20:19:00">[20:19:00]</a> <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a> <a class="yt-timestamp" data-t="20:52:00">[20:52:00]</a> <a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a> <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>.

In summary, Monad's unique combination of [[asynchronous_execution_in_blockchain | asynchronous execution]], [[optimistic_parallel_execution_algorithm | optimistic parallel execution]], and a custom-built, MPT-native database (Monad DB) forms its "secret sauce" for achieving [[discussion_on_high_throughput_blockchains | high throughput]] and [[blockchain_performance_optimization | performance optimization]] in a decentralized, EVM-compatible environment <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>.