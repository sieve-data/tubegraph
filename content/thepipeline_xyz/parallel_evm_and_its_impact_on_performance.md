---
title: Parallel EVM and its impact on performance
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

The concept of the [[Parallel Execution in Blockchain|Parallel EVM]] has gained significant attention in the crypto space, with many teams claiming to work on their own iterations <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. Monad Labs, where Keone and James, formerly of Jump Trading and Jump Crypto, now serve as CEO and CTO respectively, pushed the first [[Parallel Execution in Blockchain|parallel EVM]] algorithm over 1.5 years ago <a class="yt-timestamp" data-t="01:16:11">[01:16:11]</a>.

## Monad's Optimistic Parallel Execution Algorithm

Monad's approach involves transactions that are linearly ordered within a block, aiming to reach the end state efficiently <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. Their "optimistic parallel execution algorithm" works as follows:
*   A batch of transactions runs in parallel, generating pending results <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.
*   Each pending result records inputs and outputs <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   These results are committed in the original transaction order <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.
*   If an input for a pending result is invalidated during commitment, that transaction is re-executed <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.
*   Re-execution is typically cheap because inputs are often in cache <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

Despite this algorithm, Monad found that [[Parallel Execution in Blockchain|parallel execution]] alone did not significantly improve [[Performance optimizations in Ethereum Virtual Machine EVM|performance]] compared to serial execution <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

## The True Bottleneck: State Access and Databases

The primary bottleneck for [[Performance optimizations in Ethereum Virtual Machine EVM|performance gains]] in blockchains is **state access** <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. Transactions depend on accounts and slots within accounts, which are stored on SSDs in Ethereum <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. The cost of reading from an SSD is significant, typically 80-100 microseconds or more per read <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>.

Existing databases used by Ethereum and other [[EVM compatibility and innovation|EVM-compatible]] blockchains, such as Pebble DB or Rock DB, do not support parallel access <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. This means that even with multiple virtual machines running in parallel, they still bottleneck on database reads, effectively leading to single-file execution <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.

> "When many virtual machines are running in parallel and going and making reads to the database, they all still bottleneck and it it effectively is kind of like a single file execution." <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>

The computationally expensive parts of blockchain operations are cryptography functions (elliptic curve, hashing) and state access <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. Complex business logic in smart contracts is relatively cheap <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>. Therefore, simply [[Parallel execution and its impact on performance|parallelizing computation]] alone doesn't yield much gain <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.

## Monad's Custom Database

Monad's solution to the state access bottleneck is a custom-built database <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>. Standard general-purpose databases like LMDB, MDBX, RocksDB, or LevelDB are not optimized for the specific access patterns of a blockchain <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>. In high-frequency trading (HFT), standard libraries are rarely used; instead, customized data structures are built to extract maximum [[Performance optimizations in Ethereum Virtual Machine EVM|performance]] from hardware <a class="yt-timestamp" data-t="13:55:00">[13:55:00]</a>.

Monad applies this HFT technique, knowing exactly how data will be used and stored, to build a highly optimized database <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>. A modern $200 SSD can perform 500,000 I/O operations per second (IOPS), but existing blockchain clients often fail to leverage this, making numerous requests for basic lookups <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>. Monad's database may make one or two requests to look up an account, compared to 20 or more for other data structures not in cache <a class="yt-timestamp" data-t="16:46:00">[16:46:00]</a>. This "super optimization" extracts every last bit of [[Performance optimizations in Ethereum Virtual Machine EVM|performance]] from the hardware <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>.

## Other Key Optimizations: Separation of Execution and Consensus

Another significant optimization Monad employs is the separation of execution and consensus <a class="yt-timestamp" data-t="17:15:00">[17:15:00]</a>.
*   By not requiring execution to complete before consensus, both can run in parallel, providing more time for each <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>.
*   This relaxation in synchronization is handled by a deterministic algorithm to ensure communication and prevent "cheating" <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>.
*   In Ethereum's 12-second block times, the budget for execution is only about 100 milliseconds (1% of the block time) <a class="yt-timestamp" data-t="19:14:00">[19:14:00]</a>.
*   Moving execution out of being a prerequisite for consensus, and running it in parallel with the next consensus round, is a massive unlock for execution capacity <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>.

## The "No Shortcuts" Philosophy

Monad's tagline, "no shortcuts," reflects their commitment to deep optimization <a class="yt-timestamp" data-t="20:35:00">[20:35:00]</a>.
*   A shortcut would be to simply throw more hardware (e.g., massive amounts of RAM) at the problem <a class="yt-timestamp" data-t="21:09:00">[21:09:00]</a>. While this can improve [[Performance optimizations in Ethereum Virtual Machine EVM|performance]], it makes network participation harder and more expensive, impacting decentralization <a class="yt-timestamp" data-t="21:17:00">[21:17:00]</a>.
*   Instead, Monad aims to run on commodity hardware, like a $200 SSD, and extract maximum [[Performance optimizations in Ethereum Virtual Machine EVM|performance]] from it <a class="yt-timestamp" data-t="21:03:00">[21:03:00]</a>.
*   This approach involves meticulous, quantitative engineering, including analyzing assembly instructions and running extensive experiments with different databases <a class="yt-timestamp" data-t="30:53:00">[30:53:00]</a>.
*   Optimizations of even 5% add up significantly (e.g., 10 5% optimizations yield a 50% speedup) <a class="yt-timestamp" data-t="30:31:00">[30:31:00]</a>.
*   The team emphasizes making informed decisions based on measurement and experimentation, not just intuition or common assumptions (e.g., questioning whether access lists are truly beneficial) <a class="yt-timestamp" data-t="34:19:00">[34:19:00]</a>.
*   This rigorous process involves writing and discarding a lot of code, as is common in high-performance engineering <a class="yt-timestamp" data-t="34:36:00">[34:36:00]</a>.

## Benchmarking [[Performance optimizations in Ethereum Virtual Machine EVM|Performance Optimizations]]

Currently, there are no standardized benchmarks in crypto, allowing for unsubstantiated claims <a class="yt-timestamp" data-t="44:54:00">[44:54:00]</a>.
*   Monad internally uses replaying recent Ethereum history as their benchmark <a class="yt-timestamp" data-t="46:20:00">[46:20:00]</a>.
*   The term "TPS" (Transactions Per Second) lacks context without specifying transaction type (e.g., token transfers vs. complex Uniswap transactions) <a class="yt-timestamp" data-t="45:31:00">[45:31:00]</a>. A non-optimized client can do 50k TPS of simple token transfers <a class="yt-timestamp" data-t="45:57:00">[45:57:00]</a>.
*   Monad plans to release a publicly available GitHub repository with benchmarks that can be replicated, encouraging open, standardized benchmarking for the industry <a class="yt-timestamp" data-t="46:24:00">[46:24:00]</a>.
*   This will allow for fair comparisons and contribute to raising the standard of engineering in the blockchain space <a class="yt-timestamp" data-t="48:40:00">[48:40:00]</a>.

[!WARNING]
A common "shortcut" for artificially boosting benchmarks is to use large amounts of RAM <a class="yt-timestamp" data-t="50:24:00">[50:24:00]</a>. However, RAM is two orders of magnitude more expensive than SSDs ($20,000 for 2 terabytes of RAM versus $200 for 2 terabytes of high-quality NVMe SSD) <a class="yt-timestamp" data-t="50:32:00">[50:32:00]</a>. This approach doesn't scale or promote decentralization, as nodes would require ever-increasing RAM over time <a class="yt-timestamp" data-t="51:29:00">[51:29:00]</a>.

## [[EVM compatibility and innovation|EVM Compatibility]] and Contribution to Ethereum

Monad is [[EVM compatibility and innovation|EVM compatible]] down to the bytecode level, ensuring that everything functions exactly the same as Ethereum <a class="yt-timestamp" data-t="36:21:00">[36:21:00]</a>.
*   The choice of VM (e.g., EVM, SVM, WASM) is not a significant factor in [[Performance optimizations in Ethereum Virtual Machine EVM|performance]], as differences between them are minor <a class="yt-timestamp" data-t="37:12:00">[37:12:00]</a>. The Ethereum VM is considered "fine" and capable <a class="yt-timestamp" data-t="38:41:00">[38:41:00]</a>.
*   Full [[EVM compatibility and innovation|Ethereum compatibility]] is crucial for tooling, developer experience, and seamless porting of contracts, allowing developers to focus on business logic <a class="yt-timestamp" data-t="39:04:00">[39:04:00]</a>.

Users primarily value latency and responsiveness <a class="yt-timestamp" data-t="40:00:00">[40:00:00]</a>. While throughput depends on the application, a high throughput is necessary to support a large user base <a class="yt-timestamp" data-t="40:55:00">[40:55:00]</a>. Monad aims to build a blockchain that balances both throughput and latency to provide the best user experience <a class="yt-timestamp" data-t="41:40:00">[41:40:00]</a>.

Monad meaningfully contributes to the Ethereum ecosystem by exploring a new, orthogonal direction: rebuilding the execution stack from the ground up, researching custom databases, and implementing advanced optimizations like [[Parallel execution and its impact on performance|parallel execution]] and asynchronous execution <a class="yt-timestamp" data-t="53:38:00">[53:38:00]</a>. This work pushes the boundaries of what is possible, and any changes or innovations developed by Monad could potentially be incorporated into Ethereum itself, contributing to the broader space <a class="yt-timestamp" data-t="54:50:00">[54:50:00]</a>.

For instance, Monad envisions supporting a fully on-chain limit order book that requires sub-cent fees for orders and thousands of orders per second, enabling a level of interaction previously seen in traditional finance but not yet realized in DeFi <a class="yt-timestamp" data-t="28:33:00">[28:33:00]</a>. This exemplifies the kind of [[performance_needs_in_decentralized_finance | performance needs in decentralized finance]] that Monad is designed to address.