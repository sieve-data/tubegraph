---
title: Canceling listings and offers on Opensea
videoId: tloTgDASGQs
---

From: [[goingonchain]] <br/> 

To prepare for significant network changes like the Ethereum Merge, some users opt to cancel all their active listings and offers on Opensea as a precautionary measure <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This can be done efficiently, saving on gas fees compared to canceling individual listings <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## How to Cancel All Opensea Listings and Offers

Users can cancel all their offers and listings on Opensea by following these steps:
1.  Navigate to your profile on Opensea <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
2.  Select "More" <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
3.  Go to "Offers Made" <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
4.  There will be an option to "Cancel All Listing and Offer" <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

This method is more cost-effective in terms of gas fees than canceling each listing or offer individually <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Why Cancel Listings and Offers?

The primary reason for canceling all listings and offers is concern over potential replay attacks, especially during major network transitions like the Ethereum Merge <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Understanding Replay Attacks

A replay attack could occur if, after the Ethereum Merge, miners continue to push a proof-of-work (EthPoW) chain alongside the new proof-of-stake (POS) chain <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

For example, if an NFT listing is accepted on the EthPoW chain (where 1 ETH might hold a lower value) <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, there's a possibility this transaction could be replayed and broadcast on the POS chain <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This could result in your valuable NFT on the POS chain being sold inadvertently <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

This potential risk has also been highlighted by other blockchain security entities <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Protections and Remaining Risks

There are mechanisms in place aimed at preventing replay attacks:
*   Opensea has stated they will not support the EthPoW chain <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, though it's uncertain if transactions could still occur at the smart contract level <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   EIP-155, implemented in 2016 during the Ethereum fork to Ethereum Classic (ETC), introduced "chain IDs" to distinguish between different networks <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Ethereum has a chain ID of 1 <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, and ETC has a chain ID of 61 <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

However, the EthPoW team, despite releasing a proposed chain ID (10001), has not yet implemented it in their source code <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This means they are currently sharing the same chain ID as the main Ethereum chain <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, which increases the risk of replay attacks <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Given these concerns, some users prefer to cancel all their listings and offers to avoid potential issues and relist them once the network stabilizes <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. While the simplest approach might be to do nothing and hold ETH in a cold wallet <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, those actively seeking potential EthPoW airdrops might consider more involved strategies <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.