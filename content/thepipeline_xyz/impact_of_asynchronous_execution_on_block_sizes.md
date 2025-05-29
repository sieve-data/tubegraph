---
title: Impact of Asynchronous Execution on Block Sizes
videoId: p74IdWNK8i8
---

From: [[thepipeline_xyz]] <br/> 

[[asynchronous_execution_in_blockchain | Asynchronous execution]] is one of Monad's four core innovations, contributing to a system so [[need_for_performant_blockchains | performant]] it can process 10,000 transactions per second at sub-cent gas fees <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

On a fundamental level, [[asynchronous_execution_in_blockchain | asynchronous execution]] allows for significantly larger block sizes compared to traditional blockchain architectures <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Traditional Blockchain Transaction Flow

Typically, when a user interacts with a blockchain (e.g., via a wallet), a transaction is sent through an RPC server to a set of validators that maintain a mempool <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>, <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>, <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. One validator is chosen as the leader at a given time, building a block from these mempool transactions and ordering them <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

In most traditional blockchains, the block time (the interval from t0 to t1) is shared between transaction execution and consensus <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The time allocated for execution is often much smaller than the time required for consensus, as network messages involved in achieving consensus consume the majority of the block time budget <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>, <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

## Asynchronous Execution with Parallelism

[[asynchronous_execution_in_blockchain | Asynchronous execution]] is effective when combined with [[parallel_execution_in_blockchain_technology | parallelism]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Monad employs multiple threads to separate execution and consensus along the same timeline <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>, <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

For instance, while Block 0's consensus is being finalized on one thread, the execution of Block 0 can occur on a separate thread during the subsequent block time <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This means the entire block time is dedicated to execution, rather than a small segment <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Impact on Block Sizes and Gas Limits

The direct consequence of this architectural shift is a massive expansion of the gas limit for a block <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. By dedicating the full block time to execution, the block's capacity for transactions, measured by gas, significantly increases <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

## Benefits for Developers and Users

The expansion of block sizes through [[asynchronous_execution_in_blockchain | asynchronous execution]] offers several advantages:

*   **For App Developers**: It allows them to write more secure code without the constraint of increasing gas costs for end-users <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. With expanded gas limits, Monad opens up new design spaces, enabling developers to leverage cutting-edge primitives like proof verification and signature aggregation <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **For End Users**: Transactions become much cheaper and faster <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Monad's Innovations

Monad's [[performance_and_scalability_of_blockchain_systems | performance]] stems from a combination of innovations:

*   **[[parallel_execution_in_blockchain_technology | Parallelism]]**: Execution occurs across multiple threads <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Pipelining**: Steps like consensus and execution are pipelined across threads; for example, Block 0's consensus is followed by its execution on a separate thread <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>, <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **[[asynchronous_execution_in_blockchain | Asynchronous Execution]]**: The separation of consensus on one thread and execution on another <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>, <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>, <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

This blend of [[asynchronous_and_parallel_execution_in_blockchain_technology | Asynchronous and Parallel Execution]] is what makes Monad a [[optimizing_blockchain_performance | high-performance]] system, setting the stage for the [[the_future_of_highperformance_blockchains | future of high-performance blockchains]] and their [[applications_and_potential_of_highperformance_blockchains | applications and potential]] to deliver [[the_importance_of_high_throughput_blockchains | high throughput]] <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.