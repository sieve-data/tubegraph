---
title: Gains Network overview and platform features
videoId: UlzBJQoPlfY
---

From: [[goingonchain]] <br/> 

Gains Network offers a product called [[gains_trade_synthetic_exchange_and_leverage_trading | Gains Trade]], a synthetic exchange designed for leveraged traders on the Polygon chain <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. It aims to differentiate itself from other platforms by addressing common concerns in leverage trading <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Key Features for Traders

### Custom DON for Price Accuracy
One significant concern for traders is "scam wicks," where exchanges manipulate prices to trigger stop losses, a common issue on centralized exchanges that support futures trading <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Gains Network addresses this by building a custom Decentralized Oracle Network (DON) enabled by Chainlink <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

How the Custom DON Works:
*   When an order needs to be executed, the trading contract requests the spot price from an aggregator contract <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   The aggregator requests prices from eight different on-demand Chainlink nodes <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Each Chainlink node takes the median price from seven different exchange APIs <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   The result is sent back to the aggregator contract, which compares it with the Chainlink price feed <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   If there's a difference of more than 1.5% from the Chainlink price feed, the node's answer is rejected, and it waits for another answer <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   This process ensures traders receive a real and fair spot price <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. The platform's operation on the Polygon chain also allows for cheap gas fees, enabling frequent price updates <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Liquidity Solution with GNS Token
To solve the problem of low liquidity, Gains Network uses its [[gns_token_and_its_role_in_liquidity_and_tokenomics | GNS token]] to build up liquidity <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Trades and leverage on Gains are synthetic, meaning no real assets are bought or sold <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The platform is supported by two pools: the GNS DAI pool (for liquidity) and the trading pool <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

*   When entering a trade, users deposit DAI into the trading pool, and profits or losses are settled from this pool <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   The DAI trading pool is maintained at 110% over-collateralized <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   If the trading pool exceeds 110%, the excess DAI is used to buy GNS from the liquidity pool, and the GNS is burned <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   If the trading pool falls below 100%, GNS is minted and sold for DAI to top up the trading pool <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   This mechanism creates buying pressure on the [[gns_token_and_its_role_in_liquidity_and_tokenomics | GNS token]] if more traders are winning, making it deflationary <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Historically, more traders have lost than won, contributing to [[gns_token_and_its_role_in_liquidity_and_tokenomics | GNS token]] deflation <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Asset Selection and Leverage
With its unique custom price feed and liquidity model built on Polygon, Gains Network offers a wide selection of assets, including crypto and forex, and allows for high leverage up to 150x <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Fees and NFT Integration
Trading fees range from 0.06% to 0.08% for maker and taker, with no funding fees <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. A small spread, typically around 0.025%, should also be accounted for <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

Gains Network integrates [[nft_features_and_defi_use_cases_on_gains_network | NFTs]] (Non-Fungible Tokens) into its platform <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Owning a Gains NFT provides [[nft_features_and_defi_use_cases_on_gains_network | DeFi use cases]] <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>:
*   Lowering spread fees <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   The ability to run a bot for executing liquidations and limit orders <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   Boosting liquidity pool rewards <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Tokenomics and Statistics
The platform launched in January 2021 on the Ethereum mainnet but transitioned to the Polygon chain due to high gas fees <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. A 1:1000 split occurred, meaning one GPhantom token became 1000 [[gns_token_and_its_role_in_liquidity_and_tokenomics | GNS tokens]] <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

*   Current [[gns_token_and_its_role_in_liquidity_and_tokenomics | GNS]] total supply: 38.5 million <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   Maximum supply: 100 million <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   [[gns_token_and_its_role_in_liquidity_and_tokenomics | GNS]] is designed to be deflationary, with tokens burned as traders lose <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   From inception, the platform has earned approximately $2.8 million in fees, with accelerated growth from December last year to February this year <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   Accumulated trade volume since launch: $5 billion <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   The platform has a growing number of users <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. These metrics suggest the project may have found a product-market fit <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   The current [[gns_token_and_its_role_in_liquidity_and_tokenomics | GNS token]] inflation rate is deflationary at -25% <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Roadmap
The roadmap includes adding more crypto assets, [[gns_token_and_its_role_in_liquidity_and_tokenomics | GNS]] single-staking, multi-chain expansion, and plans for a decentralized casino <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

## Platform Walkthrough
The [[gains_trade_synthetic_exchange_and_leverage_trading | GTrade]] platform offers a simple UI where users can choose to trade crypto or forex <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   Trades can start with as little as 35 DAI <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   Users set collateral, leverage (up to 150x), stop loss, and take profit levels <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   A "tech core practice" option is available on the Polygon testnet to try out trading skills before going live <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   For those interested in providing liquidity, staking options allow contributions to the [[gns_token_and_its_role_in_liquidity_and_tokenomics | GNS]] DAI pool and the trading pool <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   The trading pool currently offers a 10% APY, and the liquidity pool offers 47% APY <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   Platform performance and statistics can be viewed on Dune Analytics <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

## Key Insights and Concerns
The model of using its own token to provide liquidity is seen as beneficial for onboarding more assets and contributing to deflation <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. The UI is simple, and the inclusion of [[nft_features_and_defi_use_cases_on_gains_network | NFTs]] provides additional features for traders, including the ability to set up trading bots <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Increasing user base, trade volume, and fee earnings indicate a strong product-market fit <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

A primary concern is that most liquidity is still on the Ethereum mainnet <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>, which could pose a liquidity challenge for the Polygon-based platform. However, multi-chain expansion could help attract more liquidity <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.