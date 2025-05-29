---
title: Types of Stablecoins
videoId: tIjZzwCB-vo
---

From: [[goingonchain]] <br/> 

To understand platforms like X Dollar, it's essential to first grasp the different types of stablecoins <a class="yt-timestamp" data-t="00:00:24"></a>. There are three primary categories of stablecoins <a class="yt-timestamp" data-t="00:00:27"></a>.

## 1. Fiat-Backed Stablecoins
This type of stablecoin is backed by traditional fiat currency <a class="yt-timestamp" data-t="00:00:29"></a>.
*   **Mechanism**: For every unit of the stablecoin in circulation, there is an equivalent amount of fiat currency held in reserve <a class="yt-timestamp" data-t="00:00:31"></a>.
*   **Example**: USDC is a fiat-backed stablecoin, where each USDC is controlled by Circle, the company that owns it <a class="yt-timestamp" data-t="00:00:32"></a>.

## 2. Algorithmic Stablecoins
Algorithmic stablecoins maintain their peg through automated algorithms <a class="yt-timestamp" data-t="00:00:38"></a>.
*   **Mechanism**: Their supply is typically backed by a volatile cryptocurrency, with an algorithm managing the supply and demand to maintain stability <a class="yt-timestamp" data-t="00:00:42"></a>.
*   **Example**: Terra UST was a well-known algorithmic stablecoin, where the supply of UST was backed by the supply of Luna <a class="yt-timestamp" data-t="00:00:40"></a>.

## 3. Crypto-Backed Stablecoins
This category of stablecoin is backed by other cryptocurrencies <a class="yt-timestamp" data-t="00:00:47"></a>.
*   **Mechanism**: Users typically overcollateralize their loans with cryptocurrency to borrow the stablecoin. The collateral ratio is crucial here <a class="yt-timestamp" data-t="00:00:54"></a>.
*   **Example**: Dai is a famous example; to borrow $500 worth of Dai, a user would need $1,000 worth of ETH, resulting in a 200% collateral ratio <a class="yt-timestamp" data-t="00:00:50"></a>.
*   **X Dollar**: The X Dollar protocol (which issues stablecoins like xUSD in v1 and XIM in v2) falls into the crypto-backed category <a class="yt-timestamp" data-t="00:01:00"></a>. It aims to be multi-chain and multi-collateral, allowing users to borrow stablecoins using assets like Matic, Avalanche, or Ethereum with a low collateral ratio of 110% and zero percent interest, although there is a one-time fixed fee <a class="yt-timestamp" data-t="00:01:03"></a>.

### Use Cases for X Dollar
X Dollar offers various use cases, including:
*   **Borrowing Stablecoins**: Users can borrow XIM (X Dollar's v2 stablecoin) by using ETH as collateral, and in the future, Matic when it connects with Polygon <a class="yt-timestamp" data-t="00:03:34"></a>. This is ideal for long-term borrowing due to the one-time fee <a class="yt-timestamp" data-t="00:02:38"></a>.
*   **Providing Liquidity (Stability Pool)**: Users can supply XIM into the stability pool, earning MATIC and Space tokens. This pool is used by the protocol to purchase liquidated assets at a discount <a class="yt-timestamp" data-t="00:02:51"></a>.
*   **Staking Protocol Tokens**: Staking the protocol token, Space, yields xSpace, which is a governance token. This allows users to participate in governance votes and earn a portion of the protocol's revenue <a class="yt-timestamp" data-t="00:03:11"></a>. The longer the lock-up period for staking, the more xSpace is received <a class="yt-timestamp" data-t="00:04:02"></a>.
*   **[[using_stablecoins_in_yield_farming | Yield Farming]]**: Users can farm Space by staking XIM 3 Curve LP tokens via Curve <a class="yt-timestamp" data-t="00:04:09"></a>.

### Key Features of X Dollar V2
*   **X Home**: Provides a dashboard showing platform metrics like protocol earnings and collateral ratio <a class="yt-timestamp" data-t="00:03:26"></a>.
*   **X Bank**: The interface for borrowing XIM with collateral like ETH <a class="yt-timestamp" data-t="00:03:34"></a>.
*   **X Pool**: Where users supply XIM into the stability pool to earn more ETH and Space <a class="yt-timestamp" data-t="00:03:41"></a>.
*   **X Stake**: For staking Space to receive xSpace <a class="yt-timestamp" data-t="00:03:54"></a>.
*   **X Farm**: For [[using_stablecoins_in_yield_farming | farming]] Space tokens <a class="yt-timestamp" data-t="00:04:09"></a>.
*   **Liquidation**: Allows users to liquidate undercollateralized positions when the collateral ratio is low (e.g., close to 110%). The liquidator pays xUSD and receives the collateral at a discount <a class="yt-timestamp" data-t="00:04:26"></a>.
*   **Redemption**: Enables users to participate in arbitrage events, particularly when xUSD depegs. If xUSD trades at 90 cents, a user can redeem it at the protocol for a value of one dollar in collateral <a class="yt-timestamp" data-t="00:04:40"></a>. This function is typically carried out by bots but is accessible to users <a class="yt-timestamp" data-t="00:04:54"></a>. Redemption is distinct from repaying a loan <a class="yt-timestamp" data-t="00:05:01"></a>.

X Dollar V2 is currently on Ethereum, with plans to expand to other chains <a class="yt-timestamp" data-t="00:05:06"></a>.