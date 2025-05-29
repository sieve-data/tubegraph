---
title: Ethereums Pectra upgrade details
videoId: KgDlTfKM8DA
---

From: [[bankless]] <br/> 

The Pectra upgrade, [[ethereum_pectra_upgrade_and_its_implications | Ethereum]]'s 19th hard fork, went live on mainnet without issue <a class="yt-timestamp" data-t="01:42:04">[01:42:04]</a>. It was [[ethereum_pectra_upgrade_and_its_implications | Ethereum]]'s largest hard fork based on the sheer number of Ethereum Improvement Proposals (EIPs) included <a class="yt-timestamp" data-t="01:50:52">[01:50:52]</a>.

### Key EIPs in Pectra

Pectra introduced several EIPs, with three considered flagship features:

*   **EIP 7691: Increased Blob Target** <a class="yt-timestamp" data-t="02:22:30">[02:22:30]</a>
    *   This EIP doubled the target capacity for blobs from three to six per block, with a maximum of nine blobs <a class="yt-timestamp" data-t="02:52:05">[02:52:05]</a>.
    *   Blobs serve as a "fast lane" for Layer 2 (L2) transactions, making L2 space more expensive if there are more than three blobs and less expensive if there are fewer <a class="yt-timestamp" data-t="02:52:05">[02:52:05]</a>.
    *   The increase allows L2s to consume more Layer 1 (L1) blob space, facilitating faster operations and supporting a higher aggregate number of transactions across the [[Ethereums rollupcentric roadmap and L2 differentiation | Ethereum Layer 2 economy]] <a class="yt-timestamp" data-t="02:52:05">[02:52:05]</a>. This effectively doubles the available [[Ethereums rollupcentric roadmap and L2 differentiation | blobspace]] <a class="yt-timestamp" data-t="02:52:05">[02:52:05]</a>.

*   **EIP 7251: Max Effective Balance** <a class="yt-timestamp" data-t="02:30:57">[02:30:57]</a>
    *   Previously, [[Ethereums ZK upgrades | ETH]] stakers could only stake in explicit 32 [[Ethereums ZK upgrades | ETH]] increments <a class="yt-timestamp" data-t="02:35:42">[02:35:42]</a>.
    *   With this EIP, stakers can now stake anywhere between 32 and 48 [[Ethereums ZK upgrades | ETH]] <a class="yt-timestamp" data-t="02:39:05">[02:39:05]</a>.
    *   This enables consolidation of multiple validator instances (e.g., 10 validators on one machine) into fewer, more efficient ones, significantly reducing the messaging bandwidth overhead required for the [[Ethereums ZK upgrades | Ethereum]] validator network <a class="yt-timestamp" data-t="02:40:48">[02:40:48]</a>. The validator count is expected to decrease, freeing up bandwidth <a class="yt-timestamp" data-t="02:40:48">[02:40:48]</a>.

*   **EIP 7702: Account Abstraction Light** <a class="yt-timestamp" data-t="02:43:56">[02:43:56]</a>
    *   This EIP allows Externally Owned Addresses (EOAs) to temporarily gain smart contract properties during a transaction and revert back to an EOA afterward <a class="yt-timestamp" data-t="02:55:58">[02:55:58]</a>.
    *   It enables batch transactions, allowing multiple transactions to be executed atomically and removing the need for repeated "approve" pop-ups, significantly improving user experience <a class="yt-timestamp" data-t="02:44:06">[02:44:06]</a>.
    *   Applications can now sponsor transactions for users, and users can pay for gas in any token (e.g., USDC instead of [[Ethereums ZK upgrades | ETH]]) <a class="yt-timestamp" data-t="02:49:50">[02:49:50]</a>.
    *   This feature is expected to reduce wallet sprawl and offer benefits like native social recovery and support for session keys, similar to smart contract wallets <a class="yt-timestamp" data-t="02:51:30">[02:51:30]</a>.

### Strategic Priorities and Future Outlook

While Pectra improved user experience and doubled blob size, it did not include explicit Layer 1 throughput increases <a class="yt-timestamp" data-t="02:58:50">[02:58:50]</a>. The current simplified roadmap for [[Ethereums roadmap and priorities | Ethereum]] focuses on scaling Layer 1, scaling blobs, and improving user experience <a class="yt-timestamp" data-t="02:58:50">[02:58:50]</a>.

The next [[ethereums_roadmap_and_upgrades | Ethereum upgrade]], Fusaka, targeted for the end of the year, will introduce "pure DAS," a 10x increase in blob space <a class="yt-timestamp" data-t="02:39:50">[02:39:50]</a>. This indicates a continued prioritization of blob space over Layer 1 block space, a point of contention for some in the community who believe Layer 1 scaling should be emphasized more <a class="yt-timestamp" data-t="03:37:37">[03:37:37]</a>.

Validators can vote to increase the Layer 1 gas limit, which could increase block size (e.g., from 36 million to 60 million gas limit) <a class="yt-timestamp" data-t="03:15:37">[03:15:37]</a>. However, there is also a call for reducing Layer 1 block times (from 12 to 8 seconds) through an EIP, which would lead to faster trading speeds, less MEV, and a more efficient DeFi <a class="yt-timestamp" data-t="03:33:05">[03:33:05]</a>. This is seen as crucial for attracting traditional finance <a class="yt-timestamp" data-t="03:37:37">[03:37:37]</a>.

Layer 1 scaling and block time reduction are currently slated for the hard fork after Fusaka, possibly named "Clamsterdam" <a class="yt-timestamp" data-t="03:14:49">[03:14:49]</a>. Despite the debate on priorities, [[Ethereums strategic pivot and future potential | Ethereum]] is also working on Layer 2 interoperability standards to enhance cross-chain composability alongside increased scaling <a class="yt-timestamp" data-t="03:41:45">[03:41:45]</a>.