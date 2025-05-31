---
title: Anchor Protocol loantovalue changes
videoId: EsKdSbuXE7g
---

From: [[when-shift-happens]] <br/> 

Kujira's Orca platform has introduced AUST bids, alongside significant updates influenced by changes in [[anchor_protocol_staking_and_borrowing | Anchor Protocol]]'s loan-to-value (LTV) mechanics <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. These changes include new metrics like the risk ratio and yield-earning aspects <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

Key updates include:
*   Existing bids in UST can be converted to AUST bids via a new dashboard <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Unlimited AUST bids are now available <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   Fees have been reduced by 50% across the board, resulting in a 0.5% fee paid in the bAsset being withdrawn <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Loan-to-Value (LTV) and Risk Ratio

[[anchor_protocol_staking_and_borrowing | Anchor Protocol]] increased the maximum LTV for bLUNA to 80% from its original 60%, while bETH remains at 60% <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This adjustment necessitated a change in how LTV is calculated, leading Kujira's Orca to adopt a "risk ratio" ideology <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

The risk ratio is defined as the percentage borrowed against the maximum amount available to borrow <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. For example, if a user holds bLUNA and bETH at equal values (e.g., 1,000 UST each), the risk ratio would be 70% (the average of bETH's 60% and bLUNA's 80%) <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. A 100% risk ratio indicates "at risk capital" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### User Interface Updates

The Orca dashboard has been updated to reflect these changes:
*   A dropdown menu in the bid amount section allows selection between UST or AUST <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Active bids are now indicated by a red dot at the top of the bar chart, replacing the previous purple coloration <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   The bar chart visually distinguishes between UST (light blue) and AUST (lime green) within the premium pool <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   A new AUST tab at the top enables direct deposits and withdrawals from [[anchor_protocol_staking_and_borrowing | Anchor Protocol]], displays all AUST bids, and facilitates conversion of existing UST bids to AUST <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## AUST Bid Thresholds and Yield

When placing an AUST bid, users select a bid threshold (low, medium, or high) <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This threshold refers to the risk of missing out on liquidations <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Due to [[anchor_protocol_staking_and_borrowing | Anchor Protocol]]'s 10-minute activation timer for liquidations, Orca automatically activates bids when the selected threshold is met <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

AUST bids earn yield on Orca when they are not active <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. They become active when the AUST bid threshold is met <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. For example, selecting a "low" threshold means AUST bids stop earning [[anchor_protocol_staking_and_borrowing | Anchor Protocol]] yield and are placed into the premium pool when there are 3 million UST of loans at a 93% risk ratio <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. While bids are active, they do not earn [[anchor_protocol_staking_and_borrowing | Anchor Protocol]] yield <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. If a liquidation does not occur and the at-risk capital drops below 100k UST, bids are retracted and resume earning UST yield <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. If a liquidation happens, users can claim their bAssets <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

### Strategic Considerations for Bid Thresholds

Setting a low risk ratio threshold increases the chance of bids being filled during a flash liquidation event <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. However, the trade-off is potentially earning less Orca or [[anchor_protocol_staking_and_borrowing | Anchor Protocol]] yield in the interim <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. Conversely, a high threshold offers more exposure to yield but risks the bid not activating in time for flash liquidations <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. Finding a middle ground is often recommended to balance these factors <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

Funds earning on [[anchor_protocol_staking_and_borrowing | Anchor Protocol]] generate a 20% yield, while funds in Orca earn 15% yield <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. The remaining yield contributes to Kujira stakers, adding utility to the Kujira token <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.