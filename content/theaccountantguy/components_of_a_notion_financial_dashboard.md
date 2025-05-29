---
title: Components of a Notion financial dashboard
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

A Notion financial dashboard, specifically demonstrated through a net worth tracker, is structured to provide a comprehensive overview of financial standing <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This type of dashboard helps track progress towards financial goals and understand the composition of assets and liabilities <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Dashboard Sections

The primary dashboard for a net worth tracker includes several key sections:

*   **Summary Section** This section provides high-level financial metrics <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. It calculates:
    *   Net worth goal amount <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   Current total net worth <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
    *   Amount still needed to reach the net worth goal <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
    *   Total net worth growth since January <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
    *   Percentage of net worth achieved relative to the targeted amount <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
    *   This section is linked to the net worth goal database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Monthly Net Worth Overview** This section provides a detailed monthly breakdown <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, specifying:
    *   Total assets for each month <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    *   Total liabilities for each month <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   Net worth for the month <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   Change in net worth for the month <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
    *   This overview is linked to the net worth database and also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Breakdowns of Assets and Liabilities** These sections offer detailed insights into financial components:
    *   **Assets Breakdown**: Shows individual assets classified into up to five categories, their respective amounts, and their proportion to total assets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This is linked to the assets breakdown database <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   **Liabilities Breakdown**: Specifies up to four types of liabilities, their corresponding amounts, and their proportion to the total liabilities <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This is linked to the liabilities breakdown database <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
    *   Both breakdown sections are displayed using a gallery layout <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

## Underlying Databases

To construct this Notion financial dashboard, five distinct databases are utilized, each serving a specific purpose <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>:

1.  **Assets and Liabilities Database** This database is central for recording all assets and liabilities monthly <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For each entry, it includes:
    *   Asset or liability description, with five types of assets specified <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   Opening balance (a number property) at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   Amount reflecting additions or deletions for the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Closing balance, calculated as opening balance plus the amount changed during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   The closing balance from one month must be manually copied as the opening balance for the subsequent month for all assets and liabilities <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
2.  **Assets Breakdown Database** This database itemizes assets and their individual proportions to the total <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. It lists the same five asset categories as in the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. The total amount for each asset from all months combined is "rolled up" from the earlier database using a formula <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. It also calculates the total asset value, rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>, and the percentage of each asset relative to the combined total assets <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
3.  **Liabilities Breakdown Database** Similar to the assets breakdown, this database details four types of liabilities and their respective amounts and proportions <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
4.  **Net Worth Database** This database calculates key financial figures for each month <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
    *   Total assets, derived from the closing balance of assets each month <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   Total liabilities, derived from the closing balance of liabilities each month <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   Net worth, calculated by deducting liabilities from assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   Change in net worth, calculated by deducting the opening net worth from the closing net worth <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. All amounts in this database are rolled over from the Assets and Liabilities Database <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
5.  **Net Worth Summary Database** This final database summarizes the financial data, pulling values from the other databases to calculate the net worth goal, total net worth, amount to goal, total growth, and the percentage of net worth achieved against the target <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

By integrating these databases, a user can effectively create a comprehensive [[notion_finance_templates_and_databases | Notion dashboard for freelancers]] or for personal finance management, providing a clear overview of their financial health <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. This detailed approach allows for [[using_notion_for_personal_finance_management | tracking income and expenses with a Notion dashboard]] and achieving a robust [[using_summary_and_financial_overview_features_in_notion | financial overview in Notion]].