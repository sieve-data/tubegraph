---
title: Calculating averages in Notion databases
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion offers [[using_formulas_in_notion | built-in formulas]], they can sometimes be complicated to understand <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This guide demonstrates how to calculate various averages for data in Notion databases using an external tool, similar to functions like `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` in Excel <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Using MyFormulaGen for Notion Calculations

The external tool used for these calculations is `myformulagen.com` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Setup and Integration

1.  **Log In/Create Account:** Head to `myformulagen.com` and log in or create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Notion Database URL:**
    *   Open your Notion database <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   If it's an inline database, click the six dots next to the database name <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   Click "Copy link" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
    *   Paste this URL into the MyFormulaGen interface <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  **Add Notion API Key:**
    *   In MyFormulaGen, click on "Settings" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Click "Get API key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Click "New integration" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Define a name (e.g., "My API key") <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
    *   Select the workspace to connect (e.g., "Accountant Guy workspace") <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
    *   Click "Save" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Once created, click on the new integration to see its "Internal Integration Secret" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   Click "Show" and copy the entire API key <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   Paste this value back into MyFormulaGen's settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect Notion Page to API Key:**
    *   Go back to the Notion page containing your database <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Click the three dots in the top right corner of the page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Click "Connections" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   Search for and select the API key you just created (e.g., "MyFormulaGen") <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Click "Confirm" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Your page and its databases are now connected <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Calculating Different Types of Averages

Once connected, you can define custom formulas in MyFormulaGen.

### 1. Overall Average Sales Revenue

To find the average of a specific column (e.g., "Revenue") for all rows:
1.  In MyFormulaGen, select "average" for the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  Choose "Revenue" as the column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  Ensure "All rows" is selected for the rows considered <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Saving Results to a Second Notion Database

To populate the calculated average into another Notion database:
1.  [[creating_a_database_in_notion_for_calculations | Create a second inline database]] in Notion (e.g., "DB_Summary") with a "Value" number column <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  Add a new row in this summary database (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
3.  Copy the link to this *second* Notion database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
4.  In MyFormulaGen, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
5.  Paste the second database's link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
6.  Select the "Value" column and the corresponding row (e.g., "Average Sales Revenue") where you want the result saved <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
7.  Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### Saving and Refreshing Formulas

To reuse formulas and update values:
1.  **Save Formula:** Click "Save the formula," give it a name (e.g., "Revenue Average"), and click "Save" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
2.  **Refresh Formula:** If your source data changes, the calculated average in Notion will not update automatically <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    *   Go to "Saved formulas" in MyFormulaGen <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   Click "Refresh formula" next to the specific formula you want to update <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. The value in Notion will then update <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

### 2. Average Sales Revenue for a Specific Month (Conditional)

To find the average for data within a specific date range:
1.  Click "New formula" in MyFormulaGen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
2.  Paste the source database URL <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
3.  Select "average" for "Revenue" for "all rows" <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
4.  Add a condition: choose the "Date" field, select "start date is between," and define the date range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
6.  Add a new row in your summary Notion database (e.g., "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
7.  Use "Add to Notion" to save this value to the correct column and row <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
8.  Save the formula (e.g., "Revenue March 2025") <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### 3. Average Sales Revenue for Specific Category and Quarter (Multiple Conditions)

To find the average with multiple conditions:
1.  Click "New formula" <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
2.  Paste the source database URL <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
3.  Select "average" for "Revenue" for "all rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
4.  Add the first condition: "Date" field, "start date is between," and define the quarter (e.g., January 1st to March 31st for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
5.  Add an "AND" condition by clicking the plus sign <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
6.  Add the second condition: choose the "Category" column and set it to "is software" <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
7.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
8.  Add a new row in your summary Notion database (e.g., "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
9.  Use "Add to Notion" to save this value <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
10. Save the formula (e.g., "Mar 2025 software") <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

### Refreshing All Formulas

After updating multiple values in your source Notion database, you can refresh all saved formulas at once:
*   In MyFormulaGen, go to "Saved formulas" <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   Click "Refresh all" <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. All the calculated values in your summary Notion database will update accordingly <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

This setup provides flexibility for [[using_excellike_formulas_in_notion | calculating values in Notion]] without dealing with complex Notion formulas directly <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. This tool also supports other operations like [[formulas_for_finding_the_sum_of_numbers_in_notion | sum]] and count, similar to Excel <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.