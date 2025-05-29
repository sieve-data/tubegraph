---
title: Comparison between Morpho and Aave
videoId: JSv0xYMS9_I
---

From: [[goingonchain]] <br/> 

Mofo is a lending and borrowing market with technology that is gaining significant interest <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Compound is looking to [[adoption_of_mofo_technology_by_other_platforms | adopt Mofo's technology]], and Barchain is willing to [[adoption_of_mofo_technology_by_other_platforms | pay a license fee to fork Mofo]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Despite not having a flashy front end <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>, Mofo distinguishes itself through its unique market structure and permissionless nature.

## Mofo Blue (Borrow Section)

Mofo's "Borrow" section, also known as Mofo Blue <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, features isolated markets <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Isolated Markets vs. Common Pool

*   **Mofo (Isolated Markets)**: Each row in the borrow section represents an isolated market <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. If a user supplies collateral in one market (e.g., WETH and USDC market), they can only borrow assets within that specific market <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This means collateral provided in one market cannot be used to borrow from another isolated market <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Aave (Common Pool)**: In contrast, when a user supplies collateral on Aave, they supply it into a large common pool <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. From this common pool, they are able to borrow from a list of assets <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. For example, supplying 0.1 ETH on Aave allows borrowing 50 GH and 50 USDC <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

### Benefits of Isolated Markets

The primary benefit of Mofo's isolated market structure is risk containment <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. If one market were to be exploited (e.g., the WETH market), the rest of the isolated markets would remain unaffected <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Permissionless and Modular Nature

*   **Mofo**: All Mofo markets are permissionless <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Anyone can create a Mofo market by providing five key parameters:
    *   Collateral asset <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>
    *   Loan asset <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
    *   Loan-to-Value (LLTV) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>
    *   Interest rate model <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
    *   Oracle <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
    These parameters are customizable but, once set in the smart contract, cannot be changed <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This provides users with certainty that market parameters will not change unexpectedly <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Aave**: In contrast, updating new tokens or changing interest rates on Aave goes through a governance model <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Earn Section

Mofo's "Earn" section consists of "votes" where users can provide liquidity and earn yield <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

*   **Curated Votes**: These votes are created and managed by "curators" <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Curators actively manage the deposited funds and allocate capital, charging a performance fee (e.g., 15%) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Liquidity Flow**: Liquidity from these "votes" flows into the various isolated markets created in the "Borrow" section <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. For example, 77% of USDC deposited into a "vote" might be allocated to the CBUSDC market <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Why Mofo's Technology is Desired

Mofo's modular and permissionless architecture makes it highly attractive <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. While established DeFi applications like Compound have seen their Total Value Locked (TVL) decline, Mofo, as a newer lending protocol, has been gaining traction <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Barchain is interested in Mofo's technology because it provides a clean, modular money market that can easily plug into their system and integrate with their native tokenomics <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.