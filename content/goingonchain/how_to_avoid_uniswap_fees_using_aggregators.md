---
title: How to avoid Uniswap fees using aggregators
videoId: 4PmgYsP2HnY
---

From: [[goingonchain]] <br/> 

[[uniswap_swap_fees | Uniswap]] recently implemented a 0.15% swap fee for using its user interface (UI) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This means an extra charge is applied when making a swap directly on the [[uniswap_swap_fees | Uniswap]] website <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While this fee may appear small, it can accumulate significantly with multiple transactions <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These collected fees benefit [[uniswap_swap_fees | Uniswap]] liquidity providers (LPs), not UNI token holders <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. As of the video's recording, this fee mechanism had generated approximately $56,000 in fees <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

There are four primary methods to avoid paying this additional 0.15% fee <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## 1. Using Aggregators (e.g., 1inch)

Aggregators such as 1inch can be utilized to circumvent the direct [[uniswap_swap_fees | Uniswap]] UI fee <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

*   **Example Comparison**: When selling 1 ETH for USDT:
    *   On 1inch (using Fusion swap mode), a user might receive 1574 USDT with a free network fee and a $24 settlement fee <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
    *   On [[uniswap_swap_fees | Uniswap]], the same transaction might yield 1569 USDT, incurring a $2.36 [[uniswap_swap_fees | Uniswap]] fee and a $5 network cost <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **How it Works**: When an order is placed with 1inch, it enters a pool where 1inch resolvers compete to fulfill it <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. If a resolver takes the order, they cover the gas fees, resulting in lower overall fees and better rates for the user <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## 2. Using C Swap

C Swap offers another avenue to avoid the [[uniswap_swap_fees | Uniswap]] UI fee <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

*   **Example Comparison**: Selling 1 ETH on C Swap could yield 1574 USDT, whereas on [[uniswap_swap_fees | Uniswap]], it might yield 1570 USDT <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **How it Works**: C Swap can be thought of as a batch order system <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. It collects user requests (intents) and places them into an order book <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. A solver then attempts to find matching orders (e.g., one user selling ETH and another buying ETH) to facilitate direct matches <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This matching process allows for competitive rates and lower fees <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## 3. Using LlamaSwap

LlamaSwap is a product by DeFi Llama, acting as an "aggregator of all aggregators," including 1inch and C Swap <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

*   **Benefits**: When selling 1 ETH through LlamaSwap, a user might receive 1575 USDT with no fees from LlamaSwap itself <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. LlamaSwap also provides a privacy feature, allowing users to hide their IP addresses <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Recommendation**: LlamaSwap is personally favored by the video's presenter <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## 4. Using the Backend Directly

For more technical users, it's possible to interact directly with the [[uniswap_swap_fees | Uniswap]] backend, thereby avoiding the UI fees <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

*   **Process**: This involves going to a platform like Etherscan (e.g., to the [[direct_integration_with_uniswap_backend_for_advanced_users | Uniswap V2 Router]] contract page) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. From there, users can navigate to "Contract," then "Write Contract," connect their Web3 wallet, and directly call the desired function (e.g., `swapETHForExactTokens`) by inputting the necessary parameters <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This method is specifically for those with advanced technical knowledge <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.