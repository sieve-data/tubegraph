---
title: Performance Challenges of Cryptography and State Access in Blockchain
videoId: VfUdVfIg7JI
---

From: [[thepipeline_xyz]] <br/> 

Optimizing [[scalability_and_performance_of_crypto_networks | blockchain performance]] is crucial, and a significant portion of the cost lies in cryptography functions and state access <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While smart contract business logic is relatively inexpensive to execute compared to typical desktop or phone applications, and optimizing computation alone doesn't yield substantial gains <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, the true bottlenecks emerge elsewhere.

## Cryptography Overheads

Cryptographic operations, such as elliptical curve cryptography and hashing functions, are inherently costly <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Transaction execution, particularly signature recovery, is one of the most expensive components <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Although some blockchain clients have begun to parallelize signature recovery to mitigate this, there's a limit to how much [[performance_gains_in_blockchain_transactions | performance]] can be gained solely through computation optimization <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## State Access and Database Latency

The most significant performance challenge, however, stems from state access and interactions with the underlying database <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### SSD Latency
A single read from an SSD can introduce a latency of 80 to 100 microseconds, or even more, depending on the SSD model and generation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This duration is "orders of magnitude longer" than the time it takes to execute a simple smart contract <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Sequential Reads in Transactions
Executing a single transaction often necessitates multiple sequential reads from the database. For instance, a transaction requires reading the sender's account to check their balance, the destination account, and potentially proxy accounts if involved <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Furthermore, data like ERC20 balances or Uniswap data are stored in specific storage slots, requiring additional reads <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

If these reads are not cached in main memory, the cumulative latency from these sequential disk accesses results in a "long time" for a single transaction to execute <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Hardware-Software Mismatch
One approach to mitigate this is to equip blockchain nodes with massive amounts of RAM, effectively avoiding disk reads and their associated latencies <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. However, this demands very large and expensive hardware, which can restrict decentralization <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Modern SSDs are highly capable, with some offering up to 500,000 I/O operations per second <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. The fundamental [[challenges_in_current_blockchain_infrastructure | challenge]] is that standard databases commonly used in blockchain clients (like Pebble DB, RocksDB, LMDB, LevelDB, and MDBX) fail to fully leverage this raw [[performance_gains_in_blockchain_transactions | performance]] <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## The Inefficiency of General-Purpose Databases

The core issue with these widely adopted databases is their general-purpose nature <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. They are designed for average [[performance_gains_in_blockchain_transactions | performance]] across a wide range of applications, not for highly specialized use cases like blockchain <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

Common problems include:
*   **Nested Data Structures**: Embedding one data structure inside another on disk can lead to very expensive traversal operations for every request <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Excessive Requests**: These general-purpose databases often make numerous requests to the hardware for basic lookups. For example, some standard implementations might require 20 disk requests to look up a single account, whereas an optimized custom database like Bana could do the same in one or two requests <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This "wastes" the underlying hardware's capability <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

## The Solution: Custom State Databases

To overcome these [[technical_challenges_and_solutions_in_blockchain_performance | technical challenges and solutions in blockchain performance]], the [[importance_of_custom_state_databases_in_blockchain | importance of custom state databases in blockchain]] becomes evident. By applying techniques from high-frequency trading (HFT), where standard libraries are bypassed in favor of custom, highly optimized data structures, developers can extract significantly better [[performance_gains_in_blockchain_transactions | performance]] from existing hardware <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

A custom database, like Bana Database, is designed with a precise understanding of how blockchain data needs to be stored and accessed <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This tailored approach allows for a reduction in the number of disk requests per operation, maximizing the throughput from high-performance SSDs and addressing the [[challenges_and_opportunities_in_blockchain_scalability | challenges and opportunities in blockchain scalability]] <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. This enables the development of a truly [[need_for_performant_blockchain | performant blockchain]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.