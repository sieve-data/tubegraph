---
title: EVM compatibility and innovation
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

Monad's public testnet is officially going live, showcasing years of technological development <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The launch of a testnet or mainnet is often seen by many protocols as the finish line, but for Monad, it's considered the starting line for continued innovation <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a> <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>.

## Building from Scratch for Technical Control

Monad has taken a unique approach, building its protocol everything from the ground up, from scratch <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This decision was driven by the need for more technical control over the product <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. While forking an open-source project allows leveraging existing maintenance and work, Monad anticipated modifying so many aspects of existing open-source projects that ongoing new features or maintenance wouldn't be leveraged effectively <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a> <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

Building from scratch allows Monad to be very particular about implementation details, such as memory allocation or disk interaction, which might be constrained by existing patterns in forked code <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This approach prioritizes simplicity, control, ongoing maintenance, and the ability to achieve the best [[performance_optimizations_in_ethereum_virtual_machine_evm | performance]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Why Others Haven't Rebuilt the EVM from Scratch

The Ethereum Virtual Machine (EVM) has existed for over 10 years <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. While other projects have improved [[performance_optimizations_in_ethereum_virtual_machine_evm | performance]] in areas like state sync (e.g., Aragon's C++ and Go clients improving network join speed), they haven't focused on raw execution [[performance_optimizations_in_ethereum_virtual_machine_evm | performance]] <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This is largely because Ethereum is "arbitrarily rate limited" to low throughput for various reasons, including maintaining very low node requirements <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Consequently, focusing on high execution throughput for Ethereum clients didn't make sense <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

Monad, however, was envisioned as a [[evolution_and_impact_of_highperformance_blockchain_technology | high-performance EVM]] chain from the outset, with no design restrictions except for aiming for 100% EVM compatibility with Ethereum <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a> <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. The goal was to leverage maximum network and hardware [[performance_optimizations_in_ethereum_virtual_machine_evm | performance]], while still targeting consumer-grade nodes (e.g., a $1,000 PC) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a> <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

This undertaking is "really hard" and requires rare low-level system engineers who typically work in big tech (operating systems), silicon manufacturing (Nvidia), or high-frequency trading <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a> <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

## Monad's Core Technical Innovations

The main challenge for Monad has been achieving concurrent execution, leveraging multiple CPU cores in machines that traditionally use single-core main threads for transaction execution <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Although transactions within a block have dependencies, Monad aims for right-pipelining to work on multiple transactions simultaneously <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Pipelined Execution and Custom Database

A key innovation is the use of a custom database, as waiting for disk access (which can take 30 microseconds or more) is a major bottleneck <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a> <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. These small delays accumulate quickly across many transactions, leading to the CPU sitting idle <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

Monad's core innovation revolves around continuously keeping the machine busy and preventing the CPU from waiting, especially for disk access <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. This approach is likened to a "washing machine" analogy: instead of doing one load of laundry from start to finish (wash, dry, fold, put away) sequentially, Monad pipelines the process, allowing multiple loads to be in different stages concurrently (one washing, another drying, a third being folded) <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a> <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This is [[parallel_evm_and_its_impact_on_performance | pipelining]], performing multiple steps across multiple objects simultaneously, distinguishing it from simple parallel transaction execution <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. Monad's architecture is "highly pipelined," constantly striving to keep the system busy <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

Building such an optimized system is analogous to the evolution of airplanes <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. The Wright brothers achieved the "0 to 1" innovation by making a plane work <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. Modern airplanes, however, represent the "1 to 100" optimization, with intricate engineering and material science making them vastly more efficient <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Similarly, Ethereum's "0 to 1" innovation enabled smart contracts and permissionless global finance <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Monad focuses on the [[performance_optimizations_in_ethereum_virtual_machine_evm | performance engineering layer]] beyond that, aiming for much greater [[performance_optimizations_in_ethereum_virtual_machine_evm | performance]] and cheaper transactions <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

## What Monad Unlocks: High-Performance EVM

Monad aims to provide a highly performant version of shared global state, offering built-in payment rails and programmability for developers <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This allows applications to scale to millions or hundreds of millions of users who already possess on-chain assets, digital identities, and historical application usage <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

Key verticals Monad can enable:
*   **High-fidelity DeFi**: Personal finance at scale for hundreds of millions of users, offering very cheap transaction fees and low slippage due to efficient liquidity provision <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   **Consumer Space**: Applications requiring scale to tens or hundreds of millions of users, supported by Monad's capacity for over a billion transactions per day <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a> <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

This is a bet on application builders leveraging high-performance infrastructure as crypto adoption continues to grow monotonically <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a> <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

### Enabling New Business Models through Low Gas Fees

A significant impact of Monad's [[performance_optimizations_in_ethereum_virtual_machine_evm | performance]] is the ability to drastically reduce gas fees <a class="yt-timestamp" data-t="00:37:30">[00:37:30]</a>. This is crucial for simplifying the user experience by abstracting away gas fee payments, allowing applications to sponsor gas costs <a class="yt-timestamp" data-t="00:37:02">[00:37:02]</a>. When gas is cheap, the cost burden on application developers for scaling is significantly reduced, enabling more sustainable business models <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a>.

This is particularly impactful in the DePIN (Decentralized Physical Infrastructure Networks) space, where potential usage is high but price-sensitive <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>. For example, if pushing data to a chain costs a fraction of a cent, it lowers the barrier to entry and unlocks new business models like marketplaces for health data or data from various consumer devices <a class="yt-timestamp" data-t="00:38:28">[00:38:28]</a>.

## Benchmarking and Addressing Misleading Metrics

Monad's development process involves constant internal replays of Ethereum history, with automated systems graphing TPS (Transactions Per Second), gas per second, and other metrics to track performance changes with every code alteration <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. The Devnet served as a feedback loop for early testers and infrastructure providers to identify what was working or missing <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

One notable Devnet usage involved a team simulating a huge number of exchange orders, sending 3 trillion gas in a couple of hours – roughly 30 days worth of Ethereum throughput <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.

### The Importance of Real-World Benchmarking

In the crypto space, TPS figures on testnets can be misleading, as metrics are often manipulated <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. The simplest blockchain operation is native token transfers <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. Early Ethereum history, dominated by simple ETH transfers, could achieve 50,000 TPS even on a single-core, unoptimized client like Silkworm <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>. Therefore, announcing "10,000 TPS for token transfers" is "not interesting because it's easily achievable" <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a> <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.

Even ERC-20 contract transfers, which update balances in a few contracts, are relatively simple <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. Real Ethereum usage involves complex protocols like AMMs (Automated Market Makers), lending protocols, and especially expensive operations like ZK proofs (Zero-Knowledge proofs), which historically cost hundreds of dollars per transaction <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a> <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. Monad's benchmarking goal is to handle this "real usage" by replaying Ethereum history <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>.

### Combating Misleading Marketing and Decentralization Trade-offs

There's a lot of misleading marketing in the space, where projects "put the finger on the scale" regarding:
*   The nature of transfers or transactions <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
*   The hardware used for benchmarking <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.
*   The geographic location and actual stake weight distribution of nodes <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>. Some projects might show nodes globally but concentrate stake weight in one location, making geographically distributed nodes irrelevant to consensus <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a> <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.

Monad "reject[s] that practice" and focuses on building a robust system that optimizes consensus and block propagation while maintaining reasonable bandwidth requirements and Byzantine fault tolerance <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. They intentionally set up highly stake-weighted nodes in diverse locations (e.g., Singapore, New York) to test algorithms and optimize for "worst-case" conditions, pushing the decentralization-performance trade-off curve forward <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a> <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>. Users should question metrics that seem to "violate the laws of physics," as they likely indicate an arrangement that isn't decentralized <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>.

## The Public Testnet: A Starting Line for Growth

The goal of the public testnet from a technology perspective is to exercise the technology, gain feedback on the client, and identify its strengths and weaknesses through real-world usage <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>.

From the foundation's perspective, it's a showcase of the technology's power and the applications built upon Monad that leverage its [[performance_optimizations_in_ethereum_virtual_machine_evm | performance]] <a class="yt-timestamp" data-t="00:33:38">[00:33:38]</a>. It's also an opportunity to generate excitement and growth in the crypto space, allowing the community to experience what Monad enables <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>.

The testnet is the first time Monad is "up to the line" for public testing, allowing anyone to run tests and experience its feel <a class="yt-timestamp" data-t="00:34:48">[00:34:48]</a>. It will provide crucial user feedback for teams building on Monad, helping them improve their products <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>. This public demonstration is expected to attract new builders, making it clear that Monad is a real, launching platform for pushing the limits of crypto <a class="yt-timestamp" data-t="00:35:31">[00:35:31]</a>.

### Future Outlook and Continued Innovation

Monad's launch is seen as a starting line, not a finish line <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a>. The team has a "massive queue of ideas" for future optimizations, rewrites, research, and new features <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>. This includes:
*   Further [[ethereum_virtual_machine_optimizations | EVM optimizations]] <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.
*   Rewriting existing components for even better [[performance_optimizations_in_ethereum_virtual_machine_evm | performance]] <a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>.
*   Ongoing research <a class="yt-timestamp" data-t="00:49:20">[00:49:20]</a>.
*   New features for usability and privacy <a class="yt-timestamp" data-t="00:49:22">[00:49:22]</a>.
*   Scaling decentralization to support thousands of nodes, on par with Ethereum and Solana <a class="yt-timestamp" data-t="00:49:30">[00:49:30]</a>.
*   Account abstraction <a class="yt-timestamp" data-t="00:49:53">[00:49:53]</a>.

The long-term vision involves continuously evolving the system, similar to how a high-frequency trading system is continually reinvented for better [[performance_optimizations_in_ethereum_virtual_machine_evm | performance]] <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>. Monad's initial launch provides high [[performance_optimizations_in_ethereum_virtual_machine_evm | performance]] and full backward compatibility for the EVM and RPC, which unlocks many use cases <a class="yt-timestamp" data-t="00:51:06">[00:51:06]</a>. Beyond this, there are numerous "fun additional improvements" planned <a class="yt-timestamp" data-t="00:51:23">[00:51:23]</a>.

Unlike projects that fork existing codebases and focus primarily on marketing, Monad believes in bringing "real innovative technology" to market <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a> <a class="yt-timestamp" data-t="00:52:35">[00:52:35]</a>. This integration of technological innovation and a go-to-market strategy is expected to make a significant impact on crypto adoption <a class="yt-timestamp" data-t="00:52:41">[00:52:41]</a>.

The increased speed and reduced cost of Monad are expected to enable both predictable applications (like more efficient DeFi) and unpredictable, novel applications that are hard to foresee, similar to how increased internet bandwidth enabled YouTube and Instagram beyond early predictions of web pages and email <a class="yt-timestamp" data-t="00:42:06">[00:42:06]</a> <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. The testnet will provide an exciting platform to observe these new usage patterns, including stress tests like NFT mints and the potential emergence of AI agents <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a> <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>.