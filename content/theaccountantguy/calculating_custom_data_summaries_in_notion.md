---
title: Calculating custom data summaries in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Notion offers inbuilt formulas for various calculations <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. However, it's possible to perform Excel-like calculations, such as sums, within Notion using an external tool <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This method allows for complex data summaries without needing to understand Notion's built-in [[using_formulas_in_notion | formulas]] or relation/rollup features <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

The tool used for this purpose is MyFormulaGen.com <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Setting Up MyFormulaGen.com

To use MyFormulaGen.com, you need to connect it to your Notion workspace via an API key <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

1.  **Create an API Key**:
    *   Log in to MyFormulaGen.com <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
    *   Go to "Settings" and click "Get API Key" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Click "New Integration" in Notion's API settings <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Give it a name (e.g., "Sum Formula Key") <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a> and select your Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   Save the integration <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   Copy the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   Paste this secret into the "Notion API Key" field on MyFormulaGen.com and click "Save settings" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

2.  **Connect Notion Databases to the API Key**:
    *   It is recommended to place all relevant databases within a single Notion page (e.g., a "Sales Dashboard" page) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   Click the three dots `...` on the Notion page containing your databases <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   Select "Add connections" and search for the API key name you created (e.g., "Sum Formula Key") <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   Confirm the connection <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This ensures all databases within that page are connected <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## Calculating Data Summaries

The following examples demonstrate how to calculate specific data summaries using MyFormulaGen.com.

### 1. Calculating Total Sales Revenue

This example shows how to calculate the [[calculating_sum_of_a_column_in_notion | sum of a column]] in a Notion database and display it in another Notion database.

*   **Objective**: Find the total sales revenue from a sales database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Notion Setup**: Create a new inline database (e.g., `db_Sales Revenue Total`) with "Description" and "Amount" columns <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Add a row named "Total Sales Revenue" <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **MyFormulaGen Steps**:
    1.  Copy the link of your source sales database (the one containing the `Revenue` column) <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
    2.  Paste the link into MyFormulaGen.com's "Notion Database" field <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    3.  Select "Sum" as the function <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    4.  Select the "Revenue" property <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    5.  Choose "All the Rows" to include all data <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    6.  Remove any default additional filters <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    7.  Click "Calculate" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. The calculated sum (e.g., $1,537) will appear <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
    8.  Click "Add to Notion" <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
    9.  Copy the link of your destination database (e.g., `db_Sales Revenue Total`) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> and paste it into MyFormulaGen.com <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
    10. Select the "Amount" column and the "Total Sales Revenue" row <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    11. Click "Save to Notion" <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. The value will appear in your Notion database <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Saving and Refreshing the Formula**:
    *   Save the formula in MyFormulaGen.com with a descriptive name (e.g., "Total Sales Revenue") <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   If the source data in Notion changes, go to "Saved Formulas" in MyFormulaGen.com and click "Refresh All" or refresh for a specific formula <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. The value in Notion will automatically update <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### 2. Calculating Total Sales Revenue for a Specific Month

This demonstrates [[using_formulas_to_calculate_differences_in_notion | using formulas to calculate differences]] and apply date filters.

*   **Objective**: Find the total sales revenue only for the month of March <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Notion Setup**: Create another inline database (e.g., `db_Sales Revenue March 2025`) with "Description" and "Amount" columns <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Add a row named "Sales Revenue March 2025" <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **MyFormulaGen Steps**:
    1.  Click "New Formula" <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
    2.  Paste the source sales database link <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
    3.  Select "Sum" function for the "Revenue" property <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a> and "All the Rows" <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
    4.  Add a condition: set the "Date" property to "is between" March 1 and March 31 <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    5.  Click "Calculate" <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
    6.  Click "Add to Notion" <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
    7.  Paste the destination database link (e.g., `db_Sales Revenue March 2025`) <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
    8.  Select the "Amount" column and the "March 2025 Sales Revenue" row <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
    9.  Click "Save to Notion" <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
    10. Save the formula <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

### 3. Calculating Sales Revenue for a Specific Quarter and Category

This example demonstrates applying multiple conditions (AND logic) for [[using_formulas_for_financial_calculations_in_notion | financial calculations]].

*   **Objective**: Find the sales revenue for Quarter 1 (Q1) 2025 specifically for the "Software" category <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
*   **Notion Setup**: Create a third inline database (e.g., `db_Sales_Category_Q1_2025`) <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a> with "Description" and "Amount" columns <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. Add a row named "Q1 2025 Sales for Software" <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.
*   **MyFormulaGen Steps**:
    1.  Click "New Formula" <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
    2.  Paste the source sales database link <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
    3.  Select "Sum" function for the "Revenue" property <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a> and "All the Rows" <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
    4.  Add the first condition: "Date" property "is between" January 1, 2025, and March 31, 2025 (for Q1) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    5.  Add a second condition using the "AND" operator (important for combining criteria) <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.
    6.  For the second condition, select the "Category" property to "is" "Software" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
    7.  Click "Calculate" <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. The result (e.g., $230) will appear <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.
    8.  Click "Add to Notion" <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
    9.  Paste the destination database link (e.g., `db_Sales_Category_Q1_2025`) <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
    10. Select the "Amount" column and the "Q1 2025 Sales for Software" row <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
    11. Click "Save to Notion" <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.
    12. Save the formula <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

## Benefits of This Method

This approach simplifies [[adding_numbers_in_notion | adding numbers]] and performing custom data summaries in Notion by:

*   **Avoiding Complex Notion Formulas**: Users do not need to learn Notion's specific formula syntax <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **No Relation/Rollup Hassles**: It bypasses the need for Notion's "relation" and "rollup" properties, which can be complex to set up <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Dynamic Updates**: Saved formulas can be easily refreshed, automatically updating calculated values in Notion whenever the source data changes <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. This is useful for [[analyzing_financial_data_with_notion_templates | analyzing financial data]] or [[customizing_sales_dashboards_in_notion | customizing sales dashboards]].
*   **Flexible Filtering**: Allows for multiple conditions (AND/OR) and various filter types (e.g., date ranges, specific categories) <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>, aiding in the [[presentation_of_expense_data_in_notion | presentation of expense data]] or other metrics.

This method offers a straightforward way to achieve custom data aggregations, particularly when [[using_the_sum_function_in_notion | using the SUM function in Notion]] or more complex filtering.