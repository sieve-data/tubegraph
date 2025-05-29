---
title: Development and impact of blockchain technology
videoId: qRsvSz7u_d4
---

From: [[acquiredfm]] <br/> 

Blockchain technology, particularly the rapidly emerging Web3 world, is central to modern internet applications. The Brave browser is positioned at the heart of this new era, arguably functioning as the single largest blockchain-based application with over 50 million monthly users <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Key Blockchain Platforms and Projects

### Solana
Solana is described as a global state machine and the world's most performant blockchain <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>. It enables developers to build applications with super low transaction fees and low latency, without compromising composability, as everything resides on a single chain with a global state <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. Solana is capable of processing tens of thousands of smart contracts simultaneously, utilizing a distributed clock via Proof of History to achieve low latency and sub-second finality <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.

### Project Serum
Project Serum is a central limit order book-based exchange built on the [[Solana Foundation | Solana]] blockchain <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. Historically, crypto traders relied on centralized exchanges, which lacked composability and allowed centralized entities unilateral control over funds <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. The shift to decentralized finance (DeFi) introduced new crypto primitives like Automated Market Makers (AMMs), which, while on-chain, lacked the capital efficiency of centralized exchanges <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. Serum addresses this by bringing the central limit order book on-chain, leveraging [[Solana Foundation | Solana]]'s parallel architecture to offer thousands of concurrently operating markets. This provides traders with the low-latency experience common in traditional financial markets, enabling composable on-chain trading of spot, spot margin, perpetuals, and dated futures through applications like Mango Markets <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

### Ethereum and EVM Compatibility
Ethereum has fostered significant developer activity and "animal spirits" around its platform <a class="yt-timestamp" data-t="01:06:54">[01:06:54]</a>. Despite its current challenges with slowness and high gas fees, the Ethereum Virtual Machine (EVM) remains influential <a class="yt-timestamp" data-t="01:07:02">[01:07:02]</a>. Its bytecode and smart contract system are supported across various other chains, such as Polygon and Avalanche's C-chain, which are EVM compatible <a class="yt-timestamp" data-t="01:07:11">[01:07:11]</a>. This compatibility allows for design and code portability across different blockchain ecosystems <a class="yt-timestamp" data-t="01:07:24">[01:07:24]</a>.

## Blockchain Integration in Brave Browser

The Brave browser has embraced blockchain technology as a core part of its mission, aiming to provide a user-first platform <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>.

### Basic Attention Token (BAT)
Brave incorporates the Basic Attention Token (BAT) system, which was prototyped using Bitcoin <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. Users who opt into Brave's private ad system receive 70% of the ad revenue in BAT, which they can use to support creators directly <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>. This system allows users to participate in funding creators without privacy invasion <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>. Brave is designed to connect users, advertisers, and creators flexibly <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.

### Native Wallet Integration
Brave is developing its own native, secure, on-chain hot wallet directly integrated into the browser <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>. This positions Brave as a pioneer, as major browsers like Chrome and Safari do not currently offer such a feature <a class="yt-timestamp" data-t="01:12:03">[01:12:03]</a>. Opera, however, did launch a self-custody wallet and dApp store in 2018 <a class="yt-timestamp" data-t="01:12:20">[01:12:20]</a>. Brave aims to make its wallet multi-chain, with [[Solana Foundation | Solana]] as the default for multi-chain dApps when no preference is expressed by the dApp or user <a class="yt-timestamp" data-t="01:14:08">[01:14:08]</a>.

### Next-Generation Ad System with Zero-Knowledge Proofs
Brave is working on a next-generation ad system called Themis, which aims to move on-chain, specifically targeting [[Solana Foundation | Solana]] <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. Themis uses a black box accumulator in the browser to build cryptographically secure ad performance numbers, which can then be put into a zero-knowledge proof system on-chain <a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>. This allows ad buyers to verify ad performance through truth claims without revealing user data <a class="yt-timestamp" data-t="01:10:24">[01:10:24]</a>.

## Challenges and Future Outlook

### Regulatory and Privacy Concerns
The integration of blockchain and token economics faces significant regulatory hurdles. Sending ad revenue to unknown self-custody wallets can lead to issues with financial regulations such as Anti-Money Laundering (AML) and Office of Foreign Assets Control (OFAC) <a class="yt-timestamp" data-t="01:08:23">[01:08:23]</a>. Know Your Customer (KYC) procedures are often required by custodians to identify financial flows <a class="yt-timestamp" data-t="01:09:02">[01:09:02]</a>. Furthermore, while users may seek anonymity on-chain, blockchain forensics can often de-anonymize wallets <a class="yt-timestamp" data-t="01:09:11">[01:09:11]</a>.

### User Experience vs. Security
A persistent trade-off exists between security and user experience in the crypto space <a class="yt-timestamp" data-t="01:19:05">[01:19:05]</a>. Self-custody, while offering greater ownership and privacy, introduces complexities for users who may fear losing private keys or struggle with managing them securely <a class="yt-timestamp" data-t="01:16:34">[01:16:34]</a>. This contrasts with traditional banking, which, while offering less autonomy, provides a smoother and less confusing user experience <a class="yt-timestamp" data-t="01:19:19">[01:19:19]</a>.

### Decentralization and Centralized Choke Points
Despite the promise of decentralization, some centralized choke points currently remain necessary to make blockchain technologies usable and efficient <a class="yt-timestamp" data-t="01:22:03">[01:22:03]</a>. Services like Infura, OpenSea, Coinbase, and Etherscan provide crucial indexing and querying capabilities that are difficult for individual users to replicate <a class="yt-timestamp" data-t="01:22:09">[01:22:09]</a>. The speaker acknowledges that servers will continue to endure alongside peer-to-peer networks <a class="yt-timestamp" data-t="01:24:04">[01:24:04]</a>. Web3 is seen as extending Web2, rather than completely replacing it <a class="yt-timestamp" data-t="01:24:10">[01:24:10]</a>. The goal is to leverage cryptography to achieve a fairer deal for users, allowing them to exert market power and secure better privacy and security properties from centralized services <a class="yt-timestamp" data-t="01:24:38">[01:24:38]</a>.

### Future Growth
Brave aims for significant growth, targeting 400 million monthly active users within three years <a class="yt-timestamp" data-t="01:28:47">[01:28:47]</a>. Achieving this scale would grant them substantial influence in web and crypto standards <a class="yt-timestamp" data-t="01:29:31">[01:29:31]</a>. This growth is anticipated to facilitate direct connections between fans and creators, enabling them to transact without demonetization or censorship <a class="yt-timestamp" data-t="01:31:29">[01:31:29]</a>. The use of Non-Fungible Tokens (NFTs) is also being explored as a basis for creator tokenomics <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a>. The ultimate goal is to move towards a system of direct on-chain sends, reducing reliance on custodians, but this still faces usability challenges <a class="yt-timestamp" data-t="01:33:51">[01:33:51]</a>.