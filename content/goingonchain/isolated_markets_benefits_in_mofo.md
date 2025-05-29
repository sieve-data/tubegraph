---
title: Isolated markets benefits in Mofo
videoId: JSv0xYMS9_I
---

From: [[goingonchain]] <br/> 

Mofo is a decentralized lending and borrowing market that stands out due to its unique architecture, particularly its use of isolated markets <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This design offers significant advantages over traditional common pool models.

## What Are Isolated Markets?

In Mofo, each lending and borrowing pair, referred to as a "market," is isolated <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This means that if a user supplies collateral to one market (e.g., WETH and USDC), they can only borrow assets from within that specific market <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. For instance, supplying ETH in the WETH-USDC market allows borrowing USDC from that market, but not from other markets like CBTC-USDC <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

This contrasts with platforms like Aave, where supplying collateral into a large common pool enables borrowing from a wide list of assets within that pool <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Benefits of Isolated Markets

The primary advantage of Mofo's isolated market structure is enhanced security and risk mitigation:

*   **Containment of Exploits:** If one market, for example, the WETH market, were to be exploited, the isolation ensures that the rest of the markets on Mofo remain unaffected <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This prevents a cascading failure across the entire protocol, protecting users in other markets.

## Permissionless and Modular Design

Mofo's markets are entirely permissionless, allowing anyone to create a new market by providing five specific parameters: the collateral asset, loan asset, Loan-to-Value (LLTV), interest rate model, and oracle <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. These parameters are customizable but become immutable once set in the smart contract, providing users with certainty about the market's rules <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This "modular" aspect, coupled with isolation, makes Mofo distinct from protocols like Compound, where updates and new token listings require governance votes <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Role of Curators

While markets are isolated, liquidity can be actively managed by "curators." Curators create "votes" where users can provide liquidity and earn yield <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Curators manage this liquidity and allocate capital across different isolated markets to optimize yield, taking a performance fee <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. For instance, a curator might deposit USDC into a vote and then allocate a significant portion to a specific market like CBTC-USDC <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This demonstrates how liquidity from these votes flows into the distinct, isolated markets <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Adoption by Other Protocols

The modular and permissionless nature of Mofo, facilitated by its isolated markets, has attracted attention from other major protocols <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Compound is looking to adopt Mofo's technology, and Vera Chain is willing to pay a license fee to fork it <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Vera Chain specifically seeks a new, clean, and modular money market that can be easily integrated into its native tokenomics <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.