---
title: Using AVG function in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion has [[using_formulas_in_notion | inbuilt formulas]], complex calculations like conditional averages can be challenging to implement directly within a Notion database <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. An external tool, such as MyFormulaGen, can be used to perform these calculations, similar to [[using_excellike_formulas_in_notion | Excel-like formulas]] like AVERAGE, AVERAGEIF, and AVERAGEIFS <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This method allows for calculation results to be pushed into a separate Notion database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Setting Up MyFormulaGen

To perform average calculations using MyFormulaGen:

1.  **Access the Tool**: Navigate to myformulagen.com and log in or create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Database URL**:
    *   Open your Notion database.
    *   If it's an inline database, click on the six-dot menu (or three dots for full-page database) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   Click "Copy link" <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   Paste this URL into the MyFormulaGen interface <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
3.  **Add API Key**:
    *   In MyFormulaGen, click on "Settings" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   Click "Get API key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Click "New integration" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Define a name (e.g., "My API key") and select your workspace <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
    *   Click "Save" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Copy the "Internal Integration Secret" (click "Show" to reveal) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Paste this API key into the MyFormulaGen settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect Notion Database**:
    *   Go back to your Notion page containing the database.
    *   Click the three dots in the top right corner of the page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Click "Connections" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   Search for and select the API key you just created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Click "Confirm" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This connects the database to the API <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Calculating Average Sales Revenue (Simple AVERAGE)

This calculates the average of a specified column without conditions.

1.  **Select Operation**: In MyFormulaGen, choose "Average" from the operations list <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  **Select Column**: Select the column for which you want to calculate the average (e.g., "Revenue") <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  **Choose Rows**: Select "All rows" to include all entries in the calculation <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  **Calculate**: Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
5.  **Save to Notion Database**:
    *   Create a new Notion database (e.g., `db_summary`) with a "Value" column formatted as a number <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   Add a new row in this summary database (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
    *   Copy the URL of this new summary database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   In MyFormulaGen, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
    *   Paste the summary database link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    *   Select the "Value" column and the corresponding row (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   Click "Save to Notion" to populate the value <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
6.  **Save Formula**: Give the formula a name (e.g., "Revenue Average") and click "Save" for future use <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
7.  **Refresh Data**: If source data changes, click "Refresh formula" (or "Refresh all") in MyFormulaGen to update the value in Notion <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## [[implementing_avgif_and_avgifs_formulas_in_notion | Calculating Average Sales Revenue for March (AVERAGEIF)]]

This demonstrates [[implementing_avgif_and_avgifs_formulas_in_notion | implementing AVGIF and AVGIFS formulas in Notion]] for a single condition.

1.  **New Formula**: Click "New formula" in MyFormulaGen and paste the primary database URL <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
2.  **Define Condition**:
    *   Select "Average" of "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
    *   Add a condition: "Date field" > "Start date" > "is between" <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   Specify the date range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
3.  **Calculate & Save**: Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>, then add a new row in your summary database (e.g., "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. Use "Add to Notion" to populate this value <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
4.  **Verify (Optional)**: You can verify the result in Notion by applying a filter to your original database for the specified month and observing the calculated average at the bottom of the column <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
5.  **Save Formula**: Save the formula (e.g., "Revenue March") <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

## [[implementing_avgif_and_avgifs_formulas_in_notion | Calculating Average Sales Revenue for Software Category in Q1 (AVERAGEIFS)]]

This demonstrates [[implementing_avgif_and_avgifs_formulas_in_notion | implementing AVGIF and AVGIFS formulas in Notion]] for multiple conditions.

1.  **New Formula**: Click "New formula" and paste the primary database URL <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
2.  **Define Conditions**:
    *   Select "Average" of "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
    *   Add the first condition: "Date field" > "Start date" > "is between" (e.g., January 1st to March 31st for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
    *   Click "plus" to add an "AND" condition <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
    *   Add the second condition: "Category" > "is" > "Software" <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
3.  **Calculate & Save**: Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>, then add a new row in your summary database (e.g., "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Use "Add to Notion" to populate this value <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
4.  **Verify (Optional)**: Apply both category and date filters in Notion to confirm the average <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
5.  **Save Formula**: Save the formula (e.g., "Mar 2025 Software") <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

### Refreshing All Formulas

Once multiple formulas are saved, you can click "Refresh all" in MyFormulaGen to update all linked values in your Notion summary database simultaneously <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

This approach provides significant flexibility for [[using_notion_for_calculations | calculating sum values with external tools in Notion]] and other operations beyond simple averages, including [[calculating_the_sum_of_a_column_in_notion | sum]] and count, similar to functionalities found in Excel <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. Remember to specify "All rows" or define custom ranges/rows as needed for your calculations <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.