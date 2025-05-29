---
title: Use of Chainlink for realtime price feeds
videoId: UlzBJQoPlfY
---

From: [[goingonchain]] <br/> 

Gains Network, a synthetic exchange built for leveraged traders on the Polygon chain, utilizes Chainlink to address crucial concerns for traders, particularly regarding price accuracy and the prevention of "scam weeks" <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Addressing the "Scam Week" Problem

A significant concern for leverage traders is the "scam week," where an exchange might purposely create a price spike or drop to trigger stop losses, leading to massive buy or sell orders <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This phenomenon often occurs on centralized exchanges that support futures trading <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Gains Network tackles this issue by building a custom Decentralized Oracle Network (DON) enabled by Chainlink <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Custom Decentralized Oracle Network (DON)

The custom DON provided by Chainlink delivers real-time prices to traders <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### Price Aggregation Process
The process for executing an order on the platform involves several steps to ensure price accuracy:
1.  **Request Spot Price:** When an order needs execution, the trading contract requests the spot price from an aggregator contract <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
2.  **Eight On-Demand Chainlink Nodes:** The aggregator contract then requests the price from eight different on-demand Chainlink nodes <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
3.  **Median Price from Exchanges:** Each Chainlink node takes the median price from seven different exchange APIs <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
4.  **Return to Aggregator:** The result is then sent back to the aggregator contract <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
5.  **Comparison and Validation:** This aggregated price is compared with the main Chainlink price feed <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. If there is a difference greater than 1.5% from the main Chainlink price feed, the node's answer is rejected <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. The system then waits for the next valid answer before providing the price to the trading contract <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

This ensures that traders receive a real and fair spot price <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Benefits of Polygon Chain Integration
Because the platform is built on the Polygon chain, it benefits from cheap gas fees <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This allows the platform to make frequent calls, ensuring the best price reflection for traders <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
> [!info] Note
> Gains Network initially launched on the mainnet in January 2021 but transited to the [[effects_of_gas_fee_surge_on_layer_2_blockchain | Polygon chain]] due to high gas fees <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

This unique setup, combining a custom price feed with liquidity built on Polygon, enables a wide selection of assets for trading, including crypto and forex <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

> [!abstract] Roadmap
> Gains Network's roadmap includes a long list of tasks, such as adding more crypto assets, GNS single staking, and [[multichain_projects | multi-chain expansion]] <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. The concern remains that most liquidity is currently on the Ethereum mainnet, posing a potential liquidity challenge for growth on Polygon <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.