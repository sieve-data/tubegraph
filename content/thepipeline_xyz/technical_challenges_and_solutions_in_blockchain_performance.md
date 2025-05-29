---
title: Technical challenges and solutions in blockchain performance
videoId: kjZShZB_7v0
---

From: [[thepipeline_xyz]] <br/> 

## Monad's Performance Claims
Monad aims to deliver a blockchain with high performance, featuring 10,000 transactions per second (TPS), full 100% EVM compatibility, sub-cent gas fees, and hardware requirements similar to Ethereum itself <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. These engineering feats have been considered impossible by many crypto participants <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Leveraging Modern Hardware
The foundation of Monad's performance lies in effectively utilizing modern hardware <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Recent advancements in SSD drives and PCI Express (PCIe 4 and 5) offer impressive bandwidth, storage capacity, and low latency <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

However, simply having powerful hardware is not enough. The key is to build software specifically designed to take advantage of these capabilities <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Relying on out-of-the-box database or file system software introduces significant algorithmic overhead and complexity, as these general-purpose tools are not optimized for specialized, high-performance use cases <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Specialized Software Development
Inspired by high-frequency trading (HFT) environments, Monad's approach involves building everything from scratch at a very low level <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This means not relying on the operating system for core functionalities and deeply understanding how hardware behaves <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Different SSD drives, for example, exhibit varying behaviors, requiring extensive benchmarking and tuning to optimize performance <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This process is a massive undertaking, often consuming days or even weeks of engineering time to diagnose and resolve performance issues <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Nevertheless, achieving even a 10% increase in TPS makes the effort worthwhile <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Understanding EVM Usage Patterns
Optimizing an EVM-compatible blockchain also requires a deep understanding of how users interact with the EVM, including common patterns of ERC20 contracts and Uniswap <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. This involves analyzing:
*   **Transaction patterns**: How transactions access state and are scheduled <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Autocorrelation**: The likelihood of an account being used again soon if it has been used recently <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Statistical Analysis**: Determining the relevant time window for such patterns <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

By analyzing these patterns, data structures can be arranged to capitalize on this information, rather than treating all data as uniformly accessed <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. For instance, the majority of state accesses often involve a relatively small number of accounts <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. This approach of continuous analytics and software refinement leads to ongoing improvement <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Development Stages: Devnet to Testnet
Monad's development progresses through distinct stages, currently in a "devnet" phase with 10,000 TPS running internally <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. The next macro step is launching a "testnet" <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

*   **Devnet**: An internal deployment where the software can be "a little rough around the edges" and boxes might require special, manual configuration <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
*   **Testnet**: Requires polishing the software into a product that external users can download, run, and support without needing developer intervention <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

This transition involves streamlining processes and eliminating the need for manual communication between development and deployment teams <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Simultaneously, a significant portion of the team remains focused on continuous [[Performance gains in blockchain transactions | performance optimization]], a process that is expected to continue for many years <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Why Layer 1 over Layer 2?
Monad's decision to launch as a Layer 1 (L1) rather than a Layer 2 (L2) is based on several factors:
*   **Bandwidth Constraints**: Existing data availability solutions for L2s often lack the necessary bandwidth. Monad's first version targets a 100 megabit connection, translating to about 8 usable megabytes per second of data <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Current L2 data availability is not close to this, which would constrain Monad's ability to utilize hardware fully <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Complexity**: Building a decentralized L2 involves significant complexity with many design trade-offs that can affect user experience (UX) or other aspects <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. By building all internal components of Monad themselves in a somewhat modular fashion, they can avoid much of this complexity <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Control and Performance**: Being an L1 provides full control over the system, ensuring the necessary performance levels are met <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. Launching as an L1 also simplifies decentralization and improves UX <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

## Competitive Advantage and Ground-Up Development
Monad's competitive advantage stems from its team's experience in HFT, which involves building low-latency systems <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. Upon evaluating existing L1s (and later L2s), the team found that many had made different trade-offs or copied components, rather than building from the ground up <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. Building from scratch provides more control and allows for the creation of a faster system when combined with specialized expertise <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

## Biggest Technical Challenge: The Database
The most significant [[challenges_in_blockchain_system_design | technical challenge]] encountered during Monad's development has been the database <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. Unlike HFT systems, which typically operate in memory without touching disk for long periods <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>, blockchain states can be tens to hundreds of gigabytes, necessitating disk storage <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

This required the team to learn about new technologies they were not personally familiar with, including SSD internal architecture and state-of-the-art storage solutions <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. Extensive experimentation and benchmarking of open-source databases like RocksDB, LevelDB, and LMDB were necessary to understand their limitations <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. In contrast, the VM and transaction execution aspects were closer to their HFT background, making them easier to develop <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

## Unlocking New Use Cases
The Monad team is most excited about seeing new applications built on their high-performance blockchain <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>. The hope is that application teams will leverage Monad's performance to build applications that were previously not feasible <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>. This validation of their work will also lead to learning opportunities through collaboration with application developers <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

High performance in a blockchain not only allows for more users but also enables greater complexity within transactions and applications themselves <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. This means an application per user can do more work than on a less performant chain <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. The goal is to open up new application possibilities and use cases, allowing developers to build innovative solutions that ultimately benefit the user experience through speed, low fees, reliability, and the ability to land transactions <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a> <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.