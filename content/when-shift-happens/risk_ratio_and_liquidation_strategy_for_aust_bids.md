---
title: Risk ratio and liquidation strategy for aUST bids
videoId: EsKdSbuXE7g
---

From: [[when-shift-happens]] <br/> 

Kajira Orca has introduced aUST bids, bringing new metrics like the risk ratio and yield-earning aspects to the platform <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. Users can convert existing UST bids to aUST bids with a single click on the new aUST dashboard <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>. There are now unlimited aUST bids available <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>, and fees across the board have been reduced by 50% to a 0.5% fee paid in the b asset being withdrawn <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.

## Understanding the Risk Ratio

The [[understanding_anchor_protocol_and_its_liquidations | Anchor Protocol]] recently increased the maximum Loan-to-Value (LTV) for bLuna to 80% from the original 60%, while bETH remains at 60% <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. This change necessitated a new calculation method, leading Kajira Orca to adopt a risk ratio ideology <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

The risk ratio summarizes the percentage borrowed against the maximum amount available to borrow <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

*   **Example**: If a user has bLuna and bETH at equal values (e.g., 1,000 UST of each), the risk ratio would be 70%. This is the average of bETH's 60% and bLuna's 80% <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. A 100% risk ratio indicates capital at risk <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

## aUST Bid Thresholds and Activation

When placing an aUST bid, users are presented with options for "low," "medium," and "high" thresholds <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. This risk setting refers to the "risk on missing out" on liquidations <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

Kajira has incorporated a mechanism into Orca for [[orca_platforms_process_of_automated_bids_and_premiums | automated bids and premiums]] to bypass Anchor's 10-minute activation timer for liquidations <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. This system allows bids to activate automatically when a user's selected threshold is met <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.

### Bid Activation and Yield Earning

[[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids earn yield on Orca]] when they are not active <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. They become active once the aUST bid threshold is met <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.

For instance, if a user selects a "low" threshold, their aUST bids will stop earning Anchor yield and be placed into the premium pool when there are 3 million UST of loans at a 93% risk ratio <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. While bids are active, they do not earn Anchor yield <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.

*   If a liquidation event does *not* occur at the selected premium, and the risk ratio drops below 100,000 UST at risk, the bids are retracted and start earning aUST yield again <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   If a liquidation *does* happen, Orca proceeds as usual, allowing users to claim their b assets <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>.

## [[impact_of_bid_threshold_settings_on_yield_and_liquidation_outcomes | Impact of Bid Threshold Settings on Yield and Liquidation Outcomes]]

The choice of risk ratio (bid threshold) significantly affects a user's strategy:

*   **Low Risk Ratio**: Setting a low risk ratio increases the chance of bids being filled quickly during a flash liquidation event <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>. However, the trade-off is potentially earning less Orca or Anchor yield in the interim, as bids activate more readily and pause yield earning <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
*   **High Risk Ratio**: Conversely, setting a high risk ratio offers more exposure to yield, but bids may not activate in time during flash liquidation events <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.

A middle-ground setting is generally recommended to balance the benefits of both yield exposure and bid activation during liquidations <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

## Yield Distribution

When funds are earning in Anchor, they yield 20% <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>. When they are active in Orca, they yield 15% <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. The remaining portion of the yield is directed back to KUJI stakers, adding utility to the Kajira token <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.

## [[user_interface_updates_for_bidding_on_aust | User Interface Updates]]

The Orca dashboard has been updated to reflect these changes:

*   A drop-down menu in the bid amount section now allows selection between UST or aUST bids <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
*   The bar chart no longer turns purple for active bids; instead, a red dot at the top of the bar indicates the active bid location <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
*   The bars now display the premium pool composition: light blue for UST and lime green for aUST <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
*   A new aUST tab at the top enables direct deposits and withdrawals from Anchor, shows all aUST bids, and facilitates conversion of existing UST bids to aUST <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.