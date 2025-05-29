---
title: Creating a Notion debt tracker
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker can be built to help monitor debt payments and progress towards becoming debt-free <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This minimalistic tracker is designed to help users track their debts effectively <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Components of the Debt Tracker

The Notion debt tracker typically includes three main sections:

1.  **Summary Section**
    This section provides an overview of all debts combined <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. It displays the total loan amount, total amount repaid, total interest repaid, and the overall repayment in percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This section is linked to the [[total_debt_database | total debt database]] <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

2.  **Debt Overview**
    This section breaks down different types of debts, such as student loans, credit cards, car loans, personal loans, home loans, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each debt category, it shows:
    *   Total loan amount <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
    *   Total amount repaid <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
    *   Total interest repaid <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
    *   Repayment in percentage <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
    *   The estimated date by which the debt will be paid off <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>

    This section is linked to the [[summary_of_debt_database | summary of debt database]] <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

3.  **Debt Progressive Payments**
    This part outlines progressive due payments for the future <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It includes the month of payment, the repayment amount, and the payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   Clicking a checkbox updates the payment status to "paid" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
    *   Updating payment progress reflects in the debt overview section under the respective debt category for amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
    *   This section is linked to individual loans from the [[loan_details_database | loan details database]] <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

## Building the Notion Debt Tracker with Databases

Building this minimalistic Notion debt tracker requires five interconnected databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### 1. Debt Database
This database lists all different types of debts <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
It includes the following properties:
*   **Name**: Specifies the type of debt (e.g., student loan, credit card, car loan, personal loan, home loan, other loan) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Loan Amount**: The total amount of the loan <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Interest Rate**: The annual interest rate for each debt, specified in percentage format <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Minimum Payment**: The minimum monthly payment required <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Additional Repayment**: Any extra amount paid during the first installment, like a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Initial Repayment Date**: The date when the first installment was repaid <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Debt-Free Period**: A formula that calculates the number of months it will take to be debt-free from the initial repayment date <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Expected Debt-Free By**: An estimated date calculated by adding the debt-free period to the initial repayment date <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount**: The outstanding loan amount before the first installment, serving as the opening balance for the [[loan_details_database | loan details database]] <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This is derived by deducting the additional payment from the loan amount <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### 2. Loan Details Database
This database captures the specifics of each repayment <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. It records details related to loan repayment, ultimately showing the outstanding balance <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
Properties include:
*   **Installment Number**: Tracks the number of installments paid against the debt <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment**: The specific date an installment was paid <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan**: Links to the [[debt_overview_database | debt overview database]] by specifying one of six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance**: The debt balance prior to the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. The first month's opening balance is the net loan outstanding from the Debt Database, while subsequent months use the previous month's closing balance <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Payment Amount**: The minimum amount paid monthly <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, it includes any additional payments <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Interest Calculation**: A formula that calculates the interest amount paid per installment (opening balance × monthly interest rate) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value**: Calculated as payment amount minus interest amount <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: Calculated as opening balance minus the principal amount for the month <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Checkbox**: Reflects the payment status as "paid" or "not paid" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment**: A formula that calculates the total amount paid (total, interest, and principal) against each debt when the checkbox is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. These amounts are also summed at the bottom <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database
This database provides a quick overview of each debt type <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
It features:
*   **Loan Amount**: Rolled up from the [[loan_details_database | loan details database]] <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid**: A roll-up value from the [[loan_details_database | loan details database]] <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid**: A roll-up value from the [[loan_details_database | loan details database]] <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid**: A roll-up value from the [[loan_details_database | loan details database]] <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount**: Calculated by subtracting the principal repaid from the loan amount <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: The ratio of principal repaid to the total loan amount, displayed as a percentage <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Debt-Free Date**: The projected date to become debt-free <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### 4. Summary of Debt Database
This database summarizes key financial figures for each type of debt <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
It calculates:
*   Total loan amount <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   The date by which the user will be free of the debt <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

All these figures are pulled in as roll-up values from the [[debt_overview_database | debt overview database]] <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### 5. Total Debt Database
This database provides a comprehensive view of all debts combined <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
It reflects the consolidated:
*   Total loan amount <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>

Similar to the [[summary_of_debt_database | summary of debt database]], these values are rolled up from the [[debt_overview_database | debt overview database]] <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

This comprehensive setup allows for effective [[using_notion_for_debt_management_and_tracking_debt_payments | tracking debt payments using Notion]] and achieving financial goals <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.