---
title: AMM changes and pool types in Spiritswap V2
videoId: ZxohPqwc8js
---

From: [[goingonchain]] <br/> 

[[Spiritswap V2 features and improvements | Spiritswap V2]] introduces significant changes to its Automated Market Maker (AMM) model and liquidity pools, moving beyond the V1 structure to offer more versatility and improved user experience <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. These updates are part of a continuous building effort by the Spiritswap team <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Overview of Liquidity in V2

The V2 homepage now provides a clear overview of a user's portfolio, including liquidity provided on Spiritswap <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. The liquidity section has been revamped with its own dedicated tab, featuring "Classic" and "Stable" pool options <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Understanding Spiritswap's AMM Model

Spiritswap operates as a Decentralized Exchange (DEX) that runs on mathematical formulas programmed into smart contracts, eliminating human interfacing <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### V1's Classic AMM (x * y = k)

The most common formula used by many DEXs, including Spiritswap V1, is `x * y = k` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Typically, a pool following this formula holds 50% of Token A and 50% of Token B <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   This "classic" version works on the concept of supply and demand <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   However, for highly correlated tokens like USDC and DAI, this formula is not ideal <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Large order volumes can lead to very high slippage, despite the expectation of a 1:1 exchange rate <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### V2's Modified Solidly AMM

In [[Spiritswap V2 features and improvements | V2]], Spiritswap has implemented a modified version of Solidly, making its AMM even more versatile <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

#### New Pool Types in V2
*   **Classic Pool**: Continues to support the standard `x*y=k` model, suitable for most token pairs <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Stable Pool**: Specifically designed for stablecoins and pegged asset tokens, such as wINSPIRIT and INSPIRIT <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This pool type addresses the high slippage issue seen with `x*y=k` for stable assets <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   **Weighted Pool (Coming in V2.1)**: Future plans include a weighted pool similar to the Balancer AMM, offering even more flexibility <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## AMM Fees and Distribution

[[Spiritswap V2 features and improvements | Spiritswap V2]] introduces a new AMM fee structure, changing from 0.3% to 0.18% per transaction <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This 0.18% fee is distributed as follows <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>:
*   **25%** goes to the base fee <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **25%** goes to the protocol <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **50%** goes to a voting fee, distributed exclusively to [[Inspirit holder benefits and rewards model in Spiritswap V2 | INSPIRIT holders]] who vote for the gauge attached to the pool where the fees were generated <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

For example, if you hold 10 INSPIRIT and direct it to the LQDR-FTM gauge, which receives 100 INSPIRIT votes, you hold a 10% share of that gauge's voting fees <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. If that pool generates 100k in fees the following week, 50k will go to the pool's vote fees, meaning you would receive 5,000 worth of LQDR and FTM tokens (10% of 50k) <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

## Real Yield Model

The new "real yield" model makes participating in [[Inspirit holder benefits and rewards model in Spiritswap V2 | INSPIRIT]] even more attractive <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This model ensures that [[Inspirit holder benefits and rewards model in Spiritswap V2 | INSPIRIT holders]] are not diluted by new SPIRIT emissions <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   For instance, if 100k SPIRIT is to be emitted and 200 million out of 500 million total SPIRIT supply is locked in INSPIRIT, 40,000 SPIRIT will be distributed directly to [[Inspirit holder benefits and rewards model in Spiritswap V2 | INSPIRIT holders]] that week <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   This mechanism provides [[Inspirit holder benefits and rewards model in Spiritswap V2 | INSPIRIT holders]] with a subsidized flow of emissions, preventing dilution by farmers and increasing the attractiveness of holding INSPIRIT <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.