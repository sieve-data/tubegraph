---
title: Understanding chain ID in cryptocurrency
videoId: tloTgDASGQs
---

From: [[goingonchain]] <br/> 

A Chain ID is a numerical identifier used to distinguish different blockchain networks. Its primary purpose is to prevent "replay attacks" by ensuring that transactions intended for one chain cannot be maliciously re-broadcast and executed on another chain <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Replay Attacks

A replay attack occurs when a valid transaction from one blockchain is copied and re-broadcast on a different, but related, blockchain <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This risk becomes particularly relevant during blockchain splits or forks.

### How Replay Attacks Work

Consider a scenario where a blockchain undergoes a fork, resulting in two separate chains (e.g., a Proof-of-Work (PoW) chain and a Proof-of-Stake (PoS) chain). If a transaction, such as an NFT listing being accepted, occurs on the less valuable PoW chain, there's a possibility that this transaction could be replayed and broadcast on the more valuable PoS chain. This could lead to a user's valuable NFT being lost on the PoS chain due to a transaction they only intended for the PoW chain <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## EIP-155: Preventing Replay Attacks

To combat replay attacks, EIP-155 (Ethereum Improvement Proposal 155) was implemented in 2016 during the fork that led to Ethereum Classic (ETC) and Ethereum (ETH) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Both ETC and ETH initially shared a network ID of 1 <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. EIP-155 introduced the concept of a Chain ID as an additional way to differentiate networks. For instance, after EIP-155, ETH was assigned a Chain ID of 1, while ETC received a Chain ID of 61 <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This ensures that transactions are valid only on the chain they were intended for, based on their signed Chain ID.

## Ethereum PoW (ETHW) and Chain ID Issues

Following the Ethereum Merge, which transitioned the mainnet from Proof-of-Work (PoW) to Proof-of-Stake (PoS) <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, a new Ethereum PoW chain (ETHW) was created by miners continuing the PoW mechanism <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. While the ETHW team released a proposed Chain ID of 10001, they have not yet implemented it in their source code <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This means that the ETHW chain currently shares the same Chain ID as the main Ethereum PoS chain <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This situation creates a potential vulnerability to replay attacks between the two chains <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Protecting Against Replay Attacks (User Actions)

Although platforms like OpenSea have stated they are not supporting ETHW, the possibility of transactions taking place at the smart contract level remains <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. To mitigate the risk of replay attacks, users can cancel all their existing offers and listings on NFT marketplaces like OpenSea, as this action incurs a cheaper gas fee compared to canceling individual listings <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Once the situation stabilizes, listings can be restored <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.