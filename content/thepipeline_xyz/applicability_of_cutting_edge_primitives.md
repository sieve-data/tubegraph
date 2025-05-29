---
title: Applicability of Cutting Edge Primitives
videoId: p74IdWNK8i8
---

From: [[thepipeline_xyz]] <br/> 

[[Monad and its Technical Innovations | Monad]] introduces several [[optimizations in EVM implementations | optimizations]] that contribute to its high performance, enabling it to process 10,000 transactions per second with sub-cent gas fees <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. One of the key innovations is asynchronous execution, which significantly impacts block sizes <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Expanded Gas Limits and New Design Spaces

The implementation of asynchronous execution allows for much larger block sizes, which in turn enables app developers to write more secure code without concern for increasing gas costs for end users <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This leads to significantly cheaper and faster transactions <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

With these expanded gas limits, [[Monad and its Technical Innovations | Monad]] opens up brand new [[The Future of Applications on Monads HighPerformance Network | design spaces]] for developers <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. These new capabilities allow developers to leverage cutting-edge primitives that were previously impractical due to high computational or transactional costs <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Examples of Cutting Edge Primitives

Specific examples of advanced primitives that become viable on [[Monad and its Technical Innovations | Monad]]'s high-performance network include:
*   **Proof verification** <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>
*   **Signature aggregation** <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>

## Technical Basis: Asynchronous Execution

Traditionally, the execution of transactions and reaching consensus for a block share a single, limited time budget within a blockchain's block time <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. In most blockchains, the time allocated for execution is much smaller than the time needed for consensus, as network messages for consensus consume the majority of the block time <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

Asynchronous execution, supported by [[Technical Details on Monads HighPerformance Features | parallelism]] (using multiple threads), separates these processes <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. For instance, while one block's consensus is being finalized, the execution of the *previous* block's transactions can occur on a separate thread <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This separation allows the entire block time to be dedicated to execution, rather than just a small segment <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

The practical implication of this technical innovation is a massive expansion of the gas budget for each block <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This increased computational capacity is what makes the [[Applicability of Cutting Edge Primitives | applicability of cutting-edge primitives]] feasible for [[applications_and_potential_of_highperformance_blockchains | applications]] requiring more complex cryptographic operations or data processing <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. The combination of [[Technical Details on Monads HighPerformance Features | parallelism]], pipelining, and asynchronous execution contributes to [[Monad and its Technical Innovations | Monad]] being a highly performant system <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.