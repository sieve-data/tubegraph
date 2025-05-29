---
title: Creating and saving custom formulas in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion offers [[using_formulas_in_notion | inbuilt formulas]], they can sometimes be complex to understand <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This article outlines how to create and save custom formulas in Notion, especially for calculations like averages, including conditional averages, using an external tool <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. This method is similar to using AVERAGE, AVERAGEIF, and AVERAGEIFS functions in [[how_to_use_excel_formulas_in_notion | Excel]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Utilizing My Formula Gen for Notion Calculations

The external tool used for this purpose is [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### Initial Setup Steps

1.  **Log in to My Formula Gen:** Go to myformulagen.com and create or log into your account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Notion Database URL:**
    *   Open your Notion database (e.g., a sales database with properties like date, product, category, quantity, revenue) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.
    *   If the database is inline, click the six dots icon, then "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Paste this URL into the designated field in [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  **Add API Key:**
    *   In [[using_my_formula_gen_for_notion_calculations | My Formula Gen]], navigate to "Settings" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Click "Get API key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
    *   Click "New integration," define a name (e.g., "My API key"), select the workspace, and click "Save" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Copy the "Internal Integration Secret" (click "Show" to reveal) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Paste this key back into [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect Notion Page to API Key:**
    *   Go back to your Notion page containing the database <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Click the three dots icon on the page, then "Connections" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
    *   Search for and select the API key you just created (e.g., "My Formula Gen") and click "Confirm" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   This connects the Notion page and its databases to the API key <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Calculating Averages

Once the setup is complete, you can define custom formulas to get desired values <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### 1. Simple Average (AVERAGE equivalent)

To find the average sales revenue from a "Revenue" column:
1.  In [[using_my_formula_gen_for_notion_calculations | My Formula Gen]], select the "Average" operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  Choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  Select "All rows" to include all data <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### 2. Conditional Average (AVERAGEIF equivalent)

To find the average sales revenue for a specific month (e.g., March):
1.  Create a new formula in [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
2.  Paste the database link <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
3.  Find the average of "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
4.  Add a condition: where the "Date" field's "start date is between" a specific range (e.g., March 1st and March 31st) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### 3. Multiple Conditional Average (AVERAGEIFS equivalent)

To find the average sales revenue for a specific category (e.g., "Software") within a quarter (e.g., Q1, Jan-Mar):
1.  Create a new formula in [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
2.  Paste the database link <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
3.  Find the average of "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
4.  Add the first condition: where the "Date" field's "start date is between" January 1st and March 31st <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
5.  Add an "AND" condition by clicking the plus button <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
6.  Add the second condition: choose the "Category" column and set it "is software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
7.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

## Saving and Updating Results in Notion

To display these calculated averages in Notion:

1.  **Create a Summary Database:** In your Notion page, create a new inline database (e.g., "DB_Summary") with a "Title" column and a "Value" column set to number format <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  **Add Rows for Each Calculation:** Create new rows in this summary database for each average you want to display (e.g., "Average Sales Revenue," "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
3.  **Copy Summary Database Link:** Click the six dots on your new summary database and select "Copy link" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
4.  **Add to Notion:** In [[using_my_formula_gen_for_notion_calculations | My Formula Gen]], after calculating a value, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
5.  **Paste Link and Select Location:** Paste the summary database link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Select the "Value" column and the specific row where you want the result saved (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
6.  **Save to Notion:** Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The value will automatically populate in your Notion database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Saving Formulas for Future Use

To easily re-run calculations after data changes:
1.  After populating a value in Notion, save the formula in [[using_my_formula_gen_for_notion_calculations | My Formula Gen]] by defining a name (e.g., "Revenue average") and clicking "Save" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
2.  Saved formulas appear under "Saved Formulas" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
3.  If data in your source database changes, simply click "Refresh formula" next to the specific saved formula, or "Refresh all" to update all saved formulas <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The values in your Notion summary database will update automatically <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

## Conclusion

This approach simplifies [[using_excelstyle_formulas_in_notion | Notion calculations]] by leveraging an external tool to create and manage custom formulas <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. It provides flexibility for calculating averages with various conditions and maintaining updated results without complex [[using_formulas_in_notion | Notion formulas]] <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. You can apply this method across multiple Notion databases and for different calculation types like sum or count <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.