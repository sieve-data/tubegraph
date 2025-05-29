---
title: Security Measures in Blockchain Interoperability
videoId: RUmWyIScfsc
---

From: [[thepipeline_xyz]] <br/> 

[[interoperability_in_blockchain_networks | Blockchain interoperability]] is a critical aspect of the evolving blockchain landscape, but it comes with significant [[security_concerns_and_solutions_in_blockchain_ecosystems | security concerns]]. Historically, centralized bridges have been a major point of vulnerability, leading to substantial financial losses [00:03:47].

## Historical Vulnerabilities: Centralized Bridges
Many early cross-chain solutions, such as Ren Protocol and Multi-chain, operated as centralized bridges [00:03:47]. These systems typically relied on a single founder or entity holding keys to funds [00:04:02]. This centralization proved to be a critical flaw, as compromising a single key could lead to the loss of all funds [00:04:07]. Major hacks in the DeFi space, including the Harmony hack, the Ronin hack, and the Multi-chain incident, were direct consequences of this centralization [00:04:14].

## Axelar's Decentralized Approach
Axelar was designed to address these fundamental [[security_concerns_and_solutions_in_blockchain_ecosystems | security concerns]] by taking a fundamentally different approach to cross-chain communication [00:04:26]. Rather than being a simple bridge, Axelar functions as a messaging platform built as a blockchain itself, connecting 56 different blockchains [00:03:30].

A key differentiator for Axelar is its emphasis on decentralization [00:06:05]. Built on the Cosmos SDK, Axelar features a fully decentralized validator set [00:06:07]. With 75 validators, attacking the network to steal funds would require corrupting a majority of these validators [00:06:24]. This distributed control makes Axelar "almost as secure as all of the chains that it connects to" [00:06:33], given that it includes many of the largest validators from major blockchain networks [00:06:33]. Axelar asserts that it is significantly more decentralized than many competitors, reportedly five times more decentralized than Wormhole, which has 19 validators [00:06:55]. This high degree of decentralization is considered a critical feature for enhancing [[security_concerns_and_solutions_in_blockchain_ecosystems | security]] [00:07:06].

## Enhanced Security Mechanisms

### Rate Limiting
Beyond decentralization, Axelar implements additional [[security_concerns_and_solutions_in_blockchain_ecosystems | security measures]] such as rate limiting [00:23:43]. Rate limiting is a simple but effective code-based check designed to minimize the impact of a hack [00:23:46]. Even if other parts of the codebase are compromised, a rate limit can cap the amount of funds that can be moved within a specific period, thereby minimizing potential damage [00:23:58].

Axelar's architecture, with its many-to-many connectivity and central blockchain, allows for customizable rate limits on the Axelar blockchain itself [00:24:04]. This means that even if an issue occurs on one of the connected blockchains, the damage can be contained by Axelar's rate limits [00:24:15]. These limits can be hourly, over six hours, or even refreshed more frequently (e.g., every 20-30 minutes) based on conditions and monitoring by a dedicated committee [00:26:57]. While not a perfect solution for absolute numbers, rate limiting remains a valuable mechanism to significantly reduce the risk compared to the total value locked (TVL) of assets [00:27:17]. Live data can also be used as a heuristic for selecting appropriate rate limits [00:27:32].

### Multi-Solution Approval
For applications requiring the highest level of [[security_concerns_and_solutions_in_blockchain_ecosystems | security]], Axelar supports multi-solution approval mechanisms. A notable example is Lido's decision to jointly work with Axelar and Wormhole for asset minting [00:24:51]. This setup requires approval from both Axelar's validator set and Wormhole's validator set before an asset is minted [00:25:23]. This creates three layers of [[security_concerns_and_solutions_in_blockchain_ecosystems | security]]: two fully independent implementations for validation, plus the option to stack rate limits on top [00:25:29]. This layered approach aims to provide the most robust cross-chain [[security_concerns_and_solutions_in_blockchain_ecosystems | security]] seen to date [00:25:36].

## Asset Security: Native vs. Wrapped Assets
The debate between native and wrapped assets often arises in discussions of cross-chain [[security_concerns_and_solutions_in_blockchain_ecosystems | security]] [00:22:14]. However, regardless of whether an asset is "native" or "wrapped," its security fundamentally depends on the underlying [[crypto_interoperability_and_crosschain_communication | bridging infrastructure]] [00:22:26]. An asset deployed across multiple chains using insecure bridging infrastructure is just as vulnerable as a wrapped asset using that same insecure infrastructure [00:22:36]. Therefore, the critical factor is robust [[security_concerns_and_solutions_in_blockchain_ecosystems | security practices]] and strong contingency mechanisms within the bridging solution itself [00:23:00]. This ensures that even in unforeseen circumstances, potential damage can be minimized [00:23:04].