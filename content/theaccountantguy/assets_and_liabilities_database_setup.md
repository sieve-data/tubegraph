---
title: Assets and Liabilities Database Setup
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

This article details the process of building a net worth tracker using Notion, specifically focusing on the setup of various databases required for comprehensive financial tracking <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The tracker includes a summary section for net worth goals, current net worth, amount needed to reach the goal, total growth, and the percentage of the goal achieved <a class="yt-timestamp" data-t="00:00:35">[00:00:52]</a>. It also provides a monthly net worth overview, [[assets_and_liabilities_breakdown | breakdown of assets]], and [[assets_and_liabilities_breakdown | liabilities breakdown]] <a class="yt-timestamp" data-t="00:00:55">[00:01:24]</a>.

To build this net worth tracker, five types of databases are required <a class="yt-timestamp" data-t="00:01:26">[00:01:30]</a>. Each database has its own specific requirements <a class="yt-timestamp" data-t="00:01:31">[00:01:33]</a>.

## Database Components

### Assets and Liabilities Database

This database serves as the primary record for all assets and liabilities for each specific month <a class="yt-timestamp" data-t="00:01:40">[00:01:46]</a>.

> [!INFO] Fields:
> *   **Asset/Liability Description**: Specifies types of assets (e.g., five types mentioned) <a class="yt-timestamp" data-t="00:01:49">[00:01:53]</a>.
> *   **Opening Balance**: A number property indicating the balance at the start of the month <a class="yt-timestamp" data-t="00:01:55">[00:01:59]</a>.
> *   **Amount**: Shows additions or deletions of assets/liabilities for the specific period <a class="yt-timestamp" data-t="00:02:00">[00:02:04]</a>.
> *   **Closing Balance**: Calculated as the opening balance plus the amount during the month <a class="yt-timestamp" data-t="00:02:06">[00:02:10]</a>.

> [!NOTE] Data Maintenance:
> The closing balance of each month for all assets and liabilities must be copied and pasted onto the opening balance of the subsequent month <a class="yt-timestamp" data-t="00:02:16">[00:02:25]</a>.

### Assets Breakdown Database

This database provides a breakup of all assets and their individual proportions to the total amount <a class="yt-timestamp" data-t="00:02:42">[00:02:46]</a>.

> [!INFO] Details:
> *   It lists the same five assets created in the [[assets_and_liabilities_breakdown | Assets and Liabilities Database]] <a class="yt-timestamp" data-t="00:02:48">[00:02:50]</a>.
> *   The total amount for each asset is rolled up from the earlier database, combining data from all months <a class="yt-timestamp" data-t="00:02:50">[00:02:56]</a>.
> *   The total assets value is calculated and rolled up from another database using a formula <a class="yt-timestamp" data-t="00:03:02">[00:03:08]</a>.
> *   The percentage of each asset relative to the total value of all assets combined is calculated and represented visually <a class="yt-timestamp" data-t="00:03:13">[00:03:20]</a>.

### Liabilities Breakdown Database

Similar to the assets breakdown, this database details the four types of liabilities and their corresponding amounts and proportions to the total <a class="yt-timestamp" data-t="00:01:16">[00:01:24]</a> <a class="yt-timestamp" data-t="00:03:20">[00:03:24]</a>.

### Net Worth Database

This database calculates key financial metrics for each subsequent month <a class="yt-timestamp" data-t="00:03:32">[00:03:40]</a>.

> [!INFO] Calculations:
> *   **Total Assets**: Considers the closing balance of assets from the [[assets_and_liabilities_breakdown | Assets and Liabilities Database]] <a class="yt-timestamp" data-t="00:03:42">[00:03:46]</a>.
> *   **Total Liabilities**: Considers the closing balance of liabilities from the [[assets_and_liabilities_breakdown | Assets and Liabilities Database]] <a class="yt-timestamp" data-t="00:03:46">[00:03:50]</a>.
> *   **Net Worth**: Calculated by deducting liabilities from the assets for the month <a class="yt-timestamp" data-t="00:03:50">[00:03:54]</a>.
> *   **Change in Net Worth**: Determined by deducting the closing net worth from the opening net worth of assets and liabilities <a class="yt-timestamp" data-t="00:03:56">[00:04:02]</a>.

> [!NOTE] Data Source:
> All amounts in this database are rolled over from the [[assets_and_liabilities_breakdown | Assets and Liabilities Database]] <a class="yt-timestamp" data-t="00:04:06">[00:04:10]</a>.

### Net Worth Summary Database

This final database summarizes all the information gathered from the preceding databases <a class="yt-timestamp" data-t="00:04:13">[00:04:16]</a>.

> [!INFO] Summary Metrics:
> *   Net worth goal <a class="yt-timestamp" data-t="00:04:19">[00:04:21]</a>
> *   Total net worth amount <a class="yt-timestamp" data-t="00:04:21">[00:04:22]</a>
> *   Amount to goal <a class="yt-timestamp" data-t="00:04:22">[00:04:23]</a>
> *   Total growth in net worth <a class="yt-timestamp" data-t="00:04:23">[00:04:25]</a>
> *   Percentage of the net worth to the targeted net worth <a class="yt-timestamp" data-t="00:04:26">[00:04:27]</a>

All values are pulled from the previously discussed databases and totaled as desired <a class="yt-timestamp" data-t="00:04:29">[00:04:33]</a>.

## Primary Dashboard Integration

The primary dashboard of the net worth tracker integrates and displays data from these databases <a class="yt-timestamp" data-t="00:04:46">[00:04:50]</a>.

*   **Summary Section**: Displays the net worth goal, total net worth, amount to goal, total growth, and percentage of net worth goal <a class="yt-timestamp" data-t="00:04:48">[00:04:56]</a>. This is linked to the Net Worth Goal database and displayed in a gallery layout <a class="yt-timestamp" data-t="00:04:57">[00:05:02]</a>.
*   **Monthly Net Worth Overview**: Specifies total assets, total liabilities, net worth, and change in net worth <a class="yt-timestamp" data-t="00:05:02">[00:05:09]</a>. It is linked to the Net Worth database and set out in a gallery layout <a class="yt-timestamp" data-t="00:05:09">[00:05:13]</a>.
*   **Assets Breakdown and Liabilities Breakdown**: These sections are linked to their respective databases and are also set out in a gallery layout <a class="yt-timestamp" data-t="00:05:15">[00:05:22]</a>.