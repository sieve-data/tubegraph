---
title: Four Pool and its significance
videoId: nc8Qi8UTT7Y
---

From: [[goingonchain]] <br/> 

The "Four Pool" is a liquidity pool containing four assets: UST, FRAX, USDT, and USDC <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While currently available on Fantom (FTM) and Arbitrum (ARB), an Ethereum pool is expected to arrive soon <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This pool aims to elevate Flux and UST within the Ethereum DeFi ecosystem <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Understanding Curve

To grasp the impact of the Four Pool, it's essential to first understand [[understanding_curve_and_its_importance | Curve]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. [[understanding_curve_and_its_importance | Curve]] is an Automated Market Maker (AMM) that functions similarly to a Decentralized Exchange (DEX) like PancakeSwap or SushiSwap <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Its uniqueness lies in its algorithm <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

A typical AMM often uses the `x * y = k` formula, popularized by Uniswap V2, which works well for most assets based on supply and demand <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. However, this formula is inefficient for stablecoins, especially for large orders, leading to high slippage <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. For instance, a 500k USDT swap on Sushi might only yield 487k USDC due to high slippage <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

[[understanding_curve_and_its_importance | Curve]] solves this issue by employing a hybrid approach with two formulas <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>:
*   `x + y = k` (Constant Sum Formula) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a> <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
*   `x * y = k` (Constant Product Formula) <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a> <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

When the liquidity pool is balanced, the algorithm functions as `x + y = k`, keeping slippage low <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. If the pool becomes imbalanced, it transitions to `x * y = k` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This hybrid model results in significantly lower slippage for stablecoin swaps on [[understanding_curve_and_its_importance | Curve]], making it a preferred platform for large traders ("whales") <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

The most popular pool on [[understanding_curve_and_its_importance | Curve]] is the "3pool," which has a Total Value Locked (TVL) of 3.3 billion <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. It's the most liquid and commonly used stablecoin pool for swaps on Ethereum <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The Curve War

A successful pool requires both liquidity and rewards to attract that liquidity <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. [[understanding_curve_and_its_importance | Curve]]'s native token, CRV, is central to the [[details_on_the_curve_war | Curve War]] <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### veCRV Mechanism
Liquidity Providers (LPs) on [[understanding_curve_and_its_importance | Curve]] earn trading fees and CRV rewards <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. These CRV rewards can be locked up to receive veCRV (vote-escrowed CRV) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   veCRV grants voting rights to boost rewards in the pool where the LP provides liquidity <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   This creates a cycle where LPs lock CRV for veCRV to boost their pool's rewards, earning more CRV <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   CRV can be locked for 1 to 4 years, with a conversion ratio of 0.25 veCRV per CRV for one year <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

### Protocol Strategy and Bribes
Stablecoin protocols seeking to increase liquidity in the Ethereum DeFi space need to establish a [[understanding_curve_and_its_importance | Curve]] pool <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. They must either acquire CRV to lock up or "bribe" existing veCRV holders to vote for their pool's rewards <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This incentivizes liquidity providers to join their pool due to boosted CRV rewards <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

Convex Finance (CVX) is the largest holder of veCRV <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   Convex allows CRV holders to get boosted rewards by converting CRV to cvxCRV (a one-way conversion) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   Convex then locks the CRV and uses it to vote for gauges, splitting rewards with cvxCRV stakers <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   Users can also lock CVX for 16 weeks to receive vlCVX, which grants more rewards and governance voting rights <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

Protocols can "bribe" vlCVX holders to vote for their pools via platforms like Votium <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. For example, Flux and UST have been paying around 56 cents per vlCVX for votes in their pool <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. This ongoing competition among protocols to accumulate CRV or bribe veCRV/vlCVX holders for more CRV emissions defines the [[details_on_the_curve_war | Curve War]] <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Four Pool's Strategy and Significance

The Four Pool is a partnership between UST, FRAX, USDC, and USDT <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Its primary objective is to replace DAI in the popular [[understanding_curve_and_its_importance | Curve]] 3pool (which consists of DAI, USDT, and USDC) <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

To achieve success on [[understanding_curve_and_its_importance | Curve]], the Four Pool needs substantial rewards <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. Terra and Frax, as the two largest protocol holders of CVX, are providing significant volume incentives to vlCVX holders <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This combined effort is intended to make the Four Pool the most liquid and widely used stablecoin pool across different chains <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

Beyond Terra and Frax, the Four Pool partnership involves other prominent protocols like Retracted, Badger, Olympus, and Token Reader, which can collectively direct substantial CVX governance power towards the Four Pool <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Reasons for Four Pool's Existence
Terraform Labs (TFL) proposed the Four Pool with several key motivations <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>:
*   **Collaboration over Competition**: Instead of individual protocols fighting for liquidity, the Four Pool promotes collaboration <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **UST as Collateral for FRAX**: UST becomes a collateralized asset for FRAX <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Decentralized Stablecoin Dominance**: The initiative aims to drive out DAI and establish FRAX and UST as the leading decentralized stablecoins within the Ethereum ecosystem, where liquidity is highest <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Facilitating Bitcoin Purchases**: A deeply liquid Four Pool allows UST to be easily swapped for USDT, which can then be used to purchase Bitcoin for the Luna Foundation Guard's (LFG) reserves <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. LFG plans to acquire 10 billion in BTC, and such liquidity is not available on the native Terra blockchain <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Once Bitcoin is bridged to Terra, it is expected to reduce the reliance on [[understanding_curve_and_its_importance | Curve]] for these large transactions <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.