---
title: Proof of Liquidity Concept
videoId: fJ8y7Y15vT0
---

From: [[bankless]] <br/> 
## Proof of Liquidity on Bar Chain

Proof of Liquidity is the core innovation of Bar Chain, a new Layer 1 blockchain. It is designed as an economic experiment to align liquidity and security at the protocol level, aiming to create a sustainable and self-reinforcing ecosystem for decentralized applications <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a> <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### Core Mechanism

Proof of Liquidity operates through a "three-party flywheel" involving three key economic actors:
1.  **Bar Chain's Application Layer** <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
2.  **Validators** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
3.  **Users holding the BGT (Bar Governance Token)** <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

The mechanism is built on two tokens:
*   **Bara (BERA)**: The native currency of the network, used for gas fees and staking <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a> <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a> <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. It functions similarly to ETH on Ethereum, where staking more Bara increases the frequency of a validator's block production <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a> <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **BGT (Bar Governance Token)**: A non-transferable, soulbound token <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. BGT cannot be earned by staking BGT itself; instead, it is primarily earned by providing liquidity on the network <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a> <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. BGT also has a one-way burn mechanism from Bara: 1 Bara can be burned to create 1 BGT <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a> <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>. This means users can gain governance power by providing value (liquidity) or by burning Bara <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.

#### Validator Rewards and Emission Distribution
The size of a validator's block reward is determined by the amount of BGT delegated to it <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. Crucially, these BGT block rewards are not primarily reaped by the validator directly, but are instead emitted into the ecosystem <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. Validators can choose to direct these BGT emissions towards specific pools, vaults, or stable tokens from applications on the network <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a> <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>.

This creates an "order book" or marketplace where applications can propose bids to validators, offering their own tokens in exchange for BGT emissions directed towards their liquidity pools <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a> <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>. Validators can then take a cut of these commissions and distribute the rest to their BGT delegates <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. This allows dApps to price their own liquidity using the network's emissions <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.

#### The Flywheel in Action
1.  **Liquidity Providers** earn BGT by providing liquidity to whitelisted pools on the network <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a> <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
2.  **BGT Holders** delegate their non-transferable BGT to validators <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a> <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
3.  **Validators**, who also stake Bara for block frequency, receive larger block rewards (in BGT) based on BGT delegations <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
4.  **Applications** collaborate with validators, offering their own tokens in exchange for validators directing BGT emissions to their liquidity pools <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a> <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.
5.  This incentivizes liquidity provision for applications, driving value back to the chain, while the chain's design drives value back to the application layer <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.

### Goals and Philosophy

The core idea behind Proof of Liquidity is to address the dichotomy often seen in Proof-of-Stake networks where significant capital secures the chain, but there isn't always sufficient liquidity present on the network itself <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Bar Chain aims to build a chain that aligns liquidity and security at the protocol level, ensuring that user capital allocation incentives point in the same direction <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

This mechanism intends to:
*   **Bootstrap Liquidity:** Provide a sustainable way for applications to gain liquidity beyond traditional, often unsustainable, liquidity mining programs <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a> <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.
*   **Support the Application Layer:** Offer protocol-level support to the application layer, unlike burst-like grant programs seen on other networks <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a> <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>. The goal is for the application layer to be value-additive to the network, not value-extractive <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
*   **Integrate Security and Applications:** Dissolve the separation between the application layer and the underlying blockchain infrastructure <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.
*   **Promote Capital Efficiency:** By tying liquidity provision to network security, it aims to achieve a better ratio of security to liquidity compared to traditional Proof-of-Stake chains <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>.

### Challenges and Outlook

Proof of Liquidity is acknowledged as an "economic experiment" with uncertain outcomes <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>. Concerns include:
*   **Sustainability:** Ensuring the system finds a "sustainable Nash equilibrium" and doesn't lead to issues like cartelization or value being directed to dead ends <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>.
*   **Centralization:** The risk of BGT emissions concentrating on a few pairs, effectively reverting to a standard Proof of Stake model <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a> <a class="yt-timestamp" data-t="00:36:27">[00:36:27]</a>.

Bar Chain addresses these by:
*   **Social Layer Conditioning:** Guiding the community towards differentiated use cases that leverage capital velocity and focus on applications with strong product-market fit and fee generation <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a>.
*   **Guardian Council:** An external, third-party council performs economic audits and acts as an "emergency break" to prevent malicious value extraction or attacks <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.

The project emphasizes setting up the system for success with guard rails, but acknowledges that as a decentralized network, it is a free-flowing ecosystem <a class="yt-timestamp" data-t="00:38:11">[00:38:11]</a>. The goal is for Proof of Liquidity to be a "force multiplier" that helps applications cross the "Chasm of Death" and achieve product-market fit <a class="yt-timestamp" data-t="00:31:28">[00:31:28]</a>.

### Market Penetration and Scaling

In a saturated crypto market, Bar Chain aims to differentiate itself through its focus on the application layer and the unique incentives provided by Proof of Liquidity <a class="yt-timestamp" data-t="00:39:06">[00:39:06]</a>. The ecosystem has a robust set of novel applications, including DeFi protocols, gaming, consumer, and social applications, as well as Layer 2s building on Bar Chain <a class="yt-timestamp" data-t="00:39:30">[00:39:30]</a> <a class="yt-timestamp" data-t="00:40:07">[00:40:07]</a>.

Bar Chain is an EVM-identical L1, meaning it runs unmodified Ethereum execution clients, making it easy to build OP Stack or Arbitrum Orbit rollups on top <a class="yt-timestamp" data-t="00:40:39">[00:40:39]</a>. This allows for closer intertwining and alignment between L1s and L2s, with Proof of Liquidity potentially forming relationships where L2 governance tokens are paired against Bara, generating native yield for the L2's bridge contract <a class="yt-timestamp" data-t="00:41:34">[00:41:34]</a>.

From a technical scaling perspective, Bar Chain is built on a framework called Beacon Kit, which allows for plug-and-play between consensus and execution layers <a class="yt-timestamp" data-t="00:44:29">[00:44:29]</a>. It is optimized for CometBFT (formerly Tendermint) consensus, providing single-slot finality <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>. While Tendermint has scaling limits for validator sets (currently around 69, expanding to 200), the framework allows for future upgrades to consensus engines for further decentralization and scale <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a> <a class="yt-timestamp" data-t="00:46:28">[00:46:28]</a>. The focus is on a fast user experience with sub-two-second block times and near-instant finality <a class="yt-timestamp" data-t="00:45:53">[00:45:53]</a>.