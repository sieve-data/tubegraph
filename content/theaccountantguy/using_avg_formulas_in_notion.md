---
title: Using AVG formulas in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

This article explains how to find the average of numbers in Notion, particularly when dealing with complex scenarios or desiring [[using_excelstyle_formulas_in_notion | Excel-style formulas]] functionality that Notion's built-in capabilities might not easily provide <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While Notion offers inbuilt formulas, they can sometimes be complicated to understand <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This guide focuses on [[implementing_excellike_formulas_in_notion_using_external_tools | implementing Excel-like formulas in Notion using an external tool]] called MyFormulaGen <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Database Structure <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>

The examples provided use a Notion sales database containing properties such as Date, Product, Category, Quantity, and Revenue <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The goal is to find the average value of the "Revenue" numbers and populate them into a second Notion database <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Average Calculation Scenarios <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>

This guide demonstrates how to calculate three types of averages, similar to AVERAGE, AVERAGEIF, and AVERAGEIFS functions in Excel <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>:
1.  **Average Sales Revenue**: The overall average of all revenue figures <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
2.  **Average Sales Revenue for a Specific Month**: For instance, only for the month of March <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
3.  **Average Sales Revenue with Multiple Conditions**: For example, for the "Software" category and only for the first quarter (January, February, and March) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Setting Up MyFormulaGen <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>

1.  **Access MyFormulaGen**: Go to myformulagen.com and log in or create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Database URL**:
    *   In Notion, open your database page <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   If it's a full-page database, click the three dots at the top right, then "Copy link" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   If it's an inline database, click the six dots next to the database title, then "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Paste this URL into MyFormulaGen <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
3.  **Add API Key**:
    *   In MyFormulaGen, click on "Settings" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   Click "Get API key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   On the Notion API page, click "New integration", define a name (e.g., "My API Key"), select your workspace, and click "Save" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Copy the "Internal Integration Secret" (click "Show" to reveal) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Paste this secret into the API key field in MyFormulaGen settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect Notion Database to API Key**:
    *   Go back to your Notion database page <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Click the three dots at the top right of the page (for full page) or the six dots (for inline database), then "Connections" <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Search for and select the API key integration you just created (e.g., "MyFormulaGen") <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Click "Confirm" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This connects the page and its databases to the API <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Calculating Averages <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>

### 1. Simple Average (AVERAGE) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>

To find the average of the "Revenue" column for all rows:
*   In MyFormulaGen, ensure the correct database URL is entered <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   Select the "Average" operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Choose "Revenue" as the column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   Select "All Rows" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### 2. Conditional Average (AVERAGEIF) <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>

To find the average sales revenue for a specific month (e.g., March):
*   Click "New Formula" in MyFormulaGen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   Paste the database link <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   Select "Average" of "Revenue" for "All Rows" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   Add a condition: choose the "Date" field <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   Set the condition to "start date is between" and define the date range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### 3. Multiple Conditional Average (AVERAGEIFS) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>

To find the average sales revenue for the "Software" category in Quarter 1 (Jan-Mar):
*   Click "New Formula" in MyFormulaGen <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   Paste the database link <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   Select "Average" of "Revenue" for "All Rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   Add the first condition: "Date" field, "start date is between" (e.g., Jan 1st to March 31st for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Add an "AND" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   Add the second condition: "Category" column, "is" "Software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

## Saving Results to Notion <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>

To put the calculated average into a Notion database:
1.  **Create a Summary Database in Notion**:
    *   Create a new inline database (e.g., "DB\_Summary") in your Notion page <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Add a "Value" property of type "Number" to this summary database <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   Create a new row in this summary database for each average you want to store (e.g., "Average Sales Revenue", "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
2.  **Copy Summary Database Link**: Click the six dots next to your summary database and "Copy link" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
3.  **Add to Notion (MyFormulaGen)**:
    *   In MyFormulaGen, after calculating the average, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
    *   Paste the summary database link into the provided field <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    *   Select the "Value" column where the number should be saved <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   Select the specific row (e.g., "Average Sales Revenue") where you want to save the value <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The value will now appear in your Notion summary database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

## Saving and Refreshing Formulas <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>

*   **Save Formula**: To reuse the calculation, click "Save Formula" in MyFormulaGen, define a name (e.g., "Revenue Average"), and click "Save" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This saves the formula under "Saved Formulas" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Refresh Formulas**: If the original data in your Notion database changes, the averages in your summary database will not automatically update <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    *   To refresh a specific formula, go to "Saved Formulas" and click "Refresh Formula" next to it <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
    *   To refresh all saved formulas, click "Refresh All" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This will update the values in your Notion summary database <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

## Conclusion <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>

This method provides a flexible way to calculate various averages in Notion without delving into complex native [[using_formulas_in_notion | Notion formulas]] <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. The external tool also supports other Excel-like operations such as [[calculating_sum_of_a_column_in_notion | calculating sum of a column in Notion]] (e.g., [[calculating_total_sales_using_sum_function_in_notion | calculating total sales using the SUM function in Notion]]), count, and [[calculating_product_of_numbers_in_notion | calculating product of numbers in Notion]] (see [[formulas_for_multiplication_in_notion | formulas for multiplication in Notion]]), offering similar [[applying_sumif_and_sumifslike_logic_in_notion | SUMIF and SUMIFS-like logic]] <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.