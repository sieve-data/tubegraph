---
title: Replay attack in blockchain
videoId: tloTgDASGQs
---

From: [[goingonchain]] <br/> 

The upcoming Ethereum Merge involves a shift in the consensus layer from Proof-of-Work (PoW) to Proof-of-Stake (PoS) <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While the Ethereum Foundation generally advises that users do not need to take any action in preparation for the Merge <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, some individuals are taking precautionary steps due to concerns about replay attacks <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## What is a Replay Attack?

A replay attack occurs when a transaction, valid on one blockchain, is rebroadcast and executed on another chain, often unintentionally by the user <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

Consider a scenario where the Ethereum PoW chain (ETHPoW) continues to operate after the Merge <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. If a user has an NFT listing that gets accepted on the ETHPoW chain, that same transaction could potentially be "replayed" and broadcast on the more valuable Ethereum PoS chain <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This could result in the loss of a valuable NFT on the main PoS chain <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Blockstream has also highlighted this potential risk <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Protections Against Replay Attacks

There are typically two main protections considered against replay attacks:

### OpenSea's Stance
OpenSea has stated that it will not support ETHPoW <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. However, there's uncertainty if transactions could still occur at the smart contract level regardless of platform support <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### EIP-155 and [[understanding_chain_id_in_cryptocurrency | Chain ID]]
In 2016, during the Ethereum hard fork that created Ethereum Classic (ETC), EIP-155 was implemented to protect against replay attacks <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This was necessary because both ETC and Ethereum (ETH) initially shared a Network ID of '1' <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. EIP-155 introduced the concept of a [[understanding_chain_id_in_cryptocurrency | Chain ID]], an additional identifier to distinguish networks <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. For example, ETH has a [[understanding_chain_id_in_cryptocurrency | Chain ID]] of '1', while ETC has a [[understanding_chain_id_in_cryptocurrency | Chain ID]] of '61' <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Transactions on one chain cannot be replayed on another if they have different [[understanding_chain_id_in_cryptocurrency | Chain ID]]s.

## Current Risk with ETHPoW

As of the time of recording, while ETHPoW has announced a proposed [[understanding_chain_id_in_cryptocurrency | Chain ID]] of 1001, they have not yet implemented it <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This means that ETHPoW is currently sharing the same [[understanding_chain_id_in_cryptocurrency | Chain ID]] as Ethereum PoS, leaving it vulnerable to replay attacks <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## Precautionary Steps

To mitigate the risk of replay attacks, some users are canceling all their OpenSea listings and offers prior to the Merge <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This can be done efficiently by going to the profile, then "more," then "offers made," and selecting "cancel all listings and offers" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This method also results in cheaper gas fees compared to canceling items individually <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The idea is to relist items once the network dust settles <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

The easiest approach for most users remains to do nothing and hold their ETH in a core wallet <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. However, for those interested in potentially claiming an ETHPoW airdrop, resources like a post by the CEO of CoinGecko can provide steps to take advantage of the Merge, while still advising caution regarding replay attacks, especially given ETHPoW's current [[understanding_chain_id_in_cryptocurrency | Chain ID]] status <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.