---
title: Flashloan technique
videoId: TNtVGKD9IOY
---

From: [[goingonchain]] <br/> 

A flash loan is a unique decentralized finance (DeFi) mechanism that allows users to borrow substantial amounts of assets without collateral, provided the borrowed amount is repaid within the same blockchain transaction (or "block") <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This means the entire loan, including borrowing and repayment, must occur instantaneously within a single atomic transaction.

## Flashloan Application: BAYC Airdrop Exploitation

An individual ("anon") successfully leveraged a [[aave_flashloan_tutorial | flash loan]] to claim a significant amount of APE tokens from Bored Ape Yacht Club (BAYC) NFTs <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This was made possible by a specific characteristic of the APE token airdrop: there was no snapshot, meaning as long as one owned a BAYC NFT, they could claim the APE tokens once <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This condition also led to a spike in the BAYC floor price <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### The Mechanism Used

The anon identified a vault on NFTX that contained five BAYC NFTs <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Similar to Real Estate Investment Trusts (REITs), owning a token from this NFTX vault meant owning a part of the underlying BAYC assets <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Crucially, these five BAYC NFTs within the vault had not yet claimed their allocated APE tokens <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### The Steps Taken

1.  **Initial Purchase (Simulated):** The anon conceptualized buying a BAYC from OpenSea, which would typically cost around $300,000 <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This step was likely symbolic to set up the context for the flash loan's value.
2.  **Flash Loan Initiation:** The anon used a "collector" function on the NFTX vault to take a flash loan <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
3.  **Borrowing and Claiming:** Within a single Ethereum transaction, the anon borrowed the five BAYC NFTs from the vault via the flash loan <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
4.  **APE Token Claim:** Immediately after borrowing, these BAYC NFTs were used to claim approximately 60,000 APE tokens <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
5.  **Repayment and Profit:** The borrowed BAYC NFTs were returned to the vault in the same transaction <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The claimed APE tokens were then sold <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

Through this sequence, the anon walked away with about $800,000 <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. The nature of this exploit has led to discussion regarding whether it constitutes an attack or an arbitrage opportunity <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

For those interested in learning more about flash loans, Aave provides documentation and tutorials on the subject <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.