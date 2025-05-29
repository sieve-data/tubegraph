---
title: Payment Tracking and Debt Progression
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker can assist in [[tracking_debt_payments_effectively | tracking debt payments]] on time and working towards becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This type of tracker provides a comprehensive overview of debt, including detailed repayment progress.

## Overview of the Notion Debt Tracker

The tracker is designed to provide a clear financial snapshot related to debt <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Summary Section
This section displays aggregate figures for all debts combined <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>

### Debt Overview
This section categorizes different types of debt, such as <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>:
*   Student loan <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
*   Credit card <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Car loan <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Personal loan <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
*   Home loan <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   Other loans <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

For each category, it shows <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
*   Estimated debt-free date <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>

### Debt Progressive Payments
This section details future due payments <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It includes <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>:
*   Month of payment <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   Amount of repayment <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
*   Status of payment (paid or not paid) <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>

When a payment is made, checking the corresponding checkbox updates the status to 'paid' and reflects the change in the debt overview section under 'amount repaid,' 'interest repaid,' and 'repayment in percentage' <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This enables real-time [[debt_payoff_progress_tracking | debt payoff progress tracking]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Building the Notion Debt Tracker

[[creating_a_notion_debt_tracker | Creating a Notion Debt Tracker]] involves setting up five interconnected databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### 1. Debt Database
This database lists all debt types, such as student loan, credit card, car loan, personal loan, home loan, and other loans <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
Key properties include <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>:
*   **Loan Amount:** Total amount of the loan <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Interest Rate:** Per annum interest rate, specified in US Dollars and in percent format <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Minimum Payment:** Minimum monthly payment amount <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Additional Repayment:** Any extra amount paid during the first installment, like a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Initial Repayment Date:** The date of the first installment payment <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Interest Rate Per Month (I Value):** Calculated by dividing the interest rate by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt Free Period:** A formula-driven property that calculates the debt-free period in months <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt Free By:** An estimated debt-free date calculated by adding the debt-free period to the initial repayment date <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount:** The opening balance of the debt before the first installment, derived by deducting additional payments from the loan amount <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### 2. Loan Details Database
This database records individual repayment details for each debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. It tracks the outstanding balance <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
Properties include <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>:
*   **Installment Number:** Identifies the payment sequence <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment of Installment:** The specific date of each repayment <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan:** Links to the type of loan being repaid <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance:** The balance of the debt before the current repayment. For the first month, it's the net loan outstanding from the Debt Database; for subsequent months, it's the closing balance of the previous month <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Payment Amount:** The amount paid each month. The first installment includes minimum and additional payments; subsequent months are equal to the minimum payment <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Interest Calculation:** A formula specifying the interest paid per installment (Opening Balance x (Interest Rate / 12)) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value:** Calculated as Payment Amount less Interest Amount <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Closing Balance:** Opening Balance minus Principal Amount <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status Checkbox:** Reflects 'paid' or 'not paid' status <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment (Amount, Interest, Principal):** Calculated when the payment checkbox is ticked, summing up the respective values at the bottom of the database <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. This enables [[tracking_payment_transactions_and_updates | tracking payment transactions and updates]] and [[tracking_receivable_and_payable_balances | tracking receivable and payable balances]] <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database
This database provides a summary of all debt types <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
Properties are rolled up from the Loan Details database or derived using formulas <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>:
*   **Loan Amount** <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>
*   **Total Amount Repaid** <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>
*   **Total Principal Repaid** <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>
*   **Total Interest Repaid** <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>
*   **Outstanding Amount of Loan:** Loan Amount minus Principal Repaid <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage:** Principal Repaid to Total Loan Amount, calculated as a percentage <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database
This database provides a per-debt summary of key metrics <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
Figures for each property are pulled as roll-up values from the Debt Overview database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>:
*   Total loan amount <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>
*   Debt-free date <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

### 5. Total Debt Database
This final database consolidates information from all debts <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
It reflects the total loan amount, total amount repaid, total interest repaid, and repayment in percentage for all debts combined <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. Values are rolled up and calculated using formulas from the Debt Overview database <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This database is crucial for overall [[tracking_and_managing_transactions_for_cash_flow | cash flow management]] and [[tracking_savings_goals_and_progress | tracking savings goals and progress]] by understanding overall debt burden.

By establishing these five databases and linking them, a comprehensive [[using_notion_for_debt_tracking | Notion debt tracking]] system can be built <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, providing valuable insights into debt progression and facilitating informed financial decisions using [[formulas_and_calculations_for_debt_tracking | formulas and calculations for debt tracking]].