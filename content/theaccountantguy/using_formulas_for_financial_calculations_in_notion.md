---
title: Using formulas for financial calculations in Notion
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker can be built using various databases and [[using_formulas_in_notion | formulas]] to track debt payments and progress toward becoming debt-free <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This tracker includes sections for a summary, debt overview, and progressive payments <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Debt Tracker Overview

The Notion debt tracker provides a summary section showing the total loan amount, total amount repaid, total interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The debt overview categorizes different loan types such as student loan, credit card, car loan, personal loan, home loan, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each category, it displays the total loan amount, total amount repaid, total interest repaid, repayment percentage, and the estimated debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

The "Debt Progressive Payments" section outlines upcoming due payments, showing the month of payment, amount, and status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Checking a box updates the payment status and reflects the progress in the debt overview section <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Databases Required for Debt Tracker

Building this minimalistic Notion debt tracker requires five key databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

1.  **Loan Details Database** <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>: Provides details related to loan repayments, calculating the outstanding balance <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
2.  **Debt Database** <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>: Holds information on all debts, including loan amount, interest rate, minimum payment, additional repayment, initial repayment date, and the estimated debt-free date <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
3.  **Debt Overview Database** <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>: Offers a quick glance at each debt, showing loan amount, total amount repaid, principal repaid, interest repaid, outstanding amount, repayment percentage, and debt-free date <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
4.  **Summary of Debt Database** <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>: Summarizes the loan amount, amount repaid, interest repaid, repayment percentage, and debt-free date for each type of debt <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
5.  **Total Debt Section Database** <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>: Displays the total debt value of all combined debts <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## [[using_formulas_in_notion | Formula]] Applications in Databases

### Debt Database Calculations

The Debt Database lists different debt types (e.g., student loan, credit card, car loan) and their associated financial properties <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

*   **Loan Amount, Interest Rate, Minimum Payment, Additional Repayment**: These are typically number properties, often specified in US dollars <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. The interest rate is calculated per annum and displayed in a percentage format <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Initial Repayment Date**: A date property indicating the first repayment date <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Interest Rate per Month (I Value)**: A [[using_formulas_in_notion | formula]] property calculated by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Debt Free Period**: A [[using_formulas_in_notion | formula]] property that calculates the debt-free period in months <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt Free By**: A [[using_formulas_in_notion | formula]] that adds the "Debt Free Period" to the "Initial Repayment Date" to estimate the debt-free date <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Net Loan Outstanding**: A [[using_formulas_in_notion | formula]] that calculates the net debt payable before the first installment, by deducting the "Additional Repayment" from the "Loan Amount" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This value serves as the opening balance for the Loan Details database <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Loan Details Database Calculations

This database tracks individual installment details for each debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

*   **Opening Balance**: For the first month's payment, this is the "Net Loan Outstanding" from the Debt Database <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. For subsequent months, it is the "Closing Balance" of the previous month <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   **Payment Amount**: Represents the minimum monthly payment <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, it also includes any additional payment <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Interest Calculation**: A [[using_formulas_in_notion | formula]] property that calculates the interest paid each installment by multiplying the "Opening Balance" with the "Interest Rate" divided by 12 <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Principal Value**: A [[using_formulas_in_notion | formula]] property calculated by subtracting the "Interest Amount" from the "Payment Amount" <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: A [[using_formulas_in_notion | formula]] property equal to the "Opening Balance" minus the "Principal Amount" for each month <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Total Repayment (Conditional)**: A [[using_formulas_in_notion | formula]] that registers the amount paid against total, interest, and principal only when the payment status checkbox is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### Debt Overview Database Calculations

This database provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

*   **Loan Amount**: Rolled up from the Loan Details database, with a [[using_formulas_in_notion | formula]] to derive the value from the rolled-up amounts <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid, Total Principal Repaid, Total Interest Repaid**: Derived as roll-up values from the Loan Details database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Outstanding Amount**: Calculated by a [[using_formulas_in_notion | formula]] that subtracts the "Principal Repaid" from the "Loan Amount" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: A [[using_formulas_in_notion | formula]] property that calculates the percentage of repayment by dividing the "Principal Repaid" by the "Total Loan Amount" <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Summary of Debt Database Calculations

This database aggregates total figures for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

*   **Loan Amount, Amount Repaid, Interest Repaid, Repayment Percentage, Debt-Free Date**: All figures are pulled in as roll-up values from the Debt Overview database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### Total Debt Database Calculations

This database shows the combined total for all debts <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

*   **Total Loan Amount, Total Amount Repaid, Total Interest Repaid, Repayment Percentage**: Values are rolled up from the Debt Overview database and populated using [[using_formulas_in_notion | formulas]] to pull the desired aggregated values <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

The completed Notion debt tracker dashboard integrates these databases to display the summary, debt overview, and debt progress sections, all dynamically updated through linked data and [[using_formulas_in_notion | formulas]] <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.