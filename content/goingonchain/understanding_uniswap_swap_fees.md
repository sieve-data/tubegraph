---
title: Understanding Uniswap swap fees
videoId: 4PmgYsP2HnY
---

From: [[goingonchain]] <br/> 

Uniswap recently implemented a 0.15% swap fee for using their user interface (UI) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This means that when a user makes a swap directly on the Uniswap website, an additional charge is applied <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While the fee might appear small, it can accumulate significantly when conducting multiple transactions <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

Currently, these fees have generated approximately $56,000 for Uniswap <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. It's important to note that these fees are directed to Uniswap Labs, not to UNI token holders <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## [[methods_to_avoid_uniswap_fees | Methods to Avoid Uniswap Fees]]

There are four primary ways to avoid paying the 0.15% Uniswap UI fee <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>:

### 1. Using an Aggregator

Aggregators help users find better rates and often lower fees by routing orders through various liquidity sources <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

*   **[[using_aggregators_like_1inch_and_c_swap | 1inch]]**
    *   When selling 1 ETH for USDT on 1inch, using "Fusion" swap mode can yield 1574 USDT with a free network fee and a $24 settlement fee <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
    *   In comparison, a direct swap on Uniswap for 1 ETH might yield only 1569 USDT, along with a $2.36 Uniswap fee and a $5 network cost <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
    *   1inch functions by placing orders into a pool where 1inch resolvers compete to fulfill the order. If a resolver takes the order, they cover the gas fees, resulting in lower overall fees and better rates for the user <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

*   **[[using_aggregators_like_1inch_and_c_swap | C Swap]]**
    *   Selling 1 ETH on C Swap can also yield 1574 USDT, whereas Uniswap might offer 1570 USDT for the same trade <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
    *   C Swap operates by batching orders, taking user intents and placing them into an order book. A solver then attempts to find matches, such as pairing a user looking to sell ETH with another looking to buy ETH <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This mechanism allows for competitive rates and reduced fees <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

*   **Llama Swap**
    *   Llama Swap, a product by DeFi Llama, acts as an aggregator of all aggregators, including C Swap and 1inch <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   When selling 1 ETH via Llama Swap, users can expect to receive around 1575 USDT with no additional fees from Llama Swap itself <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   Llama Swap also offers a privacy feature that allows users to hide their IP addresses <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### 2. [[technical_method_to_bypass_uniswap_fees | Using the Backend Directly]]

This method is more technical and allows users to bypass the UI fees by interacting directly with the Uniswap smart contract <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>, <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Users can navigate to the Uniswap V2 router contract on Etherscan, connect their Web3 wallet, and call the desired function (e.g., `sortIfForExactTokens`) by providing the necessary inputs <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This approach is best suited for individuals with technical expertise <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.