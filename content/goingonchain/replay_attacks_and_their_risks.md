---
title: Replay attacks and their risks
videoId: tloTgDASGQs
---

From: [[goingonchain]] <br/> 

A replay attack is a cybersecurity concern where a valid data transmission is maliciously or fraudulently repeated or delayed. This issue is particularly relevant in blockchain environments during significant network changes, such as the Ethereum Merge <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## How Replay Attacks Work

In the context of the Ethereum Merge, a replay attack scenario could unfold if miners continue to support and produce a Proof-of-Work (PoW) chain (referred to as ETHW) alongside the new Proof-of-Stake (PoS) chain <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

Consider an example where an NFT listing is accepted on the lower-value ETHW chain. There is a possibility that this transaction could be "replayed" or broadcast on the higher-value PoS chain, potentially leading to the loss of a valuable NFT <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This specific potential risk has also been highlighted by "Look straight" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Protective Measures

Several mechanisms aim to provide [[chain_id_and_its_role_in_protecting_against_replay_attacks | protection against replay attacks]]:

*   **OpenSea's Stance:** OpenSea has stated they will not support ETHW <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. However, there remains uncertainty about whether transactions could still occur at the smart contract level regardless of OpenSea's policy <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **EIP-155:** Implemented in 2016 during the Ethereum fork to Ethereum Classic (ETC), EIP-155 provides [[chain_id_and_its_role_in_protecting_against_replay_attacks | protection against replay attacks]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This was necessary because both ETC and ETH initially shared a network ID of one <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Chain ID:** A [[chain_id_and_its_role_in_protecting_against_replay_attacks | Chain ID]] serves as an additional identifier to distinguish between networks <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. For instance, Ethereum (ETH) has a [[chain_id_and_its_role_in_protecting_against_replay_attacks | Chain ID]] of 1, while Ethereum Classic (ETC) has a [[chain_id_and_its_role_in_protecting_against_replay_attacks | Chain ID]] of 61 <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## ETHW and Replay Attack Concerns

Despite having released a proposed [[chain_id_and_its_role_in_protecting_against_replay_attacks | Chain ID]] of 1001, the ETHW (Ethereum Proof-of-Work) chain has not yet implemented it <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Their source code shows the new [[chain_id_and_its_role_in_protecting_against_replay_attacks | Chain ID]] as commented out <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, meaning they currently share the same [[chain_id_and_its_role_in_protecting_against_replay_attacks | Chain ID]] as the PoS Ethereum chain <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This shared [[chain_id_and_its_role_in_protecting_against_replay_attacks | Chain ID]] creates an opportunity for replay attacks <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Mitigation Strategies

To mitigate the risk of replay attacks, especially concerning NFTs, one approach is to cancel all active listings and offers on platforms like OpenSea <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This can be done efficiently by navigating to "Profile," then "More," and selecting "Offers Made" to cancel all listings and offers simultaneously, which is also cheaper in terms of gas fees <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The speaker chose to "unleash everything" (cancel all listings/offers) and relist them once the situation stabilizes <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

Alternatively, the easiest approach for many users is to simply do nothing and hold their ETH in their core wallet <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. For those interested in an ETHW airdrop, a post by the CEO of CoinGecko outlines seven steps to potentially take advantage of the Merge, though it also warns about the opportunity for replay attacks due to ETHW's unchanged [[chain_id_and_its_role_in_protecting_against_replay_attacks | Chain ID]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This serves as a critical consideration for [[protection_against_scams | protection against scams]].