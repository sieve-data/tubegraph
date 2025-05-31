---
title: Impact of bid threshold settings on yield and liquidation outcomes
videoId: EsKdSbuXE7g
---

From: [[when-shift-happens]] <br/> 

The Kajira's [[orca_platforms_process_of_automated_bids_and_premiums | Orca]] platform has introduced [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]], which include new metrics such as the [[risk_ratio_and_liquidation_strategy_for_aust_bids | risk ratio]] and [[earning_interest_on_aust_bids_on_kajiras_orca | yield earning]] aspects <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This update allows for unlimited [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, and fees have been reduced by 50 percent to a 0.5 percent fee paid in the b-asset being withdrawn <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Understanding Bid Thresholds

When placing an [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bid]], users are presented with options like "low," "medium," and "high" thresholds <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This "risk" refers to the risk of missing out on liquidations <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

The [[user_interface_updates_for_bidding_on_aust | user interface]] has been updated to reflect how much of the premium pool consists of UST (light blue) and [[earning_interest_on_aust_bids_on_kajiras_orca | aUST]] (lime green) <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. A new [[user_interface_updates_for_bidding_on_aust | aUST tab]] at the top allows direct deposit and withdrawal from Anchor, shows all [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]], and facilitates converting existing UST bids to [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]] <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Automated Bid Activation

Due to Anchor's 10-minute activation timer for liquidation contracts <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, Kajira has built a mechanism into [[orca_platforms_process_of_automated_bids_and_premiums | Orca]] to automatically activate bids when a selected threshold is met <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]] on [[orca_platforms_process_of_automated_bids_and_premiums | Orca]] earn yield when they are not active <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

For example, if a "low" threshold is selected, [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]] stop earning Anchor yield and are placed into the premium pool when there are 3 million UST of loans at a 93% [[risk_ratio_and_liquidation_strategy_for_aust_bids | risk ratio]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. When bids are active, they do not earn Anchor yield <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

If liquidation does not occur at the selected premium and the [[risk_ratio_and_liquidation_strategy_for_aust_bids | risk ratio]] drops to less than 100k at risk, bids are retracted and begin earning [[earning_interest_on_aust_bids_on_kajiras_orca | aUST yield]] again <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. If liquidation happens, users can claim their b-assets <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## Impact on Yield and Liquidation Outcomes

The chosen bid threshold directly impacts the balance between potential liquidation gains and continuous [[earning_interest_on_aust_bids_on_kajiras_orca | yield earning]].

*   **Low [[risk_ratio_and_liquidation_strategy_for_aust_bids | Risk Ratio]] Setting**: Setting the [[risk_ratio_and_liquidation_strategy_for_aust_bids | risk ratio]] low increases the chance of bids being filled during a flash liquidation event <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. However, the trade-off is that users might earn less [[orca_platforms_process_of_automated_bids_and_premiums | Orca]] or Anchor yield in the meantime <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **High [[risk_ratio_and_liquidation_strategy_for_aust_bids | Risk Ratio]] Setting**: Conversely, setting the [[risk_ratio_and_liquidation_strategy_for_aust_bids | risk ratio]] high provides more exposure to yield <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The drawback is that the bid might not be activated in time during flash liquidation events <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

A middle-ground setting is generally recommended to balance the benefits of both scenarios <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Yield Rates

*   **Anchor Yield**: When funds are earning in Anchor, they yield 20% <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **[[orca_platforms_process_of_automated_bids_and_premiums | Orca]] Yield**: When funds are in [[orca_platforms_process_of_automated_bids_and_premiums | Orca]] (active bids), they yield 15% <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. The remainder of the yield goes back to Kuji stakers, adding utility to the Kujira token <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.