---
title: Importance of custom databases for EVM optimization
videoId: VfUdVfIg7JI
---

From: [[thepipeline_xyz]] <br/> 

Optimizing the performance of an [[ethereum_virtual_machine_optimizations | EVM]] client requires a deep understanding of where processing time is actually spent within a blockchain system <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. While common assumptions might point to complex computation, the most expensive parts of blockchain operations are typically cryptography functions (like elliptical curve cryptography and hashing) and state access <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

## Limitations of General Computation Optimization

Unlike desktop or phone applications, modern blockchains generally do not involve extensive computation within their smart contract logic <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>. As such, simply optimizing computation, including using [[parallel_evm_and_its_impact_on_performance | parallel EVM]] or parallel signature recovery, yields limited gains <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>. Even throwing multiple cores at the problem, which is a trivially parallel problem, doesn't significantly enhance overall [[blockchain_performance_optimization | blockchain performance]] <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.

## The Bottleneck: State Database Access

The primary bottleneck in [[performance_optimizations_in_ethereum_virtual_machine_evm | EVM]] performance is database access, particularly reading from storage <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>. A single read from an SSD can introduce a latency of 80 to 100 microseconds or more, depending on the SSD model <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. This is orders of magnitude longer than the time it takes to execute a simple smart contract <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

Executing a single transaction often requires multiple sequential reads from the database <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. For instance, processing a transaction requires reading the sender's account balance, the destination account, any proxy accounts, and specific storage slots if it's an ERC-20 token or a Uniswap transaction <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. If these reads are not cached in main memory and occur sequentially, the cumulative latency results in significant execution time for a single transaction <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. While one solution is to equip every node with very large, expensive RAM to prevent disk reads, this is not an economically viable or scalable approach <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

## Challenges with Standard Databases

Standard databases like Pebble DB, Rocks DB, LMDB (and its derivative MDBX), and Level DB are general-purpose databases <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. These databases are designed for average performance across a wide range of applications <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>. However, when used in blockchain clients, their performance can be "terrible" compared to the raw capabilities of modern SSDs <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.

One issue is that they often embed one data structure within another on disk, leading to expensive double-traversal operations for every request <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>. Furthermore, many existing [[optimization_strategies_for_blockchain_clients | blockchain clients]] using these databases make an excessive number of requests for basic lookups <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.

## The Case for Custom Databases

To achieve high [[blockchain_performance_optimization | blockchain performance]], especially in the context of an [[ethereum_virtual_machine_optimizations | EVM]], it is crucial to use custom databases tailored to the specific needs of blockchain data storage and access <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>. This approach is analogous to practices in high-frequency trading (HFT), where standard libraries and data structures are avoided in favor of customized solutions that extract maximum performance from hardware <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.

Modern SSDs are incredibly powerful, capable of 500,000 I/O operations per second <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. A custom database like [[monad_db_and_its_role_in_efficient_blockchain_operations | Monad DB]] is designed to fully leverage this raw performance by knowing exactly how data is stored and accessed <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. This allows for [[unique_database_optimizations_in_blockchains | unique database optimizations]] that drastically reduce the number of requests to the hardware <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>. For example, [[monad_db_and_its_role_in_efficient_blockchain_operations | Monad DB]] might make only one or two requests to look up an account, compared to twenty requests by other data structures not in cache <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>. This "super optimization" extracts every last bit of performance from the hardware <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.