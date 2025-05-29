---
title: Tracking Debt Payoff Progress in Notion
videoId: p7aozLHRzq0
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to utilize a [[creating_a_notion_debt_tracker | debt payment tracker]] in Notion to manage and pay off debts <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Debt Overview Section

The debt overview section categorizes debts by payment frequency <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Default categories include annual and monthly payments <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

The following details are tracked for each debt:
*   **Debt Details** <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>
*   **Loan Amount** <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   **EMI Amount** (Equated Monthly Installment) - the amount paid for each installment <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   **Interest Rate** <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>
*   **Initial Repayment** - the first payment date <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>
*   **Debt Free By** - a calculated date indicating when the debt will be paid off if repayments continue at the specified amount and interest rate <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
*   **Number of EMIs** - the total number of installments required to pay off the debt <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

### Managing Debt Categories
Users can add new payment categories, such as "weekly", by clicking the "add a group" button <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The template already includes necessary payment schedules, which can be viewed by clicking to reveal hidden groups like quarterly and weekly repayments <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Debts can be moved between repayment schedules, and all associated calculations will automatically update <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Debt Payoff Progress

This [[summary_section_in_notion_debt_tracker | summary section]] provides an overview of the debt payoff status <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It reflects all loans added to the debt categories <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

Key metrics in this section include:
*   **Total Amount Repaid** - calculated from the installments recorded at the bottom of the tracker <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This updates automatically when an EMI is paid <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Net Payoff in Percentage** - shows the percentage of the total debt paid off <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Debt Free By** - a quick reference to the estimated debt-free date <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Interest Amount** - the total interest paid so far <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Principal Amount** - the total principal repaid <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Every repayment is split into interest and principal <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Adding and Editing Debts
To quickly add a new debt, click the "add details" button <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. New debts initially appear in a "no payment frequency" column and can then be moved to the appropriate frequency <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Existing loan details can be edited by clicking on the debt field, which automatically updates all related columns and descriptions <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

## Transaction Section

This section records all debt payments made <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Paid Installment Section
The "paid installment" section displays all paid debts, bifurcated by month, with the latest month appearing at the top <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. It provides a summation of all EMIs paid for that particular month <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

Each payment entry includes:
*   **Paid Checkbox** - Ticking this marks an installment as paid, updating its status in the "paid installment" or "unpaid" column <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Payment Date** <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>
*   **Loan Details** - Allows selection of a specific loan added earlier <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **EMI Amount of Payment** <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
*   **Next Repayment Schedule** - Automatically calculated based on the loan's set payment frequency <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. For example, a monthly student loan payment made on September 30 will automatically show October 30 as the next payment <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. Similarly, an annual home loan payment on September 27, 2023, will set the next payment for September 27, 2024 <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Adding New Debt Payments
Clicking the "pay debt amount" button automatically adds a new debt payment to the schedule, set to the current date <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Users can then input details and descriptions <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. All updates made in the transaction section, such as changing an EMI amount, will automatically reflect in the [[summary_section_in_notion_debt_tracker | debt payoff progress summary]] <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.