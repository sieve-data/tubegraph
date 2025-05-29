---
title: Curve liquidity pools and rewards
videoId: nc8Qi8UTT7Y
---

From: [[goingonchain]] <br/> 

## Understanding Curve Finance

[[Curve liquidity pools and rewards | Curve]] is an Automated Market Maker (AMM), similar to decentralized exchanges (DEXs) like PancakeSwap or SushiSwap <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Its unique feature is the algorithm it employs <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Curve's Algorithm: The Stable Swap Curve

Unlike typical AMMs that use the `x * y = k` formula (popularized by Uniswap V2), which works well for most assets based on supply and demand, this formula results in high slippage for stablecoins, especially with large orders <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, 500,000 USDT on SushiSwap might only yield 487,000 USDC <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Technically, one USDT should be close to one USDC <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

[[Curve liquidity pools and rewards | Curve]] solves this by using a hybrid approach with two formulas <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>:
1.  `x + y = k` (Constant Sum Formula) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
2.  `x * y = k` (Constant Product Formula) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>

This "stable swap curve" algorithm allows for much lower slippage on stablecoin swaps, making it attractive for large transactions (whales) <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. When a [[liquidity pool]] is balanced, the algorithm functions as `x + y = k` <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. When the [[liquidity pool]] becomes imbalanced, it transitions to function as `x * y = k` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Curve's Popular Pools and Reward Mechanisms

One of the most popular [[Curve liquidity pools and rewards | Curve]] pools is the "3pool," containing DAI, USDT, and USDC, with a Total Value Locked (TVL) of 3.3 billion <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Any user on Ethereum looking to swap stablecoins will likely use this pool due to its high liquidity <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

For a pool to succeed, it requires both liquidity and rewards to attract that liquidity <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. An example is the Mim Pool, which offers CRV (Curve's native token) and SPELL rewards <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### veCRV and [[Incentive Mechanisms for Liquidity Providers | Incentive Mechanisms]]

[[Providing liquidity through platforms | Liquidity providers]] on [[Curve liquidity pools and rewards | Curve]] earn trading fees and CRV rewards <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. These CRV tokens can be locked up to receive veCRV (vote-escrowed CRV) <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **veCRV Benefits**:
    *   Voting rights in the pool you are in <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   Ability to boost your own pool's rewards <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Locking Period**: CRV can be locked for one to four years, with a conversion ratio of 0.25 to 1 veCRV per CRV <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. For instance, locking one CRV for one year yields 0.25 veCRV <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

This creates a cycle where [[providing liquidity through platforms | liquidity providers]] lock up CRV to boost their pool rewards, aiming to earn more CRV <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### The "Curve War"

For a stablecoin protocol to push liquidity into the Ethereum [[decentralized_finance_options_and_liquid_staking | DeFi]] ecosystem, it needs to set up a [[Curve liquidity pools and rewards | Curve]] pool <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. To attract [[providing liquidity through platforms | liquidity providers]], protocols must bribe or acquire CRV to lock it up and boost rewards for their specific pool <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

The "Curve War" refers to protocols competing to gain more CRV, either by purchasing it or through bribes, to increase CRV rewards for their pools <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. This ensures more CRV emissions are directed to their pools <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Flux and UST have been observed receiving a significant portion of CRV emissions <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Convex Finance's Role

Convex Finance is currently the largest holder of veCRV <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Convex allows CRV holders to get boosted rewards <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>:
*   CRV holders can convert their CRV to cvxCRV, a one-way conversion <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   Staking cvxCRV yields CRV rewards because Convex locks the CRV and uses it to vote for gauges, splitting the rewards with users <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   cvxCRV can also be locked for 16 weeks to receive vlCVX, which provides more rewards and governance voting rights <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

Protocols incentivize vlCVX holders to vote for their pools through bribes <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Votium is a protocol that facilitates these bribes, allowing other protocols to offer incentives to veCRV users <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. For example, Flux and UST have paid around 56 cents per vlCVX for users to vote for their pool <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

## The Four Pool Initiative

The "Four Pool" is a new [[liquidity pool]] initiative that includes UST, Flux, USDT, and USDC <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While currently available on Fantom (FTM) and Arbitrum (ARB), the Ethereum pool is expected soon <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

The primary goal of the Four Pool is to replace DAI in the popular 3pool, effectively removing it from the equation <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. To make the Four Pool a success on [[Curve liquidity pools and rewards | Curve]], significant rewards are necessary, for which Terra and Flux have been preparing <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### Strategic Partnerships

Frax and Terra are the two largest protocol holders of CVX and provide two of the biggest volume [[incentive_mechanisms_for_liquidity_providers | incentive mechanisms]] to vlCVX holders <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. Together, they can make the Four Pool the most liquid and utilized stable pool across chains <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

The partnership for the Four Pool is extensive, involving entities like Terraform Labs (TFL), Frax Finance, Redacted, Badger, Olympus, and Token Reactor <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This collaboration allows them to collectively push significant CVX governance towards the Four Pool <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### Reasons for the Four Pool's Creation

*   **Collaboration over Competition**: Instead of individual stablecoin protocols fighting, the Four Pool promotes cooperation <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **UST as Collateral**: UST becomes a collateralized asset for Frax, driving out DAI and establishing Flux and UST as dominant [[decentralized_finance_options_and_liquid_staking | decentralized stablecoins]] in the Ethereum ecosystem, where liquidity is highest <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Facilitating Bitcoin Purchases**: A deep and liquid Four Pool allows UST to be easily swapped for USDT, which can then be used to purchase Bitcoin <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. For example, the Luna Foundation Guard (LFG) plans to acquire 10 billion in BTC, and the Four Pool enables this, as there isn't enough liquidity on the native Terra chain <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Once Bitcoin is bridged to Terra, it is expected that less reliance on [[Curve liquidity pools and rewards | Curve]] will be needed <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.