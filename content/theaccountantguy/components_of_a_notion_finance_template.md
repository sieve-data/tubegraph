---
title: Components of a Notion finance template
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker is a financial tool designed to help users track their debt payments over time, with the ultimate goal of becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This template incorporates various sections and underlying databases to provide a comprehensive view of one's financial obligations.

## Core Sections of the Template

The main dashboard of the Notion debt tracker typically includes three primary sections:

### Summary Section
This section offers an aggregated view of all combined debts, displaying key financial metrics:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

### Debt Overview Section
This section categorizes debts and provides specific details for each type. Common debt categories include:
*   Student loan <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
*   Credit card <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Car loan <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
*   Personal loan <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   Home loan <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   Other loan <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

For each debt category, the overview displays:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
*   The estimated date by which the debt will be paid off <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>

### Debt Progressive Payments Section
This section outlines upcoming due payments and helps track the status of individual installments <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. It includes:
*   Month of payment <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   Amount of repayment <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
*   Status of payment (paid or not paid) <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>

A checkbox feature allows users to easily update the payment status. Once an amount is marked as paid, the relevant metrics in the debt overview section are automatically updated to reflect the repayment <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Underlying Databases

To power the Notion debt tracker, five interconnected databases are utilized <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>:

### 1. Debt Database
This database holds the comprehensive details of all debts <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. It contains properties such as:
*   **Name**: Specifies the type of debt (e.g., student loan, car loan) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Loan Amount**: The total amount of the loan <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Interest Rate**: The annual interest rate for each debt, specified as a percentage <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. The monthly interest rate (I value) is derived by dividing this by 12 <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Minimum Payment**: The minimum monthly payment required <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Additional Repayment**: Any extra amount paid during the first installment, like a down payment <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Initial Repayment Date**: The date of the first installment payment <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Debt Free Period**: A formula property that calculates the estimated number of months to become debt-free <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt Free By**: An estimated debt-free date, calculated by adding the Debt Free Period to the Initial Repayment Date <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount**: The opening balance of the debt before the first installment, derived by deducting any additional payment from the loan amount <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### 2. Loan Details Database
This database tracks the specifics of each repayment installment <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Its properties include:
*   **Installment Number**: Tracks the sequential number of payments <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment**: The date on which each installment is paid <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   **Category of Loan**: Links to the specific debt type in the Debt Database <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Opening Balance**: The outstanding debt before the current repayment. For the first month, this is the net loan outstanding from the Debt Database; for subsequent months, it's the previous month's closing balance <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Payment Amount**: The amount paid each month, including minimum payment and any additional repayment for the first installment <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Interest Calculation**: A formula that calculates the interest amount paid for each installment (Opening Balance \* (Interest Rate / 12)) <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Principal Value**: The principal amount paid, calculated as Payment Amount - Interest Amount <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: The remaining debt after the current payment (Opening Balance - Principal Amount) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status Checkbox**: A checkbox to mark whether a payment has been made, updating the status as "paid" or "not paid" <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Total Repayment**: A formula that considers the payment status checkbox to calculate the total amount repaid, interest paid, and principal paid <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### 3. Debt Overview Database
This database provides an overview of each debt type <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. It uses roll-up properties from the Loan Details Database:
*   **Loan Amount**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid**: A roll-up value <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid**: A roll-up value <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid**: A roll-up value <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount**: Calculated by subtracting Total Principal Repaid from Loan Amount <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: The percentage of principal repaid relative to the total loan amount <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database
This database calculates and displays the aggregated figures for each type of debt <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. It pulls values as roll-ups from the Debt Overview Database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>:
*   Total loan amount <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>
*   Debt-free date <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

### 5. Total Debt Section (Database)
This final database consolidates the total values across all debts <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Similar to the Summary of Debt Database, it uses roll-ups from the Debt Overview Database to calculate:
*   Total loan amount <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>
*   Total repayment in percentage for all combined debts <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>

This structured approach, using interconnected databases and rollup properties, enables [[Customizing Notion templates for personal finance management | Notion]] to effectively track and manage debt payments, providing clarity on financial progress and helping users achieve debt freedom. For those interested in [[overview_of_notion_finance_templates | Notion finance templates overview]] or [[notion_budget_and_expenses_template | budget tracking]], this debt tracker is a specialized component within a broader financial management system.