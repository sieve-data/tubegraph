---
title: Generating and managing SUM function results in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Notion offers [[using_formulas_to_add_numbers_in_notion | inbuilt formulas]] for various calculations, but for more complex Excel-like sum functions, especially those involving multiple conditions, an external tool like `myformulagen.com` can be used to bypass Notion's native [[using_formulas_and_rollup_properties_in_notion | relation and rollup properties]] or complex Notion formulas <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This method allows users to perform [[sum_sumif_and_sumifs_functions_in_notion | SUM, SUMIF, and SUMIFS functions]] in Notion.

## Prerequisites

To use `myformulagen.com` for Notion calculations, follow these setup steps:

1.  **Log in to MyFormulaGen.com** <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  **Set up an API Key**:
    *   Navigate to "Settings" on `myformulagen.com` and click "Get API key" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   In Notion, create a new integration (e.g., "Sum Formula Key") from the API key page <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Select your Notion workspace and save the integration <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   Copy the "Internal Integration Secret" from the newly created integration in Notion <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Paste this API key into the "Notion API key" field on `myformulagen.com` and save settings <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  **Connect Notion Databases**:
    *   Ensure all relevant Notion databases (source and destination) are placed within a single parent page <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
    *   Connect this parent page to the API key created earlier. Click the three dots on the page, select "Connections," and choose your API key (e.g., "Sum Formula Key") <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This connects all databases within that page to the API key <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Performing SUM Calculations

This tool allows for [[calculating_sum_of_a_column_in_notion | calculating the sum of a column]] in Notion based on various conditions.

### 1. Calculating Total Sales Revenue (Basic SUM)

To find the total sales revenue from a Notion database (e.g., a "Sales Database" with a "Revenue" column) and display it in another database:

*   **Source Database**: Have a database with numeric values, like a "Sales Database" containing `Date`, `Product`, `Category`, `Quantity`, `Revenue`, `Payment Method`, and `Sales Channel` columns <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   **Target Database**: [[creating_a_database_in_notion_for_calculations | Create a database]] (e.g., "DB for Sales Revenue Total") with a "Description" column (e.g., "Total Sales Revenue") and an "Amount" column (Number type) to hold the result <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

**Steps in MyFormulaGen:**
1.  On `myformulagen.com`, click "New Formula" <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
2.  Copy the link of your source "Sales Database" in Notion (by clicking the six dots next to the database name and selecting "Copy link") <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
3.  Paste the database link into the "Notion Database URL" field on `myformulagen.com` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
4.  Select "Sum" as the function from the "Notion Property" dropdown <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
5.  Choose the "Revenue" column to sum <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
6.  Select "All Rows" for the sum range <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
7.  If an extra filter is automatically added, remove it if you don't need it for a total sum <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
8.  Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
9.  Click "Add to Notion" <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
10. Copy the link of your target "DB for Sales Revenue Total" database <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
11. Paste this link into `myformulagen.com` <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
12. Select the "Amount" column and the "Total Sales Revenue" row where the calculated value should be placed <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
13. Click "Save to Notion" to push the value to your Notion database <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
14. Save the formula within `myformulagen.com` with a descriptive name (e.g., "Total Sales Revenue") <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### 2. Calculating Sales Revenue for a Specific Month (SUMIF)

To find the total sales revenue for a specific month (e.g., March 2025):

1.  Click "New Formula" on `myformulagen.com` <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
2.  Paste the source "Sales Database" link <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
3.  Select "Sum" for the "Revenue" column, considering "All Rows" <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
4.  Add a condition:
    *   Select the "Date" property.
    *   Choose "is between" for the filter condition.
    *   Enter the start and end dates (e.g., March 1, 2025, to March 31, 2025) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
6.  Click "Add to Notion" and select the target database (e.g., "DB for Sales Revenue March 2025"), column ("Amount"), and row (e.g., "Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
7.  Save the formula (e.g., "Total Sales Revenue for March 2025") <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

### 3. Calculating Sales Revenue for a Specific Quarter and Category (SUMIFS)

To find the sales revenue for Quarter 1 2025 specifically for the "Software" category:

1.  Click "New Formula" on `myformulagen.com` <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
2.  Paste the source "Sales Database" link <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
3.  Select "Sum" for the "Revenue" column, considering "All Rows" <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
4.  Add the first condition (Date Range):
    *   Select the "Date" property.
    *   Choose "is between".
    *   Enter the Quarter 1 dates (e.g., January 1, 2025, to March 31, 2025) <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
5.  Add the second condition (Category) using an "AND" operator <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>:
    *   Click the "+" button to add a new condition <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
    *   Select the "Category" property.
    *   Choose "is".
    *   Enter "Software" as the value <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
7.  Click "Add to Notion" and select the target database (e.g., "DB for Sales Category Q1 2025"), column ("Amount"), and row (e.g., "Q1 2025 Sales for Software") <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
8.  Save the formula (e.g., "Q1 2025 Sales for Software") <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

### Managing and Refreshing Results

*   **Saving Formulas**: After creating a formula, save it on `myformulagen.com` to easily access and re-run it later <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Refreshing Data**: If the source Notion database values change, the results in your target Notion database will not automatically update <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. To refresh:
    1.  Go to the "Saved Formulas" section on `myformulagen.com` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
    2.  Click "Refresh All" to update all saved formulas <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>, or click the "Refresh" icon next to a specific formula to update only that one <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
    3.  The updated values will appear in your Notion database <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

This approach simplifies complex calculations in Notion by leveraging an external tool, providing dynamic updates without requiring in-depth knowledge of Notion's [[using_formulas_to_calculate_averages_in_notion | formula functions]] or [[calculating_product_of_two_numbers_in_notion | property types]] <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. It can be used for various calculations including [[calculating_percentages_in_notion | percentages]] and [[formulas_for_multiplication_in_notion | multiplication]].