---
title: Manad Labs execution and consensus separation
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

One of [[Monad Labs Technology and Innovations | Monad]]'s key optimizations involves the separation of execution and consensus within the blockchain architecture <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. This approach involves having execution and consensus operating in two distinct "swim lanes" <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.

## How it Works

In [[Monad Labs Technology and Innovations | Monad]], transactions are linearly ordered within a block, and the goal is to reach the final state after executing each transaction as if they were run sequentially <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. The separation of execution and consensus means that execution is not required to complete before consensus <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. This allows both processes to run in [[parallelization_in_blockchain_technologies | parallel]], providing more time for each <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.

This design involves relaxing how execution and consensus synchronize with each other, which is then managed by a deterministic algorithm for communication <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

## Performance Gains and Efficiency

Running execution and consensus in [[parallelization_in_blockchain_technologies | parallel]] yields significant performance benefits <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>. If block execution is a prerequisite for responding to consensus, it slows down the chain's responsiveness <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

### Comparison to Ethereum

In Ethereum, with 12-second block times, the execution budget is roughly only 100 milliseconds within that 12-second window <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. This means only about 1% of the block time is allocated to execution <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>. This severely limits the gas limit and the total amount of work that can be done within a block <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

### "Massive Unlock"

Moving execution out of being a prerequisite for consensus, and instead running it [[parallelization_in_blockchain_technologies | parallel]] to the next round of consensus, is considered a "massive unlock" for execution <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. It's not a restriction on validators; a leader can still choose to execute all transactions before sending out their proposal, although this would require more powerful hardware <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. The key benefit is that it provides a greater budget for everyone else to run execution in [[parallelization_in_blockchain_technologies | parallel]] <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>, without compromising the user experience <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

Exploring innovations like implementing [[asynchronous_execution_in_blockchains | asynchronous execution]] is crucial for advancing the blockchain space <a class="yt-timestamp" data-t="00:53:56">[00:53:56]</a>.