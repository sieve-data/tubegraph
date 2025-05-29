---
title: Using Excellike formulas in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

While [[using_formulas_in_notion | Notion]] offers inbuilt formulas for various [[using_notion_for_calculations | calculations]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, it is possible to use Excel-like formulas in Notion by leveraging external tools <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This approach can help avoid the complexities of [[applying_formulas_and_rollup_properties_in_notion | Notion's relation and rollup properties]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## [[using_my_formula_gen_to_enhance_notion | Using My Formula Gen to Enhance Notion]]

To [[calculating_sum_values_with_external_tools_in_notion | calculate sum values with external tools in Notion]], the tool [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] (myformula.com) can be utilized <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Setting up the API Key

1.  Log in to myformula.com <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  Navigate to "Settings" and click "Get API key" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
3.  Create a "New Integration" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
4.  Provide a name for the integration (e.g., "Sum formula key") and select your Notion workspace <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
5.  Click "Save" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
6.  Go back to "Integrations," click on the newly created key, and reveal the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
7.  Copy the entire API key <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
8.  Paste the API key into the "Notion API key" field on myformula.com and click "Save settings" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Connecting Notion Databases

To ensure all relevant databases are connected:
1.  Place all databases you intend to use under a single Notion page (e.g., "Sales Dashboard") <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
2.  On that Notion page, click the three dots, select "Connections," and search for the API key name you created (e.g., "Sum formula key") <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
3.  Click on the key and "Confirm" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This connects the entire page, and by extension, all databases within it, to the API key <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## [[using_formulas_to_add_numbers_in_notion | Using Formulas to Add Numbers in Notion]] with [[using_my_formula_gen_to_enhance_notion | My Formula Gen]]

[[using_formulas_to_add_numbers_in_notion | My Formula Gen]] can be used to perform sum functions on Notion database properties <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

### Example 1: Total Sales Revenue

To find the total sales revenue from a Notion database:
1.  In [[using_my_formula_gen_to_enhance_notion | My Formula Gen]], paste the URL of the Notion database containing the sales data (e.g., a "Sales Database" with a "Revenue" property) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
2.  Select "Sum" as the function and choose the "Revenue" property <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
3.  Select "All Rows" to calculate the sum for all entries <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
4.  Remove any default second filter that may appear <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. The calculated sum will appear <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
6.  To add this value to a Notion database, click "Add to Notion" <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
7.  Provide the URL of the target Notion database (e.g., "DB for Sales Revenue Total") <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
8.  Specify the column (e.g., "Amount") and row (e.g., "Total Sales Revenue") where the value should be placed <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
9.  Click "Save to Notion" <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
10. Save the formula in [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] for future use <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Example 2: Sales Revenue for a Specific Month

To find the total sales revenue for a specific month (e.g., March):
1.  Click "New Formula" in [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
2.  Paste the URL of the sales database <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
3.  Select "Sum" for the "Revenue" property <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
4.  Add a filter condition: select the "Date" property and choose "Is Between" <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
5.  Enter the start and end dates for the desired month (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
7.  Add the calculated value to a Notion database as demonstrated above, specifying the appropriate column and row (e.g., "Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
8.  Save the formula <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

### Example 3: Sales Revenue for a Specific Quarter and Category

To find the sales revenue for a specific quarter and category (e.g., Q1 2025 for "Software" category):
1.  Click "New Formula" <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
2.  Paste the URL of the sales database <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
3.  Select "Sum" for the "Revenue" property <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
4.  Add the first filter condition: "Date" property, "Is Between," and define the quarter's dates (e.g., January 1st to March 31st, 2025) <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
5.  Add a second filter condition using "And" (important for multiple conditions) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
6.  Select the "Category" property and set the condition to "Is" "Software" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
7.  Click "Calculate" <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
8.  Add the calculated value to a Notion database (e.g., "Q1 2025 Total Sales"), specifying the appropriate column and row <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
9.  Save the formula <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

## Refreshing Calculated Values

If the original data in your Notion database changes, the calculated values in the target Notion databases will not automatically update <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   To update a specific formula's result, go to "Saved Formulas" in [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] and click "Refresh" next to that formula <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   To update all saved formulas, click "Refresh All" <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. This will re-compute and update all connected values in Notion <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

## Conclusion

Using [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] offers a straightforward way to [[managing_sales_data_with_formulas_in_notion | manage sales data with formulas in Notion]] and perform [[using_formulas_to add_numbers_in_notion | sum functions]] without requiring a deep understanding of [[using_formulas_in_notion | Notion's native formulas]] or [[applying_formulas_and_rollup_properties_in_notion | relation and rollup properties]] <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. It supports dynamic selections and multiple conditions, making it a flexible tool for various [[using_notion_for_calculations | calculations]] <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>.