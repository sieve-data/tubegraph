---
title: Orca platforms process of automated bids and premiums
videoId: iyIKTuLqOMA
---

From: [[when-shift-happens]] <br/> 

Orca is the inaugural product from [[building_cryptocurrency_platforms_focused_on_user_needs | Kajira]], a platform aiming to empower retail crypto users to compete with whales and elites [00:00:52]. Its primary function is to facilitate automated bids on collateral liquidated from the Anchor Protocol [00:01:00].

## Understanding Anchor Protocol Liquidations

To grasp Orca's functionality, it's essential to understand how liquidations occur within the Anchor Protocol [00:01:14].

*   **Loan Mechanics**: Borrowers on Anchor Protocol offer non-stable assets as collateral to obtain [[Anchor_Protocol_Overview#UST_Stablecoin | UST]] loans [00:01:43]. The maximum loan amount is typically 60% of the collateral's value [00:02:10], with the loan itself being a stablecoin (UST) pegged to the US dollar [00:01:50].
*   **At-Risk Loans**: A loan becomes "at risk" if the value of the deposited collateral, or bonded asset, falls to a point where the loan amount exceeds a predefined threshold [00:03:57].
*   **The Role of Liquidators**:
    *   Liquidators repay the shortfall on the collateral to the lender (Anchor) on behalf of the borrower [00:02:21].
    *   Once a loan is successfully liquidated, Anchor receives the UST it loaned out, and the borrower retains the UST they borrowed [00:02:39].
    *   The collateral provided by the borrower then becomes the property of the liquidator [00:02:46].
    *   Liquidators are compensated for their service via a "premium," which is effectively a discount on the price of the non-stable assets used as collateral [00:02:48].

## Orca's Automated Bidding Process

Orca streamlines access to the liquidation process, making it simple to navigate even for everyday users [00:06:54].

### Premium-Based Bidding

On Orca, the discount offered by a liquidator (the premium) can range from 1% to 30% [00:02:57]. Users can place bids at any of these premium levels [00:03:01].

Orca operates on a tiered system where bids are satisfied based on their premium:
*   **Smallest Premiums First**: [[impact_of_bid_threshold_settings_on_yield_and_liquidation_outcomes | Liquidators accepting smaller premiums (lower discounts)]] are prioritized to access at-risk capital [00:03:05]. This means all bids at the lowest premium are utilized before moving to the next highest premium [00:08:06].
*   **Tiered Progression**: The system steadily moves upwards through the premium tiers until all collateral has been liquidated or there are no more bids [00:03:25]. This differs from previous systems where the fastest execution determined who received the liquidated capital [00:03:14].

### Placing and Managing Bids

[[user_interface_updates_for_bidding_on_aUST | Orca's intuitive user interface]] allows users to place bids by deciding:
1.  **Bid Amount**: There are no minimum or maximum bid amounts [00:07:16].
2.  **Premium Level**: Users select their desired discount rate [00:07:12].

For example, a user can place a 100 UST bid at a 5% premium [00:07:31]. Once submitted, a bid becomes active after a short period, such as 10 minutes [00:07:52]. The platform visually indicates where a user's bid is positioned within the premium tiers, often by highlighting it [00:08:26].

### Payouts and Assets

When a user's bid is successful in a liquidation, the payout is received in the liquidated collateral itself, typically bonded Luna (bLuna) or bonded Ethereum (bETH) [00:08:42]. These assets then become available for withdrawal [00:08:52]. The platform also displays the user's average discount received on these collateral assets [00:09:00].

### Bid Cancellation

Users can cancel their bids at any time without a locking period, allowing them to withdraw their funds from the platform [00:09:08].

### Platform Metrics

The Orca platform displays key metrics, including:
*   Total UST pool value at each premium level [00:05:04].
*   Total locked collateral value in Anchor Protocol (e.g., 3.5 billion) [00:05:23].
*   Total pool value in Orca (e.g., 26.4 million) [00:05:31].
*   Total locked collateral in specific assets like bLuna (e.g., 65.3 million) [00:05:35].

### Potential Benefits Beyond Profit

While liquidations might seem morally conflicting, Orca can offer a more beneficial outcome for the liquidated party. By allowing bids at lower percentage rates (e.g., 2-5%), Orca can reduce the amount of collateral a liquidated person loses compared to scenarios where bids run all the way to a 30% premium, which is often targeted by bots and whales [00:06:09].

## Kajira's Broader Vision

Kajira aims to build a suite of products that provide users with access to previously inaccessible tools [00:10:33]. Beyond Orca, another product in development is Beluga [00:11:12].

### Beluga

Beluga is designed to enable users to send any CW20 tokens (Terra network tokens) to multiple addresses simultaneously using a single transaction [00:11:17]. This significantly reduces gas fees; for instance, sending to 11 different addresses cost $3.20 via Beluga, compared to an estimated $22 for 11 separate transactions [00:11:30].