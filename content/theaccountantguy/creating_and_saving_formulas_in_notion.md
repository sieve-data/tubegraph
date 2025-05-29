---
title: Creating and saving formulas in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

This article discusses how to [[using_excelstyle_formulas_in_notion | use Excel-like formulas in Notion]] for calculations, specifically focusing on the sum function, without using Notion's native formulas or rollup properties <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. The method demonstrated leverages an external tool, `myformulagen.com`, to achieve dynamic calculations and seamlessly integrate them into Notion databases <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Utilizing `myformulagen.com` for Calculations

The `myformulagen.com` tool enables users to perform calculations and push the results directly into Notion databases <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This approach simplifies complex calculations like [[using_formulas_to_add_numbers_in_notion | adding numbers in Notion]] (summation) without requiring an in-depth understanding of Notion's built-in formula capabilities <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

### Initial Setup and Connection

To connect `myformulagen.com` with Notion:
1.  **Log in to `myformulagen.com`** <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  **Set up an API key**:
    *   Navigate to "Settings" within `myformulagen.com` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   Click "Get API key" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Create a "New integration" (e.g., "sum formula key") <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Select your Notion workspace (e.g., "the accountant guy workspace") and save <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   Copy the "internal integration secret" from the newly created key <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Paste this API key into the "Notion API key" field on `myformulagen.com` and click "Save settings" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  **Connect Notion databases**:
    *   Place all Notion databases relevant to your calculations (e.g., a "Sales Dashboard" page) under a single parent page <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
    *   On the parent page in Notion, click the three dots, select "Connections," and search for your created API key (e.g., "sum") <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   Select the key and confirm the connection <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This ensures all databases within that page are connected <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   Copy the link to the Notion database you want to pull data from (e.g., a "sales database" with date, product, category, quantity, revenue, payment method, and sales channel) <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
    *   Paste this database link into the designated field on `myformulagen.com` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### [[using_formulas_to_add_numbers_in_notion | Using Formulas to Add Numbers in Notion]] (Sum Function)

Once connected, you can define your sum calculations:

#### 1. Calculating Total Sales Revenue

To find the sum of all revenue entries in a sales database:
*   On `myformulagen.com`, select "sum" as the function <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   Choose the "Revenue" field from your Notion database properties <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   Select "all the rows" to sum all entries <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   Remove any default second filters that might appear <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   To push this value into Notion, click "Add to Notion" <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   Copy the link of the target Notion database (e.g., a new database for sales revenue totals) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   Paste the link in `myformulagen.com`, then select the specific column (e.g., "Amount") and row (e.g., "Total Sales Revenue") where the calculated value should appear <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   Click "Save to Notion" <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

#### 2. Calculating Sales Revenue for a Specific Month

To sum revenue based on a date filter (e.g., March 2025):
*   Create a "New formula" on `myformulagen.com` <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   Paste the source sales database link <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
*   Select "sum" for the "Revenue" field <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   Add a condition: set the "Date" property to "is between" March 1st and March 31st <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   "Add to Notion" by selecting the target database (e.g., a new database for "Sales Revenue March 2025"), column, and row <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   Click "Save to Notion" <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

#### 3. Calculating Sales Revenue for a Specific Quarter and Category

To sum revenue with multiple conditions (e.g., Q1 2025 for "Software" category):
*   Click "New formula" <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   Paste the source sales database link <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   Select "sum" for the "Revenue" field <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
*   Add the first condition: "Date" property "is between" January 1st and March 31st (for Quarter 1) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
*   Add a second condition using "AND" (not "OR") because both conditions must be met <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
*   For the second condition, set the "Category" property to "is" "Software" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
*   "Add to Notion" by selecting the appropriate target database (e.g., a new one for "Sales Category Q1 2025"), column, and row <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   Click "Save to Notion" <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

### [[refreshing_and_updating_formulas_in_notion_databases | Refreshing and Updating Formulas in Notion Databases]]

After creating and adding a formula to Notion, it's crucial to save it in `myformulagen.com` <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   Click "Save formula" and give it a descriptive name <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   Saved formulas are accessible in the "Saved Formulas" section <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   If the source data in Notion changes, the calculated values in your target Notion databases will not automatically update <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   To update all formulas, go to "Saved Formulas" and click "Refresh all" <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   To update a specific formula, click the "Refresh" icon next to it <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. This ensures your Notion values reflect the latest data <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Benefits of this Approach

This method allows users to generate complex calculations, including conditional sums, without engaging with Notion's native formula syntax or [[using_formulas_and_rollup_properties_in_notion | rollup properties]] <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. It offers a simple and dynamic way to derive desired results from Notion databases by allowing users to select fields and define conditions via a user-friendly interface <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>.