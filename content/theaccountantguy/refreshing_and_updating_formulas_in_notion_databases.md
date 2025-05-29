---
title: Refreshing and updating formulas in Notion databases
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 
This article details how to refresh and update calculated values in Notion databases, especially when these calculations are performed using an external tool like My Formula Gen. While Notion has [[using_formulas_and_rollup_properties_in_notion | inbuilt formulas]], they can be complex, and displaying results in a separate database requires specific steps for [[dynamic_updating_of_expenses_in_notion | dynamic updating]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Overview of Calculation and Updating Process

The process involves:
1.  [[creating_a_database_in_notion_for_calculations | Creating a database in Notion]] for raw data (e.g., sales revenue, product category, date) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.
2.  Creating a second Notion database to store the calculated summary values <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
3.  Using an external tool (My Formula Gen) to perform calculations like [[using_formulas_to_calculate_averages_in_notion | finding averages]] or other [[using_excelstyle_formulas_in_notion | Excel-style formulas]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
4.  [[creating_and_saving_formulas_in_notion | Creating and saving custom formulas in Notion]] within the external tool <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
5.  Populating the calculated results into the second Notion database <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
6.  Refreshing these values when the source data changes <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

## Setting Up for Calculations and Updates

Before refreshing, the initial setup is crucial:

### Linking Notion Databases to My Formula Gen
1.  **Fetch Database URL**: Copy the URL of the Notion database containing the raw data <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This can be done by clicking the six dots of an inline database and selecting "Copy link" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Paste this URL into the designated field in My Formula Gen <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
2.  **Add API Key**: In My Formula Gen settings, generate and add an API key <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This key is confidential and unique to your use case <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
    *   Create a "New integration" in Notion's API page <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, define a name, and select your workspace <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
    *   Copy the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a> and paste it into My Formula Gen's settings <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
3.  **Connect Notion Page to API**: Go to the Notion page containing your database, click the three dots, select "Connections," and connect it to your newly created API key <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This ensures the database is connected by default <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Creating and Saving Formulas
Once connections are set up, you can [[creating_and_saving_formulas_in_notion | define custom formulas]]:
1.  **Define Formula**: Select the desired operation (e.g., "average") and the target column (e.g., "Revenue") <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. You can specify conditions like "all rows," a specific range, or custom rows <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. You can also add conditional criteria, similar to `AVERAGEIF` or `AVERAGEIFS` in Excel, such as filtering by date range or category <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>, <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
2.  **Calculate**: Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
3.  **Save to Notion**:
    *   Create a second Notion database for results (e.g., "DB_Summary") with a column for values <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Copy the link of this second database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   In My Formula Gen, click "Add to Notion," paste the second database link <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>, select the target column (e.g., "Value") and the specific row where you want to save the result <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   Click "Save to Notion" to populate the value <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
4.  **Save Formula for Future Use**: After successfully populating a value, save the formula within My Formula Gen by defining a name (e.g., "Revenue average") and clicking "Save" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This ensures the formula is available in your "Saved formulas" list <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## Refreshing and Updating Formulas

Once formulas are saved, they can be refreshed to reflect changes in the source data.

### When to Refresh
Whenever you make changes to the numerical values or other data points in your primary Notion database that affect the calculated results, you need to refresh the formulas <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. Otherwise, the second database will show the old calculated values <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### How to Refresh
1.  **Refresh a Single Formula**:
    *   Go to the "Saved formulas" section in My Formula Gen <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   Locate the specific formula you want to update.
    *   Click the "Refresh formula" button next to that formula <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. The value in your Notion database will update <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

2.  **Refresh All Saved Formulas**:
    *   If you have multiple saved formulas and wish to update all of them simultaneously, click the "Refresh all" button in the "Saved formulas" section <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>, <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. All associated values in your Notion database will be refreshed accordingly <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

### Example of Dynamic Updating

Consider a database of sales revenue, product, category, and date <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

*   **Objective 1: Average Sales Revenue (All Rows)**
    *   Initial calculation: Average Revenue is 7002 <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   After changing some revenue values (e.g., from 10 to 1000, 170 to 2000, etc.) <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
    *   Refreshing the formula updates the average to 1755 <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

*   **Objective 2: Average Sales Revenue for March Month**
    *   Initial calculation: Average for March is 362 <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This is confirmed by filtering in Notion <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
    *   After changes to source data, refreshing updates the March average to 2000 <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

*   **Objective 3: Average Sales Revenue for Software Category in Q1**
    *   Initial calculation: Average for Software in Q1 (Jan 1 - March 31) is 458 <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>, <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This is confirmed by filtering in Notion <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
    *   After changes to source data, refreshing updates this average to 2000 <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

This system allows for flexible calculations and [[dynamic_updating_of_expenses_in_notion | dynamic updates]] across Notion databases without complex [[using_formulas_and_rollup_properties_in_notion | Notion formulas]] <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.