---
title: AMM mechanism in Sudoswap
videoId: Ho0fqUXvFXk
---

From: [[goingonchain]] <br/> 

Sudoswap is a decentralized NFT marketplace that operates using an Automated Market Maker (AMM) model, which differs significantly from traditional auction and order book-based marketplaces like OpenSea, LooksRare, or Minted <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It functions similarly to [[Uniswap swap fees | Uniswap]], but for NFTs, with pricing curves based on mathematical formulas <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## How Sudoswap Works

### Fully On-Chain Operations
Unlike traditional NFT marketplaces where listings are often stored off-chain in an order book and only move on-chain upon purchase or cancellation, Sudoswap is entirely on-chain <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. As an AMM, it eliminates the need for an order book, with pricing dynamically determined by formulas and influenced by supply and demand <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Instant Liquidity
To facilitate transactions, Sudoswap requires liquidity pools, similar to how market makers or liquidity providers operate on a platform like [[Uniswap swap fees | Uniswap]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>, <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Users can create these pools, providing instant liquidity for buying and selling NFTs <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>, <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This means that if you want to sell an NFT, you can do so immediately into a pool without waiting for a specific buyer or price queue <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>, <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Becoming a Market Maker (Creating a Pool)
Sudoswap offers three main options for users to create a pool and act as a market maker <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>, <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>:

#### 1. Buy NFT with Tokens
This option functions as a buying limit order <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   You deposit a token (e.g., ETH) to buy NFTs <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   You set a target buy price <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   You can configure the pool as a Dollar-Cost Averaging (DCA) pool by setting a quantity greater than one and a "delta" value <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>, <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Each time the pool buys an NFT, the buy price adjusts downwards by the specified delta <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>, <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

#### 2. Sell NFT with Tokens
This option acts as a selling limit order <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   You deposit your NFTs (e.g., Potato) and aim to receive tokens (e.g., ETH) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   You set a target sell price <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   Similar to buying, you can set it as a DCA pool, where the sell price increases by a set delta each time an NFT is sold from the pool <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>, <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

#### 3. Both (Liquidity Provider)
This is the most common way to become a market maker, allowing you to both buy and sell NFTs and earn trading fees <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>, <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>, <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   You deposit both tokens (e.g., ETH) and NFTs into the pool <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   You set a trading fee percentage that you wish to earn on each trade <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>, <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   You define a starting sell price for your NFTs <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Bonding Curves**: The price adjustments for buying and selling within the pool are determined by the chosen bonding curve and a "delta" value <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>, <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>:
    *   **Linear Curve**: Uses a fixed price adjustment (e.g., 0.1 ETH). Each time an NFT is bought or sold, the price adjusts by a fixed amount <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>, <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>, <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
    *   **Exponential Curve**: Uses a variable, percentage-based adjustment (e.g., 10%). The price adjusts by a percentage of the current price with each transaction <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>, <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>, <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>, <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

This flexibility allows NFT holders, particularly "whales" or active traders, to establish pools and function as market makers for their collections <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>, <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## Fees and Royalties
Sudoswap charges a platform fee of 0.5%, which is lower than OpenSea's 2.5% <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>, <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. Crucially, Sudoswap has **no royalty fees** for creators <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>, <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. While creators may not favor this, traders appreciate it as they receive the full swap fee without royalty deductions <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>, <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>, <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This fee structure can lead to lower floor prices on Sudoswap compared to platforms with royalties <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## Growing Traction
Sudoswap has shown growing adoption, with a total volume of approximately $20 million and around 12,000 users <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>, <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. As of the transcript, Sudoswap does not yet have its own token <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.