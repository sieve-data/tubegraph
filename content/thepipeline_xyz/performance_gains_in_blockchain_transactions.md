---
title: Performance gains in blockchain transactions
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

The discussion around [[parallel_evm_and_blockchain_optimizations | Parallel EVM and blockchain optimizations]] has become a significant narrative in the crypto space, with many teams claiming to work on their own iterations <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. However, there's often a lack of reliable information regarding the true impact of Parallel EVM and other essential optimizations needed to achieve significant performance gains <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Optimistic Parallel Execution

Monad Labs developed its optimistic parallel execution algorithm over a year and a half ago <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. In Monad, transactions are linearly ordered within a block, aiming to reach the final state as if transactions were run sequentially, but completing the work in a shorter time <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

The algorithm functions as follows:
1.  Multiple transactions are run in parallel, generating pending results <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  Each pending result records the inputs and outputs for that transaction <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
3.  These pending results are committed in the original order of transactions <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
4.  If a pending result encounters an invalidated input, the work is rescheduled, and commitment pauses until re-execution <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

This re-execution due to conflicts is typically inexpensive because needed inputs are almost always in cache, allowing for a simple cache lookup <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### The True Bottleneck: State Access

Despite implementing optimistic parallel execution, Monad found that it yielded little improvement compared to serial execution <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The primary bottleneck identified was state access <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
Transactions depend on accounts and slots within those accounts, and this state is stored on an SSD in Ethereum <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The cost of reading from an SSD is significant <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Furthermore, the databases used by Ethereum and other EVM-compatible blockchains do not support parallel access <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This means that even with multiple virtual machines running in parallel, they still bottleneck on database reads, effectively resulting in single-file execution <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

This revelation highlighted that [[parallelization_in_blockchain_technologies | parallelization in blockchain technologies]] alone doesn't guarantee significant performance gains; the core issue lies in optimizing state access, particularly at the database level <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

> "Paralyzing computation by itself doesn't really gain that much." <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>

## Monad's Approach to Optimization

Monad's inspiration to build a more performant blockchain stemmed from experience in high-frequency trading (HFT) at Jump Trading <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. The HFT environment, being super latency-competitive, involved constantly improving systems to shave off milliseconds <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This background provided a perfect fit for tackling the [[need_for_performant_blockchain | need for a more performant blockchain]], especially for the EVM, which had not been optimized to the same degree as HFT systems <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### Custom State Database

The crucial component enabling [[parallel_evm_and_blockchain_optimizations | parallel EVM and blockchain optimizations]] to yield true performance gains is a custom database <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. Standard databases like PebbleDB or RocksDB are general-purpose <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

The most expensive parts of blockchain operations are cryptography functions (e.g., elliptical curve cryptography, hashing) and state access <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Even complex smart contract logic is relatively cheap to execute compared to reading from disk <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. A single read from an SSD can have a latency of 80-100 microseconds, which is orders of magnitude longer than executing a simple smart contract <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

Blockchain clients using standard databases can suffer from poor performance because they often embed one data structure inside another on disk, leading to expensive, multi-traversal operations for each request <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. General-purpose data structures are designed to be performant on average, but not for specific, highly optimized tasks <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

Monad's custom database is designed to extract maximum performance from modern SSDs, which are capable of 500,000 I/O operations per second (IOPS) <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. By customizing the data structure to the specific way the data is used and stored in a blockchain, Monad can achieve significantly better performance <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. This means making a tenth or a twentieth of the requests to hardware compared to other clients <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

### Separation of Execution and Consensus

Another key optimization is separating execution and consensus <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. If execution is not required to complete before consensus, both can run in parallel, providing more time for each process <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. This is not a restriction but a relaxation of synchronization <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

In Ethereum, with 12-second block times, the budget for execution is roughly 100 milliseconds, or about 1% of the total block time <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. This severely limits the gas limit and the amount of work that can be done <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. Moving execution out of being a prerequisite for consensus and running it in parallel to the next consensus round massively unlocks execution potential <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### The "No Shortcuts" Philosophy

Monad's "no shortcuts" philosophy emphasizes deeply understanding and optimizing every aspect of the system <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>. A common shortcut is to simply "throw a bunch of hardware" at the problem, such as requiring large amounts of RAM <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. While this can increase performance, it makes it harder and more expensive for regular people to participate in the network, hindering decentralization <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.

Monad aims to run on commodity hardware, like a $200 modern SSD, which is capable of immense performance if properly leveraged <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. Many small optimizations, such as optimizing translation look-aside buffers or examining assembly instructions, cumulatively add up to significant speed-ups <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>.

> "You have to do the work, right? You have to do the fundamental sort of engineering and the fundamental science and make informed decisions." <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>

This involves extensive quantitative experimentation, measuring everything, and making no assumptions. For example, the common assumption that access lists are beneficial for parallel execution might not be true; internal work suggests they could even be strictly worse <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.

## Benchmarking and Standardization

Accurate information on performance gains in blockchain is difficult to obtain due to a lack of standard benchmarks <a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a>. Anyone can claim any TPS (transactions per second) number without being held accountable <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>.

### Challenges in Metrics (TPS)

The term "TPS" itself can be misleading <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>. It's crucial to define what kind of transactions are being measured <a class="yt-timestamp" data-t="00:45:48">[00:45:48]</a>. An unoptimized client can already achieve 50k TPS for simple token transfers, making a claim of 200k TPS for such transfers less impressive without context <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>. This highlights the [[differences_in_blockchain_transaction_metrics | Differences in blockchain transaction metrics]].

### Monad's Proposed Solution

Monad has internally used replaying recent Ethereum history as its benchmark <a class="yt-timestamp" data-t="00:45:08">[00:45:08]</a>. Their plan is to release a publicly available GitHub repository where users can download and replicate benchmarks for Monad and other chains <a class="yt-timestamp" data-t="00:46:24">[00:46:24]</a>.

This open approach to benchmarking fosters progress in the technology by allowing others to:
*   Verify claims and identify areas for improvement <a class="yt-timestamp" data-t="00:46:52">[00:46:52]</a>.
*   Understand specific configurations that yield better performance <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.
*   Prevent "cheating" benchmarks by using excessive, non-commodity hardware like 256GB of RAM, which is two orders of magnitude more expensive than equivalent SSD storage <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>.

This standardization will bring more rigor to the industry, moving away from intuition-based marketing claims toward scientific and engineering practices <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>.

## User Experience and EVM Compatibility

Users generally value latency and responsiveness <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. While throughput is important for supporting a large number of users, individual user experience often prioritizes how quickly a transaction confirms or a page loads <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>. There is often a trade-off between throughput and latency in computer science, and Monad aims to strike the best balance for user experience <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.

Monad is EVM compatible down to the bytecode level <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>. This ensures that everything functions identically to Ethereum, allowing direct deployment of contracts and consistency in RPCs <a class="yt-timestamp" data-t="00:36:25">[00:36:25]</a>. The choice of VM (EVM vs. SVM, WASM, etc.) makes minor differences in performance <a class="yt-timestamp" data-t="00:37:12">[00:37:12]</a>. The EVM is a powerful bytecode standard with rich tooling and applied cryptography research <a class="yt-timestamp" data-t="00:54:20">[00:54:20]</a>. Full compatibility prioritizes developer experience, allowing them to focus on business logic rather than worrying about system differences <a class="yt-timestamp" data-t="00:39:38">[00:39:38]</a>.

Monad contributes to the EVM ecosystem by exploring new, orthogonal directions like rebuilding the execution stack from the ground up, researching custom databases, and implementing asynchronous execution <a class="yt-timestamp" data-t="00:54:39">[00:54:39]</a>. These [[technical_challenges_and_solutions_in_blockchain_performance | Technical challenges and solutions in blockchain performance]] push the boundaries of what's possible, potentially leading to future incorporations into Ethereum <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a> and driving the [[future_of_high_performance_and_scalable_blockchains | future of high performance and scalable blockchains]]. The journey of Monad and the [[performance_and_scalability_of_evm_chains | performance and scalability of EVM chains]] illustrates the [[challenges_and_opportunities_in_blockchain_scalability | challenges and opportunities in blockchain scalability]] and the [[comparison_of_different_database_structures_for_blockchain_efficiency | comparison of different database structures for blockchain efficiency]] in achieving higher performance.