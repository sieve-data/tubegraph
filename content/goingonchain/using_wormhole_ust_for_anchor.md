---
title: Using Wormhole UST for Anchor
videoId: ZqPMJJdTeCc
---

From: [[goingonchain]] <br/> 

Anchor Protocol is now available on Avalanche (AVAX) and can connect via [[connecting_metamask_for_anchor | Metamask]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. However, not all UST (TerraUSD) tokens acquired on Avalanche are compatible with Anchor Protocol <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Identifying Compatible UST for Anchor on Avalanche

UST swapped on Trader Joe's, for example, may not be the correct version for Anchor <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. If you have UST in your Metamask wallet on the Avalanche chain, but the deposit button on Anchor is disabled, it's likely due to the UST originating from an incompatible bridge service <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

For instance, UST provided by xlr (a bridge service) is designed to bring UST to Terra through their Satellite DEX, and this version is not accepted by Anchor <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The UST that Anchor Protocol is willing to accept on Avalanche must be sourced through **Wormhole** <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Steps to Obtain Wormhole UST

To acquire the correct Wormhole UST for depositing into Anchor, follow these [[steps_to_deposit_ust_into_anchor | steps]]:

1.  **Acquire Base Stablecoins**: Go to Trader Joe's and obtain either USDC or USDT <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
2.  **Access Curve Pool**: Navigate to Curve Avax Factory 55 <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  **Swap to Wormhole UST**: Within this pool, you will find UST alongside USDC and USDT <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This UST is the Wormhole-bridged version <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Swap your USDC or USDT into UST here <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
    *   Click "sell" to initiate the swap <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
    *   Confirm the transaction in your Metamask wallet <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

Once the transaction is complete and you are connected to the Anchor Avalanche chain, your Wormhole UST will be detected <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Depositing Wormhole UST into Anchor

With the correct Wormhole UST, you can proceed with the deposit:

1.  **Initiate Deposit**: On the Anchor interface, click the "Deposit" button, which should now be enabled <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  **Confirm Transactions**: There will be two transactions required for the deposit <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
    *   "Deposit Stable" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
    *   "Contract Interaction" <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>

### Restoring a Failed Deposit Transaction

If the "Deposit Stable" transaction stops or nothing happens after it <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>:

1.  **Copy Transaction ID**: Click on the "Deposit Stable" transaction and copy its transaction ID <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  **Restore Transaction**: Go back to Anchor, click on your wallet, and select "Restore Transaction" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
3.  **Paste Hash**: Paste the copied transaction hash into the designated field and click "Restore" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

Once both transactions are successfully completed, your total deposit in Anchor will increase <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, and you will begin earning interest at the displayed API (e.g., 19% API) <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.