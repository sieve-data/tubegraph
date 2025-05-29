---
title: AMM and Vaders Unique Components
videoId: Iulawbmbv6s
---

From: [[goingonchain]] <br/> 

[[introduction_to_vader_protocol | Vader Protocol]] is described as a DeFi all-in-one protocol that combines the best aspects of Thorchain and Luna to create its Automated Market Maker (AMM) <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Understanding Automated Market Makers (AMMs)

An AMM, like PancakeSwap, allows users to swap tokens and become liquidity providers <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. For tokens to be swapped, someone must provide the liquidity <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. A common problem with traditional AMMs is that liquidity providers often provide liquidity, earn tokens, and then "dump" them, moving to other pools, which negatively impacts the project <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Vader Protocol's Core Innovations

[[introduction_to_vader_protocol | Vader Protocol]] addresses the issue of liquidity retention by incorporating three unique components designed to encourage liquidity providers to remain on the platform <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>:

1.  **Bond Sales**: Similar to Olympus Pro, these allow users to mint [[introduction_to_vader_protocol | Vader]] tokens at a discount, subject to a vesting period <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This mechanism helps [[introduction_to_vader_protocol | Vader Protocol]] buy back its own liquidity <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
2.  **USDB Stablecoin**: This is the base asset of the liquidity pool <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
3.  **Continuous Liquidity Pools (CLP)**: This method aims to maximize the yield generated for liquidity pool providers, effectively treating them as "first-class citizens" on the platform <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### USDB Stablecoin Mechanism

The supply of [[introduction_to_vader_protocol | Vader]] is directly tied to the supply of USDB, functioning similarly to how Luna and UST operate <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

*   **When USDB > $1**: If USDB trades above its $1 peg, [[introduction_to_vader_protocol | Vader]] supply is burned to mint more USDB <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This increases the supply of USDB, bringing its value back to the peg, and the reduced supply of [[introduction_to_vader_protocol | Vader]] leads to an increase in its price <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **When USDB < $1**: If USDB trades below $1, USDB supply is burned to mint [[introduction_to_vader_protocol | Vader]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This lowers the supply of USDB, restoring the peg, but also increases the supply of [[introduction_to_vader_protocol | Vader]], causing its price to drop <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

In essence, higher demand for USDB results in a better price for [[introduction_to_vader_protocol | Vader]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Continuous Liquidity Pools (CLP) AMM

The [[introduction_to_vader_protocol | Vader]] AMM is an EVM version of the [[comparisons_between_astroport_and_other_amms_like_terraswap_and_uniswap | Thorchain AMM]] <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. It facilitates CLPs and offers higher fees for liquidity providers <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Similar to how [[comparisons_between_astroport_and_other_amms_like_terraswap_and_uniswap | Thorchain AMM]] requires an asset paired with its native RUNE token for liquidity provision, [[introduction_to_vader_protocol | Vader]] requires an asset paired with USDB <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This design makes USDB the base asset, thereby driving demand for it <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### [[vader_tokenomics_and_bond_sales | Bond Sales]] for Protocol-Owned Liquidity

[[vader_tokenomics_and_bond_sales | Bond sales]] are crucial for preventing liquidity from leaving the [[introduction_to_vader_protocol | Vader Protocol]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Instead of projects solely giving tokens to LPs, [[introduction_to_vader_protocol | Vader]] buys liquidity from LPs through its [[vader_tokenomics_and_bond_sales | bond sales]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. LPs sell their liquidity pool tokens to the protocol in exchange for discounted [[introduction_to_vader_protocol | Vader]] tokens <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This allows the protocol to own the liquidity pool tokens, ensuring that liquidity remains within the project <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The [[vader_tokenomics_and_bond_sales | bond sales]] derive their allocation from the community liquidity incentive <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. These sales occur at fixed times and are not perpetual <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## Synergistic Design

By integrating these three components—bond sales, the USDB stablecoin, and continuous liquidity pools—[[introduction_to_vader_protocol | Vader Protocol]] aims to create an AMM that offers deep liquidity, provides impermanent loss protection for liquidity providers (for 100 days), and establishes pre-populated demand for its stablecoin <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This approach is considered an "interesting idea" that combines the best features from various products <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Challenges and Considerations

A key challenge for [[introduction_to_vader_protocol | Vader Protocol]] lies in its execution <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, particularly given that the team behind it is anonymous <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.