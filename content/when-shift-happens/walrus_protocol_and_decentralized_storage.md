---
title: Walrus Protocol and decentralized storage
videoId: O9qGzOlFajU
---

From: [[when-shift-happens]] <br/> 

## Introduction to Walrus Protocol

Walrus Protocol is described as a [[decentralized_exchanges_and_liquidity_protocols | decentralized]] secure storage network designed for rich media and large data files <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. George Dazes, Chief Scientist and Co-founder at Mistin Labs, is one of the masterminds behind it <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The timing for Walrus Protocol is considered opportune because technology now provides an effective coordination layer with low latency, high bandwidth, and low cost <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Understanding Decentralized Storage

In a [[decentralized_exchanges_and_liquidity_protocols | decentralized]] storage network, files are not stored in one central location but are distributed across multiple places <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, <a class="yt-timestamp" data-t="01:20:40">[01:20:40]</a>. This means there is no single point of failure; a significant portion of the infrastructure can go offline, and users can still access their files <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, <a class="yt-timestamp" data-t="01:20:59">[01:20:59]</a>.

The biggest problems with traditional data storage include:
*   **Availability**: Files stored on a single computer are vulnerable to loss (e.g., house fire), and cloud providers can restrict access or go out of business <a class="yt-timestamp" data-t="01:17:36">[01:17:36]</a>, <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>.
*   **Censorship**: Centralized providers can block users from accessing or distributing content <a class="yt-timestamp" data-t="01:18:43">[01:18:43]</a>.
*   **Integrity**: Ensuring that retrieved files are the original, unedited versions <a class="yt-timestamp" data-t="01:19:01">[01:19:01]</a>.

[[decentralized_exchanges_and_liquidity_protocols | Decentralized]] storage, like Walrus, aims to solve these issues by ensuring files are available, resistant to censorship, and verifiable, free from central entities that might violate these properties <a class="yt-timestamp" data-t="01:19:49">[01:19:49]</a>. Walrus Protocol focuses on storing "big things" such as images, machine learning datasets, and audit logs, ranging from megabytes to terabytes, which differs from the smaller data (few hundred to thousand characters) typically stored directly on commodity [[blockchain_scalability_and_polkadot | blockchains]] <a class="yt-timestamp" data-t="01:21:41">[01:21:41]</a>.

## The Evolution of Decentralization

### Early Peer-to-Peer Systems
George Nezes's engagement with peer-to-peer systems began during his PhD in the early 2000s, when the internet was a hot topic <a class="yt-timestamp" data-t="02:11:01">[02:11:01]</a>. The core idea of the peer-to-peer movement was to allow people to interconnect and perform actions without mediation from large telecommunication companies or banks <a class="yt-timestamp" data-t="02:12:05">[02:12:05]</a>, <a class="yt-timestamp" data-t="02:22:23">[02:22:23]</a>. This ethos of building communities not mediated by big institutions continues to resonate <a class="yt-timestamp" data-t="02:20:53">[02:20:53]</a>.

However, early peer-to-peer systems faced significant challenges <a class="yt-timestamp" data-t="02:28:23">[02:28:23]</a>:
*   **Sybil Attack Problem**: The inability to distinguish between real entities and virtual "sock puppets" online made decentralized decision-making like voting unworkable <a class="yt-timestamp" data-t="01:18:20">[01:18:20]</a>, <a class="yt-timestamp" data-t="02:28:28">[02:28:28]</a>.
*   **Economic Sustainability**: The reliance on "spare capacity" (e.g., users' extra disk space) proved to be a fallacy, as providing reliable services still incurs costs for bandwidth, storage, compute, and operations, for which there was no solid business model or compensation <a class="yt-timestamp" data-t="02:26:11">[02:26:11]</a>, <a class="yt-timestamp" data-t="02:29:01">[02:29:01]</a>.
*   **Limited Functionality**: These systems, like BitTorrent, were popular for file sharing but lacked the ability to process consistent transactions or manage complex states, limiting their scope beyond basic content distribution <a class="yt-timestamp" data-t="02:30:18">[02:30:18]</a>.

### The Rise of Blockchains
The landscape changed with Bitcoin and Ethereum, which introduced the concept of transaction systems in open, permissionless settings <a class="yt-timestamp" data-t="03:09:12">[03:09:12]</a>, <a class="yt-timestamp" data-t="03:22:56">[03:22:56]</a>. Bitcoin solved the Sybil attack problem using Proof of Work, and later, Proof of Stake emerged <a class="yt-timestamp" data-t="01:19:07">[01:19:07]</a>, <a class="yt-timestamp" data-t="01:19:21">[01:19:21]</a>.

Ethereum was George Nezes's "aha moment" because it introduced a programming language (Solidity) and the ability to define custom rules for updating state via smart contracts, making the system programmable beyond simple currency transactions <a class="yt-timestamp" data-t="03:38:26">[03:38:26]</a>. This expanded the imagination of what [[blockchain_scalability_and_polkadot | blockchain]] systems could do, exemplified by "CryptoKitties," which demonstrated that [[blockchain_scalability_and_polkadot | blockchains]] could be used for fun, social applications beyond just money <a class="yt-timestamp" data-t="05:39:12">[05:39:12]</a>, <a class="yt-timestamp" data-t="05:49:02">[05:49:02]</a>.

Despite these breakthroughs, early [[blockchain_scalability_and_polkadot | blockchains]] had limitations in speed and cost, as seen with CryptoKitties' high transaction fees <a class="yt-timestamp" data-t="05:22:56">[05:22:56]</a>. This led to a focus on scaling up these systems for more transactions and lower latency <a class="yt-timestamp" data-t="03:16:17">[03:16:17]</a>, <a class="yt-timestamp" data-t="03:41:16">[03:41:16]</a>.

## Mistin Labs, Sui, and Walrus Protocol

George Nezes and his co-founders at Mistin Labs (formed after Facebook's Diem project folded) are building the Sui network, a modern [[blockchain_scalability_and_polkadot | blockchain]] <a class="yt-timestamp" data-t="03:48:48">[03:48:48]</a>, <a class="yt-timestamp" data-t="04:13:58">[04:13:58]</a>. Sui is presented as an effective "coordination layer" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="03:37:36">[03:37:36]</a>. Its purpose is to solve the age-old problem of coordinating across space and time without relying on centralized intermediaries that extract value <a class="yt-timestamp" data-t="04:47:50">[04:47:50]</a>, <a class="yt-timestamp" data-t="05:00:01">[05:00:01]</a>. By enabling users to keep their books (transactions) on Sui, everyone can see updates almost instantly and conduct secure, robust transactions quickly and cheaply <a class="yt-timestamp" data-t="05:09:51">[05:09:51]</a>, <a class="yt-timestamp" data-t="05:09:56">[05:09:56]</a>.

Walrus Protocol leverages Sui as its underlying transaction system <a class="yt-timestamp" data-t="01:24:41">[01:24:41]</a>. Sui handles:
*   Payments for storage <a class="yt-timestamp" data-t="01:24:44">[01:24:44]</a>
*   Management of storage space ownership <a class="yt-timestamp" data-t="01:24:47">[01:24:47]</a>
*   Defining what data should be stored or deleted <a class="yt-timestamp" data-t="01:24:51">[01:24:51]</a>
*   Managing the set of storage nodes and data handovers <a class="yt-timestamp" data-t="01:24:53">[01:24:53]</a>

This reliance on Sui’s low latency, high bandwidth, and low-cost coordination allows Walrus to focus on augmenting Sui with big file storage capabilities <a class="yt-timestamp" data-t="01:25:01">[01:25:01]</a>.

Walrus Protocol benefits from being built on Sui for several reasons <a class="yt-timestamp" data-t="01:25:39">[01:25:39]</a>:
*   **Efficiency**: Sui performs coordination functions very well, being cheap and low-latency <a class="yt-timestamp" data-t="01:25:47">[01:25:47]</a>.
*   **Composability**: Representing storage-related assets on Sui allows them to be combined with other Sui ecosystem components like [[decentralized_exchanges_and_liquidity_protocols | Decentralized exchanges and liquidity protocols]] (DeFi) or stablecoins <a class="yt-timestamp" data-t="01:25:55">[01:25:55]</a>. An example is using DeFi protocols to generate yield from stored coins to continuously pay for data storage, creating "forever living" data <a class="yt-timestamp" data-t="01:26:30">[01:26:30]</a>.
*   **User Experience**: Instead of requiring a separate blockchain and token, Walrus using Sui allows users to leverage existing assets (e.g., USDC) and DeFi protocols for seamless storage payments <a class="yt-timestamp" data-t="01:32:08">[01:32:08]</a>.

## Mistin Labs' Broader Vision

The overall vision of Mistin Labs extends beyond just Walrus Protocol. It aims to replace all components of the centralized cloud services stack with [[decentralized_exchanges_and_liquidity_protocols | decentralized]] alternatives <a class="yt-timestamp" data-t="01:27:44">[01:27:44]</a>. Sui handles the accounting layer, and Walrus provides the [[decentralized_exchanges_and_liquidity_protocols | decentralized]] cloud storage <a class="yt-timestamp" data-t="01:28:02">[01:28:02]</a>. The goal is to provide developers with all the necessary components to build rich, [[decentralized_exchanges_and_liquidity_protocols | decentralized]] applications as easily as building centralized ones on platforms like Amazon Web Services or Google Cloud <a class="yt-timestamp" data-t="01:28:29">[01:28:29]</a>.

This vision promotes a better future by reducing the power of intermediaries and technological gatekeepers <a class="yt-timestamp" data-t="01:29:10">[01:29:10]</a>. It advocates for neutral technology that does not allow a handful of powerful entities to control interactions, data, or financial transactions, fostering a more solid foundation for a technological culture <a class="yt-timestamp" data-t="01:30:16">[01:30:16]</a>.

## [[Decentralization vs centralization in crypto platforms | Decentralization vs. Practicality]]

George Nezes views [[decentralization_vs_centralization_in_crypto_platforms | decentralization]] as a security property of a system, preventing bad things from happening due to excessive central control (e.g., stopping access, perverting rules, compulsion by states) <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>. He believes a system needs "enough" [[decentralization_vs_centralization_in_crypto_platforms | decentralization]] to avoid these issues, with a good margin <a class="yt-timestamp" data-t="01:12:37">[01:12:37]</a>. However, once that state is reached, there isn't a significant advantage in continued [[decentralization_vs_centralization_in_crypto_platforms | decentralization]] <a class="yt-timestamp" data-t="01:13:13">[01:13:13]</a>.

A "pragmatic view" suggests that around 100 entities partaking in a business (e.g., shoe-making, or validator nodes) is often sufficient to ensure healthy competition and prevent cartel-like behavior, though this is an empirical observation rather than a timeless law <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>. This implies a middle-ground approach between extreme centralization and extreme [[decentralization_vs_centralization_in_crypto_platforms | decentralization]] <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

For projects, building on an existing modern [[blockchain_scalability_and_polkadot | blockchain]] like Sui is now often preferable to launching a new Layer 1, as existing L1s offer excellent, cheap, and fast infrastructure with expert teams in distributed systems, security, and cryptography <a class="yt-timestamp" data-t="01:08:42">[01:08:42]</a>.