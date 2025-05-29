---
title: Connecting Metamask for Anchor
videoId: ZqPMJJdTeCc
---

From: [[goingonchain]] <br/> 

Anchor Protocol is now available on Avalanche (AVAX) and can connect with Metamask <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. However, not all UST (TerraUSD) on Avalanche is accepted by [[anchor_protocol_business_model | Anchor]] Protocol <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Identifying Incompatible UST

If you have UST in your Metamask wallet on the Avalanche chain, but the deposit button on [[anchor_protocol_business_model | Anchor]] is disabled, it's likely due to the UST being provided by XLR <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. XLR is a bridge service that allows changing UST on Avalanche to Terra, but this version of UST is not compatible with [[anchor_protocol_business_model | Anchor]] Protocol on Avalanche <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Obtaining Compatible UST (Wormhole UST)

To deposit UST into [[anchor_protocol_business_model | Anchor]] Protocol, you need [[using_wormhole_ust_for_anchor | Wormhole]] UST <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Follow these [[steps_to_deposit_ust_into_anchor | steps to deposit UST into Anchor]]:

1.  **Acquire USDC or USDT:** Go to Trader Joe and get some USDC or USDT <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  **Swap for Wormhole UST:** Navigate to Curve AVAX Factory 55. This pool contains UST, USDC, and USDT, with the UST being the [[using_wormhole_ust_for_anchor | Wormhole]] variant <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
3.  **Perform the Swap:** Change your USDC or USDT to UST within this pool <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
4.  **Confirm Transaction:** Click "Sell" to trigger a Metamask confirmation <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Depositing UST into Anchor Protocol

Once the transaction is complete and you are connected to the [[anchor_protocol_business_model | Anchor]] Avalanche chain, your UST will be detected <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

1.  **Initiate Deposit:** Click "Deposit" and select the amount of UST you wish to deposit <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
2.  **Two Transactions:** Be aware that the deposit process involves two separate transactions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
    *   **Deposit Stable:** The first transaction <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   **Contract Interaction:** The second transaction <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### Restoring a Failed Transaction

If the "Deposit Stable" transaction stops or nothing happens, you can restore it <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>:

1.  Click on the "Deposit Stable" transaction.
2.  Copy your transaction ID <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
3.  Go back to [[anchor_protocol_business_model | Anchor]] Protocol, click on your wallet, and select "Restore Transaction" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
4.  Paste the transaction hash into the prompted field and click "Restore" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

After successful completion of both transactions, your total deposit will increase, and you will begin earning approximately 19% API <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.