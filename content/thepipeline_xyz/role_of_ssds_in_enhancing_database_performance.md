---
title: Role of SSDs in enhancing database performance
videoId: VfUdVfIg7JI
---

From: [[thepipeline_xyz]] <br/> 

Optimizing database performance is crucial for [[high_performance_blockchains | high-performance blockchains]], especially when dealing with the high demands of the Ethereum Virtual Machine (EVM) <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. While computations in smart contracts are often relatively cheap <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, and parallel processing for elements like signature recovery can be trivially parallel <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, the most expensive parts of blockchain operations are cryptography functions (like elliptical curve cryptography and hashing) and, significantly, state access from the database <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## The Database Bottleneck

Profiling code reveals that a significant amount of time is spent on database operations <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. A single read from an SSD can have a latency of 80 to 100 microseconds or more <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This is orders of magnitude longer than it takes to execute a simple smart contract <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

A typical transaction involves multiple sequential reads:
*   Reading the sender's account to check their balance <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Reading the destination account <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Reading proxy accounts <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   Accessing storage slots, such as balances for ERC20 tokens or data for Uniswap <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

If these reads are not cached in main memory, their latencies sum up, leading to considerable time for a single transaction <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## The Potential of Modern SSDs

Modern SSDs are "amazing hardware" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, offering incredible performance, such as 500,000 I/O operations per second (IOPS) <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. They represent a significant leap from older spinning disk hard drives, which required sequential reads due to their physical mechanics <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. There's a lot of untapped "juice packed into SSDs" <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

## Why Standard Databases Fall Short

Despite the raw performance of SSDs, [[challenges_of_standard_databases_in_blockchain_performance | standard databases]] like Pebble DB or Rock DB often lead to "terrible performance" when used for blockchain clients <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

The issues with general-purpose databases include:
*   **Layered data structures**: They often embed one data structure inside another, leading to expensive double-traversal for every request <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **General-purpose design**: Databases like B+ tree (lmdb, mdbx) and LSM trees (RocksDB, LevelDB) are designed to be "performant on average" for general applications <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. They are not tailored for specific access patterns.
*   **Excessive requests**: Some blockchain clients using these databases make "so many requests just to look up something basic" <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

Relying solely on hardware improvements without software optimization is a mistake <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. An algorithm with better computational complexity but poorer implementation can still perform worse <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

## The Solution: Custom Database Optimization

To truly leverage the capabilities of SSDs and achieve [[blockchain_performance_optimization | high-performance blockchains]], [[importance_of_custom_databases_for_evm_optimization | custom databases]] are essential <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This approach is common in fields like high-frequency trading (HFT), where standard libraries are avoided in favor of customized data structures to extract maximum performance <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

By knowing exactly how data will be used and stored, a custom database can be designed to perform operations in the most efficient way <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. For example, [[monad_db_and_its_role_in_efficient_blockchain_operations | Monad DB]] might make only one or two requests to look up an account, compared to 20 requests by other data structures not in cache <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. This "super optimization" is key to extracting every last bit of performance from the hardware <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.