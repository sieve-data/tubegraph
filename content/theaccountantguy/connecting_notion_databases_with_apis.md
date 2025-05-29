---
title: Connecting Notion databases with APIs
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

Connecting Notion databases with APIs allows for advanced data manipulation and reporting that might be complex or unavailable using Notion's built-in formulas alone <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This method is particularly useful for calculating aggregate values like averages from one database and populating them into another summary database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## External Tool: My Formula Gen

To achieve advanced calculations and cross-database updates, an external tool like My Formula Gen can be utilized <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This tool functions similarly to Excel's `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` functions, but applied to Notion data <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Setup Process

### 1. Account Creation and Login
Begin by heading to myformulagen.com and creating an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### 2. Fetching the Notion Database URL
The first step within My Formula Gen is to fetch the URL of the Notion database you wish to analyze <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   For an inline database, click the six-dot menu next to the database name and select "Copy link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   Paste this URL into the designated field in My Formula Gen <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### 3. Setting Up the API Key
[[connecting_notion_databases_with_api_keys_for_data_management | Connecting Notion databases with API Keys for data management]] requires setting up an API key within My Formula Gen.
*   Go to the "Settings" section in My Formula Gen and click "Add an API key" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   Click "Get API key" to be redirected to Notion's API page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   Create a "New integration" by defining a name (e.g., "My API key") and selecting the relevant Notion workspace <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   After saving, an "Internal Integration Secret" will be generated. Click "Show" and copy this secret <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   Paste the copied API key back into My Formula Gen and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### 4. Connecting Notion Page to API Key
Once the API key is set up in My Formula Gen, you need to connect your Notion page to it:
*   Navigate to the Notion page containing your database <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   Click the three dots in the top right corner of the page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   Select "Connections" and choose the API key integration you just created (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   Confirm the connection <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This ensures the database within that page is also connected <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Calculating Averages

Once the setup is complete, you can define custom formulas in My Formula Gen to get desired values.

### Example 1: Average Sales Revenue (Overall)
To find the average of a specific column (e.g., "Revenue") across all rows:
*   In My Formula Gen, select "Average" as the operation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   Select "All rows" for the calculation scope <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Example 2: Average Sales Revenue for a Specific Month (e.g., March)
To calculate a conditional average, similar to `AVERAGEIF` in Excel:
*   Create a new formula in My Formula Gen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   Select "Average" for the "Revenue" column, considering "All rows" <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   Add a condition: select the "Date" field, choose "start date is between," and define the range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### Example 3: Average Sales Revenue for Specific Category and Quarter (e.g., Software Category, Q1)
For calculations with multiple conditions, like `AVERAGEIFS` in Excel:
*   Start a new formula <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   Select "Average" for the "Revenue" column, considering "All rows" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   Add the first condition: "Date" field, "start date is between," and define the quarter range (e.g., January 1st to March 31st for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Add an "AND" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   Add the second condition: "Category" column "is software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   Click "Calculate" <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

## Saving Results to a Second Notion Database

To display the calculated averages in a separate, dedicated Notion database:
*   [[creating_a_database_in_Notion | Create a database in Notion]] to act as a summary or reporting table (e.g., "db_summary") <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This database should have a "Value" column formatted as a number <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   Add new rows to this summary database for each average you want to store (e.g., "Average Sales Revenue," "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   Copy the link of this second, summary database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   In My Formula Gen, after calculating a value, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   Paste the link of the summary database <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   Select the "Value" column and the corresponding row where you want to save the result <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   Click "Save to Notion" to populate the value <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Managing Formulas and Refreshing Values

*   **Saving Formulas:** After calculating a value and saving it to Notion, you can save the formula in My Formula Gen for future use by giving it a name (e.g., "Revenue average") <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Saved formulas are accessible under "Saved formulas" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Refreshing Values:** If the data in your source Notion database changes, the calculated averages in your summary database will become outdated <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    *   To update a single saved formula, click "Refresh formula" next to its name in My Formula Gen <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
    *   To update all saved formulas at once, click "Refresh All" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This will automatically update all corresponding values in your Notion summary database <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

This approach offers significant flexibility, allowing you to calculate various statistics (like count, sum, average) with multiple conditions and keep your Notion summary databases updated automatically <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

For further assistance, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.