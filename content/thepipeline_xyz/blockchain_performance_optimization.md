---
title: Blockchain performance optimization
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

[[high performance blockchains | High performance blockchains]] are a key focus in the development of new protocols, aiming to maximize throughput and efficiency while maintaining decentralization and compatibility. Monad's approach involves building from scratch to achieve unparalleled control and [[Optimization strategies for blockchain clients | optimization strategies for blockchain clients]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Building from Scratch for Performance
Monad chose to build its protocol entirely from scratch rather than forking an existing open-source project <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This approach provides greater technical control over the product <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

Key reasons for this decision include:
*   **Technical Control:** Building from scratch allows developers to be very particular about how components like memory allocation and disk interaction are implemented, ensuring optimal [[Performance optimizations in Ethereum Virtual Machine EVM | performance optimizations]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Avoidance of Friction:** If Monad had forked an existing project, such extensive modifications would have been needed that leveraging ongoing new features or maintenance from the original project would not have been possible <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Long-term Maintenance & Feature Development:** This approach offers simplicity, control, and better handling of ongoing maintenance responsibilities and new feature development <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

While some open-source projects are used, Monad specifically avoided forking an existing client <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

## Challenges in Achieving High Performance
Achieving [[high performance blockchains | high performance blockchains]] presents significant challenges, particularly when dealing with concurrent execution and data access <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

*   **Concurrency:** Modern machines have many cores, but most existing blockchain clients are single-core for transaction execution <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
    *   Achieving [[Parallel Execution in Blockchain | parallel execution in blockchain]] is difficult due to dependencies between transactions within a block <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. A block with 1,000 transactions is not 1,000 independent tasks <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
    *   Proper pipelining, where multiple transactions are worked on simultaneously, is crucial <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Database Performance:** The database is one of the most critical components for performance <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
    *   Waiting for disk access, which takes 30 microseconds or more, can quickly accumulate time if operations are sequential <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
    *   This sequential waiting prevents the full utilization of hardware resources, as the CPU sits idle while waiting for disk I/O <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This highlights [[challenges_of_standard_databases_in_blockchain_performance | challenges of standard databases in blockchain performance]] <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

### Monad's Innovations in Performance
Monad's main innovations focus on continuously keeping the machine busy and preventing the CPU from waiting <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   **Custom Database:** Monad built its own database ([[Monad DB and its Role in Efficient Blockchain Operations | Monad DB]]) specifically to address the bottlenecks caused by disk access <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This is a key [[Unique database optimizations in blockchains | unique database optimization in blockchains]] <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Pipelined Architecture:** Monad employs a highly pipelined architecture, akin to a "washing machine" analogy <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Just as one might wash, dry, and fold different loads of laundry concurrently, Monad processes multiple steps of different transactions simultaneously <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This contrasts with simple parallel execution where transactions run side-by-side, instead opting for an offset, pipelined approach <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Resource Utilization:** The goal is to always keep the CPU doing something, optimizing as much as possible to maintain busyness <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

> "The difference between building a system that works and a system that's really optimized... it's like going from one to one hundred." <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>

## Benchmarking and Real-World Usage
Monad emphasizes benchmarking with real-world transaction data, specifically replaying [[Ethereum Virtual Machine optimizations | Ethereum Virtual Machine optimizations]] (EVM) history, to ensure performance under actual user conditions <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

*   **Misleading Metrics:** Many projects report high Transactions Per Second (TPS) figures, but these often involve simple native token transfers or ERC-20 transfers <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
    *   Native transfers are the simplest for a blockchain to do, with some single-core clients achieving 50,000 TPS on such artificial benchmarks <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.
    *   More complex transactions, like those involving AMMs, lending protocols, or expensive ZK proofs, are far more taxing on the system <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
*   **Monad's Standard:** Monad aims to handle real usage, even optimizing for historically expensive computations like ZK proofs <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>.
*   **False Marketing:** The space often suffers from misleading marketing regarding performance metrics <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. Tricks include:
    *   Manipulating the nature of transfers or transactions <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
    *   Using high-end hardware for benchmarking <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.
    *   Centralizing stake weight in one geographic location to speed up consensus, despite having nodes distributed globally <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.
    *   Violating the laws of physics, implying unrealistic data transmission times <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>.
*   **Monad's Approach to Robustness:** Monad intentionally sets up highly stake-weighted nodes in diverse geographical locations (e.g., Singapore, New York) to test and optimize performance under worst-case conditions <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>.

## Unlocking New Applications
[[Blockchain scalability and highperformance systems | Blockchain scalability and high-performance systems]] unlock new possibilities for developers and users. Monad envisions itself as a [[high performance blockchains | high-performance blockchain]] that offers shared global state with built-in payment rails and programmability <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

This infrastructure is designed to support millions or hundreds of millions of users who already have assets and digital identities on-chain <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

Specific verticals enabled by Monad's performance include:
*   **High-Fidelity DeFi:** Enabling personal finance at scale with cheap transaction fees and low slippage, leading to more efficient markets <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
*   **Consumer Space:** Supporting applications that need to scale to hundreds of millions of users with over a billion transactions per day <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. This includes areas like DePIN (Decentralized Physical Infrastructure Networks) with price-sensitive data pushing <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>.
*   **Simplified User Experience:** Monad's low transaction costs make it easier for applications to sponsor gas fees, abstracting away a significant barrier for users and enabling sustainable business models for developers <a class="yt-timestamp" data-t="00:37:28">[00:37:28]</a>.

## Public Testnet: The Starting Line
The launch of Monad's public testnet is seen not as a finish line, but as the "crossing the starting line" for continued innovation and growth <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

*   **Devnet vs. Testnet:** The devnet served as an early feedback loop for infrastructure providers to identify missing features and usage patterns <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>. The public testnet is a new phase, allowing broader community participation and testing <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.
    *   During devnet, a team sent 3 trillion gas of usage (equivalent to about 30 days of Ethereum throughput) in a few hours, simulating complex exchange orders <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
*   **Anticipated Use Cases:** The testnet will reveal unanticipated use patterns <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>. Examples include:
    *   Large-scale NFT mints <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>.
    *   High concurrency from geographically spread users <a class="yt-timestamp" data-t="00:27:45">[00:27:45]</a>.
    *   Potential for AI agents to interact with the network <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>.
*   **Graceful Degradation:** The goal is for the system to handle stress gracefully and degrade smoothly rather than failing outright or providing poor user experiences (e.g., reverted transactions, RPC errors) <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.
*   **Long-Term Vision:** Monad has a "massive queue of ideas" for future optimizations, rewrites for even better performance, new features for usability and privacy, and increased decentralization to support thousands of nodes <a class="yt-timestamp" data-t="00:48:59">[00:48:59]</a>. This journey is seen as a long-term evolution, akin to constantly reinventing a high-performance trading system <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>.
*   **Beyond Go-to-Market:** Unlike many projects that focus on marketing existing codebases, Monad believes in bringing real, innovative technology to market as the start of a broader effort to drive crypto adoption <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>.