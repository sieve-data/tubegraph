---
title: Connecting Notion databases with external tools using API keys
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion offers [[setting_up_a_database_in_notion | built-in formulas]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, they can sometimes be complex <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. To perform more advanced calculations, such as finding specific averages, and then displaying these results in a separate Notion database, external tools can be utilized <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This process involves [[utilizing_api_keys_to_connect_notion_to_pdf_generation_tools | connecting Notion databases]] to external services via API keys <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Using MyFormulaGen to Calculate Averages

An external tool called MyFormulaGen can be used to calculate complex averages and push them to a Notion database <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This is analogous to `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` functions in Excel <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Initial Setup

1.  **Access MyFormulaGen:** Navigate to myformulagen.com and create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Database URL:**
    *   Open your Notion database.
    *   If it's an inline database, click the six dots next to the database name <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, then select "Copy link" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
    *   If it's a full-page database, click on the three dots at the top right <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, then "Copy link to view" <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   Paste this URL into the designated field in MyFormulaGen <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### [[configuring_api_keys_for_notion_integration | Configuring API Keys for Notion Integration]]

To allow MyFormulaGen to interact with your Notion data, you need to create and connect an API key:

1.  **Generate API Key:**
    *   In MyFormulaGen, go to "Settings" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a> and click "Get API key" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This redirects you to Notion's API page <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Click "New integration" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, give it a name (e.g., "My API Key") <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, and select your workspace <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. Click "Submit" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Once created, click on the new integration to reveal the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Click "Show" and copy this secret <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
2.  **Add API Key to MyFormulaGen:** Paste the copied API key into the "API key" field in MyFormulaGen's settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
3.  **Connect Notion Page to API Key:**
    *   Go back to the Notion page containing your database.
    *   Click the three dots at the top right of the Notion page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Select "Connections" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a> and search for the name of the API key you just created <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a> (e.g., "MyFormulaGen").
    *   Click on it and "Confirm" to connect the page and its databases to the API key <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Defining and Saving Formulas

Once the connection is established, you can define custom formulas in MyFormulaGen.

#### Example 1: Average Sales Revenue (All Rows)

To find the average of a column (e.g., "Revenue") for all rows <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>:

1.  In MyFormulaGen, select the "Average" operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  Choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  Set the row consideration to "All rows" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a> to see the result <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

#### Example 2: Average Sales Revenue for March

To find the average revenue for a specific month (e.g., March) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>:

1.  In MyFormulaGen, select "Average" for the "Revenue" column <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
2.  Add a condition: "Date field" > "Start date" > "is between" <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
3.  Define the date range, for example, "March 1" to "March 31" <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

#### Example 3: Average Sales Revenue for Software Category in Q1

To calculate the average revenue for a specific category and quarter <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>:

1.  Select "Average" for the "Revenue" column <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
2.  Add the first condition: "Date field" > "Start date" > "is between" "January 1" to "March 31" (for Quarter 1) <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
3.  Add an "AND" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>: "Category column" > "is" > "Software" <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

### [[connecting_notion_database_with_pdf_output | Connecting Notion database with PDF output]] (Outputting to a Second Database)

To save the calculated values in a separate Notion database:

1.  **Create a Summary Database:** In Notion, create a new inline database (e.g., `db_summary`) with a "Title" column and a "Value" column formatted as a number <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Add rows for each average you want to store (e.g., "Average Sales Revenue", "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
2.  **Copy Summary Database Link:** Get the link to this new summary database <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
3.  **Add to Notion (MyFormulaGen):**
    *   In MyFormulaGen, after calculating a value, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
    *   Paste the summary database link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    *   Select the target "Value" column and the specific row (e.g., "Average Sales Revenue") where you want to save the result <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The value will automatically populate in your Notion database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Saving and Refreshing Formulas

To reuse formulas and update values:

1.  **Save Formula:** After a calculation, define a name for the formula (e.g., "Revenue average") <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a> and click "Save" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. Saved formulas appear under "Saved formulas" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
2.  **Refresh Values:** If your source data in Notion changes <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>:
    *   Click "Refresh all" to update all saved formulas <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   Alternatively, select a specific saved formula and click "Refresh formula" <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The updated average will reflect in your summary database <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

This approach demonstrates how to connect [[using_databases_for_financial_tracking_in_notion | Notion databases]] to external tools using API keys <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>, allowing for calculations beyond Notion's native capabilities and seamless integration of results <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.