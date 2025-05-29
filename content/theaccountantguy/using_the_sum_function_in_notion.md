---
title: Using the SUM function in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[calculating_sum_of_a_column_in_notion | calculate the sum of a column]] in Notion databases using an external tool, `myformulagen.com`, to achieve [[using_excelstyle_formulas_in_notion | Excel-like formulas]] functionality. This method allows for [[calculating_custom_data_summaries_in_notion | custom data summaries]] without relying on Notion's native formulas, relations, or rollups, which can be complex for specific calculations <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Setting Up `myformulagen.com`

To use the `myformulagen.com` tool for [[calculating_sum_of_a_column_in_notion | sum calculations]], you must first establish a connection between Notion and the tool via Notion's API <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a> <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### Obtaining Your Notion API Key

1.  Navigate to `myformulagen.com` <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
2.  Click on "Settings" and then "Get API key" within the tool <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
3.  This will open a new screen to create a personal API key <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
4.  Click "New Integration," provide a name (e.g., "Sum formula key"), select your Notion workspace, and click "Save" <a class="yt-timestamp" data-t="00:02:51">[00:03:07]</a>.
5.  After creation, select the new integration to reveal the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
6.  Click "Show" and then "Copy" to copy the API key <a class="yt-timestamp" data-t="00:03:17">[00:03:24]</a>.
7.  Paste this copied API key into the "Notion API key" field on `myformulagen.com` and click "Save settings" <a class="yt-timestamp" data-t="00:03:26">[00:03:33]</a>.

### Connecting Notion Databases to the API Key

For the tool to access your Notion databases, the page containing them must be connected to the created API key <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

1.  Ensure all relevant databases are located within a single Notion page (e.g., "Sales Dashboard") <a class="yt-timestamp" data-t="00:03:41">[00:03:49]</a>.
2.  On that Notion page, click the three dots (`...`) menu <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
3.  Go to "Connections" and search for the name of the API key you created (e.g., "Sum formula key") <a class="yt-timestamp" data-t="00:03:51">[00:04:04]</a>.
4.  Select the key and click "Confirm" <a class="yt-timestamp" data-t="00:04:06">[00:04:07]</a>.
5.  This connection ensures that all databases within that page are linked to the API key <a class="yt-timestamp" data-t="00:04:11">[00:04:17]</a>.

## Calculating Sums Using `myformulagen.com`

The tool allows you to specify a source database, a property to sum, and conditions to filter the rows for the sum.

### Example 1: Total Sales Revenue

This example demonstrates [[calculating_sum_of_a_column_in_notion | finding the total sum of a revenue column]] from a sales database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

1.  **Identify Source Database**: In Notion, locate the sales database (e.g., "Sales Database") containing the 'Revenue' column <a class="yt-timestamp" data-t="00:04:27">[00:04:30]</a>.
2.  **Copy Database Link**: Click the six dots (`⋮⋮`) next to the database title and select "Copy link" <a class="yt-timestamp" data-t="00:04:34">[00:04:38]</a>.
3.  **Paste into Tool**: In `myformulagen.com`, paste the database link into the designated field <a class="yt-timestamp" data-t="00:05:07">[00:05:10]</a>. This will enable the "Notion Property" field <a class="yt-timestamp" data-t="00:05:12">[00:05:13]</a>.
4.  **Configure Sum Function**:
    *   Select "Sum" from the function dropdown <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   Choose "Revenue" as the property to sum <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    *   Select "all rows" for the calculation scope <a class="yt-timestamp" data-t="00:05:28">[00:05:30]</a>.
    *   Remove any default second filter if present, as it's not needed for a simple total sum <a class="yt-timestamp" data-t="00:05:48">[00:05:51]</a>.
5.  **Calculate**: Click "Calculate" to see the sum (e.g., $1,537) <a class="yt-timestamp" data-t="00:05:42">[00:05:57]</a>.
6.  **Add to Notion**:
    *   Create a separate Notion database (e.g., "DB for Sales Revenue Total") with a 'Description' and 'Amount' column to display the result <a class="yt-timestamp" data-t="00:00:48">[00:01:32]</a>.
    *   Copy the link of this *target* database <a class="yt-timestamp" data-t="00:07:07">[00:07:11]</a>.
    *   In `myformulagen.com`, click "Add to Notion," paste the target database link <a class="yt-timestamp" data-t="00:07:00">[00:07:26]</a>.
    *   Select the target 'Amount' column and the relevant row (e.g., "Total Sales Revenue") where the sum should appear <a class="yt-timestamp" data-t="00:07:27">[00:07:39]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. The value will populate in Notion <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
7.  **Save Formula**: Click "Save formula" in the tool and give it a descriptive name (e.g., "Total Sales Revenue") <a class="yt-timestamp" data-t="00:08:01">[00:08:11]</a>.

### Example 2: Total Sales Revenue for March

This example [[calculating_sum_of_a_column_in_notion | calculates the sum]] of sales revenue specifically for the month of March <a class="yt-timestamp" data-t="00:09:32">[00:09:35]</a>.

1.  Click "New formula" in `myformulagen.com` <a class="yt-timestamp" data-t="00:09:44">[00:09:47]</a>.
2.  Copy and paste the source sales database link again <a class="yt-timestamp" data-t="00:09:49">[00:09:52]</a>.
3.  Select "Sum" for the 'Revenue' property and "all rows" <a class="yt-timestamp" data-t="00:09:56">[00:10:02]</a>.
4.  **Add Date Filter**:
    *   Add a new condition <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   Select the 'Date' property <a class="yt-timestamp" data-t="00:10:24">[00:10:26]</a>.
    *   Choose "is between" and input the start date (March 1st) and end date (March 31st) <a class="yt-timestamp" data-t="00:10:30">[00:10:39]</a>.
5.  Click "Calculate" to get the filtered sum (e.g., $1,145) <a class="yt-timestamp" data-t="00:10:54">[00:10:55]</a>.
6.  **Add to Notion**: Create a new target database (e.g., "DB for Sales Revenue March 2025") with 'Description' and 'Amount' columns <a class="yt-timestamp" data-t="00:11:05">[00:11:40]</a>.
7.  Copy its link, paste it into the tool, and select the appropriate column ('Amount') and row ('Sales Revenue March 2025') <a class="yt-timestamp" data-t="00:12:50">[00:13:22]</a>.
8.  Click "Save to Notion" and then save the formula with a descriptive name <a class="yt-timestamp" data-t="00:13:41">[00:13:55]</a>.

### Example 3: Total Sales Revenue for Q1 2025 (Software Category)

This example demonstrates [[calculating_sum_of_a_column_in_notion | summing revenue]] with multiple conditions: a date range *and* a specific category <a class="yt-timestamp" data-t="00:14:41">[00:14:46]</a>.

1.  Click "New formula" <a class="yt-timestamp" data-t="00:14:57">[00:14:58]</a>.
2.  Copy and paste the source sales database link <a class="yt-timestamp" data-t="00:15:00">[00:15:04]</a>.
3.  Select "Sum" for the 'Revenue' property and "all rows" <a class="yt-timestamp" data-t="00:15:11">[00:15:23]</a>.
4.  **Add Date Condition**:
    *   Add a condition for the 'Date' property <a class="yt-timestamp" data-t="00:15:32">[00:15:35]</a>.
    *   Select "is between" and set the range from January 1st, 2025, to March 31st, 2025 (representing Q1) <a class="yt-timestamp" data-t="00:15:48">[00:15:57]</a>.
5.  **Add Category Condition (AND)**:
    *   Crucially, select "AND" to combine conditions, meaning both must be true <a class="yt-timestamp" data-t="00:16:05">[00:16:22]</a>.
    *   Click "Duplicate" or the plus sign (`+`) to add another condition <a class="yt-timestamp" data-t="00:16:26">[00:16:31]</a>.
    *   Select the 'Category' property and set it to "is" "Software" <a class="yt-timestamp" data-t="00:16:33">[00:16:45]</a>.
6.  Click "Calculate" to get the result (e.g., $230) <a class="yt-timestamp" data-t="00:17:08">[00:17:13]</a>.
7.  **Add to Notion**: Create a third target database (e.g., "DB for Sales Category Q1 2025") <a class="yt-timestamp" data-t="00:17:56">[00:18:14]</a>.
8.  Copy its link, paste it, and select the 'Amount' column and the specific row (e.g., "Q1 2025 Sales for Software") <a class="yt-timestamp" data-t="00:18:59">[00:19:18]</a>.
9.  Click "Save to Notion" and save the formula <a class="yt-timestamp" data-t="00:19:20">[00:19:39]</a>.

### Refreshing Calculations in Notion

When data in your original Notion sales database changes, the calculated sums in your target databases will not update automatically. You need to manually refresh them <a class="yt-timestamp" data-t="00:08:31">[00:08:45]</a>.

*   In `myformulagen.com`, go to "Saved formulas" <a class="yt-timestamp" data-t="00:08:53">[00:08:55]</a>.
*   Click "Refresh all" to update all saved formulas <a class="yt-timestamp" data-t="00:08:55">[00:09:14]</a>.
*   Alternatively, click the individual refresh icon next to a specific formula to update only that one <a class="yt-timestamp" data-t="00:09:15">[00:09:21]</a>.

## Benefits

This method offers a straightforward way to perform [[calculating_sum_of_a_column_in_notion | sum calculations]] and create [[calculating_custom_data_summaries_in_notion | custom data summaries]] in Notion without needing to understand or apply Notion's built-in formulas, relations, or rollups <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a> <a class="yt-timestamp" data-t="00:22:05">[00:22:13]</a>. It provides a dynamic and easy-to-use alternative for [[using_formulas_for_financial_calculations_in_notion | financial calculations]] and other data aggregation needs, especially when mimicking [[how_to_use_excel_formulas_in_notion | Excel-style formulas]] <a class="yt-timestamp" data-t="00:22:15">[00:22:28]</a>.

<br>
For further queries, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:22:32">[00:22:47]</a>.