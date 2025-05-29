---
title: Parallel Processing and Pipelining in Monad
videoId: p74IdWNK8i8
---

From: [[thepipeline_xyz]] <br/> 

[[understanding_monads_from_developer_and_user_perspective | Monad]] introduces asynchronous execution as one of its four key innovations, contributing to its ability to achieve 10,000 transactions per second at sub-cent gas fees <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This approach leverages [[technical_details_on_monads_highperformance_features | parallelism]] and pipelining to optimize blockchain operations <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Impact of Asynchronous Execution
Asynchronous execution fundamentally allows for much larger block sizes <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **For Developers:** It enables the writing of more secure code without concern for increasing gas costs for end-users <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The expanded gas limits open up new design spaces, allowing developers to utilize cutting-edge primitives like proof verification and signature aggregation <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **For Users:** It results in significantly cheaper and faster transactions <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Traditional Blockchain Process
Typically, when a user sends a transaction:
1.  Their wallet interacts with an RPC server <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
2.  The transaction is sent through the RPC server to a set of validators that maintain a mempool <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
3.  A leader validator selects transactions from the mempool and builds a block, defining their order <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

In most current blockchains, the entire block time (from t0 to t1) is shared for all operations: block building, transaction execution, and consensus <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The time allocated for execution is often much smaller than for consensus, as network messages for consensus consume the majority of the time budget <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## [[performance_improvements_with_monads_technology | Monad]]'s Approach: Parallelism and Pipelining
[[understanding_monads_from_developer_and_user_perspective | Monad]] separates the execution and consensus phases onto different threads, enabling asynchronous execution <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Parallelism
[[technical_details_on_monads_highperformance_features | Monad]] utilizes multiple threads for processing <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This allows for parallel execution of different operations on different threads <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. For instance, while one thread is dedicated to achieving consensus for a block, another thread can simultaneously handle the execution of transactions <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This represents parallelism because two distinct processes are occurring concurrently <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Pipelining
[[technical_details_on_monads_highperformance_features | Monad]] also implements pipelining <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. This means that the phases of block processing (consensus and execution) are ordered sequentially but overlap across different blocks on separate threads <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   For Block 0, the first thread focuses on consensus.
*   Subsequently, on a second thread, Block 0's execution is performed <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

This separation means that the time budget for execution is no longer a small segment of the block time but the entire block time itself <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This massively expands the gas budget for a block <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Combination for [[performance_improvements_with_monads_technology | Performance]]
The combination of [[technical_details_on_monads_highperformance_features | parallelism]] (multiple threads doing work concurrently) and pipelining (ordered steps overlapping across blocks) facilitates asynchronous execution <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This comprehensive approach is what makes [[understanding_monads_from_developer_and_user_perspective | Monad]] a highly performant system <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.