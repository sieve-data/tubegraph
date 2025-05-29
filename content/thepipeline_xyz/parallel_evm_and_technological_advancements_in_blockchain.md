---
title: parallel evm and technological advancements in blockchain
videoId: wMa6GXjDyH4
---

From: [[thepipeline_xyz]] <br/> 

## Introduction

The blockchain ecosystem is continually evolving, with a strong focus on enhancing performance, interoperability, and user experience. Recent developments, particularly in [[parallel_execution_in_blockchain_technology | parallel execution]] of the Ethereum Virtual Machine (EVM), are poised to address long-standing [[challenges_and_innovations_in_blockchain_development | challenges]] and unlock new possibilities for decentralized applications <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## LayerZero: A Transport Layer for Interoperability

LayerZero aims to connect various distributed execution environments within the blockchain space, much like the internet's TCP/IP stack connects diverse computer systems <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. The protocol functions as a base packet, enabling arbitrary contract invocation and the seamless movement of data between different chains <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Its core purpose is to allow distinct blockchains to communicate and interact, facilitating a [[the_evolution_of_blockchain_and_infrastructure_scaling | multi-chain future]] where applications can abstract away the complexities of cross-chain communication <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

LayerZero is agnostic to validation methodologies, focusing purely on the transport layer <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. This approach allows other "competitive" solutions to potentially operate within LayerZero as validation sets or verifiers, demonstrating a move towards synergy rather than pure competition in the interoperability space <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.

### Omni-chain Fungible Tokens (OFTs)

A significant advancement facilitated by LayerZero is the concept of Omni-chain Fungible Tokens (OFTs) <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>. Historically, moving assets between chains involved wrapped assets, which introduced perpetual risk for users holding IOUs <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>. OFTs enable native asset transfer with instant guaranteed finality, eliminating the need for external bridging providers <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. This means asset issuers can manage their assets directly through smart contracts, moving large sums (e.g., $100 million in Tether) for negligible gas costs <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>. This drastically reduces friction and improves capital efficiency, leading to tighter spreads for market makers and fairer pricing mechanisms across chains <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.

## Monad and the [[parallel_evm_and_its_impact_on_crypto | Parallel EVM]]

Monad is developing a high-performance blockchain designed to significantly increase transaction throughput and reduce costs. A cornerstone of Monad's approach is its [[parallel_execution_in_blockchain_technology | parallel execution]] of the EVM, which is a key technological advancement <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>.

### Addressing Bottlenecks in EVM Execution

The decision to [[parallel_execution_in_blockchain_technology | parallelize the EVM]] stems from in-depth performance analysis, which identified state access as the single biggest bottleneck in existing Ethereum clients <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>. Current Ethereum clients, like Go Ethereum (Geth), use inefficient commodity key-value stores (e.g., LevelDB) for Merkel tree data, requiring many lookups for a single piece of state <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>.

Monad embarked on a nearly year-long journey to build a new custom database with two critical properties:
1.  **Natively storing Merkel tree data**: Optimized for this specific data structure <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>.
2.  **Asynchronous reads and writes**: This allows multiple virtual machines running in parallel to access different regions of the Merkel tree concurrently without blocking each other <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>.

This custom database enables [[parallel_execution_in_blockchain_technology | parallel access]] to the state, significantly improving the performance of the [[parallel_evm_and_its_impact_on_crypto | parallel EVM]] <a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>. Monad aims for 10,000 transactions per second (TPS) throughput <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>, a scale comparable to existing payment processing systems <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

### Impact of Monad's Parallel EVM

The Monad team anticipates that [[evm_compatibility_and_its_impact_on_developers | EVM compatibility]] with underlying architectural changes will enable new types of [[applications_and_potential_of_highperformance_blockchains | applications]] not possible elsewhere due to throughput limitations <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>. This includes:
*   On-chain games <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>
*   Fully on-chain order books for trading <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>
*   Social applications with high interactivity <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>

This enhanced performance facilitates a seamless user experience, allowing users to explore new environments and opportunities without worrying about the logistics or high costs of cross-chain interactions <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>. It also opens up possibilities for split functionality between execution and data, leveraging existing data from other blockchains within the high-performance Monad environment <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.

## Real-World Problem Solving

The advancements in [[parallel_evm_and_its_impact_on_crypto | Parallel EVM]] and interoperability aim to address significant real-world problems:

*   **Disrupting Finance and Money**: Crypto's core appeal lies in providing permissionless access and self-sovereignty over money, challenging traditional banking and financial industries <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Payments**: High transaction fees (e.g., credit card fees of 3% or more) are a significant cost for businesses <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Crypto offers a way for direct, low-cost payments using a phone, especially beneficial in areas where credit cards are less common <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Personal Finance (DeFi)**: Improving efficiency in decentralized finance by reducing slippage and execution costs to be comparable or better than centralized trading environments <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. This requires high-performance environments for market makers to quote tightly and compete spreads down <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.
*   **Reducing Friction and Costs**: High transaction fees on some blockchains deter users and developers <a class="yt-timestamp" data-t="00:48:06">[00:48:06]</a>. For example, the cost of currency exchange at airports or high slippage in DeFi transactions <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. High-throughput chains with low transaction costs enable more frequent and diverse on-chain actions, transforming the user experience and potentially fostering new application categories <a class="yt-timestamp" data-t="00:49:41">[00:49:41]</a>.
*   **Developer Habits**: Developers currently often optimize for gas costs, which can lead to omitting defensive assertions and increasing security risks <a class="yt-timestamp" data-t="00:50:32">[00:50:32]</a>. Lower transaction costs free developers to build more robust and secure protocols <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>.

## The Future Outlook

The goal for technologies like LayerZero and Monad is to become invisible infrastructure, much like the internet's underlying protocols <a class="yt-timestamp" data-t="00:45:06">[00:45:06]</a>. This abstraction will allow developers to build [[applications_and_potential_of_highperformance_blockchains | applications]] without needing to understand the intricate details of cross-chain communication or the underlying blockchain's architecture <a class="yt-timestamp" data-t="00:45:15">[00:45:15]</a>.

The future of [[the_future_of_highperformance_blockchains | high-performance blockchains]] and cross-chain communication lies in systems that offer strong, orthogonal trade-offs compared to existing chains, doing things that are fundamentally different or structurally superior <a class="yt-timestamp" data-t="00:46:04">[00:46:04]</a>. The shift towards lower transaction costs and improved performance is expected to "renormalize" user and developer expectations, enabling broader adoption of decentralized technologies and fostering a new wave of innovative [[applications_and_potential_of_highperformance_blockchains | applications]] <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>.