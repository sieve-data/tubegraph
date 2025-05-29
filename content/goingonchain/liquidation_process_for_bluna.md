---
title: Liquidation Process for bLuna
videoId: uoTmNMkp9-Y
---

From: [[goingonchain]] <br/> 

When users take out loans on decentralized finance platforms like [[Anchor Protocol and bLuna Loans | Anchor Protocol]], they often deposit bLuna as collateral <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This allows them to borrow money against their deposited bLuna <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Loan-to-Value (LTV) and Liquidation Trigger

A key metric in this process is the Loan-to-Value (LTV) ratio. While the recommended LTV for a loan might be 45% <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>, liquidation occurs if the LTV reaches 60% <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

For example:
*   If you deposit 2 bLuna when bLuna is $50, your collateral is worth $100 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
*   This would typically allow you to borrow $45 <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   If bLuna's price drops to $30, your 2 bLuna are now worth $60 <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   At this point, your LTV would be 75%, exceeding the 60% liquidation threshold <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   When liquidated, the borrower keeps the borrowed funds but loses their bLuna collateral <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Destination of Liquidated bLuna

Historically, liquidated bLuna would primarily go to "whales" or "bots" who participated in a specialized liquidation auction <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. These participants were able to bid for the liquidated bLuna, often acquiring it at a significant discount <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

For instance:
*   If the highest bid from a bot was $25 and the market price was $30 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, the bot would be getting the bLuna at a 16.6% discount (or 16.6% premium relative to their bid price) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Retail Participation via OCRA

The [[OCRA Kujira Platform for Buying Liquidated bLuna | OCRA (Kujira) platform]] aims to democratize this process by allowing retail investors to bid for liquidated bLuna <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Bidding Process on OCRA
*   Users place bids by specifying a "premium" <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   A higher premium means the bidder is willing to pay less for the bLuna <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   Bidders deposit their UST amount <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   The system prioritizes bids with the lowest premium first <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   A premium of 0% essentially means buying bLuna at the current market price <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   Users receive discounted bLuna when their bid is successful <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   OCRA charges a 1% fee upon withdrawal of the purchased bLuna <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### OCRA's Revenue
OCRA generates revenue from two main sources <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>:
1.  UST collected from smart contract executions <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
2.  The 1% withdrawal fee <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

Additionally, OCRA has its own "Kuji" tokens, which can be used to pay transaction fees at a discounted rate of 50% to 90% off the UST value <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. The OCRA team also has notable investors and partners <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. While potentially less exciting in a bull market, these platforms can offer good deals when the market experiences downturns <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.