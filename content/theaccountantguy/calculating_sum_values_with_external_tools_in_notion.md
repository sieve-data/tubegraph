---
title: Calculating sum values with external tools in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

This article explores a method for [[calculating_the_sum_of_a_column_in_notion | calculating sum values]] in Notion using an external tool, offering an alternative to Notion's inbuilt [[using_formulas_in_notion | formulas]] or relation and rollup properties <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. The focus is on implementing [[using_excellike_formulas_in_notion | Excel-like formulas in Notion]] for sum functions <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Overview of the Sales Database

For demonstration purposes, a sales database is used <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. It includes the following fields:
*   Date <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   Product <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   Category <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   Quantity <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   Revenue <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   Payment method <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   Sales Channel <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>

The goal is to derive specific sum information from this database and display it in separate Notion databases <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a> <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Target Calculations

The following sum calculations will be demonstrated:
1.  Total Sales Revenue <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
2.  Total Sales Revenue for the March month <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>
3.  Sales Revenue for Quarter 1 (Q1) 2025 for the "Software" category <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>

## Using MyFormulaGen.com for Calculations

The external tool used for these calculations is MyFormulaGen.com <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Setup Steps

1.  **Log in to MyFormulaGen.com**: Access the tool's interface <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  **Set up Notion API Key**:
    *   In MyFormulaGen.com, click on "Settings" and then "Get API Key" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   On the Notion API page, click "New integration" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Give the integration a name (e.g., "Sum formula key") and select your workspace <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   Click "Save" <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
    *   Copy the "Internal Integration Secret" by clicking "Show" and then "Copy" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Paste this API key into the "Notion API key" field on MyFormulaGen.com and click "Save Settings" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  **Connect Notion Databases**:
    *   Ensure all databases you plan to use are within a single Notion page (e.g., "Sales Dashboard") <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a> <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   From the Notion page containing your databases, click the three dots (`...`) menu <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   Go to "Connections" and select the API key you just created (e.g., "Sum formula key") <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
    *   Click "Confirm" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This connects the entire page and its contained databases to the API <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Performing the Calculations

#### 1. Total Sales Revenue

To calculate the total sales revenue from the main sales database:
*   In MyFormulaGen.com, copy the link of your source sales database (by hovering over the database, clicking the six dots, and selecting "Copy link") <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   Paste the link into the MyFormulaGen.com interface <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   Select "sum" as the operation and "Revenue" as the Notion property <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   Choose "all rows" for the calculation range <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   Remove any default second filter that might appear <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Once the value is calculated, click "Add to Notion" <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   Copy the link of the target Notion database (where you want the sum to appear) and paste it into MyFormulaGen.com <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   Select the target column (e.g., "Amount") and row (e.g., "Total sales revenue") in your target Notion database <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   Click "Save to Notion" <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   Save the formula in MyFormulaGen.com for future use <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

#### 2. Total Sales Revenue for March

To find the total sales revenue for March:
*   Click "New formula" in MyFormulaGen.com <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   Paste the source sales database link <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
*   Select "sum" and "Revenue" <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   Add a filter: set the "Date" property to "is between" March 1st and March 31st <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a> <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   Click "Add to Notion", copy the link of your target database (e.g., a new database for March sales) <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a> <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
*   Paste the link, select the appropriate column and row, and click "Save to Notion" <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a> <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
*   Save the formula <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

#### 3. Sales Revenue for Q1 2025 for Software Category

To find the sales revenue for the "Software" category in Q1 (January 1st to March 31st):
*   Click "New formula" <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   Paste the source sales database link <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   Select "sum" and "Revenue" <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   Add the first condition: "Date" property "is between" January 1st, 2025, and March 31st, 2025 (for Q1) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a> <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.
*   Add a second condition using "AND" <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. Click the "plus" icon or "duplicate" the existing condition to add another filter <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   Set the "Category" property to "is" "Software" <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
*   Click "Add to Notion", copy the link of your target database (e.g., a new database for Q1 sales) <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   Paste the link, select the appropriate column and row, and click "Save to Notion" <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a> <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
*   Save the formula <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

## Dynamic Updates and Saved Formulas

Once formulas are saved in MyFormulaGen.com, they can be found in the "Saved Formulas" section <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a> <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.

>[!INFO] Refreshing Data
> If values in the original Notion database change, the calculated sums in the target databases will not update automatically <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. To reflect these changes, go to "Saved Formulas" in MyFormulaGen.com and click "Refresh All" <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. This will recompute and update all saved formulas in Notion <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. You can also refresh individual formulas <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

## Benefits of This Method

This approach simplifies [[using_notion_for_calculations | calculations in Notion]] by avoiding the complexities of [[applying_formulas_and_rollup_properties_in_notion | Notion's native formulas and rollup properties]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a> <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. It provides a dynamic way to [[different_methods_to_calculate_sums_in_notion | calculate sums]] with multiple conditions, making it user-friendly for [[managing_sales_data_with_formulas_in_notion | managing sales data with formulas in Notion]] or similar data sets <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.

> For further queries, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a> <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>. More videos covering other [[using_excellike_formulas_in_notion | Excel-like formulas in Notion]] will be released in the future <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.