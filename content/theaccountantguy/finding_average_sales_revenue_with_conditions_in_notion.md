---
title: Finding average sales revenue with conditions in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While [[using_avg_formulas_in_notion | Notion]] has built-in features to display averages, incorporating them into a separate database, especially with specific conditions, can be complex <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. An external tool, MyFormulaGen, can simplify the process of finding average sales revenue, even with multiple conditions, similar to `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` functions in Excel <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Initial Setup: Connecting Notion to MyFormulaGen

To begin, you will need a Notion sales database containing properties such as date, product, category, quantity, and revenue <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

### Step 1: Obtain the Notion Database URL
1.  Navigate to your Notion database <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
2.  If the database is an inline database, click on the six dots next to its title and select "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
3.  If it's a full-page database, click the "Share" button at the top right, then "Copy link" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
4.  Paste this URL into the designated field on MyFormulaGen.com <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Step 2: Generate and Connect a Notion API Key
1.  On MyFormulaGen, go to "Settings" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  Click "Get API Key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
3.  Click "New integration" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
4.  Define a name for your API key (e.g., "My API key") <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
5.  Select the relevant Notion workspace (e.g., "Accountant Guy workspace") <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
6.  Click "Save" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
7.  Copy the "Internal Integration Secret" that is generated <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
8.  Paste this secret into the API key field on MyFormulaGen and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
9.  Return to your Notion page containing the database. Click the three dots menu at the top right, then "Connections," and add the API key you just created (e.g., "MyFormulaGen") <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
10. Confirm the connection <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Your Notion database is now connected <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Calculating Average Sales Revenue

### 1. Overall Average Sales Revenue
To find the average of the entire 'Revenue' column in your sales database:
1.  In MyFormulaGen, select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  Choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  Select "All rows" to include all data entries <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  Click "Calculate" to see the average value <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

To save this value to a separate Notion database:
1.  Create a new inline database in Notion, for example, named "DB_Summary," with a "Value" column formatted as a number <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  Add a new row, such as "Average Sales Revenue" <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
3.  Copy the link of this summary database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
4.  In MyFormulaGen, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
5.  Paste the summary database link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
6.  Select the "Value" column and the "Average Sales Revenue" row <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
7.  Click "Save to Notion" to populate the value <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
8.  Save the formula in MyFormulaGen (e.g., "Revenue Average") for future use <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### 2. Average Sales Revenue for a Specific Month (e.g., March)
To calculate the average for a specific period:
1.  Click "New Formula" in MyFormulaGen <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
2.  Paste your primary database link <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
3.  Select "Average" for the "Revenue" column <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
4.  Add a condition: choose the "Date" field, then "Start date is between," and specify the date range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
6.  Add a new row in your Notion summary database (e.g., "Average Sales Revenue March 2025") and save the calculated value as before <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
7.  Save this new formula in MyFormulaGen <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### 3. Average Sales Revenue with Multiple Conditions (e.g., Software Category, Q1)
For more granular analysis, you can add multiple conditions, similar to [[applying_sumif_and_sumifslike_logic_in_notion | SUMIF and SUMIFS-like logic]]:
1.  Click "New Formula" <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
2.  Paste your primary database link and set up the "Average" for "Revenue" <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
3.  Add the first condition: "Date field" > "Start date is between" > "January 1st" and "March 31st" (for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
4.  Add an "and" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
5.  For the second condition, choose the "Category" column and set "is" to "Software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
7.  Create a new row in your Notion summary database (e.g., "Average Sales March 2025 Software") and save the value <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
8.  Save this formula <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Refreshing Values
If you update data in your primary Notion sales database, the average values in your summary database will not automatically update <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. To refresh them:
1.  Go to the "Saved formulas" section in MyFormulaGen <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
2.  You can either click "Refresh formula" next to a specific saved formula to update only that value, or click "Refresh all" to update all saved formulas at once <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

This method allows you to easily track and display various average sales metrics in Notion without complex [[using_formulas_in_notion | Notion formulas]] <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. The tool also supports other operations like [[calculating_total_sales_using_sum_function_in_notion | SUM]] and COUNT, similar to what's found in Excel <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.