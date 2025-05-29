---
title: Gains Network Overview
videoId: UlzBJQoPlfY
---

From: [[goingonchain]] <br/> 

Gains Network is a platform featuring Gains Trade, a synthetic exchange designed for leveraged traders on the Polygon chain <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The platform aims to differentiate itself in the competitive leveraged trading space <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Key Features

Gains Network addresses several critical concerns for traders:

### Combating "Scam Weeks"

A common issue in leverage trading, particularly on centralized exchanges, is the "scam week" – a sudden, thin price spike or drop designed to trigger stop losses <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Gains Network tackles this by building a custom Decentralized Oracle Network (DON) powered by Chainlink <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

*   **Process:** When an order is executed, the trading contract requests a spot price from an aggregator contract <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The aggregator requests prices from eight different on-demand Chainlink nodes <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Each node takes the median price from seven different exchange APIs and sends the result back <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. If a node's answer deviates by more than 1.5% from the Chainlink price feed, it is rejected, and the platform waits for the next answer <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Benefits:** This system ensures traders receive a real and fair spot price <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Operating on Polygon also provides cheap gas fees, enabling frequent price updates for optimal reflection <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Addressing Low Liquidity

Gains Network uses its native GNS token to build liquidity for its synthetic trades <a class="yt-timestamp" data-t="00:01:58">[00:02:03]</a>. Synthetic trades mean there is no real spot asset being bought or sold <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

*   **Vaults:** The platform is supported by two vaults: the GNS DAI pool (acting as liquidity) and the trading vault <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Liquidity Mechanism ([[role_of_gns_tokens_in_gains_network|Role of GNS Tokens in Gains Network]]):**
    *   Traders deposit DAI into the trading vault when entering a trade and receive profits/losses from it upon exit <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
    *   The DAI trading vault is maintained at 110% over-collateralized <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   If the trading vault exceeds 110%, the excess DAI buys GNS from the liquidity pool, and the GNS is burned <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   If the trading vault falls below 100%, GNS is minted and sold for DAI to replenish the trading vault <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   This mechanism creates buying pressure on the GNS token when more traders are winning/losing, making GNS deflationary <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Statistics indicate that historically, more traders lose than win, contributing to GNS deflation <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Product Offerings

Gains Trade offers a wide selection of assets, including crypto and forex, with high leverage options up to 150x <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Fees and NFTs

*   **Fees:** Trading fees are 0.06% to 0.08% for maker and taker, with no funding fees <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. A small spread of approximately 0.025% is also present <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **NFT Utility:** Gains NFTs provide DeFi use cases, such as lowering spread fees, enabling bots for liquidation and limit orders, and boosting liquidity pool rewards <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Platform Details

### [[gains_network_tokenomics_and_statistics|Gains Network Tokenomics and Statistics]]

*   **Launch & Transition:** The platform launched in January 2021 on Ethereum Mainnet but transitioned to Polygon due to high gas fees <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. A 1:1000 split occurred, converting gPhantom tokens to GNS <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Supply:** The total supply of GNS is 38.5 million, with a maximum supply of 100 million <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. GNS is designed to be deflationary, with tokens burned as traders lose <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### Performance Statistics

*   **Fees Earned:** From inception, the platform has earned approximately $2.8 million in fees, with accelerated growth from December to February <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Trade Volume:** Accumulated trade volume has reached $5 billion <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **User Growth:** The number of users is steadily increasing <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   These metrics suggest the project may have achieved product-market fit <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Roadmap

Future plans include adding more crypto assets, GNS single staking, multi-chain expansion, and potentially a decentralized casino <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### Market Comparison

Gains Network's market cap is still relatively small compared to leaders like dYdX, but it aims to capture market share <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

## Platform Walkthrough

*   **GTrade Interface:** The platform allows users to choose between crypto and forex trading <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Trades can be initiated with as little as 35 DAI, with adjustable collateral and leverage up to 150x, alongside stop-loss and take-profit settings <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. The UI is simple and intuitive <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Testnet:** A "Tech Core Practice" feature on the Polygon testnet allows users to practice trading skills before live trading <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **Staking:** Users can contribute liquidity to the GNS DAI pool and the trading vault <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. The trading vault offers around 10% APY, while the liquidity pool offers approximately 47% APY <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. The GNS token currently has a deflationary inflation rate of -25% <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Statistics:** Detailed platform performance and statistics are available on Dune Analytics via the "Statistic" section <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

## Insights and [[challenges_and_opportunities_for_gains_network|Challenges and Opportunities for Gains Network]]

*   **Strengths:**
    *   Innovative use of its own token for liquidity, promoting deflation <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   Simple user interface <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   NFTs offer valuable features for traders, including trading bot setup <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
    *   Business statistics indicate strong product-market fit with increasing users, trade volume, and fee earnings <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Concerns:**
    *   A significant portion of liquidity currently resides on the Ethereum Mainnet <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   Multi-chain expansion could significantly increase liquidity and user base <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## Community

Gains Network maintains an active presence on Twitter and has a vibrant Discord community <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.