---
title: Security and scalability in crosschain communication
videoId: RUmWyIScfsc
---

From: [[thepipeline_xyz]] <br/> 

The Axel Network is an [[interoperability_and_blockchain_communication | interoperability]] network structured as a blockchain that connects various other blockchains, currently supporting 56 and growing <a class="yt-timestamp" data-t="03:30:30">[03:30:30]</a>. While it solves the bridging problem, Axel is primarily a messaging platform upon which diverse applications like cross-chain DEXes, money markets, and NFT marketplaces can be built <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.

## Challenges with Centralized Bridges

Historically, centralized bridges like Ren protocol and Multi-Chain (which recently lost all funds) were prevalent <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. These bridges were not designed to scale and typically relied on centralized entities holding funds in a single key <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. Once this key was compromised, all funds could be lost, as seen in major DeFi hacks like Harmony, Ronin, and Multi-Chain <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. This centralization was the root cause of these vulnerabilities <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.

## Axel Network's Approach to Security

Axel takes a different approach to [[challenges_and_solutions_in_blockchain_bridging | solving cross-chain challenges]], focusing on decentralization and robust security measures <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.

### Decentralized Validator Set
Axel is designed as a blockchain based on the Cosmos SDK, featuring a fully decentralized validator set <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. With 75 validators, attacking the network to steal funds would require corrupting a majority of them <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>. This makes Axel almost as secure as the chains it connects to, differentiating it from competitors like Wormhole (19 validators) and others with only a handful <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>. This decentralization is crucial for security <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.

### Rate Limiting
Rate limiting is a simple but effective piece of code that can be added to every transaction to minimize the impact of a hack, even if the rest of the codebase is compromised <a class="yt-timestamp" data-t="23:46:00">[23:46:00]</a>. Axel's many-to-many connectivity architecture allows for customizable rate limits on the Axel blockchain itself <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>. This means that even if a connected blockchain breaks, damage can be contained, and if Axel itself faces an issue, rate limits can still minimize the damage <a class="yt-timestamp" data-t="24:12:00">[24:12:00]</a>. These limits can be set hourly or over longer periods (e.g., six hours), and potentially refreshed more frequently in the future based on real-time data <a class="yt-timestamp" data-t="26:57:00">[26:57:00]</a>.

### Layered Security
For applications requiring extreme security, such as Lio, a layered approach can be implemented <a class="yt-timestamp" data-t="24:40:00">[24:40:00]</a>. Lio's community voted to work with both Axel and Wormhole, requiring approval from both validator sets before an asset is minted <a class="yt-timestamp" data-t="24:54:00">[24:54:00]</a>. This combines two independent implementations with stacked rate limits, creating three layers of security for cross-chain assets <a class="yt-timestamp" data-t="25:29:00">[25:29:00]</a>.

## Axel Network's Approach to Scalability

Axel's architecture directly addresses [[blockchain_scalability_and_highperformance_systems | blockchain scalability]] challenges, particularly in the context of connecting numerous chains <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>.

### Many-to-Many Connectivity
A key differentiator for Axel is its many-to-many connectivity model <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. By acting as a blockchain connected to other blockchains, Axel enables a one-off connection to its network, through which messages can be routed to any other connected blockchain <a class="yt-timestamp" data-t="05:25:00">[05:25:25]</a>. This contrasts with competitors who often offer only pairwise connectivity, making it significantly harder to add new chains and limiting connections to a subset of available chains <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>. This architecture greatly simplifies adding new chains <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.

### Simplified Developer Experience (General Message Passing - GMP)
Axel's General Message Passing (GMP) protocol allows developers to build cross-chain applications without needing to redeploy on numerous chains <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>. Developers can maintain the core logic of their application (the "brain") on a fast EVM chain like Monad, while users from other networks can seamlessly interact with it through small pieces of code deployed on their respective chains <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>. This abstracts away the complexity of Web3, enabling direct user interaction without intermediate bridging steps <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>. Developers can send their first message through Axel's documentation in approximately 10 minutes <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.

### Interchain Token Service
The Interchain Token Service, currently in beta, is a code-free, permissionless tokenization and bridging solution <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>. It allows anyone, including those without coding experience, to launch a token across multiple chains from day one with the best security <a class="yt-timestamp" data-t="19:56:00">[19:56:00]</a>. This service aims to change the industry by making it "meaningless" to launch a token on only a single chain, promoting native cross-chain deployment <a class="yt-timestamp" data-t="20:11:00">[20:11:00]</a>.

## Evolution and Future of Interoperability

The demand for [[interoperability_and_blockchain_communication | interoperability]] has rapidly evolved. A year ago, many teams were content operating on a single chain, but now, launching on two or three chains with plans for more is standard <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>. This shift is driven by the rapid fragmentation of liquidity and users across an increasing number of blockchains (thousands of chains are projected) <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>.

### Impact of High-Performance Blockchains
The emergence of high-performance blockchains like Monad, with fast transaction finality, significantly improves the user experience for cross-chain applications <a class="yt-timestamp" data-t="16:57:00">[16:57:00]</a>. While Ethereum transactions can take 15-20 minutes, or even longer for L2s, messages on chains like Monad can pass in 60-90 seconds, making cross-chain interactions more accessible and cheaper due to lower gas costs <a class="yt-timestamp" data-t="13:44:00">[13:44:00]</a>. This will lead to an exponential increase in cross-chain transactions as the number of chains grows <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>.

### Ubiquitous Interoperability
In the long term, [[interoperability_and_blockchain_communication | interoperability]] is expected to become an invisible layer integrated into every application across DeFi, gaming, real-world asset tokenization, and NFTs <a class="yt-timestamp" data-t="31:10:00">[31:10:00]</a>. The goal is to abstract away the underlying blockchain complexities, allowing users to only focus on assets and applications, with wallets managing cross-chain balances and communication seamlessly <a class="yt-timestamp" data-t="31:33:00">[31:33:00]</a>. This vision positions [[interoperability_and_blockchain_communication | interoperability]] as a fundamental component of the Web3 experience <a class="yt-timestamp" data-t="32:07:00">[32:07:07]</a>.