---
title: Integration of Applications and Validators
videoId: fJ8y7Y15vT0
---

From: [[bankless]] <br/> 

Berachain, a new Layer 1 (L1) blockchain, emphasizes a unique core innovation called Proof of Liquidity to integrate its application layer with its validators and economic incentives <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This approach aims to align liquidity and security at the protocol level <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

## Berachain's Proof of Liquidity

Proof of Liquidity operates as a three-way flywheel involving Berachain's application layer, its validator set, and a new economic actor holding a non-transferable governance token <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. This mechanism breaks from the typical Proof of Stake blockchain model <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Core Components

Berachain utilizes two main tokens:
*   **Bara (BERA)**: The gas and staking token of the network <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Validators stake BERA, and the amount staked affects the frequency of their block production (linear weighted block production) <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a> <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. Transaction fees are denominated in BERA <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>.
*   **Berachain Governance Token (BGT)**: A non-transferable, soulbound token <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. BGT determines the size of a validator's block reward <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a> <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. BGT cannot be earned by staking BGT itself; instead, it is primarily earned by providing liquidity on the network <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a> <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>. BGT also represents governance power, allowing holders to sway network incentives <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.

A key economic link is that BERA can be burned one-way to create BGT, but BGT cannot be converted back to BERA <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a> <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>. This enforces a "technical contract" where users must provide a useful service, like liquidity provision, to earn the network's inflation, which is denominated in BGT <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a> <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

### The Interplay: Applications and Validators

The core of Proof of Liquidity is the symbiotic relationship between applications and validators <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>:
1.  **Validator Block Rewards and Emissions**: When a validator builds a block, the BGT block rewards are primarily emitted into the ecosystem, not just reaped by the validator <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
2.  **Reward Vaults/Cutting Board**: Validators can choose to direct these BGT emissions towards specific pools or vaults from applications on the network <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a> <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>. Initially, this includes a native decentralized exchange (DEX) built into the chain to bootstrap the function <a class="yt-timestamp" data-t="00:34:07">[00:34:07]</a>. Over time, any application can join this "Reward Vault" set via governance approval <a class="yt-timestamp" data-t="00:34:28">[00:34:28]</a>.
3.  **Incentive Marketplace**: Applications can propose bids in this marketplace, offering their own tokens in exchange for BGT emissions directed by validators <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a> <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. Validators take a commission cut, distributing the rest to their BGT delegates <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
4.  **User Liquidity Provision**: Users provide liquidity to applications' pools/vaults to earn BGT <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a> <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. They then delegate this earned BGT to validators <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. Users might delegate to validators who incentivize pools they care about, or to those supporting other ecosystem projects whose incentives they desire <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a> <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
5.  **Mutual Benefit**: This creates a system where applications can effectively price their own liquidity using the network's emissions <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>. Validators and their BGT delegates earn a diverse portfolio of ecosystem project tokens <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>. The goal is for the application layer to be value-additive, not extractive, to the network <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.

This integration is intended to cause hundreds of millions of dollars to flow into the network as incentives supporting applications, rather than flowing away <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>. It dissolves the separation between the application layer and the underlying blockchain infrastructure <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

### Sustainability and Challenges

The success of Proof of Liquidity is considered an "economic experiment with uncertain and unproven outcomes" <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a> <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>. Concerns include:
*   **Concentration Risk**: The possibility that all BGT emissions might concentrate on specific pairs, such as Liquid Staking Token (LST) pairs, which would reduce the differentiation from traditional Proof of Stake <a class="yt-timestamp" data-t="00:36:27">[00:36:27]</a>.
*   **Cartel Formation**: The risk of a cartel forming that could vote in a way that erodes the mechanism <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>.

To mitigate these risks, Berachain relies on:
*   **Social Layer Conditioning**: Guiding the community towards interesting and differentiated use cases, focusing on applications with sufficient fee generation and product-market fit <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a>.
*   **Governance Guardian Council**: An external third-party council, including economic auditors, designed to serve as an emergency brake against harmful actions, such as attempts to extract value from the network <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.

## Market Penetration and Technical Aspects

Berachain launched its mainnet in February 2025, entering a saturated crypto market <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>. Its strategy for market penetration is multi-factorial, focusing on the application layer <a class="yt-timestamp" data-t="00:39:06">[00:39:06]</a>.

### Application Layer Focus
Berachain aims to set itself apart by fostering a diverse ecosystem of applications, including:
*   Next-level DeFi protocols (e.g., hyperplex, exponents, Smiley) <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>
*   Gaming, consumer, and social applications (e.g., Honey Chat, Puff Paw) <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>
*   Layer 2s (L2s) building on Berachain, which can be app-specific or vertical-specific (e.g., RWA, consumer) <a class="yt-timestamp" data-t="00:40:07">[00:40:07]</a>.

The team has actively supported over 60 to 75 novel applications, ensuring they are well-positioned for success upon launch <a class="yt-timestamp" data-t="00:42:30">[00:42:30]</a>.

### Technical Foundation
Berachain is built on a framework called Beacon Kit, developed in-house, which allows for plug-and-play functionality between its consensus and execution layers <a class="yt-timestamp" data-t="00:44:29">[00:44:29]</a>.
*   **Consensus**: It is optimized for Tendermint (Comet) consensus, offering single-slot finality <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>. However, this also imposes fundamental scaling limits for the validator set <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>. The current validator set is around 69, with a planned expansion to 200+ over time <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>. The framework allows for upgrading or swapping out consensus engines in the future <a class="yt-timestamp" data-t="00:46:30">[00:46:30]</a>.
*   **EVM Identical**: Berachain is EVM identical, meaning it runs unmodified Ethereum execution clients <a class="yt-timestamp" data-t="00:40:39">[00:40:39]</a>. This makes it easy to build OP Stack or Arbitrum Orbit rollups on top <a class="yt-timestamp" data-t="00:40:57">[00:40:57]</a>. This enables a more closely intertwined relationship between L1s and L2s, where an L2's governance token can be paired with BERA on the Berachain network, generating BGT rewards that can be directed to the L2's bridge contract for native yield <a class="yt-timestamp" data-t="00:41:35">[00:41:35]</a>.
*   **Speed**: While not its sole focus, Berachain offers sub-two-second block times with near-instant finality, aiming for a smooth user experience <a class="yt-timestamp" data-t="00:45:51">[00:45:51]</a>.

## Community-First Approach

Berachain originated as an NFT project (Bong Bears) before evolving into a blockchain <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This led to a "community-first" approach, where the community and their intellectual capital contributed to the development of Proof of Liquidity, rather than a technical breakthrough preceding community formation <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a> <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

Despite raising venture capital, Berachain maintains its commitment to the community. A significant portion of its token airdrop went to community members and those who helped build the project from the ground up, with resources directed to fuel ecosystem growth and community engagement <a class="yt-timestamp" data-t="00:50:31">[00:50:31]</a> <a class="yt-timestamp" data-t="00:53:04">[00:53:04]</a>. The team is actively involved with application builders in various communication channels to provide resources and support <a class="yt-timestamp" data-t="00:43:46">[00:43:46]</a>.

## 2025 Roadmap

Key focus areas for Berachain in 2025 include:
*   Supporting the launch of new applications within the ecosystem <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>.
*   Shipping technical roadmap items, including enabling withdrawals later in the year and introducing slashing features <a class="yt-timestamp" data-t="00:54:15">[00:54:15]</a>.
*   Ensuring the L2 stack is optimized for developers <a class="yt-timestamp" data-t="00:54:27">[00:54:27]</a>.
*   Team growth and expansion into APAC regions (especially East Asia), Europe, and institutional partnerships <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.