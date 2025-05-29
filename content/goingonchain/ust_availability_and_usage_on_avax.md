---
title: UST availability and usage on AVAX
videoId: HWTUANwNhJ4
---

From: [[goingonchain]] <br/> 

Anchor protocol has expanded its services to the [[advantages_of_avalanche_platform | Avalanche]] blockchain, allowing users to deposit and borrow UST directly on the [[advantages_of_avalanche_platform | AVAX]] chain <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This integration simplifies the process for users looking to engage with Anchor's yield opportunities on [[advantages_of_avalanche_platform | Avalanche]] <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Obtaining UST on Avalanche

Previously, acquiring UST for use on Anchor's [[advantages_of_avalanche_platform | Avalanche]] deployment involved obtaining Wormhole UST from Curve, specifically under Factory 55 <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

However, UST can now be easily obtained from Trader Joe on the [[advantages_of_avalanche_platform | Avalanche]] chain <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>, <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

[!WARNING]
When acquiring UST from Trader Joe, it is crucial to differentiate between two types:
*   `ust.axl` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   `ust` (without the `.axl` suffix) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

Anchor on [[advantages_of_avalanche_platform | Avalanche]] will only recognize and accept the `ust` (without `.axl`) for deposits <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>, <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>, <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

When withdrawing UST from Anchor on [[advantages_of_avalanche_platform | Avalanche]], the funds are sent directly back to the user's Metamask wallet <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. From Metamask, users can return to Trader Joe to convert the UST into other crypto assets <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Borrowing UST on Avalanche with sAVAX

To address the imbalance between depositing and borrowing on Anchor (where deposits currently outnumber borrows), Anchor has been adding more collateral options <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>, <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This strategy aims to attract more users from other ecosystems to borrow UST <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

One such new collateral option is staked [[introduction_of_new_collateral_like_avex | AVAX]] (`sAVAX`) <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

### Obtaining sAVAX

`sAVAX` can be obtained by staking [[introduction_of_new_collateral_like_avex | AVAX]] on [[using_benqi_on_avalanche | Benqi's]] liquid staking platform <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>, <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>, <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. `sAVAX` is a yield-bearing token, currently earning approximately 7.2% APR <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### Using sAVAX as Collateral

Once `sAVAX` is acquired, it can be provided as collateral on Anchor's [[advantages_of_avalanche_platform | Avalanche]] chain <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The recommended loan-to-value (LTV) ratio for borrowing is 75% <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

While `wAVAX` (wrapped [[introduction_of_new_collateral_like_avex | AVAX]]) also exists on the Terra chain, using it for borrowing would require bridging `sAVAX` over the Wormhole to Terra to become `wAVAX` <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>, <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This process is generally considered cumbersome and unnecessary given Anchor's direct integration with the [[advantages_of_avalanche_platform | Avalanche]] chain <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>, <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Having Anchor directly connected to the [[advantages_of_avalanche_platform | AVAX]] chain for deposits and borrowing remains the most convenient way to earn yield <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.