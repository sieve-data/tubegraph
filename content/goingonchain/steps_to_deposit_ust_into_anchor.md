---
title: Steps to deposit UST into Anchor
videoId: ZqPMJJdTeCc
---

From: [[goingonchain]] <br/> 

Anchor Protocol is now available on Avalanche (AVAX) and supports connections via [[connecting_metamask_for_anchor | Metamask]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. However, it's crucial to use the correct version of UST (TerraUSD) for deposits, as not all UST available on Avalanche is accepted by Anchor <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Identifying Accepted UST

The UST swapped on Trader Joe, particularly if it's provided by the XLR bridge service, is not accepted by Anchor <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This type of UST is designed for XLR's Satellite DEX and for bridging to Terra <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

Anchor will only accept [[using_wormhole_ust_for_anchor | Wormhole UST]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. If you have unaccepted UST in your [[connecting_metamask_for_anchor | Metamask]] wallet on the Avalanche chain, the deposit button on Anchor will be disabled <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Obtaining Wormhole UST for Anchor

To get the [[using_wormhole_ust_for_anchor | Wormhole UST]] that Anchor accepts, follow these steps:
1.  **Acquire Stablecoins:** Go to Trader Joe and get either USDC or USDT <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The example provided uses USDT <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
2.  **Access Curve Pool:** Navigate to Curve AVAX Factory 55 <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
3.  **Swap to Wormhole UST:** Within this pool, you will find UST, USDC, and USDT <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. The UST in this specific pool is the [[using_wormhole_ust_for_anchor | Wormhole UST]] <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Swap your USDC or USDT to UST <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This action will trigger a [[connecting_metamask_for_anchor | Metamask]] confirmation <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Depositing UST into Anchor

Once the transaction for acquiring [[using_wormhole_ust_for_anchor | Wormhole UST]] is complete:
1.  **Connect to Anchor:** Ensure your [[connecting_metamask_for_anchor | Metamask]] wallet is connected to the Avalanche chain on the Anchor protocol <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
2.  **Detect UST:** Anchor will detect your acquired [[using_wormhole_ust_for_anchor | Wormhole UST]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
3.  **Initiate Deposit:** Click the "Deposit" button, which should now be enabled, and confirm the amount you wish to deposit <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Transaction Process and Troubleshooting

The deposit process involves two distinct transactions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
1.  **Deposit Stable** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
2.  **Contract Interaction** <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>

### Troubleshooting Failed Transactions
If the "Deposit Stable" transaction stops or fails without completing the deposit <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>:
1.  **Copy Transaction ID:** Click on the "Deposit Stable" transaction to copy its transaction ID <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  **Restore Transaction:** Go back to Anchor, click on your wallet icon, select "Restore Transaction" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
3.  **Input Hash:** Paste the copied transaction hash into the required field and click "Restore" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

Once both transactions are successfully completed, your total deposit in Anchor will increase, and you will begin earning an approximate 19% API on your deposited UST <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.