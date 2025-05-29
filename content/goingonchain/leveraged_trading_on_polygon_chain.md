---
title: Leveraged Trading on Polygon Chain
videoId: UlzBJQoPlfY
---

From: [[goingonchain]] <br/> 

Gains Network offers an interesting product called Gains Trade, which is a synthetic exchange built specifically for [[leverage_strategies_on_defi_platforms | leveraged traders]] on the [[polygon_and_layer_2_development | Polygon]] chain <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The platform aims to differentiate itself in the competitive landscape of [[leverage_strategies_on_defi_platforms | leveraged trading]] platforms <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Key Concerns for Leveraged Traders and Gains Trade Solutions

Traders in [[leverage_strategies_on_defi_platforms | leveraged trading]] are typically concerned about two main points: scam wicks (price manipulation) and low liquidity <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a> <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Price Manipulation (Scam Wicks)
A "scam wick" is a situation where an exchange purposely creates a sudden price spike or drop to trigger stop-losses, resulting in massive buy or sell orders <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This phenomenon usually occurs on centralized exchanges that support futures trading <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Gains Trade addresses this problem by building a custom Decentralized Oracle Network (DON) enabled by Chainlink <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **How it works:**
    *   When an order is executed, the trading contract requests the spot price from an aggregator contract <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
    *   The aggregator contract requests prices from eight different on-demand Chainlink nodes <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   Each Chainlink node takes the median price from seven different exchange APIs and sends the result back to the aggregator contract <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
    *   This result is then compared with the Chainlink price feed <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   If the difference exceeds 1.5% from the Chainlink price feed, the node's answer is rejected, and the system waits for the next answer <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   This process ensures that traders receive a real and fair spot price <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The platform's operation on the [[polygon_and_layer_2_development | Polygon]] chain allows for cheap gas fees, enabling frequent price calls to reflect the best price <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Low Liquidity
Gains Trade builds its liquidity using the GNS token <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Trades and leverage on Gains are synthetic, meaning no real spot assets are bought or sold <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. The platform is supported by two pools:
1.  **GNS DAI Pool:** Acts as the liquidity <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
2.  **Trading Pool:** Used for depositing DAI when entering a trade and receiving profits/losses when exiting <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

The DAI trading pool is maintained at 110% over-collateralized <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   If the trading pool exceeds 110%, the extra DAI is used to buy GNS from the GNS DAI pool, and that GNS is burned <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   If the trading pool falls below 100%, GNS is minted and sold for DAI to top up the trading pool <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
This mechanism creates buying pressure on the GNS token if more traders are winning or losing, making GNS deflationary <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Statistical data since the project's start indicates more traders lose than win, contributing to GNS deflation <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Platform Features

Gains Trade's unique setup, including its custom price feed and liquidity model on [[polygon_and_layer_2_development | Polygon]], enables several features:
*   **Asset Selection:** Wide selection of assets for trading, including crypto and forex <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Fair Spot Price:** Ensures traders get a fair spot price <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **High Leverage:** Offers high leverage up to 150x <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Fees:** Transaction fees range from 0.06% to 0.08% for maker and taker orders, with no funding fees <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. There is also a small spread, typically around 0.025% <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### NFT Utility
Gains NFTs come with interesting DeFi use cases <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a> <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Lower Fees:** They can lower spread fees <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Bot Execution:** Enable users to run bots for executing liquidations and limit orders <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **LP Rewards Boost:** Provide the ability to boost liquidity pool rewards <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
Bronze level NFTs were observed selling for 1.14 ETH on OpenSea <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Tokenomics and Statistics

The Gains Network platform launched in January 2021 on the Ethereum Mainnet but transitioned to the [[polygon_and_layer_2_development | Polygon]] chain due to high gas fees <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. During this transition, a one-to-one thousand split was performed, meaning 1,000 GNS tokens were issued for every GPhantom token <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

*   **Current Supply:** The total supply of GNS is 38.5 million <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Maximum Supply:** The maximum supply is 100 million <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Deflationary Design:** GNS is designed to be deflationary, with more tokens burned as traders lose <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. The current inflation rate for GNS is -25%, indicating deflation <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Platform Performance
Key statistics indicate strong growth:
*   **Fees Earned:** From inception, the platform has earned approximately $2.8 million in fees <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Growth Acceleration:** Fee growth accelerated significantly from December to February <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Trade Volume:** Accumulated trade volume since launch is $5 billion <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **User Growth:** There is a growing number of users <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
These metrics suggest that the project may have found a product-market fit <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Roadmap

The roadmap includes a long list of planned tasks <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>:
*   Adding more crypto assets <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   GNS single staking <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   Multi-chain expansion <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   Plans to venture into a decentralized casino <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

## Market Position and Concerns

Compared to market leaders like dYdX, Gains Network's market cap is still relatively small <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. A key concern is that most liquidity for such platforms currently resides on the Ethereum Mainnet, potentially posing a liquidity challenge for platforms built on [[polygon_and_layer_2_development | Polygon]] <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. However, multi-chain capabilities could help attract more liquidity <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## Platform Walkthrough

The G Trade platform has a simple UI <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Trading Interface:** Users can choose to trade between crypto or forex <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Trades can be started with as little as 35 DAI, by setting collateral, leverage (up to 150x), stop loss, and take profit <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Practice Mode:** A "tech core practice" feature is available on the [[polygon_and_layer_2_development | Polygon]] testnet, allowing users to try out their trading skills before going live <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Staking:** For those not interested in trading, staking options are available for contributing liquidity to the GNS DAI pool and the trading pool <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
    *   The trading pool offers a 10% APY <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
    *   The liquidity pool offers 47% APY <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   **Statistics:** Platform performance and statistics are available via Dune Analytics <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

## Thoughts and Conclusion

The idea of using an own token to provide liquidity is appealing, as it helps onboard more assets and contributes to the token's deflationary nature <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The platform's UI is simple, and the inclusion of NFTs to provide additional features for traders, including setting up trading bots, is a smart move <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Business statistics, such as increasing users, trade volume, and fees, point to a strong product-market fit <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. However, the concentration of liquidity on the Ethereum Mainnet remains a challenge for a trading platform on [[polygon_and_layer_2_development | Polygon]] <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. Multi-chain expansion could help attract more users and liquidity <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

> [!NOTE] Disclosure
> The presenter is not currently invested in Gains Network <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

For those interested, Gains Network can be followed on Twitter and has a vibrant Discord community <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.