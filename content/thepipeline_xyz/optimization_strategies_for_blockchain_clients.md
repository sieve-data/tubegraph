---
title: Optimization strategies for blockchain clients
videoId: VfUdVfIg7JI
---

From: [[thepipeline_xyz]] <br/> 

Optimizing blockchain client performance requires a deep understanding of where execution time is truly spent. While complex business logic in smart contracts is relatively cheap to execute compared to traditional applications <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, the most expensive parts of blockchain operations are cryptography functions (like elliptical curve cryptography and hashing) and state access <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Optimizing computation itself doesn't yield significant gains <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Some clients already implement [[Parallel Execution in Blockchain | parallel execution]] for signature recovery, which is a major part of transaction execution <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Database as a Bottleneck

Profiling reveals that a significant amount of time is spent on database operations <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. A single read from an SSD can have a latency of 80 to 100 microseconds or more, which is orders of magnitude longer than executing a simple smart contract <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. A single transaction often requires multiple sequential reads, such as reading the sender's account for balance, the destination account, proxy accounts, and storage slots for data like ERC20 balances or Uniswap data <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. If this data is not cached in main memory, these sequential reads accumulate, leading to prolonged transaction execution times <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

While one approach to mitigate this is to equip nodes with very large amounts of RAM to avoid disk reads entirely, significant [[blockchain_performance_optimization | performance optimization]] can still be achieved through optimized code that effectively leverages modern SSD capabilities <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Challenges with Standard Databases

Many blockchain clients currently use standard databases like Pebble DB or RocksDB <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, or other types such as B+ tree databases (e.g., LMDB, MDBX) and LSM trees (e.g., LevelDB, RocksDB) <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. However, these general-purpose databases are not designed for the specific needs of blockchain clients and lead to suboptimal performance <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

The issues include:
*   **Layered data structures**: Some implementations, like Go Ethereum (Geth), embed one data structure inside another on disk, leading to expensive double traversals for every request <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **General-purpose design**: Standard databases are built to be performant on average for a wide range of applications <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. This means they are not optimized for the specific data access patterns found in blockchain clients. For example, a standard database might require 20 requests to hardware to look up basic information not in cache, whereas a highly optimized database like the one used by Monb might only need one or two requests <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This highlights the [[challenges_of_standard_databases_in_blockchain_performance | challenges of standard databases in blockchain performance]].

## Custom Database Solutions

To achieve [[high_performance_blockchains | high performance blockchains]], a custom state database is crucial <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The approach involves applying techniques common in high-frequency trading (HFT), where standard libraries and data structures are avoided in favor of highly customized ones <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. By tailoring the data structure to the specific usage model, significantly better performance can be extracted from the hardware <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

This means:
*   **Knowing the data usage**: Developers know exactly how blockchain data is used and how it should be stored <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Leveraging modern SSDs**: Modern SSDs offer impressive capabilities, with some reaching 500,000 IOPS (Input/Output Operations Per Second) <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. However, this raw performance is often wasted by inefficient general-purpose database implementations <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. By implementing [[unique_database_optimizations_in_blockchains | unique database optimizations in blockchains]], the full potential of this hardware can be leveraged <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

By implementing custom databases specifically designed for blockchain data, clients can drastically reduce the number of disk requests needed for basic lookups, thereby maximizing the throughput of the underlying hardware and addressing [[growth_and_scalability_challenges_in_blockchain_ecosystems | growth and scalability challenges in blockchain ecosystems]] <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. This is a critical aspect of [[blockchain_scalability_and_highperformance_systems | blockchain scalability and high-performance systems]].