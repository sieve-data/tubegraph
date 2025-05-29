---
title: Using Google Sheets for Personal Finance
videoId: r6C5tHcfAes
---

From: [[theaccountantguy]] <br/> 

S. Biswal, also known as "The Accountant Guy," has developed a [[personal_finance_tracking | personal finance tracker]] using [[using_google_sheets_for_tracking | Google Sheets]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This comprehensive tool is designed to help individuals track and manage their finances, although it can also be adapted for business use <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

The tracker is organized into five primary tabs, in addition to an instructions tab <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:
1.  Monthly Budget <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
2.  [[investment_dashboard_in_google_sheets | Investment Dashboard]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>
3.  Sinking Fund Analysis <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
4.  Debt Payment Report <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>
5.  Report Section (Dynamic Reporting Presentation) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

---

## Monthly Budget Tab

The Monthly Budget tab allows users to set monthly budgets for both income and expenses <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It features an "Expenses Overview" on the left and an "Income Overview" on the right <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Highlighted cells are automatically computed and should not be edited manually <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Expenses
Users input expenses, such as gas, Wi-Fi, and phone bills, for specific months <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The budgeted amount for each expense is set here <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. As actual expenses are entered in the transactions area, the sheet calculates:
*   Incurred expenses <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Difference between budgeted and actual amounts <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>
*   Whether the user is "under budget" or "over budget" <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

For example, if a budgeted amount for phone bills in March is $1,400, and an actual expense of $1,300 is entered, the sheet shows the user is "under budget" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. If $1,500 is entered, it reflects "over budget" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Income
The income section operates on similar principles, allowing users to set targeted income amounts for respective months <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Transactions and Overviews
The transaction area includes columns for date, details (with a dropdown for income or expense categories), and amount <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

The sheet provides dynamic overviews:
*   **Expense Overview**: Shows total budgeted amount, total incurred expenses, and the difference <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. A bar graph visually represents budgeted vs. actual expenses <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Income Overview**: Displays total targeted income, actual income achieved, and the difference <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. A graph compares targeted and actual income <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

This tab is useful for [[budgeting_with_spreadsheets | budgeting]] and tracking all bills, subscriptions, and income <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

---

## Investment Dashboard

The [[investment_dashboard_in_google_sheets | Investment Dashboard]] is fully dynamic <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Users only need to enter the stock symbol, number of shares, and purchase price <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. All other values update automatically in real-time as stock market trading occurs <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

The dashboard provides a quick representation of:
*   Market value of held symbols <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>
*   Cost and market value analysis <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>
*   Growth and symbol representation <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>
*   Portfolio value <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
*   Portfolio gain (absolute and percentage) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>
*   Dividend income <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
*   Total holdings <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>

---

## Sinking Fund Analysis

This tab helps users manage "sinking funds" with a similar approach to the monthly budget <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Users specify:
*   Name of the sinking fund <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>
*   Goal amount for each fund <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>
*   Desired monthly contribution <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>
*   Any starting amount already saved <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>

Based on entries, the sheet calculates:
*   Amount saved so far <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>
*   Amount remaining to save <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>
*   Total progress percentage (savings divided by goal amount) <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>
*   Estimated completion date and months to completion based on monthly contributions <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

A quick graph on the right visually represents the total savings made (green bar) versus the amount still needed to save (black bar) for each fund <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

---

## Debt Payment Report

This section helps manage debts by allowing users to input debt information <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>:
*   Loan amount <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
*   Interest rate <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
*   Minimum EMI (Equated Monthly Installment) payment <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>
*   Additional down payment made <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>
*   Initial repayment date <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>

The sheet automatically computes:
*   Loan outstanding at the beginning <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
*   Debt-free date (if minimum payments are maintained) <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>
*   Interest repaid so far <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>
*   Principal repaid <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>
*   Total repayment value <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>
*   Repayment percentage <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>

For each payment entry, the sheet automatically calculates the interest and principal components of the EMI, and updates the loan outstanding <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

An overview graph shows the amount paid in green and the amount remaining for repayment <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. The tab also summarizes total loan amount, total repaid amount (broken into principal and interest), outstanding amount, total repayment percentage, number of loans, and combined minimum EMI <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

---

## Reporting Section

The Reporting section is a dynamic presentation tool that allows users to analyze their finances at a glance <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Users can select different categories from a dropdown menu, such as expense, income, sinking fund, or debt details <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. By selecting a specific month, the reports dynamically update to reflect the corresponding data <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.

This section provides:
*   Total values for the selected category and month <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>
*   A quick pie chart reflecting the total division or breakdown of the selected data <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

This feature is highly dynamic, providing immediate insights into financial trends and helping users analyze their finances efficiently <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

---

This [[track_income_and_expenses_in_google_sheets | Google Sheets]]-based [[personal_finance_tracking | personal finance tracker]] combines budgeting, investment analysis, sinking fund management, and debt payment tracking into one dynamic tool, providing a comprehensive solution for managing finances <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. For customization requests, S. Biswal can be reached at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.