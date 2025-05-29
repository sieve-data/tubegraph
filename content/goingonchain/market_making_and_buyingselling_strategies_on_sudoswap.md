---
title: Market making and buyingselling strategies on Sudoswap
videoId: Ho0fqUXvFXk
---

From: [[goingonchain]] <br/> 

Sudoswap is a decentralized NFT marketplace that operates differently from traditional auction and order book-based platforms like OpenSea [00:00:09]. It functions as an [[amm_mechanism_in_sudoswap | AMM mechanism in Sudoswap]], similar to [[safe_token_purchasing_on_uniswap | Uniswap]], where pricing curves are determined by formulas [00:00:18]. This setup offers benefits but also presents unique challenges to its user interface [00:00:29].

Sudoswap V2 launched as a decentralized NFT marketplace, evolving from its earlier function of OTC (over-the-counter) swaps for NFTs [00:01:14].

## Core Mechanism: Fully On-Chain AMM

Unlike order book marketplaces where listings are stored off-chain and transactions only go on-chain upon purchase or cancellation, Sudoswap is a fully on-chain AMM [00:02:05]. This means everything, including pricing, is on-chain, powered by formulas dependent on supply and demand [00:02:09]. There are no traditional order books [00:02:11].

For Sudoswap to function, it requires liquidity pools, which are provided by market makers or liquidity providers [00:02:20].

## Instant Liquidity for Buying and Selling

One key feature of Sudoswap is its instant liquidity for buying and selling NFTs [00:02:27]. This is achieved through user-created pools [00:02:52].

*   **Buying:** Users can immediately buy an NFT by selecting from existing pools, choosing the cheapest price (lowest offering) [00:03:09]. NFTs can be added to a shopping cart [00:03:47].
*   **Selling:** Users can instantly sell an NFT into a pool at the best available offer price, without needing to wait for a buyer [00:03:18].
*   **Sweep Mode:** This mode allows users to purchase multiple NFTs at once from various pools, sweeping the floor of a collection [00:03:52].

## Becoming a Market Maker: Creating Pools

Sudoswap allows users to create their own pools and become market makers, earning trading fees [00:04:19]. There are three main types of pools that can be created:

### 1. Buy NFT with Tokens (Buy Limit Order / DCA Pool)

This option allows users to set a buy limit order for NFTs [00:04:47].
*   Users deposit ETH (or other tokens) to buy NFTs [00:04:51].
*   A specific buy price can be set, acting as a limit order [00:04:57]. If only buying one NFT, the chosen bonding curve (linear or exponential) and delta value do not significantly affect the single purchase [00:05:01].
*   **DCA (Dollar-Cost Averaging) Pool:** By setting a quantity greater than one, this pool can function as a DCA strategy [00:05:34].
    *   The `delta` value determines how the buy price adjusts downwards each time the pool acquires an NFT [00:05:39]. For example, a delta of 0.1 means the buy price drops by 0.1 ETH for each subsequent NFT purchased [00:05:44].

### 2. Sell NFT with Tokens (Sell Limit Order / DCA Pool)

This option allows users to set a sell limit order for their NFTs [00:06:01].
*   Users deposit their NFTs to sell for ETH (or other tokens) [00:06:04].
*   A specific sell price can be set, acting as a limit order [00:06:09]. Similar to buying, for a single NFT, the bonding curve and delta do not heavily influence the outcome [00:06:14].
*   **DCA Pool:** For selling multiple NFTs, this can also be set up as a DCA strategy [00:06:29].
    *   The `delta` value determines how the sell price increases each time an NFT is sold from the pool [00:06:32]. For example, a delta of 0.1 means the sell price increases by 0.1 ETH for each subsequent NFT sold [00:06:35].

### 3. Market Maker Pool (Buy and Sell)

This is the most comprehensive option, allowing users to deposit both ETH and NFTs to provide liquidity for both buying and selling [00:07:01].
*   Market makers earn trading fees on every transaction that takes place in their pool [00:07:14].
*   **Fee Amount:** A trading fee percentage can be set by the pool creator [00:07:21].
*   **Bonding Curves:**
    *   **Linear Curve:** Uses a fixed price adjustment (e.g., 0.1 ETH) [00:07:38]. When buying into the pool, the offer price (what the pool pays) goes down by the fixed delta with each purchase [00:08:22]. When selling from the pool, the selling price (what the pool charges) goes up by the fixed delta with each sale [00:08:31].
    *   **Exponential Curve:** Uses a variable, percentage-based adjustment (e.g., 10%) [00:07:41]. The offer price decreases by a set percentage after each NFT is bought into the pool [00:08:43]. The selling price also adjusts upward by a set percentage each time an NFT is sold from the pool [00:08:51].
*   **Delta:** The `delta` value determines the magnitude of price adjustment with each transaction within the pool [00:07:56].

## Fee Structure and Trader Preference

[[comparison_of_sudoswap_fees_with_other_platforms | Sudoswap's fee structure]] is different from other marketplaces:
*   **Platform Fee:** Sudoswap charges a platform fee of 0.5% [00:09:37], which is lower than OpenSea's 2.5% [00:09:24].
*   **No Royalty Fees:** Sudoswap does not impose royalty fees [00:09:11]. This means creators do not earn royalties on secondary sales through Sudoswap [00:09:47].
*   **Trader Preference:** Traders often prefer Sudoswap due to the absence of royalty fees, allowing them to keep more of the swap fee when setting up a pool [00:09:16]. This can sometimes lead to lower floor prices on Sudoswap compared to OpenSea due to reduced overall costs [00:10:10].

## Growing Traction

Sudoswap has seen significant growth, with a total volume of approximately $20 million and around 12,000 users [00:10:32]. The platform earns platform fees [00:10:42], and there is speculation about a potential token airdrop in the future, although this is not confirmed [00:10:47].