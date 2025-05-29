---
title: Parallel EVM and blockchain optimizations
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

Monad Labs, with Keone as CEO and James as CTO, is at the forefront of [[Parallelization in blockchain technologies | parallel EVM]] development and essential optimizations to achieve true [[Performance gains in blockchain transactions | Performance gains]] in blockchain performance <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Monad's Optimistic Parallel Execution Algorithm

Monad Labs developed and implemented their optimistic parallel execution algorithm over one and a half years ago <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. In Monad, transactions are linearly ordered within a block, aiming to reach the end state as if they were run one after another, but completing the work faster <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

The algorithm functions by running multiple transactions in parallel, generating pending results <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Each pending result records the inputs and outputs for its transaction <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. These results are then committed in the original transaction order <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. If a pending result's input has been invalidated during this process, the work is rescheduled, and further commitments are paused until that transaction is re-executed <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This re-execution is typically inexpensive because needed inputs are usually cached <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

Despite this algorithm, Monad found that [[Parallelization in blockchain technologies | parallel execution]] alone did not yield significant [[Performance gains in blockchain transactions | improvement]] compared to serial execution <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## The True Bottleneck: State Access

The primary bottleneck in blockchain performance is state access <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Transactions depend on accounts and their slots, with this state stored on an SSD in Ethereum <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The cost of reading from an SSD is substantial <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. Existing databases used by Ethereum and other EVM-compatible blockchains do not support parallel access <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This means that even with multiple virtual machines running in parallel, they still bottleneck on database reads, effectively leading to single-file execution <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

The most expensive parts of blockchain operations include cryptography functions (elliptical curve cryptography, hashing) and state access <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Complex smart contract business logic is relatively cheap to execute compared to typical desktop or phone programs <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Therefore, parallelizing computation by itself offers limited benefit <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

A single read from an SSD can have a latency of 80 to 100 microseconds or more <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. This is orders of magnitude longer than it takes to execute a simple smart contract <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. Transactions typically involve multiple reads (sender account, destination account, proxy accounts, storage slots like ERC20 balances), which, if sequential, accumulate into significant execution times <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

### Monad's Custom Database

Monad's inspiration to build a custom database stemmed from identifying state access as the bottleneck and the realization that existing general-purpose databases like PebbleDB or RocksDB are not optimized for blockchain use cases <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>, <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

Standard databases often embed one data structure inside another on disk, making every request traverse two data structures, which is expensive <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. While different database types exist (B+ tree databases like LMDB/MDBX, LSM trees like RocksDB/LevelDB), their general-purpose design means they are optimized for average performance, not the specific access patterns of a blockchain <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

Monad's custom database is designed specifically for how blockchain data is stored and accessed, a technique borrowed from high-frequency trading (HFT) where customized data structures lead to significantly better hardware performance <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. Modern SSDs are highly performant (e.g., 500,000 I/O operations per second for a $200 SSD) <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>, <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>, but general database implementations fail to leverage this capability <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. Some blockchain clients use these databases in a way that requires numerous requests for basic lookups (e.g., 20 requests for a non-cached lookup, vs. 1-2 for Monad's database), wasting hardware potential <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.

## Separation of Execution and Consensus

Another key optimization is the separation of execution and consensus <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. By not requiring execution to complete before consensus, both processes can run in parallel, providing more time for each <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. This relaxation of synchronization allows for a greater budget for execution <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. For example, in Ethereum, with 12-second block times, the execution budget is only about 100 milliseconds (1% of the block time), severely limiting the gas limit and work capacity <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. Running execution in parallel to the next round of consensus is a massive unlock for execution throughput <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

## "No Shortcuts" Philosophy

Monad's "no shortcuts" approach emphasizes deep, quantitative understanding and engineering over quick fixes <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. Shortcuts, such as simply throwing large amounts of hardware (e.g., RAM) at the problem, make it harder and more expensive for regular people to participate in the network, hindering decentralization <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. While Monad aims to run on commodity hardware (like a $200 SSD), it focuses on maximizing performance within those constraints, rather than requiring expensive, large-RAM servers <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>, <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.

This philosophy is rooted in their background in high-frequency trading, where systems were optimized down to tens or hundreds of nanoseconds <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>. This involves looking at code compilation, assembly instructions, and making countless micro-optimizations that accumulate to significant speed-ups <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>.

Monad's approach involves:
*   **Challenging Intuitions**: Assumptions, like access lists being universally beneficial for [[Parallelization in blockchain technologies | parallel execution]] or state preloading, are rigorously tested and often found to be incorrect <a class="yt-timestamp" data-t="00:31:44">[00:31:44]</a>.
*   **Measurement and Experimentation**: Every decision is informed by data and extensive experimentation, including writing and discarding code that doesn't meet performance goals <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.
*   **Avoiding Local Maximums**: Continuously seeking ways to relax constraints and explore new architectural approaches to find even faster solutions <a class="yt-timestamp" data-t="00:33:45">[00:33:45]</a>.

The **need for performant blockchain** was evident to Monad's founders during their time at Jump Crypto, working on Solana DeFi projects in 2021 <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. They recognized that existing [[optimizing_evm_implementations | EVM implementations]] were highly inefficient and lacked the level of optimization seen in high-performance trading systems <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

## Benchmarking for True Performance Gains

Currently, there are no standardized benchmarks in crypto, allowing various projects to make unsubstantiated claims about TPS (Transactions Per Second) <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>. TPS numbers without context (e.g., token transfers vs. complex Uniswap transactions) can be misleading <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>.

Monad has internally used recent Ethereum history as its benchmark <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>. Their plan is to release a publicly available GitHub repository where others can download and replicate benchmarks on their chain and other projects <a class="yt-timestamp" data-t="00:46:24">[00:46:24]</a>. This promotes transparency and allows the industry to hold projects accountable <a class="yt-timestamp" data-t="00:46:52">[00:46:52]</a>.

Standardized benchmarks would help:
*   **Validate Claims**: Prevent "cheating" by, for example, running benchmarks on systems with excessive RAM, which is far more expensive than SSDs and not scalable for decentralization <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>.
*   **Foster Innovation**: Allow projects to understand why others perform better and incorporate those ideas, raising the engineering standard of the industry <a class="yt-timestamp" data-t="00:48:16">[00:48:16]</a>.
*   **Promote Rigor**: Move away from intuition-based marketing and towards more rigorous, scientific, and quantitative engineering practices <a class="yt-timestamp" data-t="00:48:58">[00:48:58]</a>.

## Monad's Contribution to the Ethereum Ecosystem

Monad Labs aims to contribute to the [[Performance and scalability of EVM chains | performance and scalability]] of the EVM ecosystem rather than replace Ethereum <a class="yt-timestamp" data-t="00:53:09">[00:53:09]</a>. There is growing recognition within the Ethereum research community that Monad's unique approach of rebuilding the execution stack from the ground up, researching a custom database, and implementing [[Parallelization in blockchain technologies | parallel execution]] and asynchronous execution, are valuable explorations <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>. These are areas where existing Ethereum client teams, focused on other orthogonal problems, haven't had the resources to delve <a class="yt-timestamp" data-t="00:54:06">[00:54:06]</a>.

Ethereum has established the EVM as a powerful bytecode standard with rich tooling and applications, and Monad benefits greatly from this prior work <a class="yt-timestamp" data-t="00:54:20">[00:54:20]</a>. Monad's research and optimizations could potentially be incorporated into Ethereum, pushing the space forward and contributing to the [[Future of high performance and scalable blockchains | future of high performance and scalable blockchains]] <a class="yt-timestamp" data-t="00:54:46">[00:54:46]</a>.

Monad's full EVM compatibility down to the bytecode level means everything functions identically to Ethereum, providing a seamless developer experience without the need for complex changes when porting contracts or using RPCs <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>. This is crucial for developer experience, allowing them to focus on business logic rather than compatibility differences <a class="yt-timestamp" data-t="00:39:47">[00:39:47]</a>.

Ultimately, users value latency and responsiveness <a class="yt-timestamp" data-t="00:39:57">[00:39:57]</a>. While throughput depends on the application, having high throughput is essential for supporting a large user base <a class="yt-timestamp" data-t="00:41:34">[00:41:34]</a>. Monad aims to balance throughput and latency to provide the best user experience <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>.