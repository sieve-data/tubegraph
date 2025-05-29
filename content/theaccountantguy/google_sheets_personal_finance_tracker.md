---
title: Google Sheets personal finance tracker
videoId: r6C5tHcfAes
---

From: [[theaccountantguy]] <br/> 

This article outlines the features and functionality of a [[personal_finance_tracking_spreadsheet | personal finance tracker]] developed in Google Sheets, designed for individual and potentially business purposes <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. It combines various aspects of [[tracking_income_and_expenses | tracking income and expenses]], investments, savings, and debt management into a single, dynamic tool <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

## Overview of Tabs <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>

The tracker consists of five main tabs, in addition to an instructions tab <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:
*   **Monthly Budget Tab** <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   **Investment Dashboard** <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   **Sinking Fund Analysis** <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   **Debt Payment Report** <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>
*   **Report Section** <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

## Monthly Budget Tab <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>

This tab allows users to set monthly budgets for both expenses and income <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

### Expenses Overview <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
Users can input their expenses, such as gas, Wi-Fi, and phone bills <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Dates can be set by double-clicking to select a specific day within a month <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The budgeted amount for each expense can be specified; for example, setting a budget of $1,400 for phone bills in March <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The tracker automatically calculates the actual incurred expenses, the difference between budgeted and actual amounts, and indicates whether the user is "under budget" or "over budget" <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. For instance, if a phone bill entry is $1,300 against a $1,400 budget, it shows "under budget" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. If an entry is $1,500, it reflects "over budget" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Income Section <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>
Similar to expenses, users can set targeted income amounts for respective months <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. As income entries are made in the transactions area, the overview automatically updates <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Transactions Area <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>
This section allows users to record dates, details of expenses (e.g., phone bills), and the amounts <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. A dropdown menu provides a list of all expense and income items for selection <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Dynamic Overview <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>
The tab provides a dynamic overview of expenses and income <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>:
*   **Expenses:** Shows total budgeted amount, total incurred expenses, and the difference <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. A graphical presentation compares budgeted (left bar) and actual (right bar) expense amounts <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Income:** Displays total targeted income, actual income achieved, and the positive difference <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. A graph compares targeted (left bar) and actual (right bar) income <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Investment Dashboard <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>

This dashboard is fully dynamic and updates in real-time <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Users only need to enter the stock symbol, number of shares, and purchase price <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. For example, entering "Apple" as a symbol automatically updates the price and graph in real-time <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. If 15 shares are purchased at $200, all other related calculations are automatically updated <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

Key metrics displayed include <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>:
*   Market value and cost analysis <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
*   Growth and symbol representation <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>
*   Portfolio value <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
*   Portfolio gain (in absolute value and percentage) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>
*   Dividend income and total holdings <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>

## Sinking Fund Analysis <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>

Similar to the monthly budget, this section helps manage specific savings goals <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Users specify:
*   The syncing funds to be created <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>
*   A goal amount for each fund <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>
*   Monthly contributions <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>
*   Any starting amount already saved <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>

For example, a home renovation fund might have a $5,000 target, a $400 monthly contribution, and a $2,800 starting fund <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. The tracker then shows <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>:
*   Amount saved so far <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>
*   Amount still needed to save <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>
*   Total progress (savings divided by goal amount) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>
*   Estimated completion date and months if contributions continue at the set rate <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>

Users can input the date, select the fund from a dropdown, and enter the contribution amount <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. A graph visually represents total savings (green bar) versus savings still needed (black bar) <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Debt Payment Report <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>

This section helps users manage and track their debts <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. Users input:
*   Debt information <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>
*   Loan amount taken <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
*   Interest rate <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>
*   Minimum EMI (Equated Monthly Installment) payment <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>
*   Additional down payment made <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>
*   Initial repayment date <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>

The tracker automatically calculates <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>:
*   Loan outstanding at the beginning <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
*   Estimated debt-free date if minimum repayments are maintained <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>
*   Interest repayment made so far <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>
*   Principal repaid <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>
*   Total repayment value and its percentage <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>

Users can specify the date, choose the debt from a dropdown, and enter the EMI amount <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. The sheet automatically computes the interest value, principal value, and remaining loan outstanding <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. For example, a $3,850 student loan payment might reflect $166.37 as interest and $3,683.63 as principal <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

The overview displays <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>:
*   Amount paid (green) and amount left (black) <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>
*   Total loan amount, total repaid amount (broken down by principal and interest) <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>
*   Outstanding amount, total repayment percentage <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>
*   Number of loans and combined minimum EMI <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>

## Report Section <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>

This is a dynamic reporting presentation <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Users can select from a dropdown list of categories such as expense, income, sinking fund, and debt details <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. Investment details are viewed directly in the Investment Dashboard and are not part of this report section <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

Users can select a specific month to see updated values and analysis <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. For instance, selecting "income" for January shows an income of $4,150, along with a pie chart reflecting the total division of income <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Changing the month or category (e.g., to "expense" or "sinking fund") dynamically updates the displayed analysis <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

## Customization and Support

The tracker is described as entirely dynamic <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. For further customization or assistance beyond the provided template, users can contact the creator at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. The template is available for immediate download and use <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.