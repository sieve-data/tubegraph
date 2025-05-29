---
title: Use cases and earning yield with xDollar
videoId: tIjZzwCB-vo
---

From: [[goingonchain]] <br/> 

[[introduction_to_xdollar_protocol | xDollar]] is a lending protocol that enables users to borrow stablecoins <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It is a crypto-backed protocol, similar to Dai <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. [[features_of_xdollar_v1_and_v2 | xDollar V1]] launched on Avalanche, Polygon, and Arbitrum, while [[features_of_xdollar_v1_and_v2 | xDollar V2]] launched on Ethereum and is expanding to other chains <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Borrowing Stablecoins

xDollar allows users to borrow stablecoins like xUSD (V1) or xIM (V2) at a low collateral ratio and zero percent interest <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

### Key Features for Borrowing
*   **Low Collateral Ratio**: The collateral ratio is 110% <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. For comparison, borrowing $500 worth of Dai typically requires $1000 worth of ETH (200% collateral ratio) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Zero Percent Interest**: Borrowing stablecoins incurs zero interest <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **One-Time Fixed Fee**: There is a one-time fixed fee for borrowing <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This makes it more suitable for long-term loans rather than short-term ones <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Multi-Collateral**: Users can use various assets like MATIC, AVAX, or Ethereum as collateral <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Multi-Chain Capabilities**: [[crosschain_capabilities_and_future_expansions_for_xdollar | xDollar aims to be multi-chain]], allowing for cheaper fees on networks like Polygon <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Borrowing Process Example
If xDollar V2 supports Polygon, users with MATIC can use it to borrow xIM, swap xIM for USDC, and use it to buy other assets <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This strategy is best for long-term borrowing due to the one-time fee <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Earning Yield with xDollar

xDollar offers several ways to [[earning_yield_on_hundred_finance | earn yield]] and participate in the protocol.

### 1. Supplying to the Stability Pool (XPool)
Users can provide xIM into the stability pool <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Mechanism**: When borrowers are liquidated due to low collateral ratios, the protocol uses xIM from this pool to buy the liquidated assets <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Earning**: This allows users to acquire assets like MATIC at a discount and [[earning_yield_on_hundred_finance | earn more ETH]] and SPACE tokens (the protocol token) <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### 2. Staking SPACE Tokens (XStake)
Users can stake SPACE, the protocol token for [[features_of_xdollar_v1_and_v2 | xDollar V2]] (V1 used XTO) <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Mechanism**: Staking SPACE yields xSPACE, which is a governance token <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Earning**: With xSPACE, users can participate in governance votes and [[earning_yield_on_hundred_finance | earn a cut of the protocol's revenue]] <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Users can choose the lock-up period, with longer lock-ups yielding more xSPACE <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### 3. Yield Farming (XFarm)
Users can [[yield_farming_and_growing_your_crypto | farm SPACE]] by staking their xIM 3 Curve LP tokens <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This is done via Curve <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## Advanced Features: Liquidation and Redemption

### Liquidation (Risky Troll)
*   **Mechanism**: Users can liquidate someone else's position if their collateral ratio falls too low (e.g., close to 110%) <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Earning**: By paying xUSD, the liquidator receives the collateral at a discount <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Redemption
*   **Mechanism**: This feature allows users to participate in arbitrage events <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. For example, if xUSD de-pegs to $0.90, users can come to the protocol with xUSD, which is valued at $1.00 for redemption, allowing for profit <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Note**: Redemption is not equivalent to paying off a loan <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. This is often carried out by bots, but users can also perform this arbitrage <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

xDollar offers various ways to interact with the protocol, from borrowing [[earning_interest_on_stablecoins | stablecoins]] with low collateral to [[earning_yield_on_hundred_finance | earning yield]] through stability pools, staking, and [[yield_farming_and_growing_your_crypto | yield farming]] <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.