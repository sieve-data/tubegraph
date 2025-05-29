---
title: Uniswap swap fees
videoId: 4PmgYsP2HnY
---

From: [[goingonchain]] <br/> 

Recently, Uniswap implemented a 0.15% swap fee for using their user interface (UI) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This means that when users make a swap directly through the Uniswap website, an additional charge is applied <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While this fee might seem small individually, it can accumulate significantly with multiple transactions <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These fees are directed to Uniswap Labs and do not benefit UNI token holders <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Currently, this fee structure has generated approximately $56,000 in fees for Uniswap Labs <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Strategies to Avoid Uniswap Swap Fees

There are four primary methods to avoid paying the 0.15% Uniswap UI fee <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### 1. Using Aggregators

Aggregators like [[using_1inch_and_c_swap_for_costeffective_crypto_transactions | 1inch]] can help users avoid these fees <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

*   **How it works**: When an order is placed with [[using_1inch_and_c_swap_for_costeffective_crypto_transactions | 1inch]], it enters a "will pull" system where [[using_1inch_and_c_swap_for_costeffective_crypto_transactions | 1inch]] resolvers compete to fulfill the order <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. If a resolver takes the order, they cover the gas fees <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **Cost Comparison Example (Selling 1 ETH for USDT)**:
    *   **[[using_1inch_and_c_swap_for_costeffective_crypto_transactions | 1inch]]**: Returns $1574 USDT with a free network fee and a $24 settlement fee <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
    *   **Uniswap**: Returns $1569 USDT with a $2.36 Uniswap fee and a $5 network cost <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Benefits**: Users typically pay less in fees and often receive better rates <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### 2. Using C Swap

[[using_1inch_and_c_swap_for_costeffective_crypto_transactions | C Swap]] is another option for avoiding Uniswap fees <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

*   **How it works**: [[using_1inch_and_c_swap_for_costeffective_crypto_transactions | C Swap]] operates on a batch order system <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. It collects user requests (intents) and places them into an order book, where a solver attempts to find matching orders (e.g., someone selling ETH matched with someone buying ETH) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Cost Comparison Example (Selling 1 ETH)**:
    *   **[[using_1inch_and_c_swap_for_costeffective_crypto_transactions | C Swap]]**: Returns $1574 <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
    *   **Uniswap**: Returns $1570 <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Benefits**: Users can achieve comparable rates and pay lower fees <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### 3. Using Llama Swap

Llama Swap, a product by Defi Llama, functions as an aggregator of all aggregators, including [[using_1inch_and_c_swap_for_costeffective_crypto_transactions | C Swap]] and [[using_1inch_and_c_swap_for_costeffective_crypto_transactions | 1inch]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

*   **Cost Example (Selling 1 ETH)**: Users can get $1575 with no fees charged by Llama Swap <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Additional Features**: Llama Swap also offers a privacy feature that allows users to hide their IP addresses <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   The speaker personally prefers Llama Swap <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### 4. Using the Backend Directly

For more technical users, it's possible to interact directly with the Uniswap backend to avoid fees <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

*   **Process**: This involves going to Etherscan, navigating to the Uniswap V2 router contract, selecting the "Write Contract" option, connecting a Web3 wallet, and directly calling the desired function (e.g., "sort if for exact tokens") by providing the necessary inputs <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Suitability**: This method is ideal for individuals with a more technical understanding of blockchain interactions <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.