---
title: Creating a Notion Debt Tracker
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

This article outlines how to create a Notion debt tracker to help manage and track debt payments, aiming for debt freedom <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The tracker provides a comprehensive overview of your financial obligations and progress towards repayment <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Tracker Overview and Features

A [[using_notion_for_debt_tracking | Notion debt tracker]] includes several key sections:

*   **Summary Section**: Displays the total loan amount, total amount repaid, total interest repaid, and repayment in percentage for all debts combined <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Debt Overview**: Provides a detailed breakdown for specific debt categories such as student loan, credit card, car loan, personal loan, home loan, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each category, it shows the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Debt Progressive Payments**: Shows upcoming due payments, including the month of payment, repayment amount, and payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Checking a box updates the payment status, which then reflects in the debt overview section <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Database Requirements for a Notion Debt Tracker

To build this minimalistic [[database_requirements_for_a_notion_debt_tracker | Notion debt tracker]], five databases are required <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>:

1.  **Debt Database**: Holds the entire database of all debts <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **Loan Details Database**: Provides details related to loan repayments, leading to the outstanding balance <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
3.  **Debt Overview Database**: Gives an overview of each debt <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
4.  **Summary of Debt Database**: Shows a summary of each type of debt <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
5.  **Total Debt Database**: Displays the combined total debt value <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Building the Databases

### 1. Debt Database

This database lists all different types of debt <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
Common debt types include student loan, credit card, car loan, personal loan, home loan, and other loans <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

**Properties**:
*   **Name**: Default property specifying the type of debt (e.g., student loan, credit card) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Loan Amount**: Total amount of the loan (Number property, US dollars) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Interest Rate**: Interest rate per annum (Number property, US dollars, Percentage format) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Minimum Payment**: Minimum monthly payment required (Number property, US dollars) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Additional Repayment**: Amount paid during the first installment, such as a down payment (Number property, US dollars) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Initial Repayment Date**: The date when the first installment was repaid (Date property) <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Interest Rate per Month**: Interest rate divided by 12 (Formula: `Interest Rate / 12`) <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt-Free Period**: Calculates the debt-free period in months (Formula property) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt Free By**: Estimated debt-free date, adding the Debt-Free Period to the Initial Repayment Date (Formula property) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount**: Calculates the net debt payable before the first installment, which serves as the opening balance for the Loan Details database (Formula: `Loan Amount - Additional Payment`) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>, <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### 2. Loan Details Database

This database is used to fill in the repayment details for each debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

**Properties**:
*   **Installment Number**: Specifies the installment number paid against the debt <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment**: The date of repayment for the installment (Date property) <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan**: Relates to the debt overview database, specifying one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance**: The debt balance prior to the repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. For the first month, this is the "Net Loan Outstanding Amount" from the Debt Database; for subsequent months, it's the previous month's closing balance <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Payment Amount**: The minimum amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.For the first installment, it includes the minimum amount and any additional payment <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Interest Calculation**: The interest amount paid for each installment (Formula: `Opening Balance * (Interest Rate / 12)`) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value**: The principal amount paid (Formula: `Payment Amount - Interest Amount`) <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Closing Balance**: The remaining balance after principal repayment (Formula: `Opening Balance - Principal Amount`) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status Checkbox**: A checkbox property to reflect whether the payment is "paid" or "not paid" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Amount Paid against Total/Interest/Principal**: These are formula properties that calculate the total repayment, interest paid, and principal paid *only* when the "Payment Status" checkbox is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. The total repayment amounts for total, interest, and principal are summed up at the bottom of the database <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database

This database provides an overview of all types of debts <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

**Properties**:
*   **Loan Amount**: Rolled up from the "Loan Details Database" and derived using a formula from the rolled-up amounts <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid**: A roll-up value from the "Loan Details Database" <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid**: A roll-up value from the "Loan Details Database" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid**: A roll-up value from the "Loan Details Database" <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount**: Calculated by deducting the "Principal Repaid" from the "Loan Amount" (Formula) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: Calculates the percentage of principal repaid against the total loan amount (Formula) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database

This database calculates the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the debt-free date for each individual debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
The figures for each property are pulled as a roll-up from the "Debt Overview Database" <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This process is repeated for all debt types <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

### 5. Total Debt Database

This database reflects the total loan amount, total amount repaid, total interest repaid, and the repayment percentage for *all* debts combined <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
Similar to the "Summary of Debt Database", values are rolled up from the "Debt Overview Database" and populated using a formula <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

## Primary Dashboard Integration

After building all the databases, they are integrated into the main dashboard:

*   **Summary Section**: Linked to the "Total Debt Database" to display combined totals for loan amount, amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section**: Linked to the "Summary of Debt Database" to show individual debt details including loan amount, amount repaid, interest repaid, repayment percentage, and debt-free date <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section**: Linked to the "Loan Details Database" to display progressive repayments, dates, and amounts for individual loans <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

This comprehensive [[managing_debt_and_loans_in_notion | Notion system]] helps users effectively [[tracking_personal_finances_in_notion | track personal finances]] and work towards becoming debt-free.