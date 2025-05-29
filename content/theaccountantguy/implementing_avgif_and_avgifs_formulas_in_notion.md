---
title: Implementing AVGIF and AVGIFS formulas in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

This article explains how to find the [[using_avg_function_in_notion | average of numbers in Notion]], including conditional averages, using an external tool to bypass the complexities of [[using_formulas_in_notion | Notion's inbuilt formulas]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The process demonstrates how to replicate [[using_excellike_formulas_in_notion | Excel-like AVERAGE, AVERAGEIF, and AVERAGEIFS formulas in Notion]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Example Sales Database <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>

The demonstration uses a sales database in Notion with properties such as:
*   Date <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>
*   Product <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>
*   Category <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>
*   Quantity <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
*   Revenue <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>

The goal is to find the average revenue values and save them into a separate Notion database <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Calculation Objectives <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>

The tutorial covers three specific average calculations:
1.  **Average Sales Revenue**: The overall average of all revenue numbers <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
2.  **Average Sales Revenue for March Month**: The average revenue specifically for sales occurring in March <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
3.  **Average Sales Revenue for Software Category in Quarter 1**: The average revenue for sales of "Software" products that occurred in January, February, or March (Q1) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Tool Used: [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

To perform these calculations and integrate them into Notion, an external tool called [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] is used <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Setup Steps <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>

1.  **Log In to [[using_my_formula_gen_to_enhance_notion | My Formula Gen]]**: Go to myformulagen.com and create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Database URL**: Copy the URL of the Notion database you want to calculate values from <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This can be done by clicking the "six dots" icon on an inline database and selecting "copy link" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Paste this URL into [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  **Add API Key**:
    *   Navigate to "Settings" in [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   Click "Get API Key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Create a "New Integration" by defining a name and selecting your Notion workspace <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Copy the "Internal Integration Secret" (API key) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Paste the API key into the "API key" field in [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    [!NOTE]
    The API key is confidential and unique to your use case <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
4.  **Connect API Key to Notion Page**: Go back to your Notion page containing the database, click the "three dots" menu, select "Connections," and add the API key you just created <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The database within that page will then be connected by default <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Calculating Average Sales Revenue (AVERAGE) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>

1.  In [[using_my_formula_gen_to_enhance_notion | My Formula Gen]], select the "Average" operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  Choose "Revenue" as the column to average <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  Select "All rows" to consider all entries in the database <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  Click "Calculate" to see the average result <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
5.  **Save to Notion Database**:
    *   Create a second Notion database (e.g., "db_summary") with a "Value" column formatted as a number <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Add a new row to this database (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
    *   Copy the link of this summary database <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
    *   In [[using_my_formula_gen_to_enhance_notion | My Formula Gen]], click "Add to Notion", paste the summary database link, select the "Value" column, and choose the "Average Sales Revenue" row <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
    *   Click "Save to Notion" to populate the value <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
6.  **Save Formula**: Give the formula a name (e.g., "Revenue average") and click "Save" to store it for future use <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Calculating Average Sales Revenue for March Month (AVGIF) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

1.  Click "New Formula" in [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
2.  Paste the original sales database URL <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
3.  Select the "Average" operation for the "Revenue" column <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
4.  Add a condition: where the "Date" field's "Start date is between" March 1st and March 31st <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
6.  Add a new row in your summary database (e.g., "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
7.  Use "Add to Notion" again to save the calculated value to this new row <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
8.  Save the formula (e.g., "Revenue March 2025 average") <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

## Calculating Average Sales Revenue for Software Category in Quarter 1 (AVGIFS) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>

1.  Click "New Formula" and paste the sales database URL <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
2.  Select the "Average" operation for the "Revenue" column <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
3.  Add the first condition: where the "Date" field's "Start date is between" January 1st and March 31st (for Q1) <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Add an "and" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
5.  Add the second condition: where the "Category" column "is" "Software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
7.  Add a new row in your summary database (e.g., "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
8.  Use "Add to Notion" to save the value to this new row <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
9.  Save the formula (e.g., "Mar 2025 software") <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

## Updating Values and Refreshing Formulas <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>

If you make changes to the numerical values in your source Notion database, the averages in your summary database will not update automatically <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. To refresh them:
1.  Go to the "Saved Formulas" section in [[using_my_formula_gen_to_enhance_notion | My Formula Gen]] <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
2.  You can either click "Refresh All" to update all saved formulas at once, or click "Refresh Formula" next to a specific formula to update only that value <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

This setup allows you to easily create, save, and refresh complex average calculations in Notion, much like [[using_excellike_formulas_in_notion | Excel-like formulas in Notion]] <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>, simplifying [[using_notion_for_calculations | Notion for calculations]] without directly using [[using_formulas_in_notion | Notion formulas]] <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

[[using_formulas_to_add_numbers_in_notion | Other operations like Sum]] and [[using_formulas_to_subtract_in_notion | Count]] are also available in [[applying_formulas_and_rollup_properties_in_notion | My Formula Gen]] <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>, providing flexibility for [[managing_sales_data_with_formulas_in_notion | managing sales data with formulas in Notion]] or other calculation needs.