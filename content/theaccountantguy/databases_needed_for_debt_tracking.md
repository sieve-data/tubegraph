---
title: Databases needed for debt tracking
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A minimalistic [[creating_a_notion_debt_tracker | Notion debt tracker]] can be built using five core databases to help track debt payments on time and work towards becoming debt-free <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This tracker provides a summary section showing total loan amount, total amount repaid, total interest repaid, and repayment in percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. It also includes a debt overview for various loan types like student loan, credit card, car loan, personal loan, home loan, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

The tracker also features a "Debt Progressive Payments" section, which outlines future progressive due payments, including the month, repayment amount, and payment status (paid/not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Checking a box updates the payment status to "paid" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. When an amount is paid, it updates the "debt overview" section with the amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Core Databases for the Debt Tracker

To construct this Notion debt tracker, five specific databases are required <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### 1. Debt Database

This database lists all different types of debt <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a> and holds the entire record of all debts <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

**Key Properties:**
*   **Name:** Default property, specifying debt types such as student loan, credit card, car loan, personal loan, home loan, and other loan <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Loan Amount:** Total amount of the loan against the debt, a number property formatted in US dollars <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Interest Rate:** Per annum interest rate for each debt, a number property formatted as a percentage <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Minimum Payment:** Minimum monthly payment to be repaid each month, a number property formatted in US dollars <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Additional Repayment:** Amount paid during the first installment, like a down payment, a number property formatted in US dollars <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Initial Repayment Date:** The first installment date when the debt is repaid, a date property <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Interest Rate per Month (I Value):** Calculated by dividing the `Interest Rate` by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt-Free Period:** A formula property that calculates the debt-free period in months <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt-Free By:** An estimated debt-free date calculated by adding the `Debt-Free Period` to the `Initial Repayment Date` <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Net Loan Outstanding Amount:** Calculates the net debt payable before the first installment date, serving as the opening balance for the `Loan Details` database <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This is derived by deducting the `Additional Repayment` from the `Loan Amount` <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### 2. Loan Details Database

This database is used to fill in the details of repayment for each debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

**Key Properties:**
*   **Installment Number:** Specifies the number of installments paid against the debt <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment of Installment:** Specifies the date of repayment for each installment, a date property <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan:** Related to the `Debt Overview` database, specifying one of the six debt categories being repaid <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance:** Debt amount prior to repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. For the first month, it's the `Net Loan Outstanding` from the `Debt` database <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. For subsequent months, it's copied from the previous month's `Closing Balance` <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Payment Amount:** The minimum amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, it includes the minimum amount and any additional payment <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>; for subsequent months, it equals the minimum amount <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Interest Calculation:** A formula property specifying the interest amount paid each installment. It's the `Opening Balance` multiplied by (`Interest Rate` / 12) <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value:** Calculated as `Payment Amount` minus `Interest Amount` <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Closing Balance:** Calculated as `Opening Balance` minus the `Principal Amount` for each month <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status:** A checkbox property reflecting whether the payment is "paid" or "not paid" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment:** A formula that calculates the total amount paid against the loan, interest, and principal, contingent on the `Payment Status` checkbox being ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### 3. Debt Overview Database

This database provides a quick overview of each debt type <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

**Key Properties:**
*   **Loan Amount:** Rolled up from the `Loan Details` database, derived using a formula <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid:** Rolled up value from the `Loan Details` database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid:** Rolled up value from the `Loan Details` database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid:** Rolled up value from the `Loan Details` database <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount:** Calculated by deducting the `Principal Repaid` from the `Loan Amount` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage:** Calculated as `Principal Repaid` to the `Total Loan Amount` in percentage format <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Debt-Free Date:** The date by which one is expected to be free of the debt <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### 4. Summary of Debt Database

This database calculates the total loan amount, total amount repaid, total interest repaid, repayment percentage, and the debt-free date for each type of debt <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. Figures for these properties are pulled in as roll-ups from the `Debt Overview` database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### 5. Total Debt Section (Database)

This section reflects the total loan amount, total amount repaid, total interest repaid, and repayment percentage for all combined debts <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. Similar to the `Summary of Debt` database, values are rolled up from the `Debt Overview` database and populated using formulas <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

## Dashboard Integration

Once all databases are built, they integrate into the primary dashboard:

*   **Summary Section:** Linked to the `Total Debt` database, this section displays the total loan amount, total amount repaid, total interest repaid, and repayment percentage for all combined debts <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section:** Linked to the `Summary of Debt` database, it details each debt type with its total loan amount, total amount repaid, interest repaid, repayment percentage, and debt-free date <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section:** Linked to the `Loan Details` database, this section shows progressive repayments of debts with corresponding dates and amounts <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

This structured approach using [[utilizing_notion_databases_for_financial_tracking | Notion databases]] allows for comprehensive and organized [[debt_payment_tracking_and_reporting | debt payment tracking and reporting]], aiding in the journey to becoming debt-free.