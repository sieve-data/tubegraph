---
title: Anchor on Avalanche overview
videoId: ZqPMJJdTeCc
---

From: [[goingonchain]] <br/> 

Anchor Protocol is now available on [[advantages_of_avalanche_platform | Avalanche]], and it can connect to MetaMask <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Differentiating UST on Avalanche

It's important to note that not all UST (TerraUSD) tokens available on [[advantages_of_avalanche_platform | Avalanche]] are accepted by Anchor Protocol <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

### Unacceptable UST (XLR Bridge)

UST obtained through XLR's bridge service (e.g., swapped on Trader Joe) is not accepted by Anchor <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. If you have this type of UST in your MetaMask wallet while connected to the Avalanche chain on Anchor, the deposit button will be disabled <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. XLR allows converting UST on Avalanche to a modified version on Terra via their Satellite DEX <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Acceptable UST (Wormhole Bridge)

The UST that Anchor Protocol accepts on [[advantages_of_avalanche_platform | Avalanche]] originates from the Wormhole bridge <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Acquiring Wormhole UST for Anchor

To get Wormhole UST, follow these steps, which are part of [[farming_opportunities_on_avalanche_with_ust | farming opportunities on Avalanche with UST]]:

1.  **Obtain USDC or USDT**: Go to Trader Joe and acquire either USDC or USDT <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
2.  **Use Curve Avax Pool**: Navigate to Curve Avax Factory 55 <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This pool contains UST, USDC, and USDT, with the UST being the Wormhole version <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
3.  **Swap to UST**: Swap your USDC or USDT to UST within this pool <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This will require a MetaMask confirmation <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Depositing UST into Anchor

This section provides a [[tutorial_on_avalanche_usage | tutorial on Avalanche usage]] for depositing UST into Anchor:

1.  **Connect and Detect UST**: Once the transaction is complete and you are connected to the Anchor [[advantages_of_avalanche_platform | Avalanche]] chain, Anchor will detect your Wormhole UST <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
2.  **Initiate Deposit**: Click the "Deposit" button and select the amount of UST you wish to deposit, then hit "Proceed" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Two Transactions**: Note that two transactions are required for the deposit to complete <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>:
    *   "Deposit stable" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
    *   "Contract interaction" <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>

### Troubleshooting Deposit

If the "deposit stable" transaction stops or nothing happens <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>:

1.  Click the "deposit stable" transaction.
2.  Copy its transactional ID <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
3.  Go back to Anchor, click on your wallet, and find the "Restore transaction" option <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
4.  Paste the transaction hash and hit "Restore" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

After successful deposit, your total deposit amount will increase, and you will begin earning an Annual Percentage Yield (APY), for example, 19% <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.