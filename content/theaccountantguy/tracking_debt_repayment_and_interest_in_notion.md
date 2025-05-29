---
title: Tracking debt repayment and interest in Notion
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

This article details how to [[creating_a_notion_debt_tracker | create a Notion debt tracker]] designed to help users track debt payments, understand interest repayments, and work towards becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Tracker Overview

The [[creating_a_notion_debt_tracker | Notion debt tracker]] features several sections to provide a comprehensive view of one's debt situation:

*   **Summary Section**
    This section provides an at-a-glance summary showing the total loan amount, total amount repaid, total interest repaid, and the repayment in percentage for all combined debts <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview**
    This section categorizes debts into types such as student loan, credit card, car loan, personal loan, home loan, and other loans <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For each category, it displays the total loan amount, total amount repaid, total interest repaid, repayment percentage, and the estimated date of being debt-free <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Debt Progressive Payments**
    This part outlines future due payments, detailing the month of payment, the repayment amount, and the payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Updating Progress

When a payment is made, clicking a checkbox updates the status to "paid" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This update is reflected in the debt overview section, showing changes in the amount repaid, interest repaid, and repayment percentage for the respective debt <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Users simply click and enter the payment amount and update the payment status to track their progress <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Building the Notion Debt Tracker

The [[creating_a_notion_debt_tracker | minimalistic Notion debt tracker]] requires five distinct databases <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>:

### 1. Debt Database

This database lists all different types of debts <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. It includes the following properties:

*   **Name Property:** Specifies the type of debt (e.g., student loan, credit card, car loan, personal loan, home loan, other loan) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a> <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Loan Amount:** The total amount of the loan <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Interest Rate:** The annual interest rate for each debt, specified in percent format <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a> <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Minimum Payment:** The minimum monthly payment required <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Additional Repayment:** Any extra amount paid during the first installment, such as a down payment <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Initial Repayment Date:** The date when the first installment was repaid <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a> <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Interest Rate Per Month:** Calculated by dividing the annual interest rate by 12 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Debt-Free Period:** A formula that calculates the period in months until the debt is paid off <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a> <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Expected Debt-Free By:** An estimated debt-free date calculated by adding the debt-free period to the initial repayment date <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Net Loan Outstanding Amount:** The net debt payable before the first installment, serving as the opening balance for the loan details database <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a> <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This is derived by deducting the additional payment from the loan amount <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### 2. Loan Details Database

This database stores the specifics of repayments for each debt <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Key properties include:

*   **Installment Number:** Specifies the number of installments paid against a debt <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Date of Payment of Installment:** The date of each repayment <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Category of Loan:** Relates to the debt overview database, specifying one of the six debt categories <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Opening Balance of Debt:** The outstanding balance prior to a repayment <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. The first month's payment uses the Net Loan Outstanding from the Debt Database, while subsequent months copy the previous month's closing balance <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Payment Amount:** The minimum monthly payment, which for the first installment includes any additional payment <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Interest Calculation:** A formula specifying the interest amount paid per installment, calculated as `opening balance * (interest rate / 12)` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Principal Value:** Calculated as `payment amount - interest amount` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Closing Balance:** Calculated as `opening balance - principal amount` <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Checkbox:** Reflects the payment status (paid or not paid) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Total Repayment:** A formula that considers the amount paid and the checkbox status to calculate total amount, interest, and principal paid against each debt <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a> <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. These amounts are also summed at the bottom <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Debt Overview Database

This database provides an overview of all debt types <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>:

*   **Loan Amount:** Rolled up from the Loan Details database <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Total Amount Repaid, Total Principal Repaid, Total Interest Repaid:** These are roll-up values from the Loan Details database <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Outstanding Amount of Loan:** Calculated as `loan amount - principal repaid` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Repayment in Percentage:** The ratio of `principal repaid` to `total loan amount`, calculated in percentage <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### 4. Summary of Debt Database

This database calculates a summary for each debt type <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>:

*   **Total Loan Amount, Total Amount Repaid, Total Interest Repaid, Repayment in Percentage, Debt-Free Date:** These figures are pulled in as roll-up values from the Debt Overview database for each debt type <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

### 5. Total Debt Database

This final database reflects the aggregated totals for all combined debts <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>:

*   **Total Loan Amount, Total Amount Repaid, Total Interest Repaid, and Repayment Percentage:** These values are rolled up from the Debt Overview database and populated using formulas <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Primary Dashboard Structure

The primary dashboard provides a unified view of the debt situation <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>:

*   **Summary Section:** Linked to the Total Debt database, showing overall loan, repaid, interest, and repayment percentage <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Debt Overview Section:** Linked to the Summary of Debt database, displaying details for each debt type <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Debt Progress Section:** Linked to the Loan Details database, showcasing progressive repayments with dates and amounts <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

This comprehensive [[creating_a_notion_debt_tracker | Notion debt tracker]] allows for detailed [[managing_debts_and_loans_in_notion | managing debts and loans in Notion]], helping users stay on track with their repayment goals <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.