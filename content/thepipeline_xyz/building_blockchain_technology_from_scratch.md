---
title: Building blockchain technology from scratch
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

[[monad_blockchain_development | Monad]] has adopted a unique strategy by building its protocol entirely from the ground up, rather than forking an existing open-source project <a class="yt-timestamp" data-t="01:46:27">[01:46:27]</a>. This approach ensures greater technical control and allows for very specific implementations that optimize performance <a class="yt-timestamp" data-t="02:06:09">[02:06:09]</a>.

## Why Build From Scratch?

Building a blockchain from scratch provides more technical control over the product <a class="yt-timestamp" data-t="02:04:47">[02:04:47]</a>. While forking an open-source project allows leveraging existing work, [[monad_blockchain_development | Monad]] anticipated needing to modify so many aspects that it would not have benefited from ongoing maintenance or new features of a forked project <a class="yt-timestamp" data-t="02:17:17">[02:17:17]</a>. This ground-up approach allows for precise control over memory allocation, disk interaction, and other low-level system details to achieve optimal performance <a class="yt-timestamp" data-t="02:41:09">[02:41:09]</a>.

The decision to build from scratch also addresses the historical context of Ethereum's design, which was deliberately rate-limited to maintain low node requirements <a class="yt-timestamp" data-t="04:06:07">[04:06:07]</a>. In contrast, [[monad_blockchain_development | Monad]] was envisioned as a high-performance EVM chain with no design restrictions other than 100% EVM compatibility <a class="yt-timestamp" data-t="04:24:47">[04:24:47]</a>. The goal was to maximize network and hardware performance while still targeting consumer-grade nodes, achievable with a PC costing around $1,000 <a class="yt-timestamp" data-t="04:50:35">[04:50:35]</a>.

Building such a system is inherently difficult, requiring highly skilled low-level system engineers who are rare in the general development community <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

## Technical [[challenges_in_blockchain_system_design | Challenges in Blockchain System Design]] and [[technical_challenges_and_solutions_in_blockchain_performance | Solutions]]

The main [[challenges_in_blockchain_system_design | challenges]] in building [[monad_blockchain_development | Monad]] revolved around achieving concurrent execution to leverage multi-core machines <a class="yt-timestamp" data-t="06:16:34">[06:16:34]</a>. Most existing clients are single-core for transaction execution <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>. Key [[technical_challenges_and_solutions_in_blockchain_performance | innovations]] include:

*   **[[parallelization_in_blockchain_technologies | Pipelined Execution]]**: Overcoming dependencies between transactions in a block to work on multiple transactions simultaneously <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>. This is likened to a "washing machine" analogy, where different loads are processed in parallel stages (washing, drying, folding) to increase throughput <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>.
*   **Database Optimization**: Eliminating delays from disk access, which can be significant (30 microseconds or more) <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>. [[monad_blockchain_development | Monad]]'s database design ensures the CPU is constantly busy, minimizing idle time spent waiting for disk I/O <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>.
*   **Constant Machine Utilization**: The core [[innovation_in_blockchain_technology_and_applications | innovation]] in [[monad_blockchain_development | Monad]] is to keep the machine busy, minimizing waiting times, especially for disk access <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.

This intense optimization represents the "1 to 100" stage of [[innovation_in_blockchain_technology_and_applications | innovation]], similar to evolving the Wright brothers' first airplane into a modern, highly optimized jet <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.

## What [[monad_blockchain_development | Monad]] Unlocks

[[monad_blockchain_development | Monad]] aims to provide a performant version of shared global state with built-in payment rails and programmability, enabling applications to reach millions or hundreds of millions of users <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>. This includes:

*   **High-Fidelity DeFi**: Enabling personal finance at scale with cheap transaction fees and low slippage, fostering efficient on-chain markets <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>.
*   **Consumer Applications**: Supporting consumer-facing applications that require [[scaling_blockchain_ecosystems | scaling]] to hundreds of millions of users, targeting over a billion transactions per day <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>. This is a bet on the consistent growth of crypto adoption <a class="yt-timestamp" data-t="15:23:00">[15:23:00]</a>.
*   **Sponsored Gas Fees**: Facilitating applications that sponsor gas fees for users, making the user experience simpler and enabling new business models where transaction costs are a fraction of a cent <a class="yt-timestamp" data-t="37:11:00">[37:11:00]</a>. This is particularly relevant for DePIN (decentralized physical infrastructure networks) spaces, such as marketplaces for health data or device-contributed compute/data <a class="yt-timestamp" data-t="38:18:00">[38:18:00]</a>.
*   **Unpredictable Applications**: Just as the internet's bandwidth improvements led to unforeseen applications like YouTube and Instagram, [[monad_blockchain_development | Monad]]'s performance could enable entirely new types of applications, such as AI agents or complex inscription activities <a class="yt-timestamp" data-t="42:50:00">[42:50:00]</a>.

## The Path Forward: Testnet as a Starting Line

The launch of the public testnet is viewed not as a finish line, but as a starting line <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>. It serves as a showcase of the technology and a feedback loop from early testers and infrastructure providers <a class="yt-timestamp" data-t="17:22:00">[17:22:00]</a>.

### Benchmarking Real Usage

[[monad_blockchain_development | Monad]]'s devnet facilitated significant stress testing, including a team sending 3 trillion gas worth of usage in a few hours, equivalent to about 30 days of Ethereum throughput <a class="yt-timestamp" data-t="17:53:00">[17:53:00]</a>.

A key aspect of [[monad_blockchain_development | Monad]]'s benchmarking strategy is replaying real Ethereum history, rather than simple token transfers <a class="yt-timestamp" data-t="19:39:00">[19:39:00]</a>. Simple token transfers or ERC-20 contract updates are relatively easy for blockchains to process, making high TPS (transactions per second) numbers misleading <a class="yt-timestamp" data-t="19:51:00">[19:51:00]</a>. Real-world Ethereum usage involves complex smart contracts, AMMs, lending protocols, and expensive computations like ZK proofs, which are far more taxing <a class="yt-timestamp" data-t="21:26:00">[21:26:00]</a>. [[monad_blockchain_development | Monad]] aims to handle this "real usage" effectively <a class="yt-timestamp" data-t="22:34:00">[22:34:00]</a>.

### Rejecting Misleading Metrics

[[monad_blockchain_development | Monad]] deliberately avoids deceptive benchmarking practices common in the space, such as:
*   Artificially simple transaction types <a class="yt-timestamp" data-t="22:56:00">[22:56:00]</a>.
*   Using extremely high-end, inaccessible hardware <a class="yt-timestamp" data-t="23:02:00">[23:02:00]</a>.
*   Manipulating node geographic distribution or stake weight to appear decentralized while centralizing consensus <a class="yt-timestamp" data-t="23:04:00">[23:04:00]</a>.

Instead, [[monad_blockchain_development | Monad]] intentionally tests worst-case scenarios, like highly stake-weighted nodes in distant geographical locations (e.g., Singapore and New York), to optimize performance under challenging conditions <a class="yt-timestamp" data-t="25:35:00">[25:35:00]</a>. The focus is on using [[technology_focus_and_pragmatism_in_blockchain_development | technology]] to advance the decentralization-performance tradeoff curve <a class="yt-timestamp" data-t="24:40:00">[24:40:00]</a>.

### Continuous [[innovation_in_blockchain_technology_and_applications | Innovation]]

The public testnet's goal is to exercise the [[monad_blockchain_development | Monad]] technology, gather feedback, and identify areas for further optimization <a class="yt-timestamp" data-t="32:45:00">[32:45:00]</a>. While aiming for seamless user experiences even under stress (e.g., graceful degradation instead of errors during NFT mints), the team recognizes that continuous improvement is necessary <a class="yt-timestamp" data-t="29:05:00">[29:05:00]</a>.

[[monad_blockchain_development | Monad]]'s team has a "massive queue of ideas" for ongoing optimizations, rewrites, research, and new features like usability, privacy, and increased decentralization <a class="yt-timestamp" data-t="48:59:00">[48:59:00]</a>. While the client will support hundreds of nodes at launch, the long-term goal is to reach thousands, on par with Ethereum and Solana <a class="yt-timestamp" data-t="49:31:00">[49:31:00]</a>. This long-term vision emphasizes that the launch is just the beginning of many years of [[innovation_in_blockchain_technology_and_applications | innovation]] and work <a class="yt-timestamp" data-t="50:09:00">[50:09:00]</a>. This reflects [[technology_focus_and_pragmatism_in_blockchain_development | a focus on real technological innovation]] rather than merely a go-to-market strategy <a class="yt-timestamp" data-t="52:35:00">[52:35:00]</a>.

The public testnet also serves as a showcase for applications already built on [[monad_blockchain_development | Monad]], generating excitement within the crypto space and inviting more builders to leverage its performance capabilities <a class="yt-timestamp" data-t="33:38:00">[33:38:00]</a>. It's the first time the network is openly available, allowing anyone to test it and see its real-world performance <a class="yt-timestamp" data-t="34:46:00">[34:46:00]</a>.