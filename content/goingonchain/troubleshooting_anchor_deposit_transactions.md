---
title: Troubleshooting Anchor deposit transactions
videoId: ZqPMJJdTeCc
---

From: [[goingonchain]] <br/> 

When depositing UST on Anchor Protocol through the Avalanche chain, users may encounter specific issues related to the type of UST accepted and the transaction process itself <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Unacceptable UST and its Origin

Not all UST (TerraUSD) available on Avalanche is accepted by Anchor Protocol <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. If you have UST from sources like Trader Joe or bridged via XLR, the deposit button on Anchor will be disabled, even if it's in your [[metamask_connection_for_anchor_deposits | MetaMask wallet]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

This is because UST provided by XLR is a bridge service designed to bring UST to their DEX, Satellite, and then to a modified Terra <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Anchor Protocol specifically requires UST that originates from Wormhole <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Obtaining Accepted Wormhole UST

To acquire the Wormhole UST that Anchor accepts, follow these steps:
1.  **Acquire Base Stablecoin:** Get USDC or USDT from Trader Joe <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
2.  **Navigate to Curve Pool:** Go to Curve Avax Factory 55 <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
3.  **Swap for Wormhole UST:** In this pool, you will find UST, USDC, and USDT <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. The UST here is the Wormhole UST <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Swap your USDC or USDT for Wormhole UST <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
4.  **Confirm Transaction:** Click "sell" and confirm the transaction via [[metamask_connection_for_anchor_deposits | MetaMask]] <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

Once this transaction is complete and you are connected to the Anchor Avalanche chain, your Wormhole UST will be detected, and you can proceed with the deposit <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Resolving Incomplete Deposit Transactions

Depositing into Anchor on Avalanche requires two distinct transactions to be completed:
1.  **Deposit Stable:** The initial transaction to deposit the stablecoin <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  **Contract Interaction:** The second transaction, which completes the deposit process <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

If the first transaction ("deposit stable") goes through but nothing further happens, you can manually restore the transaction:
1.  **Copy Transaction ID:** Click on the "deposit stable" transaction and copy its transaction ID (or hash) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  **Restore Transaction:** Go back to Anchor, click on your wallet, and select "restore transaction" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
3.  **Paste and Restore:** Paste the transaction hash into the provided field and hit "restore" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

After successful completion of both transactions, your total deposit on Anchor will increase, and you will begin earning interest <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.