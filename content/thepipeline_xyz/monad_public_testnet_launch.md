---
title: Monad public testnet launch
videoId: YCxOcA3ysX4
---

From: [[thepipeline_xyz]] <br/> 

The Monad public testnet is officially going live, marking a significant milestone that showcases the technology built over several years <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While the launch of a testnet or mainnet is often seen as "crossing the finish line" for many protocols, the Monad team views it as "crossing the starting line," signifying the beginning of continuous innovation and growth <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Purpose of the Public Testnet

The [[monad_testnet_introduction_and_setup | public testnet]] serves multiple key purposes:
*   **Technology Showcase**: It demonstrates the power and capabilities of the underlying Monad technology <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
*   **Feedback and Optimization**: From a technical perspective, it allows for real-world usage to gather feedback on the client, identify weaknesses, and determine areas for further optimization <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
*   **Application Showcase**: It highlights the various applications that have been developed on Monad, leveraging its performance capabilities <a class="yt-timestamp" data-t="00:33:45">[00:33:45]</a>.
*   **Community Engagement**: The testnet provides an opportunity for the community to actively engage with the protocol, test applications, and contribute to its growth <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a> <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>.
*   **Attracting Builders**: It aims to attract new developers and teams who were waiting for the testnet to launch, showcasing Monad as a powerful platform for pushing the limits of what's possible in crypto <a class="yt-timestamp" data-t="00:35:31">[00:35:31]</a>.

## Devnet vs. Public Testnet

The [[monads_devnet_launch_and_its_significance | devnet]] was primarily used for early feedback from testers and infrastructure providers, helping to identify missing features or unexpected usage patterns <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>. The Monad team constantly runs internal replays, gathering metrics on TPS (transactions per second) and gas per second, with the devnet providing an additional feedback loop <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a> <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

One notable use case on the devnet involved a team simulating 3 trillion gas usage, equivalent to about 30 days of Ethereum throughput, in just a few hours <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a> <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. This showcased Monad's ability to handle complex, high-volume scenarios that cannot exist in other environments <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a> <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

### Benchmarking with Real Usage

Unlike other projects that might boast high TPS numbers based on simple token transfers, Monad focuses on replaying actual Ethereum history to simulate real-world usage <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a> <a class="yt-timestamp" data-t="00:32:34">[00:32:34]</a>. Simple token transfers are "easily achievable" even by unoptimized, single-core clients <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. Monad aims to handle the complexity of DeFi protocols, lending protocols, and even gas-expensive ZK-proof transactions that appear on Ethereum <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a> <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.

The public testnet will reveal new usage patterns, such as high-stress events like [[available_applications_and_experiences_on_monad_testnet | NFT mints]] with many concurrent users, allowing the team to further optimize for graceful degradation rather than system failures <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a> <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

## Monad's Unique Approach: Building from Scratch

Monad's distinctive approach involves [[monad_blockchain_development | building everything from the ground up]] <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This decision was made to gain maximum technical control over the product <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. While forking an open-source project offers leverage over existing work, Monad found that they would have to modify so many aspects that ongoing maintenance and new features from the original project would not be beneficial <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

Building from scratch allows for:
*   **Specificity in Implementation**: Precise control over elements like memory allocation and disk interaction <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Ongoing Maintenance and Feature Development**: Greater simplicity and control for long-term development <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Optimal Performance**: The ability to implement things in a way that yields the best possible performance <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

This approach is rare because it's "really hard" and requires a team of "very smart engineers" with low-level system engineering skills, typically found in big tech, silicon manufacturing, or high-frequency trading firms <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a> <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. While other teams have improved aspects of EVM performance, they haven't focused on raw execution throughput because Ethereum is "arbitrarily rate limited" to low throughput due to its design goals, such as minimal node requirements <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a> <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Monad, however, was envisioned as a high-performance EVM chain from the outset, with the primary restriction being 100% EVM Ethereum compatibility <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Innovation and Challenges

The main challenges in Monad's development revolved around achieving concurrent execution while managing transaction dependencies within a block <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Existing clients are mostly single-core, but modern machines have many cores <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

Key innovations include:
*   **Pipelining**: Monad utilizes a highly pipelined architecture, likened to a "washing machine" analogy where multiple stages (wash, dry, fold) are processed concurrently for different loads <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This allows Monad to work on multiple transactions simultaneously, maximizing hardware utilization <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Optimized Database**: Recognizing that disk access is a major bottleneck (taking around 30 microseconds), Monad built its own database <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a> <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. The goal is to always keep the CPU busy, avoiding waiting for disk access, thereby fully leveraging hardware resources <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

Monad's development is akin to taking the "0 to 1" innovation of early airplanes (like the Wright brothers' first flight) and pushing it to "1 to 100" through intricate engineering and optimization, creating a "jet plane" from a "prop plane" <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a> <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a> <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

## What Monad Unlocks

Monad offers a highly performant version of shared global state with built-in payment rails and programmability <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This allows developers to build applications that can scale to "millions or tens or hundreds of millions of users" who already have on-chain assets and digital identities <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

Specific verticals seeing traction include:
*   **High-Fidelity DeFi**: Enabling personal finance at scale with cheaper transaction fees and low slippage, allowing liquidity providers to create efficient on-chain markets <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   **Consumer Space**: Any application targeting consumers that needs to scale to hundreds of millions of users, potentially supporting over a billion transactions per day <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a> <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This includes areas like DePIN (Decentralized Physical Infrastructure Networks) where pushing data to chain for a fraction of a cent can unlock new business models such as marketplaces for health data or device data <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>.
*   **Unpredictable Applications**: Just as early internet users couldn't foresee YouTube or Instagram, Monad expects new, currently unpredictable applications to emerge due to its speed, low cost, and EVM compatibility <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a> <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>. AI agents, for instance, are an exciting area for experimentation <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>.

Monad also emphasizes simplifying the user experience by enabling applications to sponsor gas fees <a class="yt-timestamp" data-t="00:37:02">[00:37:02]</a>. This is feasible because Monad's gas costs are exceptionally low, reducing the financial burden on developers and fostering sustainable business models <a class="yt-timestamp" data-t="00:37:30">[00:37:30]</a>.

## Addressing Misconceptions and Marketing

The Monad team acknowledges widespread misleading marketing in the blockchain space <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. Key distinctions in Monad's approach include:
*   **Real Benchmarking**: Avoiding inflated TPS numbers based on simple token transfers, instead using complex, real-world Ethereum historical data <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.
*   **Transparent Decentralization**: Rejecting "tricks" like geographically co-locating nodes or requiring high-end hardware for benchmarking to artificially boost performance <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a> <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>. Monad intentionally tests worst-case scenarios, such as highly stake-weighted nodes in distant locations (e.g., Singapore and New York), to optimize for robust performance in decentralized environments <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>.
*   **Physics-Bound Metrics**: Cautioning against metrics that seem to "violate the laws of physics," as they likely indicate an arrangement that compromises decentralization for performance <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>. Monad's goal is to push the decentralization-performance trade-off curve forward through technology, not by manipulating parameters <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.

Monad's team emphasizes the importance of a seamless user experience, where the system "just works" without users needing to understand complex technical failures <a class="yt-timestamp" data-t="00:32:22">[00:32:22]</a>. This contrasts with current crypto experiences where fragmented protocols and painful user journeys are common <a class="yt-timestamp" data-t="00:40:49">[00:40:49]</a>.

## Future Vision

The public testnet is not the "finish line" but the "starting line" for Monad <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a>. The team has a "massive queue of ideas" for optimizations, rewrites for even better performance, ongoing research, and new features focusing on usability, privacy, and greater decentralization <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a> <a class="yt-timestamp" data-t="00:49:20">[00:49:20]</a>. While the client will support hundreds of nodes at launch, the long-term goal is to scale to thousands, on par with Ethereum and Solana <a class="yt-timestamp" data-t="00:49:31">[00:49:31]</a>.

The project has a long-term vision, rooted in the founders' experience of continuously evolving high-performance trading systems for over eight years at Jump Trading <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a> <a class="yt-timestamp" data-t="00:50:21">[00:50:21]</a>. The initial focus is on delivering high performance and full backward compatibility for EVM and RPC, which alone will unlock many use cases. Beyond that, the team is excited about numerous additional improvements <a class="yt-timestamp" data-t="00:51:06">[00:51:06]</a>. Monad believes that bringing "real innovative technology" to market is the start of a broader effort to significantly impact crypto adoption <a class="yt-timestamp" data-t="00:52:35">[00:52:35]</a>.

## Get Involved!

The [[monad_testnet_introduction_and_setup | Monad public testnet]] is now available <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The community is encouraged to try it out, akin to a new city opening with immense opportunity <a class="yt-timestamp" data-t="00:58:46">[00:58:46]</a>. Everyone, from engineers to community managers and out-of-the-box thinkers, has the opportunity to play a role in Monad's growth and help it reach new heights <a class="yt-timestamp" data-t="00:59:33">[00:59:33]</a>. Users can begin by exploring [[available_applications_and_experiences_on_monad_testnet | available applications and experiences]] <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a> and learning about [[acquiring_and_using_testnet_tokens | acquiring and using testnet tokens]] and [[connecting_and_using_wallets_for_monad_testnet | connecting and using wallets]] for the testnet <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.