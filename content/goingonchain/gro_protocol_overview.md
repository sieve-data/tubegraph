---
title: GRO Protocol overview
videoId: LelKwA_0CpA
---

From: [[goingonchain]] <br/> 

GRO Protocol is a decentralized finance (DeFi) yield optimizer designed to balance risk and offer leverage on stablecoins <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Core Products

GRO Protocol operates on the mainnet with two primary products:

*   **Powered**
    *   Functions like a fixed deposit for stablecoins <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
    *   Offers better returns than traditional finance (TradFi) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
    *   Provides deposit protection <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Vault**
    *   Offers leveraged yield on stablecoins <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
    *   Works closely with "Powered": increased deposits in Powered lead to higher returns for Vault, as Vault leverages assets from Powered <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
    *   Any protocol losses are first covered by the Vault <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## GRO Labs on Avalanche

The GRO Protocol team has extended their expertise to the Avalanche network, introducing two active "Labs":
*   USDC Leverage Yield <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>
*   USDT Leverage Yield <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>

### How the Labs Work

The Labs leverage farms from Alpha Homora V2, which is a leveraged yield farming platform on Avalanche <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   Funds from the Lab are used as collateral to borrow AVAX <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   Stablecoins are leveraged at 2x to open new positions <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   Strategies are executed automatically based on market conditions <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   Each opening and closing of a position is considered a "strategy cycle" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   Risks are continuously rebalanced <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

While individual strategy cycles might sometimes yield negative returns, the average return for the Lab is approximately 17% <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The Lab UI displays total value locked (TVL), reserves (funds not deployed), and AVAX exposure <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Comparison to Other Stablecoin Farms

Unlike some stablecoin farms (e.g., on Trader Joe) that might offer a high APR (e.g., 17.8%) but distribute rewards in protocol tokens, GRO Labs offer yield in pure stablecoin <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This means users earn stablecoin directly, without needing to sell volatile protocol tokens to convert them back to stablecoins <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### How to Use the Lab

1.  Connect your wallet on Avalanche <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
2.  Choose the desired Lab (USDC or USDT) <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  Deposits can be made, and withdrawals are possible at any time <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
4.  There is a maximum deposit limit of $5,000 <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
5.  To increase this allowance, users need to own at least 500 GRO tokens <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### GRO Token

GRO is the governance token for the protocol <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It is currently available on Uniswap <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Performance in Volatile Markets

The GRO team conducted a test of their automated Lab strategy from December 3rd to December 6th <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. During this period, AVAX dropped approximately 20%, from $104 to $83 <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Despite this significant drop, the Lab strategy yielded a 0.5% gain <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The Lab opened and closed positions 13 times during this period <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Considerations

Yield optimization protocols like GRO can be interesting during market volatility <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. However, they are not risk-free <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Given the nascent and rapidly changing nature of DeFi, users are encouraged to conduct their own research and make informed investment decisions <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

More information about GRO Protocol can be found on their Twitter and at gro.com <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.