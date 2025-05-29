---
title: Swapping UST on Trader Joe
videoId: ZqPMJJdTeCc
---

From: [[goingonchain]] <br/> 

When using Anchor on the Avalanche chain, it's crucial to understand that not all UST (TerraUSD) tokens are interchangeable or accepted by Anchor. While Anchor is now available on Avalanche and can connect to MetaMask <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>, the UST available on Trader Joe may not be the correct type for deposit <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Understanding UST Compatibility on Avalanche

The UST available for swap on Trader Joe, often provided by Axelar, is not the UST that Anchor is willing to accept for deposits <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. For example, even if you have UST from Axelar in your MetaMask and connected to the Avalanche chain, the deposit button on Anchor might be disabled <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Axelar provides a [[how_to_bridge_ust_to_avalanche_using_keplr_wallet | bridge service]] that allows you to change UST on Avalanche and bring it to their Satellite DEX, then over to a modified Terra chain <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### The Correct UST for Anchor

The UST that Anchor is willing to accept on Avalanche is [[using_wormhole_ust_for_anchor | Wormhole UST]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Steps to Acquire and Deposit Wormhole UST

To successfully [[using_wormhole_ust_for_anchor | deposit UST into Anchor]] on the Avalanche chain, follow these [[steps_and_requirements_for_transferring_ust | steps]]:

1.  **Obtain USDC or USDT on Trader Joe:** Start by acquiring USDC or USDT from Trader Joe <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
2.  **Navigate to Curve Avax Factory 55:** Go to Curve Avax Factory 55 <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  **Swap for Wormhole UST:** Within the Curve pool (which includes UST, USDC, and USDT), exchange your USDC or USDT for the [[using_wormhole_ust_for_anchor | Wormhole UST]] <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    *   Click "sell" to initiate the swap <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
    *   Confirm the transaction in MetaMask <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
4.  **Deposit into Anchor:**
    *   Once the transaction is complete and you are connected to the Anchor Avalanche chain, your [[using_wormhole_ust_for_anchor | Wormhole UST]] should be detected <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
    *   Click the "deposit" button <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
    *   Confirm the deposit amount and hit "proceed" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Transaction Steps for Deposit

Depositing into Anchor on Avalanche requires two transactions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
1.  **Deposit Stable** <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
2.  **Contract Interaction** <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>

### Restoring a Stuck Transaction

If the "deposit stable" transaction stops and nothing happens <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>:
1.  Click on the "deposit stable" transaction.
2.  Copy your transaction ID <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
3.  Go back to Anchor, click on your wallet, and find the "restore transaction" option <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
4.  Paste the transaction hash and hit "restore" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

Upon successful deposit, your total deposit amount on Anchor will increase, and you will begin [[farming_opportunities_on_avalanche_with_ust | earning a 19% API]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.