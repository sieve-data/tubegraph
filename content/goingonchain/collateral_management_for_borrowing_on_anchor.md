---
title: Collateral management for borrowing on Anchor
videoId: HWTUANwNhJ4
---

From: [[goingonchain]] <br/> 

Anchor Protocol is undergoing changes to its operations, particularly concerning its saving rate and borrowing mechanisms <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The protocol is shifting from a fixed 19.5% saving rate to a [[interest_rates_and_yields_on_anchor|dynamic saving rate]] that adjusts monthly based on the yield reserve <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This adjustment, with a maximum monthly change of plus or minus 1.5%, will see the rate fluctuate between a minimum of 15% and a maximum of 20% <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

> [!NOTE] Dynamic Saving Rate
> The yield reserve is currently on a downward trend, indicating that [[interest_rates_and_yields_on_anchor|interest rates]] are likely to start dropping around May <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This trend is attributed to more users depositing funds than borrowing <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. To narrow this gap and ensure [[strategies_to_maintain_anchor_sustainability|Anchor's sustainability]], the protocol aims to encourage more borrowing <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Expanding Collateral Options to Boost Borrowing

To increase borrowing activity, Anchor is focused on adding more collateral options <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. By expanding the range of acceptable collateral, Anchor aims to attract users from other blockchain ecosystems <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

> [!INFO] Current Borrowing Environment
> Even with additional collateral options, market sentiment plays a significant role. In a bear market, individuals are generally less willing to take risks or engage in [[borrowing_against_crypto_assets|borrowing against crypto assets]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## Utilizing Staked AVAX (stAVAX) as Collateral on Anchor

One significant addition to Anchor's collateral options is staked [[introduction_of_new_collateral_like_avex|AVAX]] (stAVAX), allowing users to [[borrowing_against_crypto_assets|borrow UST]] against it <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Obtaining stAVAX for Collateral

To use stAVAX as [[collateral_and_staking_rewards_in_anchor|collateral on Anchor]], users can obtain it via Benqi <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>:
1.  Navigate to Benqi's liquid staking section <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
2.  Stake [[introduction_of_new_collateral_like_avex|AVAX]] to receive sAVAX (staked [[introduction_of_new_collateral_like_avex|AVAX]]) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  sAVAX is a yield-bearing token, currently earning approximately 7.2% APR <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
4.  Once sAVAX tokens are acquired, they can be brought back to Anchor to be provided as [[collateral_and_staking_rewards_in_anchor|collateral]] for borrowing <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### Borrowing Against stAVAX

When providing stAVAX as [[collateral_and_staking_rewards_in_anchor|collateral]], Anchor recommends a target borrow ratio (TBR) of 75% <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. For example, if a user has provided stAVAX collateral, they can increase their borrow amount up to this recommended ratio <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Cross-Chain Considerations for stAVAX

While Anchor on the [[introduction_of_new_collateral_like_avex|AVAX]] chain directly accepts stAVAX, a wrapped version, wAVAX, is also available on the Terra chain <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. However, using stAVAX on the Terra chain requires bridging it via a wormhole, which is generally more complex and often unnecessary for most users <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Connecting [[connecting_metamask_for_anchor|Metamask]] directly to the [[introduction_of_new_collateral_like_avex|AVAX]] chain for depositing and borrowing remains the most convenient method <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Summary of Collateral Management Updates

*   Anchor's [[interest_rates_and_yields_on_anchor|interest rates]] will become dynamic, likely starting to change in May, with a minimum of 15% and a maximum of 20% <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   To encourage more borrowing, Anchor is expanding its [[collateral_and_staking_rewards_in_anchor|collateral]] options <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   Users can now use sAVAX (staked [[introduction_of_new_collateral_like_avex|AVAX]]) as [[collateral_and_staking_rewards_in_anchor|collateral]] for [[borrowing_against_crypto_assets|borrowing]] on Anchor <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   sAVAX can be obtained through Benqi's liquid staking service <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.