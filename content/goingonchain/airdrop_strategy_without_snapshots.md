---
title: AirDrop strategy without snapshots
videoId: TNtVGKD9IOY
---

From: [[goingonchain]] <br/> 

The APEcoin (APE) token airdrop presented a unique opportunity due to its "no snapshot" rule. Typically, cryptocurrency airdrops involve a "snapshot" where a record of asset holders is taken at a specific time, and only those holders are eligible for the airdrop [00:01:14]. However, with the APEcoin airdrop, as long as an individual owned a Bored Ape Yacht Club (BAYC) NFT, they could claim the APEcoin token once, regardless of when they acquired the BAYC [00:01:01]. This rule caused the floor price of BAYC NFTs to increase [00:00:23].

At the time of the airdrop, APEcoin was valued at approximately $13 per token [00:00:04]. Each BAYC holder was eligible to receive about 10,000 APE tokens, equating to approximately $130,000 [00:00:09].

## Leveraging Flash Loans for Airdrop Claims

An anonymous individual successfully exploited this "no snapshot" rule using a [[flashloan_techniques_in_cryptocurrency | flash loan]] technique [00:00:26].

### The Mechanism

The strategy involved an NFTX vault that held five BAYC NFTs [00:00:34]. These BAYC NFTs were tokenized within the vault, meaning that holding the vault's token gave ownership of parts of the underlying BAYC assets [00:00:40]. Crucially, these five BAYC NFTs within the vault had not yet claimed their APEcoin tokens [00:00:50].

The anonymous individual executed the following steps in a single Ethereum transaction using a [[flashloan_techniques_in_cryptocurrency | flash loan]] [00:01:21]:
1.  **Borrow BAYC:** The individual borrowed the five BAYC NFTs from the NFTX vault using a [[flashloan_techniques_in_cryptocurrency | flash loan]] [00:01:23]. A [[flashloan_techniques_in_cryptocurrency | flash loan]] allows borrowing a large amount with low cost, provided it is repaid within the same blockchain block [00:01:16].
2.  **Claim APEcoin:** While holding the borrowed BAYC NFTs, the individual immediately claimed the APEcoin tokens associated with them [00:01:25]. This amounted to approximately 60,000 APE tokens [00:01:26].
3.  **Return BAYC:** The borrowed BAYC NFTs were then returned to the NFTX vault [00:01:29].
4.  **Sell APEcoin:** The claimed APEcoin tokens were sold [00:01:40].

### Outcome

Through this single transaction, the anonymous individual walked away with approximately $800,000 [00:01:44]. The nature of this exploit, whether it constitutes an attack or an arbitrage, remains a point of discussion [00:01:47].

For those interested in understanding [[flashloan_techniques_in_cryptocurrency | flash loan]] techniques, Aave (Aave Protocol) provides documentation and tutorials [00:01:55].