---
title: Formulas and Calculations for Debt Tracking
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker, designed to help monitor and manage debt payments, incorporates several formulas and calculations to provide a comprehensive overview of financial progress <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The tracker features a summary section displaying total loan amount, total amount repaid, total interest repaid, and repayment in percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Each debt category, such as student loan, credit card, or car loan, also shows its total loan amount, total amount repaid, total interest repaid, repayment percentage, and estimated debt-free date <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Updating the payment status in the progressive payments section automatically reflects the changes in the debt overview for amounts repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Core Databases and Their Calculations

To [[creating_a_notion_debt_tracker | create this Notion debt tracker]], five key databases are utilized <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

1.  Loan Details
2.  Debt Database
3.  Debt Overview Database
4.  Summary of Debt Database
5.  Total Debt Section

Each database plays a role in [[tracking_debt_payments_effectively | tracking debt payments effectively]] and includes specific formulas for various calculations.

### Debt Database Calculations

The Debt Database holds an overview of all debts, including properties like loan amount, interest rate, minimum payment, additional repayment, initial repayment date, and the expected debt-free date <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This database includes calculations for:

*   **Interest Rate Per Month (I Value)**: Calculated by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Debt-Free Period**: A formula determines the number of months it will take to become debt-free <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt-Free By**: Calculated by adding the "Debt-Free Period" to the "Initial Repayment Date" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Net Loan Outstanding Amount**: Derived by deducting any "Additional Payment" from the "Loan Amount" <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This value represents the opening balance for the Loan Details database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### Loan Details Database Calculations

This database records specific details for each installment paid against a debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Key calculations include:

*   **Opening Balance**: For the first month's payment, it's the "Net Loan Outstanding" from the Debt Database <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. For subsequent months, it's the "Closing Balance" of the previous month <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Payment Amount**: The first installment includes the "Minimum Amount" plus any "Additional Payment" <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. Subsequent months are equal to the "Minimum Amount" <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Interest Calculation**: Determined by multiplying the "Opening Balance" by the "Interest Rate" (from the Debt Database) divided by 12 <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Principal Value**: Calculated by subtracting the "Interest Amount" from the "Payment Amount" <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: Equal to the "Opening Balance" minus the "Principal Amount" for each month <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Total Repayment**: Calculated as a formula that considers the payment amount only when the associated checkbox (indicating payment status) is ticked <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This logic is also applied to calculate total interest and principal repaid <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### Debt Overview Database Calculations

This database provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. Values here are primarily "rolled up" from the Loan Details database or derived through formulas:

*   **Loan Amount**: Rolled up from the Loan Details database, with a formula used to derive its value <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid, Total Principal Repaid, Total Interest Repaid**: Derived as roll-up values from the Loan Details database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Outstanding Amount of Loan**: Calculated by subtracting the "Total Principal Repaid" from the "Loan Amount" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: Represents the "Total Principal Repaid" relative to the "Total Loan Amount," calculated as a percentage <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Summary of Debt Database

This database presents a summary for each type of debt, including total loan amount, total amount repaid, total interest repaid, repayment percentage, and the debt-free date <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. All these figures are pulled in as roll-up values from the Debt Overview database <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### Total Debt Section Database

This final database provides a combined view of all debts, showing the total loan amount, total amount repaid, total interest repaid, and the overall repayment percentage <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. Similar to the Summary of Debt database, values are rolled up from the Debt Overview database and populated using formulas <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. This database powers the primary summary section of the tracker <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

These interconnected databases and their respective formulas enable the [[using_notion_for_debt_tracking | Notion debt tracker]] to provide a clear, real-time overview of [[debt_payoff_progress_tracking | debt payoff progress tracking]] <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, aiding in achieving financial freedom.