---
title: Challenges and Solutions in Decentralized Finance DeFi
videoId: RUmWyIScfsc
---

From: [[thepipeline_xyz]] <br/> 

## The Need for Decentralized Finance
The inspiration for getting into the blockchain space, particularly Decentralized Finance ([[Innovations in Decentralized Finance | DeFi]]), stemmed from real-world financial crises. During the massive financial crisis in Greece, it became nearly impossible to send remittances or withdraw money from banks <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>. This experience underscored the importance of a censorship-resistant financial system where anyone can seamlessly transact globally using just a cell phone, especially given that many people have cell phones but lack bank accounts <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.

## [[Challenges and solutions in building decentralized applications | Challenges and Solutions in Building Decentralized Applications]] for DeFi
### Centralized Bridge Vulnerabilities
Historically, a major challenge in [[Innovations in Decentralized Finance | DeFi]] has been the centralization of bridging solutions. Early centralized bridges, such as Ren Protocol and Multi-chain, were susceptible to hacks because centralized entities held all funds in a single key <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. Once this key was compromised, all funds were lost, as evidenced by major hacks like Harmony, Ronin, and Multi-chain, which collectively resulted in billions of dollars in losses <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>. Multi-chain, for instance, recently lost all its funds <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

### Axelar's Decentralized Interoperability Solution
Axelar offers a different approach to cross-chain problems by acting as an interoperability network structured as a blockchain, rather than a bridge <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. It connects 56 blockchains and counting <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.

Key differentiators include:
*   **Many-to-Many Connectivity** Axelar's blockchain architecture allows for many-to-many connectivity, enabling a single connection to the Axelar blockchain to route messages to any other connected blockchain <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. This contrasts with pairwise connectivity offered by competitors, which makes adding new chains significantly harder <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.
*   **Enhanced Security Through Decentralization** Built on the Cosmos SDK, Axelar has a fully decentralized validator set, comprising 75 validators <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. To attack the network and steal funds, a majority of these validators would need to be corrupted <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>. Axelar is considered almost as secure as the largest chains it connects to, being five times more decentralized than solutions like Wormhole, which has 19 validators <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>.

### Onboarding Users and Developers
A significant challenge in [[Innovations in Decentralized Finance | DeFi]] has been onboarding users and developers to new blockchains, especially those with new virtual machines <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. For example, during Algorand's launch, liquidity was primarily on Ethereum, making it difficult for users to bridge assets <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.

Axelar addresses this by:
*   **General Message Passing (GMP)** Providing a general message passing platform on which various cross-chain applications can be built, including DEXes, money markets, and NFT marketplaces <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>. This abstracts away the complexities of Web3, focusing on user experience <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.
*   **Streamlined Development** Developers can deploy the "brain" of their application on a fast EVM chain like Monad, allowing users from other networks to interact seamlessly <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>. For example, users can open positions on a perps DEX built on Monad directly from chains like Arbitrum or Solana by effectively connecting a small piece of code on the origin chain to Axelar's endpoint <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. This process means no intermediate bridging step, enhancing user experience <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>. Sending a first message through Axelar can take as little as 10 minutes <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.
*   **Reducing Fragmentation** This approach centralizes application logic on one chain, preventing fragmentation and simplifying development <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.

### Cross-Chain Gas Fees and Latency
Cross-chain transactions currently incur high gas fees as users must pay for gas on the source chain, destination chain, and relay costs <a class="yt-timestamp" data-t="13:44:00">[13:44:00]</a>. This remains a prohibitive factor, even for L2s, with transactions costing from a few dollars to nearly $10 <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.

However, the proliferation of new scaling solutions and chains like Monad, which offer lower gas costs and instant finality, is expected to make cross-chain transactions cheaper and more accessible <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>. Instant finality is crucial because it reduces the time for a cross-chain command to pass from 15-20 minutes (on Ethereum) to 60-90 seconds (on chains like Monad), significantly improving user experience <a class="yt-timestamp" data-t="16:57:00">[16:57:00]</a>.

### Liquidity Fragmentation
[[Challenges and innovations in blockchain development | Decentralized Finance]] also faces liquidity fragmentation across multiple stablecoins and assets, often siloed on specific chains and requiring wrapping <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>.

Axelar's **Interchain Token Service** (ITS), currently in beta, aims to solve this by providing a code-free, permissionless tokenization and bridging solution <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>. This enables anyone to launch a token that is cross-chain from day one with robust security, supporting future scalability to any chain Axelar connects to <a class="yt-timestamp" data-t="19:07:00">[19:07:00]</a>. This service allows projects, such as Frax, to issue assets on new chains without needing to build and maintain their own native bridges <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>.

## Mitigating Interoperability Risk
Regardless of whether assets are native or wrapped, security hinges on the underlying bridging infrastructure <a class="yt-timestamp" data-t="22:26:00">[22:26:00]</a>. If insecure infrastructure is used, a loss can be catastrophic for any asset type <a class="yt-timestamp" data-t="22:39:00">[22:39:00]</a>.

Axelar mitigates risk through:
1.  **Decentralization:** As the first and only decentralized network to secure cross-chain assets, it eliminates the most common attack vector that has caused billions in losses <a class="yt-timestamp" data-t="23:16:00">[23:16:00]</a>.
2.  **Rate Limiting:** A simple code check at the end of every transaction can minimize damage during a hack <a class="yt-timestamp" data-t="23:46:00">[23:46:00]</a>. Axelar's many-to-many connectivity architecture allows for customizable rate limits on the Axelar blockchain itself, containing damage even if a connected chain breaks <a class="yt-timestamp" data-t="24:04:00">[24:24:00]</a>.
3.  **Multi-layered Security:** For maximum security, solutions like Lido have opted for a joint approval model, requiring verification from both Axelar's and Wormhole's validator sets before an asset is minted on a new chain <a class="yt-timestamp" data-t="24:49:00">[24:49:00]</a>. This combines two independent implementations with stacked rate limits, creating three layers of security <a class="yt-timestamp" data-t="25:29:00">[25:29:00]</a>. While rate limits might not perfectly align with extremely high throughput blockchains, they significantly minimize potential damage relative to the total value locked <a class="yt-timestamp" data-t="26:19:00">[26:19:00]</a>.

## Future of Interoperability in [[Innovations in Decentralized Finance | DeFi]]
Interoperability is not a "killer use case" itself, but rather an enabler for a seamless user experience in Web3, making it as easy to use as Web2 <a class="yt-timestamp" data-t="31:10:00">[31:10:00]</a>. The goal is to abstract away the underlying blockchain complexities, so users only need to think about assets and applications <a class="yt-timestamp" data-t="31:35:00">[31:35:00]</a>. For example, a user's wallet should aggregate total USDC balances across different chains and present a unified balance, using interoperability infrastructure to pass messages across networks without the user needing to know which chain an asset or application resides on <a class="yt-timestamp" data-t="31:50:00">[31:50:00]</a>.

In the next four years, interoperability is expected to be integrated into virtually every [[Challenges and opportunities for new applications in crypto and blockchain | application in the space]], including [[Innovations in Decentralized Finance | DeFi]], gaming, real-world asset tokenization, and NFTs <a class="yt-timestamp" data-t="32:08:00">[32:08:00]</a>.