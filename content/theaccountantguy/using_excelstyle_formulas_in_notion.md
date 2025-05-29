---
title: Using Excelstyle formulas in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Notion offers built-in [[using_formulas_in_notion | formulas]] for various calculations <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. However, for users seeking to perform [[how_to_use_excel_formulas_in_notion | Excel-like formulas]] directly within Notion, especially for functions like [[using_the_sum_function_in_notion | SUM]], an external tool can simplify the process without the complexities of Notion's native relation and rollup features <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

This guide demonstrates how to use [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] ([[using_my_formula_gen_for_notion_calculations | myformula.com]]) to achieve these calculations <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Setting Up My Formula Gen

To begin, you need to connect [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] to your Notion workspace:

1.  **Log In**: Navigate to [[using_my_formula_gen_for_notion_calculations | myformula.com]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  **Generate Notion API Key**:
    *   In [[using_my_formula_gen_for_notion_calculations | My Formula Gen]], go to `Settings` and click `Get API key` <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
    *   On the Notion integration page, click `New integration`, give it a name (e.g., "Sum Formula Key"), select your workspace, and click `Save` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Go back to `Integrations`, click on your newly created key, and copy the `Internal Integration Secret` by clicking `Show` and then `Copy` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   Paste this API key into the `Notion API Key` field in [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] and click `Save settings` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  **Connect Notion Page to API Key**:
    *   Ensure all databases you plan to use are within a single Notion page (e.g., "Sales Dashboard") <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
    *   On that Notion page, click the three dots (`...`) in the top right, select `Connections`, and search for and select the API key you created (e.g., "Sum Formula Key") <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   Click `Confirm`. This connects all databases within that page to the API key <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Performing Calculations with My Formula Gen

The following examples use a sales database with columns like Date, Product, Category, Quantity, Revenue, Payment Method, and Sales Channel <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### 1. Calculating Total Sales Revenue

To find the total sum of the 'Revenue' column from your sales database:

1.  **Copy Database Link**: In Notion, hover over your sales database, click the six dots (`...`), and select `Copy link` <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
2.  **Paste into My Formula Gen**: In [[using_my_formula_gen_for_notion_calculations | My Formula Gen]], paste the copied database link into the `Notion Database URL` field <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
3.  **Configure Formula**:
    *   Under `Select Notion Property`, choose `Sum` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   Select `Revenue` as the field to sum <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    *   For `Rows to calculate`, select `All Rows` <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Remove any default second filter if present, as it's not needed for a total sum <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
    *   Click `Calculate` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. The result (e.g., $1,537) will appear <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
4.  **Add to Notion**:
    *   Create a new Notion database where you want the total to appear (e.g., "DB - Sales Revenue Total" with 'Description' and 'Amount' columns) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
    *   Copy the link for this new destination database <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   In [[using_my_formula_gen_for_notion_calculations | My Formula Gen]], click `Add to Notion`, paste the destination database link <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   Select the `Amount` column and the relevant row (e.g., "Total Sales Revenue") where the value should be placed <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
    *   Click `Save to Notion` <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
5.  **Save Formula**: Click `Save Formula`, give it a name (e.g., "Total Sales Revenue"), and click `Save` <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Saved [[creating_and_saving_custom_formulas_in_notion | formulas]] can be found under the `Saved Formulas` section <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### 2. Calculating Sales Revenue for a Specific Month

To find the total sales for March 2025:

1.  **New Formula**: Click `New Formula` in [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
2.  **Paste Database Link**: Copy and paste the sales database link again <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
3.  **Configure Formula**:
    *   Select `Sum` for `Notion Property` and `Revenue` as the field <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   Add a filter: Select `Date` as the property, choose `is between` as the filter type <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   Set the date range from `March 1` to `March 31` <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
    *   Click `Calculate` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
4.  **Add to Notion**: Create a new destination database (e.g., "DB - Sales Revenue March 2025"), copy its link, and use `Add to Notion` to place the calculated value into the desired column and row <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
5.  **Save Formula**: Save the formula (e.g., "Total Sales Revenue for March 2025") <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

### 3. Calculating Sales Revenue for a Quarter and Category

To find the sales revenue for Q1 2025 specifically for the "Software" category:

1.  **New Formula**: Click `New Formula` <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
2.  **Paste Database Link**: Copy and paste the sales database link <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
3.  **Configure Formula**:
    *   Select `Sum` for `Notion Property` and `Revenue` as the field <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
    *   Add the first filter: `Date` `is between` `January 1` to `March 31` (for Q1) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   Add a second condition using the `And` operator (since both conditions must be met) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. Click `+` to add a new condition <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
    *   For the second filter, select `Category` `is` `Software` <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
    *   Click `Calculate` <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
4.  **Add to Notion**: Create a new destination database (e.g., "DB - Sales Category Q1 2025"), copy its link, and use `Add to Notion` to place the calculated value <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
5.  **Save Formula**: Save the formula (e.g., "Q1 2025 Sales for Software") <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

## Dynamic Updates and Customization

*   **Refreshing Values**: If the data in your original Notion database changes, you can automatically update the calculated values by going to `Saved Formulas` in [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] and clicking `Refresh All` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. You can also refresh individual formulas <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
*   **Currency and Number Formatting**: [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] allows you to set different currencies, number formats, and decimal places for presentation purposes <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
*   **Other Functions**: While this guide focuses on the [[using_the_sum_function_in_notion | SUM function]], [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] offers various other functions and operators, allowing for complex calculations and conditions <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

Using [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] provides a simple and dynamic way to implement [[how_to_use_excel_formulas_in_notion | Excel-like formulas in Notion]] without needing to delve into Notion's native formula complexities <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.

---
*For further queries, you can reach out to notionformyuse@gmail.com* <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.