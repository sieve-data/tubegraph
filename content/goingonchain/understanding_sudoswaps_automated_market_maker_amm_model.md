---
title: Understanding Sudoswaps Automated Market Maker AMM model
videoId: Ho0fqUXvFXk
---

From: [[goingonchain]] <br/> 

[[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] is a new NFT marketplace that operates differently from traditional platforms like OpenSea, LooksRare, or Minted, which are based on auctions and order books <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] is an [[how_amm_automated_market_maker_works | AMM]], similar to UniSwap but for NFTs <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Its pricing curves are based on formulas <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, which introduces interesting benefits but also challenges for the user interface due to different buying and selling processes <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Historically, [[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] facilitated OTC (Over-the-Counter) swaps for NFTs, where users could create a swap contract for negotiated trades <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The recently released V2 transformed it into a decentralized NFT marketplace <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Fully On-Chain AMM

Unlike traditional order book marketplaces where listings are stored off-chain and transactions only go on-chain upon purchase or cancellation <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>, [[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]]'s [[how_amm_automated_market_maker_works | AMM]] model means everything is on-chain <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. There are no order books; pricing is determined by formulas and dependent on supply and demand <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. For [[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] to operate, there must be liquidity pools, similar to [[how_amm_automated_market_maker_works | market makers]] or liquidity providers <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## [[instant_liquidity_and_pool_creation_on_sudoswap | Instant Liquidity]] for Buying and Selling

[[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] achieves [[instant_liquidity_and_pool_creation_on_sudoswap | instant liquidity]] by allowing users to create pools <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Just as a UniSwap requires a [[how_amm_automated_market_maker_works | market maker]] to facilitate swaps (e.g., ETH to 1INCH), where liquidity providers deposit two assets into a pool and earn a cut of the [[market_making_and_trading_fees_on_sudoswap | trading fees]] <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>, [[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] functions similarly <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Users can create pools for specific NFT collections, providing instant liquidity for others to buy and sell <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The platform displays the current lowest offering price (full price) and the best offer price if you want to sell <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This means users don't need to wait for a buyer or seller, allowing immediate transactions <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The "offer TVL" shows the total amount of ETH in all pools waiting to buy NFTs <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

*   **Buying:** Users can select individual NFTs or use "sweep mode" to buy multiple NFTs at the floor price <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Selling:** Users can instantly sell their NFTs into a pool <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Becoming a [[how_amm_automated_market_maker_works | Market Maker]]: Pool Options

When creating a new pool on [[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]], there are three options <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>:

1.  **Buy NFT with tokens:** This functions as a buying limit order <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. You deposit ETH and set a target buy price <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. If only buying one NFT, the chosen [[amm_changes_and_pool_types_in_spiritswap_v2 | bonding curve]] (linear or exponential) and delta don't significantly matter <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. However, if buying multiple NFTs (e.g., 5), the delta value becomes important as the buy price will adjust downwards with each subsequent purchase, acting as a DCA (Dollar-Cost Averaging) pool <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
2.  **Sell NFT for tokens:** This acts as a sell limit order <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. You specify the price at which you want to sell your NFT <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Similar to buying, if selling only one NFT, the curve and delta don't heavily impact the immediate sell price <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. If selling multiple NFTs (e.g., 10), you can set the price to increase with each sale (e.g., by 0.1 ETH), also functioning as a DCA pool <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
3.  **Both (Market Maker Pool):** This is the most notable option <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Users can deposit both ETH and NFTs to become a liquidity provider, earning [[market_making_and_trading_fees_on_sudoswap | trading fees]] <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. You set a [[market_making_and_trading_fees_on_sudoswap | trading fee]] percentage (e.g., 2%) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a> and a starting sell price for your NFTs <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
    *   **[[amm_changes_and_pool_types_in_spiritswap_v2 | Bonding Curves]]:**
        *   **Linear Curve:** Uses a fixed price adjustment (e.g., 0.1 ETH) for each transaction <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. If someone sells into your pool, your offer price goes down by a fixed amount per purchase; if someone buys from your pool, your selling price goes up by a fixed amount <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
        *   **Exponential Curve:** Uses a variable, percentage-based adjustment (e.g., 10% or 30%) <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. The offer price decreases or increases by a set percentage after each purchase or sale, allowing for dynamic pricing adjustments <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

This [[how_amm_automated_market_maker_works | market maker]] pool allows NFT whales or traders to create their own liquidity, earning fees <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

## [[comparison_of_fees_and_royalties_between_sudoswap_and_traditional_marketplaces | Fees and Royalties]]

[[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] has no royalty fees for creators <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. This is favored by traders, who earn the swap fee without paying royalties <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

*   **OpenSea:** Charges a 2.5% platform fee and allows creators to set royalty fees up to 10% (e.g., 5% for 'Otherdeed') <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **[[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]]:** Charges a platform fee of 0.5% (2% lower than OpenSea) and does not have royalty fees <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

The absence of royalty fees on [[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] can lead to lower floor prices compared to OpenSea <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. However, a challenge for [[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] is that if few people set up pools, there will be less selection and limited price movement <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

## Traction

As of the video, [[introduction_to_sudoswap_and_how_it_differs_from_traditional_nft_marketplaces | Sudoswap]] has approximately $20 million in total volume and about 12,000 users <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. The platform earns platform fees, but currently does not have its own token <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.