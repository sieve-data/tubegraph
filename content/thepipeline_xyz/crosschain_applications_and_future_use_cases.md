---
title: Crosschain applications and future use cases
videoId: RUmWyIScfsc
---

From: [[thepipeline_xyz]] <br/> 

## Introduction to Crosschain Interoperability
Axelar is an [[future_of_crosschain_communication | interoperability network]] structured as a blockchain that connects 56 blockchains and counting <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. It functions as a messaging platform upon which various [[enablement_of_new_onchain_applications | applications]] can be built, extending across all connected blockchains <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## Evolution of Interoperability
Historically, centralized bridges such as Ren Protocol and Multi-chain (which recently lost all its funds) were prevalent <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. These centralized entities holding funds in a single key were vulnerable to compromise, leading to major hacks like Harmony, Ronin, and Multi-chain, proving they were not scalable or secure <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

Axelar adopted a different approach, focusing on decentralized message passing rather than simple asset bridging <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. Axelar's architecture provides many-to-many connectivity, meaning a single connection to Axelar allows messages to be routed to any other blockchain it connects to <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This contrasts with competitors like Wormhole, Chainlink CCIP, and LayerZero, which typically offer pairwise connectivity, making it harder to add new chains <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Key Differentiators and Security
Axelar is designed as a blockchain using the Cosmos SDK, featuring a fully decentralized validator set of 75 validators <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. To attack the network and steal funds, a majority of these validators would need to be corrupted <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This decentralization makes Axelar almost as secure as the chains it connects to, and it is considered five times more decentralized than Wormhole (which has 19 validators) and significantly more than other competitors <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

Security measures include:
*   **Decentralization:** Eliminates common attack vectors seen in centralized bridges <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.
*   **Rate Limiting:** A simple code addition that minimizes the impact of a hack by limiting the amount of funds that can be transferred in a given period <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. Axelar's architecture allows for customizable rate limits on the Axelar blockchain itself <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.
*   **Multi-solution Approval:** For extreme security, some applications (like Lido) can require approval from multiple independent cross-chain solutions, such as both Axelar and Wormhole, before an asset is minted <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>. This provides multiple layers of security and independent implementations <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.

## Current and Emerging Crosschain Use Cases
While pure message passing use cases are still early, much of cross-chain [[Crosschain lending and interoperability in DeFi | interoperability]] today focuses on asset transfers <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

Current applications enabled by Axelar's General Message Passing (GMP) include:
*   Cross-chain DEXes <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>
*   Cross-chain money markets <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>
*   Cross-chain NFT marketplaces <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>
*   Bridging and cross-swaps <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>
*   Projects building various types of bridges (e.g., Squid, Casimir, InterSwap) on top of Axelar's infrastructure <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

### Interchain Token Service (ITS)
The [[Interchain token services | Interchain Token Service]] (ITS), currently in beta, is a code-free, permissionless tokenization and bridging solution <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. It allows anyone, even without coding knowledge, to take their token cross-chain in minutes <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. This enables projects to launch a token on multiple chains from day one with the ability to scale to any future chain Axelar supports <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. An example is the partnership with Frax, where Axelar helps issue all Frax assets on chains not supported by Frax Ferry <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

## Future Potential of Crosschain Applications
The [[future_of_blockchain_cooperation_and_multichain_ecosystems | blockchain ecosystem]] is rapidly evolving, with new chains (rollups, app chains, Cosmos chains) launching daily <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. It is becoming "almost inevitable" that cross-chain activity will grow exponentially <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. Builders are now planning to launch on multiple chains from the outset, recognizing the shifting landscape of liquidity and users <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

### Vision for the Future
*   **Ubiquitous Interoperability:** Everything seen on a single chain today will eventually have a cross-chain version <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. Beyond existing applications, new unique use cases that haven't been conceived yet will emerge <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   **Abstracted User Experience:** [[future_potential_of_blockchain_applications_and_adoption | Interoperability]] is about making web3 as user-friendly as web2 <a class="yt-timestamp" data-t="00:31:21">[00:31:21]</a>. The goal is to abstract away the complexities of different blockchains, so users only interact with assets and applications, unaware of the underlying chain where their assets or applications reside <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>. Wallets could aggregate balances across chains and use [[future_of_crosschain_communication | interoperability infrastructure]] to seamlessly pass messages <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>.
*   **Integration with All Verticals:** Interoperability is expected to be part of every single use case, including DeFi (e.g., Uniswap, dYdX, Frax, Lido), gaming (e.g., Immutable, Decentraland), and real-world asset tokenization (e.g., Ondo, Centrifuge, Mountain Protocol) <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>.

### Enabling Factors
*   **Lower Gas Fees:** Reductions in cross-chain gas fees, enabled by new scaling solutions and high-performance chains like Monad, will make cross-chain transactions cheaper and more accessible, driving greater adoption <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
*   **Fast Finality:** Instant finality on chains like Monad is crucial for cross-chain applications <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>. This drastically reduces message passing times from 15-20 minutes (or longer for L2s on Ethereum) to 60-90 seconds, significantly improving user experience <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   **Simplified Development Paradigm:** Centralizing application logic on a fast EVM chain like Monad allows developers to onboard users easily from other networks, avoiding fragmentation and simplifying development <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Developers would only need to deploy a small piece of code on other chains to connect to their main application via Axelar's endpoint <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. This architecture is predicted to be adopted by most [[innovation_in_blockchain_technology_and_applications | cross-chain applications]] in the next two years <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

The collaboration between Axelar and Monad aims to leverage Monad's high throughput to enable even more seamless cross-chain experiences <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.