---
title: Asynchronous Execution in Blockchain
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

Asynchronous execution represents a fundamental architectural shift in blockchain design, particularly observed in systems like Monad. Unlike traditional methods, it [[separation_of_execution_and_consensus_in_blockchain | separates the execution]] of transactions from the consensus process, allowing them to occur in parallel <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This approach aims to significantly improve [[blockchain_performance_optimization | blockchain performance optimization]] and throughput <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

## Interleaved Execution: The Traditional Model

Most blockchains traditionally operate using an "interleaved execution" model <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. In this setup, transaction execution and block consensus are performed in tandem within the same block time <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. For instance, in Ethereum, which has a 12-second block time, transaction execution might only occupy about 1% of that time, with the majority spent on consensus due to network latency and global distribution of nodes <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This means that processing new blocks is a sequential, chained process where execution and consensus for one block must largely complete before the next can begin <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

## How Asynchronous Execution Works

The core realization behind [[asynchronous_execution_in_blockchain | asynchronous execution]] is that given a deterministic state machine like the EVM, where the ordering and data of transactions are known, the results of execution will always be the same <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Therefore, execution does not need to happen concurrently with consensus for the *same* block <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

Instead, [[asynchronous_execution_in_blockchain | asynchronous execution]] allows:
*   **Decoupling Execution and Consensus** The execution of a block can be "pulled out" of its current block time <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Parallel Processing of Blocks** Nodes can come to consensus on the ordering and data of the *current* block, while simultaneously executing the *previous* block <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This means [[separation_of_execution_and_consensus_in_blockchain | consensus]] and execution processes operate on different "sides" or in different phases <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Expanded Execution Budget** This decoupling means that the execution process is no longer strictly constrained by the block time, allowing it to utilize the entire duration of the block time <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### Benefits

This architectural change offers several significant advantages:
*   **Higher Throughput** By expanding the "execution budget," it allows for a higher gas budget per block <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This directly translates to more transactions per second (TPS), with Monad targeting 10,000 real Ethereum transactions per second <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This contributes to [[discussion_on_high_throughput_blockchains | high throughput blockchains]] and [[high_performance_blockchains | high performance blockchains]].
*   **Lower Fees** Increased capacity generally leads to lower transaction fees <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Efficient Resource Utilization** It allows for better utilization of hardware by making sure the CPU is saturated with work, rather than waiting for consensus <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Caveats and Finality

While nodes agree on transaction ordering before execution <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>, they have a "delayed view" of the state <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. After reaching consensus on the ordering, nodes execute the transactions locally to update their state <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. This updated state is then subject to a later consensus check to ensure all nodes agree on the resulting state changes <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

Despite the delayed execution, finality in [[asynchronous_execution_in_blockchain | asynchronous execution]] systems like Monad is achieved at the point of consensus <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Because the EVM is deterministic, once the order and data of transactions are finalized by consensus, the outcome of their execution is guaranteed <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. A full node can immediately run these transactions locally to update its state as soon as consensus is reached <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

This engineering approach is gaining traction, with current proposals in other blockchains like Solana exploring similar implementations due to the significant benefits and minimal downsides it offers <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.