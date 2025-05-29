---
title: Monads performance and transaction speed
videoId: p74IdWNK8i8
---

From: [[thepipeline_xyz]] <br/> 

Monad introduces asynchronous execution as one of its [[Monads key innovations | key innovations]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This, combined with other optimizations, results in a [[monads_highperformance_blockchain_features | performant system]] capable of producing 10,000 transactions per second (TPS) at sub-cent gas fees <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Impact of Asynchronous Execution

Asynchronous execution fundamentally allows for much larger block sizes <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This enables app developers to write more secure code without concerns about increasing gas costs for end-users <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The outcome is cheaper and faster transactions with expanded gas limits <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Monad's expanded gas limits open up new design spaces, allowing developers to utilize cutting-edge primitives like proof verification and signature aggregation <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## How Transactions are Processed

Typically, when a user's wallet interacts with a blockchain, it sends a transaction through an RPC server <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This transaction is then sent to validators who maintain a mempool <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Transactions sit in the mempool until a leader validator decides to build a block, ordering these transactions within it <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Traditional Blockchain Execution

In [[monads_unique_infrastructure_versus_current_blockchain_environments | typical blockchains]], the block time — the period allocated to build a block — is shared between execution and consensus <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This means selecting transactions, putting them into a block, executing them, and reaching consensus on the block all occur within the same time segment <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. The time budget for execution in [[monads_unique_infrastructure_versus_current_blockchain_environments | most blockchains today]] is significantly smaller than the time budget for consensus, as network messages for consensus take the majority of the time <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. This limited execution time directly translates to a smaller gas limit for the block <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Monad's Asynchronous Execution with Parallelism

Asynchronous execution on Monad is made possible by parallelism <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Monad utilizes multiple threads to separate execution and consensus <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

*   **Separation of Concerns**: For a given block (e.g., Block Zero), the entire block time can be dedicated to performing consensus <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Pipelining**: The execution of Block Zero occurs in the subsequent block time, on a separate thread <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This creates a pipeline where consensus for one block occurs while execution for a previous block is happening concurrently <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Expanded Gas Budget**: Because execution is performed on a separate thread and can utilize an entire block time, the gas budget is massively expanded <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This allows for significantly more complex and numerous transactions within each block.

This combination of parallelism, pipelining, and the separation of consensus and execution into asynchronous processes makes Monad a [[monads_highperformance_blockchain_features | performance system]] <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.