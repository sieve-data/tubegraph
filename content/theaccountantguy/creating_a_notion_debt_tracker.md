---
title: Creating a Notion debt tracker
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A [[managing_debts_and_loans_in_notion | Notion debt tracker]] is designed to help users monitor debt payments, ensure timely repayments, and work towards becoming debt-free <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This tracker provides a comprehensive overview of your financial obligations and repayment progress <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Key Sections of the Tracker

The [[managing_debts_and_loans_in_notion | Notion debt tracker]] typically includes several key sections for easy financial management:

*   **Summary Section** This section displays the total loan amount, total amount repaid, total interest repaid, and the overall repayment percentage across all debts <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Debt Overview** Provides a detailed breakdown for different types of loans, such as student loans, credit cards, car loans, personal loans, and home loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each loan type, it shows the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Debt Progressive Payments** Outlines upcoming due payments by month, including the payment amount and its status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Checking a box updates the payment status, and this progress is reflected in the Debt Overview section <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Building the [[managing_debts_and_loans_in_notion | Notion Debt Tracker]]

To build this [[setting_up_notion_for_personal_finance_tracking | personal finance tracker]], five distinct databases are required <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### 1. Debt Database

This database lists all different types of debts <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a> and holds comprehensive details for each <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

**Properties:**
*   **Name:** The default property used to specify the type of debt (e.g., student loan, credit card, car loan, personal loan, home loan, other loan) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Loan Amount:** The total original amount of the loan (Number property, US Dollars) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Interest Rate:** The annual interest rate for each debt (Number property, Percent format) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   **Interest Rate Per Month (I Value):** A formula property calculating the monthly interest rate by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Minimum Payment:** The minimum monthly payment required <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Additional Repayment:** Any extra payment made during the first installment, like a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Initial Repayment Date:** The date when the first installment of the debt was repaid <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Debt Free Period:** A formula that calculates the number of months it will take to become debt-free from the initial repayment date <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Expected Debt Free By:** A formula that calculates an estimated debt-free date by adding the Debt Free Period to the Initial Repayment Date <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount:** A formula that calculates the loan amount outstanding before the first installment, by deducting the additional payment from the loan amount <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This acts as the opening balance for the Loan Details database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 2. Loan Details Database

This database is used to track individual repayments against each debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

**Properties:**
*   **Installment Number:** Specifies the number of the installment being paid <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment:** The specific date when the installment was repaid (Date property) <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan:** Relates to the Debt Overview database, linking the payment to one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance:** The outstanding debt amount before the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    *   For the first month, this is the "Net Loan Outstanding Amount" from the Debt Database <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   For subsequent months, it's the "Closing Balance" from the previous month <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.# [[managing_debts_and_loans_in_notion | Creating a Notion Debt Tracker]]

A [[managing_debts_and_loans_in_notion | Notion debt tracker]] is designed to help users monitor debt payments, ensure timely repayments, and work towards becoming debt-free <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This tracker provides a comprehensive overview of your financial obligations and repayment progress <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Key Sections of the Tracker

The [[managing_debts_and_loans_in_notion | Notion debt tracker]] typically includes several key sections for easy financial management:

*   **Summary Section** This section displays the total loan amount, total amount repaid, total interest repaid, and the overall repayment percentage across all debts <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Debt Overview** Provides a detailed breakdown for different types of loans, such as student loans, credit cards, car loans, personal loans, and home loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each loan type, it shows the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the estimated debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Debt Progressive Payments** Outlines upcoming due payments by month, including the payment amount and its status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Checking a box updates the payment status, and this progress is reflected in the Debt Overview section <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Building the [[managing_debts_and_loans_in_notion | Notion Debt Tracker]]

To build this [[setting_up_notion_for_personal_finance_tracking | personal finance tracker]], five distinct databases are required <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### 1. Debt Database

This database lists all different types of debts <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a> and holds comprehensive details for each <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

**Properties:**
*   **Name:** The default property used to specify the type of debt (e.g., student loan, credit card, car loan, personal loan, home loan, other loan) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Loan Amount:** The total original amount of the loan (Number property, US Dollars) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Interest Rate:** The annual interest rate for each debt (Number property, Percent format) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   **Interest Rate Per Month (I Value):** A formula property calculating the monthly interest rate by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Minimum Payment:** The minimum monthly payment required <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Additional Repayment:** Any extra payment made during the first installment, like a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Initial Repayment Date:** The date when the first installment of the debt was repaid <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Debt Free Period:** A formula that calculates the number of months it will take to become debt-free from the initial repayment date <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Expected Debt Free By:** A formula that calculates an estimated debt-free date by adding the Debt Free Period to the Initial Repayment Date <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount:** A formula that calculates the loan amount outstanding before the first installment, by deducting the additional payment from the loan amount <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This acts as the opening balance for the Loan Details database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 2. Loan Details Database

This database is used to track individual repayments against each debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

**Properties:**
*   **Installment Number:** Specifies the number of the installment being paid <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment:** The specific date when the installment was repaid (Date property) <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan:** Relates to the Debt Overview database, linking the payment to one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance:** The outstanding debt amount before the current repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    *   For the first month, this is the "Net Loan Outstanding Amount" from the Debt Database <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   For subsequent months, it's the "Closing Balance" from the previous month <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   **Payment Amount:** The minimum amount paid each month <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For the first installment, this includes the minimum amount and any additional payment <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Interest Calculation:** A formula that calculates the interest amount paid for each installment <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a> (Opening Balance multiplied by the monthly interest rate) <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Principal Value:** A formula derived by subtracting the Interest Amount from the Payment Amount <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance:** A formula derived by subtracting the Principal Amount from the Opening Balance for each month <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Payment Status:** A checkbox to reflect whether the payment has been made ("paid" or "not paid") <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment:** A formula that accounts for the total amount paid against the debt, activated when the payment status checkbox is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Total Interest Paid:** A similar formula that sums the interest paid when the checkbox is ticked <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Total Principal Paid:** A similar formula that sums the principal paid when the checkbox is ticked <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### 3. Debt Overview Database

This database provides a summary view of all types of debts <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

**Properties:**
*   **Loan Amount:** Rolled up from the Loan Details database and derived using a formula <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid:** Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Total Principal Repaid:** Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Total Interest Repaid:** Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Outstanding Amount:** Calculated by subtracting the Principal Repaid from the Loan Amount <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage:** Calculated as the Principal Repaid divided by the Total Loan Amount, expressed as a percentage <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database

This database calculates and displays key financial figures for each debt type <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

**Properties:**
*   **Total Loan Amount:** Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Total Amount Repaid:** Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Total Interest Repaid:** Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   **Repayment in Percentage:** Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Debt Free Date:** Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### 5. Total Debt Section Database

This final database aggregates all debt values to provide an overall financial picture <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

**Properties:**
*   **Total Loan Amount:** Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Total Amount Repaid:** Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Total Interest Repaid:** Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Repayment in Percentage:** Rolled up from the Debt Overview database <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Primary Dashboard Setup

The primary dashboard integrates these databases to present a unified view of your debt tracking:

*   **Summary Section:** Links to the Total Debt Database to show combined totals for loan amount, amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section:** Links to the Summary of Debt Database, displaying individual debt details like loan amount, amount repaid, interest repaid, repayment percentage, and debt-free date for each debt type <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section:** Links to the Loan Details Database, showcasing progressive repayments with corresponding dates and amounts for each individual loan <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

This setup completes the [[managing_debts_and_loans_in_notion | Notion debt tracker]], providing a comprehensive tool for managing and understanding your debts <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.