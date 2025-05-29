---
title: Creating and saving custom formulas in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

This article details how to create and save custom formulas in Notion, particularly for calculating averages, including conditional averages, by integrating an external tool. This method addresses the complexities that can arise when using Notion's built-in formulas and allows results to be saved to a separate database <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Why Use External Tools for Notion Formulas?

While Notion has built-in formulas, they can sometimes be complicated to understand <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. An external tool allows for the calculation of various metrics, such as averages (similar to AVERAGE, AVERAGEIF, and AVERAGEIFS functions in Excel), and the saving of these results into a separate Notion database <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Tool Setup: MyFormulaGen

The process involves using an external tool called MyFormulaGen <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Accessing MyFormulaGen and Logging In
First, navigate to myformulagen.com and create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Fetching Notion Database URL
To calculate values, you need to provide the database URL from Notion <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   For an inline database, click on the six dots icon next to the database name and select "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   For a full-page database, click on the three dots at the top right, then "Copy link" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Paste this URL into MyFormulaGen <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Setting Up API Key
An API key is required for MyFormulaGen to connect to your Notion workspace <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
1.  In MyFormulaGen, click on "Settings" and then "Get API key" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  This redirects you to Notion's API page where you can create a new integration <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  Click "New integration," define a name (e.g., "My API Key"), and select the relevant Notion workspace <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
4.  Save the integration <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
5.  Copy the "Internal Integration Secret" (API key) and paste it into MyFormulaGen's settings, then click "Save changes" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Connecting Notion Page to API Key
After setting up the API key, you need to connect the Notion page containing your database to this API key <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
1.  In Notion, go to the page with your database.
2.  Click on the three dots in the top right corner of the page <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  Select "Add connections" (or "Connections") and search for the name of your API key (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
4.  Confirm the connection <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This connects both the page and the database within it <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Creating Custom Formulas

Once the setup is complete, you can define [[creating_and_saving_formulas_in_notion | custom formulas]] in MyFormulaGen.

### 1. Calculating Simple Average Sales Revenue
To find the average of a column (e.g., "Revenue") for all rows <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>:
1.  In MyFormulaGen, select "average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  Choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  Select "all rows" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
5.  **Saving to Notion**:
    *   [[creating_a_database_in_notion_for_calculations | Create a second database]] in Notion to store the results, for example, named `db_summary` with a "Value" column formatted as a number <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Create a new row in this summary database, e.g., "Average Sales Revenue" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   In MyFormulaGen, click "Add to Notion," paste the URL of the `db_summary` database, select the "Value" column, and the "Average Sales Revenue" row <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
    *   Click "Save to Notion" to update the value <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
6.  **[[creating_and_saving_formulas_in_notion | Saving the Formula]]**: Give the formula a name (e.g., "Revenue average") and click "Save" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This saves it under "Saved Formulas" for future use <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### 2. Calculating Average Sales Revenue for March Month
To find the average of "Revenue" only for the month of March <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>:
1.  Click "New Formula" in MyFormulaGen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
2.  Paste the original database link <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
3.  Select "average" for "Revenue" and "all rows" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
4.  Add a condition: Choose "Date field start date is between" and set the range from March 1st to March 31st <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
6.  Add a new row in your summary database (e.g., "Average Sales Revenue March 2025") and save the value using "Add to Notion" as before <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
7.  [[creating_and_saving_formulas_in_notion | Save the formula]] (e.g., "Revenue March 2025") <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### 3. Calculating Average Sales Revenue for Software Category in Q1
To find the average of "Revenue" for the "Software" category during Quarter 1 (Jan-Mar) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>:
1.  Click "New Formula" and paste the original database link <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
2.  Select "average" for "Revenue" <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
3.  Add the first condition: "Date field start date is between" Jan 1st and March 31st (for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
4.  Add an "and" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
5.  Add the second condition: Choose the "Category" column and set it to "is software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
7.  Add a new row in your summary database (e.g., "Average Sales March 2025 Software") and save the value <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
8.  [[creating_and_saving_formulas_in_notion | Save the formula]] (e.g., "Mar 2025 Software") <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

## Refreshing and Updating Formulas

After modifying data in your source Notion database, the calculated values in your summary database will become outdated <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   To update a specific formula, go to "Saved Formulas" in MyFormulaGen and click "Refresh formula" next to the desired entry <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   To update all saved formulas, click "Refresh all" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This will refresh all values in the target Notion database <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

## Flexibility and Other Operations

This setup provides flexibility for various calculations <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. Besides [[using_formulas_to_calculate_averages_in_notion | average]], the tool supports other operations like [[using_formulas_to_add_numbers_in_notion | sum]] and count, similar to [[using_excelstyle_formulas_in_notion | Excel-style formulas]] <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. You can choose to calculate for "all rows," a specific "range," or "custom rows" <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This method allows you to easily [[refreshing_and_updating_formulas_in_notion_databases | refresh and update formulas in Notion databases]] for various analytical needs <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.