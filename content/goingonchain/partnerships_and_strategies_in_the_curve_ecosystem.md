---
title: Partnerships and strategies in the Curve ecosystem
videoId: nc8Qi8UTT7Y
---

From: [[goingonchain]] <br/> 

The **4-pool** is a liquidity pool consisting of four assets: UST, FLUX, USDT, and USDC <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. These pools are currently available on Fantom (FTM) and Arbitrum (ARB) <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, with an Ethereum pool expected to arrive soon <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The 4-pool is designed to elevate FLUX and UST within the Ethereum DeFi ecosystem <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Understanding Curve's Importance

To understand the impact of the 4-pool, it is essential to first understand [[Curve and its algorithm | Curve]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. [[Curve and its algorithm | Curve]] is an Automated Market Maker (AMM) that utilizes a special algorithm <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Unlike typical AMMs that use an `x * y = k` formula (popularized by Uniswap v2), which leads to high slippage for stablecoin swaps <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, [[Curve and its algorithm | Curve]] employs a hybrid approach <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

[[Curve and its algorithm | Curve]] uses two formulas:
*   `x + y = k` (constant sum formula) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>: This formula is applied when the liquidity pool is balanced, resulting in minimal slippage <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   `x * y = k` (constant product formula) <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>: This formula is used when the pool becomes imbalanced, resembling traditional AMM behavior <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

This hybrid approach allows [[Curve and its algorithm | Curve]] to offer significantly lower slippage for large stablecoin swaps compared to other DEXes like SushiSwap <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, making it a preferred platform for large traders ("whales") <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

The most popular pool on [[Curve and its algorithm | Curve]] is the 3-pool (DAI, USDT, USDC), boasting a Total Value Locked (TVL) of 3.3 billion <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. For a pool to succeed, it needs both high liquidity and attractive rewards <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## The Curve War

The term "Curve War" refers to the competition among protocols to control CRV emissions and boost their own pools <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### CRV Tokenomics and veCRV

CRV is the native token of [[Curve and its algorithm | Curve]] <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. As a [[Curve liquidity pools and rewards | liquidity provider]] on [[Curve and its algorithm | Curve]], users earn trading fees and CRV rewards <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Users can lock up their CRV tokens to receive `veCRV` (vote-escrowed CRV) <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. `veCRV` holders can vote on which pools receive boosted CRV rewards <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This creates a cycle where [[Curve liquidity pools and rewards | liquidity providers]] lock CRV to boost their own pools, earning more CRV <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. CRV can be locked for 1 to 4 years, with conversion ratios from 0.25 `veCRV` per CRV for one year to 1 `veCRV` per CRV for four years <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

### Role of Convex Finance

For a stablecoin protocol to establish significant liquidity in the Ethereum DeFi space, it typically needs to set up a [[Curve and its algorithm | Curve]] pool and then either buy or bribe CRV holders to lock up their CRV and boost rewards for their pool <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

[[Convex Finance and its role in Curve ecosystem | Convex Finance]] plays a pivotal role in the Curve War because it is currently the largest holder of `veCRV` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. [[Convex Finance and its role in Curve ecosystem | Convex Finance]] allows CRV holders to earn boosted rewards <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   CRV holders can convert CRV to `cvxCRV` (a one-way conversion) <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   `cvxCRV` can be staked to earn CRV rewards, as [[Convex Finance and its role in Curve ecosystem | Convex Finance]] takes the underlying CRV, locks it, and uses it to vote for gauges, splitting the rewards with its users <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Users can also lock `CVX` (Convex's native token) for 16 weeks to receive `vlCVX` (vote-locked CVX), which grants more rewards and governance voting rights <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

Protocols actively bribe `vlCVX` holders to vote for their specific pools. Votium is a platform that facilitates these bribes <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. For example, FLUX and UST have been observed paying approximately 56 cents per `vlCVX` to incentivize votes for their pools <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. This intense competition for CRV emissions is the essence of the Curve War <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## The 4-Pool Strategy and Partnerships

The 4-pool represents a strategic partnership between UST, FLUX, USDC, and USDT <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Its primary goal is to replace DAI in the prominent stablecoin pool, effectively removing DAI from the equation <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

To ensure the 4-pool's success on [[Curve and its algorithm | Curve]], significant rewards are necessary <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. Terra and Frax have been preparing for this by becoming two of the largest protocol holders of CVX <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. They also offer substantial volume incentives to `vlCVX` holders <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This collective effort aims to make the 4-pool the most liquid and utilized stablecoin pool across chains <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

The partnerships supporting the 4-pool are extensive, including Terra, Frax, Redacted, BadgerDAO, OlympusDAO, and Tokemak <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This broad alliance allows them to exert significant influence on CVX governance to direct emissions towards the 4-pool <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

The strategic reasons behind the 4-pool initiative are multifaceted:
*   **Collaboration over Competition**: Instead of rivaling each other, protocols like UST and Frax are working together <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **UST as Collateral**: UST is positioned to become a collateralized asset for Frax <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Decentralized Stablecoin Dominance**: The partnership aims to drive out DAI, establishing FLUX and UST as the leading decentralized stablecoins, particularly within the Ethereum ecosystem where liquidity is highest <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Bitcoin Acquisition for TFL**: Terraform Labs (TFL) plans to acquire 10 billion USD worth of Bitcoin <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Since there isn't enough liquidity on the native Terra blockchain for such large purchases <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>, a deeply liquid 4-pool would enable efficient swaps of UST for USDT to facilitate these Bitcoin acquisitions <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.