---
title: Building a blockchain from scratch
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

The public testnet for the Monad protocol is now live, showcasing a unique technological approach built from the ground up <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This launch is viewed not as a finish line, but as the starting line for continued development and optimization <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

## Why Build from Scratch?

Monad's decision to build its protocol completely from scratch, rather than forking an existing open-source project, stems from the desire for greater technical control and performance optimization <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.

Key reasons include:
*   **Technical Control** The "from scratch" approach allows precise control over fundamental implementations, such as memory allocation and disk interaction, which is crucial for achieving peak [[Optimizing blockchain performance | performance]] <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
*   **Avoiding Forking Limitations** While forking an open-source project can leverage existing work, Monad anticipated needing to modify so many aspects that ongoing maintenance and new feature development would become impractical <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   **High Performance Vision** Unlike Ethereum, which is "arbitrarily rate-limited" to low throughput for various reasons (e.g., low node requirements), Monad was envisioned as a high-performance EVM chain from the outset, with no design space restrictions other than 100% EVM compatibility <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.
*   **Difficulty** Building such a system is inherently challenging, requiring specialized low-level system engineers who are difficult to find, as they typically work in big tech, silicon manufacturing, or high-frequency trading firms <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

## [[Challenges and innovations in blockchain development | Challenges and Innovations]]

Monad's development focused on overcoming significant technical hurdles to maximize throughput and efficiency.

### Core Challenges & Solutions
*   **Concurrent Execution** Modern machines have multiple cores, but most existing blockchain clients are single-core for transaction execution. Monad aims to leverage these cores for concurrent execution, which is complicated by dependencies between transactions within a block <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.
*   **Database Optimization** The database is a critical component, as waiting for disk access (which can take 30 microseconds or more) can quickly add up and leave the CPU idle. Monad built its own database to keep the CPU constantly busy and avoid these bottlenecks <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.
*   **[[Optimizing blockchain performance | Pipelining]] Architecture** This approach, likened to a "washing machine" analogy (where washing, drying, and folding different loads happen concurrently), involves doing multiple steps of a process across multiple objects simultaneously. Monad's highly pipelined architecture always tries to keep the machine busy, even when waiting for disk access <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.

### The "Zero to One" vs. "One to 100" Analogy
Developing a functional distributed system like Ethereum was a "zero to one" innovation, enabling smart contracts and permissionless global finance <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. However, it left a lot of "slack" in the system, with a 12-second block budget. Monad represents the "one to 100" step, focusing on [[Performance and scalability of blockchain systems | performance engineering]] to achieve much higher throughput and cheaper transactions <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>.

## What Monad Unlocks

Monad aims to provide a highly [[need for performant blockchains | performant]] version of shared global state, complete with built-in payment rails and programmability. This foundation allows developers to build and distribute applications to millions of users who already possess on-chain assets and digital identities <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>.

Specific verticals and opportunities Monad hopes to unlock:
*   **High-Fidelity DeFi** Enabling personal finance to scale to hundreds of millions of users with extremely low transaction fees and reduced slippage. This allows liquidity providers to create highly efficient markets on fully on-chain exchanges <a class="yt-timestamp" data-t="13:45:00">[13:45:00]</a>.
*   **Consumer-Facing Applications** Applications targeting a massive consumer base (hundreds of millions of users) require the scale Monad provides, with capabilities for over a billion transactions per day <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>.
*   **New Business Models** By making gas fees extremely cheap, Monad enables application developers to easily sponsor gas for users, reducing the cost burden and unlocking new business models, particularly in the DePIN (Decentralized Physical Infrastructure Networks) space <a class="yt-timestamp" data-t="37:28:00">[37:28:00]</a>.

Monad's long-term vision extends beyond launch, with a "massive queue of ideas" for future optimizations, rewrites, research, and new features focusing on usability, privacy, and further decentralization to support thousands of nodes <a class="yt-timestamp" data-t="49:09:00">[49:09:00]</a>.

## Testnet vs. Devnet & Benchmarking Standards

The public testnet differs from the earlier devnet, which primarily served as a feedback loop for early testers and infrastructure providers <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>. On the devnet, a team simulated 3 trillion gas usage over a few hours, equivalent to about 30 days of Ethereum's throughput <a class="yt-timestamp" data-t="17:53:00">[17:53:00]</a>.

Monad emphasizes realistic benchmarking:
*   **Real Usage Replay** Monad uses replayed Ethereum history for benchmarking to simulate real user activity and complex transaction patterns, not just simple token transfers <a class="yt-timestamp" data-t="19:39:00">[19:39:00]</a>.
*   **Avoiding Misleading Metrics** Simple native token transfers are easy for any blockchain to process, with even unoptimized single-core clients achieving 50,000 transactions per second (TPS) on artificial benchmarks <a class="yt-timestamp" data-t="19:51:00">[19:51:00]</a>. Monad's goal is to handle the more complex and expensive computations seen on real Ethereum, including AMMs, lending protocols, and ZK-proofs <a class="yt-timestamp" data-t="21:26:00">[21:26:00]</a>.
*   **Decentralization vs. Performance** Monad rejects "tricks" used by some projects to inflate TPS numbers, such as co-locating nodes, using extremely high-spec hardware requirements, or centralizing stake weight <a class="yt-timestamp" data-t="23:13:00">[23:13:00]</a>. Instead, Monad intentionally tests worst-case scenarios with geographically distributed and highly stake-weighted nodes to ensure robustness and decentralization while pushing the performance curve <a class="yt-timestamp" data-t="25:59:00">[25:59:00]</a>.

## Goals of the Public Testnet

The public testnet serves multiple purposes:
*   **Technology Exercise** It allows for real-world usage of the client to identify strengths and weaknesses and determine areas for further optimization <a class="yt-timestamp" data-t="32:47:00">[32:47:00]</a>.
*   **Showcase** It demonstrates the power of Monad's technology and the applications built upon its high-performance capabilities <a class="yt-timestamp" data-t="33:34:00">[33:34:00]</a>.
*   **Community Engagement** It provides an opportunity for the community to interact directly with the chain, test applications, and attract new builders and users <a class="yt-timestamp" data-t="34:07:00">[34:07:00]</a>.
*   **Unanticipated Usage Patterns** While internal testing covers many scenarios, the testnet is expected to reveal new and unpredictable usage patterns (e.g., mass NFT mints, AI agents spamming transactions) that will inform future optimizations <a class="yt-timestamp" data-t="27:50:00">[27:50:00]</a>. The aim is for the system to degrade gracefully under load rather than failing completely <a class="yt-timestamp" data-t="29:05:00">[29:05:00]</a>.

The launch of the testnet is not merely a milestone but the beginning of a long journey of innovation and growth, driven by a long-term vision to continually enhance the [[blockchain for beginners | blockchain]]'s performance and decentralization capabilities <a class="yt-timestamp" data-t="50:50:00">[50:50:00]</a>.