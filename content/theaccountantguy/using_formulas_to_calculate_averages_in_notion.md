---
title: Using formulas to calculate averages in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion offers built-in ways to display averages within a database, more complex calculations, such as averages with specific conditions or saving results to a separate database, often require external tools <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This guide demonstrates how to calculate various types of averages in Notion using My Formula Gen, mimicking functions like `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` from Excel <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Setting Up My Formula Gen

To begin, you will need to set up an account and connect My Formula Gen to your Notion workspace <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

1.  **Access My Formula Gen**: Navigate to myformulagen.com and log in or create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Get Database URL**:
    *   Open your Notion database.
    *   For inline databases, click the "six dots" icon next to the database title and select "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Paste this URL into the specified field in My Formula Gen <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  **Create and Connect API Key**:
    *   In My Formula Gen, go to "Settings" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   Click "Get API Key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Click "New integration," define a name (e.g., "My API Key"), select your workspace, and click "Save" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Copy the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Paste this key back into My Formula Gen settings and click "Save Changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   In your Notion page containing the database, click the three dots menu, select "Connections," and add the API key you just created <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Calculating Averages

My Formula Gen allows for various average calculations, from simple to complex <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### 1. Average Sales Revenue (Simple Average)

To find the average of a specific column across all rows:

1.  In My Formula Gen, select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  Choose the target column (e.g., "Revenue") <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  Select "All rows" for the range <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. The result will be displayed <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

### 2. Average Sales Revenue for a Specific Month (Conditional Average)

To find the average for data within a specific date range (e.g., March):

1.  Click "New Formula" in My Formula Gen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
2.  Paste your database URL <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
3.  Select "Average" for the "Revenue" column, considering "All rows" <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
4.  Add a condition: choose the "Date" field, set "Start date is between," and input the desired date range (e.g., March 1 to March 31) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### 3. Average Sales Revenue for Specific Category and Quarter (Multi-conditional Average)

To find the average based on multiple conditions (e.g., "Software" category and Q1 dates):

1.  Click "New Formula" <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
2.  Paste your database URL <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
3.  Select "Average" for the "Revenue" column, considering "All rows" <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
4.  Add the first condition: "Date" field, "Start date is between," and input the Q1 date range (e.g., January 1 to March 31) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
5.  Add an "AND" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
6.  Add the second condition: choose the "Category" column and set it to "is software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
7.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## Saving Results to a Separate Notion Database

To store these calculated averages in a separate Notion database:

1.  **Create a Summary Database**: In Notion, create a new inline database (e.g., `db_summary`) with a "Title" property and a "Value" property set to "Number" format <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Add rows for each average you want to store (e.g., "Average Sales Revenue," "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
2.  **Copy Summary Database Link**: Click the "six dots" icon next to the summary database and select "Copy link" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
3.  **Add to Notion**: In My Formula Gen, after calculating an average, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
4.  Paste the summary database link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
5.  Select the target "Column" (e.g., "Value") and the specific "Row" where you want to save the result (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
6.  Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The value will update in your Notion summary database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

## [[creating_and_saving_formulas_in_notion | Creating and saving custom formulas in Notion]]

My Formula Gen allows you to [[creating_and_saving_formulas_in_notion | save custom formulas]] for future use and easy refreshing <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

1.  **Save Formula**: After calculating and saving a value to Notion, click "Save the formula" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
2.  Define a name for the formula (e.g., "Revenue average") and click "Save" <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. The formula will appear under "Saved Formulas" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
3.  **Refresh Values**: If your source data in Notion changes, you can update the calculated averages:
    *   Click "Saved Formulas" <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   To refresh a single formula, click "Refresh formula" next to its name <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
    *   To refresh all saved formulas, click "Refresh all" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

This process allows for dynamic average calculations in Notion, overcoming limitations of built-in features <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. Beyond averages, My Formula Gen supports other operations like sum and count, similar to Excel functions <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.