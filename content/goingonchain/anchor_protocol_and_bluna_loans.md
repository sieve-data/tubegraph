---
title: Anchor Protocol and bLuna Loans
videoId: uoTmNMkp9-Y
---

From: [[goingonchain]] <br/> 

On the [[anchor_protocol_business_model | Anchor Protocol]], users can take out loans by depositing bLuna as collateral <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The recommended Loan-to-Value (LTV) ratio is 45% <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Users face liquidation if their LTV reaches 60% <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## [[Collateral management for borrowing on Anchor | Liquidation Process for bLuna]]

If a user's collateral value drops, increasing their LTV above 60%, their bLuna collateral will be liquidated <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. The user gets to keep the borrowed funds, but loses their bLuna <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

For example:
*   Assume bLuna is valued at $50 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
*   Depositing 2 bLuna collateralizes $100 <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   This allows borrowing $45 (45% LTV) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   If bLuna drops to $30, the 2 bLuna collateral is now worth $60 <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   The LTV becomes 75% ($45 / $60), which exceeds the 60% liquidation threshold <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   The collateral (bLuna) is liquidated <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### Liquidation Auctions

Once liquidated, the bLuna is typically acquired by "whales" or "bots" through a liquidation auction <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

The auction mechanism works as follows:
*   Suppose the highest bid for bLuna is $25, while the market price is $30 <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   The difference is $5, meaning the bidder is acquiring the bLuna at a 16.6% "premium" (or discount relative to market price) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## [[OCRA Kujira Platform for Buying Liquidated bLuna | OCRA Kujira Platform]]

[[OCRA Kujira Platform for Buying Liquidated bLuna | OCRA]] is a platform that allows retail users to participate in bidding for liquidated bLuna <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

When bidding:
*   Users submit a "premium" <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. A higher premium means a user is willing to pay less for the bLuna <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   The bid is placed with a UST amount as a deposit <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   The system prioritizes bids with the lowest premium <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. A 0% premium means buying bLuna at the market price <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

[[OCRA Kujira Platform for Buying Liquidated bLuna | OCRA]] charges a 1% fee when a user withdraws their discounted bLuna <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

[[OCRA Kujira Platform for Buying Liquidated bLuna | OCRA]]'s revenue sources include UST from smart contract execution and the 1% withdrawal fee <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. They also have their own Kujira tokens, which can be used to pay transaction fees at a 50-90% discount on the UST value <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

The [[OCRA Kujira Platform for Buying Liquidated bLuna | Kujira]] team has strong investors and partners <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. While potentially less exciting in a bull market, such platforms could offer good deals when the market turns <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.