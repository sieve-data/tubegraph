---
title: How Kujira auction system works
videoId: uoTmNMkp9-Y
---

From: [[goingonchain]] <br/> 

Kujira introduces an auction system designed to allow retail users to participate in the liquidation of bLuna (bonded Luna), a process traditionally dominated by large institutional players or bots <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This system, referred to as Orca, enables users to [[buying_luna_for_cheap_using_kujira | buy Luna for cheap]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## The Liquidation Process

Users can take loans via Anchor Protocol by depositing bLuna as collateral <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.
The recommended Loan-to-Value (LTV) is 45% <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
Liquidation occurs if the LTV reaches 60% <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### Example of Liquidation
Assume bLuna is $50:
*   Depositing 2 bLuna (worth $100) allows borrowing $45 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
*   If bLuna drops to $30, the 2 bLuna collateral becomes worth $60 <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   The LTV then becomes 75% ($45 borrowed / $60 collateral), exceeding the 60% liquidation threshold <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   The user keeps the $45 borrowed but loses their bLuna <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

The bLuna from these liquidations then enters the auction system <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Kujira (Orca) Auction System

The Orca platform allows retail users to bid for liquidated bLuna <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### How Bidding Works
1.  **Premium/Discount Bids**: Bidders place a "premium" or discount bid <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    *   For example, if the highest bid is $25 and the market price is $30, the difference of $5 means the bidder is getting the bLuna at a 16.6% "premium" or discount <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
2.  **Placing Bids**: Users input their desired [[premium_bids_and_discounts_for_bluna | premium]] (e.g., 10%) and deposit UST <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
    *   A higher premium means the user is willing to pay less for the bLuna <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   Bids typically range from 4% to 6% premium <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
3.  **Bid Execution**: The system triggers bids with the lowest premium first <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
    *   A 0% premium means buying bLuna at the market price <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
4.  **Outcome**: Successful bidders acquire discounted bLuna <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## [[kujiras_revenue_model_and_investor_insights | Kujira's Revenue Model and Investor Insights]]

Orca generates revenue from two primary sources <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
1.  UST from smart contract execution <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
2.  A 1% withdrawal fee charged when users withdraw their discounted bLuna <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

Kujira also has its own tokens, called GUCCI tokens, which can be used to pay transaction fees <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Paying with GUCCI tokens offers a discount of 50% to 90% on the UST value of the fees <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

The team behind Kujira has strong investors and partners <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The project was scheduled to conduct its Initial DEX Offering (IDO) on November 12th <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. While potentially less exciting in a bull market, such systems can offer significant opportunities to acquire assets at good deals during market downturns <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.