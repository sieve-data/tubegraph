---
title: Ethereum Layer 2 scaling and future of Bitcoin Layer 2s
videoId: MqrlFj_5LtY
---

From: [[bankless]] <br/> 

## [[ethereums_layer_1_l1_and_layer_2_l2_scaling_strategies | Ethereum Layer 2 Scaling]] and the Pectra Upgrade

The Ethereum network continues to evolve with significant upgrades aimed at improving user experience and scaling capabilities. The Pectra upgrade, which went live on May 7th, 2024 <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>, introduced several key Ethereum Improvement Proposals (EIPs).

### Key EIPs in Pectra

*   **EIP 7702 (Account Abstraction for EOAs)**: This EIP enables all EOAs (Externally Owned Accounts) to function with smart contract capabilities for one-off contract code execution, reverting to a vanilla EOA afterwards <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>. This is considered a major UX upgrade, allowing for features like batch transactions and sponsor-paid token-denominated gas fees <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>. For example, users can consolidate a series of transactions, including approvals, into a single click, eliminating multiple pop-ups <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>. Layer 1 applications can also cover users' gas fees, or fees can be paid in stablecoins or other tokens <a class="yt-timestamp" data-t="01:02:13">[01:02:13]</a>.
*   **EIP 7691 (Blob Capacity Expansion)**: This EIP doubles the target blob capacity from 3 to 6 <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>. While this represents a meaningful percentage increase, the raw data capacity is still considered small when compared to other chains like Celestia or Avail <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. Current Ethereum data throughput is in kilobytes, whereas Celestia pushes megabytes per second <a class="yt-timestamp" data-t="01:05:30">[01:05:30]</a>.
*   **EIP 7251 (Max Effective Balance)**: This EIP allows validators to stake a range of ETH, from 32 ETH up to 2048 ETH, instead of a rigid 32 ETH <a class="yt-timestamp" data-t="01:02:23">[01:02:23]</a>. This change is expected to lead to a reduction in network gossip overhead, as fewer validators will need to communicate <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. The bandwidth saved from Max Effective Balance (Max EB) reduction translates into the increased blob count in the same hard fork <a class="yt-timestamp" data-t="01:08:17">[01:08:17]</a>.

### Strategic Priorities and Challenges for [[ethereum_scaling_and_strategic_pivot | Ethereum Scaling]]

The Pectra upgrade highlights Ethereum's focus on a three-pronged approach to scaling: scaling the L1, scaling blobs, and improving UX <a class="yt-timestamp" data-t="01:04:18">[01:04:18]</a>. EIPs 7702 and 7691 contribute significantly to the latter two points <a class="yt-timestamp" data-t="01:04:22">[01:04:22]</a>.

Despite these advancements, there are ongoing debates about the optimal [[scaling_ethereum_layer_1_and_layer_2_improvements | scaling strategies]]. Some argue that [[scaling_ethereum_layer_one | scaling Ethereum Layer One]] directly, for instance by reducing block times and increasing gas limits, could offer more immediate benefits than expanding blob capacity <a class="yt-timestamp" data-t="01:11:37">[01:11:37]</a>. This is because faster blocks would benefit trading and sophisticated MEV (Maximal Extractable Value) mitigation infrastructure, which is a strong advantage for Ethereum in attracting Wall Street interest <a class="yt-timestamp" data-t="01:12:35">[01:12:35]</a>.

Concerns persist about Ethereum's ability to keep pace with the demand for data throughput compared to modular chains like Celestia and Avail, which already offer significantly higher bandwidth <a class="yt-timestamp" data-t="01:06:08">[01:06:08]</a>. The choice between prioritizing premium execution (fast, secure transactions) and premium Data Availability (DA) is a strategic one <a class="yt-timestamp" data-t="01:11:18">[01:11:18]</a>. While Ethereum is seen as winning on premium execution, its DA capabilities are far behind competitors <a class="yt-timestamp" data-t="01:11:23">[01:11:23]</a>.

The development of Pectra itself was protracted and messy, serving as a learning experience for future upgrades like Purge (EIP-4844) <a class="yt-timestamp" data-t="01:02:58">[01:02:58]</a>. The community hopes to ship Purge faster, with a concentrated focus on its core purpose <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>.

The broader [[the_role_of_layer_1_and_layer_2_in_the_ethereum_ecosystem | role of layer 1 and layer 2 in the Ethereum ecosystem]] suggests that as [[developments_in_the_ethereum_layer_2_ecosystem | Layer 2s develop]], the L1 may become a credibly neutral, highly secure settlement layer for high-value, infrequent transactions, such as treasury movements, rather than a high-throughput trading environment <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>.

## The Future of Bitcoin Layer 2s

Bitcoin is embarking on its own journey into multi-chain architectures and Layer 2s <a class="yt-timestamp" data-t="01:16:33">[01:16:33]</a>. The experience of [[layer_1_and_layer_2_integration_in_ethereum | Ethereum's Layer 2 integration]] offers lessons, but it's important not to "overanalogize" between the two ecosystems <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>.

### Key Differences between Bitcoin and Ethereum L2s

*   **User Base and Desire**: Bitcoin's user base is perceived as fundamentally different, often consisting of asset holders rather than active blockchain users <a class="yt-timestamp" data-t="01:18:37">[01:18:37]</a>. While there's an overlap with Ordinals traders and memecoin enthusiasts on other chains like Solana, the core desire for Bitcoin L2s is often zero-to-one functionality (e.g., trustless DeFi capabilities for Bitcoin) that isn't possible on its L1 <a class="yt-timestamp" data-t="01:17:49">[01:17:49]</a>. Ethereum L2s, in contrast, often aim to make existing L1 activities faster and cheaper <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a>.
*   **Technical Constraints**: Bitcoin's L1 has significantly smaller block sizes and slower transaction times than Ethereum <a class="yt-timestamp" data-t="01:18:17">[01:18:17]</a>. It uses Proof-of-Work, and currently lacks native ZK verification capabilities, making the technical challenges for building Bitcoin L2s distinct <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>.

Given these fundamental differences, the market for Bitcoin L2s is expected to play out differently from Ethereum's. The primary goal for Bitcoin L2s is to provide functionalities that the Bitcoin L1 cannot, rather than merely optimizing existing ones <a class="yt-timestamp" data-t="01:19:48">[01:19:48]</a>. The market structure of permissionless development means that similar "fractals" of what was seen in Ethereum L2s might emerge, but with different incentives and outcomes <a class="yt-timestamp" data-t="01:16:55">[01:16:55]</a>.