---
title: Connecting and saving formula results in Notion databases
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion offers [[using_formulas_in_notion | built-in formulas]], calculating and displaying certain aggregate values, especially in a separate [[creating_a_database_in_notion | database]], can be complex <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. An external tool, MyFormulaGen, simplifies this process by allowing users to define custom formulas and automatically update results in a Notion [[creating_a_database_in_notion | database]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

The process demonstrated involves calculating three types of average sales revenue from a source [[creating_a_database_in_notion | database]] with properties like date, product, category, quantity, and revenue <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>:
1.  Overall average sales revenue <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
2.  Average sales revenue for a specific month (e.g., March) <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
3.  Average sales revenue for a specific category (e.g., software) within a defined quarter (e.g., Q1) <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Setting Up MyFormulaGen

### Account Creation
First, navigate to myformulagen.com and create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Fetching the Source Database URL
To begin, you need the URL of the Notion [[creating_a_database_in_notion | database]] from which values will be calculated <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   If your [[creating_a_database_in_notion | database]] is in a full-page view, click on the "Share" button and then "Copy link" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   If it's an inline [[creating_a_database_in_notion | database]], click on the six dots next to the [[creating_a_database_in_notion | database]] title and select "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   Paste this URL into the MyFormulaGen interface <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Setting Up the API Key and Connecting Notion
MyFormulaGen requires an [[connecting_relational_databases_with_notion_api | API key]] to interact with your Notion workspace <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
1.  In MyFormulaGen, click on "Settings" and then "Get [[connecting_relational_databases_with_notion_api | API key]]" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a> <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This will redirect you to Notion's Integrations page <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
2.  Click on "New integration," define a name (e.g., "My API Key"), and select the relevant workspace <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Click "Save" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
3.  Copy the "Internal Integration Secret" from the newly created integration <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
4.  Paste this secret into the [[connecting_relational_databases_with_notion_api | API key]] field in MyFormulaGen settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a> <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
5.  Finally, in your Notion page containing the source [[creating_a_database_in_notion | database]], click the three dots in the top right corner, select "Add connections," and choose the integration you just created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a> <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This connects the page and its contained [[creating_a_database_in_notion | databases]] to MyFormulaGen <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Calculating and Saving Averages

### Step 1: Overall Average Sales Revenue
To calculate the overall average of a numerical column (e.g., "Revenue") <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>:
1.  In MyFormulaGen, select "Average" as the operation and choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a> <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
2.  Set the range to "all rows" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
3.  **To save this to Notion**:
    *   Create a second Notion [[creating_a_database_in_notion | database]] (e.g., "DB_Summary") within the same page, with columns like "Title" and "Value" (set as a number property) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Add a new row in this summary [[creating_a_database_in_notion | database]] (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
    *   Copy the link of this *second* summary [[creating_a_database_in_notion | database]] <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   In MyFormulaGen, click "Add to Notion," paste the summary [[creating_a_database_in_notion | database]] link, select the "Value" column, and choose the "Average Sales Revenue" row <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
    *   Click "Save to Notion" to update the value in your summary [[creating_a_database_in_notion | database]] <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
4.  **Save the formula**: Give the formula a name (e.g., "Revenue average") and click "Save" for future use <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### Step 2: Average Sales Revenue for a Specific Month (e.g., March)
This involves adding a date condition, similar to `AVERAGEIF` in Excel <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
1.  Click "New Formula" in MyFormulaGen and paste the source [[creating_a_database_in_notion | database]] URL <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
2.  Select "Average" for "Revenue" for "all rows" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
3.  Add a condition: "where the date field's start date is between" March 1st and March 31st <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
5.  Create a new row in your summary [[creating_a_database_in_notion | database]] (e.g., "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
6.  Use "Add to Notion" again, select the summary [[creating_a_database_in_notion | database]], the "Value" column, and the new "March" row <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
7.  Save the formula (e.g., "Revenue March") <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

### Step 3: Average Sales Revenue for Category and Quarter (e.g., Software, Q1)
This involves multiple conditions, similar to `AVERAGEIFS` in Excel <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
1.  Start a "New Formula" and paste the source [[creating_a_database_in_notion | database]] URL <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
2.  Select "Average" for "Revenue" for "all rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
3.  Add the first condition: "where the date field's start date is between" January 1st and March 31st (for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
4.  Add an "AND" condition using the plus button <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
5.  Select the "Category" column and set the condition "is software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
7.  Create a new row in your summary [[creating_a_database_in_notion | database]] (e.g., "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
8.  Use "Add to Notion" to save the result, selecting the appropriate column and row <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
9.  Save the formula (e.g., "Mar 2025 Software") <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

## Updating Formulas and Values
If the data in your source Notion [[creating_a_database_in_notion | database]] changes, the calculated averages in your summary [[creating_a_database_in_notion | database]] will not automatically update <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   To refresh the values, go back to MyFormulaGen's "Saved Formulas" section <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   You can click "Refresh All" to update all saved formulas <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   Alternatively, click "Refresh Formula" next to a specific saved formula to update only that value <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   This ensures your summary [[creating_a_database_in_notion | database]] always reflects the latest calculations from your source data <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

This setup provides flexibility for calculating various metrics and presenting data in different Notion [[creating_a_database_in_notion | databases]] without complex [[using_formulas_in_notion | Notion formulas]] <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.