---
title: Impact of asynchronous execution on block size and security
videoId: p74IdWNK8i8
---

From: [[thepipeline_xyz]] <br/> 

[[Asynchronous Execution in Blockchain | Asynchronous execution]] is one of four key innovations introduced by Monad, combining various optimizations to create a system capable of producing 10,000 transactions per second at sub-cent gas fees <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This approach fundamentally enables significantly larger block sizes compared to traditional blockchains <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Benefits of Asynchronous Execution

The impact of [[Asynchronous Execution in Blockchain | asynchronous execution]] translates into several key benefits:

*   **Larger Block Sizes and Expanded Gas Limits**
    *   In traditional blockchains, the execution and consensus phases share the same block time <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The time budget for execution is often much smaller than that for consensus, as network messages for consensus consume the majority of the time <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   With [[Asynchronous Execution in Blockchain | asynchronous execution]], which relies on [[Parallel Execution in Blockchain | parallelism]] using multiple threads <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, the consensus for a block (e.g., Block Zero) can be completed on one thread, while its execution is handled on a separate thread in the subsequent block time <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   This [[separation_of_execution_and_consensus_in_blockchain | separation of execution and consensus on multiple threads]] means that the entire block time can be dedicated to execution <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This massively expands the gas budget available for transactions <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

*   **Enhanced Security and Developer Capabilities**
    *   Larger block sizes enable app developers to write more [[Security and scalability in crosschain communication | secure]] code without concerns about increasing gas costs for end users <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
    *   This expansion of gas limits opens up new design spaces for developers, allowing them to leverage cutting-edge primitives like proof verification and signature aggregation <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
    *   The outcome for end users is significantly cheaper and faster transactions <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## How it Works

The concept of [[Asynchronous Execution in Blockchain | asynchronous execution]] is intertwined with [[Parallel Execution in Blockchain | parallelism]] and pipelining within the blockchain architecture <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

In a typical blockchain interaction, a transaction is sent from a wallet via an RPC server to a set of validators that maintain a mempool <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. A leader validator selects transactions from the mempool and builds a block, ordering them <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

In a traditional setup, execution (processing transactions) and consensus (agreeing on the block order and state) occur sequentially within the same block time <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This means the time available for execution is constrained by the overall block time, and often, consensus takes up the majority of this time <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

[[Asynchronous Execution in Blockchain | Asynchronous execution]] utilizes multiple threads for these processes <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This allows for:
*   **[[Parallel Execution in Blockchain | Parallelism]]**: Different blocks can be processed concurrently on separate threads <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Pipelining**: The consensus for one block (e.g., Block Zero) can be finalized, while the execution for that same block occurs in the next block time on a separate thread <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. This [[separation_of_execution_and_consensus_in_blockchain | separation of consensus on one thread and execution on another]] is the core of [[Asynchronous Execution in Blockchain | asynchronous execution]] <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

This combination of [[Parallel Execution in Blockchain | parallelism]], pipelining, and [[Asynchronous Execution in Blockchain | asynchronous execution]] contributes to Monad's high [[blockchain_performance_optimization | performance]] <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.