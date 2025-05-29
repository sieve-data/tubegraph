---
title: Differences in blockchain transaction metrics
videoId: rXMlv51Mmsc
---

From: [[thepipeline_xyz]] <br/> 

Measuring the [[performance_gains_in_blockchain_transactions | performance]] of blockchain platforms can be complex, with various metrics often leading to confusion and differing interpretations. One of the most frequently discussed, yet often misunderstood, metrics is Transactions Per Second (TPS) <a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>.

## Understanding and Measuring TPS

The concept of [[understanding_and_measuring_TPS_in_blockchain | TPS]] aims to quantify the throughput of a blockchain, indicating how many transactions it can process in a given second <a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>. However, the definition of what constitutes a "transaction" can vary significantly across different platforms, leading to inflated or incomparable numbers <a class="yt-timestamp" data-t="00:49:24">[00:49:24]</a>.

### The Solana Case: Voting Transactions

A prominent example of differing [[understanding_and_measuring_TPS_in_blockchain | TPS]] reporting comes from [[comparison_between_different_blockchain_platforms | Solana]]. Its main block explorers advertise a high [[understanding_and_measuring_TPS_in_blockchain | TPS]] number, which includes not only user-initiated transactions (like swapping tokens or minting NFTs) but also votes from validators <a class="yt-timestamp" data-t="00:47:16">[00:47:16]</a>.

While these votes are technically formulated as [[comparison_between_different_blockchain_platforms | Solana]] transactions, they are distinct from direct user interactions <a class="yt-timestamp" data-t="00:47:42">[00:47:42]</a>. The "true [[understanding_and_measuring_TPS_in_blockchain | TPS]]" for user-driven activities on [[comparison_between_different_blockchain_platforms | Solana]] is approximately 500 transactions per second, with an additional 2500 or more votes occurring every second <a class="yt-timestamp" data-t="00:47:59">[00:47:59]</a>. This means a reported [[understanding_and_measuring_TPS_in_blockchain | TPS]] of 3000 would include both <a class="yt-timestamp" data-t="00:48:15">[00:48:15]</a>.

For Monad, the plan is to only count "real transactions"—smart contract interactions and transfers—and not include votes in any reported [[understanding_and_measuring_TPS_in_blockchain | TPS]] figures <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.

### Varied Transaction Definitions

Other platforms also adopt different definitions:
*   Some, like [[comparison_between_different_blockchain_platforms | Aptos]] or [[comparison_between_different_blockchain_platforms | Sui]], might count an "instruction" as a transaction <a class="yt-timestamp" data-t="00:48:57">[00:48:57]</a>. This means a single smart contract invocation that executes several sub-instructions could be counted as ten transactions, distorting the actual throughput <a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>. This non-uniformity makes direct [[comparison_between_different_blockchain_platforms | comparison between different blockchain platforms]] difficult <a class="yt-timestamp" data-t="00:49:24">[00:49:24]</a>.

## Capacity vs. Demand

Another layer of confusion in measuring [[understanding_and_measuring_TPS_in_blockchain | blockchain]] performance is the difference between a system's maximum possible throughput and the current demand it experiences <a class="yt-timestamp" data-t="00:49:39">[00:49:39]</a>. If a system's capacity far exceeds its current usage, the observed [[understanding_and_measuring_TPS_in_blockchain | TPS]] will be much lower than its theoretical maximum <a class="yt-timestamp" data-t="00:49:52">[00:49:52]</a>.

Furthermore, when teams try to demonstrate maximum capacity by loading their testnets with transactions, questions arise about whether the testnet accurately reflects a real-world production environment <a class="yt-timestamp" data-t="00:50:04">[00:50:04]</a>.

## Towards Standardization and Transparency

The current landscape is characterized by "information wars" where different teams advertise performance metrics in ways that favor their platforms <a class="yt-timestamp" data-t="00:50:46">[00:50:46]</a>.

To address this, a better approach would be to:
*   **Reproducible Benchmarks**: Implement reproducible benchmarks with open-source GitHub repositories <a class="yt-timestamp" data-t="00:50:49">[00:50:49]</a>. This involves publishing full scripts that define how servers are deployed globally and how transactions are sent to nodes, allowing others to verify and reproduce the results <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>. Monad plans to introduce such benchmarks for its own platform and potentially for [[comparison_between_different_blockchain_platforms | competitive benchmarks]] <a class="yt-timestamp" data-t="00:51:17">[00:51:17]</a>.
*   **Standardized Metrics**: Recognize that transaction sizes and complexities vary <a class="yt-timestamp" data-t="00:51:47">[00:51:47]</a>. While simple transfers might allow for accurate [[comparison_between_different_blockchain_platforms | comparison between different blockchain platforms]], real-world activity involving complex smart contract interactions makes [[understanding_and_measuring_TPS_in_blockchain | TPS]] a less reliable metric <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>.
*   **"Bytes Per Second"**: For a more consistent measure of raw throughput in a production system, "bytes per second" could be a better benchmark. This metric abstracts away the conditional definitions of a "transaction" across different blockchains <a class="yt-timestamp" data-t="00:52:32">[00:52:32]</a>.
*   **Historical Benchmarking**: Monad uses the historical Ethereum transaction history as a benchmark, providing a proxy for real-life activity given the varying composition of transactions <a class="yt-timestamp" data-t="00:52:56">[00:52:56]</a>.

In conclusion, while [[understanding_and_measuring_TPS_in_blockchain | TPS]] is a significant metric for blockchain [[performance_gains_in_blockchain_transactions | performance]], its effectiveness is often diluted by conflated definitions and measurement methodologies <a class="yt-timestamp" data-t="00:53:25">[00:53:25]</a>. The [[need_for_performant_blockchain | need for performant blockchain]] requires a commitment to transparent and reproducible benchmarking practices for meaningful [[comparison_of_different_database_structures_for_blockchain_efficiency | comparison of different database structures for blockchain efficiency]] and [[challenges_in_blockchain_system_design | blockchain system design]] <a class="yt-timestamp" data-t="00:51:40">[00:51:40]</a>, ultimately driving the industry forward through better understanding of [[technical_challenges_and_solutions_in_blockchain_performance | technical challenges and solutions in blockchain performance]] and [[challenges_in_current_blockchain_infrastructure | current blockchain infrastructure]].