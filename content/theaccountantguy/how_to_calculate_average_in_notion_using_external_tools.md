---
title: How to calculate average in Notion using external tools
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion offers [[using_formulas_in_notion | inbuilt formulas]] for calculations, they can be complex, especially when attempting to transfer results to different databases or apply conditional logic. This article outlines how to calculate various averages in Notion using an external tool called My Formula Gen, similar to [[using_excellike_formulas_in_notion | Excel]]'s AVERAGE, AVERAGEIF, and AVERAGEIFS functions. <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>

## Initial Setup in Notion <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>

Begin with a Notion database containing properties such as Date, Product, Category, Quantity, and Revenue. <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> The goal is to calculate the average of the Revenue column and display it in a separate Notion database. <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>

Specific calculations to be performed:
1.  Overall average sales revenue. <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
2.  Average sales revenue for the March month only. <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
3.  Average sales revenue for the "Software" category within the first quarter (Jan-Mar). <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>

## Connecting Notion to My Formula Gen

My Formula Gen is an external tool used to perform these calculations. <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

### Step 1: Log in to My Formula Gen <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   Head to myformulagen.com and create an account. <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>

### Step 2: Fetch Notion Database URL <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
*   In your Notion database, click the "six dots" icon or the page-level three dots, then "Copy link" to get the database URL. <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   Paste this URL into My Formula Gen. <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>

### Step 3: Add API Key <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   In My Formula Gen, navigate to Settings and click "Add an API key." <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Click "Get API key" to be redirected to Notion's API page. <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>
*   Click "New integration," define a name (e.g., "My API Key"), select the workspace, and click "Save." <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>
*   Copy the "Internal Integration Secret" (click "Show" to reveal it). <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>
*   Paste this API key into My Formula Gen's settings and click "Save changes." <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>

### Step 4: Connect Notion Page to API Key <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>
*   Go back to your Notion page containing the database. <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>
*   Click the three dots at the top right of the Notion page, select "Connections," and choose the API key you just created. <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a> This connects the page and its databases to the API. <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>

## Performing Average Calculations

### 1. Overall Average Sales Revenue

*   In My Formula Gen, ensure the Notion database link is entered. <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>
*   Select "Average" as the operation. <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>
*   Choose "Revenue" as the column for calculation. <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>
*   Select "All rows" to include all data entries. <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
*   Click "Calculate" to see the result. <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>

#### Displaying Results in Notion

*   Create a new "Database - Inline" in Notion, renaming it (e.g., "DB_Summary"). <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>
*   Add a "Value" property, set to "Number" format. <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>
*   Create a new row (e.g., "Average Sales Revenue"). <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>
*   Copy the link to this new "DB_Summary" database. <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>
*   In My Formula Gen, click "Add to Notion," paste the "DB_Summary" link, select the "Value" column, and the "Average Sales Revenue" row. <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>
*   Click "Save to Notion" to update the value in your Notion database. <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>

#### Saving and Refreshing Formulas

*   Save the formula in My Formula Gen by defining a name (e.g., "Revenue Average"). <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
*   If data in the source database changes, click "Refresh formula" (for a specific formula) or "Refresh all" (for all saved formulas) in My Formula Gen to update the results in Notion. <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a> <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>

### 2. Average Sales Revenue for March Month

This demonstrates conditional averaging, similar to AVERAGEIF in [[using_excellike_formulas_in_notion | Excel]].
*   Click "New Formula" in My Formula Gen. <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>
*   Select "Average" for "Revenue" column on "All rows." <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>
*   Add a condition: "Date" field (or "Start Date") "is between" March 1st and March 31st. <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
*   Click "Calculate." <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>
*   Create a new row in your "DB_Summary" (e.g., "Average Sales Revenue March 2025") and save the calculated value to it. <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a> <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>
*   Save this formula (e.g., "Revenue March 2025 Average"). <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>
*   You can verify this by applying a filter in Notion for the March dates; the Notion summary average will match. <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>

### 3. Average Sales Revenue for Software Category in Q1

This demonstrates multiple conditional averages, similar to AVERAGEIFS in [[using_excellike_formulas_in_notion | Excel]].
*   Click "New Formula" in My Formula Gen. <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>
*   Select "Average" for "Revenue" column on "All rows." <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>
*   Add the first condition: "Date" field "is between" January 1st and March 31st (for Q1). <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>
*   Add a second (AND) condition: "Category" column "is" "Software." <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>
*   Click "Calculate." <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
*   Create a new row in "DB_Summary" (e.g., "Average Sales March 2025 Software") and save the value. <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>
*   Save this formula (e.g., "Mar 2025 Software"). <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>

## Conclusion

Using My Formula Gen allows users to [[implementing_excellike_formulas_in_notion | implement Excel-like formulas in Notion]] for calculating averages, including complex conditional scenarios, and easily update results in a separate Notion database. <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a> This provides a lot of flexibility for [[analyzing_financial_data_using_notion | analyzing financial data using Notion]] or [[monthly_performance_tracking_with_notion | monthly performance tracking with Notion]], beyond Notion's native capabilities. The tool also supports other operations like [[calculating_the_sum_of_a_column_in_notion | sum]], count, and is implied to support operations like [[calculating_product_of_numbers_in_notion | product of numbers]] or [[applying_formula_for_multiplication_in_notion | multiplication]], in addition to [[adding_numbers_in_notion | adding numbers]]. <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>

For further assistance, you can reach out to notionformyuse@gmail.com. <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>