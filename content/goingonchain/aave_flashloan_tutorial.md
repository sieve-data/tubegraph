---
title: Aave flashloan tutorial
videoId: TNtVGKD9IOY
---

From: [[goingonchain]] <br/> 

## Understanding Flashloans

A [[flashloan_technique | flash loan]] is a technique that allows users to borrow a large amount of cryptocurrency with very low cost, with the critical condition that the borrowed amount must be repaid within the same blockchain transaction (or "block") <a class="yt-timestamp" data-t="01:14:875">[01:14:875]</a>. If the loan is not repaid in the same block, the entire transaction reverts, as if it never happened.

## Aave's Role in Flashloans

While this article details a specific flashloan exploit, Aave provides documentation and tutorials for those interested in learning more about how to use [[flashloan_technique | flash loans]] <a class="yt-timestamp" data-t="01:53:725">[01:53:725]</a>.

## Case Study: The Anonymous Flashloan Exploit with BAYC and ApeCoin

An anonymous individual successfully leveraged a [[flashloan_technique | flash loan]] to acquire approximately $800,000 worth of ApeCoin (APE) tokens by exploiting the airdrop mechanics of Bored Ape Yacht Club (BAYC) NFTs <a class="yt-timestamp" data-t="01:44:815">[01:44:815]</a>.

### ApeCoin Airdrop Mechanism

The ApeCoin airdrop for BAYC holders had a unique aspect: there was no snapshot <a class="yt-timestamp" data-t="01:16:35">[01:16:35]</a>. This meant that as long as one owned a BAYC NFT, they could claim the ApeCoin tokens once <a class="yt-timestamp" data-t="01:00:155">[01:00:155]</a>. At the time of the exploit, one BAYC NFT was entitled to about 10,000 ApeCoin tokens, valued at approximately $130,000 <a class="yt-timestamp" data-t="00:07:115">[00:07:115]</a>.

### The NFTX Vault

The anonymous actor identified a vault on NFTX that contained five BAYC NFTs <a class="yt-timestamp" data-t="00:32:445">[00:32:445]</a>. This vault allowed the contained BAYC NFTs to be tokenized, similar to how a real estate investment trust (REIT) represents ownership of underlying assets <a class="yt-timestamp" data-t="00:40:485">[00:40:485]</a>. Importantly, these five BAYC NFTs in the vault had not yet claimed their ApeCoin tokens <a class="yt-timestamp" data-t="00:52:955">[00:52:955]</a>.

### The Flashloan Process

The anonymous individual executed the following steps within a single Ethereum transaction:
1.  **Acquire BAYC Token:** They initially acquired a BAYC token from OpenSea, costing around $300,000 <a class="yt-timestamp" data-t="01:06:585">[01:06:585]</a>.
2.  **Flashloan Initiation:** This acquired BAYC token was then used as collateral on the NFTX vault to take out a [[flashloan_technique | flash loan]] <a class="yt-timestamp" data-t="01:09:595">[01:09:595]</a>.
3.  **Borrow and Claim:** Within the same transaction, the anon borrowed the five BAYC NFTs from the vault <a class="yt-timestamp" data-t="01:21:405">[01:21:405]</a>. They immediately used these borrowed NFTs to claim approximately 60,000 ApeCoin tokens <a class="yt-timestamp" data-t="01:24:905">[01:24:905]</a>.
4.  **Repay and Sell:** The borrowed BAYC NFTs were returned to the vault <a class="yt-timestamp" data-t="01:28:905">[01:28:905]</a>. The anon then sold the initial BAYC token they had purchased back to the vault <a class="yt-timestamp" data-t="01:37:925">[01:37:925]</a>. Finally, the claimed ApeCoin tokens were sold <a class="yt-timestamp" data-t="01:40:875">[01:40:875]</a>.

### Outcome

Through this sophisticated execution within a single transaction, the anonymous individual reportedly profited about $800,000 <a class="yt-timestamp" data-t="01:44:815">[01:44:815]</a>. This event sparked discussion on whether such a maneuver constitutes an attack or a form of arbitrage <a class="yt-timestamp" data-t="01:47:335">[01:47:335]</a>.