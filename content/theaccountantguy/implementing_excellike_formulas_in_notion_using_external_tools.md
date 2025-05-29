---
title: Implementing Excellike formulas in Notion using external tools
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion has [[using_formulas_in_notion | inbuilt formulas]], they can sometimes be complicated to understand <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This article demonstrates how to calculate averages in Notion, including conditional averages, by leveraging an external tool, [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]], to achieve [[using_excelstyle_formulas_in_notion | Excel-like formulas]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This method simplifies finding values like total average sales revenue, average sales revenue for a specific month (e.g., March), or average sales revenue for a specific category within a quarter (e.g., software in Q1) <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Setting Up My Formula Gen for Notion Integration

To begin, you will need to set up [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] and connect it to your Notion database <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

1.  **Access My Formula Gen**: Go to myformulagen.com and log in or create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Database URL**:
    *   Open your Notion database.
    *   Click the three dots in the top right corner of the database.
    *   Select "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Paste this URL into the designated field in [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  **Generate Notion API Key**:
    *   In [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]], click on "Settings" and then "Get API key" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This redirects you to Notion's API page.
    *   Click "New integration" and define a name for your API key (e.g., "My API key") <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Select your workspace and click "Save" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   Copy the "Internal Integration Secret" (API key) shown <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Paste this API key into the API key field in [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect Notion Page to API Key**:
    *   Go back to your Notion page containing the database.
    *   Click the three dots in the top right corner of the page (not the database itself).
    *   Click "Connections" and select the API key you just created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   Confirm the connection <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This connects both the page and the database within it <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

Once these connections are established, you can define custom [[using_formulas_in_notion | formulas]] in [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] to get desired values <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

## Calculating Averages in Notion

This process simulates [[using_avg_formulas_in_notion | AVERAGE]], AVERAGEIF, and AVERAGEIFS functions found in Excel <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### 1. Simple Average of Sales Revenue

To find the overall average of the "Revenue" column:

1.  In [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]], paste your database URL <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
2.  Select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
3.  Choose "Revenue" as the column to average <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
4.  Ensure "All rows" is selected to consider the entire dataset <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The result will be displayed <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

To save this value to a separate Notion database:

1.  Create a new inline database in Notion (e.g., "DB_Summary") with a "Title" column and a "Value" column (set to Number format) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  Add a new row for your average (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
3.  Copy the link to this new "DB_Summary" database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
4.  In [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]], click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
5.  Paste the "DB_Summary" link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
6.  Select "Value" for the column and the specific row (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
7.  Click "Save to Notion" to populate the value <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

For future use, save the formula in [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] by defining a name (e.g., "Revenue Average") and clicking "Save" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. If data in your source database changes, simply click "Refresh formula" (or "Refresh all" for multiple saved formulas) in [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] to update the Notion summary <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### 2. Conditional Average: Sales Revenue for a Specific Month

To find the average sales revenue only for March:

1.  Start a "New formula" in [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] and paste the source database URL <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
2.  Select "Average" for "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
3.  Add a condition: Choose the "Date" field, set "start date is between," and define the range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
5.  Add a new row in your "DB_Summary" Notion database (e.g., "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
6.  Use "Add to Notion" in [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] to save the value to the correct row <a class="yt-timestamp" data-t="00:09:09">[00:09:10]</a>.
7.  Save this formula (e.g., "Revenue March 2025 Average") for future use <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

### 3. Multi-Conditional Average: Sales Revenue for Category in a Quarter

To find the average sales revenue for the "Software" category only during the first quarter (Q1):

1.  Start a "New formula" in [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] and paste the source database URL <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
2.  Select "Average" for "Revenue" for "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
3.  Add the first condition: Choose the "Date" field, set "start date is between," and define the Q1 range (January 1st to March 31st) <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
4.  Add an "AND" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>: Click the "+" button.
5.  Add the second condition: Choose the "Category" column and set it to "is software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
7.  Add a new row in your "DB_Summary" Notion database (e.g., "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
8.  Use "Add to Notion" in [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] to save the value <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
9.  Save this formula (e.g., "Mar 2025 Software") <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Refreshing Data

After making changes to your source Notion database, you can update all calculated values in your summary database by going to the "Saved Formulas" section in [[setting_up_and_using_my_formula_gen_in_notion | My Formula Gen]] and clicking "Refresh all" <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This will update all saved formulas with the latest data <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

This approach provides a flexible way to implement [[applying_sumif_and_sumifslike_logic_in_notion | SUMIF and SUMIFS-like logic]] and other [[using_excelstyle_formulas_in_notion | Excel-like formulas]] in Notion, offering more advanced data manipulation capabilities without the complexity of Notion's native [[using_formulas_in_notion | formulas]] <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.