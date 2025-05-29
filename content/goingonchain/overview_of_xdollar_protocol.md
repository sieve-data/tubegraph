---
title: Overview of xDollar Protocol
videoId: tIjZzwCB-vo
---

From: [[goingonchain]] <br/> 

xDollar is a lending protocol that enables users to borrow stablecoins with a low collateral ratio and at a zero percent interest rate <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The protocol is designed to be [[multicollateral_and_multichain_features_of_xdollar | multi-chain and multi-collateral]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Types of Stablecoins and xDollar's Category

To understand xDollar, it's helpful to know the different types of stablecoins <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>:
*   **Fiat-backed**: Like [[usdc_commitment_and_reward_distribution | USDC]], where each token is backed by one USD controlled by a company like Circle <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   **Algorithmic**: Such as Terra UST, where the supply of UST is backed by the supply of Luna <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Crypto-backed**: For example, Dai, where borrowing $500 worth of Dai requires $1,000 worth of ETH, implying a 200% collateral ratio <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

xDollar falls into the crypto-backed category <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Key Features of xDollar

xDollar aims to be multi-chain and multi-collateral, allowing users to use assets like MATIC, Avalanche, or Ethereum to borrow stablecoins <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Low Collateral Ratio**: It features a low collateral ratio of 110% <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This is a significant advantage for DeFi traders <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Zero Percent Interest**: Borrowing incurs a 0% interest rate <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **One-Time Fixed Fee**: There is a one-time fixed fee for borrowing <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This makes it more suitable for long-term loans rather than short-term ones <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## Team and Backing

The xDollar team is anonymous, but they have strong backing, including Vfec, known for creating Vfat Tools <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## [[xdollar_v1_and_v2_differences | xDollar v1 and v2 Differences]]

With the launch of v2, some naming conventions and supported chains have changed <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>:
*   **Stablecoin Name**: In v1, the stablecoin was called xUSD; in v2, it's called xIM (xDollar Inter-Money) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Protocol Token Name**: In v1, the protocol token was XTO; in v2, it's called SPACE <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Supported Chains**: v1 works with Polygon, Avalanche, and Arbitrum <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. v2 currently works with Ethereum and is working to onboard more Layer 2 solutions <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. xDollar v1 is currently undergoing a migration <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Use Cases and Features

### Borrowing Stablecoins (xBank)
Users can borrow the xIM stablecoin using ETH, and eventually MATIC when v2 connects with Polygon <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. This allows users to obtain stablecoins to swap for other assets without selling their underlying collateral <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### [[earning_yield_with_xdollar | Earning Yield with xDollar]] (xPool - Stability Pool)
Users can provide xIM into a stability pool to earn rewards in the form of liquidated assets (e.g., MATIC) and SPACE tokens <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. When borrowers' positions are liquidated, the xIM from this pool is used to buy the liquidated assets at a discount, which is then distributed to the pool providers <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Staking SPACE (xStake)
Staking the SPACE protocol token allows users to earn xSPACE, which is a governance token <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. With xSPACE, users can participate in governance votes and earn a share of the protocol's revenue <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. The longer the SPACE is locked up, the more xSPACE is received <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Farming (xFarm)
Users can farm SPACE tokens by staking their xIM 3 Curve LP tokens via Curve <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Liquidation (Risky Trove)
The liquidation mechanism allows users to liquidate another user's position if its collateral ratio falls low enough (close to 110%) <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. The liquidator pays xUSD/xIM and receives the collateral at a discount <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Redemption
Redemption is an arbitrage mechanism for users to engage in when the xUSD/xIM stablecoin depegs <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. If xUSD depegs to $0.90, users can provide xUSD (valued at $1) and receive an equivalent amount of collateral <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This function is typically carried out by bots but is also accessible to users <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. It's important to note that redemption is not the same as paying off a loan <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Current Status and Resources

Currently, xDollar v2 is deployed only on Ethereum <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. The team is working towards deployment on other chains <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

For more information, users can visit the xDollar Twitter account (@xdollarfi) or join their Discord server <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.