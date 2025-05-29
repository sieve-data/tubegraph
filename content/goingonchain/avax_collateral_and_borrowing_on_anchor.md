---
title: AVAX Collateral and Borrowing on Anchor
videoId: HWTUANwNhJ4
---

From: [[goingonchain]] <br/> 

Anchor Protocol has been undergoing changes, including the implementation of a dynamic saving rate, which adjusts monthly based on a formula and the yield reserve <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The saving rate will no longer be fixed at 19.5% <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, with a maximum of 20% and a minimum of 15% <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Due to a current trend of more people depositing than [[lending_and_borrowing_process_on_anchor_protocol | borrowing]], the yield reserve is on a downward trend <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

To narrow this gap and encourage more [[strategies_to_improve_anchors_borrowing | borrowing]], Anchor needs to add more collateral options <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. By adding more [[role_of_collateral_in_anchor_protocol | collateral]], Anchor aims to attract users from other ecosystems to [[lending_and_borrowing_process_on_anchor_protocol | borrow]] UST <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Using AVAX as Collateral

One of the new collateral options available is staked AVAX (sAVAX) <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Obtaining sAVAX
To acquire sAVAX, users can visit Benqi's liquid staking platform, where AVAX can be staked and converted into sAVAX <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. sAVAX is a yield-bearing token that earns approximately 7.2% APR <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### Providing sAVAX as Collateral
Once sAVAX is obtained, it can be provided as [[role_of_collateral_in_anchor_protocol | collateral]] on Anchor Protocol directly on the Avalanche (AVAX) chain <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Borrowing with sAVAX
With sAVAX provided as collateral, users can [[using_savax_to_borrow | borrow]] UST <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The recommended target [[anchor_protocol_loans_and_liquidation | borrow]] ratio (tbr) for borrowing is 75% <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### wAVAX on Terra Chain
It is also possible to bridge staked AVAX (sAVAX) over the Wormhole to the Terra chain, where it becomes wrapped sAVAX (wAVAX) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. However, this process is generally more cumbersome and unnecessary for most users given Anchor's direct connection to the AVAX chain <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Acquiring UST on AVAX for Anchor
To [[ust_on_avax | deposit UST]] into Anchor on the AVAX chain, users can obtain UST from Trader Joe <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. It is crucial to select the correct version of UST:

*   **UST without `.axl`**: This is the version accepted by Anchor on Avalanche <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **UST.axl**: This version is *not* recognized by Anchor <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

Deposited UST can be easily withdrawn back to a MetaMask wallet and then swapped for other crypto assets on platforms like Trader Joe <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

The direct connection of Anchor to the AVAX chain, allowing for deposits and [[lending_and_borrowing_process_on_anchor_protocol | borrowing]] with sAVAX, offers a convenient way to earn yield <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.