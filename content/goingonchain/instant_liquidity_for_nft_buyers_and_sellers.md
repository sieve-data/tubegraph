---
title: Instant liquidity for NFT buyers and sellers
videoId: Ho0fqUXvFXk
---

From: [[goingonchain]] <br/> 

SudoSwap is an NFT marketplace that operates using an Automated Market Maker (AMM) model, similar to Uniswap, but for NFTs <a class="yt-timestamp" data-t="00:1:17">[01:17]</a> <a class="yt-timestamp" data-t="00:02:05">[02:05]</a>. This approach allows for [[impact_of_liquidity_pools_on_stablecoins | instant liquidity]] for both buying and selling NFTs, a significant departure from traditional auction and order book-based marketplaces like OpenSea, LooksRare, or Minted <a class="yt-timestamp" data-t="00:00:11">[00:11]</a> <a class="yt-timestamp" data-t="00:02:26">[02:26]</a>.

## How SudoSwap Provides Instant Liquidity

Unlike order book marketplaces where listings are stored off-chain and transactions only go on-chain upon purchase or cancellation, SudoSwap's AMM model means everything is on-chain <a class="yt-timestamp" data-t="00:01:39">[01:39]</a> <a class="yt-timestamp" data-t="00:02:03">[02:03]</a>. Pricing is powered by formulas based on supply and demand within liquidity pools <a class="yt-timestamp" data-t="00:02:14">[02:14]</a> <a class="yt-timestamp" data-t="00:00:23">[00:23]</a>.

For SudoSwap to function, there must be pools created by market makers or [[liquidity_providers_and_incentives | liquidity providers]] <a class="yt-timestamp" data-t="00:02:20">[02:20]</a> <a class="yt-timestamp" data-t="00:02:24">[02:24]</a>. These providers deposit both ETH (or other tokens) and NFTs into a pool <a class="yt-timestamp" data-t="00:07:05">[07:05]</a>.

### Instant Buying and Selling for Users

Users can immediately buy or sell NFTs from these existing pools without waiting for an individual buyer or seller to match their price, unlike OpenSea <a class="yt-timestamp" data-t="00:03:26">[03:26]</a> <a class="yt-timestamp" data-t="00:04:11">[04:11]</a>.

*   **Buying**: The "floor price" represents the lowest offering currently available in a pool <a class="yt-timestamp" data-t="00:03:09">[03:09]</a>. Users can select NFTs they like and add them to a shopping cart, similar to e-commerce <a class="yt-timestamp" data-t="00:03:40">[03:40]</a> <a class="yt-timestamp" data-t="00:03:47">[03:47]</a>. A "sweep mode" allows purchasing multiple NFTs from the floor instantly <a class="yt-timestamp" data-t="00:03:52">[03:52]</a>.
*   **Selling**: The "best offer" is the price a user will receive if they sell an NFT directly into a pool <a class="yt-timestamp" data-t="00:03:18">[03:18]</a>. Users can sell their NFTs instantly into a pool, receiving funds immediately <a class="yt-timestamp" data-t="00:04:03">[04:03]</a> <a class="yt-timestamp" data-t="00:04:11">[04:11]</a>.

## Becoming a Market Maker

Users can create their own pools, effectively becoming a market maker, with three options <a class="yt-timestamp" data-t="00:04:20">[04:20]</a>:

1.  **Buy NFT with tokens**: This functions like a buying limit order <a class="yt-timestamp" data-t="00:04:30">[04:30]</a>. A user deposits ETH and sets a target buy price for an NFT <a class="yt-timestamp" data-t="00:04:51">[04:51]</a>.
    *   **Single NFT**: If only buying one NFT, the chosen bonding curve (linear or exponential) and delta value do not significantly affect the initial limit order <a class="yt-timestamp" data-t="00:05:01">[05:01]</a>. The pool will be triggered when the NFT price drops to the set limit <a class="yt-timestamp" data-t="00:05:23">[05:23]</a>.
    *   **DCA Pool**: For buying multiple NFTs (e.g., 5), the pool can act as a dollar-cost averaging (DCA) tool. The buy price adjusts downwards by a set delta each time the pool acquires an NFT <a class="yt-timestamp" data-t="00:05:34">[05:34]</a>.
2.  **Sell NFT with tokens**: This functions like a selling limit order <a class="yt-timestamp" data-t="00:04:36">[04:36]</a>. A user deposits their NFT(s) and sets a target sell price <a class="yt-timestamp" data-t="00:06:01">[06:01]</a>.
    *   **Single NFT**: For selling one NFT, the bonding curve and delta do not significantly affect the initial limit order <a class="yt-timestamp" data-t="00:06:14">[06:14]</a>.
    *   **DCA Pool**: For selling multiple NFTs (e.g., 10), the pool can act as a DCA tool for selling. The sell price can be set to increase by a delta after each NFT is sold <a class="yt-timestamp" data-t="00:06:29">[06:29]</a>.
3.  **Do both (Market Maker Pool)**: This option allows users to deposit both ETH and NFTs into a pool <a class="yt-timestamp" data-t="00:07:03">[07:03]</a>. This makes them a [[liquidity_providers_and_incentives | liquidity provider]] and allows them to earn trading fees <a class="yt-timestamp" data-t="00:04:38">[04:38]</a> <a class="yt-timestamp" data-t="00:07:16">[07:16]</a>.
    *   **Trading Fees**: Users set the percentage of trading fees they wish to earn per trade <a class="yt-timestamp" data-t="00:07:21">[07:21]</a>.
    *   **Bonding Curves**:
        *   **Linear Curve**: Prices adjust by a fixed amount (in ETH) each time an NFT is bought or sold from the pool <a class="yt-timestamp" data-t="00:07:38">[07:38]</a> <a class="yt-timestamp" data-t="00:07:50">[07:50]</a>.
        *   **Exponential Curve**: Prices adjust by a variable percentage <a class="yt-timestamp" data-t="00:07:41">[07:41]</a> <a class="yt-timestamp" data-t="00:07:45">[07:45]</a>. For example, a 30% delta means the buy price adjusts downwards by 30% after each purchase, and the sell price adjusts upwards by 30% after each sale <a class="yt-timestamp" data-t="00:08:41">[08:41]</a>.

This market maker model is particularly attractive for NFT whales or traders who hold multiple NFTs of the same collection <a class="yt-timestamp" data-t="00:09:00">[09:00]</a>.

## Fee Structure and Impact

SudoSwap charges a platform fee of 0.5%, which is significantly lower than OpenSea's 2.5% platform fee <a class="yt-timestamp" data-t="00:09:22">[09:22]</a> <a class="yt-timestamp" data-t="00:09:38">[09:38]</a>. Additionally, SudoSwap does not impose royalty fees for creators <a class="yt-timestamp" data-t="00:09:11">[09:11]</a> <a class="yt-timestamp" data-t="00:09:44">[09:44]</a>. While creators may not favor this, traders benefit by avoiding royalty fees when setting up pools and earning swap fees <a class="yt-timestamp" data-t="00:09:16">[09:16]</a>.

This fee structure can sometimes result in a lower floor price for NFTs on SudoSwap compared to OpenSea <a class="yt-timestamp" data-t="00:10:06">[10:06]</a>.

## Considerations

Despite the benefits of instant liquidity, the effectiveness of SudoSwap relies on active participation from [[liquidity_providers_and_incentives | liquidity providers]] <a class="yt-timestamp" data-t="00:10:18">[10:18]</a>. If there are few people setting up pools, selection may be limited, and the floor price might not move much <a class="yt-timestamp" data-t="00:10:20">[10:20]</a>.