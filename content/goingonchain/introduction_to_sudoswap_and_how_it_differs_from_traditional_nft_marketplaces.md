---
title: Introduction to Sudoswap and how it differs from traditional NFT marketplaces
videoId: Ho0fqUXvFXk
---

From: [[goingonchain]] <br/> 

Sudoswap is a new NFT marketplace that operates differently from traditional platforms like OpenSea, LooksRare, and Minted <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Unlike auction and order book-based marketplaces, Sudoswap is an Automated Market Maker (AMM) <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a> <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Its pricing curves are based on formulas, similar to [[understanding_sudoswaps_automated_market_maker_amm_model | Uniswap]] but adapted for NFTs <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a> <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. This setup brings specific benefits, though it also presents [[user_interface_changes_in_spiritswap_v2 | UI challenges]] due to a different buying and selling process <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a> <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## History and Evolution

Sudoswap has been in operation for an extended period, initially facilitating over-the-counter (OTC) swaps for NFTs <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a> <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. In this prior model, users could negotiate a trade for an NFT (e.g., swapping a Moonbird for an ETH brick) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Once negotiated, a swap contract would be created on Sudoswap, and the transaction would proceed upon acceptance by both parties <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a> <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Recently, Sudoswap released V2, transforming it into the decentralized NFT marketplace it is known as today <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a> <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Key Differences from Traditional Marketplaces

### Fully On-Chain vs. Off-Chain Order Books

Traditional NFT marketplaces like OpenSea operate with off-chain order books <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a> <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. When a user lists an NFT, they sign a transaction that goes into an off-chain order book <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This listing then appears on the front-end of the website <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The transaction is only recorded on-chain when the order is fulfilled (i.e., someone buys or the listing is canceled) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

In contrast, Sudoswap is a fully on-chain AMM <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Everything occurs on-chain, eliminating the need for an order book <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a> <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a> <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Its pricing is determined by formulas and influenced by supply and demand within liquidity pools <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a> <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### [[instant_liquidity_and_pool_creation_on_sudoswap | Instant Liquidity and Market Making]]

Sudoswap requires the presence of pools, which are maintained by [[market_making_and_trading_fees_on_sudoswap | market makers]] or liquidity providers <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a> <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This system allows for instant liquidity for both buying and selling NFTs <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a> <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

*   **Buying:** Users can immediately purchase an NFT at the lowest available price (the "floor price") from an existing pool <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a> <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a> <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Selling:** Similarly, users can instantly sell an NFT into a pool at the best offer price, without needing to wait for a buyer or queue their price like on OpenSea <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a> <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a> <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a> <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a> <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a> <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

Users can also create their own pools, acting as [[market_making_and_trading_fees_on_sudoswap | market makers]] to buy NFTs with tokens, sell NFTs for tokens, or do both simultaneously <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a> <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a> <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a> <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a> <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. Creating a pool allows users to earn trading fees, similar to a liquidity provider in a token swap pool <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a> <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a> <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a> <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. These pools can be configured with linear or exponential bonding curves, which dictate how the buy/sell price adjusts as NFTs are traded <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a> <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a> <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a> <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### [[comparison_of_fees_and_royalties_between_sudoswap_and_traditional_marketplaces | Fees and Royalties]]

One significant difference lies in the fee structure:

*   **Sudoswap:** Charges a platform fee of 0.5% and has no royalty fees <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a> <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a> <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a> <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. This makes it attractive to traders who earn swap fees without incurring royalty costs <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a> <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **OpenSea:** Charges a platform fee of 2.5%, and creators can set a royalty fee of up to 10% <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a> <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a> <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a> <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

The absence of royalty fees on Sudoswap means creators do not earn passive income from secondary sales, which they might dislike <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. However, the lower platform fees and no royalties can lead to a lower floor price for NFTs on Sudoswap compared to OpenSea <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a> <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a> <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

## Current Traction

As of the transcript, Sudoswap's total volume was approximately $20 million with about 12,000 users <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a> <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a> <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. The platform has not yet released its own token <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.