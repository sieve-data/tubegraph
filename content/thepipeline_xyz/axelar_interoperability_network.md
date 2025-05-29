---
title: Axelar interoperability network
videoId: RUmWyIScfsc
---

From: [[thepipeline_xyz]] <br/> 

Axelar is a blockchain-structured [[interoperability_and_blockchain_communication | interoperability network]] that connects 56 blockchains and counting, functioning as a messaging platform rather than a mere bridge [00:03:28]. It enables the creation of diverse cross-chain applications such as DEXes, money markets, and NFT marketplaces, similar to how applications are built on single chains like Ethereum or Monad, but spanning across multiple blockchains [00:04:36].

## Origins and Vision
Axelar's co-founders, Georgios and Sergey, met at MIT and were part of the founding team of the Algorand blockchain [00:00:46]. Georgios was inspired to enter the crypto space by Bitcoin's censorship-resistant financial system, particularly during the Greek financial crisis when traditional financial services were difficult to access [00:01:11]. The experience of developing Algorand highlighted the challenge of onboarding users and developers to new blockchains due to existing liquidity on networks like Ethereum and the lack of easy bridging solutions [00:07:51]. This led to the development of Axelar as a generalizable platform for message passing, aiming to abstract away Web3 complexities and enable seamless user experiences [00:08:48].

### Key Personnel
*   **Georgios** - Co-founder of Axelar Network [00:00:38].
*   **Sergey** - Co-founder of Axelar Network, led the standardization of BLS signatures used in Ethereum 2.0 [00:00:40, 00:02:07, 00:02:16].
*   **Jason** - Head of DeFi at Axelar [00:02:31, 00:02:35].

## Core Differentiators

Axelar distinguishes itself from competitors like Wormhole, Chainlink CCIP, and LayerZero through its architecture and security [00:05:01].

### Architecture: Many-to-Many Connectivity
Axelar's blockchain-based architecture allows for "many-to-many" connectivity [00:05:19]. Blockchains can establish a single connection to the Axelar network, which then allows messages to be routed to any of the other connected blockchains [00:05:27]. This contrasts with competitors who often offer "pairwise connectivity," making it significantly harder to add new chains and connect them to all existing networks [00:05:43].

### Security: Decentralization and Layered Mechanisms
Axelar is designed as a blockchain based on the Cosmos SDK, featuring a fully decentralized validator set [00:06:07]. With 75 validators, it is described as being five times more decentralized than Wormhole (which has 19 validators) and significantly more than other competitors [00:06:18, 00:06:55]. To compromise the network and steal funds, a majority of these validators would need to be corrupted [00:06:25]. This decentralization eliminates a common attack vector that has resulted in billions of dollars in losses across the DeFi space [00:07:06, 00:23:30].

Additional security measures include:
*   **Rate Limiting**: A simple code check added to transactions to minimize the impact of hacks, even if the core code breaks [00:23:46]. Axelar's architecture allows for customizable rate limits on its own blockchain, helping to contain damage even if a connected chain is compromised [00:24:09]. These limits can be hourly, over six hours, or refreshed more frequently based on live data [00:26:57, 00:27:32].
*   **Joint Approval**: For extreme security, applications can opt to require approval from multiple independent cross-chain solutions [00:24:40]. An example is the Lido community, which voted to work jointly with both Axelar and Wormhole, requiring approval from both validator sets before an asset is minted [00:24:52, 00:25:09]. This creates multiple layers of security, including stacked rate limits [00:25:31, 00:25:36].

## Developer Experience: General Message Passing (GMP)
Axelar's General Message Passing (GMP) protocol simplifies cross-chain development [00:09:25]. Developers can deploy the "brain" of their application on a fast EVM chain like Monad and allow users from other networks (e.g., Arbitrum, Solana) to interact with it easily [00:10:06]. This means a developer would only need to deploy a small piece of code on other chains, connecting it to Axelar's endpoint to pass messages to their main application [00:10:43].

This approach allows for direct interaction without an intermediate bridging step, abstracting away complex application logic from connectivity [00:11:31, 00:11:58]. It also addresses blockchain fragmentation, allowing all users to be brought to a single ecosystem like Monad, simplifying the development paradigm [00:12:09, 00:12:26].

## Use Cases and the [[future_of_crosschain_communication | Future of Interoperability]]
While many initial cross-chain use cases have focused on asset transfers (bridging, cross-swaps), Axelar anticipates a future where every single-chain application will have a cross-chain equivalent, alongside new, unique use cases [00:13:26, 00:14:58, 00:15:03].

Key drivers for this future include:
*   **Reduced Gas Fees**: As scaling solutions and chains like Monad lower gas costs, cross-chain transactions will become cheaper and more accessible [00:14:04].
*   **Exponential Growth**: The rapid launch of new chains (rollups, app chains, Cosmos chains) means cross-chain transactions will scale exponentially [00:14:27, 00:19:52].
*   **Instant Finality**: Chains with instant finality, such as Monad, significantly improve the user experience for cross-chain applications by reducing message passing times from 15-20 minutes (on Ethereum) to 60-90 seconds [00:16:57, 00:17:28, 00:17:31].

### [[Interchain token services | Interchain Token Service]] (ITS)
Axelar's Interchain Token Service (ITS), currently in beta, offers a code-free, permissionless solution for tokenization and bridging [00:18:28, 00:20:51]. This allows users to launch tokens that are cross-chain from day one with robust security, addressing issues like liquidity fragmentation across different chains [00:19:04, 00:20:20, 00:20:26]. An example is the partnership with Frax, where Axelar helps issue Frax assets on chains not supported by Frax Ferry, demonstrating a shift towards relying on specialized interoperability solutions [00:19:39, 00:20:01].

Ultimately, Axelar envisions interoperability as an invisible layer, abstracting away the complexities of different blockchains for users [00:31:12]. Users should only need to think about assets and applications, with wallets seamlessly managing balances across chains and using interoperability infrastructure in the background [00:31:35, 00:32:02]. Axelar is actively working with teams across DeFi (Uniswap, dYdX, Frax, Lido), gaming (Immutable, Decentraland), and real-world asset tokenization (Ondo, Centrifuge, Mountain Protocol) to embed this cross-chain capability [00:32:17, 00:32:41].

## [[Monads collaboration with Axelar | Collaboration with Monad]]
Axelar publicly committed to supporting Monad from an early stage [00:28:09]. The collaboration stems from a connection forged nearly two years prior through a common investor, Dragonfly [00:28:30, 00:28:50]. The Axelar team, particularly Georgios, recognized the technical legitimacy of Monad's founders and their approach to scalability, as well as the strong community and demand from builders for Monad integration [00:29:01, 00:29:36, 00:29:50]. For an [[interoperability_and_blockchain_communication | interoperability platform]], being available on new, promising chains like Monad from day one is crucial for capturing developers and new opportunities [00:30:06]. Monad's instant finality is particularly important for enhancing cross-chain application performance [00:16:57].

## Final Alpha
Jason's "final alpha" emphasizes that while narratives in crypto change quickly, long-term success is built on good technology and a strong community [00:34:21]. He notes that Monad embodies both, advising to ignore the noise and seek projects with these qualities [00:34:33, 00:34:41, 00:34:48]. Unice echoes this, stressing the importance of conviction in founders and maintaining one's own convictions amidst market hype [00:35:27, 00:35:58].