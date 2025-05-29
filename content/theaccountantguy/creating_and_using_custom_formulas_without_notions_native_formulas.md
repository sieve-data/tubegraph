---
title: Creating and using custom formulas without Notions native formulas
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Notion offers built-in formulas for calculations <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. However, it's possible to [[using_excellike_formulas_in_notion | use Excel-like formulas in Notion]] without relying on Notion's native formula syntax or complex relation and rollup properties <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a> <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This method leverages a third-party tool to perform calculations like the SUM function <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Utilizing My Formula Gen for Notion Calculations

The tool used for this approach is [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] (myformula.com) <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Initial Setup

1.  **Log In to MyFormula.com** <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  **Connect Notion via API Key**:
    *   Navigate to "Settings" in MyFormula.com and click "Get API key" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   In Notion, create a new integration (e.g., "Sum formula key") <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Select your Notion workspace and save <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   Copy the "Internal Integration Secret" from the newly created integration in Notion <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Paste this API key into the "Notion API key" field in MyFormula.com settings and click "Save settings" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  **Connect Notion Page/Databases**:
    *   Ensure all databases you wish to use are within a single Notion page (e.g., a "Sales Dashboard" page) <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
    *   On that Notion page, click the three dots in the top right corner, select "Connections," and add the integration you just created (e.g., "Sum formula key") <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. This connects everything within that page to the API key <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Example 1: Calculating Total Sales Revenue

To find the total sales revenue from a sales database:

1.  **Copy Database Link**: In Notion, hover over your sales database, click the six dots, and select "Copy link" <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
2.  **Paste into My Formula Gen**: Paste the copied database link into the designated field in MyFormula.com <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This will enable the Notion property field <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
3.  **Define Formula**:
    *   Select the "Sum" function <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   Choose the "Revenue" property from your sales database <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    *   Select "all the rows" to sum all revenue entries <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Remove any default second filter that might appear <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   Click "Calculate" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
4.  **Add to Notion**:
    *   Create a separate Notion database (e.g., `db_sales_revenue_total`) to display the result <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Define columns like "Description" and "Amount" <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
    *   Copy the link for this new target database <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
    *   In MyFormula.com, click "Add to Notion" and paste the target database link <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   Select the target column (e.g., "Amount") and the specific row (e.g., "Total sales revenue") where you want the value to appear <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
    *   Save the formula in MyFormula.com for future use (e.g., "Total sales revenue") <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Dynamic Updates

If the values in your original sales database change, the displayed total in Notion won't update automatically <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. To refresh the calculation:

*   Go to "Saved formulas" in MyFormula.com <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   Click "Refresh all" to update all saved formulas <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   Alternatively, click the individual "Refresh" button next to a specific formula to update only that one <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Example 2: Calculating Sales Revenue for a Specific Month

To find total sales revenue only for the month of March:

1.  **New Formula**: Click "New formula" in MyFormula.com <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
2.  **Copy/Paste Source Database Link**: Repeat the step of copying and pasting the sales database link <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
3.  **Define Formula with Filter**:
    *   Select "Sum" and "Revenue" for "all the rows" <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   Add a filter: select the "Date" property, choose "is between," and manually enter "March 1" and "March 31" <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   Click "Calculate" <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
4.  **Add to Notion**:
    *   Create another Notion database (e.g., `db_sales_revenue_March_2025`) with "Description" and "Amount" columns <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
    *   Copy and paste its link into MyFormula.com <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    *   Select the target "Amount" column and the relevant row (e.g., "Sales revenue March 2025") <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
    *   Save the formula (e.g., "Total sales revenue for March 2025") <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

### Example 3: Calculating Sales Revenue for a Specific Quarter and Category

To find the sales revenue for Quarter 1 (Q1) 2025 for the "Software" category:

1.  **New Formula**: Click "New formula" <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
2.  **Copy/Paste Source Database Link**: Repeat the step <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
3.  **Define Formula with Multiple Conditions**:
    *   Select "Sum" and "Revenue" for "all the rows" <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
    *   Add the first condition: Select "Date," choose "is between," and set the range from "January 1 2025" to "March 31 2025" (for Q1) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   Crucially, ensure the logical operator between conditions is "AND" <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
    *   Add a second condition: Select "Category," choose "is," and enter "Software" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
    *   Click "Calculate" <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
4.  **Add to Notion**:
    *   Create a third Notion database (e.g., `db_sales_category_q1_2025`) with "Description" and "Amount" columns <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
    *   Copy and paste its link into MyFormula.com <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.
    *   Select the target "Amount" column and the relevant row (e.g., "Q1 2025 sales for software") <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.
    *   Save the formula <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

### Benefits

This method allows users to perform [[using_notion_for_calculations | calculations in Notion]] and [[using_formulas_to_add_numbers_in_notion | add numbers in Notion]] (or other operations) with [[creating_custom_formulas_and_linking_databases_in_notion | custom formulas]] without needing to learn Notion's specific formula syntax or use [[applying_formulas_and_rollup_properties_in_notion | Notion's relation and rollup properties]] <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. It's a dynamic and intuitive way to manage [[managing_sales_data_with_formulas_in_notion | sales data with formulas in Notion]] and other numerical data <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

> [!INFO]
> For any queries, feel free to reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>.