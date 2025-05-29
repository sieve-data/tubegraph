---
title: Berachain Overview and Introduction
videoId: fJ8y7Y15vT0
---

From: [[bankless]] <br/> 

Berachain is a new Layer 1 blockchain project co-founded by Smokey the Bara, which recently launched its mainnet <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The project distinguishes itself with its core innovation called "Proof of Liquidity" <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Origins and Community Formation

Unlike traditional blockchain projects that often start with a technical breakthrough, Berachain's inception was a "happy accident" rooted in its unique community <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. The project began as a collection of 100 NFTs called "The Bong Bears," depicting bears with bongs <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>, <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. These NFTs were designed to "multiply or rebase," reducing scarcity and allowing more participants into the ecosystem <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>, <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

The community largely formed from DeFi-native Discord channels, attracting both humor-oriented individuals and those interested in game theory and liquidity mechanisms <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. The name "Beas" (instead of bears) originated as a joke within this Discord community and stuck <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>, <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This unique, meme-driven approach meant that the community was established *before* the technical innovation, with members actively contributing ideas and fostering productive conversations <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>, <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

The initial goal was to explore what could be done with an NFT project beyond typical animal themes <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This led to discussions around capital efficiency and liquid staking, specifically addressing the paradox of secure chains lacking on-network liquidity <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Berachain was thus built to align liquidity and security at the protocol level, ensuring that user capital allocation supports both <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

For more information on the community's role, see [[Berachains Unique Community Formation]].

## Proof of Liquidity (PoL)

Proof of Liquidity is Berachain's core innovation designed to integrate liquidity directly with network security <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. It operates through a three-party flywheel mechanism involving:

1.  **Berachain's Application Layer (Apps)** <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
2.  **Validators (Stakers)** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
3.  **BGT (Berachain Governance Token) Delegators** <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>

### The Role of Tokens: Bara and BGT

Berachain utilizes a dual-token model:
*   **Bara (BEA)**: This is the native currency of the blockchain, serving as the gas token and the staking token for network security, similar to ETH for Ethereum <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Validators stake Bara, and the amount staked influences the frequency of block production <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>, <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **BGT (Berachain Governance Token)**: This token is *non-transferable* and *soulbound* <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>, <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. It cannot be staked to earn more BGT <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. Instead, BGT is earned by providing liquidity on the network or performing other governance-whitelisted activities <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>, <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. The amount of BGT *delegated* to a validator directly affects the *size* of that validator's block reward <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>, <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

### The Flywheel Mechanism

1.  **BGT Generation**: Users provide liquidity on Berachain's network (e.g., through pools or stable tokens from applications) and earn BGT <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>, <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
2.  **Delegation to Validators**: BGT holders delegate their BGT to validators <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. This delegation boosts the block rewards for those validators <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
3.  **Validator-Application Relationship**: Validators then direct these BGT emissions (block rewards) primarily to specific pools or "reward vaults" on the network, which are often stable tokens from applications <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>, <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. This creates a marketplace where applications can bid for BGT emissions in exchange for their own tokens, effectively pricing their liquidity <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>, <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. Validators can take a cut of these commissions and distribute the rest to their BGT delegators <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
4.  **Bara Conversion**: To close the loop, Bara can be burned one-way to create BGT, but BGT cannot be converted back to Bara <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>, <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>. This means inflation within the network is primarily in the form of BGT <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>. This mechanism enforces a "technical contract" where earning network rewards requires providing a useful service, such as liquidity provision <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.

The goal of Proof of Liquidity is to ensure the application layer is "value additive" to the network, with the chain driving value back to applications, creating a self-reinforcing system of liquidity and security <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>, <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>. This system aims to dissolve the separation between the application layer and the underlying blockchain infrastructure <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

While promising, the outcome of this "economic experiment" is uncertain, and its success may require "relatively heavy top-down control and influence" to maintain balance <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>.

## Technical Aspects and Scaling

Berachain is an EVM-identical Layer 1 <a class="yt-timestamp" data-t="00:31:11">[00:31:11]</a>, meaning it runs "unmodified ETH execution clients" and is fully compatible with existing Ethereum Improvement Proposals (EIPs) and opcodes <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>. This makes it easy for developers to build Layer 2 rollups (like OP Stack or Arbitrum Orbit) on top of Berachain <a class="yt-timestamp" data-t="00:40:57">[00:40:57]</a>.

The chain is built on a custom framework called "Beacon Kit," which allows for a high degree of plug-and-play between the consensus and execution layers <a class="yt-timestamp" data-t="00:44:30">[00:44:30]</a>. Currently, it's optimized for Tendermint consensus (more precisely, Comet), which provides single-slot finality <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>, <a class="yt-timestamp" data-t="00:44:46">[00:44:46]</a>. While this offers fast transaction finality (sub-two-second block times) <a class="yt-timestamp" data-t="00:45:53">[00:45:53]</a>, it also presents "fundamental scaling limits" for validator sets <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>. Berachain currently has around 69 validators, with plans to expand to a cap of 200+ over time <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>. Future upgrades to the consensus mechanism will be needed for further scaling and decentralization <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>.

## Market Penetration and Challenges

Launching in a "saturated" crypto industry <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>, Berachain's strategy for market penetration is multi-factorial, with a strong focus on its application layer <a class="yt-timestamp" data-t="00:39:06">[00:39:06]</a>. The project aims to host novel and differentiated applications that leverage its unique economic model <a class="yt-timestamp" data-t="00:39:49">[00:39:49]</a>, <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. Examples of applications include DeFi protocols, gaming, consumer apps, and social platforms <a class="yt-timestamp" data-t="00:39:30">[00:39:30]</a>.

The project has faced criticism, particularly accusations of being a "VC chain" <a class="yt-timestamp" data-t="00:48:11">[00:48:11]</a>. Smokey acknowledges raising venture capital "a long time ago" when staking locked tokens was typical <a class="yt-timestamp" data-t="00:49:18">[00:49:18]</a>, <a class="yt-timestamp" data-t="00:49:23">[00:49:23]</a>. However, he emphasizes that Berachain originated as a community project and remains community-focused <a class="yt-timestamp" data-t="00:50:29">[00:50:29]</a>, <a class="yt-timestamp" data-t="00:50:44">[00:50:44]</a>.

### Airdrop and Community Rewards
To reward its community, Berachain implemented a "request for proposal" program <a class="yt-timestamp" data-t="00:51:36">[00:51:36]</a>. This program allowed applications and community groups (e.g., builders' communities) to submit plans on how they would use airdropped tokens for ecosystem growth and user base expansion on mainnet <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a>, <a class="yt-timestamp" data-t="00:51:57">[00:51:57]</a>. Over 127 application teams and 70+ community groups received these rewards <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>. Smokey asserts that the majority of benefits from Berachain have gone to community-related individuals <a class="yt-timestamp" data-t="00:52:14">[00:52:14]</a>.

More details on challenges in the crypto industry can be found at [[Navigating the crypto industry and market challenges]].

## 2025 Roadmap and Future Plans

For 2025, Berachain's roadmap includes significant technical and ecosystem developments:
*   **Ecosystem Growth**: Supporting the launch of numerous new applications and helping them overcome challenges <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>, <a class="yt-timestamp" data-t="00:54:07">[00:54:07]</a>.
*   **Technical Milestones**: Shipping withdrawals later in the year, implementing slashing mechanisms, and refining the Layer 2 stack to support highly optimized dApp manifestations <a class="yt-timestamp" data-t="00:54:20">[00:54:20]</a>, <a class="yt-timestamp" data-t="00:54:27">[00:54:27]</a>.
*   **Team Expansion**: Continuing to expand the team, particularly in APAC regions, Europe, and focusing on institutional partnerships <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>, <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a>. These partnerships aim to build interesting extensions of Berachain based on observed growth and opportunities <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>, <a class="yt-timestamp" data-t="00:55:09">[00:55:09]</a>.

For more details on the future, see [[Market Challenges and Future Plans for Berachain]].