---
title: Dynamic Saving Rate on Anchor
videoId: HWTUANwNhJ4
---

From: [[goingonchain]] <br/> 

The Anchor Protocol has introduced a dynamic saving rate, which means the [[Interest rates on Anchor Protocol | Anchor saving rate]] is no longer fixed at 19.5% <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Instead, it will be adjusted based on a specific formula <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Rate Adjustment Mechanism

The adjustment formula is tied to the yield reserve:
*   If the yield reserve goes up by 1.5%, the earn rate will also go up by 1.5% <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   If the yield reserve goes down by 1.5%, the earn rate will go down by 1.5% <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

These adjustments, with a fixed change of plus or minus 1.5%, will be performed on a monthly basis <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Rate Limits and Timeline

The lowest the [[Interest rates on Anchor Protocol | Anchor earn rate]] can go is 15% <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, and the maximum it can reach is 20% <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

Assuming the yield reserve continues its current downward trend in April <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>, the first adjustment is expected in May <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This means the interest rate will most likely start dropping in May <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Reasons for the Change

The primary reason for this change is that there are currently more people depositing funds than borrowing on the platform <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. To narrow this gap and ensure the [[Sustainability of Anchor platform | sustainability of the Anchor platform]], Anchor needs to increase borrowing <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### [[Strategies to improve Anchors borrowing | Strategies to Increase Borrowing]]

To encourage more borrowing, Anchor plans to add more collateral options <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. By adding more collateral, they can attract users from other ecosystems to borrow UST <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. For example, users can now borrow UST with staked AVAX (sAVAX) <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

However, the effectiveness of adding more collateral also depends on market sentiment <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. In a bear market, people are generally less willing to take risks or borrow, even with additional collateral options available <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Anchor Protocol on Avalanche (AVAX)

Anchor has connected directly to the Avalanche (AVAX) chain, making it more convenient to deposit and borrow <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Obtaining UST on Avalanche

Initially, to deposit UST on Anchor on AVAX, users had to obtain Wormhole UST from Curve's factory 55 <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Now, UST can be easily acquired from Trader Joe <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

When acquiring UST from Trader Joe for Anchor, it is crucial to pay attention to the two types of UST available:
*   `UST.axl` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   `UST` (without the `.axl` extension) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

Anchor on Avalanche will only accept `UST` without the `.axl` extension <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. If a user tries to deposit `UST.axl`, Anchor will not recognize it <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

When withdrawing UST from Anchor, it goes directly to the user's MetaMask wallet, from where it can be exchanged for other crypto assets on platforms like Trader Joe <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### [[AVAX Collateral and Borrowing on Anchor | Staked AVAX (sAVAX) as Collateral]]

Users can provide staked AVAX (sAVAX) as collateral on Anchor <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. To obtain sAVAX, users can visit Banky, specifically their liquid staking section <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Here, AVAX can be staked and converted into sAVAX <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. sAVAX is a yield-bearing token, currently earning approximately 7.2% APR <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Once sAVAX is acquired, it can be used on Anchor to borrow <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The recommended loan-to-value (LTV) ratio for borrowing is 75% <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

While a wrapped version of sAVAX (wstAVAX or wAVAX) exists on the Terra chain, requiring users to bridge their sAVAX over the Wormhole <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, most users are unlikely to do this due to its complexity and current lack of significant advantages on Terra <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Direct connection to the AVAX chain for depositing and borrowing remains the most convenient way to earn yield <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Summary of [[anchor_earn_interest_rate_changes | Anchor Earn Interest Rate Changes]]

*   The [[Interest rates on Anchor Protocol | Anchor interest rate]] will begin changing, most likely in May <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   The rate will fluctuate between a minimum of 15% and a maximum of 20% <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   For Anchor on AVAX, UST can be obtained from Trader Joe, ensuring to get the version without `.axl` <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   sAVAX can be obtained from Banky's liquid staking service and used as collateral for borrowing <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.