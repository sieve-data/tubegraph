---
title: Parallel EVM and its impact on crypto
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

The concept of a [[parallel_evm_and_technological_advancements_in_blockchain | Parallel EVM]] has become a significant topic in the [[crypto_ecosystem_developments | crypto ecosystem]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Despite growing interest and claims from various teams, there's often a lack of clear, reliable information regarding its true impact and the necessary optimizations for achieving substantial performance gains <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Monad Labs, founded by Keone and James who previously worked together at Jump Trading and Jump Crypto, has been a pioneer in this field, having pushed the first [[parallel_evm_and_technological_advancements_in_blockchain | parallel EVM]] algorithm over a year and a half ago <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Monad's Optimistic Parallel Execution

Monad's approach to [[parallel_evm_and_technological_advancements_in_blockchain | parallel EVM]] is based on an optimistic parallel execution algorithm <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. In this model, transactions within a block are linearly ordered, with the objective of reaching the final state as if they were executed sequentially, but in a shorter timeframe <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

The algorithm functions as follows:
1.  **Parallel Execution**: A batch of transactions is run in parallel, generating pending results <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
2.  **Record Keeping**: Each pending result includes a record of the inputs and outputs for its respective transaction <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
3.  **Ordered Commitment**: These pending results are then committed in the original order of transactions <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
4.  **Conflict Resolution**: If, during commitment, an input for a pending result is found to be invalidated, the associated transaction is re-scheduled for execution, and no further commitments occur until it's re-executed <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

This method, also known as optimistic concurrency control, is relatively simple and intuitive <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Re-execution due to conflicts is typically efficient, as necessary inputs are often already in the cache, requiring only a simple cache lookup <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## The Bottleneck: State Access

Despite the apparent simplicity and elegance of [[parallel_evm_and_technological_advancements_in_blockchain | parallel EVM]], Monad's early implementation revealed that it offered little improvement over serial execution <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The primary bottleneck was identified as **state access** <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

Transactions rely on accessing accounts and storage slots, which are typically stored on SSDs in Ethereum <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The cost of reading from an SSD is significant <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Furthermore, the databases commonly used by Ethereum and other [[evm_compatibility_and_its_impact_on_developers | EVM compatible]] blockchains (like Pebble DB or RocksDB) do not natively support parallel access <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This means that even with multiple virtual machines running in parallel, all read requests still bottleneck at the database, effectively resulting in single-file execution <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

> "The actual bottleneck is State access... The databases that Ethereum and other blockchains that [[evm_compatibility_and_its_impact_on_developers | EVM compatible]] use to store that state do not support parallel access." <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>

### Monad's Solution: Custom State Database

Recognizing state access as the true bottleneck, Monad focused on building a **custom state database** <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Standard general-purpose databases like RocksDB or LMDB are not optimized for the specific access patterns of blockchain state <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

James, Monad's CTO and the architect behind their database, highlights that the most expensive parts of blockchain operations are cryptography, hashing, and state access <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Simple smart contract logic is relatively cheap to execute <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. A single read from an SSD can take 80-100 microseconds or more, orders of magnitude longer than executing a simple smart contract <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. Multiple sequential reads for sender accounts, destination accounts, proxy accounts, or storage slots (like ERC-20 balances) quickly add up <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

A "shortcut" would be to simply throw more RAM at the problem, requiring very expensive hardware <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. However, modern SSDs are incredibly performant, offering hundreds of thousands of I/O operations per second for an affordable price <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. The issue lies in inefficient software utilization of this hardware <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

Monad's custom database is designed specifically for blockchain state access, avoiding common pitfalls like embedding one data structure inside another on disk, which creates expensive, multi-traversal operations <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. By customizing the data structure to the exact use case, Monad can extract significantly more performance from the hardware <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. For instance, Monad's database may only require one or two requests to look up an account, compared to potentially 20 requests for other data structures not in cache <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This deep optimization ensures that commodity hardware can achieve high performance <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.

### Separation of Execution and Consensus

Another key optimization by Monad is the **separation of execution and consensus** <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. Unlike traditional models where execution must complete before consensus can proceed, Monad relaxes this synchronization <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. This allows execution and consensus to run in parallel, providing more time for both processes <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.

In Ethereum, with 12-second block times, the actual budget for execution is only about 100 milliseconds, roughly 1% of the total block time <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. This severely limits the gas limit and the amount of work that can be done per block <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. By moving execution out of the prerequisite path for consensus and running it in parallel to the next round of consensus, Monad unlocks a massive budget for execution <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. This approach doesn't restrict leaders who wish to execute transactions before proposing a block; it simply offers a greater budget for everyone else to run them in parallel <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.

## "No Shortcuts" Philosophy

Monad's development ethos is encapsulated by the tagline "no shortcuts" <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>. This means:
*   **Commodity Hardware Focus**: Instead of relying on expensive, high-end hardware, Monad builds systems that perform optimally on commodity hardware, making network participation more accessible and cost-effective <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.
*   **Deep Optimization**: Drawing from their background in high-frequency trading (HFT), where shaving off nanoseconds means winning opportunities, Monad applies hyper-optimization techniques to every component <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. This includes micro-optimizations, such as optimizing the translation lookaside buffer (TLB) for virtual-to-physical address translation, even if it yields only small percentage gains <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>.
*   **Quantitative and Scientific Approach**: Development is driven by rigorous measurement, experimentation, and a deep understanding of hardware behavior, even down to assembly instructions <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>. Assumptions, like the intuitive idea that access lists are always better, are rigorously tested and often found to be incorrect <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>.
*   **Iterative Development**: Teams must be willing to write, rewrite, and discard code as part of the engineering process to achieve optimal performance <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>.

This meticulous, ground-up approach takes significant time and investment <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>.

## [[evm_compatibility_and_its_impact_on_developers | EVM Compatibility]] and Developer Experience

Monad is committed to full [[evm_compatibility_and_its_impact_on_developers | EVM compatibility]] down to the bytecode level, ensuring that everything functions exactly the same as on Ethereum <a class="yt-timestamp" data-t="00:36:24">[00:36:24]</a>. This stands in contrast to some chains that claim [[evm_compatibility_and_its_impact_on_developers | EVM compatibility]] but have "hiccups" or differences in contract execution or RPC, creating obstacles for developers <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.

Monad believes that the [[EVM and Move integration in blockchain development | EVM]] itself is a robust standard, and differences between VMs like SVM or WASM are often minor, not providing intrinsic special capabilities <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>. The focus should be on consistent tooling and developer experience <a class="yt-timestamp" data-t="00:39:05">[00:39:05]</a>. When developers don't have to worry about compatibility issues, they can focus more on business logic and building for the end-user <a class="yt-timestamp" data-t="00:39:47">[00:39:47]</a>.

Users, on the other hand, primarily value responsiveness and low latency <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. While throughput is important for supporting many users, it might not directly impact an individual user in all applications <a class="yt-timestamp" data-t="00:41:34">[00:41:34]</a>. Monad aims to balance throughput and latency to provide the best user experience <a class="yt-timestamp" data-t="00:41:53">[00:41:53]</a>.

## The Need for Standard Benchmarks

A significant challenge in the [[crypto_ecosystem_developments | crypto ecosystem]] is the lack of standardized benchmarks, making it difficult to assess true performance gains and verify claims <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>. Monad advocates for open, reproducible benchmarks <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>.

Monad internally uses **replaying Ethereum history** as its primary benchmark <a class="yt-timestamp" data-t="00:45:08">[00:45:08]</a>. This provides context to TPS (Transactions Per Second) claims, as "TPS" can mean vastly different things (e.g., simple token transfers vs. complex Uniswap or borrowing protocol transactions) <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>. An unoptimized client can achieve 50k TPS for basic token transfers from early Ethereum history, making high TPS numbers for simple operations less impressive <a class="yt-timestamp" data-t="00:45:57">[00:45:57]</a>.

Monad plans to build a publicly available GitHub repository where users can download and replicate benchmarks for their chain and others <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>. This promotes rigor in the industry, allowing for informed scientific and engineering decisions, and fosters collaboration by enabling others to identify and incorporate optimizations <a class="yt-timestamp" data-t="00:48:13">[00:48:13]</a>. It also helps expose "cheating" in benchmarks, such as jacking up RAM requirements, which are not scalable or decentralized <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>.

## Contribution to the Ethereum Ecosystem

Monad's mission is not to "kill Ethereum" but to meaningfully contribute to and expand the [[EVM compatibility and its impact on developers | EVM]] ecosystem <a class="yt-timestamp" data-t="00:53:09">[00:53:09]</a>. The Ethereum research community increasingly recognizes the value of Monad's unique approach: rebuilding the execution stack from the ground up, researching custom databases, and implementing [[optimizations in EVM implementations | asynchronous execution]] and [[parallel_evm_and_technological_advancements_in_blockchain | parallel execution]] <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.

Monad benefits from the rich tooling, applications, and applied cryptography research within the existing [[EVM and Move integration in blockchain development | EVM]] context <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>. By exploring new, orthogonal directions and pushing the boundaries of what's possible, Monad aims to advance the space forward. Potential future changes and [[optimizations in EVM implementations | optimizations]] developed by Monad could even be incorporated back into Ethereum, further enriching an already diverse and powerful [[crypto_ecosystem_developments | crypto ecosystem]] <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a>.

> "Monad has benefited a lot from all of the work that has come before and we're exploring in a new orthogonal direction that we think will ultimately help push the space forward." <a class="yt-timestamp" data-t="00:54:36">[00:54:36]</a>

## Future Applications

The high performance capabilities offered by Monad are expected to enable entirely new applications in the crypto space, such as fully on-chain limit order books <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>. To support such demanding applications, the blockchain needs to handle sub-cent fees for order submissions and cancellations, and support thousands of orders per second <a class="yt-timestamp" data-t="00:28:41">[00:28:41]</a>. This level of infrastructure is crucial for traditional financial institutions to engage with decentralized finance, leveraging features like self-custody and composability at scale <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>.

Ultimately, Monad's work underscores that true performance gains in [[parallel_evm_and_technological_advancements_in_blockchain | parallel EVM]] and blockchain technology require not just theoretical algorithms but a comprehensive suite of highly focused, ground-up [[optimizations in EVM implementations | optimizations]], particularly at the state database level, coupled with rigorous engineering principles and a commitment to open, standardized benchmarks.