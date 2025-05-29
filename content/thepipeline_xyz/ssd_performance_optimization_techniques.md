---
title: SSD Performance Optimization Techniques
videoId: VfUdVfIg7JI
---

From: [[thepipeline_xyz]] <br/> 

For [[optimizing_ethereum_virtual_machine_performance | optimizing a performant EVM]], a key consideration is the custom state database, such as Bana Database, rather than standard implementations like Pebble DB or RocksDB <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Identifying Blockchain Performance Bottlenecks

The most expensive parts in [[technical_challenges_and_solutions_in_blockchain_performance | blockchain performance]] are typically cryptography functions, electrical curve cryptography, hashing functions, and state access <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. In contrast, complex business logic in most smart contracts is relatively inexpensive to execute <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

[[optimizing_evm_implementations | Optimizing computation]] in modern blockchain doesn't yield significant [[performance_gains_in_blockchain_transactions | performance gains]] because there isn't extensive computation involved <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Some clients already have [[parallel_evm_and_blockchain_optimizations | parallel signature recovery]], which is one of the most expensive parts of transaction execution <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

When profiling code, it becomes clear that most time is spent on database operations <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. A single read from an SSD can have a latency of 80 to 100 microseconds or more, depending on the model and generation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This is orders of magnitude longer than executing a simple smart contract <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Sequential Database Reads

Executing a single transaction often involves multiple sequential database reads:
*   Reading the sender's account to check their balance <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Reading the destination account <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Reading proxy accounts if applicable <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   Reading storage slots, such as balances in ERC-20 tokens or data in Uniswap <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

If these reads are performed sequentially and are not cached in main memory, their cumulative latency can make a single transaction execution quite long <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Limitations of General-Purpose Databases

While simply adding more RAM to cache everything is an option to avoid disk reads, it necessitates very large and expensive hardware <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Modern SSDs are capable of incredible [[impact_of_high_throughput_on_system_performance | high performance]], with some achieving 500,000 I/O operations per second <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. However, many general-purpose databases commonly used by [[blockchain_redesign_for_high_performance | blockchain clients]], like Pebble DB or RocksDB, fail to leverage this raw performance effectively <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

Common issues include:
*   **Layered Data Structures**: Embedding one data structure inside another on disk, leading to expensive double-traversal for every request <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **General-Purpose Design**: Databases like B+ tree databases (LMDB, MDBX) and LSM trees (RocksDB, LevelDB) are designed for general applications <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. They aim for average performance rather than specialized, peak performance <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

This general design leads to inefficient use of hardware capabilities <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Some databases make 20 requests to hardware for a basic lookup that a custom solution might achieve in one or two requests <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

## The Power of Customization

The approach for Bana Database is inspired by techniques from high-frequency trading (HFT) <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. In HFT, standard libraries and general data structures are avoided because customizing the data structure to the specific trading model extracts significantly better [[performance_gains_in_blockchain_transactions | performance]] from the hardware <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

By knowing exactly how the data needs to be used and stored for blockchain applications, a custom database can be implemented to achieve optimal [[performance_gains_in_blockchain_transactions | performance]] <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This allows for massive [[performance_gains_in_blockchain_transactions | performance gains]] by customizing the use of SSDs to be maximally efficient <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. It's crucial not to forget about software optimizations, as even an algorithm with better computational complexity might perform worse if poorly implemented <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.