---
title: Market making and trading fees on Sudoswap
videoId: Ho0fqUXvFXk
---

From: [[goingonchain]] <br/> 

[[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] is a new NFT marketplace that operates differently from traditional platforms like OpenSea, LooksRare, or Minted, which are based on auctions and order books <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. [[understanding_sudoswaps_automated_market_maker_amm_model | Sudoswap]] is an Automated Market Maker (AMM) for NFTs, similar to Uniswap for tokens, where pricing curves are based on formulas <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This setup brings both benefits and challenges to the user interface <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Fully On-Chain Operations

Unlike traditional order book marketplaces where listings are signed off-chain and stored in an off-chain order book until a purchase is made <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, Sudoswap is an AMM where everything is on-chain <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. There are no order books; pricing is determined by formulas dependent on supply and demand <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. For Sudoswap to function, liquidity pools must exist, involving market makers or liquidity providers <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## [[instant_liquidity_and_pool_creation_on_sudoswap | Instant Liquidity and Pool Creation]]

Sudoswap provides [[instant_liquidity_and_pool_creation_on_sudoswap | instant liquidity for buying and selling]] NFTs <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Similar to Uniswap, where liquidity providers supply two assets (e.g., ETH and 1inch) into a pool to facilitate swaps and earn trading fees <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, Sudoswap operates on the same principle for NFTs <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

Users can create pools, which provide the instant liquidity for others to buy and sell <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Floor Price (Lowest Offering)**: This is the cheapest price at which you can buy an NFT from a pool <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Best Offer (Selling Price)**: This is the price you receive if you sell your NFT directly into a pool <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This means you don't need to wait or queue for your price like on OpenSea <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Sweep Mode**: For buying, users can select a "sweep mode" to buy multiple NFTs by choosing a quantity (e.g., seven) <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## Becoming a Market Maker

Users can become market makers by creating new pools with three main options <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>:

### 1. Buy NFT with Tokens (Buy Limit Order)
This option allows users to set a buy limit order <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Setting a Price**: You deposit tokens (e.g., ETH) and specify a price at which you want to buy an NFT (e.g., 0.6 ETH for a "potato") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Bonding Curve and Delta**: If buying only one NFT, the chosen bonding curve (linear or exponential) and delta value don't significantly affect the single purchase price <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The pool acts as a limit order, triggered when the NFT price reaches your set price <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **DCA Pool**: By changing the quantity of NFTs to buy (e.g., 5), the "delta" becomes relevant <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Each time the pool buys an NFT, the buying price adjusts downwards by the set delta (e.g., 0.1), functioning like a Dollar-Cost Averaging (DCA) pool <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### 2. Sell NFT with Tokens (Sell Limit Order)
This option functions as a sell limit order <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Setting a Price**: You deposit NFTs (e.g., "potato") and set a price at which you want to sell them (e.g., 1.2 ETH) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Bonding Curve and Delta**: Similar to buying, if selling only one NFT, the bonding curve and delta don't matter as much <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It sets a straightforward limit order <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **DCA Pool**: If selling multiple NFTs (e.g., 10 "potatoes"), the delta can be used to increase the selling price for each subsequent NFT sold <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. For example, an increase of 0.1 ETH per NFT would result in selling the first at 1.2 ETH, the second at 1.3 ETH, and so on <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

### 3. Market Maker Pool (Both Buy and Sell)
This is considered the most interesting option, allowing users to deposit both ETH and NFTs to create a pool <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Earning Trading Fees**: As a liquidity provider, you earn trading fees when trades occur within your pool <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. You set the percentage of the trading fee you want to make per trade (e.g., 2%) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Bonding Curves**:
    *   **Linear Curve**: Uses a fixed price adjustment (e.g., 0.05 ETH) <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. If someone sells into your pool, your offer price decreases by the fixed delta with each purchase <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. If someone buys from your pool, your selling price increases by the fixed delta with each sale <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
    *   **Exponential Curve**: Uses a variable, percentage-based adjustment (e.g., 10% or 30%) <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. The offer price decreases or selling price increases by a set percentage with each trade <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. This is particularly useful for NFT whales or traders who want to manage a collection of NFTs <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

## [[comparison_of_fees_and_royalties_between_sudoswap_and_traditional_marketplaces | Trading Fees and Royalties]]

Sudoswap has a distinct fee structure compared to traditional marketplaces:
*   **Sudoswap Fees**:
    *   **Platform Fee**: 0.5% <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
    *   **Royalty Fees**: None <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. This means creators do not receive royalty payments on Sudoswap trades <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Comparison to OpenSea**:
    *   **Platform Fee**: OpenSea charges a 2.5% platform fee <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Sudoswap's fee is 2% lower <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
    *   **Royalty Fees**: OpenSea allows creators to set royalty fees up to 10% (e.g., 5% for "otherdeed" NFTs) <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Sudoswap does not have royalty fees <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

This absence of royalty fees is why creators may dislike Sudoswap, as they miss out on potential earnings (e.g., 6.45k from a 72 ETH Bored Ape Yacht Club sale at 5% royalty) <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. However, traders prefer it because they earn the swap fee when setting up a pool and avoid royalty payments <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. The reduction in platform fees and absence of royalties can lead to lower floor prices on Sudoswap compared to OpenSea <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### Challenges
A potential challenge for Sudoswap is that if too few people set up pools, there will be less selection for buyers, and floor prices may not move significantly <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

## Growing Traction

Sudoswap has shown growing traction, with a total volume of approximately $20 million and around 12,000 users <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. The platform has also earned a notable amount in total platform fees <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.