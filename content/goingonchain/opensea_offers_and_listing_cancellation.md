---
title: Opensea offers and listing cancellation
videoId: tloTgDASGQs
---

From: [[goingonchain]] <br/> 

Ahead of "the Merge," a significant change to Ethereum's consensus layer from Proof-of-Work (PoW) to Proof-of-Stake (PoS), users might consider cancelling their offers and listings on [[how_to_revoke_opensea_contract | Opensea]] [00:00:04]. While the Ethereum Foundation Vlog states that users technically do not need to do anything for the Merge [00:00:09], some individuals choose to take precautionary measures due to concerns about potential "replay attacks" [00:00:47].

## How to Cancel All Offers and Listings on Opensea

To cancel all your offers and listings on [[how_to_revoke_opensea_contract | Opensea]] at once, rather than individually [00:00:28]:
1.  Navigate to your profile [00:00:32].
2.  Go to "More" [00:00:33].
3.  Select "Offers" [00:00:34].
4.  There will be an option to "Cancel all listing and offer" [00:00:35].
This method is also noted to have cheaper gas fees compared to canceling items one by one [00:00:40].

## The Risk of Replay Attacks

The primary reason for cancelling offers and listings is concern over "replay attacks" [00:00:47].

### What is a Replay Attack?
A replay attack occurs if, after the Merge, a Proof-of-Work (PoW) chain (referred to as ETHW) continues to exist [00:00:54]. If a listing of yours is accepted on the ETHW chain for a certain amount of ETH (e.g., 1 ETH) [00:00:59], and that ETH on the ETHW chain has a low value [00:01:04], there is a possibility that this transaction could be "replayed" and broadcast on the legitimate Proof-of-Stake (PoS) chain [00:01:06]. This could result in your valuable NFT being sold on the PoS chain at the low value of the ETHW chain [00:01:11]. Lookonchain also highlighted this potential risk [00:01:17].

### Protections and Remaining Concerns
There are two factors related to protecting against replay attacks:
1.  **Opensea's Stance**: [[how_to_revoke_opensea_contract | Opensea]] has stated that it will not support the ETHW chain [00:01:22]. However, there is uncertainty if transactions could still occur at the smart contract level regardless of platform support [00:01:26].
2.  **EIP-155 Implementation**: During the 2016 Ethereum (ETH) fork to Ethereum Classic (ETC), EIP-155 was implemented to provide protection against replay attacks [00:01:31]. This was necessary because both ETC and ETH initially shared a network ID of one [00:01:39]. Chain IDs were introduced as an additional way to differentiate networks [00:01:42], with ETH having a chain ID of 1 and ETC having a chain ID of 61 [00:01:47].
    *   **ETHW's Chain ID Issue**: While ETHW has released its intended chain ID (10001), it had not implemented it by the time of this video [00:01:52]. Its source code showed the change commented out, meaning it was still sharing the same chain ID as the main Ethereum chain [00:01:58]. This lack of a distinct chain ID leaves it vulnerable to replay attacks [00:02:32].

Given these concerns, some users, not being "gigabrains," choose to cancel all their listings and offers to avoid potential issues [00:02:05]. Once the dust settles after the Merge, listings can be re-established [00:02:08].

## Alternative Approach
The easiest thing to do is to "do nothing" and simply hold your ETH in your core wallet [00:02:12]. However, if you are interested in an ETHW airdrop, you might look into strategies shared by figures like the CEO of CoinGecko, who discussed seven steps to potentially take full advantage of the Merge [00:02:17].