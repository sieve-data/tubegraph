---
title: Future of CrossChain Applications and User Experience
videoId: RUmWyIScfsc
---

From: [[thepipeline_xyz]] <br/> 

Axelar is an [[crypto_interoperability_and_crosschain_communication | interoperability network]] designed as a blockchain to connect different blockchains, currently supporting 56 and counting <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Unlike centralized bridges that proved prone to hacks, Axelar aims to solve the cross-chain problem through a decentralized, messaging-based approach <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. It functions as a messaging platform upon which developers can build cross-chain applications such as DEXes, money markets, and NFT marketplaces, akin to building applications on Ethereum or Monad, but spanning across various blockchains <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Key Differentiators and Vision

Axelar's architecture is built on two core differentiators:
1.  **Many-to-Many Connectivity**: As a blockchain itself, Axelar offers a single point of connection for other chains, allowing for "many-to-many" connectivity. This makes it significantly easier to add new chains compared to competitors that primarily offer pairwise connections <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
2.  **Decentralized Security**: Built on the Cosmos SDK, Axelar has a fully decentralized validator set of 75 validators, making it significantly more decentralized than many competitors. Attacking the network would require corrupting a majority of these validators, providing a high level of security comparable to the chains it connects <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

The inspiration for Axelar came from the challenges of onboarding users and developers to new blockchains like Algorand, where liquidity was siloed on chains like Ethereum and bridging was complex <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. The vision was to create a generalizable platform for message passing, enabling a seamless [[Experiences on blockchain platforms | user experience]] and abstracting away the complexities of Web3 for developers <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

## General Message Passing (GMP) for Developers

Axelar's General Message Passing (GMP) protocol allows developers to build applications whose core logic resides on a fast EVM chain like Monad, while still allowing users from other networks (e.g., Arbitrum, Solana) to easily interact with them <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. For example, a developer can deploy a small piece of code on an origin chain, connect it to Axelar's endpoint, and pass a message to the application's "brain" on Monad. This enables direct user interaction without an intermediary bridging step <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

This approach solves liquidity fragmentation, allowing applications to consolidate their logic and users on a single chain, simplifying the development paradigm <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. It is predicted that most [[future_of_onchain_data_and_applications | cross-chain applications]] in the next two years will adopt this architecture <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

## Current and Future Use Cases

While asset transfers remain a primary focus in [[crypto_interoperability_and_crosschain_communication | cross-chain interoperability]] today, the space is still early <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. High cross-chain gas fees (source chain, destination chain, relay costs) currently restrict more complex message-passing use cases <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. However, with new scaling solutions and high-throughput chains like Monad, cross-chain transactions will become cheaper and more accessible, leading to exponential growth <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

The [[future_of_crypto_adoption_and_use_cases | future of cross-chain]] is envisioned to include cross-chain versions of every application seen on a single chain today (e.g., cross-chain DEXes, cross-chain swaps), alongside entirely new, unforeseen use cases <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

### Evolution of Interoperability Perception
Just a year ago, many teams preferred to remain on a single chain <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. Today, the conversation has drastically shifted, with teams planning to launch on multiple chains from day one due to the rapidly shifting landscape of liquidity and users <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. The increasing accessibility and developer-friendliness of [[Axelars Approach to CrossChain Connectivity | interoperability solutions]] like Axelar will further accelerate this trend <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

## Addressing Liquidity Fragmentation and Security

One major challenge in DeFi is liquidity fragmentation across multiple stablecoins or assets <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. Axelar addresses this with its **Interchain Token Service (ITS)**. Currently in beta, ITS is the first code-free, permissionless tokenization and bridging solution <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. It allows anyone, from meme coin creators to large projects like Frax, to launch and manage tokens on multiple chains from day one with robust security <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. Frax, for instance, partners with Axelar to issue its assets on chains not supported by its native bridge, recognizing Axelar's expertise in cross-chain asset issuance <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>. This service embodies the ethos of decentralization and permissionless access <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

### Mitigating Risks
Axelar mitigates interoperability risks through several layers of security:
*   **Decentralization**: The decentralized validator set eliminates the most common attack vector seen in centralized bridges <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
*   **Rate Limiting**: A simple but effective piece of code that can be added to the end of every transaction to minimize the impact of a hack. Axelar's architecture allows for customizable rate limits on the Axelar blockchain itself, containing damage even if a connected chain breaks <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.
*   **Multi-Provider Approval**: For maximum security, applications can require approval from multiple independent [[Axelars Approach to CrossChain Connectivity | cross-chain solutions]]. For example, Lido uses both Axelar and Wormhole's validator sets for asset minting, creating three layers of security including stacked rate limits <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>.

## Impact of High-Performance Blockchains

High-performance blockchains like Monad are crucial for the [[future_applications_and_scalability_in_the_crypto_space | future of cross-chain applications]]. Today, slow finality on chains like Ethereum (15-20 minutes for cross-chain messages, longer for L2s) limits user experience <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. With instant finality on chains like Monad, messages can be passed much faster (e.g., 60-90 seconds), significantly improving the user experience and enabling more complex cross-chain interactions <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.

Axelar's early commitment to Monad stems from the Monad team's strong technical foundation, the excitement within the community, and the demand from builders to integrate with new, interesting ecosystems like Monad <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>. This collaboration will be crucial for the [[future of decentralized applications and high throughput ecosystems | future of decentralized applications and high throughput ecosystems]].

## The Invisible Future of Interoperability

Interoperability is not about a single "killer use case" but about enhancing the [[Experiences on blockchain platforms | user experience]] and making Web3 as intuitive as Web2 <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. The goal is to abstract away the underlying blockchain complexities so users only need to think about assets and applications. For instance, a wallet should automatically combine asset balances across different chains and use [[Axelars Approach to CrossChain Connectivity | interoperability infrastructure]] to seamlessly pass messages across networks <a class="yt-timestamp" data-t="00:31:33">[00:31:33]</a>.

In four years, [[crypto_interoperability_and_crosschain_communication | interoperability]] is expected to be an integral part of virtually every application across DeFi, gaming, real-world asset tokenization, and NFTs, becoming an invisible, ubiquitous layer enabling a truly seamless cross-chain experience <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.