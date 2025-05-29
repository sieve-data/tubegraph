---
title: Debt payment tracking and reporting
videoId: r6C5tHcfAes
---

From: [[theaccountantguy]] <br/> 
A personal finance tracker developed in a Google Sheet includes a dedicated section for [[tracking_loan_details_and_repayments | debt payment tracking and reporting]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This feature allows users to monitor total debts, the amount of interest and principal paid, and the outstanding loan balance <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Debt Payment Report Setup
The [[debt_overview_and_payment_schedule_setup | debt payment report]] requires specific information to be entered for accurate tracking <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>:

*   **Debt Information:** Details about the debt itself <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Loan Amount:** The total amount of the loan taken <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Interest Rate:** The applicable interest rate for the loan <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Minimum EMI Payment:** The minimum equated monthly installment to be paid <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Additional Down Payment:** Any extra payment made at the time of obtaining the loan <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Initial Repayment Date:** The first date any repayment was made towards the loan <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

Once these initial details are provided, the tracker automatically calculates the loan outstanding at the beginning of the period <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### Tracking Debt Payment Transactions
On the right side of the debt payment report, users can [[managing_debt_payment_transactions | specify transactions]] <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>:

1.  **Date:** Enter the payment date <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
2.  **Debt Selection:** Choose the specific debt from a dropdown list <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
3.  **EMI Amount:** Specify the EMI amount paid <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

The sheet then automatically computes the interest value, principal value, and the updated loan outstanding for each payment <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. As subsequent installments are paid, the outstanding loan amount continuously reduces <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

### Debt Payment Analysis and Overview
The debt payment report provides a comprehensive overview and analysis of all debts <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>:

*   **Debt-Free Date:** Estimates when the debt will be cleared if minimum repayments continue <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **Repayment Breakdown:** Shows how much interest and principal have been repaid so far <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Total Repayment Value & Percentage:** The sum of all repayments and the percentage of the total loan repaid <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   **Visual Progress:** A graph indicates the amount paid (green bar) versus the amount remaining (black bar) for each debt <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Summary Metrics:**
    *   Total loan amount <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
    *   Total amount repaid (broken down by principal and interest) <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
    *   Amount outstanding (calculated as loan amount less repaid amount) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
    *   Total repayment in percentage <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
    *   Number of loans taken <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
    *   Total minimum EMI to be paid across all combined loans <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

This analysis provides a quick understanding of how much has been paid and how much is still outstanding for each loan <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

### Dynamic Reporting Section
The reporting section is a core part of the personal finance tracker, allowing users to dynamically view financial data <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Users can select "debt details" from a dropdown <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. By choosing a specific month, the report will automatically update to reflect the debt details for that period <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. This dynamic feature allows for quick analysis of personal finances at a glance <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.