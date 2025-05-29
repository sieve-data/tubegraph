---
title: The Merge on Ethereum
videoId: tloTgDASGQs
---

From: [[goingonchain]] <br/> 

The highly anticipated [[ethereum_merge_and_its_implications | Ethereum merge]] is approaching, signifying a fundamental shift in the network's consensus mechanism <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Understanding The Merge

The merge primarily involves [[ethereums_transition_from_pow_to_pos | changing the consensus layer from Proof-of-Work (PoW) to Proof-of-Stake (PoS)]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. According to the Ethereum Foundation Vlog, users are generally not required to take any action <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Preparing for The Merge

Despite the general advice, some users are taking precautions due to potential risks. One common action is to cancel all outstanding offers and listings on platforms like [[smart_contract_migration_issues_on_opensea | OpenSea]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### How to Cancel Listings/Offers on OpenSea

Users can cancel all their listings and offers at once, which is more cost-effective in terms of [[impact_of_ethereum_merge_on_gas_fees | gas fees]] than canceling them individually <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This can be done by navigating to:
*   Profile <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>
*   More <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   Offers <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>
*   Then select "Cancel all listings and offer" <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>

### Concern: Replay Attacks

The primary reason for canceling listings is the concern over replay attacks <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

#### What is a Replay Attack?
A replay attack occurs if, after the merge, miners continue to operate a Proof-of-Work (PoW) Ethereum chain (e.g., ETH PoW) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. If a transaction, such as an NFT listing being accepted, occurs on this lower-value PoW chain, there's a possibility that the same transaction could be "replayed" and broadcast on the main, valuable PoS chain <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This could result in the loss of valuable NFTs on the main PoS chain <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Protections Against Replay Attacks

There are measures that offer some protection against replay attacks:

1.  **OpenSea's Stance**: [[smart_contract_migration_issues_on_opensea | OpenSea]] has stated they will not support the ETH PoW chain <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. However, it's uncertain if transactions could still occur at the smart contract level <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
2.  **EIP-155 (Chain ID)**: Implemented in 2016 during the Ethereum fork to Ethereum Classic (ETC), EIP-155 introduced a "chain ID" <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This additional identifier helps distinguish networks, preventing transactions from one chain (like ETC with chain ID 61) from being replayed on another (like Ethereum with chain ID 1) <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### The ETH PoW Chain ID Issue

While the ETH PoW developers have released a proposed chain ID (10001), they have not yet implemented it in their source code, meaning they currently share the same chain ID as the main Ethereum PoS chain <a class="yt-timestamp" data-t="00:01:53">[00:02:03]</a>. This shared chain ID creates a potential vulnerability for replay attacks <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

Given these complexities, some users choose to cancel all their listings and offers, planning to relist them once the situation stabilizes <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## General Advice for The Merge

The simplest approach for most users is to do nothing and hold their ETH in a cold wallet <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

For those interested in chasing potential ETH PoW airdrops, resources are available (e.g., a post by the CEO of CoinGecko outlining seven steps to take advantage of the merge) <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. However, it is crucial to remember the potential for replay attacks, especially if ETH PoW does not change its chain ID <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.