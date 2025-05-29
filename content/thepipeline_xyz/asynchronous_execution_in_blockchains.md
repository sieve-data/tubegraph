---
title: Asynchronous execution in blockchains
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

Asynchronous execution in blockchains fundamentally redesigns how transaction execution and consensus are handled, moving away from traditional sequential processing <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This approach aims to maximize the utilization of underlying hardware and improve overall blockchain performance <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## How it Works

The core idea behind asynchronous execution is the realization that execution can be "pulled out" of the consensus process <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. In a deterministic state machine, such as the EVM, if the ordering of transactions and their data are known, the execution results will always be the same <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This deterministic nature allows for the separation of execution from the immediate consensus process <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

In an asynchronously executing system, the blockchain can order the current block while simultaneously executing the previous block <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This means consensus and execution operate on different timelines <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. Nodes first come to consensus on the transaction ordering and data of a block <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>, and then execute it <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This contrasts with traditional interleaved execution, where execution and consensus happen in tandem within a single block time <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### Comparison to Interleaved Execution

Historically, many blockchains, like Ethereum, use interleaved execution <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. In this model, execution and consensus are tightly coupled within each block time <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. For example, in Ethereum's 12-second block time, execution might only take about 1% of that duration, while consensus takes significantly more time due to network latency among globally distributed nodes <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Blocks are processed sequentially, one after another <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

Asynchronous execution, however, enables two blocks to be worked on in [[parallel_execution_methods | parallel]] <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. The system can be coming to consensus on the data and ordering of the current block, while concurrently executing the previously ordered block <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

## Benefits

This approach offers several significant advantages:

*   **Expanded Execution Budget** Asynchronous execution greatly expands the execution budget, which in turn allows for a larger gas budget per block <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **[[high_throughput_blockchains_and_infrastructure_challenges | Higher Throughput]] and Lower Fees** A larger gas budget directly translates to [[high_throughput_blockchains_and_infrastructure_challenges | higher throughput]] and lower transaction fees <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Single-Slot Finality** Even though execution occurs later, finality is achieved at the point of consensus <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Because the ordering and data are known and deterministic, a full node can immediately execute transactions locally as soon as consensus is reached, providing an immediate state update <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

## Considerations

While beneficial, asynchronous execution requires careful design:

*   **State Synchronization** Systems utilizing asynchronous execution must implement checks to ensure all nodes remain synchronized <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Nodes may have a delayed view of the state, meaning after consensus, they execute locally to obtain the updated state, which is then re-verified through consensus at a later point to confirm agreement across all nodes <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## Industry Adoption

The concept of asynchronous execution is gaining traction in the blockchain space <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. Other prominent blockchains, like Solana, are exploring similar models, as it is recognized as an effective engineering solution with significant benefits, such as a larger gas budget, with few downsides <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.