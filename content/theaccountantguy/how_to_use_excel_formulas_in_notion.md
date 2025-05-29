---
title: How to use Excel formulas in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion has [[using_formulas_in_notion | inbuilt formulas]], they can sometimes be complicated to understand <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This guide demonstrates how to calculate averages in Notion, including conditional averages, using an external tool called My Formula Gen, similar to how AVERAGE, AVERAGEIF, and AVERAGEIFS functions work in [[using_excelstyle_formulas_in_notion | Excel]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This method allows for complex [[using_formulas_for_financial_calculations_in_notion | financial calculations]] without direct Notion formula complications <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Setting Up My Formula Gen

To get started with [[using_my_formula_gen_for_notion_calculations | My Formula Gen for Notion calculations]]:

1.  **Access My Formula Gen**: Navigate to myformulagen.com and create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Database URL**: Copy the URL of your Notion database. This can be done by clicking on the three dots next to an inline database and selecting "Copy link," or by opening a full-page database and copying its URL <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Paste this URL into the designated field in My Formula Gen <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  **Add API Key**:
    *   Go to "Settings" in My Formula Gen and click "Get API Key" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   This redirects you to Notion's API page where you can create a new integration <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Define a name for your integration (e.g., "My API Key") and select the Notion workspace it will access <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Once created, click on the integration to reveal the "Internal Integration Secret." Copy this secret <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Paste the copied API key into My Formula Gen's settings and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect Notion Page to API Key**:
    *   In your Notion page containing the database, click the three dots in the top right corner <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Go to "Connections" and select the API key you just created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   Confirm the connection <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This connects both the page and any databases within it <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Calculating Averages

Once setup is complete, you can define your custom formulas <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. For these examples, we'll use a sales database with `Date`, `Product`, `Category`, `Quantity`, and `Revenue` columns <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

### 1. Calculating Overall Average Sales Revenue

To find the average of all `Revenue` numbers:

1.  In My Formula Gen, select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  Choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  Select "All rows" to include all entries in the calculation <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

To save this value to a Notion database:

1.  Create a second "summary" database in Notion, ideally with a "Value" property set to "Number" format <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Add a row, e.g., "Average Sales Revenue" <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
2.  Copy the link of this summary database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
3.  In My Formula Gen, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Paste the summary database link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
4.  Select the "Value" column and the "Average Sales Revenue" row <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
5.  Click "Save to Notion" to populate the value <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

To easily update this value in the future, [[creating_and_saving_custom_formulas_in_notion | save the formula]]:

1.  Click "Save formula" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
2.  Give it a name (e.g., "Revenue Average") and click "Save" <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
3.  If data in the source database changes, go to "Saved formulas" in My Formula Gen and click "Refresh formula" next to "Revenue Average" to update the Notion value <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### 2. Calculating Average Sales Revenue for a Specific Month

To find the average sales revenue *only* for the month of March:

1.  Click "New formula" in My Formula Gen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a> and paste the source database URL <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
2.  Select "Average" for `Revenue` column, "All rows" <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
3.  Add a condition: `Date` field `start date` `is between` March 1st and March 31st <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
5.  Add a new row in your Notion summary database (e.g., "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
6.  Use "Add to Notion" as described above to save the calculated value to the new row <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
7.  [[creating_and_saving_custom_formulas_in_notion | Save the formula]] (e.g., "Revenue March 2025 Average") for future use <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

### 3. Calculating Average Sales Revenue for a Specific Category and Quarter

To find the average sales revenue for the "Software" category during Quarter 1 (Jan-Mar):

1.  Click "New formula" and paste the source database URL <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
2.  Select "Average" for `Revenue` column, "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
3.  Add the first condition: `Date` field `start date` `is between` January 1st and March 31st <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
4.  Add an "and" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>: Choose the "Category" column `is` "Software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
6.  Add a new row in your Notion summary database (e.g., "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
7.  Use "Add to Notion" to save the calculated value <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
8.  [[creating_and_saving_custom_formulas_in_notion | Save the formula]] (e.g., "Mar 2025 Software") <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

## Refreshing All Saved Formulas

If you update data in your source Notion database, you can refresh all saved formulas at once:

1.  Go to "Saved formulas" in My Formula Gen <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
2.  Click "Refresh All" to update all linked values in your Notion summary database(s) <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

My Formula Gen offers flexibility by supporting various operations, including the [[using_the_sum_function_in_notion | SUM function in Notion]], count, and other functions commonly found in Excel <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.