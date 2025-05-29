---
title: Connecting Notion databases via API
videoId: yaWvFwek_EM
---

From: [[theaccountantguy]] <br/> 

While Notion offers built-in formulas, they can sometimes be complicated for advanced calculations like finding averages across different databases or with specific conditions <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. To overcome this, external tools can be used to [[linking_databases_in_notion | connect Notion databases]] and perform complex calculations, then push the results to another Notion database <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. This guide demonstrates how to achieve this using MyFormulaGen.

## Using MyFormulaGen to Connect and Calculate

MyFormulaGen is an external tool that allows users to perform advanced calculations on Notion data and save the results back into Notion [[creating_a_database_in_notion | databases]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### Step 1: Obtain the Source Database URL

First, you need the URL of the Notion [[setting_up_a_database_in_notion | database]] from which you want to calculate values. This can be copied from an inline database by clicking the "copy link" option <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Step 2: Set Up Notion API Key in MyFormulaGen

To allow MyFormulaGen to interact with your Notion workspace, you need to provide an [[integrating_notion_with_an_api_key_for_database_access | API key]]:
1.  Go to the settings in MyFormulaGen and click "add an [[integrating_notion_with_an_api_key_for_database_access | API key]]" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
2.  Click "get API key" to be redirected to Notion's integration page <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
3.  Create a new integration, define a name (e.g., "My API key"), select your workspace, and save <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
4.  Copy the "Internal Integration Secret" from the newly created integration <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
5.  Paste this secret into MyFormulaGen's API key field and click "Save changes" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Step 3: Connect Notion Database to the API Key

For the API key to access your Notion [[creating_a_database_in_notion | database]], you must explicitly grant it connection:
1.  Navigate to the Notion page containing your source [[setting_up_databases_in_notion | database]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  Click the three dots `...` on the Notion page <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  Select "Add connections" (or "Connections") and search for the name of the API key you created <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
4.  Click on the API key and confirm the connection <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This connects the page and any inline [[creating_and_connecting_databases_in_notion | databases]] on it to the API key <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Step 4: Define Custom Formulas in MyFormulaGen

With the connection established, you can define formulas in MyFormulaGen:
1.  Paste the source [[creating_a_database_in_notion | database]] URL into MyFormulaGen <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  Select the desired operation (e.g., "average") and the target column (e.g., "Revenue") <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
3.  Choose the scope (e.g., "all rows," "first five rows," "custom rows") <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  Click "Calculate" to see the result <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Step 5: Set Up a Target Notion Database for Results

To save the calculated values back to Notion, create a second [[creating_a_database_in_notion | database]] to store the results:
1.  Create a new inline database in Notion (e.g., "DB\_summary") <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  Add a "Value" column and set its type to "Number" <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
3.  Add rows for each type of average you want to store (e.g., "Average Sales Revenue," "Average Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
4.  Copy the link of this second database <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Step 6: Save Results to Notion

In MyFormulaGen, after calculating:
1.  Click "Add to Notion" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
2.  Paste the link of the target [[connecting_notion_databases_and_templates | database]] (the summary database) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  Select the "Value" column and the specific row where you want to save the result <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
4.  Click "Save to Notion" <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The value will automatically update in your Notion database <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Step 7: Save and Refresh Formulas

To reuse calculations and keep data updated:
1.  Save the formula in MyFormulaGen with a descriptive name (e.g., "Revenue Average") <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
2.  If the source data in Notion changes, you can refresh the saved formulas <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
3.  Click "Refresh all" to update all saved formulas, or click "Refresh formula" next to a specific saved formula to update only that one <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

## Examples of Average Calculations

The process can be applied to various average calculations, similar to `AVERAGE`, `AVERAGEIF`, and `AVERAGEIFS` functions in Excel <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### 1. Overall Average Sales Revenue

This calculates the average of a specific column (e.g., "Revenue") across all rows in the source database <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### 2. Average Sales Revenue for a Specific Month

This involves adding a condition to the average calculation. For example, to find the average revenue for March:
1.  Select "Average" for the "Revenue" column <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
2.  Add a condition: "Date field" (start date) "is between" "March 1" and "March 31" <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
3.  Calculate and save to a specific row in the summary database <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### 3. Average Sales Revenue for a Specific Category and Quarter

This uses multiple conditions for a more refined average:
1.  Select "Average" for the "Revenue" column <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
2.  Add the first condition: "Date field" (start date) "is between" "January 1" and "March 31" (for Q1) <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
3.  Add an "AND" condition <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
4.  Add the second condition: "Category column" "is" "Software" <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
5.  Calculate and save to the summary database <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

By following these steps, you can [[connecting_notion_database_with_api_for_bulk_document_generation | connect Notion databases with an API]] and perform dynamic calculations, automatically updating values in your Notion pages without complex Notion formulas <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. MyFormulaGen also offers other operations like Sum and Count <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.