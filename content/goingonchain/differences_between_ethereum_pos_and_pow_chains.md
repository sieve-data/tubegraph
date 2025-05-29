---
title: Differences between Ethereum POS and POW chains
videoId: tloTgDASGQs
---

From: [[goingonchain]] <br/> 

The upcoming Ethereum Merge, scheduled for September 2022, marks a significant shift for the Ethereum blockchain <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Purpose of the Merge

The merge primarily involves [[transition_from_proof_of_work_to_proof_of_stake | changing the consensus layer]] from [[proof_of_work_vs_proof_of_stake | Proof of Work (POW)]] to [[proof_of_work_vs_proof_of_stake | Proof of Stake (POS)]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Despite this fundamental change, the Ethereum mainnet remains the same <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Replay Attack Risk

A primary concern post-merge is the potential for "replay attacks" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. If miners continue to operate and produce an Ethereum POW chain after the merge, a transaction executed on this POW chain could potentially be "replayed" and broadcast on the new POS chain <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, if an NFT listing is accepted on the low-value POW chain, that transaction could be re-broadcast on the POS chain, leading to the loss of a valuable NFT <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This risk has also been highlighted by Lookonchain <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Protections and Current Status

1.  **OpenSea's Stance**: OpenSea has stated they will not be supporting the Ethereum POW chain (ETHW) <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. However, it is uncertain if transactions could still occur at the smart contract level <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
2.  **EIP155 Implementation**: During the 2016 Ethereum fork to Ethereum Classic (ETC), EIP155 was implemented to protect against replay attacks <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Initially, both ETC and ETH shared a network ID of one <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Chain IDs were introduced as an additional method to distinguish networks <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The main Ethereum chain has a chain ID of 1, while ETC has a chain ID of 61 <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
3.  **ETHW Chain ID**: Although the Ethereum POW chain (ETHW) has announced a chain ID of 1001, they have not yet implemented it in their source code <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This means that currently, the ETHW chain still shares the same chain ID as the main Ethereum chain, which could create an opportunity for replay attacks <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Preparing for the Merge

While the Ethereum Foundation's blog states that users generally do not need to do anything to [[preparing_for_the_ethereum_merge | prepare for the merge]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, some users may take precautions <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

One suggested precaution is to cancel all offers and listings on platforms like OpenSea <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This can be done in OpenSea by going to "Profile," then "More," and finally "Offers Made," where there is an option to cancel all listings and offers, which is also a more gas-efficient option than canceling one by one <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The reason for this is to mitigate the risk of replay attacks <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Once the post-merge environment stabilizes, listings can be re-established <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

The easiest approach is to simply hold Ethereum in a cold wallet and do nothing <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. However, for those interested in potential ETHW airdrops, the CEO of CoinGecko has shared thoughts and steps to potentially take advantage of the merge <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. It is important to remember the potential for replay attacks, especially given that ETHW has not yet changed its chain ID <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.