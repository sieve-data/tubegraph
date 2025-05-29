---
title: Using Notion for financial planning and debt overview
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

[[Creating a Notion debt tracker | Creating a Notion debt tracker]] in Notion can help track debt payments on time and assist in becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This system allows for [[using_notion_for_personal_finance_management | personal finance management]] and [[using_notion_for_financial_tracking | financial tracking]] by providing a comprehensive overview of debts <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Overview of the Notion Debt Tracker

The Notion debt tracker typically includes:
*   **Summary Section**: Displays the total loan amount, total amount repaid, total interest repaid, and repayment in percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Debt Overview**: Categories like student loan, credit card, car loan, personal loan, home loan, and other loans are listed <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Under each category, it shows the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Debt Progressive Payments**: Outlines future due payments, including the month of payment, amount of repayment, and payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

When an amount is repaid, checking a checkbox updates the status and reflects the payment in the Debt Overview section for amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Building the Notion Debt Tracker

[[Building databases for debt management in Notion | Building databases for debt management in Notion]] for this minimalistic tracker requires five key databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

### 1. Debt Database
This database lists all different types of debt <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a> and is the starting point for [[setting_up_notion_for_personal_finance_tracking | setting up Notion for personal finance tracking]] related to debt. It includes the following properties:
*   **Name**: Specifies the type of debt (e.g., student loan, credit card) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Loan Amount**: The total amount of the loan <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Interest Rate**: Per annum interest rate, specified in percent format <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Minimum Payment**: The minimum monthly payment to be repaid <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Additional Repayment**: Any additional amount paid during the first installment, like a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Initial Repayment Date**: The first installment date <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Interest Rate Per Month**: Calculated by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt Free Period**: A formula that calculates the debt-free period in months <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt Free By**: An estimated debt-free date derived by adding the debt-free period to the initial repayment date <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount**: The amount of loan outstanding before the first installment, serving as the opening balance for the Loan Details database <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This is derived by deducting the additional payment from the loan amount <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### 2. Loan Details Database
This database holds repayment details for each debt, crucial for [[how_to_use_notion_for_tracking_debt_payments | how to use Notion for tracking debt payments]] and [[using_notion_for_debt_management_and_tracking_debt_payments | using Notion for debt management and tracking debt payments]].
*   **Installment Number**: Specifies the number of installments paid <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment**: The date of repayment for each installment <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan**: Relates to the debt overview database, specifying one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance**: The debt balance prior to the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. The first month's opening balance is the `Net Loan Outstanding` from the Debt database; subsequent months copy the previous month's closing balance <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Payment Amount**: The minimum amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, it includes the minimum amount plus any additional payment <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Interest Calculation**: A formula for the interest amount paid in each installment (Opening Balance * Interest Rate / 12) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value**: Payment amount less the interest amount paid <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: Opening balance less the principal amount for the month <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status Checkbox**: Reflects whether the payment is paid or not paid <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment**: A formula that is considered when an amount is paid and the checkbox is ticked <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This logic also applies to interest and principal values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### 3. Debt Overview Database
This database provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Loan Amount**: Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid, Total Principal Repaid, Total Interest Repaid**: Derived as roll-up values from the Loan Details database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Outstanding Amount**: Calculated by deducting the principal repaid from the loan amount <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: Principal repaid divided by the total loan amount, shown as a percentage <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database
This database calculates key figures for each debt type, aiding in [[managing_debts_and_loans_using_notion | managing debts and loans using Notion]] and [[using_notion_for_personal_finance | using Notion for personal finance]].
*   **Total Loan Amount, Total Amount Repaid, Total Interest Repaid, Repayment in Percentage, Debt Free Date**: Figures are pulled in as roll-ups from the Debt Overview database <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

### 5. Total Debt Section
This final database reflects combined totals for all debts, helping with overall [[using_notion_for_financial_tracking | financial tracking]].
*   **Total Loan Amount, Total Amount Repaid, Total Interest Repaid, Repayment in Percentage**: Values rolled up from the Debt Overview database and calculated using formulas <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

## Primary Dashboard
The primary dashboard integrates these databases to provide a comprehensive view:
*   **Summary Section**: Linked to the Total Debt database, showing combined totals for loan amount, amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section**: Linked to the Summary of Debt database, detailing each debt type's loan amount, repaid amount, interest repaid, repayment percentage, and debt-free date <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section**: Linked to the Loan Details database, displaying progressive repayments with corresponding dates and amounts <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.