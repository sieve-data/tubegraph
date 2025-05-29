---
title: Challenges in building highperformance systems
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

Developing high-performance systems, especially in the context of blockchain technology, presents unique and significant challenges. Monad's approach highlights several key areas where traditional methods fall short and innovation is required <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## The "Build from Scratch" Approach

Monad's decision to build its protocol from the ground up, rather than forking an existing open-source project, was driven by the need for greater technical control <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Forking would necessitate modifying so many aspects of existing projects that leveraging ongoing maintenance or new features would become impractical <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Building from scratch allows for:
*   **Precise Implementation Control** <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>: This includes fine-tuning memory allocation, disk interaction, and other low-level details crucial for optimal performance <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Avoiding Friction** <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>: Existing EVM implementations, such as Ethereum clients, are often "arbitrarily rate-limited" due to design choices focused on low node requirements, rather than raw execution throughput <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. To achieve high performance, a different design space is required <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Scarcity of Specialized Talent

One of the significant [[Startup Challenges in Hardware Development | challenges]] in building [[high performance blockchains | high-performance blockchain]] systems is the difficulty in finding qualified low-level system engineers <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. These specialists typically work in fields like:
*   Big tech, focusing on operating systems (e.g., Linux) <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>
*   Silicon manufacturing (e.g., Nvidia) <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>
*   [[Highfrequency trading systems and performance optimization | High-frequency trading firms]] <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>

Their expertise in creating [[high performance blockchains | high-performance systems]] is critical but not commonly found among general developers <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

## Technical Hurdles in Concurrency and Data Management

The core of building [[blockchain_scalability_and_highperformance_systems | high-performance blockchain systems]] involves overcoming specific technical obstacles:

### Concurrent Execution
Modern machines feature many cores, yet most existing blockchain clients only use a single core for transaction execution, with auxiliary threads for other tasks <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. The challenge is to leverage these multiple cores by enabling concurrent execution of transactions <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. This is complicated by:
*   **Transaction Dependencies** <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>: Transactions within a block are not always independent tasks; they often have interdependencies that must be managed <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Pipelining** <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>: Implementing pipelining, where multiple steps of different transactions are processed simultaneously, is crucial for efficiency <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This requires understanding transaction relationships and potentially removing dependencies <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Monad's architecture is "highly pipeline" to keep the CPU constantly active <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### Database Performance
The database is a critical component, and waiting for disk access is a major performance bottleneck <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Even 30 microseconds of disk access time, when compounded across many transactions and accesses per transaction, quickly adds up, leading to an underutilized CPU <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. Monad addressed this by building its own database, ensuring the CPU is always busy and not waiting for disk I/O <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. This is a key innovation in their drive for [[blockchain_scalability_and_highperformance_systems | high-performance systems]] <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Benchmarking Real-World Performance

Accurate performance benchmarking is another challenge, as many projects use misleading metrics <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. Simple token transfers are easily achievable, even by unoptimized, single-core clients <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. To truly assess performance, Monad benchmarks using replayed Ethereum history because it includes:
*   **Complex Contract Interactions** <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>: Real Ethereum history involves diverse protocols, including AMMs, lending protocols, and computationally expensive ZK proofs, which are far more taxing than simple transfers <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.
*   **Realistic Usage Patterns** <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>: This approach simulates what the system looks like with actual users, exposing potential bottlenecks and use patterns not anticipated during internal testing <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

## Overcoming Decentralization-Performance Trade-offs

A significant [[challenges_and_strategies_in_building_crypto_infrastructure | challenge in building crypto infrastructure]] is pushing the decentralization-performance trade-off curve forward <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. Many projects employ "tricks" to inflate performance metrics without true decentralization:
*   **Geographical Collocation** <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>: Having all nodes in one location, or concentrating stake weight in a few collocated nodes, can make consensus appear faster by reducing latency, but compromises decentralization <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.
*   **High Hardware Requirements** <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>: Relying on a small number of nodes with very high hardware or bandwidth requirements limits participation <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>.

Monad actively tests worst-case scenarios, like having highly staked nodes in geographically distant locations (e.g., Singapore and New York), to ensure the algorithm performs well under true decentralized conditions <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>. The aim is to make decentralization more performant through technological innovation, rather than by manipulating parameters or centralizing the network <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.

## Anticipating Unforeseen Usage Patterns

Even with robust internal testing and Ethereum replay, real-world usage on a public testnet can expose unexpected behaviors <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>. Scenarios like:
*   Thousands of concurrent users performing complex actions (e.g., [[High transaction volume challenges | NFT mints]] at the same time) <a class="yt-timestamp" data-t="00:27:45">[00:27:45]</a>.
*   The emergence of new applications or actors, such as AI agents, that might "crash the testnet" through intense, automated activity <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>, <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>.

These events test the system's ability to "gracefully degrade" rather than fall over completely, providing a poor user experience with errors or reverted transactions <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>. A robust system should simply "just work" without needing stories or excuses for failures across different layers of the stack (RPC, validator, distribution network) <a class="yt-timestamp" data-t="00:32:22">[00:32:22]</a>.

Ultimately, building [[high performance blockchains | high-performance blockchain]] systems is not a finish line but a starting line, with continuous work needed for optimizations, new features, and research to support increasing decentralization and usability <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>.