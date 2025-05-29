---
title: Metamask connection for Anchor deposits
videoId: ZqPMJJdTeCc
---

From: [[goingonchain]] <br/> 

Anchor Protocol can connect to [[metamask_security_features | Metamask]] and is now available on Avalanche (AVAX) <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This allows users to deposit UST via [[metamask_security_features | Metamask]] on the Avalanche chain <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Specific UST Requirements for Anchor Deposits

Not all UST (TerraUSD) tokens are accepted by Anchor Protocol for deposits <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. For example, UST acquired through services like XLM's bridge on Trader Joe might be detected in [[metamask_security_features | Metamask]], but the deposit button on Anchor will be disabled <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

Anchor Protocol specifically accepts UST that originates from Wormhole <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### How to Acquire Wormhole UST

To obtain the correct Wormhole UST for deposits on Anchor:
1.  Go to Trader Joe and acquire USDC or USDT <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
2.  Navigate to Curve Avex Factory 55 <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This pool contains UST, USDC, and USDT, where the UST is the compatible Wormhole UST <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>, <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
3.  Swap your acquired USDC or USDT for UST <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This transaction will trigger a [[metamask_security_features | Metamask]] confirmation <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

Once the transaction is complete and you are connected to the Anchor Avalanche chain, your UST balance should be detected and available for deposit <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Deposit Process

To deposit UST on Anchor via [[metamask_security_features | Metamask]]:
1.  Click the "Deposit" button on the Anchor interface <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
2.  Enter the amount of UST you wish to deposit and click "Proceed" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
3.  Be aware that there will be two separate [[metamask_security_features | Metamask]] transactions required for the deposit <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>, <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
    *   The first transaction is "Deposit Stable" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   The second transaction is "Contract Interaction" <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

After successful completion of both transactions, your total deposit on Anchor will increase, and you will begin earning interest at the displayed API <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Troubleshooting Failed Deposits

If the "Deposit Stable" transaction stops and nothing happens, you can manually restore the transaction <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>, <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>:
1.  Click on "Deposit Stable" <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  Copy your transactional ID <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
3.  Go back to Anchor, click on your wallet, and select "Restore Transaction" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  Paste the transaction hash and click "Restore" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>, <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

> [!WARNING] Important Note
> Remember that two transactions are required for depositing into Anchor on Avalanche: "Deposit Stable" and "Contract Interaction" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
>
> For more general [[troubleshooting_anchor_deposit_transactions | troubleshooting of Anchor deposit transactions]], consult related guides.