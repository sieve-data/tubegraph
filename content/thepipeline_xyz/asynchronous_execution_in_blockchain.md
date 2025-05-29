---
title: Asynchronous Execution in Blockchain
videoId: p74IdWNK8i8
---

From: [[thepipeline_xyz]] <br/> 

[[Asynchronous and Parallel Execution in Blockchain Technology | Asynchronous execution]] is one of four core innovations introduced by Monad, forming part of a combination of optimizations that allow the system to achieve 10,000 transactions per second (TPS) at sub-cent gas fees <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Impact of Asynchronous Execution

On a fundamental level, [[impact_of_asynchronous_execution_on_block_sizes | asynchronous execution allows for much larger block sizes]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This capability offers several benefits:
*   **Enhanced Security for Developers** App developers can write more secure code without concern for increasing gas costs for end users <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Cheaper and Faster Transactions** It leads to significantly cheaper and faster transactions <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **New Design Spaces** With expanded gas limits, Monad opens up new design spaces, enabling developers to use cutting-edge primitives like proof verification and signature aggregation <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Traditional Blockchain Transaction Flow

To understand [[asynchronous_and_parallel_execution_in_blockchain_technology | asynchronous execution]], it's helpful to review the typical transaction process in blockchains:
1.  **Initiation** A user's wallet interacts with an RPC server to send a transaction <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
2.  **Mempool** The transaction is sent to a set of validators who maintain a "mempool" where transactions await processing <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
3.  **Block Building** A validator is chosen as the leader, selects transactions from the mempool, and builds a block, defining their order <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
4.  **Block Time Constraints** In typical blockchains, the "block time" (t0 to t1) encompasses all operations: block building, transaction execution (blue), and consensus (green) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   The time allocated for execution within this block time is relatively small <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
    *   The majority of the block time is consumed by consensus, largely due to network messages <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

## Monad's Approach: Asynchronous Execution with Parallelism

[[Asynchronous and Parallel Execution in Blockchain Technology | Asynchronous execution]] is only effective when coupled with [[parallel_execution_in_blockchain_technology | parallelism]] <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Monad achieves this by using multiple threads <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   Instead of bundling execution and consensus within a single block's time, Monad separates these processes onto different threads, operating on the same timeline <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   For a given block (e.g., block zero), the system can dedicate the entire block time to consensus <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   Execution for that same block can then occur in the *next* block's time, on a separate thread <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   This effectively extends the time budget for execution to the entire block time, rather than a small segment <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   This separation allows for a massive expansion of the block's gas budget or gas limit <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Interplay with Other Monad Innovations

The concept of [[asynchronous_and_parallel_execution_in_blockchain_technology | asynchronous execution]] in Monad is deeply intertwined with other [[optimizing_blockchain_performance | performance optimizations]]:
*   **[[Parallel execution in blockchain technology | Parallelism]]** is evident in the use of two or more threads working simultaneously <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Pipelining** occurs between the threads, as block zero first undergoes consensus on one thread, and then its execution is performed on another thread <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   The separation of consensus (on one thread) and execution (on another thread) defines [[asynchronous_and_parallel_execution_in_blockchain_technology | asynchronous execution]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

This combination of [[parallel_execution_in_blockchain_technology | parallelism]], pipelining, and [[asynchronous_and_parallel_execution_in_blockchain_technology | asynchronous execution]] is what makes Monad a high-performance system capable of addressing the [[need_for_performant_blockchains | need for performant blockchains]] and achieving [[the_importance_of_high_throughput_blockchains | high throughput]] <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.