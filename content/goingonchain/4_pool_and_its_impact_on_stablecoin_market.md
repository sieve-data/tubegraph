---
title: 4 Pool and its impact on stablecoin market
videoId: nc8Qi8UTT7Y
---

From: [[goingonchain]] <br/> 

4 Pool is a significant development aiming to enhance the presence of certain [[types_of_stablecoins | stablecoins]] within the Ethereum DeFi ecosystem <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## What is 4 Pool?

The 4 Pool is a [[using_stablecoins_in_yield_farming | liquidity pool]] currently available on Fantom (FTM) and Arbitrum (ARB) One, with an Ethereum pool expected to arrive soon <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. It contains four assets:
*   UST <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   FLUX <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   USDT <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   USDC <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>

## Understanding Curve Finance

To grasp the impact of 4 Pool, it's essential to understand Curve Finance ("Curve") <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

### Curve as an Automated Market Maker (AMM)
Curve is an Automated Market Maker (AMM), similar to decentralized exchanges (DEXs) like PancakeSwap or SushiSwap <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. What sets Curve apart is its unique algorithm <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Curve's Algorithm for [[types_of_stablecoins | Stablecoins]]
Typical DEXs use the `x * y = k` formula, which works well for most assets based on supply and demand <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. However, this formula leads to high slippage for [[types_of_stablecoins | stablecoins]], especially with large orders, because one USDT should ideally trade for close to one USDC <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

Curve addresses this issue with a hybrid approach using two formulas <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>:
1.  **`x + y = k` (Constant Sum Formula)**: When the [[using_stablecoins_in_yield_farming | liquidity pool]] is balanced, the algorithm functions similarly to `x + y = k`, resulting in minimal slippage <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
2.  **`x * y = k` (Constant Product Formula)**: When the [[using_stablecoins_in_yield_farming | liquidity pool]] becomes imbalanced, the algorithm shifts to function more like `x * y = k` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

This hybrid model allows Curve to maintain very low slippage for [[types_of_stablecoins | stablecoin]] swaps, making it popular among large traders ("whales") <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. For example, a 500,000 USDT swap on SushiSwap might yield 487,000 USDC due to high slippage, while on Curve, the slippage is much lower, getting closer to the full amount <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## The Curve War

Curve's popularity has led to a fierce competition known as the "Curve War" <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

### Liquidity and Rewards
For a [[using_stablecoins_in_yield_farming | liquidity pool]] to succeed on Curve, it needs significant liquidity, which is attracted by rewards <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. The native token for Curve is CRV <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### veCRV and Boosting Rewards
[[using_stablecoins_in_yield_farming | Liquidity providers]] on Curve earn trading fees and CRV rewards <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. By locking up CRV tokens for a period of one to four years, users receive veCRV (vote-escrowed CRV) <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. veCRV holders can vote to boost the rewards of the specific pool they are in <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This creates a cycle where LPs lock CRV to earn more veCRV, use it to boost their pool's rewards, and attract more liquidity <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Convex Finance (CVX)
Convex Finance (Convex) is the largest holder of veCRV <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Convex allows CRV holders to gain boosted rewards by converting their CRV to cvxCRV <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This conversion is one-way, meaning cvxCRV cannot be directly converted back to CRV through Convex (only via secondary markets) <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. When users stake cvxCRV, Convex aggregates their CRV, locks it for veCRV, and uses the voting power to boost rewards, which are then shared with the users <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

Additionally, users can lock their CVX tokens for 16 weeks to receive vlCVX, which grants more rewards and governance voting rights <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Bribing for Votes (Votium)
Protocols looking to establish liquidity in the Ethereum DeFi space need to set up a Curve pool <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. To boost their pool's rewards and attract liquidity, they either buy CRV to lock up or bribe existing veCRV holders <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Votium is a protocol that facilitates these bribes, allowing other protocols to pay vlCVX users to vote for their specific pools <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. For instance, FLUX and UST have been observed paying around 56 cents per vlCVX for users to vote for their pool <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

This intense competition for CRV rewards and voting power among protocols, either by acquiring CRV or offering bribes, is what defines the "Curve War" <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. FLUX and UST have secured a significant portion of CRV emissions due to their active participation <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## 4 Pool's Goals and Impact

The 4 Pool represents a strategic partnership between UST, FLUX, USDC, and USDT <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

### Replacing DAI and Dominating Stablecoin Liquidity
One of 4 Pool's primary goals is to "say bye bye to DAI" <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. The most popular existing [[types_of_stablecoins | stablecoin]] pool on Curve is the "3pool," consisting of DAI, USDT, and USDC <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. 4 Pool aims to replace DAI with UST and FLUX, establishing itself as the most liquid and utilized [[types_of_stablecoins | stablecoin]] pool across chains <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Strategic Partnerships and Incentives
Terra and Frax are key partners in the 4 Pool initiative <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. They are two of the largest protocol holders of CVX and provide significant volume incentives to vlCVX holders, which helps direct governance votes towards the 4 Pool <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. Other partners include Retracted, Badger, and Olympus Token Reader, collectively pushing CVX governance towards the 4 Pool <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Reasons Behind the Collaboration
The collaboration behind 4 Pool stems from several strategic objectives <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>:
*   **Cooperation over Competition**: Instead of individual protocols fighting, 4 Pool fosters collaboration between UST, Frax, and other partners <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **UST as Collateral**: UST becomes a collateralized asset for Frax <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Decentralized [[types_of_stablecoins | Stablecoin]] Dominance**: The initiative aims to drive out DAI, allowing FLUX and UST to become dominant decentralized [[types_of_stablecoins | stablecoins]] within the Ethereum ecosystem, where liquidity is highest <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Facilitating Bitcoin Purchases**: A deep and liquid 4 Pool allows UST to be swapped for USDT, facilitating large-scale Bitcoin purchases by the Luna Foundation Guard (LFG), which plans to acquire 10 billion USD worth of Bitcoin <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. This deep liquidity is crucial as there isn't sufficient liquidity on the native Terra chain for such large transactions <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. While the initial plan is to use Curve, the expectation is that once Bitcoin is bridged to Terra, the reliance on Curve for these purchases might decrease <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.