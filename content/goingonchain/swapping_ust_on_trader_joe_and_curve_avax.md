---
title: Swapping UST on Trader Joe and Curve AVAX
videoId: ZqPMJJdTeCc
---

From: [[goingonchain]] <br/> 

Anchor is now available on Avalanche (AVAX) and can connect to MetaMask <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. However, the type of UST (TerraUSD) available on Trader Joe may not be the one accepted by Anchor <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Understanding Different UST Types

The UST found on Trader Joe, often provided by the XLR bridge service, is not directly accepted by Anchor <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This XLR-provided UST can be brought from Avalanche to their Satellite DEX, and then to a modified version of Terra <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. When attempting to deposit this type of UST into Anchor, the deposit button will be disabled <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

The UST that Anchor is willing to accept is derived from Wormhole <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Acquiring Anchor-Compatible UST

To obtain the correct Wormhole UST for Anchor, follow these steps:

1.  **Obtain USDC or USDT on Trader Joe**: Start by acquiring USDC or USDT from Trader Joe <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
2.  **Navigate to Curve AVAX Factory 55**: Go to the Curve AVAX Factory 55 pool <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This pool contains a mix of UST, USDC, and USDT <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. The UST in this specific pool is the Wormhole UST <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
3.  **Swap to Wormhole UST**: Exchange your USDC or USDT for UST within this pool <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This will trigger a MetaMask confirmation <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

This process enables [[bridging_ust_to_avalanche | Bridging UST to Avalanche]] in a way that is compatible with Anchor.

## Depositing to Anchor

Once the transaction is complete and you have Wormhole UST, connect to the Anchor Avalanche chain <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Anchor will detect your UST, and you can proceed with the deposit <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

Note that depositing into Anchor on Avalanche requires two separate transactions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:

1.  **Deposit Stable** <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
2.  **Contract Interaction** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

Upon successful deposit, your total deposit amount on Anchor will increase, and you will begin earning an Annual Percentage Yield (APY), such as 19% <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Troubleshooting Deposits

If the "Deposit Stable" transaction stops or nothing happens after initiation <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>:

1.  Click on the "Deposit Stable" transaction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  Copy your transaction ID <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
3.  Go back to Anchor, click on your wallet, and select "Restore Transaction" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
4.  Paste the transaction hash into the provided field and click "Restore" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.