---
title: Creating a Notion Debt Tracker
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker can assist in tracking debt payments on time and help users become debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This minimalistic tracker is built using five distinct databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Tracker Overview

The Notion debt tracker typically includes three main sections:
*   **Summary Section** This section provides an overview of the total loan amount, total amount repaid, total interest repaid, and the repayment in percentage for all combined debts <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview** This section provides a detailed view of different debt categories, such as student loans, credit cards, car loans, personal loans, home loans, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each category, it displays the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a> <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progressive Payments** This section outlines progressive due payments for the time ahead, showing the month of payment, the amount of repayment, and the payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Clicking a checkbox updates the payment status, which is then reflected in the Debt Overview section <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a> <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Database Components

The [[using_notion_for_debt_tracking | Notion debt tracker]] is constructed using five databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

### 1. Debt Database

This database lists all different types of debts, such as student loan, credit card, car loan, personal loan, home loan, and other loan <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a> <a class="yt-timestamp" data-t="00:04:92">[00:04:92]</a>.
It includes the following properties:
*   **Name** (default property): Specifies the type of debt <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Loan Amount**: The total amount of the loan against the debt <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This is a number property, specified in US dollars <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Interest Rate (per annum)**: The interest rate per annum for each debt, specified in US dollars and formatted as a percentage <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a> <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Minimum Payment**: The minimum monthly payment to be repaid <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This is a number property <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Additional Repayment**: An additional repayment amount made during the first installment, such as a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This is a number property <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Initial Repayment Date**: The first installment date when the debt was repaid <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This is a date property <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Interest Rate Per Month**: A calculation of the interest rate per month, derived by dividing the `Interest Rate` by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt Free Period**: A formula that calculates the debt-free period in months <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt Free By**: An estimated debt-free date, calculated by adding the `Debt Free Period` to the `Initial Repayment Date` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Net Loan Outstanding Amount**: The amount of loan outstanding before the first repayment, derived by deducting the `Additional Repayment` from the `Loan Amount` <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a> <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This serves as the opening balance for the Loan Details database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### 2. Loan Details Database

This database records the details of each debt repayment <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
It includes the following properties:
*   **Installment Number**: Specifies the number of installments paid against the debt <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment of Installment**: The date of repayment for each installment <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. This has a date property <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Category of Loan**: A relation to the `Debt Overview Database` specifying one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance**: The outstanding debt amount prior to the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. For the first month, it's the `Net Loan Outstanding` from the `Debt Database`; for subsequent months, it's the `Closing Balance` of the previous month <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Payment Amount**: The amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, it includes the minimum and any additional payments; for subsequent months, it's just the minimum amount <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Interest Calculation**: A formula calculating the interest amount paid per installment (Opening Balance \* Interest Rate / 12) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Principal Value**: A formula calculating the principal amount paid (Payment Amount - Interest Amount) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance**: A formula calculating the remaining balance (Opening Balance - Principal Amount) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status**: A checkbox that reflects if the payment is "paid" or "not paid" <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment**: A formula that calculates the total amount repaid against the debt when the `Payment Status` checkbox is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Similar logic applies for `Interest` and `Principal Value` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. The total amounts repaid are summed up at the bottom of the database <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database

This database provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
It contains the following properties:
*   **Loan Amount**: Rolled up from the `Loan Details Database` and derived using a formula <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid**, **Total Principal Repaid**, and **Total Interest Repaid**: These are derived as roll-up values from the respective fields in the `Loan Details Database` <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Outstanding Amount**: Calculated by deducting the `Principal Repaid` from the `Loan Amount` using a formula <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage**: The percentage of principal repaid to the total loan amount <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database

This database calculates summarized figures for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
It includes:
*   **Total Loan Amount** <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Total Amount Repaid** <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Total Interest Repaid** <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Repayment in Percentage** <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   **Debt-Free Date** <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
All these figures are pulled in as roll-up values from the `Debt Overview Database` for each debt type <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### 5. Total Debt Database

This database aggregates the total debt value for all debts combined <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
It shows:
*   **Total Loan Amount** <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   **Total Amount Repaid** <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Total Interest Repaid** <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Repayment in Percentage** <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
These values are rolled up from the `Debt Overview Database` and populated using formulas <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

## Primary Dashboard Integration

The primary dashboard links the various sections to their respective databases:
*   The **Summary section** is linked to the `Total Debt Database` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   The **Debt Overview section** is linked to the `Summary of Debt Database` <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   The **Debt Progress section** is linked to the `Loan Details Database` <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

This comprehensive [[managing_debts_and_loans_with_notion | Notion debt tracker]] allows for detailed monitoring of debt obligations and progress towards becoming debt-free <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.