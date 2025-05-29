---
title: Creating a Notion debt tracker
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker can assist in [[debt_payment_tracking_using_notion | tracking debt payments]] on time and facilitating the journey to becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This tracker provides a comprehensive view of outstanding debts and progress towards repayment <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Tracker Overview

The debt tracker is organized into key sections for easy understanding and management:

### Summary Section
This section provides an aggregate view of all debts, showing:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>
This section is linked to the "Total Debt" database <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

### Debt Overview
This section categorizes debts into specific types, such as:
*   Student loan <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
*   Credit card <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Car loan <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
*   Personal loan <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   Home loan <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   Other loan <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

For each debt category, the tracker displays:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
*   The estimated date of debt freedom <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
This section is linked to the "Summary of Debt" database <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

### Debt Progressive Payments
This section outlines future due payments progressively <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It shows:
*   Month of payment <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   Amount of repayment <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
*   Status of payment (paid or not paid) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

When an amount is repaid, checking a box updates the status to "paid" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This update reflects in the Debt Overview section for the respective debt under "amount repaid," "interest repaid," and "repayment in percentage" <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
This section is linked to the "Loan Details" database <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

## Building the Notion Debt Tracker Databases

To construct this Notion debt tracker, five interconnected databases are required <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

### 1. Debt Database
The "Debt Database" is the foundational component, holding the entire database of all debts <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This is the first database to be built for the tracker <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

**Properties:**
*   **Name (Default Property):** Specifies the type of debt (e.g., Student Loan, Credit Card, Car Loan, Personal Loan, Home Loan, Other Loan) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Loan Amount:** The total amount of the loan <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This is a number property in US dollars <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Interest Rate:** The annual interest rate for each debt <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This is a number property in percent format <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Minimum Payment:** The minimum monthly payment required <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This is a number property in US dollars <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Additional Repayment:** Any extra amount paid during the first installment, like a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This is a number property in US dollars <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Initial Repayment Date:** The date when the first installment was repaid <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This has a date property <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Interest Rate Per Month (I Value):** A formula property that calculates the interest rate per month by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Debt Free Period:** A formula property that calculates the estimated time in months to become debt-free <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Expected Debt Free By:** A formula property that calculates an estimated debt-free date by adding the "Debt Free Period" to the "Initial Repayment Date" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount:** A formula property that calculates the net debt payable before the first installment, serving as the opening balance for the "Loan Details" database <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This is derived by deducting the "Additional Repayment" from the "Loan Amount" <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

[[building_a_debt_database_in_notion | Building a debt database in Notion]] is the first step in creating the overall tracker.

### 2. Loan Details Database
This database is used to record the specific details of each repayment installment for every debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

**Properties:**
*   **Installment Number:** Specifies the number of installments paid against the debt <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment:** Specifies the date of repayment for each installment <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. This has a date property <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Category of Loan:** Relates to the debt overview database, specifying one of the six debt categories being repaid <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance:** The balance of the debt prior to the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    *   For the first month's payment, this is the "Net Loan Outstanding Amount" from the "Debt Database" <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   For subsequent months, this is the closing balance of the previous month <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **Payment Amount:** The amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
    *   For the first installment, it includes the minimum amount and any additional payment <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   For subsequent months, it is equal to the minimum payment amount <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Interest Calculation:** A formula specifying the interest amount paid in each installment <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This is calculated as: `Opening Balance * (Interest Rate / 12)` <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Principal Value:** A formula calculated as: `Payment Amount - Interest Amount` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance:** A formula calculated as: `Opening Balance - Principal Amount` <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status:** A checkbox that reflects if the payment is "paid" or "not paid" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment (Total Amount, Interest, Principal):** Formulas that calculate the amount paid against the total amount, interest, and principal, specifically when the "Payment Status" checkbox is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. These values are also summed at the bottom of the database <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database
This database provides a high-level overview of each debt type <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

**Properties:**
*   **Loan Amount:** Rolled up from the "Loan Details" database and derived using a formula <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid:** Rolled up from the "Loan Details" database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid:** Rolled up from the "Loan Details" database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid:** Rolled up from the "Loan Details" database <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount:** Calculated by subtracting the "Principal Repaid" from the "Loan Amount" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage:** Calculated as the "Principal Repaid" divided by the "Total Loan Amount," expressed as a percentage <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database
The "Summary of Debt" database calculates and displays key metrics for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

**Properties (all rolled up from the "Debt Overview" database):**
*   Total loan amount <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>
*   The date by which one will be free of the debt <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

This database pulls the figures for each property as a roll-up, repeating the process for all debt types <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. [[synthesizing_debt_overview_and_summary_in_notion | Synthesizing debt overview and summary in Notion]] is crucial for this stage.

### 5. Total Debt Database
The "Total Debt" database provides a consolidated view of all debts combined <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

**Properties (all rolled up from the "Debt Overview" database and populated using formulas):**
*   Total loan amount <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>

This completes the construction of all necessary databases for the Notion debt tracker <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.