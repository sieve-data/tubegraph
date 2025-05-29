---
title: Setting up and using My Formula Gen in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

This guide explains how to use an external tool, My Formula Gen, to perform advanced calculations like averages in Notion, similar to [[using_excelstyle_formulas_in_notion | Excel-like formulas]] such as AVERAGE, AVERAGEIF, and AVERAGEIFS <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. While Notion has [[using_formulas_in_notion | built-in formulas]], they can sometimes be complicated <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. My Formula Gen helps overcome this complexity by providing a simpler interface to define conditions and perform calculations <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Getting Started with My Formula Gen

### 1. Account Creation and Login
First, navigate to myformulagen.com and either log in or create a new account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### 2. Fetching Notion Database URL
To integrate with Notion, you need the URL of your Notion database.
*   For an inline database, click the six dots next to the database title, then "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   For a full-page database, click on the three dots at the top right, then "Copy link" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
Paste this URL into the My Formula Gen interface where prompted <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### 3. [[setting_up_api_for_integrating_notion_with_myformulagen_tool | Setting up API Integration]]
This step is crucial for My Formula Gen to interact with your Notion workspace <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   In My Formula Gen, click on "Settings" and then "Add an API key" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Clicking "Get API key" will redirect you to Notion's API page <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   On the Notion API page, click "New integration" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   Define a name for your integration (e.g., "My API key") <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   Select the Notion workspace you intend to use <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a> and click "Save" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   Once created, click on the integration name to reveal the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. Click "Show" to view the key <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   Copy this secret value <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> and paste it into the API key field in My Formula Gen, then click "Save changes" <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### 4. Connecting Notion Page to API Key
After [[setting_up_api_for_integrating_notion_with_myformulagen_tool | setting up the API key]] in My Formula Gen, you must connect your Notion page to it:
*   Go back to the Notion page where your database is located <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   Click the three dots at the top right of the Notion page <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   Select "Connections" and then search for and connect to the API key you just created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This connects both the page and the database within it <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Calculating Averages with My Formula Gen

Once the setup is complete, you can define custom formulas. This process generally involves specifying the database, the column for calculation, and any conditions. The results can be saved to a second Notion database for easy viewing <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Example 1: Overall Average Sales Revenue
To find the average of a column (e.g., "Revenue") for all rows <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>:
1.  Enter the Notion database URL in My Formula Gen <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
2.  Select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
3.  Choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
4.  Specify "All rows" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
5.  Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

To save this value to a new Notion database (e.g., `db_summary` with a `Value` column):
1.  Create a new inline database in Notion, add a `Value` column (set to number format), and create a new row (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  Copy the link of this *second* database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
3.  In My Formula Gen, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
4.  Paste the second database link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
5.  Select the "Value" column and the "Average Sales Revenue" row <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
6.  Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The value will now appear in your summary database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Example 2: Average Sales Revenue for a Specific Month (e.g., March)
To calculate a conditional average (similar to AVERAGEIF in Excel) <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>:
1.  Click "New formula" in My Formula Gen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a> and paste the primary database URL <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
2.  Select "Average" of "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
3.  Add a condition: where the "Date" field's "Start date is between" March 1st and March 31st <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
5.  Save this result to a new row in your summary database (e.g., "Average Sales Revenue March 2025") following the steps in Example 1 <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### Example 3: Average Sales Revenue for Specific Category and Quarter (e.g., Software, Q1)
For multiple conditions (similar to AVERAGEIFS in Excel) <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>:
1.  Click "New formula" <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a> and paste the primary database URL <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
2.  Select "Average" of "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
3.  Add the first condition: "Date" field "Start date is between" January 1st and March 31st (for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
4.  Add an "AND" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a> by clicking the plus sign.
5.  Add the second condition: "Category" column "is" "Software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
7.  Save this result to a new row in your summary database (e.g., "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

## [[automating_updates_in_notion_databases_with_myformulagen_tool | Saving and Refreshing Formulas]]
My Formula Gen allows you to save formulas for future use and [[automating_updates_in_notion_databases_with_myformulagen_tool | automate updates]] <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Saving a Formula**: After calculating, click "Save formula", give it a name (e.g., "Revenue average"), and click "Save" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Saved formulas appear in the "Saved Formulas" section <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Refreshing Formulas**: If you update values in your primary Notion database <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>:
    *   To refresh a single formula: Select it from "Saved formulas" and click "Refresh formula" <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
    *   To refresh all saved formulas: Click "Refresh all" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   This will automatically update the corresponding values in your summary Notion database <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>, ensuring your data is always current <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

## Conclusion
My Formula Gen provides a flexible way to calculate various metrics in Notion, including [[adding_numbers_in_notion_using_formulas | sums]] and counts, similar to [[using_excelstyle_formulas_in_notion | Excel-like formulas]] <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. You can define specific rows or ranges for calculations if needed, rather than just "All rows" <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. This setup allows for powerful data analysis and [[automating_updates_in_notion_databases_with_myformulagen_tool | automated updates]] within your Notion workspace <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.