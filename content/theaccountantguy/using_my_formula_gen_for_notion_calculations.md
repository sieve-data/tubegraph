---
title: Using My Formula Gen for Notion calculations
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

This article explains how to calculate the average of numbers in Notion, particularly when Notion's built-in formulas might be complicated <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. While Notion can display an average directly <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>, this method focuses on putting calculated average values into a *different* database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

This process is similar to calculating `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` functions found in [[how_to_use_excel_formulas_in_notion | Excel]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Introducing My Formula Gen

To achieve these calculations, an external tool called My Formula Gen (myformulagen.com) is used <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Setting Up My Formula Gen

1.  **Create an Account**: Head to myformulagen.com and log in or create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Database URL**:
    *   In Notion, open the database you want to calculate values from <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   If the database is full-page, click on the three dots icon in the top right, then "Copy link" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   If it's an inline database, click the six dots icon next to the database title, then "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Paste this URL into the My Formula Gen interface <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
3.  **Add API Key**:
    *   In My Formula Gen, click on "Settings" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   Click "Get API key" to be redirected to the Notion API page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Click "New integration," define a name (e.g., "My API key"), select your workspace, and save <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Copy the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Paste this API key into My Formula Gen's settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect Notion Page to API**:
    *   Go back to the Notion page containing your database <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Click the three dots icon in the top right of the page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Click "Add connections" and search for the API key you just created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   Select it and click "Confirm" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This connects the page and its databases to the API key <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Calculating Averages with My Formula Gen

Once set up, you can define custom formulas to get desired values <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Objective 1: Average Sales Revenue

The first objective is to find the overall average of the "Revenue" column <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

1.  **Configure Formula**: In My Formula Gen, select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Choose "Revenue" as the column to average <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. Select "All rows" to consider all entries <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
2.  **Calculate**: Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
3.  **Populate in Notion**:
    *   Create a *second* Notion database (e.g., "DB_Summary") within the same page <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Add a "Value" column, formatted as "Number" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   Add a new row in this summary database (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   Copy the link of this second database <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
    *   In My Formula Gen, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Paste the second database link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    *   Select "Value" as the target column and the "Average Sales Revenue" row <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   Click "Save to Notion" to update the value <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
4.  **Save Formula**: Click "Save formula," give it a name (e.g., "Revenue average"), and save <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This formula will appear under "Saved Formulas" <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
5.  **Refresh Values**: If the source data changes, click "Refresh formula" next to the saved formula to update the value in Notion <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. You can also click "Refresh all" to update all saved formulas <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### Objective 2: Average Sales Revenue for March

This objective adds a condition: calculate the average sales revenue *only* for the month of March <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

1.  **New Formula**: Click "New formula" in My Formula Gen and paste the primary database URL <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
2.  **Configure Conditions**:
    *   Choose "Average" for "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
    *   Add a condition: "Date field" (the start date) "is between" "March 1" and "March 31" <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
3.  **Calculate and Populate**: Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. Add a new row in your summary database (e.g., "Average Sales Revenue March 2025"), then use "Add to Notion" to populate the value as described previously <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
4.  **Save Formula**: Save this formula as "Revenue March 2025" <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

### Objective 3: Average Sales Revenue for Software Category in Q1

This objective involves multiple conditions: average sales revenue for the "Software" category *and* for the first quarter (January 1st to March 31st) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

1.  **New Formula**: Click "New formula" and paste the primary database URL <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
2.  **Configure Multiple Conditions**:
    *   Choose "Average" for "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
    *   Add the first condition: "Date field" (start date) "is between" "January 1" and "March 31" <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
    *   Click the "plus" icon to add an `AND` condition <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
    *   Add the second condition: "Category" column "is" "Software" <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
3.  **Calculate and Populate**: Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. Add a new row in your summary database (e.g., "Average Sales March 2025 Software"), and use "Add to Notion" to populate the value <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
4.  **Save Formula**: Save this formula as "Mar 2025 software" <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

## Conclusion

This setup allows you to easily calculate complex averages and other operations that function similarly to [[using_excelstyle_formulas_in_notion | Excel-style formulas]] like `AVERAGEIF` and `AVERAGEIFS` within Notion <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. By [[creating_and_saving_custom_formulas_in_notion | creating and saving custom formulas]], and refreshing them as needed, you can maintain updated values in a summary database <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This method offers flexibility in how you present your data <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

Besides average, My Formula Gen also offers other operations like sum and count, similar to those defined in Excel <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. Ensure to select "All rows" or define specific "Custom rows" or "Range" as needed <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

For any questions, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.