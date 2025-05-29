---
title: Opportunities for application development on highperformance blockchains
videoId: kjZShZB_7v0
---

From: [[thepipeline_xyz]] <br/> 

High-performance blockchains, such as Monad, are designed to unlock new possibilities for on-chain applications by offering significantly increased throughput, reduced costs, and improved user experience. These advancements are achieved through specialized engineering and a deep understanding of underlying hardware and software interactions.

## Monad's Performance Capabilities
Monad aims to deliver a blockchain with exceptional performance, boasting:
*   10,000 transactions per second (TPS) <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   Full 100% EVM compatibility <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   Sub-cent gas fees <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   Hardware requirements very similar to Ethereum <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

The development team views 10,000 TPS as just the beginning, with continuous optimization efforts planned for the future <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Engineering Feats and Technical Approach
Achieving such performance requires sophisticated engineering, often considered "impossible" by many in the crypto space <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Monad's approach involves:

### Leveraging Modern Hardware
The team capitalizes on modern hardware advancements, including impressive SSD drives and high-bandwidth PCI Express (PCIe4, PCIe5) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This requires building custom software to fully utilize the impressive storage, bandwidth, and low latency capabilities of these components <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Specializing Software and Low-Level Optimization
Unlike general-purpose database or file system software that optimize for broad use cases, high-performance blockchains demand specialized, low-level software <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This involves:
*   **Building from Scratch**: Creating every component from the ground up to gain full control and optimize for speed <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, similar to practices in high-frequency trading (HFT) <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   **Hardware Understanding**: Deeply understanding how hardware behaves, including the nuances of different SSD drives and their performance characteristics <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This involves extensive benchmarking and tuning <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **EVM Stack Optimization**: Analyzing how the EVM is used in practice, studying usage patterns of ERC20 contracts and applications like Uniswap to optimize state access and transaction scheduling <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Statistical Analysis**: Employing statistical analysis to understand relationships between transactions and account usage patterns (e.g., autocorrelation) <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. This informs the design of data structures to maximize performance by treating frequently accessed data differently from uniformly accessed data <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Continuous Improvement**: The development process is a continuous cycle of analysis, data structure design, and software refinement to maximize efficiency <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

### Technical Challenges
One of the biggest technical challenges encountered has been the database component. Unlike HFT systems that primarily run in memory, blockchains require persistent storage for large state sizes (tens to hundreds of gigabytes) <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. This necessitated extensive learning, experimentation, and benchmarking of different database technologies to understand their limitations <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

## Why a Layer 1 (L1) over Layer 2 (L2)?
While Layer 2 solutions are a prominent narrative, Monad chose to launch as a Layer 1 for several reasons:
*   **Bandwidth Constraints**: Existing L2 data availability solutions do not offer the necessary bandwidth to support the high throughput Monad targets (e.g., 8 usable megabytes per second from a 100 megabit connection) <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Complexity**: Decentralized L2s involve significant complexity and trade-offs that can affect user experience (UX) <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. By building all components of the L1 itself, Monad avoids this complexity <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Full Control for Performance**: Being an L1 allows for full control over the system, ensuring the necessary performance is achieved without external constraints or dependencies <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. This also simplifies the UX and reduces overall system complexity <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

## Opportunities for Applications
The existence of a high-performance EVM-compatible blockchain like Monad creates significant [[enablement_of_new_onchain_applications | opportunities for new on-chain applications]]:
*   **Unlocking New Use Cases**: Application teams previously constrained by lower-performing chains can now build applications that were not feasible before <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
*   **Increased Complexity per User**: High throughput not only supports more users but also enables more complex transactions and applications per user <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. This means applications can perform more work on-chain than previously possible <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.
*   **Enhanced User Experience**: The core goal of performance improvements is to enhance the user experience, offering faster transaction finality, lower fees, and higher reliability <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
*   **Developer Collaboration**: The core engineering team is excited to collaborate with application teams, leveraging their domain knowledge to refine the platform and optimize the user experience <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.

> "I just want to see some like cool apps...when the app teams come in and build apps that really leverage the performance of Monad I think that's going to be really cool" <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>

Ultimately, high-performance blockchains promise to expand what's possible in the blockchain space, leading to more robust, complex, and user-friendly decentralized applications <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.