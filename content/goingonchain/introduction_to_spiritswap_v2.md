---
title: Introduction to Spiritswap V2
videoId: ZxohPqwc8js
---

From: [[goingonchain]] <br/> 

Spiritswap is a project that continues to build even during bear markets, and they are releasing their V2 version with significant improvements <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The V2 version aims for a better and more seamless user experience through a complete UI revamp <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Beyond cosmetic changes, V2 also introduces substantial functional enhancements <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## [[comparison_between_spiritswap_v1_and_v2 | Comparison with V1]]

Spiritswap V1 was a fork of Uniswap V2, but Spiritswap V2 has added numerous features to it <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## [[new_features_in_spiritswap_v2 | New Features in Spiritswap V2]]

### Revamped Homepage and Portfolio Overview
The V2 homepage provides a clear overview of a user's portfolio <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This overview takes into account five components <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>:
*   Tokens held in the wallet <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
*   Liquidity provided on Spiritswap <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   In-spirit holdings <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Set limit orders <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
*   Lending and borrowing activities <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>

### Bridge Enhancements
The bridging functionality has been revamped <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Integrated Swap and Bridge**: In V1, users had to first bridge assets (e.g., from Ethereum mainnet to Fantom chain) and then execute a separate swap to get Spiritswap tokens <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. In V2, users can swap while they bridge, meaning they can bring assets over from Ethereum to Fantom and receive Spiritswap tokens or other Fantom chain tokens in a single transaction <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Bridge Mode Selection**: Users can choose between "cheapest" and "fastest" bridge modes based on their needs <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
    *   **Cheapest**: Takes more time but offers the best rate <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
    *   **Fastest**: Might not offer the best rate but executes in the shortest time <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Liquidity Tab and AMM Versatility
The liquidity section now has its own dedicated tab with "Classic" and "Stable" options <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **AMM Mechanism**: Spiritswap is a Decentralized Exchange (DEX) that operates on mathematical formulas programmed into smart contracts, typically using the `x * y = k` formula <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Classic Pools**: These pools, often containing 50% of token A and 50% of token B, work on the concept of supply and demand <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Stable Pools**: For highly correlated tokens like USDC and DAI, the classic formula can lead to high slippage with large order volumes <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. In V2, Spiritswap utilizes a modified version of Solidly, making its AMM more versatile <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This allows for stable pools, which are beneficial for stablecoins and pegged assets like wSPIRIT and inSPIRIT <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Future Weighted Pools**: Spiritswap V2.1 will introduce weighted pools, similar to Balancer's AMM <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### inSPIRIT Page Improvements and Benefits for Holders
The inSPIRIT page in V2 has seen significant UI improvements, making it clearer and less cluttered compared to V1 <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Clear Voting Page**: Users can clearly see where their votes are going and how to execute them <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Dashboard Overview**: The dashboard shows the current in-spirit balance and locked SPIRIT <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Claimable Bribes Reward**: A major new feature is the integration of claimable bribes rewards directly onto the inSPIRIT page <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Previously, protocols would drop bribes directly to users, making tracking and claiming tedious <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Now, users can claim their rewards and bribes directly from this page <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This is relevant to [[case_studies_on_crypto_bribes_beats_and_spirit_swap | crypto bribes]]
*   **Enhanced Benefits for inSPIRIT Holders**: Holders of inSPIRIT, who take on more risk by locking their tokens, receive additional benefits <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>:
    *   **AMM Fee Distribution**: The AMM fees are changing from 0.3% to 0.18% <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This 0.18% fee is distributed as follows <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>:
        *   25% goes to a base fee <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
        *   25% goes to the protocol <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
        *   50% goes to a voting fee, which is distributed only to in-spirit holders who vote for the gauge attached to a specific pool <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
        *   *Example*: If a user has 10 inSPIRIT and directs it to the LQDR-FTM gauge, which receives 100 inSPIRIT votes, the user has a 10% share of that gauge's voting fees <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. If the pool generates 100k in fees the following week, 50k of those fees go to the pool's vote fees, and the user would receive 5,000 worth of LQDR and FTM tokens (10% of 50k) <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
    *   **Real Yield Model**: This model makes participating in inSPIRIT more attractive by preventing dilution of inSPIRIT holders by SPIRIT emissions <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. In V2, inSPIRIT holders will not be diluted <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. For example, if 100k SPIRIT are to be emitted in a week and 200 million out of 500 million total SPIRIT supply are locked in inSPIRIT, 40,000 SPIRIT would be distributed to inSPIRIT holders that week <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. This ensures inSPIRIT holders receive a subsidized flow of emissions, protecting them from dilution by farmers <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.