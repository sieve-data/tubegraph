---
title: Preparing for the Ethereum Merge
videoId: tloTgDASGQs
---

From: [[goingonchain]] <br/> 

The [[understanding_the_ethereum_merge | Ethereum Merge]] involves changing the blockchain's consensus layer from [[transition_from_proof_of_work_to_proof_of_stake | Proof of Work (PoW)]] to Proof of Stake (PoS) <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The mainnet itself will remain the same <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

The Ethereum Foundation has stated that users do not need to take any specific action to prepare for the [[understanding_the_ethereum_merge | Merge]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The easiest approach is simply to do nothing and hold your ETH in a cold wallet <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## Personal Preparations for the Merge

Despite the official guidance, some users may choose to take precautions. One suggested action is to cancel all offers and listings on OpenSea <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

### How to Cancel OpenSea Listings and Offers
To cancel all listings and offers on OpenSea, navigate to your profile, select "More," and then choose "Offers" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This method is noted as being cheaper in terms of [[impact_of_the_merge_on_gas_fees | gas fees]] compared to canceling items one by one <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Once the [[understanding_the_ethereum_merge | Merge]] is complete and the situation is stable, items can be relisted <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Concern: Replay Attacks

The primary reason for taking these precautions is concern about potential "replay attacks" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

#### What is a Replay Attack?
A replay attack could occur if a separate [[differences_between_ethereum_pos_and_pow_chains | PoW chain]] (referred to as ETHW) continues to be pushed forward by miners after the [[understanding_the_ethereum_merge | Merge]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. If a transaction, such as an NFT listing acceptance, occurs on this ETHW chain (where the value of ETH may be lower) <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, there is a possibility that this same transaction could be replayed and broadcast on the legitimate [[differences_between_ethereum_pos_and_pow_chains | PoS chain]] <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This could result in valuable NFTs being transferred without intent on the main PoS chain <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This potential risk has also been highlighted by LookRar <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

#### Protections Against Replay Attacks

1.  **OpenSea Policy**: OpenSea has stated they will not support the ETHW chain <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. However, there is a remaining concern about whether transactions could still take place at the smart contract level <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
2.  **[[eip1559_and_its_impact_on_ethereum_issuance | EIP-155]]**: Implemented in 2016 during the Ethereum fork to Ethereum Classic (ETC), [[eip1559_and_its_impact_on_ethereum_issuance | EIP-155]] provides protection against replay attacks by using chain IDs <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
    *   Chain IDs differentiate networks; for example, Ethereum (ETH) has a chain ID of 1 <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>, while Ethereum Classic (ETC) has a chain ID of 61 <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   The ETHW chain has released its own chain ID (10001) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, but it has not yet implemented this change in its source code, meaning it currently shares the same chain ID as Ethereum <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This lack of implementation heightens the risk of replay attacks <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Pursuing an ETHW Airdrop

For users interested in potentially receiving an ETHW airdrop, the CEO of CoinGecko has shared thoughts and seven steps that can be taken to fully leverage the [[understanding_the_ethereum_merge | Merge]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>, <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>, <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. However, it is crucial to remember the potential for replay attacks, especially given that ETHW has not yet changed its chain ID <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.