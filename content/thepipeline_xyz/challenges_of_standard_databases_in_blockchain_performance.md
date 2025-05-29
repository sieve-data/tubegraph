---
title: Challenges of standard databases in blockchain performance
videoId: VfUdVfIg7JI
---

From: [[thepipeline_xyz]] <br/> 

Developing a [[high performance blockchains | performant EVM]] (Ethereum Virtual Machine) and overall blockchain system requires careful consideration of its underlying database, as standard database implementations often introduce significant performance bottlenecks <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. While computational logic within smart contracts is relatively inexpensive to execute compared to typical desktop or phone applications <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, other aspects of blockchain operations present major performance challenges <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Core Performance Bottlenecks

The most expensive components in blockchain operations include <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>:
*   **Cryptography Functions**: This includes electrical curve cryptography and hashing functions <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **State Access**: Accessing the blockchain's state data is a significant performance drain <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Signature Recovery**: Parallel signature recovery, though already implemented in some clients, remains an expensive part of transaction execution <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

Optimization of raw computation alone offers limited gains in modern blockchains <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Instead, the focus shifts to areas like state access.

## Database Latency and State Access

Profiling blockchain code reveals that a substantial amount of time is spent on database interactions <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. A single read from an SSD can have a latency of 80 to 100 microseconds or more, depending on the SSD model and generation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This latency is orders of magnitude longer than it takes to execute a simple smart contract <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

Executing a single transaction often requires multiple sequential database reads <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>:
*   Reading the sender's account to check their balance <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Reading the destination account <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Reading proxy accounts <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   Reading storage slots, which is where data like ERC-20 balances or Uniswap data are stored <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

When these sequential reads occur without being cached in main memory, the cumulative latency results in significant transaction execution times <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. While increasing RAM to cache all data can mitigate this, it leads to very expensive hardware requirements, which is not an optimal solution for broad adoption <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Limitations of Standard Databases

General-purpose databases, such as Pebble DB or RocksDB, which are often used as standard implementations for blockchain clients, present significant performance issues <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. These databases include <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>:
*   **B+ tree databases**: LMDB and its derivative MDBX <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **LSM (Log-Structured Merge) trees**: RocksDB (a derivative of LevelDB, which was the first) <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

The fundamental problem with these options is their "general-purpose" nature <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. They are designed for average performance across a wide range of applications, not for highly specialized and performant use cases <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

Specific issues include:
*   **Embedded Data Structures**: Embedding one data structure inside another that is stored on disk leads to highly expensive operations, as each request traverses two data structures <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Inefficient Use of Hardware**: Despite the impressive capabilities of modern SSDs (e.g., 500,000 I/O operations per second for some hosts <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>), general-purpose databases fail to leverage this raw performance <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Excessive Requests**: Standard blockchain clients using these databases can make an unnecessarily high number of requests (e.g., 20 requests) just to look up basic information <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

This phenomenon is similar to High-Frequency Trading (HFT), where standard libraries or general data structures are avoided because customizing the data structure to the specific trading model yields significantly better performance from the hardware <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## The Solution: Custom Database Optimization

To overcome these [[growth and scalability challenges in blockchain ecosystems | challenges]] and achieve [[blockchain performance optimization | high performance]], a custom database approach is necessary <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. By understanding exactly how the data needs to be used and stored, developers can implement a database optimized for specific blockchain requirements <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

For instance, [[monad_db_and_its_role_in_efficient_blockchain_operations | Monad DB]] was developed to extract every last bit of performance from the hardware <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. It achieves this by significantly reducing the number of requests made to the hardware. While a typical data structure might make 20 requests to look up an account, [[monad_db_and_its_role_in_efficient_blockchain_operations | Monad DB]] can achieve the same lookup with just one or two requests <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. This level of [[unique_database_optimizations_in_blockchains | super optimization]] is crucial for maximizing throughput and efficiency in blockchain systems <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

This customized approach is a key part of the [[evolution and impact of highperformance blockchain technology | evolution]] towards more [[blockchain_scalability_and_highperformance_systems | performant and scalable blockchain systems]].