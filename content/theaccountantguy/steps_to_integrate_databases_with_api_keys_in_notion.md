---
title: Steps to integrate databases with API keys in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

Notion's built-in formulas can sometimes be complex to understand <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. While Notion can display averages directly <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>, putting these calculated values into a *second* Notion database requires an external tool <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This article outlines the steps to integrate Notion databases using an external tool like MyFormulaGen to perform calculations and push results to another database <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Prerequisites

*   An active account on MyFormulaGen.com <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   An existing Notion database with data, such as a sales database containing date, product, category, quantity, and revenue properties <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Steps for Integration

### 1. Fetching the Database URL

To begin, you need to obtain the URL of the Notion database from which you want to calculate values <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   If your database is displayed inline, click on the six dots next to its title and select "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   If it's a full-page database, click on it to open, then click the three dots in the top right corner and select "Copy link" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Paste this URL into the designated field in MyFormulaGen <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### 2. [[setting_up_api_keys_in_notion | Setting Up API Keys in Notion]]

An API key is essential for MyFormulaGen to interact with your Notion workspace <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This key is confidential and for your use only <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

1.  In MyFormulaGen, navigate to "Settings" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  Click on "Get API key" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, which will redirect you to Notion's API page <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  Click "New integration" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
4.  Define a name for your API key (e.g., "My API key") <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
5.  Select the Notion workspace you are currently using <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
6.  Click "Save" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
7.  Once created, click on the new integration to reveal its "Internal Integration Secret" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Click "Show" to see the full key <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
8.  Copy this secret value <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a> and paste it into the API key field in MyFormulaGen, then click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### 3. [[connecting_a_database_in_notion | Connecting the Notion Database to the API Key]]

After setting up the API key in MyFormulaGen, you must connect your Notion page (and thus the database within it) to this key.

1.  Go back to the Notion page containing your database <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
2.  Click the three dots in the top right corner of the page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  Click on "Connections" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
4.  Search for and select the API key you just created (e.g., "my formula G") <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
5.  Click "Confirm" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   Your entire Notion page is now connected to the API key, and by default, any databases inside that page are also connected <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### 4. Defining Formulas and Calculating Values

With the connection established, you can now define custom formulas in MyFormulaGen to get desired values <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

*   **Simple Average**: To find the average of a column (e.g., "Revenue"), select the average operation and the target column ("Revenue") <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. You can choose to calculate for "all rows," "first five rows," "custom rows," or "even rows" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Conditional Average**: To find an average based on a condition (e.g., average sales revenue for March), add a condition using the "where" clause <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. For dates, you can specify a range (e.g., "date field start date is between March 1 and March 31") <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Multiple Conditional Averages**: For multiple conditions (e.g., average sales revenue for "Software" category in Q1), add an "and" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Define the date range (e.g., "Jan 1 till March 31") and the category condition (e.g., "category column is software") <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

### 5. [[creating_a_database_in_notion | Creating a Second Database]] in Notion for Output

You will need a second database in Notion to store the calculated results from MyFormulaGen <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
1.  On your Notion page, click "plus" and choose "database inline" <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
2.  Rename it (e.g., "db_summary") <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
3.  Create a "Value" column, ensuring its format is set to "Number" <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
4.  Add new rows to this database for each calculation you want to store (e.g., "Average Sales Revenue," "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### 6. [[connecting_notion_database_to_pdf_output_via_api_keys | Saving Results to Notion]]

Once a calculation is performed in MyFormulaGen, you can save it directly to your Notion output database.

1.  Copy the link of the second Notion database you created for summary results <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
2.  In MyFormulaGen, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
3.  Paste the link of the second database <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Select the target column (e.g., "Value") and the specific row where you want the result to be saved (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
5.  Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The value will automatically populate in your Notion database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### 7. Saving and Refreshing Formulas

To reuse your defined formulas and keep your Notion database updated:

1.  **Save the Formula**: After a successful calculation and saving to Notion, click "Save the formula" in MyFormulaGen <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Give it a name (e.g., "Revenue average") <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. Saved formulas are accessible under "Saved formulas" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
2.  **Refresh Values**: If you update values in your source Notion database (e.g., change revenue numbers) <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>, MyFormulaGen will still show the old average <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
    *   To update a single value, navigate to "Saved formulas," select the specific formula, and click "Refresh formula" <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
    *   To update all saved formulas, click "Refresh all" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This will update all corresponding values in your Notion output database <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

This setup allows you to easily create and save formulas, then update Notion values with a single click after making changes to your source data <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

For any questions, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.