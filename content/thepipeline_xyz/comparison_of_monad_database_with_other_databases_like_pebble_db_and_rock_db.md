---
title: Comparison of Monad Database with other databases like Pebble DB and Rock DB
videoId: VfUdVfIg7JI
---

From: [[thepipeline_xyz]] <br/> 

[[monad_db_and_its_role_in_efficient_blockchain_operations|Monad DB]] is a custom state database designed to overcome the limitations of standard database implementations like Pebble DB or Rocks DB when building a performant EVM <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Blockchain Performance Bottlenecks

The most expensive operations in blockchain environments are cryptography functions, such as electrical curve cryptography and hashing functions, and state access <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Interestingly, the most complex business logic in smart contracts is relatively inexpensive to execute compared to typical desktop or phone programs, as there isn't much computation in modern blockchains <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Optimizing computation alone does not yield significant gains <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### The Latency Problem of State Access

The primary bottleneck identified in blockchain operations is database access <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. A single read from an SSD can have a latency of 80 to 100 microseconds or more <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This duration is orders of magnitude longer than the time it takes to execute a simple smart contract <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

A typical transaction involves multiple sequential reads:
*   Reading the sender's account to check balance <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Reading the destination account <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Reading proxy accounts, if applicable <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   Reading storage slots, such as balances for ERC-20 tokens or Uniswap data <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

If these reads are not cached in main memory and must be performed sequentially from disk, the cumulative latency results in a long execution time for a single transaction <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Limitations of General-Purpose Databases

While simply adding more RAM to cache data is an option, it requires expensive, large servers in data centers <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Modern SSDs are highly performant, with some achieving 500,000 I/O operations per second <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. However, many blockchain clients that use standard databases like Pebble DB or Rocks DB exhibit "terrible" performance despite the advanced hardware <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

One issue with these databases is that they often embed one data structure inside another, leading to expensive operations where every request traverses two data structures <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Common database types used for blockchain clients include:
*   **B+ tree databases**: Examples are LMDB and MDBX (an LMDB derivative) <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **LSM trees**: Examples include Rocks DB and Level DB <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

The fundamental problem with these general-purpose databases is that they are designed for average performance across a wide range of applications <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. They are not optimized for specific use cases, unlike in high-frequency trading (HFT) where custom data structures are used to extract significantly better performance from hardware <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Relying solely on hardware improvements without software optimization wastes the hardware's capabilities <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## [[monad_db_and_its_role_in_efficient_blockchain_operations|Monad DB]]'s Optimized Approach

[[monad_db_and_its_role_in_efficient_blockchain_operations|Monad DB]] applies the principle of custom data structures, specifically knowing exactly how data will be used and stored within the blockchain context <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. By implementing its own database, [[monad_db_and_its_role_in_efficient_blockchain_operations|Monad DB]] aims to leverage the full potential of modern SSDs <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

This specialization leads to significant performance gains:
*   Some traditional blockchain clients make numerous requests to look up basic information <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   [[monad_db_and_its_role_in_efficient_blockchain_operations|Monad DB]] can achieve the same lookups with a tenth or even a twentieth of the requests <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   For example, [[monad_db_and_its_role_in_efficient_blockchain_operations|Monad DB]] might make only one or two requests to look up an account (if not in cache), whereas other data structures could require up to 20 requests to the hardware <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

This "super optimization" extracts every last bit of performance from the hardware, ensuring efficiency that general-purpose databases cannot match for specific blockchain needs <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.