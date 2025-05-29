---
title: Using Excelstyle formulas in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Notion provides [[using_formulas_to_add_numbers_in_notion | inbuilt formulas]] for various calculations, but for more Excel-like functionality and for placing derived values into different databases, external tools can be utilized <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This guide focuses on using the `myformulator.com` tool to perform [[sum_sumif_and_sumifs_functions_in_notion | SUM functions]] without relying on Notion's native formulas, relations, or rollup properties <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Connecting Notion with `myformulator.com`

To begin, you need to connect your Notion workspace to `myformulator.com` via Notion's API <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Step 1: Create an API Key

1.  Log in to `myformulator.com` <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  Navigate to "Settings" and click "Get API key" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
3.  Click "New integration," give it a name (e.g., "Sum Formula Key"), and select your Notion workspace <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
4.  Save the integration, then click on the newly created integration name <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
5.  Reveal and copy the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
6.  Paste this key into the "Notion API Key" field on `myformulator.com` and click "Save settings" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Step 2: Connect Notion Databases/Pages to the API Key

For the tool to access your databases, ensure they are placed within a Notion page that is connected to the API key <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

1.  In Notion, navigate to the page containing your databases (e.g., "Sales Dashboard") <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
2.  Click the three dots in the top right corner of the page <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
3.  Select "Connections," then search for and select the API key you created (e.g., "Sum Formula Key") <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
4.  Confirm the connection <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This links all databases within that page to the API key <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## Calculating Sales Revenue using `myformulator.com`

This tool allows you to perform various [[sum_sumif_and_sumifs_functions_in_notion | SUM functions]] with specific criteria.

### Example 1: Total Sales Revenue

To find the total sales revenue from a "Sales Database" and display it in a separate "Sales Revenue Total" database:

1.  In `myformulator.com`, click "New Formula" <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
2.  Copy the link to your source "Sales Database" (using the six dots menu next to the database title in Notion) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
3.  Paste the link into the "Database URL" field on `myformulator.com` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This will enable the Notion property fields <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
4.  Select the function "SUM" and the property "Revenue" from the dropdowns <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
5.  For "Select Rows," choose "All rows" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. (If a default second filter appears, remove it by clicking the "x" icon) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. The calculated total will be displayed <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
7.  To add this value to your target database, click "Add to Notion" <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
8.  Copy the link to your target "Sales Revenue Total" database and paste it into the "Database URL" field <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
9.  Select the target column (e.g., "Amount") and the target row (e.g., "Total Sales Revenue") where you want the result to appear <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
10. Click "Save to Notion" <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. The value will now be reflected in your Notion database <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
11. To save this configuration for future use, click "Save formula" and give it a name <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Saved formulas can be found under the "Saved Formulas" section <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### [[refreshing_and_updating_formulas_in_notion_databases | Refreshing and Updating Formulas]]

If the source data in Notion changes, the calculated values in your target databases will not automatically update <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. To [[refreshing_and_updating_formulas_in_notion_databases | update them]]:

1.  Go to the "Saved Formulas" section on `myformulator.com` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
2.  Click "Refresh all" to update all saved formulas <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>, or click the individual "Refresh" button next to a specific formula <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Example 2: Sales Revenue for a Specific Month

To calculate total sales revenue for March 2025:

1.  Click "New Formula" <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
2.  Paste the source "Sales Database" URL <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
3.  Select "SUM" for "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
4.  Add a filter: select the "Date" property <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
5.  Choose "is between" and set the range from "March 1" to "March 31" <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
6.  Click "Calculate" to see the sum for that period <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
7.  Create a new target database (e.g., "Sales Revenue March 2025") in Notion <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
8.  Copy the URL of this new database and use "Add to Notion" to place the calculated value into the desired column and row <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
9.  Save the formula (e.g., "Total Sales Revenue for March 2025") <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

### Example 3: Sales Revenue for a Specific Quarter and Category

To find the sales revenue for Q1 2025 specifically for the "Software" category:

1.  Click "New Formula" <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
2.  Paste the source "Sales Database" URL <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
3.  Select "SUM" for "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
4.  Add the first condition: "Date" "is between" "January 1, 2025" and "March 31, 2025" (for Q1) <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
5.  Add a second condition using the "AND" operator (important for combining criteria) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
6.  For the second condition, select "Category" and set it to "is" "Software" <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.
7.  Click "Calculate" <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
8.  Create a new target database (e.g., "Sales Category Q1 2025 Total Sales") <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
9.  Copy its URL and use "Add to Notion" to place the value into the correct column and row <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.
10. Save the formula <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

The `myformulator.com` tool offers a user-friendly way to generate [[creating_and_saving_custom_formulas_in_notion | custom formulas]] and automatically update Notion databases without needing to understand complex Notion formulas or [[using_formulas_and_rollup_properties_in_notion | relation and rollup properties]] <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. Future videos may cover other functions like [[using_formulas_to_calculate_averages_in_notion | averages]] and [[formulas_for_multiplication_in_notion | multiplication]] <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.