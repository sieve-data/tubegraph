---
title: Methods to avoid Uniswap fees
videoId: 4PmgYsP2HnY
---

From: [[goingonchain]] <br/> 

Recently, Uniswap introduced a 0.15% swap fee for users interacting with their user interface (UI) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This means an additional charge is applied when a swap is initiated directly through the Uniswap website <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While seemingly small, this fee can accumulate significantly over multiple transactions <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. As of the transcript's recording, these fees have generated approximately $56,000 for Uniswap Labs, with the revenue going to Uniswap Labs rather than UNI token holders <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

There are four primary methods to avoid paying this 0.15% fee <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Using Aggregators

Aggregators can help users achieve better rates and lower overall costs by optimizing swap paths across various liquidity sources.

### [[using_aggregators_like_1inch_and_c_swap | 1inch]]

[[using_aggregators_like_1inch_and_c_swap | 1inch]] is an example of an aggregator that can help users avoid direct Uniswap fees <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. When using [[using_aggregators_like_1inch_and_c_swap | 1inch]], specifically with its Fusion swap mode, network fees can be free, though a settlement fee might apply (e.g., $24) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. In a comparison, a swap of 1 ETH could yield 1574 USDT on [[using_aggregators_like_1inch_and_c_swap | 1inch]], compared to 1569 USDT on Uniswap, which incurs a $2.36 Uniswap fee and a $5 network cost <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

The process on [[using_aggregators_like_1inch_and_c_swap | 1inch]] involves an order going into an order pool where [[using_aggregators_like_1inch_and_c_swap | 1inch]] resolvers compete to fulfill it <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. If a resolver takes the order, they pay for the gas, leading to lower fees and potentially better rates for the user <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### [[using_aggregators_like_1inch_and_c_swap | C Swap]]

[[using_aggregators_like_1inch_and_c_swap | C Swap]] offers another way to bypass Uniswap fees <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. For example, selling 1 ETH on [[using_aggregators_like_1inch_and_c_swap | C Swap]] could yield 1574 USDT, whereas Uniswap might yield 1570 USDT for the same trade <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. [[using_aggregators_like_1inch_and_c_swap | C Swap]] operates by taking multiple user orders (intents) and placing them into an order book <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. A "solver" then attempts to find matches between buy and sell orders, such as matching someone looking to sell ETH with someone looking to buy ETH <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This batching and matching process enables users to get competitive rates and pay lower fees <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Llama Swap

Llama Swap, a product by DeFi Llama, functions as an "aggregator of all aggregators," integrating services like [[using_aggregators_like_1inch_and_c_swap | C Swap]] and [[using_aggregators_like_1inch_and_c_swap | 1inch]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. When using Llama Swap, there are no fees from Llama Swap itself, and it can offer competitive rates (e.g., 1575 USDT for 1 ETH) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Additionally, Llama Swap provides a privacy feature that allows users to hide their IP addresses <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Direct Backend Interaction

For more technical users, it is possible to bypass the Uniswap UI fee by interacting directly with the backend smart contract <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This method involves going to Etherscan, navigating to the Uniswap V2 router contract, and selecting the "Write Contract" tab <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. After connecting a Web3 wallet, users can find and call specific functions, such as "swap ETH for exact tokens," by providing the necessary inputs <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

Among these options, Llama Swap is noted as a preferred choice for its comprehensive aggregation and lack of direct fees <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a><a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.