---
title: Building databases for debt management in Notion
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

This guide details how to [[creating_a_notion_debt_tracker | create a Notion debt tracker]] to effectively [[tracking_debt_payments_using_notion | track debt payments]] and work towards becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This tracker is designed to help you [[using_notion_for_financial_planning_and_debt_overview | manage your financial planning and debt overview]] efficiently <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Overview of the Notion Debt Tracker

The completed Notion debt tracker includes several key sections:

*   **Summary Section**: Displays the total loan amount, total amount repaid, total interest repaid, and repayment in percentage for all combined debts <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Debt Overview Section**: Categorizes debts such as student loans, credit cards, car loans, personal loans, home loans, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each category, it shows the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Debt Progressive Payments**: Outlines future due payments, including the payment month, repayment amount, and payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Checking a box updates the payment status and reflects the progress in the debt overview section <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Required Databases for the Notion Debt Tracker

To build this [[creating_a_notion_debt_tracker | minimalistic Notion debt tracker]], five interlinked databases are required <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

1.  **Loan Details Database**: Provides details related to loan repayments, showing the outstanding balance <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
2.  **Debt Database**: Holds the entire database of all debts <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
3.  **Debt Overdue Database**: Offers a quick overview of each debt <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
4.  **Summary of Debt Database**: Summarizes the loan amount, amount repaid, interest repaid, repayment percentage, and debt-free date for each type of debt <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
5.  **Total Debt Section (Database)**: Shows the combined total debt value <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Building the Databases

### 1. Debt Database

This is the starting point for [[creating_a_notion_debt_tracker | creating the Notion debt tracker]] <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. It lists different types of debt, such as student loans, credit cards, car loans, personal loans, home loans, and other loans <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

**Key Properties:**

*   **Name**: Default property, specifies the type of debt (e.g., Student Loan, Credit Card) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Loan Amount**: Total amount of the loan (Number property, US dollars) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Interest Rate**: Per annum interest rate for each debt (Number property, percentage format) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Minimum Payment**: Minimum monthly payment required for each debt (Number property, US dollars) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Additional Repayment**: Any additional repayment made during the first installment, like a down payment (Number property, US dollars) <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Initial Repayment Date**: The date when the first installment of the debt was repaid (Date property) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Interest Rate Per Month**: Calculated by dividing the annual interest rate by 12 (Formula property) <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt Free Period**: Calculates the debt-free period in months (Formula property) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt Free By**: Estimates the debt-free date by adding the debt-free period to the initial repayment date (Formula property) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Net Loan Outstanding Amount**: Calculates the net debt payable before the first installment, acting as the opening balance for the Loan Details database (Formula property) <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### 2. Loan Details Database

This database is used to fill in repayment details for each debt category <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

**Key Properties:**

*   **Installment Number**: Specifies the installment number paid against the debt <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment**: The date of repayment for each installment (Date property) <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan**: Related to the debt overview database, specifying one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance**: The debt balance before the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. For the first month, it's the net loan outstanding from the Debt Database; for subsequent months, it's the closing balance of the previous month <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Payment Amount**: The minimum amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, it includes the minimum amount and any additional payment <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Interest Calculation**: A formula specifying the interest amount paid per installment (Opening Balance \* Interest Rate Per Month) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value**: Payment amount less the interest amount paid (Formula property) <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Closing Balance**: Opening balance minus the principal amount for each month (Formula property) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status**: A checkbox reflecting if the payment is "paid" or "not paid" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment**: The amount paid against the total amount, interest, and principal for each debt <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. This is calculated via a formula when the payment status checkbox is ticked <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### 3. Debt Overview Database

This database provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

**Key Properties:**

*   **Loan Amount**: Rolled up from the Loan Details database, derived using a formula from the rolled-up amounts <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount**: Loan amount minus the principal repaid (Formula property) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: Principal repaid divided by the total loan amount, calculated as a percentage <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database

This database calculates summarized figures for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

**Key Properties (all rolled up from the Debt Overview database):**

*   **Total Loan Amount** <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>
*   **Total Amount Repaid** <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   **Total Interest Repaid** <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   **Repayment in Percentage** <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>
*   **Debt-Free Date** <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

This process is repeated for all types of debts <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

### 5. Total Debt Database

This final database reflects the combined total debt figures <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

**Key Properties (all rolled up from the Debt Overview database and calculated with formulas):**

*   **Total Loan Amount** <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
*   **Total Amount Repaid** <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
*   **Total Interest Repaid** <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>
*   **Repayment in Percentage** <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>

## Primary Dashboard

Once all databases are built, they are integrated into a primary dashboard for a comprehensive [[using_notion_for_financial_planning_and_debt_overview | financial overview]] and [[using_notion_for_debt_management_and_tracking_debt_payments | debt management and tracking debt payments]].

*   **Summary Section**: Linked to the Total Debt database, it shows the total loan amount, total amount repaid, interest repaid, and repayment in percentage for all debts combined <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section**: Linked to the Summary of Debt database, it displays each debt type with its total loan amount, total amount repaid, interest repaid, repayment in percentage, and debt-free date <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section**: Linked to the Loan Details database, it shows progressive repayments with corresponding dates and amounts <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

This structure allows for effective [[managing_debts_and_loans_using_notion | managing debts and loans using Notion]], [[using_databases for financial tracking in Notion | using databases for financial tracking in Notion]], and [[organizing_financial_data_in_Notion | organizing financial data in Notion]].