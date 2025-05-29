---
title: Setting up and using My Formula Gen tool
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

My Formula Gen is an external tool designed to help users find averages of numbers in Notion databases, providing a more straightforward alternative to Notion's built-in formulas, which can sometimes be complicated <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It allows for calculating simple averages, averages with single conditions, and averages with multiple conditions, similar to `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` functions in [[using_excel_formulas_in_notion | Excel]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Initial Setup of My Formula Gen

To begin [[setting_up_the_wizzygen_application_and_configuring_settings | setting up the Wizzygen application]] and My Formula Gen:

1.  **Access My Formula Gen**: Navigate to myformulagen.com and log in or create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Notion Database URL**:
    *   Locate the Notion database from which you want to calculate values <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   If the database is full-page, click on the three dots at the top right, then "Copy link" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   If it's an inline database, click on the six dots next to its title and select "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Paste this URL into the designated field in My Formula Gen <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  **Set Up API Key**:
    *   In My Formula Gen, click on "Settings" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   Click "Get API Key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   On Notion's API page, click "New integration" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Define a name for your API key (e.g., "My API Key") and select the workspace it will access <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
    *   Click "Save changes" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Copy the "Internal Integration Secret" by clicking "Show" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Paste this secret value into the API key field in My Formula Gen's settings and click "Save settings" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect Notion Database to API Key**:
    *   Go back to your Notion page containing the database <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Click on the three dots at the top right of the page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Select "Connections" and choose the API key you just created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This ensures the database is connected by default <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Calculating Averages

Once setup is complete, you can [[creating_custom_formulas_in_notion | create custom formulas]] to calculate averages.

### 1. Simple Average (e.g., Average Sales Revenue)

To find the average of a specific column:
*   In My Formula Gen, select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Choose the target column (e.g., "Revenue") <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   Select "All rows" to consider all entries <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### 2. Average with One Condition (e.g., Average Sales Revenue for March)

To calculate an average based on a single criterion:
*   Start a "New formula" <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   Paste the database link <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   Select "Average" for the desired column (e.g., "Revenue") and "All rows" <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   Add a condition (e.g., "Date field start date is between" March 1st and March 31st) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### 3. Average with Multiple Conditions (e.g., Average Sales Revenue for Software Category in Q1)

For averages with multiple criteria:
*   Start a "New formula" <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   Paste the database link <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   Select "Average" for the target column (e.g., "Revenue") and "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   Add the first condition (e.g., "Date field start date is between" January 1st and March 31st for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Click "Add" to add an "AND" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   Add the second condition (e.g., "Category column is software") <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

## Populating Results in Notion

To display the calculated averages within your Notion workspace:

1.  **Create a Summary Database in Notion**:
    *   In your Notion page, create a new "Database - Inline" (e.g., named "DB_Summary") <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Rename the default "Name" property to "Title" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   Add a new property, name it "Value", and set its type to "Number" <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   Add rows for each type of average you want to store (e.g., "Average Sales Revenue", "Average Sales Revenue March 2025", "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
2.  **Add Results to Notion**:
    *   In Notion, copy the link to your new summary database <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   In My Formula Gen, after calculating a result, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
    *   Paste the link of the summary database <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   Select the target "Value" column and the corresponding row (e.g., "Average Sales Revenue") where you want to save the result <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The value will automatically populate in your Notion database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

## Saving and Refreshing Formulas

To ensure your calculated averages remain up-to-date:

1.  **Save Formulas**: After successfully populating a value in Notion, click "Save the formula" in My Formula Gen <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Give it a descriptive name (e.g., "Revenue Average") and click "Save" <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. Saved formulas appear in the "Saved Formulas" section <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
2.  **Refresh Values**: If your source data in Notion changes:
    *   Go to the "Saved Formulas" section <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   You can click "Refresh all" to update all saved formulas <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>, or click "Refresh formula" next to a specific formula to update only that one <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The new values will be reflected in your Notion summary database <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

This setup allows you to easily calculate and manage various averages in Notion without needing to delve into complex Notion formulas <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. The tool also supports other operations like Count, similar to functions found in [[using_excellike_formulas_in_notion | Excel]] <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.