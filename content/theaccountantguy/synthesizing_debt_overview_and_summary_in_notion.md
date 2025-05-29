---
title: Synthesizing debt overview and summary in Notion
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A Notion debt tracker can help users monitor debt payments, facilitating the journey to becoming debt-free <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This tracker incorporates sections for a high-level summary and detailed overviews of various debts <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Key Sections

### Overall Summary Section

The primary dashboard of the Notion debt tracker features a summary section that consolidates financial information from all debts <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This section displays:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

This overall summary is directly linked to the "[[managing_finances_with_notion | Total Debt database]]" <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

### Debt Overview Section

Below the overall summary, the "Debt Overview" section provides a breakdown of each debt type <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Common debt categories include student loans, credit cards, car loans, personal loans, home loans, and other loans <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. For each category, the following information is displayed:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
*   The estimated date by which the debt will be paid off <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>

This section is connected to the "[[summary_section_of_notion_bills_tracker | Summary of Debt database]]" <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

### Debt Progressive Payments Section

This section displays progressive due payments, outlining the month of payment, the amount of repayment, and the payment status (paid or not paid) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Checking a box updates the payment status, and this progress is reflected in the "Debt Overview" section for amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This section is linked to individual loans within the "[[setting_up_loan_details_in_notion | Loan Details database]]" <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

## Underlying Databases for Synthesis

Building this minimalistic Notion debt tracker requires five interconnected databases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

1.  **[[setting_up_loan_details_in_notion | Loan Details database]]**: This database tracks individual repayment details, including installment number, date of payment, category of loan, opening balance, payment amount, interest calculation, principal value, closing balance, payment status, and the amount paid against total, interest, and principal <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
2.  **[[building_a_debt_database_in_notion | Debt database]]**: This database lists all types of debt with properties such as loan amount, interest rate, minimum payment, additional repayment, initial repayment date, debt-free period (calculated in months), expected debt-free date, and net loan outstanding amount <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
3.  **[[debt_payment_tracking_using_notion | Debt Overview database]]**: This database provides an overview of each debt, pulling roll-up values from the "[[setting_up_loan_details_in_notion | Loan Details database]]" for total amount repaid, principal repaid, and interest repaid <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. It calculates the outstanding amount (loan amount minus principal repaid) and repayment percentage (principal repaid to total loan amount) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
4.  **[[summary_section_of_notion_bills_tracker | Summary of Debt database]]**: This database calculates the total loan amount, total amount repaid, total interest repaid, repayment in percentage, and the debt-free date for each specific type of debt <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. Figures for these properties are pulled in as roll-up values from the "[[debt_payment_tracking_using_notion | Debt Overview database]]" <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
5.  **[[managing_finances_with_notion | Total Debt database]]**: This database reflects the combined total loan amount, total amount repaid, total interest repaid, and repayment in percentage for all debts <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. Similar to the "[[summary_section_of_notion_bills_tracker | Summary of Debt database]]", it rolls up values from the "[[debt_payment_tracking_using_notion | Debt Overview database]]" to calculate these combined figures <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.