---
title: Ethereum Pectra upgrade and its implications
videoId: MqrlFj_5LtY
---

From: [[bankless]] <br/> 

The [[Ethereums Pectra upgrade details | Ethereum Pectra upgrade]] went live on the morning of May 7th <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>. This upgrade introduces several new Ethereum Improvement Proposals (EIPs) aiming to enhance user experience and network scalability <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>.

## Key EIPs in Pectra

The Pectra upgrade includes several EIPs, with three significant ones highlighted:

*   **EIP 7702**: This EIP enables smart contract functionality for all Externally Owned Accounts (EOAs), essentially making them smart contract enabled <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>. This allows 0x addresses to run one-off contract code, execute it, and then revert to being a vanilla EOA, enabling account abstraction abilities <a class="yt-timestamp" data-t="01:01:46">[01:01:46]</a>.
*   **EIP 7691**: This proposal expands the blob capacity, doubling it from a target of 3 to 6 blobs <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>.
*   **EIP 7251**: This EIP adjusts the maximum effective balance for validators, allowing them to stake a range of ETH between 32 ETH and 2048 ETH, rather than a rigid 32 ETH <a class="yt-timestamp" data-t="01:01:23">[01:01:23]</a>.

## User Experience (UX) Enhancements from EIP 7702

EIP 7702 is considered a significant UX upgrade for all wallets <a class="yt-timestamp" data-t="01:01:37">[01:01:37]</a>. Key benefits include:

*   **Batch Transactions**: The ability to combine multiple transactions, including the "approve" popup, into a single one-click experience <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>. This aims to remove failed transaction issues and improve overall user flow <a class="yt-timestamp" data-t="01:02:10">[01:02:10]</a>.
*   **Sponsored Gas and Token-Denominated Gas**: Layer 1 applications can now pay for their users' gas fees, and gas fees can be paid using various tokens, primarily stablecoins <a class="yt-timestamp" data-t="01:02:13">[01:02:13]</a>. These are seen as major UX improvements for Layer 1 usage of [[Ethereums roadmap and future potential | Ethereum]] <a class="yt-timestamp" data-t="01:02:28">[01:02:28]</a>.

## Blob Capacity Expansion and Scaling Debates

EIP 7691 doubles blob capacity. While a 2x increase is notable, the raw numbers are still considered small compared to other data availability (DA) platforms like Celestia, which can push significantly more data <a class="yt-timestamp" data-t="01:05:08">[01:05:08]</a>. This highlights a broader debate about [[Ethereums roadmap and priorities | Ethereum's goals]] and its ability to keep up with the increasing demand for data throughput and bandwidth in the industry <a class="yt-timestamp" data-t="01:06:35">[01:06:35]</a>.

The increase in blob capacity is partly enabled by the bandwidth reduction achieved from EIP 7251, which allows for fewer validators and less gossip overhead <a class="yt-timestamp" data-t="01:08:34">[01:08:34]</a>.

## Validator Staking and Network Efficiency

EIP 7251, by allowing validators to consolidate their stakes up to 2048 ETH, indirectly contributes to network performance by reducing gossip overhead and making the network leaner <a class="yt-timestamp" data-t="01:07:54">[01:07:54]</a>. This reduction in bandwidth overhead frees up resources, allowing for the comfortable scaling of more blobs <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a>. This consolidation will not be instantaneous but is expected to incrementally reduce bandwidth overhead over time <a class="yt-timestamp" data-t="01:09:12">[01:09:12]</a>.

## Overall Assessment and Future Direction

### Operational Challenges and Lessons Learned
Pectra took a long time to ship and faced delays due to internal disagreements <a class="yt-timestamp" data-t="01:02:58">[01:02:58]</a>. This experience has led to lessons being learned for future upgrades, such as the upcoming Fuzion (Fossaka) upgrade, where the focus is now on faster shipping and a more targeted approach <a class="yt-timestamp" data-t="01:03:39">[01:03:39]</a>.

### [[Ethereums strategic pivot and its implications | Ethereum's Strategic Pivot]]
The current [[Ethereums roadmap and priorities | Ethereum roadmap]] emphasizes a three-pronged approach: scaling the L1, scaling blobs, and improving UX <a class="yt-timestamp" data-t="01:04:18">[01:04:18]</a>. Pectra addresses two of these to a meaningful degree: improving UX (EIP 7702) and scaling blobs (EIP 7691) <a class="yt-timestamp" data-t="01:04:22">[01:04:22]</a>.

A core debate for [[Ethereums roadmap and future potential | Ethereum]]'s future is whether its most valuable market lies in "premium execution" (fast, low-latency transactions) or "premium Data Availability" (DA) <a class="yt-timestamp" data-t="01:11:14">[01:11:14]</a>. The argument leans towards premium execution, suggesting it's a more valuable and "stickier" market for [[Ethereums strategic pivot and future potential | Ethereum]] to own <a class="yt-timestamp" data-t="01:11:23">[01:11:23]</a>.

There's a desire to lower slot times and have faster blocks on [[Ethereum pivot and ETH revival | Ethereum]]'s L1 to support trading and attract Wall Street, which prioritizes precise execution and wants to avoid MEV extraction <a class="yt-timestamp" data-t="01:12:20">[01:12:20]</a>. While challenging to implement while preserving [[Ethereums strategic pivot and its implications | Ethereum's level of decentralization]], this would position [[Ethereums roadmap and future potential | Ethereum]] as a "decentralized NASDAQ" <a class="yt-timestamp" data-t="01:13:25">[01:13:25]</a>.

Despite other chains being faster, [[Ethereums roadmap and future potential | Ethereum]]'s properties of credible neutrality, strong MEV infrastructure, and decentralization make it attractive for high-value assets like on-chain treasuries <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>. This positions [[Ethereum pivot and ETH revival | Ethereum]] to capitalize on a significant market segment, even if it's not the fastest chain <a class="yt-timestamp" data-t="01:16:21">[01:16:21]</a>.

The discussion also briefly touches upon the potential for [[Ethereums ZK upgrades | Bitcoin L2s]] to learn from [[Ethereums roadmap and future potential | Ethereum]]'s multi-chain architecture journey, although differences in user base and technical constraints suggest different outcomes <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>.