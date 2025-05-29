---
title: Custom databases in blockchain technology
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 
The [[Role and Architecture of Monad DB in Optimizing Blockchain Efficiency | Monad DB]] is a custom-built state database crucial for achieving high performance in blockchain technology, particularly for the Ethereum Virtual Machine (EVM) <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Its development stems from identifying significant bottlenecks in existing blockchain architectures.

## The Bottleneck of State Access

While [[Optimization techniques specific to blockchain databases | parallel EVM execution]] is a significant narrative in crypto, [[Monad Blockchain Technology | Monad]] discovered early on that merely implementing a parallel EVM algorithm did not lead to substantial performance improvements <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The primary bottleneck was identified as state access <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

In Ethereum, state (account information, slot data) is stored on SSDs <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The cost of reading from an SSD is considerable <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Crucially, the databases used by Ethereum and other EVM-compatible blockchains, such as PebbleDB or RocksDB, do not natively support parallel access <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This means that even if multiple virtual machines run in parallel, they still bottleneck when accessing the database, effectively resulting in single-file execution <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

The most expensive parts of blockchain operations are:
*   Cryptography functions (e.g., elliptical curve cryptography, hashing) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   State access <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

The business logic within most smart contracts is relatively inexpensive to execute compared to state access <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Paralyzing computation alone, therefore, yields minimal gains <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Limitations of General-Purpose Databases
Standard databases like LMDB, MDBX (B+ tree databases), and RocksDB, LevelDB (LSM trees) are general-purpose solutions <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. While suitable for storing and searching general data, they are not optimized for the specific access patterns and performance requirements of a blockchain <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Their generic nature means they are "performant on average" but not for highly specialized, latency-sensitive applications like blockchain state management <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

For instance, Go-Ethereum's database structure involves embedding one data structure inside another on disk, which makes every request traverse two data structures, leading to a very expensive operation <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

## The [[Role and Architecture of Monad DB in Optimizing Blockchain Efficiency | Monad DB]] Approach

The realization of the state access bottleneck led [[Monad Blockchain Technology | Monad]] to develop a custom database <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a> <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. This approach draws inspiration from high-frequency trading (HFT), where specialized systems are built from scratch, optimizing every component to shave off latency <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a> <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. In HFT, standard libraries are avoided because customizing data structures to the specific trading model extracts significantly better performance from the hardware <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

Applying this philosophy to blockchain, [[Monad Blockchain Technology | Monad]] recognized that understanding the exact data usage and storage patterns allows for building a database that leverages hardware capabilities to the maximum <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

### SSD Performance and Optimization
Modern SSDs are highly performant devices, capable of hundreds of thousands of I/O operations per second (IOPS) <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a> <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. However, many current blockchain clients using general-purpose databases fail to fully utilize this potential, resulting in poor performance <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

A key aspect of [[Role and Architecture of Monad DB in Optimizing Blockchain Efficiency | Monad DB]] is its ability to drastically reduce the number of requests to the hardware. For instance, [[Role and Architecture of Monad DB in Optimizing Blockchain Efficiency | Monad DB]] might require only one or two requests to look up an account, whereas other data structures might make 20 requests for the same information if it's not cached <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This "super optimization" extracts every last bit of performance from the SSD <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.

### Avoiding Shortcuts
The "no shortcuts" philosophy adopted by [[Monad Blockchain Technology | Monad]] emphasizes deep optimization rather than simply throwing more expensive hardware at the problem <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. A shortcut could be to require a very large amount of RAM to cache all state and avoid disk reads <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. However, this is not sustainable for long-term growth and decentralization:
*   **Cost:** RAM is two orders of magnitude more expensive than SSDs (e.g., 2 TB of high-quality NVMe SSD costs about $200, while 2 TB of RAM costs around $20,000) <a class="yt-timestamp" data-t="00:50:32">[00:50:32]</a>.
*   **Scalability:** While state will grow over time, managing this growth is more feasible with affordable SSDs than constantly increasing RAM requirements <a class="yt-timestamp" data-t="00:51:07">[00:51:07]</a>.
*   **Decentralization:** High hardware requirements hinder participation from regular users, centralizing the network <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.

Instead of relying on excessive RAM, [[Monad Blockchain Technology | Monad]] focuses on:
*   Building systems from the ground up to be performant <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   Deeply understanding the hardware and making informed engineering decisions <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.
*   Conducting extensive quantitative experimentation with different database types to identify and address engineering issues <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
*   Focusing on micro-optimizations (e.g., optimizing Translation Lookaside Buffer for 5% gain) that collectively lead to significant speedups <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>.
*   Questioning common assumptions (e.g., whether access lists are truly beneficial for performance) and validating them through measurement and experimentation <a class="yt-timestamp" data-t="00:31:44">[00:31:44]</a>.

This comprehensive approach, focusing on a custom state database and fine-grained optimizations, is essential for unlocking true performance gains and enabling the EVM to scale <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.