---
title: Filtering data by date and category in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion offers built-in formulas, more complex calculations like conditional averages (similar to `AVERAGEIF` or `AVERAGEIFS` in Excel) can be challenging to implement directly <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This article demonstrates how to filter data by date and category in Notion using an external tool called MyFormulaGen to calculate specific averages and populate them into a separate Notion database <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Setup: Connecting Notion to MyFormulaGen

To perform advanced filtering and calculations, you first need to connect your Notion workspace to MyFormulaGen.

### 1. Get Your Database URL
First, identify the Notion database containing the data you wish to analyze (e.g., a sales database with columns like Date, Product, Category, Quantity, and Revenue) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.
*   Open your Notion page with the database <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   If your database is inline, click the six dots next to it and select "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   Paste this URL into the designated field on MyFormulaGen <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### 2. Create and Connect an API Key
MyFormulaGen requires an API key to interact with your Notion workspace <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   In MyFormulaGen, navigate to "Settings" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Click "Get API Key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   Click "New integration," define a name (e.g., "My API Key"), select the relevant Notion workspace, and click "Save" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   Copy the "Internal Integration Secret" that is generated <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   Paste this API key back into MyFormulaGen's settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   Finally, in Notion, on the page containing your database, click the three dots in the top right corner, select "Connections," and connect the API key you just created <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This connects both the page and the database within it <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Calculating Averages with Filters

Once setup is complete, you can define custom formulas in MyFormulaGen to calculate filtered averages. The results will be stored in a second Notion database, which you create for summary purposes <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### 1. Simple Average (No Filter)
To calculate a general average (e.g., average sales revenue) for all rows in a database:
*   In MyFormulaGen, select the "Average" operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   Set the row consideration to "All rows" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   To save this value to a Notion database (e.g., `db_summary` with a 'Value' column), create a new row (e.g., "Average Sales Revenue") in the summary database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   In MyFormulaGen, click "Add to Notion," paste the link of your summary database, select the target column ("Value") and the specific row ("Average Sales Revenue"), then click "Save to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

### 2. Filtering by Date (e.g., Average Sales Revenue for March)
To find the average for a specific month:
*   Click "New formula" in MyFormulaGen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   Paste your source database URL <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   Select "Average" for the "Revenue" column, considering "All rows" <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   Add a condition: Choose the "Date" field, select "Start date is between," and define the range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   Add this value to a new row in your summary database (e.g., "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

### 3. Filtering by Date and Category (e.g., Average Sales Revenue for Software Category in Q1)
For more complex filtering with multiple conditions:
*   Click "New formula" <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   Paste your source database URL <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   Select "Average" for the "Revenue" column, considering "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   Add the first condition: "Date" field, "Start date is between," defining the quarter (e.g., January 1st to March 31st for Q1) <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   Add an "AND" condition <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   Add the second condition: Choose the "Category" column and set it to "is Software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   Add this value to a new row in your summary database (e.g., "Average Sales - March 2025 Software") <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

## Saving and Updating Formulas

After setting up a formula, you can save it for future use.
*   Click "Save" in MyFormulaGen and provide a name (e.g., "Revenue Average") <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   Saved formulas appear under "Saved Formulas" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   If your source data changes, you can refresh the calculated values in Notion. Either click "Refresh All" to update all saved formulas, or select a specific formula and click "Refresh Formula" to update only that one <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

This approach provides a flexible way to perform complex filtered calculations on your Notion data without relying on intricate Notion formulas directly <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.