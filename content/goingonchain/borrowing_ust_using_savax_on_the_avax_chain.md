---
title: Borrowing UST using SAVAX on the AVAX chain
videoId: HWTUANwNhJ4
---

From: [[goingonchain]] <br/> 

Anchor Protocol has undergone significant changes, impacting its saving rate and introducing new borrowing opportunities on different chains, including Avalanche (AVAX).

## Anchor Protocol Dynamic Saving Rate

Anchor Protocol's saving rate is no longer fixed at 19.5% <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It is now adjusted monthly based on a formula tied to the yield reserve <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a> <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

Key adjustments:
*   **Adjustment Trigger** The first adjustment was expected in May, assuming the yield reserve continued its downward trend <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a> <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Rate Fluctuation** The maximum monthly change is plus or minus 1.5% <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The lowest the rate can drop is 15%, and the maximum it can reach is 20% <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Reason for Change** This dynamic rate is implemented because more users are depositing funds than borrowing, leading to a decreasing yield reserve <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. To narrow this gap, Anchor aims to encourage more borrowing by adding new collateral options <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## UST Availability and Usage on Avalanche (AVAX)

[[ust_availability_and_usage_on_avax | UST]] is now more easily accessible on the Avalanche chain for use with Anchor Protocol <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

*   **Getting UST** While initially requiring Wormhole UST from Curve's factory 55 <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, users can now acquire UST directly from Trader Joe <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Important Distinction** When obtaining UST from Trader Joe, ensure you select the one *without* the `.axl` extension (i.e., `UST` instead of `UST.axl`) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Anchor on Avalanche only recognizes the `UST` token without the `.axl` designation for deposits <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Withdrawals** Withdrawing UST from Anchor on Avalanche will return the funds directly to your Metamask wallet <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Borrowing UST using SAVAX as Collateral

Anchor Protocol now supports [[introduction_of_new_collateral_like_avex | staked AVAX (SAVAX)]] as collateral for [[borrowing_against_crypto_assets | borrowing UST]] directly on the Avalanche chain <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a> <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This integration allows for a more convenient way to earn yield compared to cross-chain transfers to the Terra chain <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a> <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Process for Converting AVAX to SAVAX and Using in Anchor

The [[process_for_converting_avax_to_savax_and_using_in_anchor | process for converting AVAX to SAVAX]] and using it as collateral is as follows:

1.  **Acquire SAVAX** SAVAX can be obtained through liquid staking platforms like Benqi <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Navigate to their liquid staking section to convert your AVAX into SAVAX <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
2.  **SAVAX as a Yield-Bearing Token** SAVAX is a yield-bearing token, currently earning approximately 7.2% APR <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  **Provide Collateral on Anchor** Once you have SAVAX, connect to Anchor on the Avalanche chain and use SAVAX to provide collateral <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a> <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
4.  **Borrowing against SAVAX** You can then borrow UST against your SAVAX collateral. Anchor typically recommends a borrowing ratio, such as 75% tbr (target borrow ratio) <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a> <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

!> **Note**: While wrapped SAVAX (wstAVAX) exists on the Terra chain, borrowing with SAVAX directly on the Avalanche chain is generally more convenient and avoids cross-chain complexities unless specific "money lego" opportunities arise on Terra <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a> <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

This direct integration of Anchor on the Avalanche chain simplifies the process of depositing and borrowing for users <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.