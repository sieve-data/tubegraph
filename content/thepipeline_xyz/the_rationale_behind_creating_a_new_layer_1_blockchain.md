---
title: The rationale behind creating a new Layer 1 blockchain
videoId: kjZShZB_7v0
---

From: [[thepipeline_xyz]] <br/> 

Creating a new Layer 1 (L1) blockchain, such as Monad, is driven by the ambition to achieve unprecedented performance and address the [[challenges_in_current_blockchain_infrastructure | limitations of existing blockchain infrastructure]]. This approach stems from a belief that the underlying hardware is capable of far more than current blockchain designs allow, and that specialized, ground-up development is essential to unlock this potential <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Core Principles and Capabilities

Monad aims to demonstrate that a high-performance, fully EVM-compatible blockchain with low transaction fees and reasonable hardware requirements is achievable <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Key aspects of this rationale include:

*   **Unlocking Modern Hardware Potential**
    Modern hardware, including SSD drives, PCI E4, and PCI E5, offers impressive bandwidth, storage, and low latency <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. However, existing software often relies on general-purpose database or file system solutions that introduce algorithmic overhead and are not optimized for specific blockchain needs <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. To achieve maximum performance, software must be specialized to take full advantage of this hardware <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Building from Scratch for Optimal Performance**
    Drawing parallels from high-frequency trading (HFT), where general libraries or software are insufficient for latency-sensitive operations <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>, Monad's team believes in [[building_blockchain_technology_from_scratch | building everything from scratch]] at a very low level <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This means minimizing reliance on the operating system and deeply understanding how different hardware components, like SSD drives, behave to fine-tune performance <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Deep Understanding of EVM Usage Patterns**
    Optimizing an EVM-compatible chain requires thorough analysis of how users interact with the EVM, including usage patterns of ERC-20 contracts and Uniswap <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This involves understanding transaction patterns, state access, scheduling, and autocorrelation (e.g., accounts used recently are likely to be used again soon) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This statistical analysis informs the design of data structures and software for continuous improvement <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

## Why a New Layer 1, Not a Layer 2?

The decision to build a new L1 rather than an L2 is based on several strategic considerations:

*   **Bandwidth and Data Availability Constraints**
    Existing Layer 2 solutions often face bandwidth limitations, especially regarding data availability. Monad targets a 100 megabit connection, which translates to approximately 8 usable megabytes per second of data <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Current data availability solutions on L2s don't come close to this, which would constrain Monad's desired performance <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Complexity and Trade-offs of Decentralized L2s**
    Building a decentralized L2 involves significant complexity and various design trade-offs that can affect user experience (UX) and other aspects <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. By building all components of Monad internally, which are designed to be somewhat modular, the team can avoid much of this external complexity <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Full Control for Performance and Decentralization**
    Launching as an L1 provides full control over the system, allowing the team to ensure the necessary performance <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. It's considered easier to achieve high [[need_for_performant_blockchain | performance]] and [[decentralization_in_blockchain | decentralization]] when building a dedicated L1, simplifying the overall design and improving UX <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This avoids the complexities of coordinating between separate data and execution chains <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

## Competitive Advantage and Impact

The idea for Monad emerged from the team's competitive advantage in building low-latency systems, honed through experience in HFT <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. They observed that existing L1s made different trade-offs or simply copied software components <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. By [[building_blockchain_technology_from_scratch | building from the ground up]] with this specialized expertise, they believed they could create a significantly faster and more performant blockchain <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

The goal is to enable new applications and use cases that are not feasible on lower-performing chains <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. This is not just about supporting more users (e.g., 10,000 users instead of 1,000), but also about enabling more complex applications per user <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>, thereby expanding the possibilities of what can be built in the blockchain space <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.