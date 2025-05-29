---
title: Comparison between Spiritswap V1 and V2
videoId: ZxohPqwc8js
---

From: [[goingonchain]] <br/> 

SpiritSwap V2 represents a significant advancement for the platform, particularly during a bear market where the team prioritized continuous building <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The goal of V2 is to provide a better and more seamless user experience <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## User Interface and Experience
SpiritSwap V1's homepage was described as "cluttered" <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. In contrast, V2 features a complete revamp of the UI, focusing on better user experience <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

The V2 homepage provides a clear overview of a user's portfolio, taking into account five components:
*   Tokens in wallet <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
*   Liquidity provided on SpiritSwap <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   inSPIRIT holdings <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Set limit orders <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
*   Lending and borrowing activities <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>

## Enhanced Bridge Functionality
The bridging process has been significantly revamped in V2 <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **V1:** Users first had to bridge assets from a mainnet (e.g., Ethereum) to the Fantom chain, and then execute a separate swap to get SpiritSwap tokens <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **V2:** Users can now swap while they bridge. This means assets brought over from Ethereum to the Fantom chain can directly become SpiritSwap tokens or any other Fantom chain tokens in a single transaction <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

Additionally, users can choose between two bridge modes based on their needs <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>:
*   **Cheapest:** Takes longer but offers the best rate <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   **Fastest:** Might not yield the best rate but executes in the shortest time <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Liquidity Pools and AMM Evolution
In V2, liquidity now has its own dedicated tab, featuring "classic" and "stable" pool options <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

*   **V1 (Classic AMM):** SpiritSwap V1 was a fork of [[comparisons_between_astroport_and_other_amms_like_terraswap_and_uniswap | Uniswap]] V2 <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Decentralized exchanges (DEXs) like SpiritSwap run on mathematical formulas without human interfacing <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Most DEXs use the formula `x * y = k`, where pools typically consist of 50% Token A and 50% Token B <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. While suitable for most pairs, this classic model can lead to high slippage for highly correlated tokens like USDC and DAI, where theoretically a 1:1 exchange should occur <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

*   **V2 (Modified Solidly AMM):** SpiritSwap V2 introduces a modified version of Solidly, making its Automated Market Maker (AMM) even more versatile <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. It supports:
    *   **Classic Pools:** For general token pairs <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
    *   **Stable Pools:** Ideal for stablecoins (e.g., USDC, DAI) and pegged assets (e.g., winSPIRIT, inSPIRIT) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   **Weighted Pools (V2.1):** Similar to Balancer AMM, these will be introduced in V2.1 <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## inSPIRIT (veSPIRIT) Improvements
The inSPIRIT page also received a significant UI improvement <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. V1's inSPIRIT page was "cluttered and a little bit messy" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. In V2, it is much clearer, offering:
*   A clear voting page to track votes and execute them <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   A dashboard displaying current inSPIRIT balance and locked SPIRIT <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Claimable Bribe Rewards:** A new feature allows users to directly claim their bribe rewards from the inSPIRIT page, making it easier to track and claim rewards that protocols previously distributed <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Benefits for inSPIRIT Holders
inSPIRIT holders are receiving more benefits due to the increased risk of locking their tokens <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>:

*   **AMM Fee Distribution:** The AMM fees have been adjusted from 0.3% to 0.18% <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. These 0.18% fees are distributed as follows:
    *   25% goes to a base fee <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   25% goes to the protocol <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
    *   50% goes to a voting fee, distributed only to inSPIRIT holders who vote for the gauge attached to the pool <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

    For example, if an inSPIRIT holder directs 10 inSPIRIT to an LQDR-FTM gauge that receives a total of 100 inSPIRIT votes (giving them a 10% share), and the pool generates 100k in fees the following week:
    *   25k fees go to all inSPIRIT holders via the base fee <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
    *   25k fees go to Liquid Driver as protocol fees <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   50k fees go to the pool's vote fees. With a 10% share of this pool, the inSPIRIT holder would receive 5,000 worth of LQDR and FTM tokens <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

*   **Real Yield Model:** This model makes participating in inSPIRIT more attractive by preventing dilution of inSPIRIT holders <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. In V1, Spirit emission could dilute inSPIRIT holders <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. In V2, a portion of the weekly Spirit emission is distributed to inSPIRIT holders, subsidizing their flows and preventing dilution by "farmers" <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
    *   For instance, if 100k SPIRIT are emitted in a week, and 200 million of the 500 million total SPIRIT supply are locked in inSPIRIT, 40,000 SPIRIT would be distributed to inSPIRIT holders that week <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

SpiritSwap V2 offers more than just UI changes, introducing significant improvements under the hood <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.