---
title: Permissionless and modular aspects of Mofo
videoId: JSv0xYMS9_I
---

From: [[goingonchain]] <br/> 
Mofo is a [[multichain_lending_and_borrowing_protocol | lending and borrowing market]] notable for its advanced technology, which even Compound is considering adopting, and Berachain plans to license and fork <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Its core strengths lie in its permissionless and modular design <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Permissionless Aspects

Mofo markets are entirely permissionless <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This means anyone can create a new Mofo market by providing five essential parameters:
*   Collateral asset <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
*   Loan asset <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
*   Loan-to-Value (LLTV) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
*   Interest rate model <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
*   Oracle <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>

Once these parameters are set in the smart contract, they become immutable and cannot be changed <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This provides users with certainty that market conditions will not change unexpectedly <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. In [[comparison_between_mofo_and_aave_markets | contrast to platforms like Aave]], where updates to tokens or interest rates require a governance model, Mofo allows for a more decentralized and predictable creation of markets <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Modular Aspects

Mofo's modularity is evident in its [[mofo_lending_and_borrowing_market_features | isolated market structure]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Each lending and borrowing pair operates as an independent market <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. For example, if a user supplies ETH to the WETH-USDC market, they can only borrow assets within that specific market <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. They cannot borrow from other isolated markets, such as cBTC-USDC, even if they have supplied collateral elsewhere <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This differs significantly from platforms like Aave, where supplied collateral enters a large common pool, allowing borrowing from a wide list of assets within that pool <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Benefits of Modularity
*   **Enhanced Security**: The primary [[isolated_markets_benefits_in_mofo | benefit of isolated markets]] is security <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. If one market (e.g., WETH) is exploited, the rest of the Mofo markets remain unaffected <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Flexibility and Integration**: The modular design makes Mofo easier to integrate <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Berachain, for instance, seeks Mofo's new, clean, and modular money market to plug into its native tokenomics system <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Curator System**: The "earn" section of Mofo also demonstrates modularity. Users provide liquidity to "votes," which are created and managed by [[role_of_curators_and_earning_yield_in_mofo | curators]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. These curators actively manage the capital, allocating it to different markets created within Mofo, creating a modular system of capital deployment <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Overall, Mofo's permissionless market creation and modular, isolated structure contribute to its growing traction compared to older DeFi applications <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.