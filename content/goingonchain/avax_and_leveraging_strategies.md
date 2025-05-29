---
title: AVAX and leveraging strategies
videoId: LelKwA_0CpA
---

From: [[goingonchain]] <br/> 

In a volatile market, protocols like Grow Protocol offer strategies to generate yields from stablecoins using leverage on the Avalanche network <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Grow Protocol is a DeFi yield optimizer that balances risk and offers leverage on stablecoins <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Grow Protocol's Offerings

Grow Protocol provides two key products:
*   **Powered** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>: Functions like a fixed deposit for stablecoins, offering better returns than traditional finance with deposit protection <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Vault** <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>: Offers [[leverage_long_and_short_strategies | leveraged yield]] on stablecoins <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. The two products are interconnected: more deposits in Powered lead to higher returns for the Vault, as the Vault leverages assets from Powered. In return, any protocol losses are first covered by the Vault <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Grow Labs on Avalanche

The Grow Protocol team has brought its expertise to Avalanche, introducing two active "Labs":
*   USDC [[leverage_long_and_short_strategies | leveraged yield]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>
*   USDT [[leverage_long_and_short_strategies | leveraged yield]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>

### How the Labs Work
The Labs leverage farms from Alpha Homora v2, which is a [[defi_strategies_on_avalanche | leveraged yield]] farming platform on Avalanche <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
1.  Funds from the Lab are used as collateral to borrow AVAX <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
2.  Stablecoins are leveraged at 2x to open new positions <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  Based on market conditions, the Labs automatically execute [[investment_strategies_in_a_volatile_market | strategies]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
4.  Each opening and closing of a position is considered a "strategy cycle" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
5.  All operations are automated, with continuous risk rebalancing <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

While individual strategy cycles might sometimes show negative returns, the average return of the Labs is approximately 17% <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The Lab UI displays key metrics like Total Value Locked (TVL), reserve funds not yet deployed, and AVAX exposure <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Comparison to Other Stablecoin Farms
Unlike some other stablecoin farms, such as the USDT farm on [[swapping_ust_on_trader_joe_and_curve_avax | Trader Joe]] which offers rewards broken down into pool APR and JOE APR, the Grow Labs provide a pure stablecoin APY <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This means users earn stablecoins directly, without needing to sell protocol tokens back into stablecoins <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. The USDT Lab currently yields around 17% APY <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## How to Use the Labs

To use Grow Labs:
1.  Connect your wallet to the Avalanche network <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
2.  Select "Lab" and choose either the USDC or USDT Lab <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
3.  You can deposit or withdraw stablecoins at any time <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
4.  The maximum initial deposit is $5,000 <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. To increase this allowance, users must hold at least 500 GROW, the governance token, which is available on Uniswap <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Performance During Market Volatility

The Grow Protocol team conducted a test of their automated Lab [[investment_strategies_in_a_volatile_market | strategy]] <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. From December 3rd to December 6th, AVAX dropped approximately 20%, from $104 to $83 <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Despite this significant drop, a $5,000 investment in the Lab yielded a 0.5% gain during that period <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The Lab opened and closed positions 13 times within the same timeframe <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

> [!CAUTION] Disclaimer
> Yield optimization protocols, especially those involving [[leverage_long_and_short_strategies | leverage]], are not risk-free <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Given the rapidly evolving nature of DeFi, it is crucial to conduct your own research (DYOR) before making any investment decisions <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.