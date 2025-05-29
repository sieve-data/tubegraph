---
title: Loan and repayment details management
videoId: p7aozLHRzq0
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to utilize a [[monitoring_debt_payment_and_loan_repayment_progress | debt payment tracker]] to [[managing_debt_and_loan_repayments | manage and pay off debts]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The tracker is designed to help users [[tracking_debt_payoff_progress | track debt payoff progress]] and manage various loan details efficiently.

## Debt Overview Section

The debt overview section categorizes debts and displays essential information for each loan <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Key fields include:

*   **Debt Details**: Specific information about the debt <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Loan Amount**: The total amount of the loan <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **EMI Amount**: The amount to be paid for each installment <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Interest Rate**: The specified interest rate for the loan <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **Initial Repayment**: The first date an installment will be paid <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Debt Free By**: A calculated date indicating when the debt will be paid off if repayments continue at the specified amount and interest rate <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Number of EMIs**: The total number of installments required to pay off the debt <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Managing Repayment Schedules and Categories

The tracker allows for flexible [[setting_up_repayment_schedules | setting up repayment schedules]] and categories:

*   **Adding New Categories**: Users can add new repayment periods (e.g., weekly, quarterly) by clicking an "add a group" button and specifying the period <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Existing schedules like annual and monthly payments are pre-added <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Hidden groups for quarterly and weekly repayments can also be accessed <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Moving Debts Between Categories**: Debts can be moved to any repayment schedule by simply dragging the line item <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This action automatically updates the repayment schedule and related calculations <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Adding and Editing Loan Details

*   **Adding New Debt**: A "pay debt amount" button allows users to quickly add a new debt payment to the schedule based on the current date, after which details can be typed in <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Editing Existing Loans**: To edit existing loan details, users can click on the debt field and type in desired changes, which will automatically update across all related columns and descriptions <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. This is part of [[setting_up_loan_details_database | setting up loan details database]].

## Debt Payoff Progress Section

This section provides a summary of the overall debt payoff status <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. It reflects:

*   **Total Repaid Amount**: The sum of all loan amounts that have been repaid <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This figure is updated automatically based on installments recorded <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Net Payoff in Percentage**: The percentage of the total debt that has been paid off <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Debt Free By**: A quick reference to the overall debt-free date <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Interest Amount**: The total interest paid so far <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Principal Amount**: The total principal amount repaid <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Every debt repayment is split into interest and principal amounts <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Transaction Section (Paid Installments)

This section details all debt payments made to date <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. It is bifurcated by month, with the latest month appearing at the top <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

Key features include:

*   **Payment Status**: A checkbox indicates if an amount has been paid. Ticking or unticking this box updates the "paid installment" or "unpaid column" sections automatically <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Payment Date**: Users can input the specific date of payment <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Loan Details Selection**: Users can select the specific loan for which the payment is being made <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **EMI Amount of Payment**: The amount of the installment paid <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Next Repayment Schedule**: The system automatically calculates the next repayment date based on the loan's payment frequency <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. For example, a monthly student loan payment made on September 30 will show October 30 as the next payment date <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. Similarly, for an annual loan, like a [[mortgage_payment_tracking | home loan]], a payment made on September 27, 2023, will show September 27, 2024, as the next repayment date <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. This feature can be used for [[managing_notifications_and_repayment_schedules_in_notion | managing notifications and repayment schedules]].

### Automated Updates

All data within the tracker updates automatically as details are added or changed <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. For instance, changing an EMI amount in the transaction section instantly updates the total repaid amount and other summary metrics in the debt payoff progress section <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This continuous updating ensures effective [[tracking_debt_repayments_and_progress | tracking debt repayments and progress]].