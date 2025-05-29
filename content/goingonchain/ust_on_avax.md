---
title: UST on AVAX
videoId: HWTUANwNhJ4
---

From: [[goingonchain]] <br/> 

UST (TerraUSD) can be utilized on the Avalanche (AVAX) blockchain, particularly through its integration with Anchor Protocol. This allows users to deposit UST for yield or borrow UST using Avalanche-native collateral.

## Obtaining UST on Avalanche
Previously, users would obtain Wormhole UST from Curve's Factory 55 pool to use with Anchor on Avalanche <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. However, it is now easier to acquire UST directly from Trader Joe <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Important Distinction on Trader Joe
When acquiring UST on Trader Joe, users must pay attention to the two types available:
*   `ust.axl` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   `ust` (without `.axl` suffix) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

For deposits into [[anchor_integration_on_avalanche | Anchor on Avalanche]], the `ust` (without `.axl`) version is required as it is the one accepted by the protocol <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>, <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Depositing and Withdrawing UST on Anchor (AVAX Chain)
Once the correct `ust` is obtained, it can be deposited directly into [[anchor_integration_on_avalanche | Anchor on the Avalanche chain]] <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. Withdrawals from Anchor on Avalanche will return UST directly to the user's Metamask wallet <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>, from which it can be swapped for other crypto assets on platforms like Trader Joe <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Dynamic Saving Rate on Anchor
The Anchor saving rate, which applies to UST deposits, is no longer fixed at 19.5% <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. It is now dynamically adjusted monthly based on a formula <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

Key details of the dynamic rate:
*   **Monthly Adjustment:** Max change is +/- 1.5% <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Lowest Rate:** 15% <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Highest Rate:** 20% <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Expected Trend:** Due to a downward trend in the yield reserve, the interest rate was expected to start dropping in May <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Reason for Drop:** More people are depositing than borrowing on Anchor, leading to a strain on the yield reserve <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Solution:** Anchor aims to add more collateral options to encourage borrowing and narrow this gap <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Borrowing UST with AVAX Collateral
Users can borrow UST by providing [[avax_collateral_and_borrowing_on_anchor | staked AVAX (sAVAX)]] as collateral on [[anchor_integration_on_avalanche | Anchor on the Avalanche chain]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

To obtain sAVAX:
1.  Go to Benqi Finance <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
2.  Navigate to their Liquid Staking section <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>, <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
3.  Stake AVAX to receive sAVAX <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>, <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
    *   sAVAX is a yield-bearing token, earning approximately 7.2% APR <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
4.  Bring the sAVAX back to Anchor to provide it as collateral <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

The recommended Loan-to-Value (LTV) ratio for borrowing against sAVAX is typically 75% <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>, <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### wAVAX on Terra Chain
While it is possible to bridge sAVAX across the Wormhole to the Terra chain, where it becomes wAVAX (wrapped sAVAX), this process is more cumbersome and generally unnecessary unless there are specific "money lego" opportunities on Terra that utilize wAVAX <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>, <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>, <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. The direct connection of Anchor to the Avalanche chain for depositing and borrowing remains the most convenient method <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Market Sentiment
The willingness to borrow, even with additional collateral options, can be affected by market sentiment. In a bear market, people are typically less willing to take on risk or borrow <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.