---
title: challenges and propositions in blockchain technology
videoId: y9Ac0ybjuHk
---

From: [[thepipeline_xyz]] <br/> 

This article explores key challenges and innovative solutions in blockchain technology, drawing insights from Rousi, co-founder of Movement Labs, and Kevin G, leading developer relations at Monad. The discussion highlights the shared vision of enhancing blockchain performance and celebrating new use cases <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.

## Current Challenges Facing Blockchain Ecosystems

The blockchain space faces several critical [[growth and scalability challenges in blockchain ecosystems | challenges]], particularly concerning performance, security, and broader adoption.

### Performance and Scalability
One of the most pressing issues is the inability of current infrastructure, especially execution layers, to handle widespread demand <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>. Existing EVM (Ethereum Virtual Machine) solutions are described as slow, clunky, and broken <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **User Onboarding:** Blockchains struggle to onboard a large number of users effectively <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. When user numbers exceed a certain threshold (e.g., 50,000 users), gas fees skyrocket, making the network unusable <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   **Inconsistent Gas Fees:** Even on modern EVMs like Arbitrum, gas fees can be inconsistent, fluctuating from a dollar to $23, which can disrupt trading strategies for average users <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>.
*   **Infrastructure Readiness:** Current infrastructure is not yet ready for mass adoption. A single app with the user base of Web2 giants like Instagram or Facebook would cause every blockchain today to break, including Solana <a class="yt-timestamp" data-t="11:04:00">[11:04:04]</a>.

### Security Concerns
Blockchain security is a significant concern, with billions of dollars lost annually to smart contract hacks <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>, <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>, <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. The user experience demands users to execute actions correctly, with a huge risk of loss <a class="yt-timestamp" data-t="25:17:00">[25:17:00]</a>.

### Developer Experience
Developing on certain blockchain ecosystems can be challenging. For instance, writing in Rust for Solana is difficult, and there's a financial disincentive for developers to use new languages when most TVL (Total Value Locked) and volume are in EVM <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.

### User Adoption and Perception
A common misconception among non-technical individuals is that blockchains are ready to scale and handle any application <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>. The general perception of crypto often views it as a "niche scam" or associated with "selling monkey pictures online" <a class="yt-timestamp" data-t="19:19:00">[19:19:00]</a>. Crypto-native games, often featuring Ponzi mechanics, have contributed to this negative perception <a class="yt-timestamp" data-t="40:30:00">[40:30:00]</a>.

### Centralization Points
Modern-day rollups, while offering scalability, often have centralization points that need to be addressed <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

## Innovative Propositions and Solutions

New projects are tackling these [[technology advancements and infrastructure in blockchain | challenges]] with novel approaches focused on performance, security, and developer-friendly environments.

### High-Performance Blockchain Architectures

#### Movement Labs
Movement Labs is building the first network of Move-based blockchains <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.
*   **Move VM:** Utilizes the Move language and Move VM, originally developed by Facebook's Diem project with over a billion dollars in research, to bring novel concepts to networks like Ethereum <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.
*   **M2 Rollup:** Movement is launching M2, the first Move rollup on Ethereum, leveraging Ethereum's security and liquidity <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>, <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.
*   **Data Availability (DA):** It partners with Celestia for data availability to avoid high gas fees on Ethereum, offering performance similar to Layer 1s with extremely low gas fees <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.
*   **Decentralized Sequencer:** Employs Snow Consensus (from the Avalanche system) for its decentralized sequencer set. This consensus mechanism has low hardware requirements, high decentralization, and instant finality <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>. Financial incentives are baked in, requiring staking of the native Move token to participate in sequencing, thus incentivizing network uptime <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

#### Monad
Monad focuses on making the EVM fast while remaining fully EVM bytecode compatible <a class="yt-timestamp" data-t="29:05:00">[29:05:00]</a>.
*   **L1 Approach:** Monad's design as an L1 allows fundamental changes to the database and consensus mechanisms, which are necessary to make the EVM truly fast <a class="yt-timestamp" data-t="29:26:00">[29:26:00]</a>.
*   **Paralyzed Runtimes & Localized Fee Markets:** These are crucial for ensuring consistent user experience and stable gas fees <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>.

### Developer-Friendly Environments

#### Movement Labs' Fractal Transpiler
Movement Labs developed "Fractal," a transpiler that allows any Solidity code (EVM opcodes) to be mapped to Move opcodes and launched on the Move VM <a class="yt-timestamp" data-t="23:39:00">[23:39:00]</a>. This provides backward compatibility for next-generation technology, akin to PS4 games working on a PS5 <a class="yt-timestamp" data-t="23:30:00">[23:30:00]</a>.

#### Monad's EVM Compatibility
Monad's commitment to full EVM bytecode compatibility offers long-term benefits, especially in the context of ongoing research in ZK (Zero-Knowledge) and rollups, which are often centered around the EVM <a class="yt-timestamp" data-t="31:17:00">[31:17:00]</a>.

### Enhanced Security Measures

#### Movement Labs
The Move VM inherently includes formal verification methods, which are proving mechanisms built directly into the VM <a class="yt-timestamp" data-t="26:09:00">[26:09:00]</a>. This approach aims to cut down 90% of smart contract hacks, addressing the annual $4 billion loss <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>. While writing directly in Move code offers the highest security, the Solidity transpiler still provides strong security by mapping Solidity scripts to statistically typed Move opcodes <a class="yt-timestamp" data-t="26:30:00">[26:30:00]</a>.

#### Monad
Monad addresses security by:
1.  **Reducing Development Cost:** Enabling developers to implement more checks without compromising security for gas optimization <a class="yt-timestamp" data-t="33:41:00">[33:41:00]</a>.
2.  **L1 Specific Instructions:** As an L1, Monad can add special instructions to the VM, such as marking a contract as non-reentrant, to prevent common attack vectors directly at the VM level <a class="yt-timestamp" data-t="34:07:00">[34:07:00]</a>.

### Collaborative Mindset

A significant shift in the blockchain ecosystem is the move from rigid competition to greater collaboration. The execution layer is described as the "friendliest layer" where different VMs (Move, EVM, Solana VM) are seen as interesting pieces of technology designed for specific use cases, rather than subjects of tribal wars <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.
*   **Tired of Fighting:** The community is growing tired of internal conflicts that have hindered the space's progress, acknowledging that infighting (e.g., Ethereum vs. Solana) benefits no one <a class="yt-timestamp" data-t="16:39:00">[16:39:00]</a>.
*   **Grow the Pie:** The prevailing mindset is to "grow the pie" by enabling more use cases rather than fighting over existing market share <a class="yt-timestamp" data-t="32:27:00">[32:27:00]</a>.
*   **Mutual Contribution:** Projects aim to contribute back to foundational layers like Ethereum while pursuing first-principles engineering solutions without being constrained by social layers <a class="yt-timestamp" data-t="30:39:00">[30:39:00]</a>. This collaborative spirit fosters learning from each other's designs <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>.

## Future Use Cases and Impact

With advancements in infrastructure, the industry is poised to unlock new application cases that were previously impossible.

*   **Payments:** Cross-border payments are ripe for disruption. Current methods are expensive and cumbersome, but with improved blockchain infrastructure (like paralyzed next-gen chains) and better wallet experiences (e.g., account abstraction, Venmo-like transaction signing), stablecoins and crypto can enable seamless, low-cost global transfers <a class="yt-timestamp" data-t="35:54:00">[35:54:00]</a>. The goal is to reach a point where a Visa Network could be supported on-chain <a class="yt-timestamp" data-t="37:11:00">[37:11:00]</a>.
*   **Retail Trading:** On-chain order books and retail trading are becoming viable with improved slippage, making it profitable for market makers <a class="yt-timestamp" data-t="37:21:00">[37:21:00]</a>. This represents a significant [[challenges and advancements in highfrequency trading and blockchain | opportunity for DeFi]] and broader financial applications.
*   **Gaming:** While still nascent, blockchain gaming is progressing. The focus is shifting to building genuinely fun games first, then integrating blockchain components like asset and state tracking, rather than running entire game engines on-chain <a class="yt-timestamp" data-t="38:47:00">[38:47:00]</a>. The goal is to move beyond "Ponzi game" mechanics to sustainable economics and to leverage social coordination dynamics for unique, non-financial experiences <a class="yt-timestamp" data-t="40:41:00">[40:41:00]</a>.

## Conclusion
The blockchain industry is at an exciting juncture, with line of sight on solutions to major scalability and security challenges. While not yet ready for billions of users, the foundational [[technology advancements and infrastructure in blockchain | infrastructure]] is nearing completion <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>. The shift towards collaboration and a focus on real-world use cases, combined with significant engineering breakthroughs, signals a promising future for widespread blockchain adoption and impact <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>.