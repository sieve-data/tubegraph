---
title: Details on the Curve War
videoId: nc8Qi8UTT7Y
---

From: [[goingonchain]] <br/> 

The "Curve War" refers to the competition among various decentralized finance (DeFi) protocols to gain influence and control over the [[understanding_curve_and_its_importance | Curve]] Finance ecosystem, primarily by accumulating and locking the native CRV token to boost liquidity rewards for their own pools <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>. This influence is crucial for stablecoin protocols looking to establish deep liquidity within the Ethereum DeFi space <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.

## Understanding Curve

[[understanding_curve_and_its_importance | Curve]] is an Automated Market Maker (AMM), similar to decentralized exchanges like PancakeSwap or SushiSwap <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. What distinguishes [[understanding_curve_and_its_importance | Curve]] is its specialized algorithm <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.

Traditional AMMs, such as Uniswap V2, typically use the `x * y = k` formula, which works well for most assets based on supply and demand <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. However, this formula results in high slippage for stablecoin swaps, especially for large orders, where ideally one USDT should yield close to one USDC <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>.

[[understanding_curve_and_its_importance | Curve]] solves this problem using a hybrid approach combining two formulas: `x + y = k` and `x * y = k` <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.
*   When a liquidity pool is balanced, the algorithm functions as `x + y = k` (constant sum formula), resulting in very low slippage <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   When the pool becomes imbalanced, the algorithm shifts to `x * y = k` (constant product formula) <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

This design significantly reduces slippage for large stablecoin swaps compared to other AMMs, making it favored by large liquidity providers (whales) <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

## Mechanics of the Curve War

For a liquidity pool on [[understanding_curve_and_its_importance | Curve]] to be successful, it needs deep liquidity and attractive rewards <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>. The most popular pool on [[understanding_curve_and_its_importance | Curve]] is the 3-pool (DAI, USDT, USDC), with a Total Value Locked (TVL) of 3.3 billion <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.

### CRV and veCRV

CRV is the native token of [[understanding_curve_and_its_importance | Curve]] <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. Liquidity providers (LPs) on [[understanding_curve_and_its_importance | Curve]] earn trading fees and CRV rewards <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. LPs can choose to lock their CRV tokens to receive veCRV (Vote-Escrowed CRV) <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
*   veCRV holders gain voting rights to influence which pools receive higher CRV emissions (rewards) <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
*   Locking CRV for one to four years yields a 0.25 to 1 conversion ratio to veCRV <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.
*   This creates a cycle: LPs lock CRV to get veCRV, use voting rights to boost their own pools, and earn more CRV <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

### The Role of Convex Finance and Votium

Stablecoin protocols aiming to attract liquidity on [[understanding_curve_and_its_importance | Curve]] need to either acquire CRV to lock themselves or bribe existing veCRV holders to vote for their pools <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. This is where Convex Finance comes in <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.

*   **Convex Finance:** Convex is currently the largest holder of veCRV <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. It allows CRV holders to convert their CRV to cvxCRV (a one-way conversion) and stake it to earn boosted CRV rewards <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. Convex takes the users' CRV, locks it for veCRV, and uses it to vote for gauges, splitting the rewards with the users <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>. Users can also lock their cvx tokens for 16 weeks to obtain vlCVX, which provides more rewards and governance voting rights <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
*   **Votium:** Votium is a protocol that enables other protocols to offer "bribes" to vlCVX holders to influence their votes towards specific pools <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. For example, Flux and UST have been observed paying around 56 cents per vlCVX for votes in their pool <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.

The "Curve War" is essentially this battle among protocols to acquire more CRV, either through direct purchase or by bribing veCRV/vlCVX holders, to direct CRV rewards to their respective pools <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

## The Four Pool

The "Four Pool" is a specific liquidity pool initiative that highlights the dynamics of the Curve War <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>. It is a partnership between UST, FLUX, USDT, and USDC <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.

### Goals of the Four Pool
The primary goal of the Four Pool is to replace DAI in the popular 3-pool (DAI, USDT, USDC), effectively "saying goodbye to DAI" <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.

To achieve success on [[understanding_curve_and_its_importance | Curve]], the Four Pool needs substantial rewards <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>. Terra (TFL) and Frax are key players in this, being two of the largest protocol holders of CVX (Convex Finance's token) <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>. They provide significant volume incentives to vlCVX holders <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.

The Four Pool has garnered partnerships beyond Terra and Frax, including Retracted, Badger, Olympus, and Token Reader <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>. These collaborations aim to direct substantial CVX governance power towards the Four Pool <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

### Strategic Motivations
The strategy behind the Four Pool involves collaboration rather than competition among stablecoin protocols like UST and Frax <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>.
*   UST becomes a collateralized asset for Frax <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.
*   The partnership aims to drive out DAI and establish FLUX and UST as the dominant decentralized stablecoins within the Ethereum ecosystem, where liquidity is highest <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
*   A deeper Four Pool facilitates Terra's (TFL) plan to acquire Bitcoin <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>. A deep, liquid Four Pool enables UST to be swapped for USDT to make large Bitcoin purchases, as native on-chain liquidity for such large orders is limited <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>.