---
title: Comparison of yield strategies on Avalanche
videoId: LelKwA_0CpA
---

From: [[goingonchain]] <br/> 

Grow Protocol is a DeFi yield optimizer designed to balance risk and offer leverage on stablecoins <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It provides mechanisms to [[yield_farming_and_growing_your_crypto | grow your crypto]] by maximizing yields from stablecoin holdings <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Grow Protocol's Core Products

On the main net, Grow Protocol offers two primary products:

*   **Powered**
    *   Functions like a fixed deposit for stablecoins <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
    *   Offers better returns than traditional finance (TradFi) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
    *   Includes deposit protection <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Vault**
    *   Provides [[leveraged_yield_products_on_avalanche | leveraged yield]] on stablecoins <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
    *   Works in conjunction with Powered: higher deposits in Powered lead to higher returns for Vault, as Vault leverages assets from Powered <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
    *   Any protocol losses are first covered by the Vault <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Grow Labs on Avalanche

Grow Protocol has extended its expertise to the [[advantages_of_avalanche_platform | Avalanche platform]], introducing two active "Labs":
*   USDC Leverage Yield <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>
*   USDT Leverage Yield <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>

### How Labs Work

Grow Labs leverage farms from Alpha Homora v2, which is a [[leveraged_yield_products_on_avalanche | leveraged yield farming platform]] on [[advantages_of_avalanche_platform | Avalanche]] <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
1.  Funds from the Lab are used as collateral to borrow AVAX <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  Stablecoins are leveraged at 2x to open new positions <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  Strategies are executed automatically based on market conditions <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
4.  Each opening and closing of a position is termed a "strategy cycle" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
5.  Risks are continuously rebalanced through this automated process <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
6.  While individual strategy cycles may sometimes yield negative returns, the average return is approximately 17% <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
7.  The Lab UI displays Total Value Locked (TVL), reserve funds (not deployed), and AVAX exposure <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Comparison to Other Stablecoin Farms

When comparing Grow Labs to other stablecoin farms on [[advantages_of_avalanche_platform | Avalanche]]:

| Feature         | Grow USDT Lab              | Trader Joe USDT Farm       |
| :-------------- | :------------------------- | :------------------------- |
| **APY/APR**     | Around 17% APY <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a> | 17.8% APR <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>  |
| **Reward Type** | Pure stablecoin <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a> | Pool APR + JOE APR <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a> |
| **Liquidity**   | Earn pure stablecoin without needing to sell protocol tokens <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a> | Requires selling JOE tokens to convert rewards back to stablecoins <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a> |

## How to Use Grow Labs

To interact with Grow Labs:
1.  Connect your wallet, ensuring you are on the [[advantages_of_avalanche_platform | Avalanche platform]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
2.  Select "Lab" and choose either the USDC or USDT Lab <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  You can deposit or withdraw stablecoins at any time <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
4.  The default maximum deposit limit is 5,000 stablecoins <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
5.  To increase your deposit allowance, you must own at least 500 GROW tokens <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   GROW is the governance token for Grow Protocol <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   It is currently available on the mainnet and can be obtained from Unison <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Performance During Market Volatility

The Grow team conducted a test on their automated Lab strategy:
*   On December 3rd, they deposited 5,000 stablecoins <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   Between December 3rd and December 6th, AVAX dropped from $104 to $83, a decline of approximately 20% <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Despite this significant AVAX price drop, the Lab strategy yielded a 0.5% gain <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   During this period, the Lab opened and closed positions 13 times <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

> [!CAUTION] Not Risk-Free
> Yield optimization protocols, especially in the rapidly evolving DeFi space, are not risk-free <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. It is crucial to conduct your own research (DYOR) and make informed investment decisions <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

For more information about Grow Protocol and its strategies to earn more yield with stablecoins, you can visit their Twitter or their website at group.com <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.