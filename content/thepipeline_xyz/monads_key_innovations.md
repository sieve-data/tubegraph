---
title: Monads key innovations
videoId: p74IdWNK8i8
---

From: [[thepipeline_xyz]] <br/> 

[[overview_of_monad_and_its_community | Monad]] introduces four key innovations, which are a combination of various optimizations designed to yield a highly [[monads_performance_and_transaction_speed | performant]] system <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This infrastructure allows [[monads_performance_and_transaction_speed | Monad]] to achieve 10,000 [[monads_performance_and_transaction_speed | transactions]] per second at sub-cent gas fees <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. One of these core innovations is **asynchronous execution** <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Asynchronous Execution

Asynchronous execution fundamentally impacts [[monads_unique_infrastructure_versus_current_blockchain_environments | block sizes]], allowing them to be significantly larger than on traditional blockchains <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This feature enables app developers to write more secure code without concern for increasing gas costs for end users <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The result is much cheaper and faster [[monads_performance_and_transaction_speed | transactions]] <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. With expanded gas limits, [[overview_of_monad_and_its_community | Monad]] opens up new [[developments_in_the_monad_ecosystem | design spaces]], allowing developers to leverage cutting-edge primitives like proof verification and signature aggregation <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Traditional Blockchain Execution

In typical blockchain environments, when a user sends a transaction via a wallet, it interacts with an RPC server <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This transaction is then sent to a set of validators, which maintain a mempool <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. A leader validator selects transactions from the mempool to build a block <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

The key concept in typical blockchains is that the block time—the period allocated for building a block, executing transactions, and achieving consensus—is shared <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This means execution and consensus occur within the same `t0` to `t1` block time <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

> "In most blockchains today like the time budget for execution is actually much smaller than the time budget for consensus here in green um because consensus takes a lot more time these Network messages across take the majority of time to actually add it to the blockchain" <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>

Consequently, the time budget for execution (and thus the gas limit of the block) is relatively small <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### How Asynchronous Execution Works in Monad

The concept of asynchronous execution in [[understanding_the_concept_of_monad | Monad]] relies on [[monads_unique_infrastructure_versus_current_blockchain_environments | parallelism]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. [[monads_unique_infrastructure_versus_current_blockchain_environments | Monad]] utilizes multiple threads, separating the execution and consensus phases of block processing <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

Instead of bundling execution and consensus within a single block's time, [[understanding_the_concept_of_monad | Monad]] allows:
*   **Separation of Concerns**: For a given block (e.g., Block 0), the validator spends all its allocated time on consensus <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Dedicated Execution Time**: In the *next* block time, the entire duration is used to execute the previous block (e.g., Block 0's execution is done in Block 1's time slot) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This means the time budget for execution becomes the *entire* block time, not just a small segment <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

This separation massively expands the gas budget for a block <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

#### Contributing Concepts

Asynchronous execution in [[understanding_the_concept_of_monad | Monad]] is a result of combining several advanced concepts:
*   **[[monads_unique_infrastructure_versus_current_blockchain_environments | Parallelism]]**: Utilizing multiple threads to process different aspects of block creation simultaneously <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Pipelining**: A sequential processing of tasks across different threads. For example, Block 0 undergoes consensus on one thread, and then its execution is performed on another thread <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Consensus is completed first, followed by execution <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

This combination of [[monads_unique_infrastructure_versus_current_blockchain_environments | parallelism]], pipelining, and the distinct separation of consensus on one thread and execution on another thread is what defines asynchronous execution and makes [[overview_of_monad_and_its_community | Monad]] a highly [[monads_performance_and_transaction_speed | performant]] system <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.