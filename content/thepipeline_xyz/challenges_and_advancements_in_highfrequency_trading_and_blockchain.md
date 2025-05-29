---
title: Challenges and advancements in highfrequency trading and blockchain
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

The development of high-performance blockchain technology, particularly in the EVM (Ethereum Virtual Machine) ecosystem, has been significantly influenced by concepts and engineering principles derived from high-frequency trading (HFT) systems <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. This article explores the challenges inherent in scaling blockchain performance and the advancements proposed by projects like Monad Labs, drawing parallels with the demanding world of HFT.

## High-Frequency Trading (HFT) and Performance Optimization

Keone and James, founders of Monad Labs, gained extensive experience building full trading systems for high-frequency trading at Jump Trading, later transitioning to Jump Crypto <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This field is characterized by extreme competitiveness and a constant drive for minimal latency <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

In HFT, the goal is to process market data, make rapid trading decisions, and send orders back to exchanges faster than competitors <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. Even nanoseconds of delay can determine success or failure in securing a trade <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. This environment necessitates building highly performant systems from scratch, constantly optimizing and shaving off latency <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

Key aspects of HFT and their relevance to blockchain include:
*   **Extreme Latency Competition:** Small differences in processing speed dictate trade outcomes <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Optimization at the Core:** A constant focus on improving system performance, often involving the creation of custom data structures and avoiding general-purpose libraries <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
*   **Massive Volume with Thin Margins:** Daily notional volumes can reach tens of billions of dollars, with profit margins often less than a basis point per trade <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>. This requires systems capable of handling tens of millions of orders daily across hundreds of instruments <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>.
*   **Deep Hardware Understanding:** Optimizing performance involves a quantitative approach, running experiments, and understanding how code translates to assembly instructions at a low level to maximize hardware capabilities <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>.

This background in [[highfrequency_trading_systems_and_performance_optimization | Highfrequency trading systems and performance optimization]] provided a unique foundation for identifying and tackling performance bottlenecks in [[cryptocurrency_and_blockchain_technology | blockchain technology]] <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

## Blockchain Performance Challenges

Upon entering the crypto space, particularly working with Solana DeFi, it became evident that there was a significant need for more performant blockchains, especially within the EVM ecosystem, which was found to be very inefficient and unoptimized compared to HFT systems <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### The Parallel EVM and Its Limitations

While parallel EVM has become a major narrative in crypto, Monad Labs' early implementation of an optimistic parallel execution algorithm over one and a half years ago revealed that it alone offered limited improvement over serial execution <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. This is because the core bottleneck lies elsewhere <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

Optimistic parallel execution works by running transactions in parallel, generating pending results with input/output records <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. These results are committed in the original transaction order, and if an input is invalidated due to a conflict, the work is re-executed <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. Re-execution is often cheap as inputs are usually cached <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

### State Access: The Primary Bottleneck

The actual bottleneck for performance in blockchains, including Ethereum, is state access <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. Transactions depend on accounts and slots stored on SSDs, and the cost of reading from an SSD is significant (e.g., 80-100 microseconds per read) <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

Standard databases (like Pebble DB, RocksDB, LMDB, and mdbx derivatives) used by Ethereum and other EVM-compatible blockchains to store state do not support efficient parallel access <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. When multiple virtual machines attempt parallel reads, they still bottleneck, effectively leading to single-file execution <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. These general-purpose databases are not optimized for the specific access patterns of a blockchain, resulting in poor performance despite capable hardware <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. This represents a significant challenge in [[challenges_of_standard_databases_in_blockchain_performance | challenges of standard databases in blockchain performance]].

Other key [[challenges_and_propositions_in_blockchain_technology | challenges and propositions in blockchain technology]] identified include:
*   **Cryptographic Functions:** Elliptic curve cryptography and hashing are expensive <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.
*   **Computation vs. State Access:** The computational logic in most smart contracts is relatively cheap compared to state access <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>.
*   **VM Choice Impact:** The choice of VM (EVM, SVM, WASM) makes minor differences in performance <a class="yt-timestamp" data-t="03:37:12">[03:37:12]</a>.
*   **Access Lists:** Counter-intuitively, access lists, intended to improve state prediction, may actually worsen performance due to overhead <a class="yt-timestamp" data-t="03:22:01">[03:22:01]</a>.

## Monad's Advancements and Solutions

Monad Labs addresses these challenges through several key [[technology_advancements_and_infrastructure_in_blockchain | technology advancements and infrastructure in blockchain]] and optimizations:

### 1. Custom State Database

Monad built a custom database from scratch, specifically designed for blockchain state storage <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>. This approach allows them to maximize the performance of modern SSDs (e.g., 500,000 I/O operations per second for a $200 SSD) <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>. By customizing the data structure to known usage patterns, they can extract significantly better performance than general-purpose databases, making far fewer requests to the hardware per lookup <a class="yt-timestamp" data-t="16:27:00">[16:27:00]</a>. This is critical for realizing true performance gains from parallel execution <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

### 2. Optimistic Parallel Execution (with State Access Optimization)

While Monad implemented optimistic parallel execution early on <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>, they recognized that its impact on performance is limited without addressing the underlying state access bottleneck <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. Their innovation lies in combining this algorithm with a highly optimized custom database, which makes re-execution cheap and efficient <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

### 3. Separation of Execution and Consensus

Monad separates execution and consensus, allowing them to operate in parallel <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. In current blockchains like Ethereum, the execution budget within a block is very small (e.g., ~100 milliseconds within a 12-second block, or 1% of the time) <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. By not requiring execution to complete before consensus, Monad provides a much larger time budget for execution, significantly unlocking performance <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. This approach is not a restriction but a relaxation of synchronization, handled deterministically <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

### 4. No Shortcuts Approach

Monad's development philosophy, "no shortcuts," emphasizes fundamental engineering and scientific rigor <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. This means:
*   **Commodity Hardware Focus:** The goal is to run effectively on commodity hardware (e.g., $200 SSDs), avoiding the shortcut of simply requiring expensive, large-RAM machines, which hinders decentralization and scalability <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **Deep Understanding and Experimentation:** Measuring everything, making no assumptions, and constantly experimenting are key <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. This includes micro-optimizations like translation look-aside buffer optimization, even if they only yield small percentage gains, as they accumulate <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   **Building from Scratch:** Developing core components like the database from the ground up to achieve maximum performance <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.
*   **Iterative Development:** Being willing to write and discard code to find the most optimal solutions <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

## Impact and Future Outlook

Monad's approach aims to significantly expand the EVM ecosystem by providing a highly performant and scalable blockchain <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>. By meticulously rebuilding the execution stack, researching custom databases, implementing parallel and asynchronous execution, Monad explores a new, orthogonal direction for blockchain development <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>. This work could ultimately lead to changes being incorporated into Ethereum itself, pushing the entire space forward <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. This aligns with [[evolution_and_impact_of_highperformance_blockchain_technology | evolution and impact of highperformance blockchain technology]] and [[future_developments_in_crypto_and_blockchain_technology | future developments in crypto and blockchain technology]].

A critical step for ensuring transparency and progress in the industry is the establishment of standardized benchmarks <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. Currently, claims of high TPS (transactions per second) lack context, as the complexity of transactions (e.g., simple token transfers vs. complex Uniswap or borrowing protocol interactions) can drastically alter performance figures <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. Monad plans to release a publicly available GitHub repository with benchmarks, likely using recent Ethereum history as a standard, to allow for verifiable and replicable performance comparisons <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. This initiative aims to bring more rigor and scientific practice to the blockchain industry, moving beyond intuition and marketing claims <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>. This will also facilitate more meaningful [[discussion_on_high_throughput_blockchains | Discussion on high throughput blockchains]].

The goal is to enable a blockchain capable of handling the scale of traditional finance, supporting interactions like fully on-chain limit order books with sub-cent fees and thousands of orders per second <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>. Ultimately, users value responsiveness and low latency, and while throughput depends on the application, a high throughput is essential for broad user adoption <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.