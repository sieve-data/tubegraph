---
title: Building a Minimalistic Finance Template in Notion
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

The Accountant Guy introduces a Notion debt tracker designed to help users track debt payments on time and achieve debt-free status <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This minimalistic [[using_notion_for_financial_management | Notion]] finance template includes several key sections to monitor progress.

## Key Sections of the Debt Tracker

The debt tracker features several sections for comprehensive debt management:

### Summary Section
This section provides an overview of all combined debts, displaying:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

### Debt Overview
This section categorizes debts and provides specific details for each:
*   **Categories**: Student loan, credit card, car loan, personal loan, home loan, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Details per category**: Total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Debt Progressive Payments
This section outlines future due payments progressively <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It shows:
*   Month of payment <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   Amount of repayment <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
*   Status of payment (paid or not paid) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

Updating progress is straightforward: clicking a checkbox updates the status to "paid" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Entering the payment amount and updating the status reflects the progress in the debt overview section under "amount repaid," "interest repaid," and "repayment in percentage" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Building the Notion Debt Tracker

To construct this minimalistic [[creating_a_minimalistic_budget_planner_using_notion | Notion]] debt tracker, five interconnected databases are required <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

1.  Loan Details Database <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
2.  Debt Database <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
3.  Debt Overview Database <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
4.  Summary of Debt Database <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>
5.  Total Debt Section Database <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>

### 1. Debt Database

This is the foundational database where all types of debts are listed <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

#### Properties:
*   **Name**: Default property listing debt types (e.g., student loan, credit card, car loan, personal loan, home loan, other loan) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Loan Amount**: Total amount of the loan (number property, US dollars) <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Interest Rate**: Per annum interest rate for each debt (number property, US dollars, percent format) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Minimum Payment**: Minimum monthly payment amount (number property, US dollars) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Additional Repayment**: Any additional amount paid during the first installment, such as a down payment (number property, US dollars) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Initial Repayment Date**: The first installment date when the debt is repaid (date property) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Interest Rate Per Month**: Calculated by dividing the annual interest rate by 12 (formula property) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Debt-Free Period**: Calculates the debt-free period in months (formula property) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt-Free By**: Estimates the debt-free date by adding the Debt-Free Period to the Initial Repayment Date (formula property) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Net Loan Outstanding Amount**: Calculates the net debt payable before the first installment, serving as the opening balance for the Loan Details database (formula property: Loan Amount - Additional Repayment) <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### 2. Loan Details Database

This database records the repayment details for each debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

#### Properties:
*   **Installment Number**: Specifies the number of installments paid against the debt <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment**: The date of repayment for each installment (date property) <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan**: Related to the Debt Overview database, specifying one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance**: The balance of the debt before the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    *   For the first month, it's the `Net Loan Outstanding` from the Debt database <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   For subsequent months, it's the `Closing Balance` of the previous month <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   **Payment Amount**: The minimum amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
    *   For the first installment, it includes the minimum amount and any additional payment <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   For subsequent months, it's just the minimum amount <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Interest Calculation**: The interest amount paid per installment (formula: `Opening Balance * Interest Rate / 12`) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value**: The principal amount paid (`Payment Amount - Interest Amount`) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: The remaining balance after payment (`Opening Balance - Principal Amount`) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status Checkbox**: Reflects whether the payment is "paid" or "not paid" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Amount Paid against Total/Interest/Principal**: Calculated using a formula that considers if the `Payment Status Checkbox` is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
    *   These amounts are summed up at the bottom of the database <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database

This database provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

#### Properties:
*   **Loan Amount**: Rolled up from the `Loan Details` database and derived using a formula <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid**: Rolled up from the `Loan Details` database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid**: Rolled up from the `Loan Details` database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid**: Rolled up from the `Loan Details` database <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount**: Calculated by subtracting `Principal Repaid` from `Loan Amount` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: Calculates `Principal Repaid` as a percentage of `Total Loan Amount` <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database

This database calculates specific totals for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

#### Properties:
*   Total loan amount <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>
*   Date by which the debt will be free <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

All figures for these properties are pulled in as roll-up values from the `Debt Overview` database <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### 5. Total Debt Database

This database reflects the combined values for all debts <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

#### Properties:
*   Total loan amount <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>

Similar to the `Summary of Debt` database, values are rolled up from the `Debt Overview` database and calculated using formulas <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

## Primary Dashboard

The primary dashboard integrates these databases to provide a comprehensive view of finances.

*   **Summary Section**: Displays the total loan amount, total amount repaid, interest repaid, and repayment in percentage for all combined debts, linked to the `Total Debt` database <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section**: Shows details for each debt, including loan amount, total repaid, interest repaid, repayment percentage, and debt-free date, linked to the `Summary of Debt` database <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section**: Displays progressive repayments with corresponding dates and amounts, linked to the `Loan Details` database <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

This [[using_notion_for_finance_management | Notion]] debt tracker provides a structured approach to managing and tracking debt payments, aiding users in becoming debt-free <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. A template is available for download <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.