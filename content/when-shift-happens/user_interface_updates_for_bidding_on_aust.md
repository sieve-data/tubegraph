---
title: User interface updates for bidding on aUST
videoId: EsKdSbuXE7g
---

From: [[when-shift-happens]] <br/> 

Kajira's Orca platform has rolled out significant user interface (UI) updates to support the introduction of [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]], aiming to enhance user experience and provide clearer visual information <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Converting Existing UST Bids

Users with existing UST bids can easily convert them to [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]]. This conversion is performed directly from the new aUST dashboard with a single click <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Dashboard Enhancements

Several visual elements on the Orca dashboard have been updated:

### Bid Amount Dropdown
A new dropdown menu has been added to the bid amount section, allowing users to select between UST or [[earning_interest_on_aust_bids_on_kajiras_orca | aUST]] for their bids <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Active Bid Indicator
The bar chart no longer turns purple to indicate an active bid. Instead, a red dot at the top of the bar now signifies the user's active bid location <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Premium Pool Composition
The UI bars have been updated to visually represent the composition of the [[orca_platforms_process_of_automated_bids_and_premiums | premium pool]] <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>:
*   **Light Blue**: Represents the portion of the premium pool made up of UST <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Lime Green**: Indicates the portion made up of [[earning_interest_on_aust_bids_on_kajiras_orca | aUST]] <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

This visual update allows users to quickly assess information for their bidding strategy <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## aUST Tab

A dedicated aUST tab has been introduced at the top of the interface <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This tab provides comprehensive functionalities:
*   **Direct Deposit/Withdrawal**: Users can deposit and withdraw funds directly from Anchor Protocol <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Bid Management**: It displays all of a user's [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Conversion**: Allows for the conversion of existing UST bids to [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Bid Threshold Settings

When placing an [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bid]], users are presented with a screen to set their bid threshold <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Options include "low," "medium," and "high" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

This "risk" setting specifically refers to the risk of *missing out* on liquidation events <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Kajira has implemented a mechanism in Orca to automatically activate bids when the selected threshold is met, circumventing Anchor's 10-minute activation timer <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Impact of Threshold Settings
*   **Low Risk Ratio**: Setting a low [[risk_ratio_and_liquidation_strategy_for_aust_bids | risk ratio]] (e.g., bids activating when 3 million UST of loans are at a 93% [[risk_ratio_and_liquidation_strategy_for_aust_bids | risk ratio]] <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>) increases the chance of bids being filled during flash liquidation events <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. However, this may lead to less Orca or Anchor yield being earned in the interim <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **High Risk Ratio**: A higher [[risk_ratio_and_liquidation_strategy_for_aust_bids | risk ratio]] offers more exposure to yield, but bids might not activate in time during flash liquidation events <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

The recommended approach is to find a middle ground to balance these factors <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

When [[earning_interest_on_aust_bids_on_kajiras_orca | aUST bids]] are active, they do not earn Anchor yield <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. If a liquidation does not occur and the [[risk_ratio_and_liquidation_strategy_for_aust_bids | risk ratio]] drops, bids are retracted and resume earning [[earning_interest_on_aust_bids_on_kajiras_orca | aUST]] yield <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. If a liquidation happens, users can claim their b-assets <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

The continuous development and rapid feature deployment by the Kajira team address community concerns and aim to provide an improved user experience <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.