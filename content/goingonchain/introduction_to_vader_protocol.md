---
title: Introduction to Vader Protocol
videoId: Iulawbmbv6s
---

From: [[goingonchain]] <br/> 

Vader is presented as a DeFi all-in-one protocol that integrates concepts from Thorchain and Luna <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## What is Vader?

Vader functions as an Automated Market Maker (AMM) <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, akin to ThorSwap, SushiSwap, and UniSwap <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Its uniqueness stems from the specific components it uses to build its AMM <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Traditional AMMs often face an issue where liquidity providers (LPs) farm tokens, then dump them and move to other projects <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. To counter this and ensure LPs stay, Vader incorporates three key components <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>:
1.  **Bond sales** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
2.  **USDB stablecoin** <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>
3.  **Continuous Liquidity Pools (CLP)** for its AMM <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>

### USDB Stablecoin

USDB is Vader's stablecoin and serves as the base asset for its liquidity pools <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Its mechanism is similar to how Luna and UST operated <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>, where the supply of Vader is tied to the supply of USDB <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

*   **Pegging:** One USDB aims to equal one USD <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **If USDB price > $1:** Vader supply is burned to mint more USDB. This increases the supply of USDB, bringing its value back to $1. Simultaneously, the reduced supply of Vader causes its price to increase <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **If USDB price < $1:** USDB supply is burned to mint Vader. This lowers the supply of USDB, helping to restore the peg. However, it also increases the supply of Vader, which can cause the Vader price to drop <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

In essence, higher demand for USDB generally translates to a better price for Vader <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Automated Market Maker (AMM)

Vader's AMM is an EVM (Ethereum Virtual Machine) version of the Thorchain AMM <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. It facilitates Continuous Liquidity Pools (CLP) and offers higher fees for liquidity providers, especially those who are "first-class citizens" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

Similar to Thorchain where LPs provide an asset with its native token (RUNE) <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, Vader requires LPs to provide an asset along with USDB <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This structure drives demand for USDB as it is the base asset in all liquidity pools <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### Bond Sales

To prevent liquidity from leaving the project, Vader utilizes bond sales <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This mechanism allows Vader to buy liquidity from LPs, similar to Olympus Pro <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. LPs can mint Vader at a discount, subject to a vesting period <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

In this process, users sell their liquidity pool tokens to the protocol in exchange for discounted Vader tokens <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This ensures that the protocol owns the liquidity pool tokens, preventing liquidity from exiting the project <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The Vader tokens sold through bond sales come from the community liquidity incentive allocation <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. These bond sales occur at fixed times and are not necessarily perpetual <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>; for example, Vader's first bond sale sold out in 30 minutes <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

The combination of these three components creates an AMM that offers deep liquidity, provides impermanent loss protection for 100 days for LPs, and features a stablecoin with pre-populated demand <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

## Team and [[vader_tokenomics_and_community_aspects | Vader Tokenomics]]

The Vader team remains anonymous <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>, with the community lead identified as "Dogs Mervin" <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

Regarding [[vader_tokenomics_and_community_aspects | Vader Tokenomics]]:
*   **VE Holders:** Early investors ("ve holders") took their ETH and minted it into VE, then used VE to exchange for Vader tokens <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. They received 50% upfront, with 50% vesting over one year <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Team Allocation:** The team's allocation is 10%, with a two-year linear vesting schedule <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Ecosystem and Liquidity Incentive:** The remaining tokens are allocated for ecosystem development and liquidity incentives <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. The bond sales, for instance, draw from this Vader liquidity incentive <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Closing Thoughts

The concept of integrating these three distinct elements is considered very interesting, taking the best aspects from each product <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. However, potential challenges include the anonymous nature of the team <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a> and a vesting period that may be considered somewhat short <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.