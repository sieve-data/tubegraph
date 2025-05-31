---
title: Earning interest on aUST bids on Kajiras Orca
videoId: EsKdSbuXE7g
---

From: [[when-shift-happens]] <br/> 

Kujira's Orca platform has introduced aUST bids, allowing users to earn yield while participating in liquidation events <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This feature comes with several key updates and a new yield-earning mechanism <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Key Updates for aUST Bids

Upon the launch of aUST bids, several significant changes were implemented:
*   **Conversion of Existing Bids**: Any bids previously held in UST can be converted to aUST bids with a single click via the new aUST dashboard <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   **Unlimited Bids**: Users now have access to unlimited aUST bids <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **Reduced Fees**: Fees across the platform have been reduced by 50%, resulting in a 0.5% fee paid in the bAsset being withdrawn <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Risk Ratio Calculation

Following [[Anchor Protocol staking and borrowing | Anchor Protocol's]] increase of the loan-to-value (LTV) max for bLUNA to 80% (from 60%), while bETH remains at 60%, Kujira's Orca has transitioned to a "risk ratio" ideology <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>. The risk ratio is essentially the percentage borrowed against the maximum available to borrow <a class="yt-timestamp" data-t="01:31:02">[01:31:02]</a>.

For example, if a user holds bLUNA and bETH at equal values (e.g., 1,000 UST of each), the risk ratio would be 70%, which is the average of 60% for bETH and 80% for bLUNA <a class="yt-timestamp" data-t="01:39:02">[01:39:02]</a>. A 100% risk ratio indicates at-risk capital <a class="yt-timestamp" data-t="01:56:02">[01:56:02]</a>.

## [[user_interface_updates_for_bidding_on_aUST | User Interface Updates]]

The Orca platform's user interface has been updated to accommodate aUST bids <a class="yt-timestamp" data-t="02:29:02">[02:29:02]</a>:
*   **Bid Amount Selection**: A dropdown menu in the bid amount section now allows users to select between UST or aUST <a class="yt-timestamp" data-t="02:08:02">[02:08:02]</a>.
*   **Active Bid Indication**: The bar chart no longer turns purple for an active bid; instead, a red dot at the top of the bar indicates the active bid location <a class="yt-timestamp" data-t="02:17:02">[02:17:02]</a>.
*   **Premium Pool Reflection**: Bars now show the composition of the premium pool: light blue for UST and lime green for aUST <a class="yt-timestamp" data-t="02:31:02">[02:31:02]</a>.
*   **aUST Tab**: A dedicated aUST tab at the top enables direct deposits and withdrawals from Anchor, displays all aUST bids, and allows conversion of existing UST bids to aUST <a class="yt-timestamp" data-t="02:50:02">[02:50:02]</a>.

## Bid Threshold and Automated Activation

When placing an aUST bid, users select a threshold labeled "low," "medium," or "high" <a class="yt-timestamp" data-t="03:10:02">[03:10:02]</a>. This refers to the risk of *missing out* on liquidations <a class="yt-timestamp" data-t="03:21:02">[03:21:02]</a>.

To circumvent [[Anchor Protocol staking and borrowing | Anchor's]] 10-minute activation timer for liquidations, Kujira has integrated a mechanism into Orca for [[Orca platforms process of automated bids and premiums | automated bid activation]] <a class="yt-timestamp" data-t="03:35:02">[03:35:02]</a>. Bids become active when the selected aUST bid threshold is met <a class="yt-timestamp" data-t="03:58:02">[03:58:02]</a>.

For instance, if "low" is selected, aUST bids will stop earning Anchor yield and will be placed into the premium pool when there are 3 million UST of loans at a 93% risk ratio <a class="yt-timestamp" data-t="04:02:02">[04:02:02]</a>.

## Earning Yield on aUST Bids

The yield earning process for aUST bids depends on their activation status:
*   **Inactive Bids**: When bids are not active, they earn yield on Orca Earn <a class="yt-timestamp" data-t="03:51:02">[03:51:02]</a>. Specifically, when funds are earning in Anchor, they generate a 20% yield <a class="yt-timestamp" data-t="05:18:02">[05:18:02]</a>.
*   **Active Bids**: While bids are active in the premium pool, they do not earn Anchor yield <a class="yt-timestamp" data-t="04:18:02">[04:18:02]</a>.
*   **Retracted Bids**: If a liquidation does not occur at the selected premium and the risk ratio drops to less than 100k at-risk, bids are retracted and begin earning aUST yield again <a class="yt-timestamp" data-t="04:22:02">[04:22:02]</a>. If a liquidation does happen, users can claim their bAssets <a class="yt-timestamp" data-t="04:35:02">[04:35:02]</a>.

### Trade-offs for Yield Exposure

The choice of risk ratio impacts both the chance of bids being filled and yield earnings <a class="yt-timestamp" data-t="04:43:02">[04:43:02]</a>:
*   **Low Risk Ratio**: Setting a low risk ratio increases the chance of bids being filled in flash liquidation events. However, it may result in earning less Orca or Anchor yield in the meantime <a class="yt-timestamp" data-t="04:46:02">[04:46:02]</a>.
*   **High Risk Ratio**: Conversely, a high risk ratio offers more exposure to yield, but bids might not be activated in time during flash liquidation events <a class="yt-timestamp" data-t="04:58:02">[04:58:02]</a>. A balanced approach is often recommended <a class="yt-timestamp" data-t="05:08:02">[05:08:02]</a>.

When funds are in Orca (meaning not active and earning Anchor yield), they earn a 15% yield. The remaining portion of the yield makes its way back to Kuji stakers, adding utility to the Kujira token <a class="yt-timestamp" data-t="05:22:02">[05:22:02]</a>.