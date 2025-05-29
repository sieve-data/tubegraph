---
title: Introduction to Monad and its capabilities
videoId: kjZShZB_7v0
---

From: [[thepipeline_xyz]] <br/> 

Monad, co-founded by James Hunsaker, who is also its CTO and considered the "Godfather of the parallel EVM," has garnered significant attention and even disbelief within the community due to its ambitious capabilities <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Core Capabilities

Monad aims to deliver performance previously thought impossible in the crypto space <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Its key capabilities include:
*   **High Transaction Throughput:** 10,000 transactions per second (TPS) <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Full EVM Compatibility:** 100% compatibility with the Ethereum Virtual Machine (EVM) <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **Low Transaction Costs:** Sub-cent gas fees <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Accessible Hardware Requirements:** Hardware requirements are very similar to Ethereum <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Engineering Philosophy and Achievements

The Monad team's ability to achieve these engineering feats stems from a specialized approach to software development, rooted in experience with high-frequency trading (HFT) <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a> <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### Leveraging Modern Hardware
Monad's performance is built upon taking full advantage of modern hardware, such as impressive SSD drives and high-bandwidth PCI E4/E5 interfaces <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Unlike general-purpose software that optimizes for broad use cases, Monad specializes its software to maximize performance <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This involves:
*   **From-Scratch Development:** Building everything from the ground up, at a very low level, without relying on operating system functionalities or "out-of-the-box" database software and file systems, which introduce algorithmic overhead <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Deep Hardware Understanding:** Focusing on how hardware behaves, including extensive benchmarking of different SSD drives to understand their specific performance nuances <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a> <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This process can be time-consuming, sometimes taking days or weeks of engineering effort to resolve performance issues <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

### EVM Optimization and Data Analytics
Beyond hardware, Monad deeply understands the EVM stack and user interaction patterns <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This includes:
*   **Usage Pattern Analysis:** Analyzing how the blockchain is used, such as common usage patterns for ERC20 contracts and Uniswap <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Transaction Behavior:** Understanding transaction patterns, how they access state, how they are scheduled, and the relationships between transactions across blocks, including autocorrelation (e.g., an account recently used is likely to be used again soon) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a> <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Statistical Analysis:** Conducting statistical analysis to determine the extent of these patterns and arranging data structures to take advantage of this information, avoiding uniform access assumptions <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a> <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Continuous Improvement:** This process involves a continuous cycle of analytics, building optimized data structures and software, and ongoing performance optimization <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a> <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Challenges Faced
One of the biggest technical challenges for Monad has been developing its database <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. Unlike HFT systems that primarily run in memory and rarely touch the disk, blockchain state sizes (tens to hundreds of gigabytes) necessitate robust disk storage <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a> <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. This required learning new technologies, extensive experimentation, and benchmarking open-source databases like RocksDB, LevelDB, and LMDB to understand their limitations <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a> <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

## Development Phases: Devnet to Testnet

Monad is currently in its "devnet" phase, where 10,000 TPS is already running internally <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a> <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. The next major step is transitioning to "testnet" <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   **Devnet:** An internal deployment where the software might be "rough around the edges" and boxes require manual, special configuration <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. There's direct communication between developers and deployment teams <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Testnet:** Requires significant polishing to make the software a usable product for external users <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. It must be easy for people to download, run, and support without requiring developer intervention for debugging <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

## Why a Layer 1 (L1) Instead of a Layer 2 (L2)?

The Monad team chose to build an L1 rather than an L2 despite the prevalent L2 narrative in crypto <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>:
*   **Bandwidth Constraints:** Existing data availability solutions for L2s do not provide sufficient bandwidth to support Monad's target of a 100-megabit connection (8 usable megabytes per second of data) <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. Monad aims to avoid constraints and fully utilize hardware <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   **Complexity:** Building a decentralized L2 involves significant complexity due to various design trade-offs affecting user experience and other aspects <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. By building Monad's components from scratch and maintaining internal modularity, the team avoids this complexity <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Full Control & Performance:** Developing a custom L1 gives Monad full control over the system, ensuring optimal performance and decentralization <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a> <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. It also simplifies the user experience by avoiding the complexities of separate chains for data and execution <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

## Future Outlook

James Hunsaker is most excited to see applications that fully leverage Monad's performance <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>. He believes this will validate the team's work and foster collaboration with application teams to enhance user experience through speed, low fees, and reliability <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a> <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. Monad's enhanced performance is expected to unlock new use cases and applications that were previously not viable on less performant chains <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>. This includes supporting not just more users, but also more complex applications per user <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

The **Monad community** is vibrant, known for its impressive art and humor, constantly active in platforms like Discord and Telegram <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a> <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.