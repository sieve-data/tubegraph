---
title: Performance and scalability of EVM chains
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

The public testnet for Monad is going live, serving as a showcase for its underlying technology in achieving [[Scalability and performance of crypto networks | scalability and performance in crypto networks]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This launch is seen not as a finish line, but as a starting line for further innovation <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Monad's "Build From Scratch" Approach

Monad has taken a unique approach by building its protocol entirely from the ground up, rather than forking existing open-source projects <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This was done to gain greater technical control over the product <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, allowing for specific implementations of core functionalities like memory allocation and disk interaction to maximize [[Optimizing Ethereum Virtual Machine performance | performance]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Why Others Haven't Adopted This Approach
While some projects have improved performance in areas like state sync, a focus on raw execution performance for EVM chains has been rare <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This is largely because Ethereum itself is "arbitrarily rate-limited" to low throughput to maintain low node requirements <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Monad, however, was envisioned as a high-performance EVM chain from the start, with the primary restriction being 100% EVM compatibility <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Another goal was to target consumer-grade nodes (around $1,000 PCs) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

Building from scratch is also an inherently difficult and massive undertaking, requiring specialized low-level system engineers <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. These engineers are typically found in large tech companies, silicon manufacturers, or high-frequency trading firms, making them hard to come by in the blockchain space <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Technical Innovations for Performance
The main [[Technical challenges and solutions in blockchain performance | technical challenges]] in achieving high performance include:
*   **Concurrent Execution:** Modern machines have many cores, but most existing EVM clients are single-core for transaction execution <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **Transaction Dependencies:** Transactions within a block are not entirely independent tasks; there are dependencies that complicate [[Parallelization in blockchain technologies | parallelization]] <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Disk Access Latency:** Waiting for disk access (which can take 30 microseconds or more) causes the CPU to sit idle, significantly slowing down sequential operations <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

Monad's key innovations focus on keeping the machine busy and [[Optimizing Ethereum Virtual Machine performance | optimizing EVM implementations]] <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. This involves:
*   **Pipelining:** Employing a highly pipelined architecture, akin to doing multiple steps of a process (like laundry) across multiple objects simultaneously, rather than completing one entirely before starting the next <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This contrasts with simple [[parallel_evm_and_blockchain_optimizations | parallel execution]] where transactions might run side-by-side without an offset <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Custom Database:** Building a custom database to minimize CPU waiting time for disk access <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Benchmarking and Misleading Metrics
Measuring [[Performance gains in blockchain transactions | blockchain performance]] accurately is challenging due to widespread misleading marketing <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.
*   **Simplicity of Token Transfers:** The simplest task for a blockchain is native token transfers <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. Even unoptimized, single-core clients can achieve 50,000 transactions per second (TPS) on artificial benchmarks of simple token transfers <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>. Claims of 10,000 TPS for token transfers are not impressive as they are "easily achievable" <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.
*   **Real-World Usage:** Real Ethereum history, including complex transactions like AMMs, lending protocols, and ZK proofs (which can cost $500 per transaction), is far more taxing <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. Monad's benchmarks aim to handle this real usage <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>.
*   **Deceptive Practices:** Other ways projects manipulate performance metrics include:
    *   Using high-end hardware <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.
    *   Geographic collocation of nodes or concentrating stake weight in one location, which can artificially boost consensus speeds by circumventing the physics of data propagation <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.
    *   High bandwidth requirements for nodes <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>.
    Monad intentionally tests worst-case conditions by setting up highly stake-weighted nodes in distant locations (e.g., Singapore and New York) to optimize for real-world decentralization and robust performance <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>.

## What Monad Unlocks
Monad aims to provide a highly performant version of shared global state with built-in payment rails and programmability <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This infrastructure is designed to enable new applications and user experiences that require high throughput:
*   **High-Fidelity DeFi:** Facilitating personal finance at scale for hundreds of millions of users with cheap transaction fees and low slippage, allowing liquidity providers to offer efficient on-chain markets <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
*   **Consumer Space:** Supporting consumer-facing applications that need to scale to hundreds of millions of users and require billions of transactions per day <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.
*   **Simplified User Experience:** Enabling applications to sponsor gas fees for users, making transactions feel free, which requires very low underlying gas costs <a class="yt-timestamp" data-t="00:37:02">[00:37:02]</a>.
*   **DePIN (Decentralized Physical Infrastructure Networks):** Lowering the cost of entry for business models in DePIN, such as marketplaces for health data or device data, where consumers contribute resources (compute, cameras) to a broader network <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>.

This represents a bet on application builders leveraging performant infrastructure for growth, driven by a "monotonically increasing" trend in crypto adoption <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

## Public Testnet vs. Devnet
The Devnet's purpose was to gather early feedback, continuously run internal replays, and analyze performance metrics like TPS and gas per second <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. It provided a feedback loop for identifying unanticipated use patterns and necessary fixes <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. One team sent 3 trillion gas (equivalent to about 30 days of Ethereum throughput) through Devnet in just a few hours <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.

The Public Testnet marks a new phase <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. It is designed for wider public access, allowing real users to test applications, potentially uncover new, unanticipated stress scenarios like large-scale NFT mints or AI agents spamming the network <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>. The goal is to observe how the system gracefully handles being pushed to its limits without failing or degrading user experience with errors <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.

## Goals of the Public Testnet
For Category Labs, the goal is to exercise the technology, gain more feedback on the client's strengths and weaknesses, and identify areas for future work <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>.

For the Monad Foundation and the community, the public testnet aims to:
*   Showcase the power of the technology and the applications built on top of it <a class="yt-timestamp" data-t="00:33:38">[00:33:38]</a>.
*   Generate excitement and allow users to experience what high performance enables <a class="yt-timestamp" data-t="00:34:07">[00:34:07]</a>.
*   Serve as the "starting line" where Monad's capabilities become publicly apparent <a class="yt-timestamp" data-t="00:34:48">[00:34:48]</a>.
*   Attract new developers and foster ecosystem growth by enabling teams to deploy and get user feedback <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>.

## Misconceptions About Monad and Blockchain Development
A common misconception in the crypto space is that launching a testnet or mainnet is the "finish line" for a protocol, leading to a lack of further innovation or growth <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>. Many believe that "technology doesn't matter" or that "go-to-market is more important than technology," leading to minor changes to existing codebases without significant technological advancement <a class="yt-timestamp" data-t="00:51:41">[00:51:41]</a>.

Monad, however, views its public launch as merely the "starting line" <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a>. The team has a "massive queue of ideas" for future optimizations, rewrites, research, new features for usability and privacy, and increasing decentralization to support thousands of nodes (matching Ethereum and Solana) <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>. Their long-term vision involves many years of continuous innovation, focusing on delivering high performance and full backward compatibility as a foundational layer for broader crypto adoption <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a>.