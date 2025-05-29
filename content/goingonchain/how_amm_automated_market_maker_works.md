---
title: How AMM Automated Market Maker works
videoId: Iulawbmbv6s
---

From: [[goingonchain]] <br/> 

An [[understanding_sudoswaps_automated_market_maker_amm_model | Automated Market Maker]] (AMM) is a core component of decentralized finance (DeFi) that facilitates token swaps and liquidity provision. It functions similarly to platforms like ThorSwap, SushiSwap, and Uniswap <a class="yt-timestamp" data-t="00:00:16"></a>.

## How AMMs Work

In a typical AMM, users can swap tokens <a class="yt-timestamp" data-t="00:00:34"></a>. This functionality relies on liquidity providers (LPs) who supply assets to liquidity pools <a class="yt-timestamp" data-t="00:00:36"></a>. LPs add liquidity to these pools, enabling others to trade <a class="yt-timestamp" data-t="00:00:43"></a>.

### The Problem with Traditional AMM Liquidity
Historically, AMMs faced a challenge where liquidity providers would enter a pool, earn tokens as incentives, and then "dump" these tokens before moving to other pools <a class="yt-timestamp" data-t="00:00:52"></a>. This behavior could negatively impact the project's stability <a class="yt-timestamp" data-t="00:00:56"></a>.

## Vader's Unique AMM Approach

Vader is a DeFi "all-in-one" protocol that combines elements from ThorChain and Luna <a class="yt-timestamp" data-t="00:00:03"></a>. It utilizes three distinct components to ensure liquidity providers remain committed to the platform <a class="yt-timestamp" data-t="00:00:59"></a>:
1.  Bond Sales <a class="yt-timestamp" data-t="00:01:05"></a>
2.  USDV Stablecoin <a class="yt-timestamp" data-t="00:01:19"></a>
3.  Continuous Liquidity Pools (CLP) <a class="yt-timestamp" data-t="00:01:24"></a>

### USDV Stablecoin Mechanism
Vader's stablecoin, USDV, is the base asset for its liquidity pools <a class="yt-timestamp" data-t="00:01:21"></a>. Its mechanism is similar to how Luna and [[ust_mechanism_and_market_panic | UST worked]] <a class="yt-timestamp" data-t="00:01:43"></a>. The supply of Vader tokens is directly tied to the supply of USDV <a class="yt-timestamp" data-t="00:01:47"></a>:
*   **USDV above $1:** If USDV's value exceeds $1, Vader supply is burned to mint more USDV. This increases the USDV supply, bringing its value back to $1. A reduced Vader supply simultaneously drives up its price <a class="yt-timestamp" data-t="00:01:55"></a>.
*   **USDV below $1:** If USDV's value drops below $1, USDV supply is burned to mint Vader. This lowers the USDV supply, restoring its peg. However, it also increases the Vader supply, causing its price to drop <a class="yt-timestamp" data-t="00:02:14"></a>.
*   In essence, higher demand for USDV translates to a better price for Vader <a class="yt-timestamp" data-t="00:02:27"></a>. The demand for USDV stems from its use as the base asset in Vader's AMM <a class="yt-timestamp" data-t="00:03:14"></a>.

### Vader's AMM: An EVM Version of Thorchain
The Vader AMM operates as an EVM (Ethereum Virtual Machine) version of the Thorchain AMM <a class="yt-timestamp" data-t="00:02:43"></a>.
*   It specifically facilitates Continuous Liquidity Pools (CLP) <a class="yt-timestamp" data-t="00:02:48"></a>.
*   CLPs are designed to maximize the yield generated for liquidity providers, treating them as "first-class citizens" <a class="yt-timestamp" data-t="00:01:27"></a>.
*   Similar to Thorchain, where LPs must provide an asset alongside its native token (RUNE), Vader requires LPs to provide an asset together with USDV <a class="yt-timestamp" data-t="00:03:00"></a>. This requirement directly drives demand for USDV <a class="yt-timestamp" data-t="00:03:17"></a>.

### Bond Sales for Liquidity Protection
To prevent liquidity from leaving the platform, Vader utilizes bond sales, inspired by Olympus Pro <a class="yt-timestamp" data-t="00:01:05"></a>.
*   This mechanism allows users to mint Vader tokens at a discount, subject to a vesting period <a class="yt-timestamp" data-t="00:01:10"></a>.
*   Through these sales, Vader buys liquidity from liquidity providers <a class="yt-timestamp" data-t="00:03:43"></a>. LPs can sell their liquidity pool tokens and receive discounted Vader tokens in return <a class="yt-timestamp" data-t="00:03:47"></a>.
*   By purchasing these liquidity pool tokens, the protocol itself owns the liquidity, ensuring it remains within the project <a class="yt-timestamp" data-t="00:03:52"></a>.
*   The Vader tokens used for bond sales originate from the community liquidity incentive allocation <a class="yt-timestamp" data-t="00:04:00"></a>. These sales occur at fixed times and are not perpetual <a class="yt-timestamp" data-t="00:04:05"></a>. Vader's first bond sale sold out in 30 minutes <a class="yt-timestamp" data-t="00:04:14"></a>.

By integrating these three components, Vader aims to create an AMM that offers deep liquidity, provides 100 days of impermanent loss protection for LPs, and maintains a stablecoin with pre-populated demand <a class="yt-timestamp" data-t="00:04:19"></a>.