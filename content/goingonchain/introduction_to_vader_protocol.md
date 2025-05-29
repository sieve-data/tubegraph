---
title: Introduction to Vader Protocol
videoId: Iulawbmbv6s
---

From: [[goingonchain]] <br/> 

Vader Protocol is a DeFi all-in-one protocol that combines concepts from ThorChain and Luna to create an Automated Market Maker (AMM) <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It functions similarly to ThorSwap, SushiSwap, and UniSwap, but distinguishes itself through its [[AMM and Vaders Unique Components | unique components]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Understanding Automated Market Makers (AMMs)

An AMM, like PancakeSwap, allows users to swap tokens and become liquidity providers (LPs) <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. LPs provide liquidity for token swaps <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
A common issue with traditional AMMs is that LPs often provide liquidity to earn tokens, then "farm and dump" them, which negatively impacts the project <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Vader Protocol's Unique Components

Vader Protocol utilizes three distinct components to ensure liquidity providers remain engaged and to maintain project stability <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>:

### 1. Bond Sales

Vader employs a system similar to Olympus Pro, where users can mint Vader tokens at a discount subject to a vesting period <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This mechanism helps the Vader Protocol buy back its own liquidity <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### 2. USDV Stablecoin

USDV is Vader's stablecoin and serves as the base asset for its liquidity pools <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Its mechanism is comparable to how Luna and UST operate, where the supply of Vader is directly linked to the supply of USDV <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

*   **Pegging Mechanism:** One USDV is pegged to one USD <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   If USDV exceeds one dollar, Vader supply is burned to mint more USDV, increasing USDV supply and bringing its value back to the peg <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This also reduces Vader supply, causing its price to rise <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
    *   If USDV falls below one dollar, USDV supply is burned to mint Vader, decreasing USDV supply and restoring the peg <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This increases Vader supply, leading to a drop in its price <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Impact on Vader Price:** Higher demand for USDV generally leads to a better price for Vader <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### 3. Continuous Liquidity Pools (CLP) AMM

The Vader AMM is an EVM (Ethereum Virtual Machine) version of the ThorChain AMM <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. It facilitates CLPs, which are designed to maximize the yield for liquidity pool providers <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. It offers higher fees, especially for LPs who hold USDV <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. To provide liquidity on Vader, users must provide an asset paired with USDV, similar to how ThorChain requires its native RUNE token <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This requirement drives demand for USDV <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Protecting Liquidity through Bond Sales

Vader's [[Vader Tokenomics and Bond Sales | bond sales]] aim to prevent liquidity from leaving the protocol <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Unlike older methods where projects incentivize LPs with tokens that are often dumped, Vader directly buys liquidity from LPs via these sales <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. LPs sell their liquidity pool tokens to Vader in exchange for discounted Vader tokens <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This allows the protocol to own the liquidity pool tokens, ensuring that liquidity remains within the project <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The Vader tokens sold through bond sales come from the community liquidity incentive allocation <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. These sales occur at fixed times and are not perpetual; Vader's first bond sale sold out in 30 minutes <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## Overall Benefits

By integrating these three components, Vader Protocol forms an AMM that offers:
*   Deep liquidity <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
*   Impermanent loss protection for 100 days for liquidity providers <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>
*   A stablecoin (USDV) with pre-populated demand <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>

## Team and Tokenomics

The Vader Protocol team is anonymous, with Dogs Mervin serving as the community lead on Twitter <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Vader Tokenomics
The [[Vader Tokenomics and Bond Sales | Vader tokenomics]] model includes:
*   **vE Holders:** Considered early investors, vE holders converted their ETH into vE tokens and can exchange vE for Vader tokens <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. They receive 50% upfront and 50% vested over one year <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
*   **Team Allocation:** The team receives a 10% allocation with a two-year linear vesting period <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Ecosystem and Liquidity Incentive:** The remaining tokens are allocated for ecosystem development and liquidity incentives, from which the bond sales are sourced <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Closing Thoughts

Vader Protocol presents an interesting approach by integrating the best aspects of different DeFi products <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. However, a significant [[Challenges and Considerations for Vader Protocol | challenge]] lies in its execution <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, particularly with the anonymous team and what some might view as a relatively short vesting period <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

*Disclaimer: This is not financial advice. Always conduct your own research before making investment decisions <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.*