---
title: Tracking Debt Repayments and Progress
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion Debt Tracker can help individuals [[monitoring_debt_payment_and_loan_repayment_progress | track debt payments on time]] and work towards becoming debt-free <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This tool aims to provide a clear overview of financial obligations and progress towards eliminating them <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Key Features

The tracker is designed with several sections to provide a comprehensive view of debt management:

*   **Summary Section** This section displays key aggregated financial figures, including the total loan amount, total amount repaid, total interest repaid, and the overall repayment percentage <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Debt Overview** This part breaks down debts into specific categories such as student loans, credit cards, car loans, personal loans, home loans (which can utilize [[mortgage_payment_tracking | Mortgage Payment Tracking]]), and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each category, it shows the total loan amount, total amount repaid, total interest repaid, repayment percentage, and the projected debt-free date <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Debt Progressive Payments** This section outlines progressive due payments for the future <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It includes the month of payment, repayment amount, and the status (paid or not paid) <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This feature enables detailed [[tracking_transactions_and_payment_percentages | tracking of transactions and payment percentages]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Updating Progress

To [[tracking_debt_payoff_progress | track debt payoff progress]], users can interact with the tracker by clicking a checkbox once an amount is repaid, which updates the payment status to "paid" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Entering the payment amount and updating the status reflects progress <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Once a payment is recorded, it automatically updates the corresponding debt in the Debt Overview section for amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Building the Notion Debt Tracker

[[creating_a_notion_debt_tracker | Creating a Notion Debt Tracker]] requires five core databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

1.  **Debt Database** This database holds comprehensive information for all debts, including the loan amount, interest rate, minimum monthly payment, any additional repayment (like a down payment), the initial repayment date, and the calculated debt-free period in months <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. It also calculates an expected debt-free date and the net loan outstanding amount before the first installment <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   **Properties**
        *   **Name:** Categorizes debt (e.g., student loan, credit card, car loan) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
        *   **Loan Amount, Interest Rate, Minimum Payment, Additional Repayment:** Number properties, with interest rate specified per annum and in percentage format <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
        *   **Initial Repayment Date:** Date property for the first payment <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
        *   **Interest Rate Per Month (I-value):** Formula property, interest rate divided by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
        *   **Debt-Free Period:** Formula property calculating debt-free period in months <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
        *   **Expected Debt-Free By:** Formula property, adding debt-free period to the initial repayment date <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
        *   **Net Loan Outstanding:** Formula property, loan amount minus additional payment <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

2.  **Loan Details Database** This database is crucial for [[loan_and_repayment_details_management | loan and repayment details management]] and [[setting_up_repayment_schedules | setting up repayment schedules]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
    *   **Properties**
        *   **Installment Number:** Specifies the number of installments paid <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
        *   **Date of Payment of Installment:** Date property <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
        *   **Category of Loan:** Relates to the debt overview database <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
        *   **Opening Balance:** The net loan outstanding from the Debt Database for the first month; subsequent months use the previous month's closing balance <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
        *   **Payment Amount:** Minimum monthly payment, including additional payment for the first installment <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
        *   **Interest Calculation:** Formula property, (opening balance \* interest rate) / 12 <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
        *   **Principal Value:** Formula property, payment amount minus interest amount <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
        *   **Closing Balance:** Formula property, opening balance minus principal amount <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
        *   **Payment Status:** Checkbox property for paid/not paid <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
        *   **Total Repayment (Total Amount, Interest, Principal):** Formula properties, considered when the checkbox is ticked <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. These amounts are also summed at the bottom of the database <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

3.  **Debt Overview Database** Provides a glance at each debt <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   **Properties:** Includes loan amount, total amount repaid, principal repaid, interest repaid, outstanding amount, repayment percentage, and debt-free date <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Values are rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
    *   **Outstanding Amount:** Calculated by loan amount minus principal repaid <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
    *   **Repayment in Percentage:** Calculated as principal repaid to total loan amount <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

4.  **Summary of Debt Database** Shows aggregated figures for each type of debt <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   **Properties:** Displays loan amount, amount repaid, interest repaid, repayment percentage, and debt-free date for each debt type <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Figures are pulled as roll-up values from the Debt Overview database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

5.  **Total Debt Database** Reflects the combined total values for all debts <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
    *   **Properties:** Shows total loan amount, total amount repaid, total interest repaid, and overall repayment percentage for all debts combined <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. Values are rolled up from the Debt Overview database and populated using formulas <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Primary Dashboard

The primary dashboard provides a user-friendly interface for [[managing_debt_and_loan_repayments | managing debt and loan repayments]]:

*   **Summary Section:** Presents combined totals (total loan amount, total amount repaid, interest repaid, repayment percentage) linked to the Total Debt database <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section:** Details each debt with its loan amount, total amount repaid, interest repaid, repayment percentage, and debt-free date, linked to the Summary of Debt database <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section:** Shows progressive repayments with dates and amounts, linked to individual loans from the Loan Details database <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.