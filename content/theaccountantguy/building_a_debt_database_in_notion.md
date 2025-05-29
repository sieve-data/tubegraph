---
title: Building a debt database in Notion
videoId: WV13JDi5DMY
---

From: [[theaccountantguy]] <br/> 

To effectively track and manage debt payments towards becoming debt-free, a [[creating_a_notion_debt_tracker | Notion debt tracker]] requires several interconnected databases <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. One of the foundational components is the Debt Database <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Purpose of the Debt Database

The Debt Database serves as the central repository for all personal debt information <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. It's designed to list and detail each type of debt a user has <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

This database includes key financial parameters for each debt, such as <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>:
*   The total loan amount <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>
*   Interest rate <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   Minimum payment required <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>
*   Any additional repayment made initially <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>
*   The initial repayment date <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>
*   The projected date by which the debt will be fully repaid <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>

## Key Properties and Their Functions

The Debt Database is structured with several properties (columns in Notion) to capture comprehensive information for each loan <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>:

### Debt Categories
The database accommodates various types of debts <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>:
*   Student Loan <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>
*   Credit Card <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>
*   Car Loan <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>
*   Personal Loan <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>
*   Home Loan <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>
*   Other Loan <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>

These are typically specified in the "Name" property, which is a default property when [[creating a database in Notion | creating a database]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Financial Details (Number Properties)
*   **Loan Amount**: The total amount of the loan against the debt <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This is a number property, often specified in US dollars <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Interest Rate**: The annual interest rate for each debt <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This is a number property, specified in percentage format <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Minimum Payment**: The minimum monthly payment required for each debt <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This is a number property, also specified in US dollars <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Additional Repayment**: Any additional amount paid during the first installment, such as a down payment <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. This is a number property <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Date Property
*   **Initial Repayment Date**: The date when the first installment for the debt was made <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This is a date property <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Calculated Properties (Formulas)
*   **Interest Rate Per Month (I value)**: Calculated by dividing the `Interest Rate` (per annum) by 12 <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Debt Free Period**: A formula property that calculates the estimated time in months it will take to become debt-free from the initial repayment date <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Expected Debt Free By**: Calculates an estimated debt-free date by adding the `Debt Free Period` to the `Initial Repayment Date` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Net Loan Outstanding Amount**: Calculates the net debt payable before the first installment date <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This is derived by deducting the `Additional Payment` from the `Loan Amount` <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This value serves as the opening balance for the `Loan Details` database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## Integration with Other Databases

The Debt Database is crucial as it feeds into other essential databases within the [[creating_a_notion_debt_tracker | Notion debt tracker]]:
*   **Loan Details Database**: The `Net Loan Outstanding Amount` from the Debt Database becomes the opening balance for the first month's payment in the `Loan Details` database <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Debt Overview Database**: Information from the Debt Database is rolled up or referenced in the `Debt Overview` database to provide a summary of each debt <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Summary of Debt Database**: Totals and percentages are pulled from the Debt Overview database to provide a high-level summary <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Total Debt Database**: Aggregates all debt values to show combined totals <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.