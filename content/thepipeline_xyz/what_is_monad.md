---
title: What is Monad
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

[[introduction_to_monad_and_its_capabilities | Monad]] is a full-scratch redesign of a blockchain that aims to combine high performance with full EVM compatibility and decentralization <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Overview
### From a Developer Perspective
[[introduction_to_monad_and_its_capabilities | Monad]] is a full EVM L1 equivalent blockchain <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Developers familiar with EVM will find it feels the same to work with, but it offers access to a high-performance system <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. It maintains full EVM RPC compatibility, meaning existing wallets and indexers should work out of the box <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Developers can port over any existing contract and tap into the EVM research and network effect <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### From a User Perspective
[[introduction_to_monad_and_its_capabilities | Monad]] is a platform where Ethereum applications can find a home and realize the vision of a "world computer" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. It is designed as a high-performance, low-cost system, with transactions like Uniswap V2 costing hundreds of a cent <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Key Features
*   **High Performance**
    *   10,000 real Ethereum transactions per second <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
    *   Single block times and single slot finality <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Full EVM Compatibility**
    *   Looks very similar to Ethereum in shape <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
    *   Maintains full EVM RPC compatibility <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Decentralization**
    *   Aims to stay true to decentralization with hundreds of nodes participating in consensus globally <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   Maintains reasonable hardware requirements for nodes <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. For a consumer full node, the target internet requirement is about 100 megabits per second <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Addressing Blockchain Bottlenecks
[[introduction_to_monad_and_its_capabilities | Monad]] addresses four fundamental constraints in a blockchain <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>:
1.  **Network Bandwidth:** Internet overhead <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
2.  **CPU Throughput:** How fast computer cores can run <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
3.  **State Access:** Database and historical state of the chain <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
4.  **State Growth:** Current accounts, balances, and the ability to retrieve them <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

Many blockchains take "shortcuts" to achieve certain properties, such as requiring very high internet connections (1 GB or 10 GB), placing all nodes physically close together, or increasing RAM requirements, which makes nodes expensive <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

[[introduction_to_monad_and_its_capabilities | Monad]]'s goals are to get the most out of commodity hardware, design software that saturates hardware through all bottlenecks, and preserve decentralization with reasonable RAM requirements and a globally distributed network of hundreds of nodes <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## [[introduction_to_monad_and_its_capabilities | Monad]]'s Architectural Innovations
[[introduction_to_monad_and_its_capabilities | Monad]] utilizes a new software architecture that is a full redesign <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. The only part kept from the EVM was its bytecode (instructions), while consensus, the execution engine, parallel execution, and the custom State database (Monad DB) were rebuilt <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Asynchronous Execution
Unlike typical blockchains that use "interleaved execution" where execution and consensus are done in tandem within a block time (e.g., Ethereum's 12-second block time, where execution is only about 1% of the time and consensus takes much longer) <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, [[introduction_to_monad_and_its_capabilities | Monad]] employs asynchronous execution <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

Asynchronous execution stems from the realization that if you have a deterministic state machine like the EVM, and you know the transaction ordering and data, you don't need to execute to know the results will always be the same <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This allows [[introduction_to_monad_and_its_capabilities | Monad]] to pull execution out of the current block and run it in parallel with the next block's ordering process <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

This means nodes come to consensus on transaction ordering *prior* to execution, working on two blocks in parallel <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This greatly expands the execution and gas budget, leading to higher throughput and lower fees <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Finality is achieved at consensus time, as a full node can run transactions locally as soon as consensus is reached <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### Parallel Execution
[[introduction_to_monad_and_its_capabilities | Monad]] implements parallel execution to utilize modern computers' multiple cores, effectively turning "one lane into multiple lanes" <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Traditionally, transactions are linearly ordered and serially executed <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. [[introduction_to_monad_and_its_capabilities | Monad]] maintains this ordering but executes everything in parallel using **optimistic parallel execution** (also known as software transactional memory or optimistic concurrency control) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

How it works:
1.  Assume everything can run in parallel and generate pending results <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
2.  Walk through the pending results in order, attempting to commit them <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
3.  If a pending result relied on a previous one that changed, re-execute it with the new state <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

The algorithm ensures a transaction is never executed more than once *serially* during the commit phase <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. The overhead of re-execution is low because the state is cached, and reading data from disk is the most time-consuming part, not the execution itself <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. This model also eliminates the need for access lists, reducing bandwidth overhead for developers <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

### [[introduction_to_monad_and_its_capabilities | Monad DB]] (The Secret Sauce)
[[introduction_to_monad_and_its_capabilities | Monad DB]] is a custom state database that makes Ethereum state native to how Ethereum works logically <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. It feeds the parallel execution engine by enabling parallel state access <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. Without it, parallel execution would be bottlenecked by waiting for data to be pulled from the database for each transaction <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. [[introduction_to_monad_and_its_capabilities | Monad DB]] achieves this with asynchronous I/O, allowing many requests to be issued in parallel <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.

Traditional Ethereum clients often use off-the-shelf databases (like b-trees or LSM trees) to store the Merkel Patricia Trie (MPT), which is Ethereum's logical state structure for succinct verification <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>. This creates a "tree traversal within a tree traversal," where traversing the MPT logically requires multiple lookups in the underlying, differently structured physical database, leading to 16 to 32 times more overhead <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

[[introduction_to_monad_and_its_capabilities | Monad DB]] fully rebuilds the database so that the Merkel Patricia Trie is the *actual* way data is stored on disk <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. This removes the indirection and significantly reduces lookups per traversal <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. Combined with asynchronous I/O (using a kernel technology called IOU ring) <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>, [[introduction_to_monad_and_its_capabilities | Monad DB]] enables parallel state access, which is crucial for saturating and making parallel execution truly effective <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.

---
If you have further questions or want to learn more, you can reach out via the [[introduction_to_monad_and_its_capabilities | Monad]] account on Twitter or Telegram <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>.