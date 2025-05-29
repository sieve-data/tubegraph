---
title: Using Excellike formulas in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

While Notion offers inbuilt [[using_formulas_in_notion | formulas]], it is also possible to integrate Excel-like functionality for advanced calculations without directly using Notion's native formula language or complex relation and rollup properties <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This method simplifies [[creating_custom_formulas_in_notion | creating custom formulas in Notion]] and automates the process of [[creating_formulas_for_common_notion_tasks | creating formulas for common Notion tasks]].

## Using MyFormulaGen.com for Notion Calculations

The MyFormulaGen.com tool allows users to perform calculations in Notion databases that mimic Excel functions, such as finding the sum of numbers <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a> <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This method is particularly useful for [[formulas_for_finding_the_sum_of_numbers_in_notion | formulas for finding the sum of numbers in Notion]].

### Setup Process

1.  **Access the Tool**: Navigate to MyFormulaGen.com <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
2.  **Generate Notion API Key**:
    *   Click on 'Settings' in MyFormulaGen.com <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   Select 'Get API key' <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Create a new integration in Notion by clicking 'New integration' <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Give it a name (e.g., "Sum Formula Key") <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
    *   Choose your Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   Copy the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Paste this secret into the 'Notion API key' field on MyFormulaGen.com and click 'Save settings' <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a> <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
3.  **Connect Notion Database**:
    *   Ensure your Notion databases are within a shared page (e.g., "Sales Dashboard") <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a> <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   On the Notion page containing the databases, click the three dots, select 'Connections', and search for the API key created earlier <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a> <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    *   Confirm the connection <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This links all databases within that page to the API key <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a> <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

### Practical Examples of Summation

The process involves defining the source database, the property to sum, and any specific filters. The result is then outputted to a designated Notion database.

#### Example 1: Total Sales Revenue

To find the total sales revenue from a "Sales Database" and display it in a separate database (e.g., `DB_Sales_Revenue_Total`), follow these steps:

1.  **[[creating_a_database_in_notion_for_calculations | Create a database in Notion for calculations]]**: Create a new Notion database (e.g., `DB_Sales_Revenue_Total`) with columns like "Description" and "Amount" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a> <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
2.  **Copy Source Database Link**: In Notion, hover over the "Sales Database," click the six dots, and select 'Copy link' <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a> <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
3.  **Configure Formula in MyFormulaGen.com**:
    *   Paste the copied database link into the 'Database URL' field <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   Select 'Sum' for the operation <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   Choose the 'Revenue' field as the Notion Property <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    *   Select 'All rows' for the range <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Remove any default second filter if present <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   Click 'Calculate' <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a> <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
4.  **Add to Notion**:
    *   Click 'Add to Notion' <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
    *   Copy the link of the target database (`DB_Sales_Revenue_Total`) <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
    *   Paste it into the designated field in MyFormulaGen.com <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
    *   Select the 'Amount' column and the appropriate row (e.g., "Total Sales Revenue") <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a> <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   Click 'Save to Notion' <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
    *   Save the formula within MyFormulaGen.com for future use (e.g., "Total Sales Revenue") <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a> <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

#### Example 2: Total Sales Revenue for a Specific Month (e.g., March 2025)

1.  **Create New Formula**: Click 'New Formula' in MyFormulaGen.com <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a> <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
2.  **Paste Source Database Link**: Use the same "Sales Database" link <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
3.  **Configure Filters**:
    *   Select 'Sum' of the 'Revenue' field for 'All rows' <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   Add a filter: 'Date' property 'is between' March 1st and March 31st <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   Click 'Calculate' <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
4.  **Add to Notion**:
    *   [[creating_a_database_in_notion_for_calculations | Create a new Notion database]] (e.g., `DB_Sales_Revenue_March_2025`) <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
    *   Copy its link <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    *   Paste into MyFormulaGen.com, select the 'Amount' column and relevant row (e.g., "Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a> <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
    *   Click 'Save to Notion' <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a> and save the formula <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

#### Example 3: Sales Revenue for Q1 2025 (Software Category)

1.  **Create New Formula**: Click 'New Formula' <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
2.  **Paste Source Database Link**: Use the "Sales Database" link <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
3.  **Configure Multiple Filters**:
    *   Select 'Sum' of 'Revenue' for 'All rows' <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
    *   Add first condition: 'Date' property 'is between' January 1st and March 31st (for Q1) <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
    *   Ensure the logical operator is 'AND' <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
    *   Add second condition: 'Category' property 'is' "Software" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a> <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
    *   Click 'Calculate' <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
4.  **Add to Notion**:
    *   [[creating_a_database_in_notion_for_calculations | Create a third Notion database]] (e.g., `DB_Sales_Category_Q1_2025`) <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.
    *   Copy its link <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.
    *   Paste it into MyFormulaGen.com, select 'Amount' column and relevant row (e.g., "Q1 2025 Sales for Software") <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a> <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
    *   Click 'Save to Notion' <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a> and save the formula <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.

### Dynamic Updates

After setting up and saving formulas, any changes made in the original Notion sales database will not automatically reflect in the output databases <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. To update, simply go to the 'Saved formulas' section in MyFormulaGen.com and click 'Refresh all' <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a> <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. This will recompute and update all saved formulas, ensuring the Notion databases display the latest values <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Alternatively, you can refresh individual formulas <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

This approach offers a dynamic way to perform calculations without needing to understand Notion's internal formula syntax <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.

```ad-tip
For further assistance, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a> <a class="yt-timestamp" data-t="00:22:44">[00:22:44]</a>. More videos are planned to cover various Excel formulas in Notion <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.
```