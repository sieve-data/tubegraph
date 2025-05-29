---
title: Components of a Notion debt tracker
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A [[creating_a_notion_debt_tracker | Notion debt tracker]] is a tool designed to help users monitor debt payments, manage them effectively, and work towards becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This minimalistic tracker is built using five distinct databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Tracker Sections Overview

The tracker is organized into several key sections:

### Summary Section
This section provides a high-level overview of all debts, displaying the total loan amount, total amount repaid, total interest repaid, and the repayment in percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This section is linked to the "Total Debt" database <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

### Debt Overview
Under this section, specific categories of debt are listed, including student loans, credit cards, car loans, personal loans, home loans, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each category, it shows the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated date of becoming debt-free <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This section is linked to the "Summary of Debt" database <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

### Debt Progressive Payments
This section outlines future progressive due payments <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It displays the month of payment, the amount due, and the payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Clicking a checkbox updates the payment status, and entering the payment amount updates progress <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Once an amount is paid, it updates the corresponding "debt overview" section with the amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This section is linked to the "Loan Details" database <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

## Essential Databases

To build this [[creating_a_notion_debt_tracker | Notion debt tracker]], five databases are required <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

### 1. Debt Database
This database holds all debt-related information <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Properties**:
    *   **Name**: Default property, lists debt types (e.g., student loan, credit card, car loan, personal loan, home loan, other loan) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
    *   **Loan Amount**: Total loan amount, a number property <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
    *   **Interest Rate**: Annual interest rate, a number property displayed in percentage format <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   **Minimum Payment**: Minimum monthly repayment amount, a number property <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
    *   **Additional Repayment**: Amount paid during the first installment (e.g., down payment), a number property <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
    *   **Initial Repayment Date**: Date of the first installment payment <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   **Interest Rate Per Month**: Calculated by dividing the interest rate by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
    *   **Debt Free Period**: A formula property calculating the debt-free period in months <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
    *   **Expected Debt Free By**: A formula property calculating the estimated debt-free date by adding the debt-free period to the initial repayment date <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   **Net Loan Outstanding Amount**: A formula property that calculates the outstanding loan amount before the first installment, by deducting the additional payment from the loan amount <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This value serves as the opening balance for the "Loan Details" database <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### 2. Loan Details Database
This database records individual installment payments <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Properties**:
    *   **Installment Number**: Specifies the sequential number of payments made against a debt <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
    *   **Date of Payment of Installment**: The date when an installment is repaid <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
    *   **Category of Loan**: Relates to the "Debt Overview" database, specifying one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
    *   **Opening Balance**: The outstanding debt balance before the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. For the first month, this is the net loan outstanding from the "Debt" database; for subsequent months, it's the closing balance of the previous month <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   **Payment Amount**: The amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, it includes the minimum amount and any additional payment; for subsequent months, it's the minimum amount <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   **Interest Calculation**: A formula property calculating the interest amount paid per installment (opening balance × interest rate / 12) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
    *   **Principal Value**: A formula property calculated as payment amount minus interest amount <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   **Closing Balance**: A formula property calculated as opening balance minus principal amount <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
    *   **Checkbox**: Reflects payment status (paid/not paid); clicking it updates the status <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
    *   **Total Repayment**: A formula property that calculates the total amount paid (including interest and principal) when the checkbox is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### 3. Debt Overview Database
This database provides an overview of each debt type <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Properties**:
    *   **Loan Amount**: Rolled up from the "Loan Details" database <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
    *   **Total Amount Repaid**: Rolled up from the "Loan Details" database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   **Total Principal Repaid**: Rolled up from the "Loan Details" database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
    *   **Total Interest Repaid**: Rolled up from the "Loan Details" database <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
    *   **Outstanding Amount**: Calculated by deducting the total principal repaid from the loan amount <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
    *   **Repayment in Percentage**: Calculated as the principal repaid divided by the total loan amount, displayed as a percentage <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database
This database calculates total figures for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Properties**:
    *   **Total Loan Amount**: Rolled up from the "Debt Overview" database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
    *   **Total Amount Repaid**: Rolled up from the "Debt Overview" database <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
    *   **Total Interest Repaid**: Rolled up from the "Debt Overview" database <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
    *   **Repayment in Percentage**: Rolled up from the "Debt Overview" database <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
    *   **Debt Free Date**: Rolled up from the "Debt Overview" database <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### 5. Total Debt Database
This database provides combined totals for all debts <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   **Properties**:
    *   **Total Loan Amount**: Reflects the total loan value of all debts combined <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   **Total Amount Repaid**: Combined total of all amounts repaid <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   **Total Interest Repaid**: Combined total of all interest repaid <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
    *   **Repayment in Percentage**: Combined repayment percentage for all debts <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
These values are rolled up from the "Debt Overview" database and populated using formulas <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.