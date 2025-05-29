---
title: Managing debt payments and statuses
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker can assist in [[tracking debt payments and budgets | tracking debt payments]] on time to help achieve debt-free status <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This tracker offers a comprehensive overview and management system for various debt categories <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Key Features of the Notion Debt Tracker

The Notion debt tracker includes several key sections to help users manage their debt:

*   **Summary Section**: Displays the total loan amount, total amount repaid, total interest repaid, and repayment in percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   [[Overview and management of debt categories | Debt Overview]]: Categorizes debt into types such as student loan, credit card, car loan, personal loan, home loan, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each category, it shows the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the projected debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   [[Tracking progress of debt payoff | Debt Progressive Payments]]: Outlines future due payments, detailing the month of payment, repayment amount, and payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Checking a box updates the payment status and reflects the progress in the debt overview section, showing updates to the amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Building the Notion Debt Tracker

Building this minimalistic Notion debt tracker requires five interconnected databases <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>:

1.  Loan Details <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
2.  Debt <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
3.  Debt Overdue <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
4.  Summary of Debt <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>
5.  Total Debt <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>

### 1. Debt Database

The Debt database lists all types of debt <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>, including student loan, credit card, car loan, personal loan, home loan, and other loans <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

Properties within this database include:
*   **Name**: Default property specifying the type of debt <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Loan Amount**: Total amount of the loan <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Interest Rate**: Annual interest rate for each debt, specified as a percentage <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Minimum Payment**: Minimum monthly payment required <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Additional Repayment**: Amount paid during the first installment, such as a down payment <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Initial Repayment Date**: Date of the first installment payment <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Interest Rate per Month**: A formula property calculated by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt Free Period**: A formula that calculates the period in months to become debt-free <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt Free By**: A formula property that adds the Debt Free Period to the Initial Repayment Date to estimate the debt-free date <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Net Loan Outstanding Amount**: A formula property calculating the net debt payable before the first installment, derived by deducting additional payments from the loan amount <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This acts as the opening balance for the Loan Details database <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### 2. Loan Details Database

This database holds the installment-specific details of debt repayment <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

Properties within this database include:
*   **Installment Number**: Specifies the sequence of payments made <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment of Installment**: The specific date when an installment is repaid <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan**: Relates to the debt overview database, specifying one of the six debt categories being repaid <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance**: The debt amount outstanding before the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. For the first month, this is the Net Loan Outstanding from the Debt database; for subsequent months, it is the closing balance of the previous month <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Payment Amount**: The minimum monthly payment <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, it includes the minimum amount and any additional payment <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Interest Calculation**: A formula property specifying the interest amount paid per installment <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>, calculated as opening balance multiplied by the monthly interest rate <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Principal Value**: A formula property calculated as the payment amount minus the interest amount paid <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: A formula property equal to the opening balance minus the principal amount for each month <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status**: A checkbox that reflects whether the payment is paid or not paid <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Clicking it updates the status <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   [[Tracking transactions and invoice statuses | Total Repayment]]: A formula property that calculates the amount paid against the total amount, interest, and principal, contingent on the payment status checkbox being ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. The total amounts repaid against total, interest, and principal are also summed at the bottom of the database <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database

This database provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

Properties within this database include:
*   **Loan Amount**: Rolled up from the Loan Details database, derived using a formula <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount**: A formula property calculated by deducting the principal repaid from the loan amount <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: A formula property showing the principal repaid as a percentage of the total loan amount <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database

This database calculates summarized figures for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

Properties within this database include:
*   **Total Loan Amount**: Pulled in as a roll-up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Total Amount Repaid**: Pulled in as a roll-up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Total Interest Repaid**: Pulled in as a roll-up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   **Repayment in Percentage**: Pulled in as a roll-up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Debt-Free Date**: Pulled in as a roll-up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### 5. Total Debt Database

This database reflects the combined total values for all debts <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

Properties within this database include:
*   **Total Loan Amount**: Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Total Amount Repaid**: Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   **Total Interest Repaid**: Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   **Repayment and Percentage**: Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

## Primary Dashboard

The primary dashboard of the Notion debt tracker provides a consolidated view of debt progress:

*   **Summary Section**: Displays the total loan amount, total amount repaid, total interest repaid, and repayment in percentage for all combined debts, linked to the Total Debt database <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   [[Debt and liability tracking | Debt Overview Section]]: Shows individual debt categories with their total loan amount, total amount repaid, interest repaid, repayment percentage, and debt-free date, linked to the Summary of Debt database <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   [[Debt payment tracking and analysis | Debt Progress Section]]: Presents progressive repayments of debts with corresponding dates and amounts, linked to the Loan Details database <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

This comprehensive Notion setup facilitates efficient [[repayment schedules and customization | tracking of repayment schedules]] and provides a clear path towards becoming debt-free <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.