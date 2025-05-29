---
title: Using Excel formulas in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

This article explains how to find the average of numbers in Notion, mimicking [[Using Excellike formulas in Notion | Excel's]] `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` functions <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. While Notion has [[Using formulas in Notion | inbuilt formulas]], they can be complex to understand <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, especially when trying to display calculated averages in a separate database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This method uses an external tool, MyFormulaGen.com <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, to simplify these calculations.

## Setting Up MyFormulaGen

To use MyFormulaGen for calculations in Notion, you need to set up the connection between the tool and your Notion workspace.

### 1. Create an Account and Log In

*   Go to MyFormulaGen.com and create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Once logged in, you'll see its interface <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### 2. Fetch Your Notion Database URL

The first step within MyFormulaGen is to provide the URL of the Notion database you want to perform calculations on <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

*   In Notion, open your database (either full page or inline) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   Click the "..." (three dots) icon at the top right of the database <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Select "Copy link" <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   Paste this URL into the designated field on MyFormulaGen <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   *Alternative for inline databases:* Click the six dots next to the database title, then "Copy link" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### 3. Generate and Add an API Key

An API key is required for MyFormulaGen to interact with your Notion workspace <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

*   In MyFormulaGen, click on "Settings" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Click "Get API Key" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, which will redirect you to Notion's API page <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   Click "+ New integration" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   Define a name for your API key (e.g., "My API key") <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   Select the Notion workspace you are using <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   Click "Save changes" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   Once created, click on your new integration to reveal the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   Click "Show" and copy the entire API key <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   Paste this key back into MyFormulaGen's settings <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> and click "Save settings" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### 4. Connect Notion Database to API Key

The final connection step ensures the Notion page containing your database can be accessed by the API key <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

*   In Notion, go back to the page where your database is located <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   Click the "..." (three dots) icon at the top right of the *page* <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   Click "Connections" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   Search for and select the API key you just created (e.g., "MyFormulaGen") <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   Click "Confirm" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   The database within this page will now be connected by default <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Calculating Averages with MyFormulaGen

Once set up, you can define [[Creating custom formulas in Notion | custom formulas]] in MyFormulaGen to get desired values <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### 1. Find Average Sales Revenue (Simple Average)

To find the average of a column, such as "Revenue," across all rows <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>:

*   In MyFormulaGen, select the "Average" operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Choose "Revenue" as the column <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   Select "All rows" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a> to see the result <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### 2. Save Result to a Notion Database

To display the calculated average in a separate Notion database:

*   [[Creating a database in Notion for calculations | Create a new inline database]] in Notion (e.g., "DB_Summary") with a `Title` column and a `Value` column set to "Number" format <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   Add a new row in this summary database (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   In MyFormulaGen, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   Copy the link of your *summary database* <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a> and paste it into MyFormulaGen's second database link field <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   Select "Value" as the column to save to <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a> and select the corresponding row (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a> to update the value in your summary database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### 3. Save Formula for Future Use

To reuse the formula and refresh values when data changes:

*   Click "Save formula" in MyFormulaGen <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   Give it a name (e.g., "Revenue Average") <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a> and click "Save" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. The formula will appear under "Saved Formulas" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   If values in your source database change, click "Refresh formula" next to the saved formula <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, or "Refresh all" to update all saved formulas <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### 4. Find Average Sales Revenue for March (Conditional Average - AVERAGEIF)

To find the average of "Revenue" only for a specific month (e.g., March) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>:

*   Click "New formula" in MyFormulaGen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   Paste your source database URL again <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   Select "Average" of "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   Add a condition:
    *   Click "Add condition" <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
    *   Choose the "Date" field <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   Select "start date is between" <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
    *   Set the date range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   Add a new row in your summary database (e.g., "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   Use "Add to Notion" to save the value to the correct row in your summary database <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   Save this formula (e.g., "Revenue March 2025 average") <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### 5. Find Average Sales Revenue for Software Category and Q1 (Multiple Conditional Average - AVERAGEIFS)

To find the average for a specific category (Software) within a quarter (Q1) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>:

*   Click "New formula" in MyFormulaGen <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   Paste your source database URL <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   Select "Average" of "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   Add the first condition: "Date" field, "start date is between" January 1st to March 31st (for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Add a second `AND` condition:
    *   Click the "+" button to add another condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   Choose the "Category" column <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
    *   Select "is" and enter "Software" <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   Add a new row in your summary database (e.g., "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   Use "Add to Notion" to save the value <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   Save this formula (e.g., "Mar 2025 software") <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

## Conclusion

This setup allows you to easily [[Creating custom formulas in Notion | create custom formulas]] in MyFormulaGen, save them, and refresh them to update values in your Notion database whenever your source data changes <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. MyFormulaGen offers flexibility, including other [[Formulas for finding the sum of numbers in Notion | sum]], count, and more [[Using Excellike formulas in Notion | Excel-like functions]] beyond just average <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. You can also specify calculations for [[Multiplying numbers in Notion | custom rows]] or ranges, not just all rows <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.