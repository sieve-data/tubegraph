---
title: Updating payment progress in notion
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker can be used to track debt payments on time and help users become debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This tracker includes sections that update payment progress, such as a summary, a debt overview, and progressive payment details <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Tracking Payment Progress

The Notion debt tracker provides several views to monitor payment progress:
*   **Summary Section** This section shows the total loan amount, total amount repaid, total interest repaid, and the repayment in percentage for all combined debts <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview** This section details progress for each debt type, including student loan, [[notion_credit_card_payment_overview | credit card]], car loan, personal loan, home loan, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each debt, it displays the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated date of being debt-free <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a> <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
*   **Debt Progressive Payments** This section outlines progressive due payments, showing the month of payment, the amount of repayment, and the status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a> <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

## How to Update Payment Status

Payment progress is updated interactively within the tracker:
*   **Updating Status** To update the status, simply click the checkbox next to a payment <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This changes the status to "paid" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Entering Payment Amount** Users can click and enter the payment amount, then update the payment status to reflect their progress <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Reflection of Updates

When an amount is marked as paid, the changes are automatically reflected across the Notion debt tracker:
*   **Debt Overview** The "amount repaid," "interest repaid," and "repayment in percentage" values update in the debt overview section under the respective debt categories <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Loan Details Database** The [[tracking_debt_payoff_progress_in_notion | Notion debt tracker]]'s `loan details` database contains a checkbox to reflect the payment status as paid or not paid <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Clicking this checkbox updates the payment status <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Calculations** The total repayment, interest paid, and principal amount paid against each debt are calculated by formula when the payment checkbox is ticked <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a> <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. These amounts are also summed up at the bottom of the section <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Databases Involved in Progress Tracking

Building this minimalistic Notion debt tracker requires five databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

1.  **Debt Database**
    *   Lists different types of debt <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
    *   Properties include loan amount, interest rate per annum, minimum monthly payment, additional repayment amount, initial repayment date, debt-free period, expected debt-free date, and net loan outstanding amount <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   The `net loan outstanding amount` serves as the opening balance for the `loan details` database <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

2.  **Loan Details Database**
    *   This database holds details for each repayment <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
    *   Properties include installment number, date of payment, category of loan, opening balance, payment amount, interest calculation, principal value, closing balance, a checkbox for payment status, and the amount paid against total amount, interest, and principal <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
    *   The opening balance for the first month is the net loan outstanding from the `debt` database; subsequent months use the previous month's closing balance <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   The payment amount for the first installment includes minimum and additional payments, while subsequent payments are the minimum amount <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

3.  **Debt Overview Database**
    *   Provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
    *   Properties include loan amount (rolled up from `loan details` database), total amount repaid, total principal repaid, and total interest repaid (all rolled up from `loan details` database) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
    *   Calculates outstanding amount (loan amount less principal repaid) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a> and repayment in percentage (principal repaid to total loan amount) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

4.  **Summary of Debt Database**
    *   Calculates the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the debt-free date for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
    *   Figures for these properties are pulled as roll-ups from the `debt overview` database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

5.  **Total Debt Section**
    *   Reflects the total loan amount, total amount repaid, total interest repaid, and repayment in percentage for all debts combined <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
    *   Values are rolled up from the `debt overview` database using formulas <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

> [!INFO] Dashboard Linkage
> The primary dashboard's summary section is linked to the `total debt` database <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. The `debt overview` section is linked to the `summary of debt` database <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. The `debt progress` section is linked to the `loan details` database <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.