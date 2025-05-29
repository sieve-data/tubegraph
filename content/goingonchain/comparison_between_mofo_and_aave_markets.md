---
title: Comparison between Mofo and Aave markets
videoId: JSv0xYMS9_I
---

From: [[goingonchain]] <br/> 

Mofo is a lending and borrowing market that has garnered attention, with Compound reportedly looking to adopt its technology and Vera Chain planning to pay a license fee to fork it <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Despite not having a flashy front end, Mofo's underlying technology offers significant advantages in its market structure <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Market Structure: Isolated vs. Common Pool

### Mofo: Isolated Markets (Mofo Blue)
Mofo operates with [[mofo_lending_and_borrowing_market_features | isolated markets]], also known as Mofo Blue <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Each row on the "borrow" tab represents an independent market <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

*   **Borrowing Logic**: In Mofo, if a user supplies collateral to a specific market (e.g., WETH and USDC), they can only borrow assets *within that same market* <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. For example, supplying 0.1 ETH to the WETH/USDC market allows borrowing USDC from that market, but not from other markets like CBTC/USDC <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Benefits of Isolation**: The primary benefit of [[isolated_markets_benefits_in_mofo | isolated markets]] is risk containment <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. If one market, such as WETH/USDC, were to be exploited, the other isolated markets would remain unaffected <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Aave: Common Pool
In contrast to Mofo, Aave utilizes a large common pool for its assets <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

*   **Borrowing Logic**: When a user supplies collateral to Aave (e.g., 0.1 ETH), they are supplying into a single, large common pool <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. From this common pool, they are then able to borrow from a list of various assets available within that pool <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Market Creation and Customization

### Mofo: Permissionless and Modular
Mofo distinguishes itself through its [[permissionless and modular aspects of Mofo | permissionless and modular]] design <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

*   **Market Creation**: Anyone can create a Mofo market by providing five specific parameters: the collateral asset, loan asset, Loan-to-Value (LLTV), interest rate model, and oracle <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Fixed Parameters**: While these parameters are customizable upon creation, once they are set in the smart contract, they cannot be changed <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This provides users with certainty that market parameters will not change unexpectedly <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Aave: Governance Model
Aave, on the other hand, manages updates and changes through a governance model <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

*   **Updates**: Updates such as adding new tokens or changing interest rates go through a governance process <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Earning Yield and Curators in Mofo

Mofo also features an "earn" section where users can provide liquidity and earn yield <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

*   **Votes and Curators**: These "votes" are created and managed by [[role_of_curators_and_earning_yield_in_mofo | curators]], who actively manage the vote and charge a performance fee (e.g., 15%) for their services <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Liquidity Flow**: The liquidity provided by users in these votes (e.g., USDC in a seamless USDC vote) is then allocated by curators to different markets <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. For instance, 77% of USDC from a vote might go into the CBUSDC market, where it can be borrowed <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This demonstrates how liquidity from the "earn" side flows into the various isolated markets created on Mofo <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Mofo's Growing Traction

While established protocols like Compound have seen their Total Value Locked (TVL) decrease relative to other DeFi applications, Mofo, as a newer lending protocol, has been gaining significant traction <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Vera Chain's interest in Mofo's technology stems from its modular design, which makes it easier to integrate a new, clean money market into their native tokenomics system <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.