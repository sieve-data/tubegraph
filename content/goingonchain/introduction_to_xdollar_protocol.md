---
title: Introduction to xDollar protocol
videoId: tIjZzwCB-vo
---

From: [[goingonchain]] <br/> 

xDollar is a lending protocol that enables users to borrow [[usdb_stablecoin_mechanism | stablecoins]] at a low collateral ratio with zero percent interest <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Core Characteristics
xDollar is designed to be multi-chain and multi-collateral, allowing users to borrow [[usdb_stablecoin_mechanism | stablecoins]] using assets like MATIC, Avalanche, or Ethereum as collateral <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

Key features include:
*   **Low Collateral Ratio** A minimum collateral ratio of 110% <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Zero Percent Interest** Borrowers pay zero interest <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **One-Time Fixed Fee** A one-time fixed fee is applied to loans <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This makes it more suitable for long-term loans rather than short-term ones <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Cheap Fees** If deployed on Polygon, it offers low transaction fees <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Type of Stablecoin Protocol
To understand xDollar, it's important to know the different types of [[usdb_stablecoin_mechanism | stablecoins]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>:
1.  **Fiat-Backed:** Such as USDC, where each unit is backed by one USD held by a company like Circle <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
2.  **Algorithmic:** For example, Terra UST, where the supply of UST is backed by the supply of Luna <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
3.  **Crypto-Backed:** Like DAI, where borrowing a stablecoin requires over-collateralization with [[introduction_to_cryptocurrency | crypto]] assets (e.g., $1000 worth of ETH for $500 worth of DAI, a 200% collateral ratio) <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

xDollar belongs to the crypto-backed category <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## xDollar V1 and V2
[[features_of_xdollar_v1_and_v2 | Features of xDollar V1 and V2]] include distinct names for stablecoins and protocol tokens, as well as different chain support:

| Feature           | xDollar V1             | xDollar V2                          |
| :---------------- | :--------------------- | :---------------------------------- |
| **Stablecoin**    | xUSD <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>           | XIM (xDollar Inter-Money) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> |
| **Protocol Token**| XTO <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>            | SPACE <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>               |
| **Chains**        | Polygon, Avalanche, Arbitrum <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a> | Ethereum (currently), working to onboard more Layer 2 solutions and protocols <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>, <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a> |

xDollar V1 is currently undergoing a migration <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Team
The xDollar team is anonymous, but they have strong backing from figures like V-Fect (creator of V-Fad 2) and V-Fad, who are well-known in the DeFi and yield farming communities <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Key Platform Features (UI Sections)
The xDollar V2 platform features several sections:
*   **X-Home:** Displays the platform's dashboard, protocol earnings, and collateral ratio (CR) <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **X-Bank:** Where users borrow XIM (stablecoin) using ETH, or MATIC when integrated <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **X-Pool (Stability Pool):** Users supply XIM to this pool to earn more ETH and SPACE. The protocol uses the XIM to buy liquidated assets, allowing users to acquire collateral at a discount <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **X-Stake:** Users stake their SPACE protocol tokens to receive xSPACE, a governance token that allows participation in governance voting and earning a share of the protocol's revenue <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>, <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The longer the lock-up period, the more xSPACE is received <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **X-Farm:** Users can farm SPACE by staking XIM 3 Curve LP tokens via Curve <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Other Protocol Features
*   **Liquidation (Risky Trove):** Allows users to liquidate another user's position if their collateral ratio falls too low (e.g., close to 110%). The liquidator pays xUSD and receives the collateral at a discount <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Redemption:** Users can take part in arbitrage events. If xUSD de-pegs to 90 cents, users can use xUSD (valued at one dollar by the protocol) to redeem collateral from other positions. This is typically carried out by bots but is also open to users <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Redemption is not the same as repaying a loan <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

For more details on borrowing, earning yield, and strategies, see [[use_cases_and_earning_yield_with_xdollar | Use Cases and Earning Yield with xDollar]]. For information on multi-chain ambitions, see [[crosschain_capabilities_and_future_expansions_for_xdollar | Crosschain Capabilities and Future Expansions for xDollar]].