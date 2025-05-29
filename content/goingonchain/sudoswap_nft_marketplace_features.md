---
title: Sudoswap NFT marketplace features
videoId: Ho0fqUXvFXk
---

From: [[goingonchain]] <br/> 

Sudoswap is an NFT marketplace that operates distinctly from conventional platforms like OpenSea, LooksRare, and Minted, which are based on auctions and order books <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Instead, Sudoswap functions as an [[amm_mechanism_in_sudoswap | AMM]] (Automated Market Maker), akin to [[Uniswap swap fees | Uniswap]], but for NFTs <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Its pricing curves are determined by formulas, which offers unique benefits while also presenting different UI challenges for buying and selling <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## History
Sudoswap has been in operation for a significant period, originally facilitating OTC (over-the-counter) swaps for NFTs. For instance, users could arrange a trade for an NFT like Moonbird for Bric, then utilize Sudoswap to create a swap contract for both parties to accept <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The decentralized NFT marketplace known today was released as Sudoswap V2 <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Key Features

### Fully On-Chain Operation
Unlike traditional order book marketplaces where listings are stored off-chain until a transaction occurs, Sudoswap operates entirely on-chain <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. As an [[amm_mechanism_in_sudoswap | AMM]], there is no order book; pricing is algorithmically determined by supply and demand <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### [[instant_liquidity_for_nft_buyers_and_sellers | Instant Liquidity]]
Sudoswap provides [[instant_liquidity_for_nft_buyers_and_sellers | instant liquidity]] for NFT buying and selling, eliminating the need to wait for orders to be filled, unlike OpenSea <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This is achieved through liquidity pools, where users can create pools, effectively acting as market makers or liquidity providers <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Pool Buy Price**: The lowest offering price for an NFT <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Pool Offer Price**: The price at which you can immediately sell an NFT into a pool <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Offer TVL**: The total amount of ETH in all pools waiting to buy your NFTs <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
Users can buy multiple NFTs using a "sweep mode" to sweep the floor <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Selling is also immediate; users can select their NFT and sell directly into a pool <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### [[market_making_and_buyingselling_strategies_on_sudoswap | Market Making and Buying/Selling Strategies]]
Sudoswap allows users to create different types of pools to facilitate [[market_making_and_buyingselling_strategies_on_sudoswap | buying and selling strategies]]:

1.  **Buy NFT with Tokens**:
    *   Acts as a buying limit order <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Users deposit ETH and specify a desired buy price for an NFT <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   Can be configured as a DCA (Dollar-Cost Averaging) pool, where the buy price adjusts downwards by a specified delta after each purchase <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

2.  **Sell NFT with Tokens**:
    *   Acts as a selling limit order <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   Users deposit NFTs and specify a desired sell price to receive ETH <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
    *   Can also be configured as a DCA pool, where the sell price adjusts upwards by a specified delta after each sale <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

3.  **Market Maker Pool (Both Buy and Sell)**:
    *   Allows users to deposit both ETH and NFTs, acting as a liquidity provider <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   Users earn trading fees from transactions within their pool <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
    *   **Bonding Curves**: Determine how prices adjust as NFTs are bought or sold from the pool <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>:
        *   **Linear Curve**: Uses a fixed price adjustment (e.g., 0.1 ETH) <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
        *   **Exponential Curve**: Uses a variable, percentage-based adjustment (e.g., 10%) <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    *   This feature is particularly beneficial for NFT whales or traders who want to provide liquidity and earn fees <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

### No Royalty Fees
Sudoswap charges a platform fee of 0.5%, which is lower than OpenSea's 2.5% <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. Additionally, Sudoswap does not enforce royalty fees for creators <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. While this is less favorable for creators who rely on royalties, it is attractive to traders and market makers who benefit from lower costs and can earn swap fees without paying royalties <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This can lead to lower floor prices on Sudoswap compared to OpenSea <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## Challenges
A potential drawback is that if few people set up pools, there will be less selection of NFTs, and floor prices may not move significantly <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

## Traction
As of the video's recording, Sudoswap has a total volume of approximately $20 million and around 12,000 users <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. The platform does not currently have its own token, leading to speculation about potential future airdrops <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.