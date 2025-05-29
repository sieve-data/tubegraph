---
title: Setting Up Loan Details Database
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 
The [[database_setup_for_notion_bills_tracker | Notion Debt Tracker]] requires five databases, one of which is the Loan Details database <a class="yt-timestamp" data-t="00:02:33"></a>. This database provides specific details related to a loan's repayment, ultimately showing the outstanding balance <a class="yt-timestamp" data-t="00:02:36"></a>.

### Purpose and Connection

The Loan Details database is where you fill in specific repayment information for each debt listed in the Debt database <a class="yt-timestamp" data-t="00:06:13"></a>. The "Net Loan Outstanding Amount" from the Debt database serves as the opening balance for the first month's payment in the Loan Details database <a class="yt-timestamp" data-t="00:04:41"></a>. For subsequent months, the closing balance of the previous month is copied to the current month's opening balance <a class="yt-timestamp" data-t="00:07:05"></a>.

### Database Properties

The Loan Details database includes several key properties:

*   **Installment Number** <a class="yt-timestamp" data-t="00:06:21"></a>
    *   Specifies the number of installments paid against a debt <a class="yt-timestamp" data-t="00:06:23"></a>.
*   **Date of Payment of Installment** <a class="yt-timestamp" data-t="00:06:29"></a>
    *   Specifies the date of debt repayment for each installment, utilizing a date property <a class="yt-timestamp" data-t="00:06:31"></a>.
*   **Category of Loan** <a class="yt-timestamp" data-t="00:06:39"></a>
    *   Relates to the Debt Overview database <a class="yt-timestamp" data-t="00:06:41"></a>.
    *   Specifies one of six categories of debt being repaid (e.g., student loan, credit card, car loan, personal loan, home loan, other loan) <a class="yt-timestamp" data-t="00:06:46"></a>.
*   **Opening Balance of Debt** <a class="yt-timestamp" data-t="00:06:55"></a>
    *   Represents the debt amount prior to repayment <a class="yt-timestamp" data-t="00:06:57"></a>.
    *   The first month's payment amount is the "Net Loan Outstanding" from the Debt database <a class="yt-timestamp" data-t="00:07:00"></a>.
    *   For subsequent months, the closing balance of the previous month is copied to the current month's opening balance <a class="yt-timestamp" data-t="00:07:05"></a>.
*   **Payment Amount** <a class="yt-timestamp" data-t="00:07:21"></a>
    *   The minimum amount paid each month <a class="yt-timestamp" data-t="00:07:23"></a>.
    *   For the first installment, it includes the minimum amount and any additional payment (e.g., down payment) <a class="yt-timestamp" data-t="00:07:26"></a>.
    *   For subsequent months, it equals the minimum amount <a class="yt-timestamp" data-t="00:07:31"></a>.
*   **Interest Calculation** <a class="yt-timestamp" data-t="00:07:38"></a>
    *   A formula property that specifies the interest amount paid per installment <a class="yt-timestamp" data-t="00:07:38"></a>.
    *   Calculated as `Opening Balance × (Interest Rate / 12)` <a class="yt-timestamp" data-t="00:07:43"></a>.
*   **Principal Value** <a class="yt-timestamp" data-t="00:07:48"></a>
    *   A formula property calculated as `Payment Amount - Interest Amount` <a class="yt-timestamp" data-t="00:07:48"></a>.
*   **Closing Balance** <a class="yt-timestamp" data-t="00:07:56"></a>
    *   A formula property equal to `Opening Balance - Principal Amount` for each month <a class="yt-timestamp" data-t="00:07:58"></a>.
*   **Payment Status Checkbox** <a class="yt-timestamp" data-t="00:08:02"></a>
    *   Reflects whether the payment is paid or not paid <a class="yt-timestamp" data-t="00:08:04"></a>.
    *   Clicking the checkbox updates the payment status <a class="yt-timestamp" data-t="00:08:07"></a>.
*   **Amount Paid against Total Amount, Interest, and Principal** <a class="yt-timestamp" data-t="00:08:12"></a>
    *   The total repayment is calculated using a formula that considers when an amount is paid and the checkbox is ticked <a class="yt-timestamp" data-t="00:08:21"></a>.
    *   This logic is applied for interest and principal values as well <a class="yt-timestamp" data-t="00:08:29"></a>.
    *   The amounts repaid against the total, interest, and principal are summed up at the bottom of the database <a class="yt-timestamp" data-t="00:08:42"></a>.