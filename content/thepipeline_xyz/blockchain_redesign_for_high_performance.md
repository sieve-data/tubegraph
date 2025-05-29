---
title: Blockchain redesign for high performance
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

Monad is a blockchain that represents a fundamental, from-scratch redesign, while retaining full EVM L1 equivalence and RPC compatibility. It aims to address the [[need for performant blockchain | need for performant blockchains]] by delivering significantly higher throughput and lower costs, making it a place where Ethereum applications can realize the vision of a world computer <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Monad from a Developer Perspective
Monad offers a fully EVM-equivalent L1 blockchain <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Developers familiar with EVM environments will find it feels largely the same, allowing them to port existing contracts and tap into existing EVM research and network effects <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Key features include:
*   **High Performance**: Targeting 10,000 real Ethereum transactions per second <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Single Block Times and Single Slot Finality**: Provides quick finality for transactions <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Full EVM RPC Compatibility**: Wallets, indexers, and other tools work out-of-the-box <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## Monad from a User Perspective
For users, Monad provides a [[future_of_high_performance_and_scalable_blockchains | high-performance, low-cost system]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Transaction costs are significantly reduced, for example, a Uniswap V2 transaction could cost hundreds of a cent <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. It aims to maintain decentralization with hundreds of nodes participating in consensus globally, while keeping hardware requirements reasonable <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## How Monad Achieves Performance
Monad's approach involves a new software architecture designed to maximize commodity hardware utilization and saturate all subsequent bottlenecks <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Understanding Blockchain Bottlenecks
Traditional distributed systems and blockchains face four fundamental constraints <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>:
1.  **Network Bandwidth**: Internet overhead for data transfer <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
2.  **CPU Throughput**: Speed of processor cores <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
3.  **State Access**: Speed of accessing the database and historical chain state <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
4.  **State Growth**: Managing current accounts and balances <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

Previous approaches often took "shortcuts" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>:
*   **High Bandwidth Requirements**: Some blockchains demand 1 GB or 10 GB internet connections for nodes, increasing costs <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Monad targets 100 megabits per second <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   **Centralized Node Placement**: Placing all nodes physically close together to reduce latency, sacrificing global distribution <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   **High RAM Requirements**: Requiring large amounts of RAM makes nodes expensive, as RAM is the most costly component in a computer system <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

Monad's goals are to get the most out of commodity hardware, design software that saturates hardware through all bottlenecks, and preserve decentralization by maintaining reasonable RAM requirements and supporting a globally distributed network of hundreds of nodes <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### New Software Architecture
Monad's redesign keeps only the EVM bytecode instructions, rebuilding everything else from the ground up <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>:
*   Fully rebuilt consensus <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   Fully rebuilt execution engine <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   Implemented [[parallel_evm_and_blockchain_optimizations | parallel execution]] <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   Custom state database called Monad DB <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Asynchronous Execution
Most blockchains today use "interleaved execution," where execution and consensus happen in tandem within a block time. For instance, in Ethereum, execution might only take 1% of the 12-second block time, with consensus consuming the majority due to global communication latency <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

[[monads_unique_approach_to_blockchain_performance | Monad's asynchronous execution]] stems from the realization that if a state machine like the EVM is deterministic (meaning you know the transaction ordering and data), the execution results will always be the same <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This allows execution to be pulled out of the current block and run in parallel with the consensus of the *next* block <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

*   Nodes come to consensus on transaction ordering *prior* to execution <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   Two blocks are processed in parallel: ordering the current block while executing the previous block <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   This significantly expands the execution budget and gas budget, leading to higher throughput and lower fees <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   Finality is at consensus time because the deterministic nature of the EVM ensures that if the data and order are known, the outcome is fixed <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### Parallel Execution
[[parallel_evm_and_blockchain_optimizations | Parallel execution]] is a core innovation of Monad, turning a single lane of sequential execution into multiple lanes to utilize modern multi-core CPUs <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. While transactions are still linearly ordered by consensus, they are executed in parallel <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

Monad uses a technique called "optimistic parallel execution," also known as software transactional memory (STM) or optimistic concurrency control (OCC) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>:
1.  Assume all transactions can run in parallel from a synced view of the world <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
2.  Generate a set of pending results <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
3.  Commit results serially. If a transaction's pending result relied on a state that was changed by a previously committed transaction, that transaction is re-executed with the updated state <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.

The overhead of re-execution is minimal because the most time-consuming part of a transaction is typically retrieving state from the database, not the execution itself <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. By caching state, re-execution is a light operation <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. This model eliminates the need for developers to deal with complex access lists, reducing bandwidth overhead while still providing high performance <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

### Monad DB (Custom State Database)
[[monads_unique_approach_to_blockchain_performance | Monad DB]] is a custom-built state database crucial for enabling parallel execution by allowing parallel state access <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. If the system is constantly waiting for the database to retrieve dependencies, parallel execution becomes irrelevant <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. Monad DB uses asynchronous IO to issue many requests to the database in parallel, feeding the execution engine as results return <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.

Modern hard drives (SSDs) offer high bandwidth and millions of IO operations per second, though lookup latency is higher than RAM <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. The key is to saturate this memory bandwidth by constantly pulling data from state in parallel to prevent bottlenecks <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

#### The Merkle Patricia Trie Problem
Ethereum stores its state in a Merkel Patricia Trie (MPT), which is a tree structure allowing for succinct verification of transactions and state <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. This means one can verify if data under a root is as expected by checking the root hash, without downloading and re-executing entire blocks <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

However, existing databases used by Ethereum clients (like LevelDB or PebbleDB) are typically B-trees or LSM-trees, not native MPTs <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. This creates a "tree traversal within a tree traversal" problem: when logically traversing the MPT, the system has to perform multiple lookups in the underlying, different physical database structure to find the next node. This can incur 16 to 32 times more overhead per lookup <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.

#### Monad DB's Solution
[[comparison_of_different_database_structures_for_blockchain_efficiency | Monad DB]] is a complete rebuild of a database where the Merkle Patricia Trie *is* the native way data is stored on disk <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. This removes the "tree in-direction" <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   **Native MPT Structure**: The MPT is stored directly on disk <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.
*   **Asynchronous IO (IO_Uring)**: Utilizes kernel technology like IO_Uring to spawn many parallel lookups <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.

This combination provides [[technical_challenges_and_solutions_in_blockchain_performance | parallel state access]] alongside [[parallel_evm_and_blockchain_optimizations | parallel execution]], which is the "secret sauce" that makes high-performance parallel execution truly feasible <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.

These innovations result in significant [[performance_gains_in_blockchain_transactions | performance gains]] and open up [[opportunities_for_application_development_on_highperformance_blockchains | opportunities for application development]] on high-performance blockchains.