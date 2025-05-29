---
title: Monads HighPerformance Blockchain Features
videoId: hXxU3epZw9E
---

From: [[thepipeline_xyz]] <br/> 

Monad is an EVM-equivalent L1 blockchain designed from scratch to deliver [[monads_performance_and_transaction_speed | high performance]] and efficiency, serving as a new home for Ethereum applications <a class="yt-timestamp" data-t="01:21:21">[01:21:21]</a>. It targets a vision of the world computer, offering a [[blockchain_scalability_and_highperformance_systems | high-performance]], low-cost system while maintaining decentralization <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

## Key Performance Metrics
Monad aims to provide a [[high_performance_blockchains | high-performance system]] with significant improvements over existing blockchains:
*   **Transaction Speed:** 10,000 *real* Ethereum transactions per second (TPS), not just transfers <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. This is achieved by running the actual Ethereum state through the blockchain <a class="yt-timestamp" data-t="00:49:57">[00:49:57]</a>.
*   **Finality:** Single block times and single slot finality <a class="yt-timestamp" data-t="00:58:14">[00:58:14]</a>. Finality is reached at consensus time <a class="yt-timestamp" data-t="09:48:29">[09:48:29]</a>.
*   **Transaction Costs:** Costs are as low as hundreds of a cent for a UniSwap V2 transaction <a class="yt-timestamp" data-t="01:30:11">[01:30:11]</a>.
*   **Compatibility:** Maintains full EVM RPC compatibility, allowing existing wallets and indexers to work out of the box <a class="yt-timestamp" data-t="01:02:18">[01:02:18]</a>. Developers can port over any contract and tap into existing EVM research and network effects <a class="yt-timestamp" data-t="01:53:07">[01:53:07]</a>.
*   **Decentralization:** Strives for decentralization with hundreds of nodes participating in consensus globally <a class="yt-timestamp" data-t="01:36:34">[01:36:34]</a>, while maintaining reasonable hardware requirements, such as targeting 100 megabits per second internet for a consumer full node <a class="yt-timestamp" data-t="03:03:03">[03:03:03]</a>.

## Addressing Blockchain Bottlenecks
Traditional blockchains face four fundamental constraints:
1.  **Network Bandwidth:** Internet overhead <a class="yt-timestamp" data-t="02:24:26">[02:24:26]</a>.
2.  **CPU Throughput:** Speed of computer cores <a class="yt-timestamp" data-t="02:28:44">[02:28:44]</a>.
3.  **State Access:** Database and historical state of the chain <a class="yt-timestamp" data-t="02:32:14">[02:32:14]</a>.
4.  **State Growth:** Current accounts and their balances <a class="yt-timestamp" data-t="02:38:20">[02:38:20]</a>.

Many blockchains overcome these by increasing bandwidth requirements (e.g., 1 GB or 10 GB connections), centralizing nodes (placing them close together), or increasing RAM requirements, which makes nodes expensive <a class="yt-timestamp" data-t="03:08:18">[03:08:18]</a>. Monad's goal is to maximize commodity hardware efficiency through a new software architecture <a class="yt-timestamp" data-t="04:02:08">[04:02:08]</a>.

## Monad's Key Innovations
Monad's [[monads_key_innovations | high performance]] is rooted in a full scratch redesign of its architecture <a class="yt-timestamp" data-t="03:32:41">[03:32:41]</a>. While keeping the EVM bytecode, Monad rebuilt its consensus, execution engine, and introduced a custom state database <a class="yt-timestamp" data-t="04:41:40">[04:41:40]</a>.

### Asynchronous Execution
Unlike most blockchains that use interleaved execution (where execution and consensus are done in tandem within a block time), Monad implements asynchronous execution <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.
*   **Concept:** This stems from the realization that if you have a deterministic state machine like the EVM, and you know the transaction ordering and data, you don't need to execute to know the results will be the same <a class="yt-timestamp" data-t="06:37:07">[06:37:07]</a>.
*   **Mechanism:** Monad pulls execution out of the current block and runs it in tandem with the *next* block <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. This means ordering the current block while executing the previous block <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>.
*   **Benefits:** This greatly expands the execution budget and gas budget, leading to higher throughput and lower fees <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>. Many [[development_and_technical_innovation_in_blockchains_like_solana_and_monad | blockchains]] are moving in this direction, with proposals in Solana to do the same <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>.

### Parallel Execution
[[monads_performance_and_transaction_speed | Parallel execution]], a hot topic in the blockchain space, involves taking one lane of execution and turning it into multiple lanes, utilizing modern computers' multiple cores <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.
*   **Traditional vs. Monad:** Historically, transactions are linearly ordered and serially executed <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>. Monad maintains the consensus ordering but executes everything in parallel, committing results in the correct order <a class="yt-timestamp" data-t="10:59:00">[10:59:00]</a>.
*   **Optimistic Parallel Execution:** Monad uses optimistic parallel execution (also called software transactional memory or optimistic concurrency control) <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>. It assumes everything can run in parallel, generates pending results, and then re-executes only conflicted transactions with the new state <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.
*   **Efficiency:** The overhead of re-execution is low because the state is already cached <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>. This approach eliminates the need for access lists, reducing bandwidth overhead while providing a familiar EVM interface <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.

### [[monad_db_and_its_role_in_efficient_blockchain_operations | Monad DB]]
The underlying technology that makes [[monads_performance_and_transaction_speed | parallel execution]] truly effective is [[monad_db_and_its_role_in_efficient_blockchain_operations | Monad DB]], a custom state database <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
*   **Role:** [[monad_db_and_its_role_in_efficient_blockchain_operations | Monad DB]] feeds the parallel execution engine by enabling parallel state access <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>. Without it, the system would bottleneck waiting for database lookups for each transaction <a class="yt-timestamp" data-t="15:16:00">[15:16:00]</a>.
*   **Asynchronous I/O (IO_Uring):** It achieves this through asynchronous I/O using kernel technology called IO_Uring <a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a>. This allows Monad to issue many parallel requests to the database, ensuring the system's other parts are not bottlenecked <a class="yt-timestamp" data-t="15:25:00">[15:25:00]</a>.
*   **Native Merkle Patricia Try Storage:** Ethereum logically uses a Merkle Patricia Try (MPT) for succinct verification of transactions and state, allowing quick checks of a root to verify underlying data <a class="yt-timestamp" data-t="17:13:00">[17:13:00]</a>. However, most Ethereum clients use off-the-shelf databases (like B-trees or LSM trees) that are not natively MPTs, leading to inefficient "tree traversal within a tree traversal" <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>.
*   **[[monads_unique_infrastructure_versus_current_blockchain_environments | Monad DB's Innovation]]:** [[monad_db_and_its_role_in_efficient_blockchain_operations | Monad DB]] is a full rebuild of a database where the Merkle Patricia Try is the *actual* way data is stored on disk <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>. This removes the indirection, making data lookups 16 to 32 times more efficient per tree traversal <a class="yt-timestamp" data-t="20:10:00">[20:10:00]</a>. This combined with asynchronous I/O allows for both [[monads_performance_and_transaction_speed | parallel state access]] and parallel execution, which is the "secret sauce" for Monad's performance <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>.

By combining asynchronous execution, optimistic parallel execution, and a custom, MPT-native database like [[monad_db_and_its_role_in_efficient_blockchain_operations | Monad DB]], Monad aims to saturate hardware capabilities and deliver [[blockchain_scalability_and_highperformance_systems | high throughput]] while maintaining decentralization and full EVM compatibility <a class="yt-timestamp" data-t="04:02:08">[04:02:08]</a>.