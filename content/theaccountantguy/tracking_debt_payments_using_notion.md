---
title: Tracking debt payments using Notion
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

This article details how to [[creating_a_notion_debt_tracker | create a Notion debt tracker]] to effectively [[using_notion_for_debt_management_and_tracking_debt_payments | track debt payments]] on time and help achieve debt freedom <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Overview of the Notion Debt Tracker

The [[creating_a_notion_debt_tracker | Notion debt tracker]] includes several key sections:
*   **Summary Section** Shows the total loan amount, total amount repaid, total interest repaid, and repayment in percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Debt Overview** Features categories like student loan, credit card, car loan, personal loan, home loan, and other loan types <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Under each category, it displays the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated date of being debt-free <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Debt Progressive Payments** Outlines progressive due payments for the time ahead, showing the month of payment, repayment amount, and payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Clicking a checkbox updates the payment status <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. When an amount is paid, it updates the "debt overview" section for the respective debt's amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Building the Notion Debt Tracker

To build this minimalistic [[creating_a_notion_debt_tracker | Notion debt tracker]], five databases are required <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:
1.  Loan Details Database <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
2.  Debt Database <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
3.  Debt Overview Database <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
4.  Summary of Debt Database <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>
5.  Total Debt Database <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>

### 1. Debt Database

This database lists different types of debt, such as student loan, credit card, car loan, personal loan, home loan, and other loan <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

Key properties include:
*   **Name:** The default property for specifying debt types <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Loan Amount:** The total amount of the loan, a number property in US dollars <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Interest Rate:** The per annum interest rate for each debt, a number property in percent format <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Minimum Payment:** The minimum monthly payment to be repaid <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Additional Repayment:** Any additional amount paid during the first installment, like a down payment <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Initial Repayment Date:** The first installment date when the debt is repaid <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Interest Rate Per Month:** Calculated by dividing the interest rate by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt Free Period:** A formula that calculates the debt-free period in months <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt Free By:** An estimated debt-free date calculated by adding the "Debt Free Period" to the "Initial Repayment Date" <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Net Loan Outstanding Amount:** The net debt payable before the first installment date, serving as the opening balance for the Loan Details database <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. It's derived by deducting the "Additional Payment" from the "Loan Amount" <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### 2. Loan Details Database

This database stores details related to loan repayments, helping track the outstanding balance <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

Key properties include:
*   **Installment Number:** Specifies the number of installments paid <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Date of Payment of Installment:** The date of debt repayment per installment, a date property <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan:** Relates to the "Debt Overview Database," specifying one of six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance:** The balance prior to repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. The first month's payment amount is the "Net Loan Outstanding" from the Debt Database, and subsequent months use the previous month's closing balance <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Payment Amount:** The minimum amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, it includes the minimum amount and any additional payment; for subsequent months, it's the minimum amount <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Interest Calculation:** A formula specifying the interest amount paid per installment, calculated as "Opening Balance" multiplied by ("Interest Rate" divided by 12) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value:** Calculated as "Payment Amount" less "Interest Amount" <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Closing Balance:** Equal to "Opening Balance" less "Principal Amount" for each month <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status:** A checkbox reflecting if payment is paid or not paid <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Amount Paid:** The total amount paid, interest paid, and principal paid against each debt, calculated by a formula when the checkbox is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. These amounts are also summed at the bottom <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database

This database provides a quick overview of all debt types <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

Key properties include:
*   **Loan Amount:** Rolled up from the "Loan Details Database" <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid:** Rolled up from the "Loan Details Database" <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid:** Rolled up from the "Loan Details Database" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid:** Rolled up from the "Loan Details Database" <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount:** Calculated by deducting the "Principal Repaid" from the "Loan Amount" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage:** The percentage of "Principal Repaid" to the "Total Loan Amount" <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database

This database calculates and displays summary figures for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

Key properties include:
*   **Total Loan Amount** <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>
*   **Total Amount Repaid** <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   **Total Interest Repaid** <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   **Repayment in Percentage** <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>
*   **Debt Free Date** <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

All these figures are pulled in as roll-up values from the "Debt Overview Database" <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### 5. Total Debt Database

This database reflects combined total values for all debts <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

Key properties include:
*   **Total Loan Amount** <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
*   **Total Amount Repaid** <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
*   **Total Interest Repaid** <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>
*   **Repayment in Percentage** <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>

These values are rolled up from the "Debt Overview Database" <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

## Primary Dashboard

The primary dashboard integrates information from the databases to provide a comprehensive view of debt management.

*   **Summary Section:** Shows the total loan amount, total amount repaid, interest repaid, and repayment in percentage for all debts combined, linked to the "Total Debt Database" <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section:** Displays details for each debt, including total loan amount, total amount repaid, interest repaid, repayment percentage, and the debt-free date, linked to the "Summary of Debt Database" <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section:** Shows progressive repayments with corresponding dates and amounts, linked to individual loans from the "Loan Details Database" <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

This setup allows for a minimalistic yet effective [[how_to_use_notion_for_tracking_debt_payments | Notion-based debt tracker]] to monitor and manage debt repayment progress <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.