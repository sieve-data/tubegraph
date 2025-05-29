---
title: Understanding Debt Overview and Summary
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

A crucial component of a Notion debt tracker is the ability to provide a comprehensive overview and summary of all outstanding debts. This functionality helps users monitor their progress towards becoming debt-free <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Summary Section

The tracker includes a summary section that aggregates key financial figures. This section displays:
*   The total loan amount <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
*   The total amount repaid <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   The total interest repaid <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   The repayment in percentage <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

This summary is linked to the [[total_debt_section | total debt database]] <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## Debt Overview Section

The debt overview section provides a detailed breakdown of different debt categories. It includes:
*   Student loan <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
*   Credit card <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Car loan <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Personal loan <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
*   Home loan <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   Other loans <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

Under each debt category, the following details are presented:
*   Total loan amount <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   The estimated date of being debt-free <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>

This section updates automatically as payments are recorded, reflecting the amount repaid, interest repaid, and repayment percentage <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The debt overview section is linked to the [[summary_of_debt_database | Summary of Debt database]] <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## Databases for Overview and Summary

To build this tracker, five databases are required, including specific ones for overview and summary purposes <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### Debt Overdue Database

This database provides a quick overview of each debt <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. It includes properties such as:
*   Loan amount <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>
*   Principal repaid <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>
*   Interest repaid <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>
*   Outstanding amount <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>
*   Repayment percentage <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
*   Debt-free date <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>

In the Notion setup, the loan amount is derived as a roll-up from the [[loan_details_database | Loan Details database]] <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Similarly, the total amount repaid, total principal repaid, and total interest repaid are also roll-up values from the [[loan_details_database | Loan Details database]] <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. The outstanding amount is calculated by deducting the principal repaid from the loan amount <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>, and the repayment in percentage is the ratio of principal repaid to the total loan amount <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Summary of Debt Database

This database calculates and displays summary figures for each type of debt <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. It shows:
*   Total loan amount <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>
*   Total amount repaid <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   Total interest repaid <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
*   Repayment in percentage <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>
*   The debt-free date <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>

These figures are pulled as roll-up values from the [[debt_overdue_database | Debt Overview database]] <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### Total Debt Database

The total debt database aggregates the combined value of all debts <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. It reflects:
*   The total loan amount <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
*   The total amount repaid <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
*   The total interest repaid <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>
*   The repayment in percentage for all combined debts <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>

Similar to the [[summary_of_debt_database | Summary of Debt database]], values in this database are rolled up from the [[debt_overdue_database | Debt Overview database]] to calculate the respective totals <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. This database serves as the foundation for the main dashboard's summary section <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.