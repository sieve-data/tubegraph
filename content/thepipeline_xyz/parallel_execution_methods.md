---
title: Parallel execution methods
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

Modern blockchain architectures, like Monad, are redesigning their systems from scratch to overcome the performance bottlenecks of traditional distributed systems, particularly focusing on optimizing how transactions are processed. This involves implementing sophisticated parallel execution methods and novel database designs <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

## Monad's Approach to Performance

Monad aims to achieve high performance (10,000 transactions per second for real Ethereum historical transactions) <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, single block times, and single slot finality, all while maintaining full EVM RPC compatibility and supporting hundreds of decentralized nodes globally with reasonable hardware requirements <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. To do this, Monad implements a new software architecture, rebuilding its execution engine and introducing a custom state database called MonadDB <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>, <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

This approach is possible by addressing fundamental blockchain constraints such as network bandwidth, CPU throughput, state access, and state growth, without resorting to shortcuts like requiring extremely high internet connections or centralizing nodes <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. The goal is to maximize the potential of commodity hardware while preserving [[decentralization]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

The core components enabling this performance are:
*   [[asynchronous_execution_in_blockchains | Asynchronous Execution]]
*   [[parallelization_in_blockchain_technologies | Parallel Execution]]
*   MonadDB (custom State Database)

### [[asynchronous_execution_in_blockchains | Asynchronous Execution]]

Most traditional blockchains operate with "interleaved execution," where transaction execution and consensus occur in tandem within a single block time <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. For example, in Ethereum, execution might only take up 1% of the 12-second block time, with consensus consuming the majority due to network latency <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>, <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

Monad's [[asynchronous_execution_in_blockchains | asynchronous execution]] stems from the realization that execution can be decoupled from consensus <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Because the EVM is a deterministic state machine, if the ordering and data of transactions are known, the execution results will always be the same <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This allows Monad to pull execution out of the current block and perform it in parallel with the consensus process of the *next* block <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

This means:
*   Nodes reach consensus on transaction ordering *before* execution <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   Two blocks are processed in parallel: the previous block is executed while consensus is reached on the ordering and data of the current block <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>, <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   This approach significantly expands the execution budget and gas budget, leading to higher throughput and lower fees <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>, <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   Finality occurs at the consensus time, as the deterministic nature of the EVM ensures that full nodes can immediately update their state once consensus on ordering is achieved <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>, <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

Other blockchains, such as Solana, are also exploring similar asynchronous execution models <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>, <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### [[parallelization_in_blockchain_technologies | Parallel Execution]]

[[parallelization_in_blockchain_technologies | Parallel execution]] involves taking a single lane of sequential processing and turning it into multiple lanes to utilize modern computers' multi-core processors <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>, <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. In traditional blockchains, transactions are linearly ordered and serially executed <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Monad aims to maintain this consensus-determined ordering but execute everything in parallel to achieve results much faster, then commit them in the original order <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

Monad achieves this through "optimistic parallel execution," also known as software transactional memory (STM) or optimistic concurrency control (OCC) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. The process works as follows:
1.  **Initial Assumption**: The system starts with a synced view of the world and assumes all transactions can be run in parallel <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
2.  **Generate Pending Results**: Transactions are executed in parallel, generating a set of pending results <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
3.  **Serial Commitment and Re-execution**: The system then walks through these pending results in their original serial order, attempting to commit them <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. If a pending result is found to have relied on an outdated state due to a previously committed transaction, it is re-executed with the updated state <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>, <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
    *   This algorithm ensures that a transaction never needs to be executed more than once <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
    *   The overhead of re-execution is low because the necessary state is already cached in memory, making execution cheap compared to disk access <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>, <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
    *   This model eliminates the need for developers to deal with access lists, which simplifies development and reduces bandwidth overhead <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>, <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.

### MonadDB: Custom State Database

The effectiveness of [[parallelization_in_blockchain_technologies | parallel execution]] heavily relies on efficient state access. If the execution engine has to wait for the database to retrieve necessary data for each transaction, the benefits of parallelism are lost <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>, <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. MonadDB is a custom state database designed to enable parallel state access and keep the parallel execution engine saturated with data <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>, <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.

Key features of MonadDB:
*   **Asynchronous I/O**: MonadDB utilizes asynchronous I/O (via kernel technology like IOUring) to issue multiple requests to the database in parallel <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>, <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. This ensures that the system is always pulling data out of state concurrently, preventing bottlenecks <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Native Merkle Patricia Trie Storage**: Ethereum logically stores its state in a Merkle Patricia Trie (MPT), which is crucial for succinct verification of transactions and state <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>, <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. However, most existing Ethereum clients use off-the-shelf databases (like LevelDB or PebbleDB) that are not natively structured as MPTs <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>, <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. This leads to inefficient "tree traversal within a tree traversal" where logical MPT lookups require multiple physical lookups in the underlying database <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>, <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.
*   MonadDB is a full rebuild of a database where the Merkle Patricia Trie is the *actual* way data is stored on disk <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>, <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. This eliminates the indirection, reducing the number of lookups per tree traversal by 16 to 32 times <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>, <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

This combination of [[asynchronous_execution_in_blockchains | asynchronous execution]], [[monads_parallel_execution_for_high_throughput | optimistic parallel execution]], and a custom-built state database (MonadDB) that natively understands Ethereum's state structure allows Monad to achieve true [[monads_unique_approach_to_blockchain_performance | parallel execution for high throughput]] by ensuring both parallel computation and parallel state access <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>, <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>.