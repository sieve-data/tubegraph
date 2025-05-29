---
title: Interoperability in Blockchain Networks
videoId: RUmWyIScfsc
---

From: [[thepipeline_xyz]] <br/> 

[[blockchain_interoperability | Axelar]] is an [[blockchain_interoperability | interoperability network]] structured as a blockchain that connects 56 blockchains and counting [00:03:28]. It is not a bridge in the traditional sense, but rather a messaging platform upon which various [[crypto_interoperability_and_crosschain_communication | cross-chain]] applications can be built [00:04:30]. These applications include [[crosschain_interoperability_and_lending | cross-chain]] decentralized exchanges (DEXes), money markets, and NFT marketplaces [00:04:40].

## Challenges with Centralized Bridges

Historically, centralized bridges like Ren Protocol and Multi-chain (which recently lost all its funds) were prone to security vulnerabilities [00:03:47]. These bridges often relied on a single founder or centralized entity holding all funds in a key [00:04:02]. When this key was compromised, as seen in major DeFi hacks like Harmony, Ronin, and Multi-chain, all funds were lost due to centralization [00:04:14].

## Axelar's Differentiators

[[blockchain_interoperability | Axelar]] was designed to address the issues of centralization and scalability found in earlier [[blockchain_interoperability | interoperability]] solutions [00:04:26]. Its key differentiators include:

### 1. Architecture: Many-to-Many Connectivity
Unlike competitors such as Wormhole, Chainlink CCIP, and LayerZero, which typically offer only pairwise connectivity, [[blockchain_interoperability | Axelar]] leverages its blockchain architecture to provide many-to-many connectivity [00:05:01]. A single connection to the [[blockchain_interoperability | Axelar]] blockchain allows routing messages to any other connected blockchain, simplifying the process of adding new chains and ensuring broader reach [00:05:19].

### 2. [[security_measures_in_blockchain_interoperability | Decentralized Security]]
[[security_measures_in_blockchain_interoperability | Axelar]] is built on the Cosmos SDK, featuring a fully decentralized validator set [00:06:05]. With 75 validators (compared to Wormhole's 19), an attack on the network requires corrupting a majority of these validators [00:06:18]. This design makes [[blockchain_interoperability | Axelar]] almost as secure as the chains it connects to, enhancing overall [[security_measures_in_blockchain_interoperability | cross-chain security]] [00:06:36].

## Origins and Inspiration

The inspiration for [[blockchain_interoperability | Axelar]] stemmed from the challenges faced in onboarding users and developers to new blockchains like Algorand, where one of Axelar's founders, Georgios, was part of the founding team [00:07:51]. At the time, liquidity was concentrated on Ethereum, and bridging to other chains was difficult [00:08:10]. It became clear that bridging needed to evolve beyond simple asset transfers to focus on improving user experience and abstracting away the complexities of Web3 [00:08:35]. This led to the development of a more generalizable message-passing platform [00:08:48].

## General Message Passing (GMP) for Developers

The General Message Passing (GMP) protocol allows developers to build applications with their core logic on a fast EVM chain, like Monad, while enabling users from other networks to easily interact with them [00:10:09].

For example, a developer building a perp DEX on Monad can allow users from Arbitrum or Solana to open positions directly [00:10:32]. This is achieved by deploying a small piece of code on the origin chain (e.g., Arbitrum), which connects to [[blockchain_interoperability | Axelar]]'s endpoint on that chain [00:10:43]. A message, such as "deposit X amount of USDC and open a position," is passed from the origin chain to the application on Monad, eliminating the need for a separate bridging step for the user [00:11:09]. This approach centralizes application logic on one chain, reducing fragmentation and simplifying development [00:12:09].

## Current and Future Use Cases of Cross-Chain Interoperability

Currently, many [[blockchain_interoperability | cross-chain]] use cases are still focused on asset transfers, such as bridging and [[crosschain_interoperability_and_lending | cross-chain]] swaps [00:13:26]. However, as [[performance_and_scalability_of_blockchain_systems | scaling solutions]] and high-throughput blockchains like Monad reduce gas costs, [[blockchain_interoperability | cross-chain]] transactions are expected to become more accessible and numerous [00:14:05].

The growth of new chains (rollups, app chains, Cosmos chains) daily suggests that [[blockchain_interoperability | cross-chain]] activity will scale exponentially [00:14:31]. In the future, every application seen on a single chain today is likely to have a [[blockchain_interoperability | cross-chain]] version, along with entirely new use cases yet to be imagined [00:14:58].

One significant shift is that projects are now planning to launch on multiple chains from day one, recognizing the decentralized nature of liquidity and users across the ecosystem [00:16:05]. The user experience is crucial, and rapid transaction finality, such as Monad's instant finality, significantly improves [[blockchain_interoperability | cross-chain]] message passing times, reducing wait times from 15-20 minutes to 60-90 seconds [00:17:11].

### Interchain Token Service
[[blockchain_interoperability | Axelar]]'s Interchain Token Service (ITS), currently in beta, aims to simplify tokenization and bridging [00:18:28]. It provides a code-free, permissionless solution for launching and bridging tokens across multiple chains [00:18:40]. This service allows projects to issue tokens with [[security_measures_in_blockchain_interoperability | cross-chain]] functionality from day one, leveraging [[blockchain_interoperability | Axelar]]'s support for various chains [00:19:14]. For example, Frax now uses [[blockchain_interoperability | Axelar]] to issue Frax assets on chains not supported by its native Frax Ferry bridge, realizing that focusing on core products rather than managing bridging is more efficient [00:19:39].

The goal of [[blockchain_interoperability | interoperability]] is to make Web3 as user-friendly as Web2 by abstracting away the underlying blockchain complexities [00:31:15]. Users should ideally not need to know if their asset is on Solana and the application on Arbitrum; the wallet should manage this seamlessly, presenting a unified balance and using [[blockchain_interoperability | interoperability]] infrastructure to handle [[crypto_interoperability_and_crosschain_communication | cross-network communication]] [00:31:40].

## Mitigating Interoperability Risks

The [[security_measures_in_blockchain_interoperability | security]] of assets, whether native or wrapped, depends entirely on the underlying bridging infrastructure [00:22:26]. Key mechanisms employed by [[blockchain_interoperability | Axelar]] to mitigate risks include:

1.  **Decentralization:** As mentioned, [[blockchain_interoperability | Axelar]]'s decentralized validator set eliminates the most common attack vector seen in centralized bridges [00:23:16].
2.  **Rate Limiting:** A simple code-based check can be added to transactions to minimize the impact of a hack [00:23:46]. [[blockchain_interoperability | Axelar]]'s many-to-many architecture allows for customizable rate limits on its own blockchain, helping to contain damage even if a connected chain experiences a breach [00:24:06]. Rate limits can be hourly or over longer periods, and can be dynamically refreshed [00:26:57].
3.  **Multi-Provider Approval:** For the highest level of [[security_measures_in_blockchain_interoperability | security]], applications can require approval from multiple [[blockchain_interoperability | cross-chain]] solutions [00:24:49]. For instance, Lido's community decided to work jointly with both [[blockchain_interoperability | Axelar]] and Wormhole for asset minting, requiring approval from both validator sets [00:25:00]. This creates multiple layers of security, including two independent implementations and stacked rate limits [00:25:29].

While rate limiting can be juxtaposed with the high throughput of chains like Monad, [[blockchain_interoperability | cross-chain]] volume rarely matches the transaction speeds within a single chain [00:26:32]. Therefore, rate limits can still effectively cap potential damage to a small fraction of total funds [00:26:46].

## Axelar's Early Commitment to Monad

[[blockchain_interoperability | Axelar]] committed to supporting Monad at an early stage due to several factors:
*   An early introduction via common investor, Dragonfly [00:28:50].
*   Recognition of Monad's technical founders' legitimacy and focus on [[performance_and_scalability_of_blockchain_systems | scalability]] [00:28:58].
*   The strong MIT connection between the teams [00:29:13].
*   Monad's rapidly growing and decentralized community [00:29:30].
*   Anticipated demand from builders for [[blockchain_interoperability | Axelar]]'s presence on Monad, driven by the desire to be first on new, promising ecosystems [00:29:53].
*   Monad's instant finality is crucial for faster [[crypto_interoperability_and_crosschain_communication | cross-chain]] messages, improving user experience for [[crosschain_interoperability_and_lending | cross-chain applications]] [00:16:57].

## Future of Interoperability

In the long term, [[blockchain_interoperability | interoperability]] is not a "killer use case" itself, but rather a fundamental layer that enhances user experience and makes Web3 as intuitive as Web2 [00:31:07]. It aims to fully abstract away the underlying complexities of different blockchains from the user [00:31:38].

[[blockchain_interoperability | Axelar]] believes [[blockchain_interoperability | interoperability]] will become ubiquitous across all Web3 verticals, including DeFi (e.g., Uniswap, dydx, Frax, Lido), gaming (e.g., Immutable, Decentraland), and real-world asset tokenization (e.g., Ono, Centrifuge, Mountain Protocol) [00:32:11]. The [[Axelar | Axelar]] Virtual Machine (AVM) is specifically designed to support this future where [[blockchain_interoperability | interoperability]] is integrated into every application [00:33:04].

> [!NOTE] Final Alpha
> In crypto, while narratives change quickly and attention is often fleeting, long-term success is built on strong technology and a robust community [00:34:21]. Projects like Monad, possessing both, are special [00:34:41]. Ignoring the noise and focusing on projects with amazing tech and strong communities is key for long-term engagement [00:34:48]. Founders with conviction in their vision are critical for project success, and users should maintain their own convictions amidst market hype to stay focused [00:35:59].