---
title: Security and decentralization in blockchain
videoId: RUmWyIScfsc
---

From: [[thepipeline_xyz]] <br/> 

Security and [[decentralization_in_blockchain | decentralization]] are fundamental pillars in the design and operation of blockchain networks and their associated infrastructure. The history of decentralized finance (DeFi) has highlighted the critical importance of these aspects, particularly in cross-chain solutions.

## The Problem with Centralized Bridges

Historically, many early cross-chain bridges, such as Ren protocol and Multi-chain, operated as centralized entities. These bridges typically relied on a founder or a small centralized group holding all funds in a single key <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. This centralized control presented a significant vulnerability: once the key was compromised, all funds were at risk, which proved to be "just a matter of time" <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

Major hacks in the DeFi space, including the Harmony hack, the Ronin hack, and the Multi-chain incident, collectively resulted in billions of dollars lost. These incidents "all happened because of centralization" <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, underscoring the severe [[Challenges in blockchain system design | challenges in blockchain system design]] inherent in centralized bridging solutions.

## Axelar's Decentralized Approach

Axelar, as an [[interoperability_network | interoperability network]], adopted a "very different approach to solving the cross chain problem" by not being a bridge itself, but rather a messaging platform <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Its core design focuses on enhancing [[Crypto transaction security | security]] and [[decentralization_in_blockchain | decentralization]]:

1.  **Blockchain Architecture**: Axelar is structured as a blockchain built on the Cosmos SDK <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This architecture enables "many to many connectivity" <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>, allowing a single connection to Axelar to route messages to any of its 56+ connected blockchains <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This contrasts with competitors like Wormhole and Chainlink CCIP, which primarily offer "pairwise connectivity," making it harder to add new chains <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
2.  **Decentralized Validator Set**: A crucial aspect of Axelar's [[decentralization_in_blockchain | decentralization]] and [[Crypto transaction security | security]] is its fully decentralized validator set <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. With 75 validators, many of whom are familiar from the Ethereum mainnet <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>, attacking the network to steal funds would require corrupting a majority of these validators <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. This makes Axelar "almost as secure as all of the chains that it connects to" <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>, and it is significantly more decentralized than many competitors, with five times more validators than Wormhole (75 vs. 19) <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

## Mitigating Interoperability Risk

Regardless of whether assets are deployed as native or wrapped tokens, the [[Crypto transaction security | security]] of the underlying bridging infrastructure is paramount <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>. Axelar implements several layers of [[Crypto transaction security | security]] to minimize potential damage:

*   **Decentralization**: As discussed, the decentralized validator set removes the most common attack vector seen in centralized bridges <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
*   **Rate Limiting**: This simple code check can be added to every transaction to cap the amount of funds that can be moved within a certain timeframe, effectively minimizing the impact of a hack <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. Axelar's architecture allows for customizable rate limits on the Axelar blockchain itself, containing damage even if a connected blockchain experiences a break <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>. While not perfect for very high throughput chains, rate limiting can still "minimize the damage compared to the the full tvl of the different assets" <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>.
*   **Multi-Party Approval (External)**: For extreme [[Crypto transaction security | security]], applications can implement multi-party approval systems. For example, the Lido community decided to work jointly with Axelar and Wormhole, requiring approval from both validator sets before an asset is minted <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. This layered approach combines two independent implementations with stacked rate limits, creating "the most secure thing we've seen in terms of cross chain security so far" <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.

## Interchain Token Service (ITS)

Axelar's Interchain Token Service (ITS), currently in beta, exemplifies the ethos of [[decentralization_in_blockchain | decentralization]] and permissionless access. It is described as the "first code-free permissionless tokenization and bridging solution" <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. Anyone, regardless of their development skills, can use a front-end to take their token cross-chain in minutes <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>. This feature is expected to transform token launches, making it "meaningless" to launch a token on only a single chain <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>, and making cross-chain token launches the standard from day one <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

## The Future of Interoperability

The evolution of interoperability sees a shift from projects being content on a single chain to planning deployments across multiple chains from the outset <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. This is driven by the rapid growth in the number of chains and the shifting landscape of liquidity and users <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.

Ultimately, interoperability is not about a "killer use case" but about improving the overall "user experience" <a class="yt-timestamp" data-t="00:31:12">[00:31:12]</a>, making Web3 as easy to use as Web2 <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>. The goal is to abstract away the underlying blockchain complexities from the user, allowing them to focus solely on assets and applications <a class="yt-timestamp" data-t="00:31:35">[00:31:35]</a>. This vision suggests that interoperability will become an integral part of virtually every use case, from DeFi and gaming to real-world asset tokenization and NFTs <a class="yt-timestamp" data-t="00:32:11">[00:32:11]</a>.