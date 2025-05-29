---
title: Comparison of Different Database Structures for Blockchain Efficiency
videoId: VfUdVfIg7JI
---

From: [[thepipeline_xyz]] <br/> 

Achieving [[performance_gains_in_blockchain_transactions | high performance]] in blockchain systems necessitates a deep dive into the underlying data structures, particularly the state database. Rather than relying on generic solutions, the development of a [[Importance of Custom State Databases in Blockchain | custom state database]] can significantly enhance efficiency [00:00:07].

## Core Bottlenecks in Blockchain Execution

The most expensive operations in a blockchain are not primarily computation but rather cryptography functions (like elliptical curve cryptography and hashing) and state access [00:00:22]. Conversely, the complex business logic within most smart contracts is relatively inexpensive to execute compared to typical desktop or phone applications [00:00:41].

### Limitations of Computation Optimization
Currently, there isn't a lot of computation in modern blockchains, meaning optimizing computation alone doesn't yield substantial gains [00:00:55]. Some blockchain clients already feature [[Parallelization in blockchain technologies | parallel]] signature recovery, which is one of the most expensive parts of transaction execution [00:01:05]. While it's a trivially [[Parallelization in blockchain technologies | parallel]] problem where multiple cores can be utilized, there's not much further to gain in this area [00:01:20].

## The Critical Role of State Access

Profiling blockchain code reveals that a significant amount of time is spent on database operations [00:01:28]. Even a single read from an SSD can introduce a latency of 80 to 100 microseconds or more, depending on the SSD model [00:01:38]. This is orders of magnitude longer than the time it takes to execute a simple smart contract [00:01:56].

### Sequential Reads and Latency Accumulation
A single transaction often requires multiple sequential database reads:
*   Reading the sender's account to verify balance [00:02:07]
*   Reading the destination account [00:02:11]
*   Reading proxy accounts if applicable [00:02:13]
*   Reading storage slots (e.g., ERC20 token balances, Uniswap data) [00:02:17]

If these reads are not cached in main memory, their individual latencies (e.g., 80-100 microseconds) sum up, resulting in a prolonged execution time for a single transaction [00:02:30]. While adding more RAM to keep everything in memory is an option, it requires very large and expensive hardware setups [00:02:53].

## Inefficiencies of General-Purpose Databases

Common database technologies like PebbleDB, RocksDB (an LSM tree derivative of LevelDB), LMDB, and MDBX (an LMDB derivative B+ tree database) are often used in blockchain clients [00:00:09], [00:04:30]. However, their performance in this context can be "terrible" [00:03:52].

### Reasons for Poor Performance:
*   **Layered Data Structures**: General-purpose databases often embed one data structure inside another on disk, meaning every request involves traversing two data structures, an expensive operation [00:04:06].
*   **General-Purpose Design**: These databases are designed for average performance across a wide range of applications, not for the highly specific and demanding access patterns of a blockchain state [00:04:50]. General data structures and application code are not inherently performant for specialized tasks [00:05:02].

> "If you ever work in like HFT [High-Frequency Trading] this is something you'll quickly discover is like you know nobody in HFT uses standard libraries standard C++ libraries or standard because these These are general sort of data structures if you customize the data structure to the to the trading model you can extract you know way better performance from the hardware" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>

## The Advantage of Custom State Databases

The approach of using a [[Importance of Custom State Databases in Blockchain | custom state database]], such as Bana, stems from applying principles seen in High-Frequency Trading (HFT) [00:05:31]. By knowing exactly how the data will be used and stored, a specialized database can be implemented to achieve optimal performance [00:05:32].

### Leveraging Modern Hardware Capabilities
Modern SSDs are incredibly performant, with capabilities like 500,000 I/O operations per second (IOPS) [00:06:53]. However, simply having powerful hardware is insufficient; the software must be optimized to leverage it [00:07:04].

> "You can't just throw... you know one thing you study in computer science is like complexity right and an algorithm which is has better computational complexity but is actually more poorly implemented will still perform better so you can't... you can't just forget about your your optimizations and be like okay the hardware is going to take care of it you know you're just wasting basically the capability that's there" <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>

### Reduced Requests and Super Optimization
A custom database like Bana can significantly reduce the number of requests made to the hardware for basic lookups [00:07:41]. For example, Bana might require only one or two requests to look up an account not in cache, whereas general data structures might make 20 requests for the same operation [00:07:59]. This "super optimization" extracts every last bit of [[performance_gains_in_blockchain_transactions | performance]] from the hardware [00:08:14].

By customizing the database to the blockchain's specific needs, it's possible to extract superior [[performance_gains_in_blockchain_transactions | performance gains]] from SSDs, surpassing what standard models and structures can achieve [00:03:12], [00:06:31].