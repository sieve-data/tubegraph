---
title: Custom state database development by Manad
videoId: vm6ByQsdstg
---

From: [[thepipeline_xyz]] <br/> 

Monad's approach to blockchain performance, particularly for the Ethereum Virtual Machine (EVM), centers heavily on custom state database development. This strategy arose from recognizing that traditional parallelization methods alone do not yield significant performance gains due to bottlenecks at the data storage level <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## The Bottleneck: State Access

While many teams focus on parallel EVM implementations, Monad's early research showed that the actual bottleneck for performance is state access <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Transactions depend on accounts and slots within those accounts, and this state data is typically stored on an SSD <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

The cost of reading from an SSD is significant <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Standard databases used by Ethereum and other EVM-compatible blockchains, such as Pebble DB or Rock DB, do not support parallel access efficiently <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. This means that even if multiple virtual machines run in parallel, they still bottleneck when accessing the database, effectively resulting in single-file execution <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

A single read from an SSD can take 80 to 100 microseconds, which is orders of magnitude longer than executing a simple smart contract <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. Sequential reads for various components of a transaction (sender account, destination account, proxy accounts, storage slots for ERC20 balances or Uniswap data) linearly sum up these long times, significantly delaying transaction execution <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

Furthermore, general-purpose databases like B+ tree databases (LMDB, MDBX) and LSM trees (RocksDB, LevelDB) are designed for average performance across various applications, not for the highly specific and optimized needs of a blockchain <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. Embedding one data structure inside another on disk also creates an expensive traversal for every request <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

## Monad's Solution: The Custom Database

Recognizing these limitations, [[monad_blockchain_development | Monad]] chose to develop its own custom state database <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. This decision was influenced by the team's background in high-frequency trading (HFT), where custom-built systems and highly optimized data structures are crucial for shaving off latency and achieving peak performance <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. In HFT, standard libraries are rarely used; instead, data structures are customized to the specific trading model to extract superior performance from hardware <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

Monad applies this "no shortcuts" philosophy to its blockchain development. Instead of simply increasing RAM requirements—a common shortcut that doesn't scale well and centralizes the network due to higher costs <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a> <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>—Monad focuses on deep, fundamental engineering <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>.

The custom database, [[monad_db_and_its_impact | Monad DB]], is designed to leverage modern SSDs, which are highly performant (e.g., 500,000 I/O operations per second for a $200 SSD) <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a> <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>. The key is to customize access to these devices to be efficient, as general database implementations often fail to utilize the hardware's full potential <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. For example, [[monad_db_and_its_impact | Monad DB]] might make one or two requests to look up an account, compared to 20 requests by other data structures for data not in cache <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. This "super optimization" extracts every last bit of performance <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

## Impact on Performance and Decentralization

The [[importance_of_custom_state_databases_in_blockchain | custom state database]] is a crucial component that allows parallel execution to achieve true performance gains <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Without it, parallelizing the EVM would not significantly improve throughput or latency <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

By designing the database to run efficiently on commodity hardware, Monad aims to make network participation more accessible and less expensive for regular users <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>. This contrasts with solutions that rely on throwing massive amounts of RAM at the problem, which would necessitate very large, expensive data centers and compromise decentralization <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

Monad's detailed, quantitative approach involves extensive experimentation with various databases (RocksDB, LMDB) to understand their engineering issues <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>. This meticulous work ensures that the system is built from the ground up for maximum performance <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. This focus on "no shortcuts" ultimately yields a more performant, scalable, and decentralized EVM ecosystem.