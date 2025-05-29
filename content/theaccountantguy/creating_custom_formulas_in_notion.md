---
title: Creating custom formulas in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While [[using_formulas_in_notion | Notion's inbuilt formulas]] can be complicated to understand <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, it's possible to calculate complex averages, similar to AVERAGE, AVERAGEIF, and AVERAGEIFS functions in [[using_excellike_formulas_in_notion | Excel]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This can be achieved by using an external tool to generate and manage these [[creating_formulas_for_common_notion_tasks | custom formulas]] and populate the results into a Notion database <a class="yt-00:00:34">[00:00:34]</a>.

## Tool Used: My Formula Gen

This guide utilizes My Formula Gen, an external tool designed to help users [[creating_formulas_for_common_notion_tasks | create custom formulas]] for Notion <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Setup and Connection

Before [[creating_formulas_for_common_notion_tasks | custom formulas]], you need to connect your Notion database to My Formula Gen:

1.  **Log in to My Formula Gen:** Go to myformulagen.com and create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Database URL:**
    *   In Notion, find the database you want to use for calculations <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   If it's an inline database, click the six dots, then "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Paste this URL into the specified field on My Formula Gen <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
3.  **Add API Key:**
    *   Navigate to "Settings" in My Formula Gen <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Click "Get API key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
    *   Create a "New integration" by defining a name (e.g., "My API Key") and selecting your workspace <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Copy the "Internal Integration Secret" from the newly created API key <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Paste this secret into the API key field in My Formula Gen and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect API Key to Notion Page/Database:**
    *   Go back to your Notion page containing the database <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Click the three dots in the top right corner, then "Connections" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
    *   Search for and select the API key you just created (e.g., "My Formula Gen") and confirm the connection <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This connects the page and its contained database <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Calculating Averages with My Formula Gen

Once connected, you can define [[creating_formulas_for_common_notion_tasks | custom formulas]] to find averages:

### 1. Basic Average (Average Sales Revenue)

This calculates the average of a selected numerical column across all rows <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

*   In My Formula Gen, select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   Ensure "All rows" is selected <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### 2. Conditional Average (Average Sales Revenue for March)

This calculates the average based on a single condition, such as a specific month <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

*   Start a new formula in My Formula Gen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   Select "Average" of the "Revenue" column for "All rows" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   Add a condition:
    *   Select the "Date" field <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
    *   Choose "start date is between" <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
    *   Define the range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### 3. Multiple Conditional Average (Average Sales Revenue for Software in Q1)

This calculates the average based on multiple conditions, using an "AND" logic <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

*   Start a new formula <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   Select "Average" of "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   Add the first condition (Date):
    *   "Date" field, "start date is between" <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
    *   Define the range for Q1 (Jan 1st to March 31st) <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   Add the second condition (Category):
    *   Click the "plus" sign to add an "AND" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   Select the "Category" column <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
    *   Set the condition "is software" <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

## Saving Results to a Second Notion Database

To store the calculated averages:

1.  **Create a Summary Database:**
    *   In Notion, create a new "database - inline" (e.g., `db_summary`) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Add a property named "Value" with a "Number" format <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   Create new rows for each average you plan to save (e.g., "Average Sales Revenue", "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
2.  **Copy Summary Database Link:** Get the link to this new summary database <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
3.  **Add to Notion:**
    *   In My Formula Gen, after calculating a value, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
    *   Paste the link of your summary database <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    *   Select the "Value" column and the specific row where you want to save the result <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The value will populate in your Notion database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

## Saving and Refreshing Formulas

To reuse your [[creating_formulas_for_common_notion_tasks | custom formulas]] and update values:

1.  **Save Formula:** After a successful calculation, click "Save" and give the formula a name (e.g., "Revenue Average") <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Saved [[creating_formulas_for_common_notion_tasks | formulas]] appear under "Saved Formulas" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
2.  **Refresh Values:** If data in your source database changes, the calculated values in your summary database will become outdated <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    *   To update all saved [[creating_formulas_for_common_notion_tasks | formulas]], click "Refresh All" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   To update a specific formula, find it in the "Saved Formulas" list and click "Refresh formula" next to it <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. The new average will then be displayed <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

This process simplifies [[creating_formulas_for_common_notion_tasks | custom formulas]] in Notion, allowing you to calculate various averages without direct Notion formula complications <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. The tool also supports other [[using_excel_formulas_in_notion | Excel-like formulas]] such as sum and count <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.