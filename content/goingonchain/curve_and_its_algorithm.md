---
title: Curve and its algorithm
videoId: nc8Qi8UTT7Y
---

From: [[goingonchain]] <br/> 

Curve is an Automated Market Maker (AMM) that functions similarly to a decentralized exchange (DEX), like PancakeSwap or SushiSwap <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>. What makes Curve special is its unique algorithm <a class="yt-timestamp" data-t="00:45:45">[00:45:45]</a>.

## Curve's Hybrid Algorithm

Typical AMMs use the formula `x * y = k`, popularized by Uniswap v2 <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>. This formula works well for most assets, as it's based on supply and demand <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>. However, it is not ideal for stablecoins, especially for large orders, as it can result in high slippage <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>. For instance, on SushiSwap, a large stablecoin order of 500,000 USDT might only yield 487,000 USDC due to high slippage <a class="yt-timestamp" data-t="01:57:57">[01:57:57]</a>.

Curve solves this problem by using a hybrid approach with two formulas <a class="yt-timestamp" data-t="01:15:15">[01:15:15]</a>:
1.  `x + y = k` (constant sum formula) <a class="yt-timestamp" data-t="01:20:20">[01:20:20]</a>
2.  `x * y = k` (constant product formula) <a class="yt-timestamp" data-t="01:22:23">[01:22:23]</a>

### How the Hybrid Algorithm Works
*   **Balanced Pools:** When the [[curve_liquidity_pools_and_rewards | liquidity pool]] is balanced, the algorithm functions as `x + y = k` <a class="yt-timestamp" data-t="01:31:31">[01:31:31]</a>. This is represented by a "stable swap curve" that closely mirrors a constant sum line, allowing for minimal slippage <a class="yt-timestamp" data-t="01:25:25">[01:25:25]</a>.
*   **Imbalanced Pools:** If the [[curve_liquidity_pools_and_rewards | liquidity pool]] becomes imbalanced, the algorithm shifts to function as `x * y = k` <a class="yt-timestamp" data-t="01:43:43">[01:43:43]</a>. In this state, the curve resembles a constant product line <a class="yt-timestamp" data-t="01:51:51">[01:51:51]</a>.

This hybrid approach significantly reduces slippage for stablecoin swaps, making it attractive for large orders <a class="yt-timestamp" data-t="02:09:09">[02:09:09]</a>.

## Curve Pools and Rewards

Curve features various [[curve_liquidity_pools_and_rewards | liquidity pools]], with the most popular being the "3-pool" containing DAI, USDT, and USDC, boasting a Total Value Locked (TVL) of 3.3 billion <a class="yt-timestamp" data-t="02:20:20">[02:20:20]</a>. For a pool to be successful, it requires substantial liquidity and attractive rewards <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>.

[[curve_liquidity_pools_and_rewards | Liquidity providers]] on Curve earn trading fees and CRV rewards <a class="yt-timestamp" data-t="02:54:54">[02:54:54]</a>.

## CRV Token and veCRV

CRV is the native token for Curve <a class="yt-timestamp" data-t="02:47:47">[02:47:47]</a>. Users can lock up their CRV tokens to receive veCRV (Vote-Escrowed CRV) <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. The amount of veCRV received depends on the lock-up period, ranging from one to four years, with a conversion ratio of 0.25 to 1 veCRV per CRV <a class="yt-timestamp" data-t="03:19:19">[03:19:19]</a>.

With veCRV, holders gain voting power to boost rewards in the pools they are in <a class="yt-timestamp" data-t="03:05:05">[03:05:05]</a>. This creates a cycle where [[curve_liquidity_pools_and_rewards | liquidity providers]] lock up CRV to earn more veCRV, use their voting rights to boost their own pools, and thereby earn more CRV <a class="yt-timestamp" data-t="03:10:10">[03:10:10]</a>.

### The Curve Wars

For a stablecoin protocol looking to establish liquidity in the Ethereum DeFi ecosystem, setting up a Curve pool is crucial <a class="yt-timestamp" data-t="03:31:31">[03:31:31]</a>. To attract [[curve_liquidity_pools_and_rewards | liquidity providers]], these protocols need to either buy or bribe CRV holders to lock up CRV and boost rewards for their specific pool <a class="yt-timestamp" data-t="03:40:40">[03:40:40]</a>. This competition among protocols to direct CRV emissions to their pools is often referred to as the "Curve Wars" <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.

## Role of [[convex_finance_and_its_role_in_curve_ecosystem | Convex Finance]]

Protocols often engage [[convex_finance_and_its_role_in_curve_ecosystem | Convex Finance]], currently the largest holder of veCRV, to vote for their pools <a class="yt-timestamp" data-t="03:55:55">[03:55:55]</a>. [[convex_finance_and_its_role_in_curve_ecosystem | Convex Finance]] allows CRV holders to stake their CRV and receive boosted rewards in return for Convex locking up their CRV and using it to vote for gauges <a class="yt-timestamp" data-t="04:05:05">[04:05:05]</a>.

## The [[partnerships_and_strategies_in_the_curve_ecosystem | Four Pool]]

The [[partnerships_and_strategies_in_the_curve_ecosystem | Four Pool]] is a specific [[curve_liquidity_pools_and_rewards | liquidity pool]] on Curve comprising UST, FRAX, USDT, and USDC <a class="yt-timestamp" data-t="05:26:26">[05:26:26]</a>. Its primary goal is to replace DAI in the dominant stablecoin pool, making UST and FRAX decentralized stablecoins, especially within the high-liquidity Ethereum ecosystem <a class="yt-timestamp" data-t="05:39:39">[05:39:39]</a>.

To make the [[partnerships_and_strategies_in_the_curve_ecosystem | Four Pool]] successful, Terra and FRAX have been preparing by becoming the two largest protocol holders of CVX (the token of Convex Finance) and providing significant volume incentives to veCVX holders <a class="yt-timestamp" data-t="05:51:51">[05:51:51]</a>. This collective effort, along with other partnerships, aims to direct substantial CVX governance towards the [[partnerships_and_strategies_in_the_curve_ecosystem | Four Pool]], making it the most liquid and utilized stablecoin pool across chains <a class="yt-timestamp" data-t="06:03:03">[06:03:03]</a>.

One strategic reason for the [[partnerships_and_strategies_in_the_curve_ecosystem | Four Pool]] is to facilitate the purchase of Bitcoin for Terra's Luna Foundation Guard (LFG), as a deep liquid [[partnerships_and_strategies_in_the_curve_ecosystem | Four Pool]] allows UST to be swapped for USDT to make large Bitcoin purchases <a class="yt-timestamp" data-t="06:45:45">[06:45:45]</a>.