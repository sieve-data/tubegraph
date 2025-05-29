---
title: Challenges and solutions in blockchain bridging
videoId: SZw8QjJYpc8
---

From: [[thepipeline_xyz]] <br/> 

## The Problem of Blockchain Fragmentation

The proliferation of various blockchain networks, including application-specific chains and different Layer 1 (L1) solutions, presents a core challenge: how do these disparate chains communicate and share information effectively? <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a> If liquidity resides on one chain, a significant hurdle exists in transferring it to another. <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a> This issue extends to building applications that operate seamlessly across multiple chains. <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>

A significant challenge new chains encounter is [[challenges_and_strategies_in_crypto_investment | liquidity fragmentation]]. <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a> It's undesirable to have multiple variations of a stablecoin like USDC on a single chain, as this hinders a smooth user experience. <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a> From a user's perspective, navigating multiple blockchain ecosystems and moving assets between them poses [[challenges_and_strategies_in_building_crypto_infrastructure | security]], safety, and risk concerns. <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>

### Historical Bridging Challenges

In the early days of bridging, particularly around 2021, the experience was often "horrible and fragmented." <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a> There was a lack of established standards, leading to issues like multiple wrapped or even "double-wrapped" versions of assets, which required users to navigate complex swapping processes. <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a> <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a> Despite these difficulties, there was a clear product-market fit due to the immense demand for [[interoperability_and_blockchain_communication | cross-chain]] asset movement. <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>

## Wormhole: A Solution for Interoperability

Wormhole addresses these challenges by serving as a core communication layer that enables blockchains to communicate with one another. <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a> <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a> This involves blockchains A and B sending data back and forth, allowing the sharing of state—for instance, confirming an action on one chain and relaying that information to another. <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

### Key Functions and Use Cases

While token transfers are the most recognized use case with significant product-market fit, Wormhole also facilitates the transfer of NFTs, including high-value ones, across chains. <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a> The fundamental concept of [[interoperability_and_blockchain_communication | interoperability]] is not new; examples exist in traditional finance (SWIFT) and cloud computing (AWS servers). <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a> Wormhole applies this concept to blockchains in a decentralized and trustless manner. <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>

The long-term vision is for Wormhole to become a "public utility," growing organically as an open-source protocol. <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a> This includes moving towards a decentralized structure where the community eventually owns and runs the protocol. <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>

### Addressing Challenges and Improving User Experience

Wormhole aims to abstract away the complexities of bridging, making the user experience much smoother. <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a> While wrapped assets are often necessary for tokens like Ethereum or Solana that cannot be burned, the user's direct experience will increasingly involve automated swaps that provide native versions of assets. <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a> <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>

**Wormhole as a Developer Platform:**
Wormhole primarily functions as a developer platform, providing tools for building [[challenges_and_strategies_in_building_crypto_infrastructure | chain-agnostic]] applications. <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a> <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>

Key tools and features include:
*   **Token Bridge and NFT Bridges:** Built on top of the core communication layer. <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a> <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>
*   **Cross-chain Queries (Wormhole Queries):** A new tool enabling developers to securely query the state of another chain, similar to an API call. For example, an application on one chain could verify if a user holds a specific NFT on another chain before granting access or lending funds. <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a> <a class="yt-timestamp" data-t="00:55:11">[00:55:11]</a>
*   **Composability:** Developers can combine various transactions, such as automatically swapping a wrapped asset for a native one upon arrival on the destination chain. <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>
*   **Messaging Layer:** Used for advanced applications like cross-chain borrow/lend protocols and Oracle networks (e.g., Pyth). <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>

## The Future of Multi-Chain Ecosystems

The industry recognizes the need for a single standard or "connective tissue" to ensure all blockchains can communicate. <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a> Wormhole aims to be this standard, acknowledging that building such infrastructure is a "tall order." <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>

The future of multi-chain is uncertain, with various theories:
*   **Ethereum-centric:** Everything settling on Ethereum with multiple layers built on top. <a class="yt-timestamp" data-t="00:28:52">[00:28:52]</a>
*   **Multiple Settlement Layers:** Three or four main settlement layers (e.g., Monad, Solana, Sui, Ethereum) with numerous execution layers. <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>
*   **App Chain Specific Thesis:** Proliferation of specialized application chains. <a class="yt-timestamp" data-t="00:29:10">[00:29:10]</a>

Regardless of the specific outcome, a multi-chain world exists today. <a class="yt-timestamp" data-t="00:29:23">[00:29:23]</a> Just as in real-world economies, specialization and mutual benefit through connection are key. <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a> Wormhole provides the secure infrastructure, acting as the "railroads" connecting these diverse chains. <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a> It's critical for new chains to choose the right partners and ensure non-fragmented [[challenges_and_innovation_in_decentralized_finance_defi | DeFi]] primitives to build a strong financial fabric. <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>

### Emphasizing Security and User-Centricity

For blockchain bridging solutions, security is paramount. <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a> Wormhole prioritizes "defense in depth," applying layers of security measures commonly used in Web2 to minimize vulnerabilities. <a class="yt-timestamp" data-t="00:48:10">[00:48:10]</a>

Instead of focusing on competition, protocols should be "customer obsessed" and aim to "grow the pie" for the entire crypto industry. <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a> The success of crypto is measured by bringing new users and developers into the space, not by moving them between existing projects. <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a> This collaborative approach, where protocols specialize and integrate, ultimately benefits the entire ecosystem by enabling new use cases and improving overall user experience. <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a> <a class="yt-timestamp" data-t="00:42:11">[00:42:11]</a>