---
title: Creating custom formulas and linking databases in Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

Notion offers built-in formulas, but they can sometimes be complex to understand <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. For more advanced calculations and to display results in a separate database, an external tool can be used <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. This article demonstrates [[using_my_formula_gen_to_enhance_notion | Using My Formula Gen to enhance Notion]] for calculating averages with and without conditions, similar to `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` functions in Excel <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Setting Up My Formula Gen and Notion

To begin, you will need to establish a connection between your Notion database and My Formula Gen.

### 1. Log In to My Formula Gen
Access myformulagen.com and create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### 2. Fetch Database URL
Obtain the URL of the Notion database you wish to analyze.
*   If your database is inline, click the six dots, then "Copy link" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   Paste this URL into My Formula Gen <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### 3. Add API Key
API keys are confidential and unique to your use case <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   In My Formula Gen, click on `Settings` and then `Add an API key` <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Click `Get API key` to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   Click `New integration`, define a name (e.g., "My API Key"), select your workspace, and click `Save` <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   Copy the `Internal Integration Secret` from the newly created integration <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   Paste this value into My Formula Gen's API key field and click `Save changes` <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### 4. Connect Notion Page to API Key
This step [[establishing_links_and_relationships_between_databases_in_notion | establishes links and relationships between databases]] indirectly via the API.
*   Navigate back to your Notion page containing the database <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   Click the three dots at the top right of the page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   Select `Connections` and connect to the API key you just created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   This connects the entire page and its inline databases to the API key <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Calculating Average Sales Revenue

My Formula Gen allows you to [[creating_and_using_custom_formulas_without_notions_native_formulas | create and use custom formulas without Notion's native formulas]].

### 1. Overall Average Sales Revenue
To find the average of the `Revenue` column across all rows:
*   In My Formula Gen, ensure the database URL is entered <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   Select `average` as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Choose `Revenue` as the column for calculation <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   Select `all rows` to include all data <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Click `Calculate` to see the result <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### 2. Average Sales Revenue for March
To find the average revenue for a specific month (e.g., March):
*   Create a new formula in My Formula Gen <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   Enter the database link <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   Select `average` of `Revenue` for `all rows` <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   Add a condition: `Date` field `start date` is `between` `March 1` and `March 31` <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   Click `Calculate` <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### 3. Average Sales Revenue for Software Category in Q1
To calculate the average revenue for a specific category within a quarter (e.g., Software in Q1 - Jan, Feb, March):
*   Create a new formula in My Formula Gen <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   Enter the database link <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   Select `average` of `Revenue` for `all rows` <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   Add the first condition: `Date` field `start date` is `between` `January 1` and `March 31` (for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Add an `AND` condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   Add the second condition: `Category` column `is` `Software` <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   Click `Calculate` <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

## Saving and Updating Values in Notion

To store and manage your calculated averages, you can [[creating_and_using_databases_in_notion | create and use databases in Notion]].

### 1. Create a Second Notion Database
[[Creating a database in Notion | Create a new inline database]] in your Notion page to serve as a summary table <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   Rename it (e.g., `DB_Summary`) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   Add a `Value` column, set its type to `Number` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   Add rows for each calculation you want to store (e.g., "Average Sales Revenue," "Average Sales Revenue March 2025," "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

### 2. Populate Values in Notion
*   Copy the link of your newly created summary database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   In My Formula Gen, after calculating a value, click `Add to Notion` <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   Paste the summary database link <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   Select the `Value` column and the corresponding row (e.g., "Average Sales Revenue") where you want the result to be saved <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   Click `Save to Notion` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The value will automatically populate in your Notion database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### 3. Save Formulas for Future Use
To reuse formulas, especially when source data changes:
*   After populating a value, click `Save the formula` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   Give it a descriptive name (e.g., "Revenue Average") <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   Saved formulas will appear in the `Saved Formulas` section <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### 4. Refresh Values
If your source data in Notion is updated, the calculated values in your summary database will become outdated <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   Go to the `Saved Formulas` section in My Formula Gen <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   To update a specific formula, click `Refresh formula` next to it <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   To update all saved formulas, click `Refresh all` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   The updated values will reflect in your Notion summary database <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

```ad-note
This setup provides significant flexibility, allowing you to calculate various metrics beyond just averages, such as sums and counts, using My Formula Gen's operations <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
```