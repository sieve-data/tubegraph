---
title: Building databases for debt tracking
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A [[creating_a_notion_debt_tracker | Notion Debt Tracker]] can assist in [[tracking_debt_payments_and_liabilities | tracking debt payments]] on time and working towards becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This type of [[personal_finance_tracker | personal finance tracker]] provides a comprehensive [[overview_of_debt_payment_tracker | overview of debt payment tracker]] progress <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

The core components of a [[debt_tracker | Debt Tracker]] include:
*   A summary section displaying total loan amount, total amount repaid, total interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   A debt overview for various categories (e.g., student loan, credit card, car loan, personal loan, home loan, other loan), detailing total loan amount, total amount repaid, total interest repaid, repayment percentage, and the estimated debt-free date for each <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   A section for progressive debt payments, showing monthly payments, amounts, and payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Payments can be marked as paid by clicking a checkbox, which automatically updates the status and reflects in the debt overview section <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Essential Databases for a Notion Debt Tracker

To build this [[debt_tracker | minimalistic Notion Debt Tracker]], five interconnected databases are required <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:
1.  **Debt Database** <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
2.  **Loan Details Database** <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
3.  **Debt Overview Database** <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
4.  **Summary of Debt Database** <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>
5.  **Total Debt Database** <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>

### 1. Debt Database

This database lists all different types of debt <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>, such as student loan, credit card, car loan, personal loan, home loan, and other loan <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

Key properties include:
*   **Name** (default property): Specifies the type of debt <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Loan Amount**: Total amount of the loan, a number property formatted in US dollars <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Interest Rate**: Per annum interest rate, a number property formatted as a percentage <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Minimum Payment**: The minimum monthly payment due <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, a number property formatted in US dollars <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Additional Repayment**: Any extra amount paid during the first installment, like a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, a number property formatted in US dollars <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Initial Repayment Date**: The date of the first installment payment <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, a date property <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Interest Rate Per Month**: A formula property that calculates `Interest Rate / 12` <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt Free Period**: A formula property that calculates the estimated time in months to be debt-free from the initial repayment date <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Expected Debt Free By**: A formula property that calculates the estimated debt-free date by adding the `Debt Free Period` to the `Initial Repayment Date` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount**: A formula property calculating the net debt payable before the first installment, typically `Loan Amount - Additional Repayment` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This value becomes the opening balance for the Loan Details Database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### 2. Loan Details Database

This database tracks specific installment details for each debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

Key properties include:
*   **Installment Number**: Specifies which installment is being paid <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment**: The date of the installment repayment <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>, a date property <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Category of Loan**: A relation property linking to the `Debt Database` to specify which debt type the payment belongs to <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance**: The debt balance before the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    *   For the first month, this is the `Net Loan Outstanding` from the `Debt Database` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   For subsequent months, it's the `Closing Balance` of the previous month <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   **Payment Amount**: The total amount paid in a given installment <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
    *   First installment: `Minimum Payment` + `Additional Repayment` <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   Subsequent months: `Minimum Payment` <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Interest Calculation**: A formula property for the interest paid in each installment: `Opening Balance * (Interest Rate / 12)` <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Principal Value**: A formula property: `Payment Amount - Interest Amount` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: A formula property: `Opening Balance - Principal Amount` <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status Checkbox**: A checkbox property to mark payments as "paid" or "not paid" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment**: A formula property that calculates the `Payment Amount` only when the `Payment Status Checkbox` is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Similar formulas apply for `Interest Repaid` and `Principal Repaid` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   Sums of `Total Repayment`, `Interest Repaid`, and `Principal Repaid` are typically displayed at the bottom of the database view <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database

This database provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

Key properties, primarily derived as roll-up values from the `Loan Details Database` and `Debt Database`:
*   **Loan Amount**: Rolled up from the `Debt Database` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid**: Rolled up from the `Loan Details Database` <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid**: Rolled up from the `Loan Details Database` <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid**: Rolled up from the `Loan Details Database` <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount**: A formula property: `Loan Amount - Principal Repaid` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: A formula property: `(Principal Repaid / Total Loan Amount) * 100` <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database

This database calculates summarized totals for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

Key properties are all roll-up values from the `Debt Overview Database` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>:
*   **Total Loan Amount** <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>
*   **Total Amount Repaid** <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   **Total Interest Repaid** <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   **Repayment in Percentage** <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   **Debt Free Date** <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

### 5. Total Debt Database

This database combines all debts to show overall totals <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

Key properties are roll-up values from the `Debt Overview Database`, aggregated to calculate totals for all debts combined <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>:
*   **Total Loan Amount** <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
*   **Total Amount Repaid** <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
*   **Total Interest Repaid** <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>
*   **Repayment in Percentage** <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>

## Dashboard Structure

The primary dashboard of the [[creating_a_notion_debt_tracker | Notion Debt Tracker]] integrates these databases into a user-friendly interface:
*   **Summary Section**: Displays total loan amount, total amount repaid, interest repaid, and repayment in percentage for all debts combined, linked to the `Total Debt Database` <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section**: Shows details for each debt type (total loan, amount repaid, interest repaid, repayment percentage, and debt-free date), linked to the `Summary of Debt Database` <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section**: Features progressive repayments with corresponding dates and amounts, linked to the `Loan Details Database` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

[[Using databases in Notion for financial tracking | Using these databases in Notion]] creates a robust system for [[tracking_personal_finances_for_beginners | beginners to track personal finances]] and manage liabilities effectively.