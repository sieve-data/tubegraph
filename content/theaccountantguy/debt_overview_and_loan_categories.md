---
title: Debt Overview and Loan Categories
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker can be created to help monitor debt payments and progress towards becoming debt-free <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This tracker provides a summary section detailing the total loan amount, total amount repaid, total interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Debt Categories

The tracker organizes debt under various categories, including:
*   Student loan <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>
*   Credit card <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Car loan <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
*   Personal loan <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   Home loan <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   Other loan <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

For each debt category, the tracker displays the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated date of debt freedom <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Components of the Debt Tracker

To build this [[using_notion_for_debt_tracking | Notion debt tracker]], five interlinked databases are required <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

### 1. Debt Database
This database holds comprehensive information for all debts, including:
*   **Loan Amount**: The total sum of the loan <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Interest Rate**: The annual interest rate for each debt <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Minimum Payment**: The minimum monthly payment required <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Additional Repayment**: Any extra amount paid during the first installment, such as a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Initial Repayment Date**: The date when the first installment was paid <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Debt Free Period**: Calculates the estimated number of months to become debt-free <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Expected Debt Free By**: An estimated date when the debt will be fully repaid, derived by adding the debt-free period to the initial repayment date <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount**: The opening balance of the debt before the first installment, calculated by deducting the additional payment from the loan amount <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

This database specifically lists six types of debts: student loan, credit card, car loan, personal loan, home loan, and other loan <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. The interest rate is typically calculated per annum and displayed in a percentage format <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. The interest rate per month is derived by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### 2. Loan Details Database
This database records individual repayment details for each debt <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. It includes:
*   **Installment Number**: Tracks the number of payments made <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment**: The specific date of each installment payment <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan**: Links to one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance**: For the first month, it's the net loan outstanding from the Debt Database; for subsequent months, it's the closing balance of the previous month <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Payment Amount**: The minimum monthly payment, potentially including additional payments for the first installment <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Interest Calculation**: The interest portion of each installment (opening balance multiplied by the monthly interest rate) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value**: The principal portion of the payment (payment amount minus interest amount) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: The remaining debt after the principal payment (opening balance minus principal amount) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status**: A checkbox to mark payments as paid or not paid <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Amount Paid**: Tracks the total, interest, and principal amounts paid, updated when the payment status is checked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### 3. Debt Overview Database
This database provides a quick overview of each debt, detailing <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>:
*   Loan amount <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
*   Principal repaid <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>
*   Interest repaid <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>
*   Outstanding amount <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
*   Debt-free date <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>

These values are rolled up from the [[managing_and_editing_loan_details | Loan Details]] database <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. The outstanding loan amount is calculated by subtracting the principal repaid from the total loan amount <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Repayment in percentage is the principal repaid divided by the total loan amount <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database
This database calculates the total loan amount, total amount repaid, total interest repaid, repayment percentage, and the debt-free date for each individual debt category <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Figures for these properties are pulled as roll-up values from the [[debt_overview_and_classification | Debt Overview]] database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### 5. Total Debt Section
This final database presents a consolidated view of all debts combined, showing the total loan amount, total amount repaid, total interest repaid, and the overall repayment percentage <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Values are rolled up from the [[debt_overview_and_classification | Debt Overview]] database to calculate these combined totals <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

## Tracker Dashboard
The primary dashboard of the [[using_notion_for_debt_tracking | Notion debt tracker]] features three main sections:
*   **Summary Section**: Displays overall totals for loan amount, amount repaid, interest repaid, and repayment percentage across all debts, linked to the [[debt_overview_and_classification | Total Debt]] database <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section**: Presents individual debt categories with their respective loan amounts, amounts repaid, interest repaid, repayment percentages, and debt-free dates, linked to the [[debt_overview_and_classification | Summary of Debt]] database <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section**: Shows progressive debt repayments, including payment dates and amounts, linked to the [[managing_and_editing_loan_details | Loan Details]] database <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Users can click a checkbox to update payment status, which in turn updates the debt overview section with the amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.