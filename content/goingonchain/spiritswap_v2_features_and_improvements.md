---
title: Spiritswap V2 features and improvements
videoId: ZxohPqwc8js
---

From: [[goingonchain]] <br/> 

Spiritswap, a dedicated team of builders, has released its V2, introducing significant improvements over its V1 predecessor. While V1 was a fork of Uniswap V2, Spiritswap V2 incorporates numerous new features and a complete overhaul aimed at enhancing user experience and functionality <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a> <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## User Interface (UI) Revamp
Spiritswap V2 features a complete revamp of its [[user_interface_changes_in_spiritswap_v2 | user interface]], addressing the cluttered appearance of V1 <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The primary goal of this redesign is to provide a better, more seamless user experience <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Homepage Overview
The V2 homepage now offers a clear overview of a user's portfolio <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This comprehensive view takes into account five key components <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>:
*   Tokens held in the wallet <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
*   Liquidity provided on Spiritswap <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Inspirit holdings <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Set limit orders <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
*   Any lending and borrowing activities <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>

## Swap and Bridge Functionality
The bridge functionality in V2 has also undergone a significant revamp, offering a more streamlined process <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
Previously, in V1, users had to first bridge their assets (e.g., from Ethereum mainnet to the Phantom chain) and then execute a separate swap to obtain Spiritswap tokens <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
In V2, users are now able to [[swap_and_bridge_functionality_in_spiritswap_v2 | swap while they bridge]] <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This means a single transaction can facilitate bringing assets from an external chain (like Ethereum) to the Phantom chain and simultaneously acquiring Spiritswap tokens or any other desired Phantom chain tokens <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

Users can also choose between different bridge modes based on their needs <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>:
*   **Cheapest**: This option takes more time but aims to provide the best possible rate <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   **Fastest**: This option ensures the transaction is executed in the shortest time, though it might not secure the absolute best rate <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Liquidity and AMM Changes
The liquidity section in V2 now has its own dedicated tab, separating it into "Classic" and "Stable" pools <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Spiritswap, as a Decentralized Exchange (DEX), operates on mathematical formulas programmed into smart contracts, with no human interfacing <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Automated Market Maker (AMM) Enhancements
Spiritswap V2 utilizes a modified version of Solidly, making its [[amm_changes_and_pool_types_in_spiritswap_v2 | AMM (Automated Market Maker)]] even more versatile <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a> <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Classic Pool**: These pools typically use the "x times y equals k" formula, maintaining a 50/50 split between Token A and Token B <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. While suitable for most pairs, high slippage can occur with large order volumes for highly correlated assets like stablecoins <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Stable Pool**: This type of pool is specifically designed for stablecoins and pegged assets (e.g., USDC and DAI, or wINSPIRIT and INSPIRIT) to minimize slippage, as these assets should ideally trade at a 1:1 ratio <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Weighted Pool (Future 2.1 Update)**: Spiritswap V2.1 will introduce weighted pools, similar to the Balancer AMM model, allowing for different token ratios within pools <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Inspirit Holder Benefits and Rewards Model
The Inspirit page in V2 has also seen significant UI improvements, making it clearer and less cluttered compared to V1 <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. The dashboard provides a clear overview of the current Inspirit balance and locked SPIRIT <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Claimable Bridge Rewards
A notable addition is the "claimable bride rewards" feature directly on the Inspirit page <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Previously, protocols would directly drop these rewards, making them difficult to track. V2 centralizes this, allowing users to easily claim their rewards <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Enhanced Benefits for Inspirit Holders
[[Inspirit holder benefits and rewards model in Spiritswap V2 | Inspirit holders]], who take on more risk by locking their tokens, will receive increased benefits <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>:

*   **Revised AMM Fees Distribution**: The AMM fees have been adjusted from 0.3% to 0.18% <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This 0.18% fee is distributed as follows <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>:
    *   **25% Base Fee**: Distributed to all Inspirit holders <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   **25% Protocol Fee**: Goes to the protocol (e.g., Liquid Driver) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
    *   **50% Voting Fee**: Distributed exclusively to Inspirit holders who vote for the specific gauge attached to the pool that generated the fees <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. For example, if an Inspirit holder directs 10 Inspirit to an LQDR/FTM gauge, which receives a total of 100 Inspirit votes, that holder earns a 10% share of the voting fees generated by that pool <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. If the pool generated 100K in fees, 50K would go to the pool's vote fees, resulting in 5,000 worth of LQDR and FTM tokens for the Inspirit holder with a 10% share <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

*   **Real Yield Model**: This model makes participation in Inspirit even more attractive by preventing the dilution of Inspirit holders from SPIRIT emissions <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. For instance, if 100K SPIRIT is to be emitted and 200 million of 500 million total SPIRIT supply is locked in Inspirit, 40,000 SPIRIT (40%) will be distributed to Inspirit holders to subsidize their share of the emission <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. This mechanism aims to prevent dilution by farmers and enhances the attractiveness of holding Inspirit <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

Spiritswap V2 represents a substantial upgrade, moving beyond just cosmetic changes to implement core functional and economic improvements <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.