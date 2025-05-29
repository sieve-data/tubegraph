---
title: Using My Formula Gen to enhance Notion
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

[[Using formulas in Notion | Notion]] offers inbuilt formulas, but they can be complex to understand and it's challenging to display calculated results in a separate database within [[using_notion_for_calculations | Notion]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. An external tool called My Formula Gen simplifies this process, allowing users to perform complex calculations like average, average if, and average ifs, similar to [[using_excellike_formulas_in_notion | Excel-like formulas]], and integrate the results seamlessly into [[creating_custom_formulas_and_linking_databases_in_notion | Notion databases]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Setting Up My Formula Gen

To begin using My Formula Gen:

1.  **Create an Account**: Navigate to myformulagen.com and log in or create an account <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Fetch Database URL**: Obtain the URL of the [[using_formulas_in_notion | Notion database]] you wish to use for calculations. This can be done by clicking on the three dots next to the database name and selecting "Copy link" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Paste this URL into My Formula Gen <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
3.  **Generate and Add API Key**:
    *   Go to My Formula Gen settings and click "Get API key" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   This redirects you to [[using_formulas_in_notion | Notion's]] integration page where you can create a "New integration" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Define a name for your API key (e.g., "My API key") <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, select the relevant workspace, and click "Save changes" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   Copy the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a> and paste it into My Formula Gen's API key field, then click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  **Connect [[using_formulas_in_notion | Notion]] Database to API Key**:
    *   Go back to your [[using_formulas_in_notion | Notion]] page containing the database <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Click the three dots in the page's top right corner <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, select "Connections", and search for your newly created API key (e.g., "My Formula Gen") <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   Connect the API key by clicking "Confirm" <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This ensures the database is connected by default <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Calculating Averages with My Formula Gen

My Formula Gen allows for various average calculations, which can then be saved directly into a separate [[using_formulas_in_notion | Notion database]].

### 1. Finding Overall Average Sales Revenue

To find the average of a specific column, such as "Revenue" in a sales database <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>:

*   In My Formula Gen, select "Average" as the operation and choose the "Revenue" column <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Select "All rows" to calculate the average for the entire column <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

To save this result to a second [[using_formulas_in_notion | Notion database]]:

1.  Create a new inline database in [[using_formulas_in_notion | Notion]] (e.g., "DB\_summary") with a "Value" column formatted as a number <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  Add a new row for the average (e.g., "Average Sales Revenue") <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
3.  Copy the link of this second database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
4.  In My Formula Gen, click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>, paste the link of the second database <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
5.  Select the "Value" column and the corresponding row (e.g., "Average Sales Revenue") to save the calculated average <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
6.  Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

To easily update this value in the future, save the formula within My Formula Gen by defining a name (e.g., "Revenue average") and clicking "Save" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Whenever the source data changes, simply click "Refresh formula" or "Refresh all" in My Formula Gen to update the stored value in [[using_formulas_in_notion | Notion]] <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### 2. Finding Average Sales Revenue for a Specific Month (Conditional Average)

To calculate the average sales revenue for a specific period, such as March <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>:

1.  Start a new formula in My Formula Gen <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
2.  Select "Average" for the "Revenue" column <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
3.  Add a condition: choose the "Date" field and set "Start date is between" 1st March and 31st March <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
4.  Click "Calculate" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
5.  Add a new row in your summary database (e.g., "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
6.  Save the result to [[using_formulas_in_notion | Notion]] as done previously <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
7.  Save this formula as "Revenue March" for future use <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### 3. Finding Average Sales Revenue for a Specific Category and Quarter (Multiple Conditions)

For more complex calculations involving multiple conditions, like the average sales revenue for the "Software" category in Q1 (January 1st to March 31st) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>:

1.  Start a new formula <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
2.  Select "Average" for "Revenue" <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
3.  Add the first condition for the date: "Date field Start date is between" January 1st and March 31st <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
4.  Add an "AND" condition <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
5.  Add the second condition for the category: select the "Category" column and set "is software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
7.  Create a new row in your summary database (e.g., "Average Sales March 2025 Software") <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
8.  Save the result to [[using_formulas_in_notion | Notion]] and save the formula <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

### Refreshing All Saved Formulas

Once multiple formulas are saved, you can easily refresh all of them simultaneously. If you modify any values in the source database, clicking "Refresh all" within My Formula Gen will update all associated calculations in your summary database in [[using_formulas_in_notion | Notion]] <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. This provides a dynamic way to manage data without constantly [[creating_and_using_custom_formulas_without_notions_native_formulas | creating custom formulas]] or complex [[applying_formulas_and_rollup_properties_in_notion | rollup properties]] within [[using_formulas_in_notion | Notion]] itself <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

My Formula Gen supports various [[using_excellike_formulas_in_notion | Excel-like formulas]] beyond average, including count, sum, and more, offering significant flexibility for [[managing_sales_data_with_formulas_in_notion | managing sales data]] and other numerical data in [[using_formulas_in_notion | Notion]] <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. This means you can also apply concepts like [[using_formulas_to_add_numbers_in_notion | using formulas to add numbers in Notion]] and [[using_formulas_to_subtract_in_notion | using formulas to subtract in Notion]] using this tool.