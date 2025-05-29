---
title: Separation of execution and consensus in blockchain
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

The separation of execution and consensus is a key optimization that allows execution and consensus to operate in two distinct "swim lanes" within a blockchain system <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. This approach moves away from the traditional model where execution is a prerequisite for consensus, which can significantly slow down the responsiveness of the chain <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

## How it Works

In systems like Monad, the separation of execution and consensus means that the execution of transactions does not need to be completed before consensus is finalized <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. Instead, these processes can run in parallel, providing more time for both <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. This is achieved by relaxing how execution and consensus synchronize with each other, rather than imposing a restriction <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>. A deterministic algorithm manages this relaxation, ensuring proper communication and preventing any "cheating" between the two processes <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

While a leader can still choose to execute all transactions before sending out a proposal, this model grants a greater budget to all other participants to run them in parallel <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. The user experience (UX) is expected to remain the same <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

## Performance Gains

The primary benefit of separating execution and consensus is the massive unlock for execution performance <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. For instance, in Ethereum, with 12-second block times, the actual budget for execution is only about 100 milliseconds, equating to merely 1% of the total block time <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. This severe limitation impacts the gas limit and the amount of work that can be done within a block <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

By moving execution out of being a prerequisite for consensus and running it [[role_of_parallelism_and_pipelining_in_blockchain|in parallel]] to the next round of consensus, the system gains a much larger time budget for execution <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. This allows for higher throughput and better responsiveness, contributing to [[blockchain_performance_optimization|blockchain performance optimization]] and overall [[blockchain_scalability_and_highperformance_systems|scalability and high-performance systems]] <a class="yt-timestamp" data-t="00:41:36">[00:41:36]</a>.

## Contribution to Ethereum and the EVM Ecosystem

This architectural choice, along with other optimizations such as a custom state database and [[parallel_execution_in_blockchain|parallel execution]], represents an exploration in a new, orthogonal direction for blockchain development <a class="yt-timestamp" data-t="00:54:42">[00:54:42]</a>. Monad aims to push the boundaries of what is possible in the space, with the potential for these innovations to be incorporated into Ethereum itself <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a>. This contributes to the broader EVM ecosystem by providing a highly optimized execution stack <a class="yt-timestamp" data-t="00:54:29">[00:54:29]</a>. The goal is to bring more rigor to the industry's engineering and scientific practices, moving away from intuition-based marketing <a class="yt-timestamp" data-t="00:48:58">[00:48:58]</a>.