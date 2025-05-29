---
title: GRO Protocol Labs and their products
videoId: LelKwA_0CpA
---

From: [[goingonchain]] <br/> 

GRO Protocol is a DeFi yield optimizer designed to balance risk and offer leverage on stablecoins <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It has been operating on the mainnet, providing two primary products: Powered and Vault <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Core Products

### Powered
Powered functions similarly to a fixed deposit where users place stablecoins to achieve better returns than traditional finance (TradeFi) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It also offers deposit protection <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Vault
Vault offers leveraged yield on stablecoins <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Relationship Between Powered and Vault
The two products work in conjunction <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Increased deposits in Powered lead to higher returns for Vault, as Vault leverages assets from Powered <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. In return, any protocol losses are first covered by the Vault <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## GRO Protocol Labs

The GRO Protocol team has extended its expertise to Avalanche, introducing two active "Labs": the USDC leverage yield and the USDT leverage yield <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

### How Labs Work
The Labs leverage farms from Alpha Homora v2, a leveraged yield farming platform on Avalanche <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
1.  **Collateralization**: Funds from the Lab are used as collateral to borrow AVAX <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
2.  **Leverage**: Stablecoins are leveraged at 2x to open new positions <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  **Automated Strategy**: The Labs automatically execute strategies based on market conditions <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. A "strategy cycle" refers to the opening and closing of a position <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This process is automated, with risks continuously rebalanced <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Performance and Features
*   **Average Return**: The average return for Labs is approximately 17% <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. While individual strategy cycles may show negative returns, the overall average remains positive <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **User Interface**: The Labs' user interface clearly displays the Total Value Locked (TVL), the reserve (funds not currently deployed), and the AVAX exposure <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Yield Type**: Unlike some other stablecoin farms (e.g., Trader Joe's USDT farm), GRO Protocol Labs provide yield in pure stablecoin (APY), rather than protocol tokens which would need to be sold to convert back to stablecoin <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### User Interaction
Users can connect their wallet (on Avalanche) and choose between the USDC or USDT Lab <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Deposits and withdrawals can be made at any time <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Deposit Limit**: The maximum initial deposit limit is 5,000 <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Allowance Increase**: To increase the deposit allowance, users must hold at least 500 GRO, which is the governance token for the protocol <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. GRO is currently available on Uniswap <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Test Case Example
A test was conducted on the automated Lab strategy from December 3rd to December 6th <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. During this period, AVAX dropped by approximately 20% (from $104 to $83) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Despite this significant market volatility, the Lab strategy yielded a 0.5% gain on a $5,000 deposit <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The Lab opened and closed positions 13 times during this period <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Considerations
While yield optimization protocols like GRO Protocol Labs can be interesting in times of market volatility, they are not risk-free <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Users are advised to conduct their own research given the rapidly changing nature of DeFi <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.