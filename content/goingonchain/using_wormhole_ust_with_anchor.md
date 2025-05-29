---
title: Using Wormhole UST with Anchor
videoId: ZqPMJJdTeCc
---

From: [[goingonchain]] <br/> 

Anchor is now available on Avalanche (AVAX) and can connect to [[metamask_connection_for_anchor_deposits | Metamask]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. However, it's important to note that the UST available on Trader Joe, often swapped via the XLM bridge service, is not directly accepted by [[lending_and_borrowing_process_on_anchor_protocol | Anchor Protocol]] for deposits <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

For example, UST sourced from XLM, even if in Metamask, will result in a disabled deposit button on the [[lending_and_borrowing_process_on_anchor_protocol | Anchor Protocol]] Avalanche chain interface <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. The XLM bridge allows changing UST on Avalanche to bring it to their DEX, Satellite, and then to a modified Terra <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Obtaining Accepted UST

The UST that [[lending_and_borrowing_process_on_anchor_protocol | Anchor Protocol]] accepts is from Wormhole <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

To obtain Wormhole UST:
1.  Go to Trader Joe and acquire either USDC or USDT <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  Navigate to Curve Avax Factory 55 <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
3.  In this pool, you will find UST, USDC, and USDT <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. The UST here is Wormhole UST <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
4.  Swap your USDT (or USDC) to Wormhole UST <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
5.  Click "sell" which will trigger a [[metamask_connection_for_anchor_deposits | Metamask]] confirmation <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Depositing Wormhole UST to Anchor

Once the transaction is complete and you are connected to the [[lending_and_borrowing_process_on_anchor_protocol | Anchor Protocol]] Avalanche chain, your Wormhole UST will be detected <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### Deposit Process
1.  Click the deposit button <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
2.  Enter the amount of UST to deposit <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
3.  Click "proceed" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
4.  There will be two transactions required:
    *   "Deposits stable" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
    *   "Contract interaction" <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>

### Troubleshooting Deposit Transactions
[!WARNING] If the "deposit stable" transaction stops and nothing happens, you can restore it <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
1.  Click on the "deposit stable" transaction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  Copy your transaction ID <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
3.  Go back to [[lending_and_borrowing_process_on_anchor_protocol | Anchor Protocol]], click on your wallet, and find the "restore transaction" option <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  Paste the transaction hash and click "restore" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

After successfully completing both transactions, your total deposit on [[lending_and_borrowing_process_on_anchor_protocol | Anchor Protocol]] will increase, and you will begin earning an [[interest_rates_on_anchor_protocol | Annual Percentage Yield (APY)]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.