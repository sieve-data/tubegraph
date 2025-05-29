---
title: New features in Spiritswap V2
videoId: ZxohPqwc8js
---

From: [[goingonchain]] <br/> 

SpiritSwap, a project known for continuous building, has released its V2 platform, introducing significant improvements over its V1 predecessor <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. While [[comparison_between_spiritswap_v1_and_v2 | SpiritSwap V1]] was a fork of Uniswap V2 with added features <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, V2 brings a complete revamp focusing on enhanced user experience and underlying mechanics.

## User Interface and Experience Enhancements

One of the most notable changes in [[introduction_to_spiritswap_v2 | SpiritSwap V2]] is a complete overhaul of the user interface (UI) <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The goal of this revamp is to provide a better and more seamless user experience, addressing the somewhat cluttered interface of V1 <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Personalized Homepage Overview
The V2 homepage now offers a clear overview of a user's entire portfolio <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This includes five key components:
*   Tokens held in the wallet <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
*   Liquidity provided on SpiritSwap <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   In-spirits held <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Set limit orders <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
*   Lending and borrowing activities <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>

### Streamlined Bridge Functionality
The bridging process has been significantly revamped in V2 <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Previously, users would first bridge their assets from a mainnet (like Ethereum) to the Fantom chain, and then execute a separate swap to acquire SpiritSwap tokens <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. In V2, users can now swap assets directly while bridging, completing the entire process in a single transaction <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Users also have the flexibility to choose their preferred bridge mode:
*   **Cheapers**: Provides the best rate, though it may take more time <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   **Fastest**: Executes the transaction in the shortest time, potentially at a less optimal rate <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Advanced Automated Market Maker (AMM) Mechanism

SpiritSwap, operating as a decentralized exchange (DEX), relies on programmed smart contracts for its operations, using mathematical formulas instead of human interfacing <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Versatile Liquidity Pools
V2 introduces a dedicated "Liquidity" tab featuring "Classic" and "Stable" pool options <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. The core of this improvement lies in V2's AMM, which is a modified version of Solidly, offering greater versatility <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This allows for:
*   **Classic Pools**: Utilizes the traditional `x * y = k` formula, suitable for most token pairs based on supply and demand <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Stable Pools**: Specifically designed for highly correlated tokens like stablecoins (e.g., USDC and DAI) or pegged assets (e.g., wrapped Spirit and in-Spirit) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This mechanism mitigates high slippage that typically occurs with large order volumes in classic pools for such assets <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   **Future Weighted Pools**: SpiritSwap V2.1 will further expand the AMM capabilities to include weighted pools, similar to the Balancer AMM <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Enhanced In-Spirit Holder Experience

The in-spirit page in V2 has received a significant UI improvement, presenting information more clearly than in V1 <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. It now offers a clear voting page to track vote distribution and execution <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. The dashboard clearly displays the current in-spirit balance and locked spirit <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Claimable Bribes Reward
A highly anticipated feature is the integration of claimable bribes rewards directly onto the in-spirit page <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Previously, users found it tedious to track and claim bribes manually as protocols would directly drop them <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. V2 centralizes this, allowing users to claim their bribe and other rewards conveniently from one place <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Increased Benefits and "Real Yield" for In-Spirit Holders
In-spirit holders, who take on more risk by locking their tokens, are set to receive more benefits in V2 <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

#### AMM Fee Distribution
The AMM fees have been adjusted from 0.3% to 0.18% <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This 0.18% fee is distributed as follows:
*   **25% to Base Fee**: Distributed to all in-spirit holders <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **25% to Protocol**: Goes to the protocol <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **50% to Voting Fee**: Distributed exclusively to in-spirit holders who vote for the gauge attached to the specific pool that generated the fees <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. For example, if a user dedicates 10 in-spirit to a pool's gauge that receives 100 in-spirit votes, they have a 10% share of that gauge's voting fees <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. If that pool generates $100,000 in fees, $50,000 will go to the voting fee pool, with the user receiving $5,000 worth of tokens based on their 10% share <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

#### Real Yield Model to Prevent Dilution
The new "real yield" model makes participating in in-spirit more appealing by preventing dilution of in-spirit holders from Spirit emissions <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. In V2, a portion of the weekly Spirit emission is specifically distributed to in-spirit holders based on their proportion of the total locked Spirit <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. For example, if 100,000 Spirit are emitted and 200 million of a total 500 million Spirit supply is locked in in-spirit (40%), then 40,000 Spirit will be distributed to in-spirit holders that week <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This provides a subsidized flow of emission, safeguarding in-spirit holders from dilution by farmers <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

SpiritSwap V2 introduces not only cosmetic UI changes but also significant under-the-hood improvements to its bridge, AMM, and incentive models for in-spirit holders <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.