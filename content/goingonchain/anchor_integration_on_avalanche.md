---
title: Anchor integration on Avalanche
videoId: ZqPMJJdTeCc
---

From: [[goingonchain]] <br/> 

[[benqi_and_avalanche_integration | Anchor]] is now available on the [[avalanche_network_features | Avalanche]] network <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Users can connect to [[benqi_and_avalanche_integration | Anchor]] using [[metamask_connection_for_anchor_deposits | Metamask]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Understanding UST Types for Anchor

It's important to note that not all UST (TerraUSD) tokens available on the [[avalanche_network_features | Avalanche]] chain are accepted by [[benqi_and_avalanche_integration | Anchor]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

> [00:00:14] For example, if a user has UST obtained via XLR, a bridge service that allows changing UST on [[avalanche_network_features | Avalanche]] to Terra via their Satellite DEX, this specific UST will not be accepted by [[benqi_and_avalanche_integration | Anchor]] for deposits, even if it's visible in [[metamask_connection_for_anchor_deposits | Metamask]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The deposit button will appear disabled <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

[[benqi_and_avalanche_integration | Anchor]] specifically accepts UST that has been bridged through Wormhole <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Acquiring Wormhole UST for Anchor

To obtain the correct Wormhole UST for deposits on [[benqi_and_avalanche_integration | Anchor]], follow these steps:

1.  **Get USDC or USDT**: Go to Trader Joe and acquire either USDC or USDT <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
2.  **Convert to Wormhole UST**: Navigate to Curve Avax Factory 55 <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This pool contains UST, USDC, and USDT, and the UST within this pool is the accepted Wormhole UST <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Convert your USDC or USDT into UST here <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Depositing UST into Anchor

Once you have the Wormhole UST in your [[metamask_connection_for_anchor_deposits | Metamask]] wallet connected to the [[avalanche_network_features | Avalanche]] chain, you can proceed with the deposit:

1.  **Initiate Deposit**: On the [[benqi_and_avalanche_integration | Anchor]] platform, the system will detect your Wormhole UST <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Click the "deposit" button <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This action will prompt a [[metamask_connection_for_anchor_deposits | Metamask]] confirmation <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  **Confirm Transactions**: The deposit process involves two separate transactions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
    *   "Deposit stable" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
    *   "Contract interaction" <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>

Once both transactions are successful, your total deposit on [[benqi_and_avalanche_integration | Anchor]] will increase, and you will begin earning an approximate 19% API <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### Handling Failed Transactions

If the first transaction, "deposit stable," halts or does not complete properly:

1.  Click on the "deposit stable" transaction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  Copy your transaction ID <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
3.  Return to the [[benqi_and_avalanche_integration | Anchor]] platform.
4.  Click on your wallet within [[benqi_and_avalanche_integration | Anchor]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
5.  Select "restore transaction" <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
6.  Paste the copied transaction hash and click "restore" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This will help complete the deposit process <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.