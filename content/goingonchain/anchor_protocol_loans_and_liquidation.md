---
title: Anchor protocol loans and liquidation
videoId: uoTmNMkp9-Y
---

From: [[goingonchain]] <br/> 
The [[overview_of_cap_finance_protocol | Anchor Protocol]] allows users to take out loans by depositing bLuna as [[role_of_collateral_in_anchor_protocol | collateral]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This process is part of the [[lending_and_borrowing_process_on_anchor_protocol | lending and borrowing process on Anchor Protocol]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

### Loan Mechanics and Liquidation on Anchor Protocol

When taking a loan on [[overview_of_cap_finance_protocol | Anchor Protocol]], the recommended Loan-to-Value (LTV) ratio is 45% <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Users face liquidation if their LTV reaches 60% <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

For example, if a user deposits 2 bLuna, valued at $50 each, their total collateral is $100 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This allows them to borrow $45 <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. If the price of bLuna drops to $30, the 2 bLuna collateral becomes worth $60 <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. At this point, the LTV reaches 75% ($45 borrowed / $60 collateral), exceeding the 60% liquidation threshold <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. In such a scenario, the user is liquidated, keeping the $45 borrowed but losing their bLuna collateral <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### Liquidation Auctions and Orca Protocol

Historically, liquidated Luna collateral would go to "whales or bots" who participate in liquidation auctions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. These participants could bid on the liquidated bLuna, often securing it at a discount <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. For instance, if the highest bid for bLuna was $25 while the market price was $30, the bidder would acquire the bLuna at a 16.6% "premium" or discount <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

Orca Protocol is a project designed to allow retail users to participate in these liquidation auctions and bid for liquidated bLuna <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

#### How Orca Protocol Works

*   **Bidding Process**: Users can place bids on liquidated bLuna <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Bids are placed with a "premium," typically ranging from 4% to 6% <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. A higher premium indicates a lower willingness to pay for the bLuna <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Users deposit their UST amount as a bid <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Bid Triggering**: The system triggers bids with the lowest premium first <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. A 0% premium means buying bLuna at the market price <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Withdrawal Fee**: Orca charges a 1% fee when users withdraw their discounted bLuna <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Revenue Streams**: Orca generates revenue from two sources: UST from smart contract executions and the 1% withdrawal fee <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **GUCI Tokens**: Orca has its own GUCI tokens, which can be used to pay transaction fees, offering a discount of 50% to 90% off the UST value <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

Orca Protocol has strong investors and partners <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. They conducted their Initial DEX Offering (IDO) on November 12th <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. While potentially less exciting in a bull market, such a project could offer good deals when the market turns <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.