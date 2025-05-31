---
title: Understanding Anchor protocol and its liquidations
videoId: iyIKTuLqOMA
---

From: [[when-shift-happens]] <br/> 

Kajira is a platform focused on empowering retail crypto users to compete with large institutional players ("whales and elites") <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. Its first product, Orca, is designed to allow automated bids on collateral liquidated from Anchor Protocol <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. To understand what Kajira's Orca does, it's essential to first understand how [[mechanics_of_anchor_protocol | Anchor Protocol]] works <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

## How Anchor Protocol Works

[[mechanics_of_anchor_protocol | Anchor Protocol]] allows users to put up assets as collateral to borrow [[decentralized_exchanges_and_liquidity_protocols | UST]], a stablecoin pegged to the value of one US dollar <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a><a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a><a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. Borrowers provide assurance in the form of collateral to reduce the risk associated with lending [[decentralized_exchanges_and_liquidity_protocols | UST]] <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a><a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

Key points about [[mechanics_of_anchor_protocol | Anchor Protocol]]'s borrowing system:
*   A borrower puts up non-stable assets as collateral <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
*   The loan is made in a stable asset (UST) <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.
*   Borrowers can withdraw up to 60% of the value from the deposited collateral <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a><a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

## Understanding Liquidations

Liquidations are a core part of [[mechanics_of_anchor_protocol | Anchor Protocol]]'s operation <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.

### When a Loan Becomes At-Risk
A loan is deemed "at risk" if the value of the collateral (or bonded asset) falls to a point where the loan amount exceeds a predefined threshold <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

### The Liquidation Process
When an at-risk loan is liquidated:
1.  Liquidators repay the shortfall on the collateral to the lender (Anchor Protocol) on behalf of the borrower <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a><a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.
2.  Anchor Protocol receives back the [[decentralized_exchanges_and_liquidity_protocols | UST]] it loaned out <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a><a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.
3.  The borrower's collateral becomes the property of the liquidator, and the borrower forfeits that capital <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a><a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a><a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.

### Liquidator Compensation
Liquidators are paid for their service by means of a "premium," which is effectively a discount on the price of the non-stable assets used as collateral <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a><a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. This discount on Orca can vary from 1% to 30% <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

Previously, liquidations operated on a "first come, first served" basis, where the fastest executor of the contract would receive the capital <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. Now, liquidators accepting smaller premiums (lower discounts) are prioritized <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. Bids are filled by working their way up through tiers: all bids at lower premiums are utilized before moving to the next highest premium, until all collateral is shared out or liquidated <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

## Orca Protocol: Automated Liquidation Bids

Orca is Kajira's platform that streamlines the liquidation process, making it accessible to retail users <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. It allows users to "be a killer whale and beat the bots at their own game" <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.

### How to Use Orca
Users place a bid by deciding:
1.  **How much [[decentralized_exchanges_and_liquidity_protocols | UST]] to bid**: There are no minimum or maximum amounts <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>.
2.  **At which premium to bid**: Premiums range from 0% to 30% <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a><a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. The smallest premiums are satisfied first <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.

Once a bid is placed, it can be activated after 10 minutes <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>. Orca handles the actual liquidations <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>.

### Orca Interface
The Orca website displays premium rates from 0% to 30%, along with the "pool value" in [[decentralized_exchanges_and_liquidity_protocols | UST]] at each premium <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>. For example, at a 5% premium, there might be almost 10 million [[decentralized_exchanges_and_liquidity_protocols | UST]] in the pool <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.

Key metrics displayed on Orca:
*   Total locked collateral value in [[mechanics_of_anchor_protocol | Anchor Protocol]]: Currently 3.5 billion <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a><a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a><a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.
*   Total pool value in Orca: Currently 26.4 million <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a><a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>.
*   Total locked collateral in bLuna: Currently 65.3 million <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a><a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.

### Payouts and Managing Bids
When a user successfully participates in a liquidation, the payout is in the form of the collateral itself, typically bLuna or bETH <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a><a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a><a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>. This will appear as "available assets to withdraw" <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>. The platform also shows the user's average discount received on those at-risk collateral assets <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a><a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

Users can cancel their bids at any time without a locking period <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a><a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a><a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.

### Moral Consideration
While participating in liquidations might seem to create a "moral conflict" by liquidating other DeFi users, Orca offers a beneficial aspect <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a><a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. By allowing users to bid at low percentage rates (e.g., 2-5%), Orca can mitigate the loss for the person being liquidated, as opposed to situations where "bots or whales" might aim for a 30% premium <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a><a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a><a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a><a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>.

## Kajira's Broader Vision

Kajira aims to build a suite of products that provide users access to previously unseen tools <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a><a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>.

### Beluga
Another product in Kajira's roadmap is Beluga <a class="yt-timestamp" data-t="11:12:00">[11:12:00]</a>. Beluga allows users to send any CW20 tokens (tokens on the Terra network) to multiple addresses simultaneously using a single transaction <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a><a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a><a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a><a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>. For example, sending to 11 different addresses cost $3.20 in gas, whereas 11 separate transactions would have cost $22 [[decentralized_exchanges_and_liquidity_protocols | UST]] <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a><a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a><a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a><a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a><a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>. This significantly negates gas fee impact for users moving money around <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a><a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.

### Kajira Token Metrics
The Kajira token is on the Terra network, with a total supply of 150 million <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a><a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a><a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>. The project valuation is currently 27 million [[decentralized_exchanges_and_liquidity_protocols | UST]], and they aimed to raise 3 million [[decentralized_exchanges_and_liquidity_protocols | UST]] from the StarTerra raise <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a><a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a><a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.