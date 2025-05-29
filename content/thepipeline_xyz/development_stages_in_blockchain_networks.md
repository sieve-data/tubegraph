---
title: Development stages in blockchain networks
videoId: kjZShZB_7v0
---

From: [[thepipeline_xyz]] <br/> 

The development of high-performance blockchain networks like [[monad_blockchain_development | Monad]] involves distinct stages and significant engineering efforts, often tackling problems previously deemed impossible <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Core Engineering Philosophy

The engineering approach emphasizes deeply understanding and optimizing for modern hardware capabilities, such as impressive SSD drives, PCI-E4, and PCI-E5 bandwidth <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. To achieve maximum performance, it is crucial to avoid relying on general-purpose, "out-of-the-box" software like standard database or file system software, which often has algorithmic overhead and is optimized for general use cases rather than specialized high-performance needs <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

Instead, developers must:
*   **Specialize and build from scratch** <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Build everything very low-level**, avoiding reliance on the operating system to perform tasks <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Understand hardware behavior**, even down to how different SSD drives perform in specific ways <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Optimize the EVM stack** by understanding how people use the EVM, including usage patterns of ERC-20 contracts and Uniswap <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This involves analyzing transaction patterns, state access, scheduling, and autocorrelation (e.g., an account used recently is likely to be used again soon) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Arrange data structures** to leverage analytical insights into usage patterns <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

This process is a continuous cycle of improvement, often requiring days or weeks of engineering time to resolve specific performance issues <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Development Stages

### Devnet (Development Network)

The Devnet is an internal deployment phase <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. During this stage:
*   The software can be "a little rough around the edges" <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   Manual configuration of systems is acceptable <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   Internal communication between development and deployment teams handles issues <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   For [[monad_blockchain_development | Monad]], the Devnet currently achieves 10,000 transactions per second (TPS) internally with full 100% EVM compatibility, sub-cent gas fees, and hardware requirements similar to Ethereum <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### Testnet (Test Network)

Moving from Devnet to Testnet requires significant polish and preparation <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. The goal is to make the software a product that external users can download, run, and use independently without needing developer support <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. This involves making the setup and usage process much smoother <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

Throughout both stages, a significant portion of the team continuously works on performance optimization, aiming to make the network even faster <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Why Build a New Layer One (L1)?

Despite the prevalence of Layer 2 (L2) solutions, [[monad_blockchain_development | Monad]] chose to launch as a new L1 due to several factors related to [[scaling_blockchain_ecosystems | scaling blockchain ecosystems]] and [[challenges_in_blockchain_system_design | challenges in blockchain system design]]:

*   **Bandwidth Constraints**: Existing L2 data availability solutions do not offer the necessary bandwidth. A new L1 like [[monad_blockchain_development | Monad]] can target higher connection speeds (e.g., 100 megabits) to fully utilize hardware potential <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Complexity**: Building a decentralized L2 involves significant complexity and trade-offs in design <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. By building all components of [[monad_blockchain_development | Monad]] internally and modularly, much of this external complexity is avoided <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
*   **Control and Performance**: Building everything from scratch provides full control over the system, ensuring the necessary performance is achieved <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **User Experience (UX)**: An L1 can offer a simpler and better user experience by avoiding the complexities inherent in multi-chain interactions (e.g., one chain for data, another for execution) <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

The decision to build a new L1 was driven by a competitive advantage stemming from experience in high-frequency trading (HFT), which involves building extremely low-latency systems <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This expertise allows for building something faster than existing L1s and L2s, many of which had made trade-offs or copied components <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

## Challenges in Development

Developing a high-performance blockchain like [[monad_blockchain_development | Monad]] presents significant [[challenges_in_blockchain_system_design | challenges in blockchain system design]]:

*   **Database Management**: A major technical challenge is handling the database. Unlike HFT systems that operate purely in memory, blockchains must store tens to hundreds of gigabytes of state data on disk <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. This requires learning new technologies, extensive experimentation, and benchmarking existing open-source databases (like RocksDB, LevelDB, LMDB) to understand their limitations <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
*   **Talent Acquisition**: A non-technical challenge is finding and hiring skilled people in a competitive employment market, competing with big tech companies and the finance sector <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

## Future Outlook

The ultimate goal of these development efforts is to enable the creation of "cool apps" that leverage the network's high performance <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. This will provide validation for the hard work put in and foster collaboration with application teams to improve the user experience <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.

The enhanced performance unlocks new use cases and application possibilities that were previously unfeasible on lower-performing chains <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>. This not only allows for [[scaling_blockchain_ecosystems | scaling blockchain ecosystems]] to more users (e.g., supporting 10,000 users on an order book instead of 1,000) but also increases the complexity and richness of applications per user <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. The anticipation for these new applications marks the next exciting stage of [[future_potential_of_blockchain_applications_and_adoption | blockchain adoption]] <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.