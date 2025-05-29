---
title: Optimistic parallel execution algorithm
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

The [[monad_blockchain_and_its_performance_optimizations | Monad blockchain]] implements an optimistic [[parallel_execution_in_blockchain_technology | parallel execution]] algorithm, which was first developed over a year and a half ago by Monad Labs <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This approach clarifies that transactions within a block are linearly ordered, with the ultimate goal of reaching the final state after executing each transaction as if done sequentially, but in a shorter timeframe <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## How it Works

The optimistic [[parallel_execution_in_blockchain_technology | parallel execution]] algorithm is relatively simple <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>:
1.  **Parallel Execution**: A batch of transactions are run simultaneously, generating "pending results" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  **Record Inputs/Outputs**: Each pending result includes a record of the inputs and outputs for its respective transaction <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
3.  **Ordered Commitment**: These pending results are then committed in the original, linear order of the transactions <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
4.  **Conflict Resolution**: If, during the commitment phase, an input for a pending result is found to have been invalidated (e.g., due to a conflict with an earlier committed transaction), that specific transaction is re-scheduled for execution <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Further commitments are paused until the re-executed transaction is processed <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

This method is also known as "optimistic concurrency control" <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Re-execution due to conflicts is often inexpensive because the necessary inputs are typically already in cache, leading to quick cache lookups <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Observed Impact and Bottlenecks

Despite its intuitive design, Monad's implementation of the optimistic [[parallel_execution_in_blockchain_technology | parallel execution]] algorithm, done over a year and a half ago, did not yield significant performance improvements compared to serial execution <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

The primary bottleneck identified was **state access** <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   Transactions have dependencies on accounts and storage slots <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   This state is typically stored on an SSD in Ethereum and other EVM-compatible blockchains <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   The cost of reading from an SSD is substantial <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, ranging from 80 to 100 microseconds or more, which is orders of magnitude longer than executing a simple smart contract <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   Existing databases used by EVM-compatible blockchains for state storage (like Pebble DB or RocksDB) do not support [[parallel_execution_in_blockchain_technology | parallel access]] efficiently <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   When multiple virtual machines attempt parallel reads to the database, they still bottleneck, effectively leading to single-file execution <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## Beyond Parallel Execution: The Need for Deeper Optimizations

The realization that [[parallel_execution_in_blockchain_technology | parallel execution]] alone wasn't enough to achieve true performance gains led Monad to explore other [[optimizations in EVM implementations | optimizations in EVM implementations]] <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. It's akin to putting a Lamborghini body on a Toyota Corolla engine; the external parallelization doesn't matter if the underlying components are slow <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

The key to unlocking performance gains for [[parallel_execution_in_blockchain_technology | parallel execution]] lies in fundamental [[optimization techniques specific to blockchain databases | optimization techniques specific to blockchain databases]] and other parts of the execution stack <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

Key areas of focus include:
*   **Custom State Database**: Monad developed its own custom database to allow for parallel access to state <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This is critical because standard general-purpose databases (like B+ tree or LSM trees) are not optimized for the specific access patterns of blockchain state <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. A custom database can leverage the high performance of modern SSDs, which can support 500,000 I/O operations per second, but only if the software is designed to extract that performance <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.
*   **Separation of Execution and Consensus**: By decoupling execution from consensus, more time is allowed for both processes to run in parallel, significantly increasing the budget for execution <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. In Ethereum, only about 100 milliseconds out of a 12-second block time is allocated to execution, which is a mere 1% <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.
*   **Micro-optimizations**: Monad performs numerous micro-optimizations, such as optimizing translation lookaside buffers (TLBs), which might individually offer small gains (e.g., 5%), but accumulate to significant speedups <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>. This involves deep analysis at the assembly instruction level <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>.

The focus on these comprehensive, ground-up [[optimizing_blockchain_performance | optimizing blockchain performance]] strategies is why Monad's tagline is "no shortcuts" <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>. It's about performing the necessary fundamental engineering and scientific work, constantly measuring and experimenting, rather than relying on intuitive but unverified assumptions <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.