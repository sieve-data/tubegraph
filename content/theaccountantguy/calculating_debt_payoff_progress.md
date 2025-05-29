---
title: Calculating debt payoff progress
videoId: p7aozLHRzq0
---

From: [[theaccountantguy]] <br/> 

The debt payment tracker includes a "Debt Payoff Progress" section to provide a comprehensive summary of all loans and their repayment status <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. This section automatically updates as new debt payment details are added or modified <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>, reflecting changes immediately <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.

## Key Metrics Tracked

The Debt Payoff Progress section integrates several crucial metrics for [[managing_debt_and_liabilities | managing debt and liabilities]] and assessing repayment status:

*   **Total Amount Repaid**
    *   This metric displays the cumulative sum of all loan installments that have been paid <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
    *   The amount is calculated from the installment payments recorded in the [[managing_debt_payment_transactions | transaction]] section <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.
    *   Whenever an EMI for any loan is paid, this total is automatically updated <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
    *   For example, if payments of $2,000 and $500 are made for a student loan, the total reflected is $2,500 <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. Changing a payment amount to $3,000 would update the total to $3,500 (3,000 + 500) <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.

*   **Net Payoff in Percentage**
    *   This percentage indicates how much of the total outstanding debt has been paid off so far <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

*   **Debt-Free By Date**
    *   This field provides a quick reference to the projected date by which a particular debt will be paid off, assuming repayments continue at the specified amount and interest rate <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. This date is also visible in the [[debt_overview_and_payment_schedule_setup | Debt Overview]] section <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>.

*   **Interest Amount Paid**
    *   This shows the total interest paid as part of the overall repayments made <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.
    *   Every payment towards a debt is split into an interest amount and a principal amount <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>, with the interest component contributing to this total <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

## How Progress is Updated

[[debt_payment_tracking_and_reporting | Debt payoff progress]] is dynamically calculated and updated based on information entered in the following sections:

*   **[[debt_overview_and_payment_schedule_setup | Debt Overview Section]]**: Initial loan amounts, EMI amounts, interest rates, and initial repayment dates are defined here <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. Changes to existing loan details are automatically reflected across all related calculations <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.
*   **Transaction Section**: This is where users record individual debt payments <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>. Marking an installment as "paid" or entering the EMI amount directly impacts the total repaid amount and subsequent progress calculations <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Adding a new debt payment entry will automatically update the overall progress <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.