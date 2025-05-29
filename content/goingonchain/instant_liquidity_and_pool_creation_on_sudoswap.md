---
title: Instant liquidity and pool creation on Sudoswap
videoId: Ho0fqUXvFXk
---

From: [[goingonchain]] <br/> 

[[Introduction to Sudoswap and how it differs from traditional NFT marketplaces | Sudoswap]] is a new NFT marketplace that operates differently from traditional auction and order book-based platforms like OpenSea, LooksRare, or Minted <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It functions as an Automated Market Maker (AMM), similar to Uniswap, where NFT pricing curves are based on formulas <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This setup offers significant benefits, particularly in providing instant liquidity, but also presents challenges in its user interface <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Originally, [[Introduction to Sudoswap and how it differs from traditional NFT marketplaces | Sudoswap]] facilitated OTC (Over-the-Counter) swaps for NFTs, allowing two parties to negotiate a trade and create a swap contract <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The V2 release transformed it into a decentralized NFT marketplace <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Fully On-Chain AMM Model

Unlike order book marketplaces where listings are stored off-chain and transactions only go on-chain upon purchase or cancellation <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, [[Understanding Sudoswaps Automated Market Maker AMM model | Sudoswap]] operates fully on-chain <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. As an AMM, there are no order books; pricing is determined by formulas dependent on supply and demand <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This requires the presence of pools, akin to market makers or liquidity providers <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Instant Liquidity for Buying and Selling

[[Understanding Sudoswaps Automated Market Maker AMM model | Sudoswap]] achieves instant liquidity by enabling users to create pools <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Similar to how [[Providing liquidity through platforms | liquidity providers]] deposit two assets (e.g., ETH and 1inch) into a Uniswap pool to facilitate swaps and earn trading fees <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>, [[Providing liquidity through platforms | Sudoswap]] allows users to provide liquidity for NFTs <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

For example, for an NFT collection, there might be multiple liquidity providers ("Potato" collection used as an example, with around 9 pools available) ready to buy and sell <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

*   **Best Price (Buy)**: This represents the lowest current offering if you want to buy an NFT <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Best Offer (Sell)**: This is the price you can instantly receive if you sell your NFT into a pool <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This eliminates the waiting period common on order book marketplaces <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

Users can select specific NFTs to buy, similar to an e-commerce shopping cart <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. A "sweep mode" allows users to easily buy multiple NFTs at once from available pools <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Selling is equally instant; users can click on their NFTs and sell them directly into a pool <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## Becoming a Market Maker: Creating Pools

Users can create new pools on [[Introduction to Sudoswap and how it differs from traditional NFT marketplaces | Sudoswap]] with three distinct options <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>:

### 1. Buy NFT with Tokens (Buy Limit Order / DCA Pool)
This option allows users to set a buy limit order <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Setup**: Deposit ETH (or other tokens) and specify the desired buy price for an NFT (e.g., 0.6 ETH for one "Potato" NFT) <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Bonding Curve & Delta**: Users can choose a bonding curve (linear or exponential) and a "delta" value <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
    *   For a single NFT purchase, the bonding curve and delta don't significantly impact the initial limit order price <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   If buying multiple NFTs, the pool can function as a DCA (Dollar-Cost Averaging) pool <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. The delta determines how the buy price adjusts downwards each time the pool acquires an NFT (e.g., 0.1 ETH decrease per NFT purchased) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### 2. Sell NFT for Tokens (Sell Limit Order / DCA Pool)
This allows users to set a sell limit order for their NFTs <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Setup**: Deposit NFTs (e.g., "Potato") and specify the desired sell price to receive ETH <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Bonding Curve & Delta**: Similar to buy pools, for a single NFT sale, the bonding curve and delta are less critical <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
    *   For selling multiple NFTs, it can act as a DCA pool <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. The delta specifies how the sell price increases each time an NFT is sold from the pool (e.g., 0.1 ETH increase per NFT sold) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

### 3. Market Maker Pool (Both Buy & Sell)
This is the most dynamic option, allowing users to deposit both ETH and NFTs to facilitate trades and earn [[market_making_and_trading_fees_on_sudoswap | trading fees]] <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Setup**: Deposit both ETH and NFTs (e.g., "Potato") <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Trading Fees**: Define the percentage of [[market_making_and_trading_fees_on_sudoswap | trading fees]] you want to earn on each transaction (e.g., 2%) <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Initial Sell Price**: Set the starting price at which you want to sell your NFTs <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Bonding Curve & Delta**: Here, the bonding curve (linear or exponential) and delta are crucial <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>:
    *   **Linear Curve**: Uses a fixed price adjustment (e.g., 0.05 ETH).
        *   If someone sells into your pool (you buy), your offer price for subsequent NFTs goes down by the delta <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
        *   If someone buys from your pool (you sell), your selling price for subsequent NFTs goes up by the delta <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
    *   **Exponential Curve**: Uses a percentage-based adjustment (e.g., 30%).
        *   Your offer price goes down by a percentage after each purchase by your pool <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
        *   Your selling price adjusts upward by a percentage each time an NFT is sold from your pool <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
This feature is highly attractive for large NFT holders or traders who wish to act as market makers <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Fees and Royalties

A significant difference of [[Introduction to Sudoswap and how it differs from traditional NFT marketplaces | Sudoswap]] from traditional marketplaces is the absence of royalty fees for creators <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. While creators may dislike this, traders prefer it as they earn swap fees without paying royalties <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

*   **OpenSea**: Charges a platform fee of 2.5% and allows creators to set royalty fees up to 10% (e.g., 5% for "Otherdeed") <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   **[[Comparison of fees and royalties between Sudoswap and traditional marketplaces | Sudoswap]]**: Charges a platform fee of 0.5% (2% lower than OpenSea) and does not have royalty fees <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This can lead to lower floor prices on [[Introduction to Sudoswap and how it differs from traditional NFT marketplaces | Sudoswap]] due to reduced fees <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

However, a potential challenge for [[Introduction to Sudoswap and how it differs from traditional NFT marketplaces | Sudoswap]] is that if too few people set up pools, there will be less selection and limited movement in floor prices <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### Growing Traction
As of the recording, [[Introduction to Sudoswap and how it differs from traditional NFT marketplaces | Sudoswap]] has seen significant growth, with a total volume of approximately $20 million and around 12,000 users <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. The platform currently earns platform fees, but does not yet have its own token <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

> [!NOTE] Disclaimer
> This information is solely for educational purposes and should not be considered financial advice <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.