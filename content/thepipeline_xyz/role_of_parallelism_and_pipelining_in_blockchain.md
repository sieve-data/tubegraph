---
title: Role of parallelism and pipelining in blockchain
videoId: p74IdWNK8i8
---

From: [[thepipeline_xyz]] <br/> 

[[asynchronous_execution_in_blockchain | Asynchronous execution]], a core innovation introduced by Monad, leverages [[parallel_execution_in_blockchain | parallelism]] and pipelining to achieve high transaction throughput <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This combination of optimizations allows Monad to process 10,000 transactions per second at sub-cent gas fees <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Impact of Asynchronous Execution

The fundamental impact of [[asynchronous_execution_in_blockchain | asynchronous execution]] is the ability to have much larger block sizes <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This capability offers several benefits:

*   **Secure Development**: App developers can write more secure code without concern for increasing gas costs for the end-user <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Cost-Efficiency and Speed**: It leads to much cheaper and faster transactions <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Expanded Design Space**: With expanded gas limits, new design spaces become available, enabling developers to use cutting-edge primitives like proof verification and signature aggregation <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Traditional Blockchain Execution Model

In a typical blockchain, when a user sends a transaction through an RPC server, it is sent to validators who maintain a mempool <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. A leader validator selects transactions from this mempool, builds a block, and orders them <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

A key characteristic of traditional blockchains is that the block time is shared between execution and consensus processes <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This means the time allocated for execution within a block is relatively small, often much smaller than the time spent on consensus due to the majority of time being consumed by network messages <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Role of Parallelism and Pipelining

[[asynchronous_execution_in_blockchain | Asynchronous execution]] fundamentally relies on [[parallel_execution_in_blockchain | parallelism]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. In systems like Monad, [[parallel_execution_in_blockchain | parallelism]] is achieved through the use of multiple threads <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

Instead of combining execution and consensus within a single block time on one thread, Monad "explodes" this process across multiple threads <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>:

*   **Separation of Concerns**: In a multi-threaded setup, one thread can dedicate its entire block time to consensus for Block 0, while another thread, during the *next* block time, can perform the execution for that same Block 0 <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Expanded Gas Budget**: This separation allows the *entire* block time to be utilized for execution, no longer limiting it to a small segment <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This significantly expands the gas budget <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Key Concepts Illustrated

This model demonstrates several core concepts:

*   **[[parallel_execution_in_blockchain | Parallelism]]**: Evident between the two threads operating concurrently <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Pipelining**: Achieved by sequencing the steps across threads. For instance, Block 0 undergoes consensus on one thread, and then its execution is performed on another thread in the subsequent block time, creating a pipeline <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **[[asynchronous_execution_in_blockchain | Asynchronous Execution]]**: Defined by the separation of consensus on one thread and execution on another <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

It is this synergistic combination of [[parallel_execution_in_blockchain | parallelism]], pipelining, and [[asynchronous_execution_in_blockchain | asynchronous execution]] that enables Monad to be a [[high_performance_blockchains | highly performant system]] <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.