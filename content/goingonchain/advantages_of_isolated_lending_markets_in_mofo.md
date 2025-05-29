---
title: Advantages of isolated lending markets in Mofo
videoId: JSv0xYMS9_I
---

From: [[goingonchain]] <br/> 

Mofo is a [[introduction_to_cryptocurrency_lending_platforms | lending and borrowing market]] designed with a unique architecture that sets it apart from traditional common pool models like Aave <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Its core innovation lies in the use of isolated lending markets, offering several key advantages <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Understanding Isolated Markets

In Mofo, each row in the "borrow" section represents a distinct and isolated market <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Unlike platforms where supplying collateral contributes to a large common pool from which multiple assets can be borrowed, Mofo restricts borrowing to assets *within* the specific market where collateral was provided <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. For example, if you supply 0.1 ETH into the WETH and USDC market, you can only borrow WETH or USDC from that specific market; you cannot borrow from other isolated markets like CBTC USDC <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Key Advantages

### Enhanced Risk Mitigation

One of the primary benefits of isolated markets is significantly reduced contagion risk <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. If one market, such as the WETH market, were to be exploited or experience a significant issue, the isolation ensures that "the rest of the markets are not affected" <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This compartmentalization of risk is a crucial security feature.

### [[permissionless_and_customizable_markets_in_mofo | Permissionless and Customizable Market Creation]]

The isolated nature of Mofo's markets allows for [[permissionless_and_customizable_markets_in_mofo | permissionless market creation]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Anyone can create a Mofo market by providing five essential parameters:
*   Collateral asset <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
*   Loan asset <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
*   Loan-to-Value (LLTV) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>
*   Interest rate model <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
*   Oracle <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>

While these parameters are customizable upon creation, they are fixed once set in the smart contract, providing users with certainty that market conditions will not change unexpectedly <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This contrasts with governance-led changes in common pool protocols <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Modular Design and Easier Integration

Mofo's modular and permissionless design, stemming from its isolated markets, makes its technology highly attractive for integration by other platforms <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. For instance, Vera Chain is looking to pay a license fee to fork Mofo's technology due to its modularity <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, allowing them to plug a "clean modular money market" into their existing system <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This ease of integration highlights a significant advantage for the [[adoption_of_mofo_technology_by_other_platforms | adoption of Mofo technology by other platforms]].