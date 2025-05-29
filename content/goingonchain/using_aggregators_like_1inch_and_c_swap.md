---
title: Using aggregators like 1inch and C Swap
videoId: 4PmgYsP2HnY
---

From: [[goingonchain]] <br/> 

Uniswap recently implemented a 0.15% swap fee for using their user interface (UI) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This means an extra charge is incurred when making a swap directly on the Uniswap site <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While seemingly small, these fees can accumulate over multiple transactions <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. As of the video's recording, these fees have generated approximately $56,000 for Uniswap's liquidity providers (LPs), not for UNI token holders <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

There are several [[methods_to_avoid_uniswap_fees | methods to avoid these Uniswap fees]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Aggregators

Aggregators offer a way to bypass the direct Uniswap UI fee by routing trades through different liquidity sources.

### 1inch Aggregator

1inch is an aggregator that can be used to achieve better rates and lower fees compared to direct Uniswap swaps <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

*   **Process**: When an order is placed with 1inch, it enters a pool where 1inch resolvers compete to fulfill it <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. If a resolver takes the order, they cover the gas fees <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **Example Comparison**:
    *   **1inch**: Selling 1 ETH yields 1574 USDT, with a free network fee and a $24 settlement fee <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
    *   **Uniswap**: Selling 1 ETH yields 1569 USDT (which is less), incurring a Uniswap fee of $2.36 and a network cost of $5 <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### C Swap Aggregator

C Swap functions similarly to a batch order system, providing competitive rates and lower fees <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

*   **Process**: When a request is made on C Swap, it compiles all "intent" orders into an order book <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. A solver then attempts to find matching orders, such as someone looking to sell ETH being matched with someone looking to buy ETH <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Example Comparison**:
    *   **C Swap**: Selling 1 ETH yields 1574 USDT <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
    *   **Uniswap**: Selling 1 ETH yields 1570 USDT <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Llama Swap (Aggregator of Aggregators)

Llama Swap, a product by DeFi Llama, acts as an aggregator of all aggregators, including both 1inch and C Swap <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

*   **Benefits**: When selling 1 ETH via Llama Swap, a user can receive 1575 USDT with no fees from Llama Swap <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. It also includes a privacy feature that allows users to hide their IP address <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Direct Backend Interaction

For more technical users, it is possible to directly interact with Uniswap's backend to avoid fees <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This involves:

*   Navigating to Etherscan for the Uniswap V2 router <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   Going to the "Contract" section and then "Write Contract" <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   Connecting a Web3 wallet <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   Calling a specific function, such as "sort ETH for exact tokens," and inputting the required parameters <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This is a [[technical_method_to_bypass_uniswap_fees | technical method to bypass Uniswap fees]] <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.