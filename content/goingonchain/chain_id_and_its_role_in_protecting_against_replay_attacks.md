---
title: Chain ID and its role in protecting against replay attacks
videoId: tloTgDASGQs
---

From: [[goingonchain]] <br/> 

Chain ID is a mechanism designed to differentiate between blockchain networks, primarily to protect against [[replay_attacks_and_their_risks | replay attacks]] <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Understanding Replay Attacks
A [[replay_attacks_and_their_risks | replay attack]] occurs when a transaction that is valid on one blockchain is also valid and executed on another blockchain <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This risk becomes particularly prevalent during a blockchain fork, where a network splits into two or more distinct chains that initially share the same transaction history and state <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

For example, if a user's NFT listing is accepted on an "EthW" (Proof-of-Work) chain, there's a possibility this transaction could be replayed and broadcast on the "PoS" (Proof-of-Stake) chain, potentially leading to the loss of a valuable NFT on the main chain <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## EIP-155: A Solution to Replay Attacks
In 2016, during the Ethereum fork that led to Ethereum Classic (ETC), [[EIP1559_and_its_Impact_on_Ethereum_Issuance | EIP-155]] was implemented to provide protection against [[replay_attacks_and_their_risks | replay attacks]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Prior to this, both Ethereum (ETH) and Ethereum Classic (ETC) shared a network ID of one <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

[[EIP1559_and_its_Impact_on_Ethereum_Issuance | EIP-155]] introduced the concept of Chain ID as an additional way to distinguish between networks <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   Ethereum (ETH) was assigned a Chain ID of 1 <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   Ethereum Classic (ETC) received a Chain ID of 61 <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

By including the Chain ID in the transaction signature, a transaction signed for one chain (e.g., ETH) becomes invalid on another chain (e.g., ETC) because the Chain IDs do not match, thereby preventing [[replay_attacks_and_their_risks | replay attacks]] <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Current Concerns: ETHPoW and Chain ID
Despite the established practice of using Chain IDs to prevent [[replay_attacks_and_their_risks | replay attacks]], concerns can arise if new chains do not properly implement their own unique Chain ID. For instance, while a proposed "ETHPoW" chain released a Chain ID of 1001, it has not yet implemented this in its source code, meaning it still shares the same Chain ID as the main Ethereum network <a class="yt=" data-t="00:01:52">[00:01:52]</a>. This oversight creates an opportunity for [[replay_attacks_and_their_risks | replay attacks]] for users interacting with such a chain <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## User Mitigation
To mitigate the risk of [[replay_attacks_and_their_risks | replay attacks]], some users choose to cancel all active listings and offers on platforms like OpenSea before significant network changes or potential forks, especially if the alternative chain has not implemented a distinct Chain ID <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Although OpenSea stated it would not support ETHPoW, the possibility of transactions occurring at the smart contract level remained a concern <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Canceling offers and listings can be done in bulk to reduce gas fees <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.