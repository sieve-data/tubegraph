---
title: Monads Key Innovations
videoId: p74IdWNK8i8
---

From: [[thepipeline_xyz]] <br/> 

[[Monad and its Technical Innovations | Monad]] introduces several key innovations that collectively contribute to its high performance, enabling it to produce 10,000 transactions per second at sub-cent gas fees <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. One of these core innovations is asynchronous execution <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. These [[Performance improvements with Monads technology | optimizations]] are a combination of many different aspects that yield a highly performant system <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Asynchronous Execution: A Core Innovation

Asynchronous execution is a fundamental innovation that allows for significantly larger block sizes compared to systems without it <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Impact of Asynchronous Execution

The impact of asynchronous execution is far-reaching:
*   **Enhanced Security for Developers** It enables app developers to write much more secure code without concerns about increasing gas costs for end-users <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Cheaper and Faster Transactions** For end-users, this translates to much cheaper and faster transactions <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Expanded Design Spaces** With expanded gas limits, [[Monad and its Technical Innovations | Monad]] opens up new design spaces, allowing developers to leverage cutting-edge primitives like proof verification and signature aggregation <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Traditional Blockchain Transaction Processing

To understand asynchronous execution, it's helpful to first understand how transactions are typically sent to a blockchain <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>:
1.  A wallet interacts with an RPC server to send a transaction <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
2.  The transaction is then sent to a set of validators that maintain the mempool <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
3.  Transactions sit in the mempool until one validator is chosen as the leader <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
4.  The leader then takes transactions from the mempool and builds a block, ordering them <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

In typical blockchains, the "block time" (t0 to t1) encompasses all stages: building the block, execution (blue segment), and consensus (green segment) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The time budget for execution is often much smaller than the time budget for consensus, as network messages for consensus consume the majority of the time <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Monad's Asynchronous Approach

The concept of asynchronous execution is only possible with parallelism <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. [[Monad and its Technical Innovations | Monad]] utilizes multiple threads <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This approach separates execution and consensus onto different threads <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>:
*   For block zero, one thread can spend all its time doing consensus <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   In the next block time, another thread can execute the entire previous block <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

This means the time budget for execution is no longer a small segment but the entire block time <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. By separating execution onto a separate thread, [[Monad and its Technical Innovations | Monad]] massively expands the gas budget available for transactions <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

### Interplay with Parallelism and Pipelining

Asynchronous execution in [[Monad and its Technical Innovations | Monad]] is intrinsically linked to other [[Technical Details on Monads HighPerformance Features | high-performance features]]:
*   **Parallelism** Parallelism is evident between the two threads, where different operations occur concurrently <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Pipelining** Pipelining exists between the steps performed on these threads <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. For example, consensus for Block 0 is completed, and then execution for Block 0 is performed afterwards on a different thread <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

This separation of consensus on one thread and execution on another thread is the essence of asynchronous execution <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. It is this combination of parallelism, pipelining, and asynchronous execution that makes [[Monad and its Technical Innovations | Monad]] such a [[Performance improvements with Monads technology | performant system]] <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.