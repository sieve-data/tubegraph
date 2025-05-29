---
title: Creating a notion debt tracker
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

This article outlines how to create a Notion [[debt_tracker | debt tracker]] designed to help you monitor debt payments and work towards becoming debt-free <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Tracker Overview

The Notion [[debt_tracker | debt tracker]] features several key sections:
*   A [[summary_section_in_notion_debt_tracker | summary section]] displaying the total loan amount, total amount repaid, total interest repaid, and repayment in percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   A [[overview_of_debt_payment_tracker | Debt Overview]] section detailing specific loan types such as student loans, credit cards, car loans, personal loans, home loans, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Each type includes its total loan amount, total amount repaid, total interest repaid, repayment percentage, and the estimated debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   A Debt Progressive Payments section that outlines upcoming due payments by month, repayment amount, and payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Tracking Payments
To [[tracking_debt_payoff_progress_in_notion | track debt payoff progress]], once an amount is repaid, checking a checkbox updates the status to "paid" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This update reflects automatically in the [[overview_of_debt_payment_tracker | Debt Overview]] section for the respective debt, updating the amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Building the Notion Debt Tracker

[[building_databases_for_debt_tracking | Building this Notion debt tracker]] requires five interconnected databases <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>:

### 1. Debt Database
This database lists all different types of debt <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a> and includes properties such as:
*   **Name**: Default property specifying the type of debt (e.g., student loan, credit card, car loan, personal loan, home loan, other loan) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Loan Amount**: Total amount of the loan <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Interest Rate**: Per annum interest rate for each debt, formatted as a percentage <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Minimum Payment**: The minimum monthly payment required <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Additional Repayment Amount**: Any extra payment made during the first installment, like a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Initial Repayment Date**: The date when the first installment was paid <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Interest Rate Per Month**: A formula property that calculates the monthly interest rate by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt Free Period**: A formula property that calculates the number of months until the debt is fully repaid <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt Free By**: A formula property that estimates the debt-free date by adding the Debt Free Period to the Initial Repayment Date <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Net Loan Outstanding Amount**: A formula property calculating the outstanding loan amount before the first installment, derived by deducting the additional payment from the loan amount <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This acts as the opening balance for the Loan Details database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### 2. Loan Details Database
This database tracks individual installment payments against each debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>:
*   **Installment Number**: Specifies the sequential number of the payment <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment of Installment**: The specific date of each payment <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan**: Links to the [[overview_of_debt_payment_tracker | Debt Overview]] database, specifying which type of loan is being repaid <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance**: The outstanding debt before the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. For the first month, it's the Net Loan Outstanding from the Debt database; for subsequent months, it's the previous month's closing balance <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Payment Amount**: The amount paid each month. For the first installment, it's the minimum amount plus any additional payment; thereafter, it's the minimum amount <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Interest Calculation**: A formula that calculates the interest portion of the payment (Opening Balance × monthly interest rate) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value**: A formula that calculates the principal portion of the payment (Payment Amount - Interest Amount) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: A formula that calculates the remaining debt (Opening Balance - Principal Amount) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status Checkbox**: A checkbox to mark payments as "paid" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment**: A formula that calculates the amount repaid against the total, interest, and principal, contingent on the payment status checkbox being ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. The sum of these amounts is also reflected at the bottom of the database <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database
This database provides a single-glance overview of each debt type <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>:
*   **Loan Amount**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount**: Calculated by deducting the Principal Repaid from the Loan Amount <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: Calculates the percentage of principal repaid against the total loan amount <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database
This database aggregates key figures for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>:
*   **Total Loan Amount**: Rolled up from the [[overview_of_debt_payment_tracker | Debt Overview]] database <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Total Amount Repaid**: Rolled up from the [[overview_of_debt_payment_tracker | Debt Overview]] database <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Total Interest Repaid**: Rolled up from the [[overview_of_debt_payment_tracker | Debt Overview]] database <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   **Repayment in Percentage**: Rolled up from the [[overview_of_debt_payment_tracker | Debt Overview]] database <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Debt Free Date**: Rolled up from the [[overview_of_debt_payment_tracker | Debt Overview]] database <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### 5. Total Debt Database
This database provides a grand total for all debts combined <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>:
*   **Total Loan Amount**: Rolled up from the [[overview_of_debt_payment_tracker | Debt Overview]] database <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Total Amount Repaid**: Rolled up from the [[overview_of_debt_payment_tracker | Debt Overview]] database <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Total Interest Repaid**: Rolled up from the [[overview_of_debt_payment_tracker | Debt Overview]] database <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   **Repayment in Percentage**: Rolled up from the [[overview_of_debt_payment_tracker | Debt Overview]] database <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

## Primary Dashboard
Once all databases are built, the primary dashboard integrates their information for an at-a-glance view <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>:

*   **Summary Section**: Displays the total loan amount, total amount repaid, total interest repaid, and repayment percentage for all combined debts, linked to the Total Debt database <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This corresponds to the [[summary_section_in_notion_debt_tracker | summary section]] described earlier.
*   **[[overview_of_debt_payment_tracker | Debt Overview]] Section**: Shows details for each debt, including loan amount, amount repaid, interest repaid, repayment percentage, and debt-free date, linked to the Summary of Debt database <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section**: Shows progressive repayments with corresponding dates and amounts, linked to individual loans from the Loan Details database <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. This section aids in [[tracking_debt_payoff_progress_in_notion | tracking debt payoff progress]].