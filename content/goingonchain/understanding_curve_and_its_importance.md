---
title: Understanding Curve and its importance
videoId: nc8Qi8UTT7Y
---

From: [[goingonchain]] <br/> 

[[Introduction to cryptocurrency | Curve]] is an Automated Market Maker (AMM), similar to a Decentralized Exchange (DEX) like PancakeSwap or SushiSwap <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Its unique strength lies in its specialized algorithm, designed to handle stablecoin swaps with minimal slippage <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Curve's Hybrid Algorithm

Traditional AMMs, like Uniswap V2, use the `x * y = k` formula <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. While effective for most assets based on supply and demand, this formula results in high slippage for stablecoin swaps, especially for large orders where one USD Tether (USDT) should ideally be close to one USD Coin (USDC) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

[[Introduction to cryptocurrency | Curve]] addresses this by employing a hybrid approach, combining two formulas <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>:
*   **Constant Sum (`x + y = k`)**: When the liquidity pool is balanced, the algorithm functions like a constant sum model. This minimizes slippage, allowing swaps close to a 1:1 ratio <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Constant Product (`x * y = k`)**: If the liquidity pool becomes imbalanced, the algorithm shifts to the constant product model to maintain stability <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

This hybrid model ensures significantly lower slippage for large stablecoin swaps compared to other DEXs, making [[Introduction to cryptocurrency | Curve]] a preferred platform for whales and large liquidity providers <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## [[Details on the Curve War | The Curve War]]

[[Details on the Curve War | The Curve War]] refers to the competition among protocols to accumulate [[Introduction to cryptocurrency | Curve's]] native token, CRV, and its locked version, veCRV (Vote-Escrowed CRV) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Liquidity and Rewards
For a liquidity pool to thrive, it requires both liquidity and attractive rewards <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Liquidity Providers (LPs) on [[Introduction to cryptocurrency | Curve]] earn trading fees and CRV rewards <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. By locking CRV for periods of one to four years, LPs receive veCRV, which grants them voting rights to boost rewards in their chosen pools <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This creates a cycle where LPs lock CRV to earn more CRV <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Role of Convex Finance
Convex Finance is currently the largest holder of veCRV <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. It allows CRV holders to convert their CRV into cvxCRV, a one-way conversion, to receive boosted CRV rewards <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Convex locks the deposited CRV to vote on gauges (reward distribution), and the rewards are then shared with cvxCRV stakers <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. Additionally, users can lock their CVX tokens for 16 weeks to obtain vlCVX, which provides more rewards and governance voting rights <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Bribes and Votium
Protocols aiming to drive liquidity into their [[Introduction to cryptocurrency | Curve]] pools either buy CRV to lock it themselves or offer bribes to vlCVX holders to vote for their pools <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Votium is a platform that facilitates these bribes, allowing protocols to pay vlCVX users for their votes <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. For instance, FLUX and UST have offered significant bribes to incentivize votes for their pools <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. This competitive bribing is central to the [[Details on the Curve War | Curve War]], as protocols vie for greater CRV emissions to boost their pool rewards <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## [[Four Pool and its significance | Four Pool]]

The [[Four Pool and its significance | Four Pool]] is a strategic partnership featuring UST, FLUX, USDC, and USDT <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Its primary objective is to replace DAI as the dominant stablecoin in the most liquid stablecoin pool on [[Introduction to cryptocurrency | Curve]], which historically included DAI, USDT, and USDC <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### Key Players and Motivations
To ensure the [[Four Pool and its significance | Four Pool's]] success on [[Introduction to cryptocurrency | Curve]], significant rewards are necessary <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. Terra and Frax, as two of the largest protocol holders of CVX, are pivotal in this effort <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. They provide substantial volume incentives to vlCVX holders, aiming to make the [[Four Pool and its significance | Four Pool]] the most liquid and utilized stablecoin pool across chains <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

The partnership also includes other notable protocols like Retracted, Badger, and Olympus Token <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Their collective influence can direct a significant amount of [[Introduction to cryptocurrency | Curve]] governance towards the [[Four Pool and its significance | Four Pool]] <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### Strategic Advantages
The motivations behind the [[Four Pool and its significance | Four Pool]] include:
*   **Collaboration over Competition**: Instead of competing, protocols like UST and Frax are working together <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **UST as Collateral**: UST becomes a collateralized asset for Frax, leveraging its stability <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Decentralized Stablecoin Dominance**: The partnership seeks to establish FLUX and UST as leading decentralized stablecoins, particularly within the highly liquid Ethereum DeFi ecosystem <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Facilitating Bitcoin Purchases**: For TerraForm Labs (TFL), a key reason is to facilitate large Bitcoin purchases <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. With a deep and liquid [[Four Pool and its significance | Four Pool]], UST can be efficiently swapped for USDT to execute these large Bitcoin acquisitions <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.