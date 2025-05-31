---
title: Kujiras objective in the crypto market
videoId: iyIKTuLqOMA
---

From: [[when-shift-happens]] <br/> 

Kujira aims to empower retail crypto users to compete directly with "whales and elites" <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. The project's broader goal is to build a [[kujiras_suite_of_products_and_future_offerings | suite of products]] that provide users access to previously uncommon tools <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

## Orca: The First Product

Kujira's initial product is Orca, a platform designed for automated bids on collateral liquidated from Anchor Protocol <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This platform seeks to allow individual users to "beat the bots at their own game" <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a> in a domain traditionally dominated by large players or automated systems <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Understanding Anchor Protocol Liquidations

To understand Orca, it is necessary to grasp how Anchor Protocol handles liquidations <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

Anchor Protocol enables users to put the value of their assets to work without selling them by offering them as collateral for a loan <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Anchor lends out UST, a stablecoin pegged to the US dollar <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>, <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Borrowers reduce the risk of lending by providing collateral <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>, <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Loans are typically over-collateralized, allowing borrowers to withdraw up to 60% of the collateral's value <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

**Liquidation Process:**
When the value of the collateral falls to a point where the loan exceeds a certain threshold, it is deemed "at-risk" <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>, <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Repayment:** Liquidators repay the collateral shortfall to the lender (Anchor) on behalf of the borrower <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. The loan amount is measured in UST <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Collateral Transfer:** Once a loan is successfully liquidated, Anchor receives its loaned UST, and the borrower forfeits their collateral <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>, <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The forfeited collateral becomes the property of the liquidator <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Liquidator Compensation:** Liquidators are paid for their service through a "premium," which is effectively a discount on the price of the non-stable assets used as collateral <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. On Orca, this discount can range from 1% to 30% <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>, <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

**Bid Priority:**
Previously, liquidations were first-come, first-served <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. However, market forces now dictate that liquidators accepting smaller premiums (lower discounts) are given first access to at-risk capital <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>, <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Bids at lower premiums are filled first, and if more collateral needs to be liquidated, the process moves up to the next highest premium tier until all collateral is distributed <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Orca User Experience

Orca simplifies the liquidation process with an intuitive and visually appealing user interface <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>, <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Users don't execute liquidations directly; Orca handles that <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

**Key Decisions for Users:**
1.  **Bid Amount:** Users choose how much UST they want to bid, with no minimum or maximum limits <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>, <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
2.  **Premium Rate:** Users select the desired premium (discount) rate for their bid, ranging from 0% to 30% <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   Bidding at lower percentage rates (e.g., 2-5%) is encouraged, as it results in less loss for the person being liquidated compared to bids at the maximum 30% premium <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>, <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

**After Placing a Bid:**
*   Bids become active after a short period (e.g., 10 minutes) <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>, <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Once a bid participates in a liquidation, the payout is received in the collateral asset (e.g., bLUNA or bETH) <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>, <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   Users can view their average discount received on liquidated assets <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   Bids can be canceled at any time, with funds immediately returned, as there is no locking period <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>, <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## [[kujiras_suite_of_products_and_future_offerings | Kujira's Suite of Products]] and [[tokenomics_and_roadmap_of_the_kujira_project | Future Offerings]]

Beyond Orca, Kujira plans to expand its product line:

### Beluga

Beluga is another product in development, designed to allow users to send any CW20 tokens (Terra network tokens) to multiple addresses simultaneously in a single transaction <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>, <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>, <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This functionality aims to significantly reduce gas fees; for example, sending tokens to 11 different addresses cost $3.20 using Beluga, compared to an estimated $22 for 11 separate transactions <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>, <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>, <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. This feature is intended to negate a large portion of the gas fee impact for users who frequently move funds <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

### Tokenomics Overview

The Kujira token will be on the Terra network, with a total supply of 150 million <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>, <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. The project's current valuation is 27 million UST <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>, <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>, with an aim to raise 3 million UST from its initial DEX offering (IDO) on StarTerra <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.