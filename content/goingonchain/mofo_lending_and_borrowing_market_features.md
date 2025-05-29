---
title: Mofo lending and borrowing market features
videoId: JSv0xYMS9_I
---

From: [[goingonchain]] <br/> 

Mofo is a [[introduction_to_cryptocurrency_lending_platforms | lending and borrowing market]] that has gained attention for its advanced technology, with entities like Compound looking to adopt its features and Bar Chain paying a license fee to fork its technology <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Borrowing (Mofo Blue)
The borrowing section of Mofo is referred to as "Mofo Blue" <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. A key feature of Mofo's borrowing markets is their [[isolated_markets_benefits_in_mofo | isolated]] nature <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Isolated Markets
In Mofo, each row in the borrow section represents a distinct, [[isolated_markets_benefits_in_mofo | isolated market]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This means:
*   If a user supplies collateral (e.g., 0.1 ETH) into a specific market (e.g., WETH/USDC), they can only borrow assets *within that same market* <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   They cannot borrow from other unrelated markets, such as cBBTC/USDC, even if they have supplied collateral elsewhere <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

This contrasts with platforms like [[comparison_between_mofo_and_aave_markets | Aave]], where supplying collateral into a common pool allows borrowing from a wide list of assets within that pool <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Benefit of Isolated Markets
The primary [[isolated_markets_benefits_in_mofo | benefit of isolated markets]] is risk containment <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. If one market (e.g., WETH) is exploited, the rest of the Mofo markets remain unaffected <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Permissionless and Modular Design
All markets within Mofo are [[permissionless_and_modular_aspects_of_mofo | permissionless]], meaning anyone can create a Mofo market <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. To create a market, five specific parameters must be provided <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>:
1.  Collateral asset <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
2.  Loan asset <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
3.  LLTV (Loan-to-Value) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
4.  Interest rate model <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
5.  Oracle <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>

Once these parameters are set in the smart contract, they are immutable and cannot be changed <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This provides users with certainty that market parameters will not change unexpectedly <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This contrasts with platforms like [[comparison_between_mofo_and_aave_markets | Aave]], where updates to new tokens or interest rates typically go through a governance model <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Earning (Yield Generation)
The "Earn" section of Mofo features "votes," where users can provide liquidity to earn yield <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Curators**: These "votes" are created and managed by curators <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Curators actively manage the deposited capital and charge a performance fee (e.g., 15%) for their services <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Liquidity Flow**: The liquidity provided by users in these "votes" is then directed by curators into the different [[isolated_markets_benefits_in_mofo | isolated markets]] created on Mofo <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. For example, 77% of USDC deposited into the "seamless USDC vote by Gunlett" might be allocated to the cBBTC/USDC market <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Why Mofo's Tech is Valued
Mofo's [[permissionless_and_modular_aspects_of_mofo | modular and permissionless]] design makes it highly attractive <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. While older DeFi applications like Compound are seeing their Total Value Locked (TVL) decline, Mofo, as a newer [[introduction_to_cryptocurrency_lending_platforms | lending protocol]], has been gaining traction <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

Bar Chain, for instance, is interested in Mofo's technology because they need a clean, modular money market to integrate into their system <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Mofo's modularity facilitates easier integration into native tokenomics <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.