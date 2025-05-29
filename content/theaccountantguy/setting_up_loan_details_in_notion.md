---
title: Setting up loan details in Notion
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

The loan details database in Notion is one of five databases required to build a minimalistic [[debt_payment_tracking_using_notion | Notion debt tracker]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This database is used to fill in the specific details of debt repayment for each loan <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Database Properties

The following properties are set up within the loan details database:

*   **Installment Number** <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>
    *   Specifies the number of installments paid against a debt <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Date of Payment of Installment** <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>
    *   Specifies the date when the installment is repaid <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
    *   This property has a date format <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Category of Loan** <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>
    *   Relates to the [[debt_payment_tracking_using_notion | debt overview]] database <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
    *   Specifies one of six predefined categories of debt being repaid <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **Opening Balance** <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>
    *   Represents the outstanding debt balance prior to the current repayment <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   For the first month's payment, this value is derived from the net loan outstanding from the [[building_a_debt_database_in_notion | debt database]] <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   For subsequent months, the closing balance of the previous month is copied to the current month's opening balance <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   **Payment Amount** <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>
    *   Represents the minimum amount paid each month <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   For the first installment, it includes the minimum amount and any additional payment made <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   For subsequent months, it is equal to the minimum amount due <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Interest Calculation** <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>
    *   A formula property that calculates the interest amount paid each installment <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
    *   This is determined by multiplying the opening balance by the interest rate and then dividing by 12 <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Principal Value** <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>
    *   A formula property calculated by subtracting the interest amount from the payment amount <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance** <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>
    *   A formula property calculated by subtracting the principal amount from the opening balance for each month <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Payment Status Checkbox** <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>
    *   Reflects whether the payment status is "paid" or "not paid" <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   Clicking this checkbox updates the payment status <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Amount Paid** <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>
    *   Calculates the total amount, interest, and principal amount paid against each debt <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
    *   This formula considers when an amount is paid and its corresponding checkbox is ticked <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   The total amounts repaid against total, interest, and principal are summed at the bottom of the database <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.