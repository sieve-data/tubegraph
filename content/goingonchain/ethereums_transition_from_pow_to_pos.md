---
title: Ethereums transition from POW to POS
videoId: tloTgDASGQs
---

From: [[goingonchain]] <br/> 

The upcoming [[the_merge_on_ethereum | Merge]] is a significant change for Ethereum, transitioning its consensus layer from [[proof_of_work_vs_proof_of_stake | Proof of Work (PoW)]] to [[proof_of_work_vs_proof_of_stake | Proof of Stake (PoS)]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The mainnet is expected to remain the same <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Preparing for The Merge

According to the [[ethereum_merge_and_its_implications | Ethereum Foundation]], users generally do not need to take any action to prepare for [[the_merge_on_ethereum | The Merge]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The simplest approach for users is to do nothing and hold their Ethereum in a core wallet <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

However, some users may choose to take precautions or prepare for potential scenarios like an Ethereum PoW (ETH PoW) airdrop <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Managing OpenSea Listings and Offers

One specific preparation step involves managing existing listings and offers on platforms like OpenSea <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Users can cancel all their listings and offers simultaneously, which is more gas-efficient than cancelling them one by one <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This can be done by navigating to "Profile," then "More," and finally "Offers" to find the "Cancel all listings and offer" option <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

This action is primarily taken out of concern for potential [[smart_contract_migration_issues_on_opensea | replay attacks]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. After [[the_merge_on_ethereum | The Merge]], users can relist their items once the situation stabilizes <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Replay Attacks

A replay attack is a potential risk where a transaction executed on one blockchain (e.g., a hypothetical ETH PoW chain) could be re-broadcast and accepted on another chain (e.g., the new [[proof_of_work_vs_proof_of_stake_in_ethereum | Ethereum PoS]] chain), potentially leading to unintended loss of valuable assets like NFTs <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This potential risk has been highlighted by various sources <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Protections Against Replay Attacks

Several mechanisms are in place or have been proposed to mitigate replay attacks:

*   **OpenSea Policy:** OpenSea has stated it will not support the ETH PoW chain <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. However, there is uncertainty about whether this prevents transactions from occurring at the smart contract level <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **EIP-155:** Implemented in 2016 during the Ethereum (ETH) and Ethereum Classic (ETC) fork, EIP-155 provides protection against replay attacks <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. It introduced "Chain IDs" as an additional way to differentiate networks <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. For example, ETH has a Chain ID of 1, while ETC has a Chain ID of 61 <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### ETH PoW Chain ID Status

While the proposed ETH PoW chain has released a Chain ID of 1001, it has not yet been fully implemented in their source code (it is currently commented out) <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This means that, as of the time of the transcript, the ETH PoW chain and the main Ethereum chain are still sharing the same Chain ID, which increases the potential for replay attacks <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.