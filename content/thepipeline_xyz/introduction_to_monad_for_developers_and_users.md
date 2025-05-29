---
title: Introduction to Monad for Developers and Users
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

[[understanding_the_concept_of_monad | Monad]] is a blockchain designed as a redesign from scratch, looking similar to Ethereum in shape, providing a full EVM L1 equivalent experience <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While often known as a "parallel EVM," it encompasses much more <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Monad from a Developer Perspective

For developers, [[understanding_the_concept_of_monad | Monad]] is a fully EVM-equivalent L1 blockchain <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. It allows developers to easily port over any existing contracts and tap into the existing EVM research and network effect <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

Key features for developers include:
*   **High Performance**: Aims for 10,000 transactions per second (TPS), referring to real historical Ethereum transactions, not just transfers <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This is achieved by running Ethereum state through the blockchain <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Single Block Times and Single Slot Finality**: Provides developers with rapid transaction finality <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Full EVM RPC Compatibility**: Anything developers are used to working with, such as wallets and indexers, works out of the box <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## Monad from a User Perspective

From a user's perspective, [[understanding_the_concept_of_monad | Monad]] serves as a platform where Ethereum applications can find a home and realize the vision of a "world computer" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

Key benefits for users include:
*   **High Performance and Low Cost**: Transactions are very inexpensive, costing hundreds of a cent for a Uniswap V2 transaction <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Decentralization**: [[understanding_the_concept_of_monad | Monad]] maintains decentralization with hundreds of nodes participating in consensus globally <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Reasonable Hardware Requirements**: This decentralization is achieved while maintaining reasonable hardware requirements for nodes <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## How Monad Achieves its Goals

[[understanding_the_concept_of_monad | Monad]] addresses fundamental constraints in distributed systems by designing software that maximizes the utility of commodity hardware while preserving decentralization <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### Blockchain Bottlenecks and Traditional Approaches

Four fundamental constraints in a blockchain are:
1.  **Network Bandwidth**: Internet overhead <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
2.  **CPU Throughput**: Speed of computer cores <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
3.  **State Access**: Database and historical state of the chain <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
4.  **State Growth**: Current accounts and their balances <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

Before [[understanding_the_concept_of_monad | Monad]], many blockchains achieved properties by taking shortcuts, such as:
*   Requiring very high internet connections (e.g., 1 GB or 10 GB vs. Monad's target of 100 megabits per second for a consumer full node) <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   Placing all nodes close together to reduce latency <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   Increasing RAM requirements, making nodes very expensive <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Monad's New Software Architecture

[[understanding_the_concept_of_monad | Monad]] employs a new software architecture that is a full redesign, retaining only the EVM bytecode (instructions for how the EVM interprets code) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This architecture includes:
*   A fully rebuilt consensus <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   A fully rebuilt execution engine <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   Implemented [[development_journey_of_monad | parallel execution]] <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   A custom state database called Monad DB <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Asynchronous Execution

Most blockchains today use "interleaved execution," where execution and consensus are done in tandem within a block time <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. For example, in Ethereum, execution might take 1% of the 12-second block time, with consensus taking significantly longer due to global node communication <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

[[understanding_the_concept_of_monad | Monad]] realizes that with a deterministic state machine like the EVM, where the ordering and data of transactions are known, execution can be pulled out of the current block and done in tandem with the *next* block <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This means:
*   The current block is ordered while the previous block is being executed <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   Nodes come to consensus on transaction ordering *prior* to execution <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   They work on two blocks in parallel <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   Execution can take up the entire block time, not constrained by consensus time <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

This approach greatly expands the "gas budget," leading to higher throughput and lower fees <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Finality in [[understanding_the_concept_of_monad | Monad]] occurs at consensus time; a full node can run transactions locally as soon as consensus is reached for immediate state updates <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### Parallel Execution

[[development_journey_of_monad | Parallel execution]] in [[understanding_the_concept_of_monad | Monad]] transforms a single processing lane into multiple lanes, leveraging modern multi-core CPUs <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. While traditional blockchains execute transactions linearly and serially, [[understanding_the_concept_of_monad | Monad]] maintains the consensus-given ordering but executes everything in parallel to get results quicker, then commits them in the original order <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

[[understanding_the_concept_of_monad | Monad]] uses **optimistic parallel execution** (also known as Software Transactional Memory or Optimistic Concurrency Control) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>:
1.  Start with a synced view of the world <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
2.  Assume everything can run in parallel and generate pending results <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
3.  Walk through the pending results in order, attempting to commit them <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
4.  If a pending result relied on a previous one that changed, re-execute it with the new state <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

The overhead of re-execution is low because the state is cached, and fetching state from the database is the most time-consuming part, not the execution itself <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. This model eliminates the need for access lists, reducing bandwidth overhead and providing a familiar EVM interface with parallel backend performance <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

### Monad DB (Custom State Database)

[[development_journey_of_monad | Monad DB]] is a custom state database that makes [[understanding_the_concept_of_monad | Monad]]'s [[development_journey_of_monad | parallel execution]] truly possible <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. It feeds the parallel execution engine by allowing parallel state access <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

The core challenge Monad DB addresses relates to how Ethereum stores state:
*   Ethereum uses a Merkel Patricia Trie (MPT) for state, which allows for succinct verification of transactions and state <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
*   Other Ethereum clients typically use off-the-shelf backend databases (like B-trees or LSM trees) to store this MPT, which are not themselves MPTs <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
*   This creates a "tree traversal within a tree traversal" problem: when traversing the logical MPT, the system has to perform multiple lookups (16 to 32 times more overhead) in the physical, non-MPT backend database <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.

[[development_journey_of_monad | Monad DB]] is a full rebuild of a database where the Merkel Patricia Trie is the *actual* way data is stored on disk <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. This removes the entire "tree indirection," resulting in 16 to 32 times fewer lookups per tree traversal <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

Combined with asynchronous I/O (using `IO_Uring` kernel technology), [[development_journey_of_monad | Monad DB]] can issue many parallel requests to the database, ensuring that the parallel execution engine is constantly saturated with data <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. This parallel state access, alongside [[development_journey_of_monad | parallel execution]], is the "secret sauce" behind [[understanding_the_concept_of_monad | Monad]]'s performance <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>.

<div class="callout note">
The consensus mechanism, while a rebuilt component of Monad's architecture, was not covered in detail in this discussion <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
</div>