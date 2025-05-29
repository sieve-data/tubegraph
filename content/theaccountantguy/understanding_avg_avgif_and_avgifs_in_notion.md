---
title: Understanding AVG AVGIF and AVGIFS in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion has built-in [[using_formulas_in_notion | formulas]] for basic calculations, they can sometimes be complicated to understand <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. For more advanced calculations like `AVERAGEIF` (average with one condition) and `AVERAGEIFS` (average with multiple conditions) similar to [[how_to_use_excel_formulas_in_notion | Excel formulas]], an external tool can simplify the process <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

This guide demonstrates how to calculate various averages of numbers in Notion using the external tool MyFormulaGen, allowing you to centralize financial data summaries and budgeting in [[utilizing_notion_for_financial_summaries_and_budgeting | Notion]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Introducing MyFormulaGen

MyFormulaGen is an external tool used to calculate averages and other metrics from Notion databases <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. It allows you to implement [[using_excelstyle_formulas_in_notion | Excel-style formulas]] like `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` within Notion <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Setup Steps for MyFormulaGen

To use MyFormulaGen, follow these initial setup steps:

1.  **Create an Account**: Go to myformulagen.com and log in or create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Database URL**:
    *   Open your Notion database (e.g., a sales database with columns like Date, Product, Category, Quantity, Revenue) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
    *   If your database is in full-page mode, click the three dots in the top right corner, then "Copy link" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   If your database is inline, click the six dots next to the database title, then "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Paste this URL into the MyFormulaGen interface <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>, <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  **Add API Key**:
    *   In MyFormulaGen, click on "Settings" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Click "Get API Key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
    *   Click "New integration," define a name (e.g., "My API Key"), and select your Notion workspace <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   Save the integration. You will see an "Internal Integration Secret" <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>, <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Click "Show" and copy this secret <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   Paste the API key into MyFormulaGen's settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect Notion Page to API Key**:
    *   Go back to the Notion page containing your database <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   Click the three dots in the top right corner of the Notion page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Select "Connections" and connect the API key you just created (e.g., "MyFormulaGen") <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>, <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This connects both the page and any inline databases within it <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Calculating Averages

You can perform various average calculations:

### 1. Simple Average (AVG)

To find the overall average sales revenue for all entries:

*   **Objective**: Calculate the average of the "Revenue" column <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   **MyFormulaGen Steps**:
    1.  Ensure your Notion database URL is entered <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    2.  Select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    3.  Choose "Revenue" as the target column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
    4.  Select "All rows" for the range <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    5.  Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Saving to Notion**:
    1.  Create a new inline database in your Notion page (e.g., "DB\_summary") with a "Name" and "Value" column (formatted as a number) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    2.  Add a new row (e.g., "Average Sales Revenue") in the "DB\_summary" database <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
    3.  Copy the link of this summary database <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    4.  In MyFormulaGen, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
    5.  Paste the summary database link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    6.  Select the "Value" column and the "Average Sales Revenue" row <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    7.  Click "Save to Notion" to populate the value <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### 2. Average with One Condition (AVGIF)

To find the average sales revenue for a specific month (e.g., March):

*   **Objective**: Find the average revenue only for the March month <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **MyFormulaGen Steps**:
    1.  Click "New formula" <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
    2.  Paste the Notion database URL <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
    3.  Select "Average" for "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
    4.  Add a condition: Choose the "Date" field, select "Start date is between," and specify the range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
    5.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Saving to Notion**:
    1.  Add a new row in your summary database (e.g., "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
    2.  Use "Add to Notion" in MyFormulaGen, paste the summary database link, and select the correct column and row to save the value <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Verification**: You can verify the result by applying a date filter in Notion for the specified month <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### 3. Average with Multiple Conditions (AVGIFS)

To find the average sales revenue for a specific category within a specific quarter (e.g., "Software" category for Q1):

*   **Objective**: Find the average sales revenue for the "Software" category only for the first quarter (Jan, Feb, March) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   **MyFormulaGen Steps**:
    1.  Click "New formula" <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
    2.  Paste the Notion database URL <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
    3.  Select "Average" for "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
    4.  Add the first condition: Choose the "Date" field, "Start date is between," and specify the range (e.g., January 1st to March 31st) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>, <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
    5.  Add a second "AND" condition: Choose the "Category" column and set it to "is software" <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>, <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
    6.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   **Saving to Notion**:
    1.  Add a new row in your summary database (e.g., "Average Sales March 2025 software") <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
    2.  Use "Add to Notion" in MyFormulaGen, paste the summary database link, and select the correct column and row to save the value <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   **Verification**: You can verify the result by applying both date and category filters in Notion <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## Managing Saved Formulas

After calculating and saving values to Notion, you can save the formulas in MyFormulaGen for future use <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

*   **Saving a Formula**: After a calculation, define a name (e.g., "Revenue average") and click "Save" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. The formula will appear under "Saved formulas" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Refreshing Values**: If your Notion database values change, you can update the calculated averages in your summary database:
    *   Go to "Saved formulas" <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   Click "Refresh all" to update all saved formulas at once <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>, <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
    *   Alternatively, click "Refresh formula" next to a specific formula to update only that value <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

This setup allows you to easily calculate and manage various financial metrics in Notion without complex [[using_formulas_in_notion | Notion formulas]] <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. MyFormulaGen offers flexibility for [[utilizing_notion_databases_for_financial_tracking | utilizing Notion databases for financial tracking]] and presenting data <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>, including other functions like [[using_the_sum_function_in_notion | SUM]] and COUNT, similar to what you might find when [[adding_numbers_in_notion | adding numbers in Notion]] or using [[using_formulas_to_calculate_differences_in_notion | formulas to calculate differences in Notion]] <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.