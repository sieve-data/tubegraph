---
title: Using My Formula Gen to connect databases in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

Notion offers built-in formulas for calculations, but they can sometimes be complicated to understand <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. An external tool called My Formula Gen can be used to calculate complex averages, similar to `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` functions in Excel, and display them in a separate Notion database <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a> <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a> <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Setting Up My Formula Gen <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>

To begin, navigate to myformulagen.com and log in or create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Fetching the Database URL <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>

The first step is to get the URL of the Notion [[setting_up_and_using_databases_in_notion | database]] from which you want to calculate values <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a> <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   If your [[creating_a_database_in_notion | database]] is in a full-page format, click on the three dots at the top right of the [[creating_a_database_in_notion | database]] page and select "Copy link" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a> <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   If your [[creating_a_database_in_notion | database]] is an inline [[creating_a_database_in_notion | database]], click on the six dots (block handle) next to the [[creating_a_database_in_notion | database]] title, then click "Copy link" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   Paste this URL into the My Formula Gen interface <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a> <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Setting Up the API Key <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>

Next, you need to add an API key for Notion integration <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
1.  In My Formula Gen, click on "Settings" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
2.  Click "Get API Key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a> <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  Click "New integration," define a name for your integration (e.g., "My API Key"), and select the appropriate workspace <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a> <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a> <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
4.  Click "Save" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
5.  Copy the "Internal Integration Secret" (API key) by clicking "Show" and then copying the value <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a> <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a> <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
6.  Paste this API key into the My Formula Gen settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a> <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a> <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### Connecting Notion Page to API Key <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>

Once the API key is created and saved in My Formula Gen, connect your Notion page containing the [[setting_up_and_using_databases_in_notion | database]]:
1.  Go back to the Notion page with your [[setting_up_and_using_databases_in_notion | database]] <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
2.  Click on the three dots at the top right of the Notion page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a> <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  Select "Connections" <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
4.  Search for and connect the API key you just created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a> <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a> <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
5.  Confirm the connection <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   This connects the entire page and, by default, any [[creating_a_database_in_notion | database]] within that page to the API key <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a> <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a> <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Calculating Averages with My Formula Gen <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>

Once connections are established, you can define custom [[using_formulas_in_notion | formulas]] to get desired values <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a> <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Simple Average (Average Sales Revenue) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>

To find the average of a column (e.g., "Revenue"):
1.  In My Formula Gen, ensure the correct Notion [[setting_up_and_using_databases_in_notion | database]] URL is entered <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
2.  Select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a> <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
3.  Choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a> <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
4.  Select "All rows" to include all data <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
5.  Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a> <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Conditional Average (Average Sales Revenue for March) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a> <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

To find the average based on a single condition (e.g., "March month"):
1.  Enter the Notion [[setting_up_and_using_databases_in_notion | database]] URL <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a> <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
2.  Select "Average" for "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a> <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a> <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
3.  Add a condition: choose the "Date" field, select "Start date is between," and define the date range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a> <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a> <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a> <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a> <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### Multi-Conditional Average (Average Sales Revenue for Software Category in Q1) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a> <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>

To find the average based on multiple conditions (e.g., "Software category" and "Quarter 1"):
1.  Enter the Notion [[setting_up_and_using_databases_in_notion | database]] URL <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a> <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
2.  Select "Average" for "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a> <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
3.  Add the first condition: for the "Date" field, select "Start date is between," and define the quarter range (e.g., January 1st to March 31st for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a> <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a> <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a> <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
4.  Add an "AND" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a> <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
5.  For the second condition, choose the "Category" column and set it to "is software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a> <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a> <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a> <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## Saving Results to a Notion Database <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>

Calculated values can be saved into a separate Notion [[setting_up_and_using_databases_in_notion | database]] for summary or reporting.
1.  Create a new inline [[creating_a_database_in_notion | database]] in your Notion page (e.g., "db\_summary") with a "Value" column formatted as a number <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a> <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a> <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a> <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a> <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a> <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a> <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
2.  Add a new row in this summary [[creating_a_database_in_notion | database]] (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a> <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a> <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
3.  Copy the link to this second summary [[creating_a_database_in_notion | database]] <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a> <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a> <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
4.  In My Formula Gen, after calculating the average, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
5.  Paste the summary [[creating_a_database_in_notion | database]] link into the provided field <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a> <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a> <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
6.  Select the "Value" column and the specific row where you want to save the result (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a> <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a> <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
7.  Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a> <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The value will appear in your Notion summary [[creating_a_database_in_notion | database]] <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a> <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
8.  Save the formula in My Formula Gen for future use (e.g., "Revenue Average") <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a> <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a> <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a> <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## Refreshing Data in Notion <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>

If values in your source Notion [[setting_up_and_using_databases_in_notion | database]] change, you can update the calculated averages in the summary [[creating_a_database_in_notion | database]]:
1.  Go to the "Saved formulas" section in My Formula Gen <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a> <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
2.  You can click "Refresh All" to update all saved [[using_formulas_in_notion | formulas]] <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a> <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
3.  Alternatively, click "Refresh formula" next to a specific saved formula to update only that value <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a> <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a> <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

This process allows for flexible data calculation and presentation in Notion without complex built-in [[using_formulas_in_notion | formulas]] <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. My Formula Gen supports various operations beyond average, such as count and sum <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.