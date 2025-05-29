---
title: Anchors dynamic earn rates and yield reserve trends
videoId: HWTUANwNhJ4
---

From: [[goingonchain]] <br/> 

Anchor Protocol has recently undergone significant changes, particularly concerning its saving rate and collateral options <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## [[dynamic_earn_rate_implementation | Dynamic Saving Rate]]

The fixed [[interest_rates_and_yields_on_anchor | Anchor saving rate]] of 19.5% is being replaced by a [[dynamic_earn_rate_implementation | dynamic saving rate]] adjusted based on a formula <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This formula directly links the [[interest_rates_and_yields_on_anchor | earn rate]] to changes in the [[yield_reserve_impact_on_interest_rates | yield reserve]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. For instance, if the [[yield_reserve_impact_on_interest_rates | yield reserve]] increases by 1.5%, the [[interest_rates_and_yields_on_anchor | earn rate]] also goes up by 1.5% <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Conversely, a 1.5% decrease in the [[yield_reserve_impact_on_interest_rates | yield reserve]] leads to a 1.5% drop in the [[interest_rates_and_yields_on_anchor | earn rate]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

These adjustments are made monthly <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. The first adjustment was projected for May, assuming the [[yield_reserve_impact_on_interest_rates | yield reserve]] continued its downward trend in April <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The maximum monthly change permitted is plus or minus 1.5% <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

The new [[interest_rates_and_yields_on_anchor | dynamic saving rate]] has a floor and a ceiling:
*   **Lowest possible rate:** 15% <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   **Maximum possible rate:** 20% <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>

Given the downward trend of the [[yield_reserve_impact_on_interest_rates | yield reserve]], the [[anchor_interest_rate_changes | interest]] rate was expected to start dropping in May <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This trend is primarily due to more users depositing funds than borrowing them <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## [[strategies_to_maintain_anchor_sustainability | Strategies to Maintain Sustainability]]

To address the imbalance between deposits and borrows, Anchor aims to increase borrowing activity <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. A key strategy for this is adding more types of [[collateral_and_staking_rewards_in_anchor | collateral]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. By supporting additional [[collateral_and_staking_rewards_in_anchor | collateral]] options, Anchor can attract users from other ecosystems to borrow UST <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For example, users can now borrow UST using staked AVAX <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

However, market sentiment also plays a significant role <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. In a bear market, users are typically less willing to take risks or borrow, which can impact borrowing rates even with more [[collateral_and_staking_rewards_in_anchor | collateral]] options <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Anchor on Avalanche (AVAX)

Anchor has expanded its operations to the Avalanche (AVAX) chain <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Obtaining UST on AVAX

Previously, obtaining Wormhole UST for Anchor on Avalanche involved using Curve's Factory 55 pool <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Now, users can easily acquire UST from Trader Joe <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

When using Trader Joe, it's crucial to distinguish between two types of UST:
*   `UST.axl` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   `UST` (without `.axl`) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

Anchor on Avalanche only accepts the `UST` token without the `.axl` suffix <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. When depositing funds for [[earning_interest_on_stablecoins | earning interest on stablecoins]], ensure you have the correct UST version <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Withdrawals of UST from Anchor on Avalanche will return to your Metamask wallet, from where you can swap them on platforms like Trader Joe <a class="yt-timestamp" data-t="00:02:55">[00:03:03]</a>.

### Using Staked AVAX as Collateral

On the AVAX chain, you can use staked AVAX (sAVAX) as [[collateral_and_staking_rewards_in_anchor | collateral]] to borrow UST <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Obtaining sAVAX:** sAVAX can be acquired from Benqi's liquid staking platform <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. By staking your AVAX on Benqi, you receive sAVAX, which is a yield-bearing token, currently offering approximately 7.2% APR <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Providing Collateral:** Once you have sAVAX, you can bring it to Anchor on the AVAX chain and provide it as [[collateral_and_staking_rewards_in_anchor | collateral]] for borrowing UST <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The recommended loan-to-value (LTV) ratio is 75% <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

While sAVAX can be bridged via Wormhole to the Terra chain to become wrapped sAVAX (wAVAX), direct use on the AVAX chain for depositing and borrowing is generally more convenient <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Summary

*   The [[anchor_interest_rate_changes | Anchor interest]] rate is transitioning to a [[dynamic_earn_rate_implementation | dynamic earn rate]], likely starting in May <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   The [[interest_rates_and_yields_on_anchor | rate]] will fluctuate between a minimum of 15% and a maximum of 20% <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   On Avalanche, UST can be obtained from Trader Joe (ensure it's the `UST` without `.axl`) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   sAVAX from Benqi liquid staking can be used as [[collateral_and_staking_rewards_in_anchor | collateral]] to borrow on Anchor <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.