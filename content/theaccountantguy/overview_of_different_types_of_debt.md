---
title: Overview of different types of debt
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A [[creating_a_notion_debt_tracker | Notion debt tracker]] is designed to help users track debt payments on time and work towards becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This tracker includes specific categories for different types of debt, alongside comprehensive details to monitor repayment progress.

## Debt Categories

The [[debt_tracker | Debt Tracker]] is structured to manage various common debt types, including:
*   Student loan <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>
*   Credit card <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Car loan <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Personal loan <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
*   Home loan <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   Other loan <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

These categories are specified in the "name" property of the debt database <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## Debt Overview and Details Tracked

For each debt category, the [[overview_of_debt_payment_tracker | Overview of Debt Payment Tracker]] provides detailed information:

### Key Metrics per Debt
Under each debt type, the [[debt_tracker | Debt Tracker]] displays:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   The estimated date by which the debt will be cleared <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>

### Progressive Payments
The [[tracking_debt_payoff_progress_in_notion | Tracking Debt Payoff Progress in Notion]] section outlines progressive due payments <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. This includes:
*   Month of payment <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   Amount of repayment <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
*   Status of payment (paid or not paid) <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>

When a payment is recorded, the status updates, and the "debt overview" section reflects the updated amount repaid, interest repaid, and repayment percentage for the respective debt <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Underlying Databases for Debt Tracking

The [[creating_a_notion_debt_tracker | Notion debt tracker]] is built upon five interconnected databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, contributing to [[building_databases_for_debt_tracking | building databases for debt tracking]]:

### Debt Database
This database holds comprehensive information for all debts, including:
*   Loan amount <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>
*   Interest rate (per annum) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   Minimum payment <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>
*   Additional repayment (e.g., down payment) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>
*   Initial repayment date <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>
*   Date when debt-free <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>
*   Debt-free period (in months) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>
*   Expected debt-free by date <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
*   Net loan outstanding amount (opening balance before first installment) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>

### Loan Details Database
This database records specific repayment information for each installment:
*   Installment number <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>
*   Date of payment <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>
*   Category of loan being repaid (linked to debt overview database) <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>
*   Opening balance of debt prior to repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>
*   Payment amount <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a> (minimum payment plus additional payment for first installment; minimum payment for subsequent months) <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>
*   Interest calculation (opening balance * interest rate/12) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>
*   Principal value (payment amount - interest amount) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>
*   Closing balance (opening balance - principal amount) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>
*   Checkbox for payment status (paid/not paid) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>
*   Amount paid against total amount, interest, and principal (calculated if checkbox is ticked) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>

### Debt Overview Database
This database provides an overview of each debt type <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, rolling up values from the Loan Details database:
*   Loan amount <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
*   Total principal repaid <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>
*   Outstanding amount (loan amount - principal repaid) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>
*   Repayment in percentage (principal repaid / total loan amount) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>

### Summary of Debt Database
This database calculates the overall summary for each debt type by rolling up figures from the Debt Overview database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>, displaying:
*   Total loan amount <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   Debt-free date <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

### Total Debt Database
This database reflects the combined totals for all debts <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>, also by rolling up values from the Debt Overview database <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. It shows:
*   Total loan amount <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>

These databases work together to provide a comprehensive system for [[tracking_debt_payments_and_liabilities | tracking debt payments and liabilities]] and [[managing_and_classifying_assets_and_liabilities | managing and classifying assets and liabilities]].