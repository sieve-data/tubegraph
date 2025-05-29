---
title: Impact of liquidity pools on stablecoins
videoId: nc8Qi8UTT7Y
---

From: [[goingonchain]] <br/> 

## Understanding Liquidity Pools and Stablecoins

A [[liquidity_providers_and_incentives | liquidity pool]] is a collection of funds locked in a smart contract that facilitates decentralized trading, borrowing, and lending. Specifically for [[types_of_stablecoins_and_their_distinctions | stablecoins]], these pools are crucial for maintaining their peg and enabling efficient swaps.

### Curve Finance's Role

Curve Finance is an Automated Market Maker (AMM) that is specifically designed for efficient trading of [[types_of_stablecoins_and_their_distinctions | stablecoins]] and similarly priced assets <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Unlike typical AMMs that use the `x * y = k` formula (popularized by Uniswap V2) which can lead to high slippage for large [[types_of_stablecoins_and_their_distinctions | stablecoin]] orders <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, Curve employs a hybrid approach <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

Curve's algorithm functions as:
*   `x + y = k` (constant sum formula) when the [[liquidity_providers_and_incentives | liquidity pool]] is balanced <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   `x * y = k` (constant product formula) when the [[liquidity_providers_and_incentives | liquidity pool]] becomes imbalanced <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

This hybrid model significantly reduces slippage for [[types_of_stablecoins_and_their_distinctions | stablecoin]] swaps, making it a preferred choice for large trades by "whales" <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>, ensuring that one [[types_of_stablecoins_and_their_distinctions | stablecoin]] (e.g., USDT) yields close to one of another (e.g., USDC) <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Attracting Liquidity to Stablecoin Pools

For a [[liquidity_providers_and_incentives | liquidity pool]] to function effectively, it requires substantial [[liquidity_providers_and_incentives | liquidity]] and attractive rewards for [[liquidity_providers_and_incentives | liquidity providers]] <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Curve's ecosystem incentivizes [[liquidity_providers_and_incentives | liquidity providers]] through:

*   **Trading Fees and CRV Rewards**: [[liquidity_providers_and_incentives | Liquidity providers]] earn a portion of trading fees and receive CRV, Curve's native token <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **veCRV (Vote Escrowed CRV)**: By locking up CRV for periods ranging from one to four years, [[liquidity_providers_and_incentives | liquidity providers]] receive veCRV <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. veCRV holders can vote on which pools receive boosted CRV rewards, creating a cycle where [[liquidity_providers_and_incentives | LPs]] lock CRV to boost their own pools and earn more <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Convex Finance**: Convex is the largest holder of veCRV <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. It allows CRV holders to convert their CRV to cvxCRV, which can then be staked to receive boosted CRV rewards <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. Convex takes the CRV, locks it for veCRV, and uses it to vote for gauges, splitting the rewards with stakers <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Bribes**: Protocols looking to boost their own pools on Curve can bribe vlCVX (Vote-Locked CVX) holders to vote for their pool's gauges <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Votium is a protocol that facilitates these bribes <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This competitive "Curve War" sees protocols fighting to accumulate or bribe for CRV emissions to direct more rewards to their respective pools <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## The 4pool Initiative

The 4pool is a strategic [[liquidity_providers_and_incentives | liquidity pool]] partnership involving [[usdb_stablecoin_mechanism | UST]], FLUX, USDC, and USDT <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. It is currently available on FTM and Arbitrum, with an Ethereum pool expected to arrive soon <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Goals of 4pool

The primary goal of the 4pool is to become the dominant [[types_of_stablecoins_and_their_distinctions | stablecoin]] pool on Curve, specifically aiming to replace DAI in the popular 3pool (DAI, USDT, USDC) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. By doing so, it seeks to make the 4pool the most liquid and utilized [[types_of_stablecoins_and_their_distinctions | stablecoin]] pool across various chains <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Strategic Partnerships

To achieve its goals, the 4pool initiative relies on strong partnerships and collective governance power:
*   **Frax and Terra (LFG)**: These are two of the largest protocol holders of CVX and provide significant volume incentives to vlCVX holders <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **Wider Alliance**: The partnership extends to other protocols like Redacted, Badger, Olympus, and Token Reader, all working together to direct CVX governance votes towards the 4pool <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Reasons for the 4pool

The drivers behind the 4pool are multi-faceted:
*   **Collaboration over Competition**: Instead of individual protocols fighting for [[liquidity_providers_and_incentives | liquidity]], the 4pool represents a collaborative effort <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **UST as Collateralized Asset**: The partnership allows [[usdb_stablecoin_mechanism | UST]] to become a collateralized asset for Frax <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Decentralized Stablecoin Dominance**: It aims to establish Frax and [[usdb_stablecoin_mechanism | UST]] as leading decentralized [[types_of_stablecoins_and_their_distinctions | stablecoins]] within the high-liquidity Ethereum DeFi ecosystem <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Facilitating Bitcoin Purchases**: A deep and liquid 4pool would enable efficient swaps of [[usdb_stablecoin_mechanism | UST]] for USDT, crucial for large-scale Bitcoin purchases planned by entities like the Luna Foundation Guard (LFG) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. This ensures sufficient [[liquidity_providers_and_incentives | liquidity]] for such transactions, as direct purchases on the native blockchain may lack the necessary depth <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.