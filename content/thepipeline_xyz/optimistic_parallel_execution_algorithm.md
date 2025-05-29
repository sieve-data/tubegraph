---
title: Optimistic parallel execution algorithm
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

The optimistic parallel execution algorithm is a core component of how Monad Labs aims to achieve high performance in its blockchain. Monad was among the first to develop a [[parallel_evm_and_its_impact_on_performance | parallel EVM]] algorithm over one and a half years ago <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## How it Works

In Monad, transactions within a block are still linearly ordered <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. The primary goal of this algorithm is to reach the final state after executing each transaction as if they were run one after another, but to accomplish this work in a shorter period <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

The process for optimistic parallel execution is described as relatively simple and intuitive, sometimes referred to as optimistic concurrency control <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>:
1.  **Parallel Execution**: A group of transactions are run in [[parallel_execution_in_blockchain | parallel]], each generating a "pending result" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  **Record Keeping**: Each pending result includes a record of the inputs and outputs for its respective transaction <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
3.  **Ordered Commitment**: These pending results are then committed in the original, linear order of the transactions <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
4.  **Conflict Resolution**: If, during the commitment phase, a pending result's inputs are found to have been invalidated (due to a conflict with an earlier committed transaction), that specific transaction's work is rescheduled for re-execution <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. No further commitments occur until the re-executed transaction is processed <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

A key aspect is that this re-execution, when conflicts arise, is generally inexpensive because the necessary inputs are almost always found in the cache, requiring only a simple cache lookup <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Performance and Bottlenecks

Despite its implementation almost a year and a half prior to discussions, Monad found that optimistic [[parallel_execution_in_blockchain | parallel execution]] on its own yielded very little improvement compared to serial transaction execution <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The reason for this became evident: the primary bottleneck in blockchain performance is **state access** <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

Transactions depend on accounts and storage slots, and this state information is typically stored on an SSD in Ethereum <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The cost of reading from an SSD is substantial <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Crucially, the databases used by Ethereum and other EVM-compatible blockchains to store this state do not support [[parallel_execution_and_its_impact_on_performance | parallel access]] <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This means that even with multiple virtual machines running in [[parallel_execution_in_blockchain | parallel]], all state reads still bottleneck at the database, effectively resulting in single-file execution <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### The Role of Custom Databases

This discovery forced Monad to pursue other [[optimization_strategies_for_blockchain_clients | optimizations]] to truly impact performance <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Merely paralyzing computation (e.g., through a [[parallel_evm_and_its_impact_on_performance | parallel EVM]]) does not inherently lead to significant gains <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. The actual performance breakthrough comes from fundamental [[blockchain_performance_optimization | optimizations]] at the state database level <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This led Monad to develop its own custom database tailored for blockchain needs, a departure from general-purpose databases like PebbleDB or RocksDB <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

According to Monad, the most expensive operations in blockchain are cryptography functions (like elliptical curve cryptography and hashing), and especially state access <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. The latency of a single read from an SSD can be 80-100 microseconds or more, which is orders of magnitude longer than executing a simple smart contract <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. Without effective caching, multiple sequential reads can sum up to long execution times for a single transaction <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

A common "shortcut" to address this is to simply increase the amount of RAM available, as RAM is much faster than SSDs <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. However, this is significantly more expensive (2 terabytes of RAM cost $20,000 compared to $200 for a high-quality 2 terabyte NVMe SSD) <a class="yt-timestamp" data-t="00:50:56">[00:50:56]</a>. This approach doesn't scale well, hinders decentralization, and avoids solving the underlying issue <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>.

By customizing the database to the specific ways blockchain data is stored and accessed, Monad aims to maximize performance from existing hardware. Standard general-purpose databases are not optimized for the specific access patterns of a blockchain, leading to inefficient read operations (e.g., 20 requests to hardware for a basic lookup versus Monad's 1-2 requests) <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.

## Conclusion

The optimistic parallel execution algorithm, while a foundational step, is only truly effective when combined with deep-level [[blockchain_performance_optimization | optimizations]], particularly in how state is managed and accessed. This requires rigorous engineering, experimentation, and a willingness to avoid "shortcuts" like simply throwing more hardware at the problem <a class="yt-timestamp" data-t="00:32:57">[00:32:57]</a>.