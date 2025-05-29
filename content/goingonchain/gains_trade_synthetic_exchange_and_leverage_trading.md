---
title: Gains Trade synthetic exchange and leverage trading
videoId: UlzBJQoPlfY
---

From: [[goingonchain]] <br/> 

Gains Trade is a synthetic exchange designed for [[Leverage long and short strategies | leveraged traders]] on the Polygon chain <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. It aims to differentiate itself from other platforms by addressing key concerns of traders <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Addressing Trader Concerns

### Price Manipulation (Scam Wicks)
A "scam wick" is a situation where an exchange or individual purposefully creates a price spike to trigger stop losses, leading to massive buy or sell orders <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This often occurs on centralized exchanges that support futures trading <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Gains Trade tackles this problem by building a custom Decentralized Oracle Network (DON) enabled by Chainlink <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This custom DON provides real-time prices to traders <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

Here's how it works:
*   When an order needs to be executed, the trading contract requests the spot price from an aggregator contract <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   The aggregator contract requests prices from eight different on-demand Chainlink nodes <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Each Chainlink node takes the median price from seven different exchange APIs and sends the result back to the aggregator contract <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   This result is compared with the Chainlink price feed <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. If the difference is more than 1.5%, the node's answer is rejected, and the platform waits for the next answer <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   This process ensures traders receive a real and fair spot price <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Since the platform is built on Polygon, it benefits from cheap gas fees, allowing for frequent price calls to reflect the best price for traders <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Low Liquidity
Gains Trade uses its GNS token to build up liquidity <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. The trades and leverage on Gains Trade are synthetic, meaning there isn't a real spot asset being bought or sold <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

The platform is supported by two pools:
1.  **GNS DAI Pool**: Acts as liquidity <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
2.  **Trading Pool**: Where users deposit DAI when entering a trade, and from which they exit with their profit or loss <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### GNS Tokenomics and Deflationary Mechanism
The DAI Trading Pool is maintained at 110% over-collateralized <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Excess Die:** If the Trading Pool exceeds 110%, the extra DAI is used to buy GNS from the GNS DAI Pool, and the GNS is then burned <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Deficit Die:** If the Trading Pool falls below 100%, GNS is minted and sold for DAI to top up the Trading Pool <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

This mechanism creates buying pressure on the GNS token when more traders are winning or losing, making GNS deflationary <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Statistics show that historically, more traders lose than win, contributing to GNS burning <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Platform Features

Gains Trade offers:
*   A wide selection of assets, including crypto and forex <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Fair spot prices due to its custom price feed <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   High leverage options, up to 150x <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Fees and [[NFT features and DeFi use cases on Gains Network | NFT]] Utility

### Trading Fees
Trading fees range from 0.06% to 0.08% for maker and taker orders <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. There are no funding fees <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. A small spread, typically around 0.025%, should also be considered <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### [[NFT features and DeFi use cases on Gains Network | NFT]] Features
Gains [[NFT features and DeFi use cases on Gains Network | NFT]]s come with interesting features for traders <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. For example, a bronze level [[NFT features and DeFi use cases on Gains Network | NFT]] was going for 1.14 ETH on OpenSea <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

These [[NFT features and DeFi use cases on Gains Network | NFT]]s provide real [[NFT features and DeFi use cases on Gains Network | DeFi]] use cases:
*   Lowering spread fees <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Ability to run a bot for executing liquidations and limit orders <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   Boosting liquidity pool rewards <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

## Tokenomics and Statistics

The Gains Network platform launched in January 2021 on the Mainnet but later transitioned to the Polygon chain due to high gas fees <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. A 1:1000 split of GPhantom to GNS tokens was implemented <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

*   **Total Supply**: Currently 38.5 million GNS <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Maximum Supply**: 100 million GNS <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Deflationary**: GNS is designed to be deflationary, with more tokens burned as traders lose <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### Platform Performance
*   **Fees Earned**: From inception, the platform has earned approximately $2.8 million in fees <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Growth accelerated from December last year to February this year <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Trade Volume**: Accumulated $5 billion in trade volume since its start <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **User Growth**: There is a growing number of users <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

These statistics suggest the project may have found a product-market fit <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. The GNS token currently has a deflation rate of -25% <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

## Roadmap

The roadmap includes a long list of tasks:
*   Adding more crypto assets <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   GNS single staking <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   Multi-chain expansion <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   Plans to venture into a decentralized casino <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

## Market Comparison

Gains' market cap is still relatively small compared to market leaders like dydx <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Platform Walkthrough

The GNS Trade platform allows users to choose between trading crypto or forex <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   Users can start with as little as 35 DAI <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   Setting collateral and leverage (up to 150x) is straightforward <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   Stop loss and take profit can be easily set <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   The UI is described as simple <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

A "tech core practice" feature is available on the Polygon testnet, allowing users to try out their trading skills before live trading <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

For those not interested in trading, staking options are available to contribute liquidity to the GNS DAI Pool and the Trading Pool <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   The Trading Pool currently offers a 10% APY <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   The liquidity pool offers 47% APY <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

Platform performance and statistics can be viewed on Dune Analytics via the "statistic" link <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

## Analyst Thoughts

*   **Pros**:
    *   Innovative use of its own token for liquidity, supporting asset onboarding and deflation <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   Simple platform UI <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   Smart inclusion of [[NFT features and DeFi use cases on Gains Network | NFT]]s providing additional features for traders, including trading bot setup <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
    *   Business metrics indicate product-market fit with increasing users, trade volume, and fee earnings <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

*   **Concerns**:
    *   Most liquidity currently resides on the Ethereum mainnet, posing a potential liquidity challenge for Polygon-based Gains Trade <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. Multi-chain expansion could address this <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## Community

The [[Gains Network overview and platform features | Gains Network]] has a vibrant Discord community <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Updates can also be followed on Twitter <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.