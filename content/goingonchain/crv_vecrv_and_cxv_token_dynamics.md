---
title: CRV veCRV and CXV token dynamics
videoId: nc8Qi8UTT7Y
---

From: [[goingonchain]] <br/> 

Curve Finance is a decentralized exchange (DEX) specifically designed for efficient stablecoin swaps with low slippage. The dynamics of its native token, CRV, and its vote-escrowed version, veCRV, along with Convex Finance's CVX token, are central to the "Curve War" – a battle among protocols to control Curve's liquidity incentives.

## What is Curve?
Curve is an Automated Market Maker (AMM) that functions similarly to other DEXs like PancakeSwap or SushiSwap <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Its unique feature is an algorithm optimized for stablecoin swaps <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Curve's Stable Swap Algorithm
Traditional AMMs use an `x * y = k` formula, which works well for most assets but leads to high slippage for large stablecoin orders <a class="yt-timestamp" data-t="00:00:51">[00:01:01]</a>. Curve solves this by employing a hybrid approach combining two formulas: `x + y = k` and `x * y = k` <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   When a liquidity pool is balanced, the algorithm functions as `x + y = k` (constant sum formula), resulting in very low slippage <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   When the pool becomes imbalanced, the algorithm shifts to `x * y = k` (constant product formula) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
This hybrid model allows for significantly lower slippage on large stablecoin swaps compared to other DEXs, making it attractive to whales <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. For example, a $500,000 USDT to USDC swap on SushiSwap might yield $487,000 USDC, while on Curve, the slippage is much lower, yielding closer to the full amount <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## The Curve War
The "Curve War" describes the competition among various DeFi protocols to accumulate or influence the voting power within Curve, primarily through veCRV, to direct CRV rewards to their respective liquidity pools <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. This is crucial for protocols that want to push liquidity into the Ethereum DeFi ecosystem <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### CRV and veCRV Dynamics
CRV is the native token of Curve Finance <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Liquidity Providers (LPs)**: LPs on Curve earn trading fees and CRV rewards <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **veCRV (Vote-Escrowed CRV)**: LPs can choose to lock up their earned CRV for a period of one to four years <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
    *   Locking CRV converts it into veCRV at a ratio of 0.25 veCRV per CRV for a one-year lock, up to 1 veCRV per CRV for a four-year lock <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   veCRV grants holders voting rights in Curve's governance <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   Holders can use their veCRV to vote for their specific liquidity pool, which boosts the CRV rewards for that pool <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This creates a cycle where LPs lock CRV to earn more CRV <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

Protocols that want to attract liquidity to their stablecoin pools on Curve need to either acquire CRV to lock up themselves or "bribe" veCRV holders to vote for their pools <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Convex Finance (CVX)
Convex Finance is a protocol that simplifies and amplifies the benefits of participating in the Curve ecosystem <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Convex is currently the largest holder of veCRV <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **cvxCRV**: CRV holders can convert their CRV to cvxCRV on Convex <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This is a one-way conversion, meaning cvxCRV cannot be directly converted back to CRV, though it can be traded on a secondary market <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Boosted Rewards**: When users stake cvxCRV, Convex takes their CRV, locks it into veCRV, and uses this collective voting power to boost rewards across various Curve gauges. The boosted CRV rewards are then split with the cvxCRV stakers <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **vlCVX (Vote-Locked CVX)**: Users can also stake Convex's native token, CVX, and lock it for 16 weeks to receive vlCVX <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. vlCVX holders receive additional rewards and governance voting rights within Convex <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Bribing with Votium
Protocols engage in bribing vlCVX holders (who control the largest pool of veCRV voting power through Convex) to vote for their specific Curve pools <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Votium is a protocol that facilitates these bribes, allowing other protocols to offer incentives to vlCVX users for their votes <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. For instance, protocols like Frax and Terra's UST have offered significant bribes to vlCVX users to direct CRV emissions to their pools <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a> <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## The 4pool and Curve War Implications
The "4pool" is a liquidity pool initiative on Curve involving UST, FRAX, USDC, and USDT <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Its primary goal is to become the most liquid and utilized stablecoin pool on Ethereum, potentially replacing the popular 3pool (DAI, USDT, USDC) by removing DAI <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a> <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

Protocols involved in the 4pool, such as Frax and Terra, are among the largest holders of CVX <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. By partnering with other major protocols like Badger, Olympus, and Tokemak, they can collectively push significant CVX governance power towards the 4pool <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a> <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This collaboration aims to consolidate power and drive out competing stablecoins like DAI, establishing UST and FRAX as leading decentralized stablecoins, particularly in the highly liquid Ethereum ecosystem <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

A deep liquid 4pool also serves strategic goals, such as enabling large UST swaps for USDT to facilitate Bitcoin purchases for Luna Foundation Guard (LFG), as native blockchain liquidity might be insufficient <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.