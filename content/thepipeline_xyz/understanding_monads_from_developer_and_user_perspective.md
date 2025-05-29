---
title: Understanding Monads from Developer and User Perspective
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

[[introduction_to_monad_and_its_community | Monad]] is a blockchain project often heard about online as a "parallel EVM," but it encompasses more than just that concept <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. It represents a full scratch redesign that visually resembles Ethereum, offering a complete EVM L1 equivalent blockchain <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Monad: A User Perspective

From a user's perspective, [[introduction_to_monad_and_its_community | Monad]] is a platform where Ethereum applications can find a home and realize the vision of a "world computer" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. It aims to be a high-performance, low-cost system, with transactions like a Uniswap V2 transaction costing hundreds of a cent <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. [[introduction_to_monad_and_its_community | Monad]] also strives to maintain decentralization, involving hundreds of nodes globally participating in consensus while keeping reasonable hardware requirements <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Monad: A Developer Perspective

For developers, [[introduction_to_monad_and_its_community | Monad]] functions as a fully EVM-equivalent L1 blockchain <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This means developers can easily port over existing contracts and leverage the established EVM research and network effect <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The experience of developing on [[introduction_to_monad_and_its_community | Monad]] is designed to feel the same as developing on an EVM, but with the benefit of a high-performance system <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

Key features for developers include:
*   High performance, targeting 10,000 *real historical Ethereum transactions* per second, not just transfers <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   Single block times and single slot finality <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   Full EVM RPC compatibility, ensuring that existing wallets, indexers, and other tools work out-of-the-box <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## How Monad Achieves Its Performance

[[performance_improvements_with_monads_technology | Monad]]'s capabilities stem from a fundamental redesign of its software architecture <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. The project focuses on getting the most out of commodity hardware by designing software that saturates hardware through various bottlenecks, while preserving decentralization through reasonable RAM requirements and a globally distributed network of hundreds of nodes <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

The core components of this new architecture include:
*   A fully rebuilt consensus mechanism <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   A fully rebuilt execution engine <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   Implemented parallel execution <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   A custom state database called Monad DB <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Asynchronous Execution

Most blockchains today use "interleaved execution," where execution and consensus are performed in tandem within a block time <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. For example, in Ethereum's 12-second block time, execution might take only 1% of the time, with consensus taking significantly longer due to global node communication <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

Asynchronous execution in [[technical_details_on_monads_highperformance_features | Monad]] stems from the realization that execution can be pulled out of consensus <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Since the EVM is a deterministic state machine and the ordering and data of transactions are known, the results will always be the same <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This allows [[technical_details_on_monads_highperformance_features | Monad]] to:
*   Order the current block while simultaneously executing the previous block <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   Come to consensus on data and its order, then execute it <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   Work on two blocks in parallel <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

This approach greatly expands the execution budget, which translates to a higher gas budget, leading to higher throughput and lower fees <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Despite the delayed execution, finality occurs at consensus time because the deterministic nature of the EVM ensures the outcome is known once the order and data are agreed upon <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### Parallel Execution

[[technical_details_on_monads_highperformance_features | Monad]]'s parallel execution takes a single processing lane and turns it into multiple lanes, utilizing modern computers' multiple cores <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Traditionally, transactions are linearly ordered and serially executed <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. [[technical_details_on_monads_highperformance_features | Monad]] aims to maintain the order provided by consensus but execute everything in parallel to get results much quicker <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

This is achieved through "optimistic parallel execution," also known as software transactional memory or optimistic concurrency control <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. The process is:
1.  Assume everything can be run in parallel, starting from a synced view of the world <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
2.  Generate a batch of pending results <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
3.  Commit these pending results in order <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
4.  If a pending result relied on a previous one that caused a conflict (e.g., changed the starting state), re-execute it with the new state <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

Although re-execution might seem inefficient, it is cheap because the state is already cached, and the most time-consuming part of a transaction is pulling state from the database, not the execution itself <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. Crucially, due to the serial commitment process, a transaction is never executed more than once <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. This model also eliminates the need for developers to deal with access lists, which simplifies development and reduces bandwidth overhead <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

### Monad DB

[[technical_details_on_monads_highperformance_features | Monad DB]] is a custom-built state database that makes Ethereum state native to how Ethereum works logically <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. Its primary role is to feed and saturate the parallel execution engine by enabling parallel state access <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. Without asynchronous I/O and parallel state access, the system would bottleneck waiting for database lookups, even with parallel execution <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

Modern SSDs offer high bandwidth (e.g., a million I/O operations per second for about $200), though lookups still take milliseconds compared to nanoseconds for RAM <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. The key is to saturate this memory bandwidth by constantly pulling things out of state in parallel <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

Ethereum stores its state in a Merkel Patricia Trie (MPT), which is a tree structure <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. The MPT is philosophically central to Ethereum as it allows for succinct verification of transactions and state. This means one can check the root of the tree to verify all data beneath it, unlike other blockchains that might require downloading and re-executing an entire block to verify a transaction <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.

The challenge is that no existing databases are natively built as MPTs; they typically use B-trees or LSM trees <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. This creates an inefficiency: when traversing the logical MPT in Ethereum, the system has to perform multiple lookups (16 to 32 times more overhead) within a different underlying database structure <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

[[technical_details_on_monads_highperformance_features | Monad DB]] addresses this by being a full rebuild of a database where the Merkel Patricia Trie is the actual way data is stored on disk <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. This removes the "tree indirection" and allows for 16 to 32 times fewer lookups per tree traversal <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. Combined with asynchronous I/O (using kernel technology like IOU ring), [[technical_details_on_monads_highperformance_features | Monad DB]] can issue many parallel lookups simultaneously, feeding data back into the parallel execution engine <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. This parallel state access, alongside parallel execution, is the "secret sauce" that makes [[technical_details_on_monads_highperformance_features | Monad]]'s high performance possible <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.