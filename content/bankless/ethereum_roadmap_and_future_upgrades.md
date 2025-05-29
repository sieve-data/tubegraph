---
title: Ethereum Roadmap and Future Upgrades
videoId: WpjcPPrrN2E
---

From: [[bankless]] <br/> 

The [[Ethereum roadmap | Ethereum roadmap]] is a continually evolving process, shaped by debate, deliberation, and rough consensus within the Ethereum All Core Devs (ACD) calls, where priorities are established and Ethereum Improvement Proposals (EIPs) are considered for inclusion or discarded <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a> <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. Tim Beiko, a coordinator of these calls, plays a central role in managing conversations and priorities across Ethereum's various components <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.

## Core Development Philosophy

The paramount priority in [[Ethereum development priorities | Ethereum development priorities]] is security <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>. Ethereum's robust approach to security is a key differentiator, ensuring the chain has never gone down <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. This focus dictates other priorities, as features are often constrained by security properties <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>. Unlike traditional finance, Ethereum lacks centralized third parties to revert transactions or fix issues, necessitating a highly secure protocol <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>. Historical events, such as the Bitcoin inflation bug and the Ethereum DAO hack, underscore the difficulty and contentious nature of social interventions, making on-chain security critical <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>.

The slow pace of [[Ethereum upgrades for 2025 | Ethereum upgrades]] is primarily due to the rigorous testing cycles required for security <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>. Many proposed EIPs are rejected or take years to iterate on before being deemed safe for deployment <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>. The aim is to remove "process and operations" related slowness, but research and development (R&D) difficulties, like those encountered during the Merge, are an inherent cost of developing complex, secure systems <a class="yt-timestamp" data-t="01:04:15">[01:04:15]</a>.

## Hard Fork Naming Convention

Following the Merge, Ethereum's hard forks combine names from two different sources: the consensus layer uses star names, and the execution layer uses Devcon city names <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. For example:
*   **Pectra** is a portmanteau of Prague (execution layer) and Electra (consensus layer) <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.
*   **Fuzaka** combines Fulu and Osaka <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.
*   **Glamsterdam** combines a "gar" name with Amsterdam, the city of the first Devcon <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

## Pectra Hard Fork (Expected May 2024)

Pectra is the next major hard fork, expected around May 2024, assuming smooth testing <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a> <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a> <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a> <a class="yt-timestamp" data-t="00:42:47">[00:42:47]</a>. Its key priorities are:

### Validator Consolidation (MaxEB)
Pectra introduces the ability for validators to increase their maximum ETH balance from 32 ETH chunks up to 2048 ETH <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a> <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. This feature offers two main benefits:
*   **Reduced Bandwidth Usage**: Large operators like Lido or Coinbase can consolidate many smaller 32 ETH validators into fewer, larger ones, significantly reducing the number of messages sent across the network. This frees up bandwidth for other scaling efforts like blobs <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a> <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a> <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.
*   **Compounding for Smaller Stakers**: Individual stakers with more than 32 ETH, but less than 2048 ETH, can now automatically compound their rewards, increasing their effective stake without running multiple validators <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a> <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.

### Increased Blob Count
Pectra will increase the average number of blobs per block from 3 to 6, with a maximum of 9 in worst-case scenarios <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. This doubling of blob space directly scales data availability for Layer 2s, leveraging the bandwidth savings from MaxEB <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a> <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. Blobs provide a cost-effective way for Layer 2s to store data temporarily, as they are deleted after a few weeks, unlike permanent call data <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

### EIP-7702 (Account Abstraction)
EIP-7702 is the first in-protocol implementation of account abstraction <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. This feature allows Externally Owned Accounts (EOAs, like MetaMask or Ledger wallets) to temporarily delegate smart contract functionality to a specific smart wallet <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a> <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. Users can choose and change these "plugins" over time, enabling features like auto-approvals or social recovery, blending the benefits of EOAs with smart contract wallets <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a> <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a> <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. This EIP has been in development since 2017-2018 <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a> and is a practical step towards improving user experience, though other account abstraction challenges like gasless transactions or private key changes remain outside its scope <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

### Pectra Timeline
Pectra is currently in its testnet phase. While initial testnets like Sepolia and Holesky encountered minor configuration issues, a new testnet, Goerli, launched on March 20th <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a> <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. The Pectra hard fork is scheduled to happen on Goerli on March 26th <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>. Staking pools and other major operators will then have a few weeks to test their infrastructure, making a mainnet activation around May a "base case" scenario <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

## Fuzaka Hard Fork (Target 2025)

Fuzaka is the next major hard fork following Pectra, with a strong community desire to ship it by the end of 2025 <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a> <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. Its two main features, PIEDAS and EOF, have been in parallel development with Pectra for over a year <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. The scope for Fuzaka is expected to remain relatively small to ensure PIEDAS ships on time <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

### PIEDAS (Proposer-Builder Separation and Data Availability Sampling)
PIEDAS represents the next qualitative leap in data availability for Ethereum <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. Currently, every node stores all blob data, even though it's deleted after a few weeks <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. PIEDAS aims to transition to a model where each node only stores a *subset* of the data but uses cryptography to probabilistically verify that other nodes hold the complete data <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. This effectively offers a 10x increase in data availability for the same amount of bandwidth <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. The target for Fuzaka is to enable up to 48 blobs per block on average, a significant jump from Pectra's 6 <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a> <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. Vitalik Buterin expressed a desire for a Fuzaka testnet with 48 blob parameters to run "the day after Pectra goes live" <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.

### EOF (Ethereum Object Format)
EOF, or Ethereum Object Format, is a major overhaul of the Ethereum Virtual Machine (EVM) <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a> <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. It's often analogized as upgrading the EVM from a "1950s computer" to a "1990s computer" <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>. This upgrade aims to:
*   **Separate Code and Data**: Improve tooling and analysis by clearly distinguishing code from data within smart contracts <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
*   **Introduce New Opcodes**: Add specific opcodes to simplify compiler development and programming languages built on the EVM <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.
*   **Remove Problematic Features**: Allow for the banning of certain undesirable features in new, opt-in EOF contracts, improving long-term security and aligning with future roadmap items <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.

EOF primarily improves the developer experience for those writing compilers and programming languages that interact with the EVM <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.

## Glamsterdam Hard Fork

Glamsterdam is a placeholder name for the hard fork after Fuzaka, with its scope yet to be finalized <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a> <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. The goal is to improve the parallelization of hard fork planning and implementation. This means finalizing Glamsterdam's scope shortly after Pectra goes live, allowing teams to begin work on it while Fuzaka is being shipped <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a> <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.

## Scaling the Layer 1 (Execution Layer)

Scaling the execution layer (Layer 1) involves increasing gas throughput or adjusting block times <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>. While the gas limit is a coarse lever for this, understanding the multivariate inputs (state growth, history growth, opcode repricing) is crucial <a class="yt-timestamp" data-t="01:09:02">[01:09:02]</a> <a class="yt-timestamp" data-t="01:09:12">[01:09:12]</a>. There is renewed interest and better understanding of these bottlenecks within the core dev community <a class="yt-timestamp" data-t="01:09:13">[01:09:13]</a>. Efforts include repricing opcodes to make certain operations cheaper and optimizing block verification due to MEV (Maximal Extractable Value) dynamics, where builders wait until the last second to build blocks <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a> <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

## Interoperability and Layer 2 Fragmentation

While core developers acknowledge the fragmentation of Layer 2s, protocol-level solutions for interoperability are complex and years away <a class="yt-timestamp" data-t="01:13:42">[01:13:42]</a> <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>. Ideas like "native rollups," which would involve common pre-compiles on Layer 1 that rollups use to interoperate better, are being explored for the long term <a class="yt-timestamp" data-t="01:14:07">[01:14:07]</a>. In the short term, the focus for interoperability remains on application-level and wallet-level standardization <a class="yt-timestamp" data-t="01:15:51">[01:15:51]</a>.

## Misconceptions

A common misconception is that features are "delayed" before an official release date has even been set <a class="yt-timestamp" data-t="01:06:56">[01:06:56]</a>. The challenge lies in communicating the inherent uncertainty of R&D timelines to the community <a class="yt-timestamp" data-t="01:07:44">[01:07:44]</a>.

## Summer of Protocols

The "Summer of Protocols" initiative aims to develop a better understanding of protocols, an analogy for how Ethereum operates <a class="yt-timestamp" data-t="01:16:37">[01:16:37]</a>. This program funds researchers, and in 2025, it focuses on funding teachers and educators to organize and condense existing knowledge about protocols into accessible formats like classes and books <a class="yt-timestamp" data-t="01:17:55">[01:17:55]</a>. The goal is to provide a unified explanation of how protocols work, drawing parallels from various domains beyond just blockchain <a class="yt-timestamp" data-t="01:18:01">[01:18:01]</a>.