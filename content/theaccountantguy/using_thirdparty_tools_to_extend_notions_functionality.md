---
title: Using thirdparty tools to extend Notions functionality
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Notion offers built-in formulas for calculations <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. However, for more complex, Excel-like calculations or to integrate results into separate databases without using Notion's native [[creating_custom_formulas_in_notion | formulas]], relations, and rollups, a third-party tool can be highly beneficial <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This approach simplifies the process and provides dynamic updates <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

## MyFormula.com: A Tool for Advanced Calculations

MyFormula.com is a third-party tool that allows users to perform advanced calculations based on [[generating_pdf_documents_from_notion_database | Notion databases]] and output the results back into Notion <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Setting Up the API Key

To connect your Notion databases with MyFormula.com, you need to set up an API key <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
1.  Log in to MyFormula.com <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  Navigate to "Settings" and click "Get API Key" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
3.  In the new Notion screen, create a "New integration" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
4.  Give it a name (e.g., "Sum formula key") and select your Notion workspace <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
5.  Save the integration to generate the API key <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
6.  Copy the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
7.  Paste this key into the "Notion API key" field on MyFormula.com and click "Save Settings" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Connecting Notion Databases

For the tool to access your databases, ensure they are placed within a Notion page that is connected to the API key <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>:
1.  On your Notion page containing the databases, click the three dots (`...`) in the top right corner <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
2.  Go to "Add connections" and search for the integration name you created (e.g., "sum formula key") <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
3.  Select the integration and click "Confirm" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This connects everything within that page, including databases, to the API key <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## Practical Applications

This tool enables various calculations to be performed on Notion data and then written back to specified Notion databases.

### 1. Calculating Total Sales Revenue

To find the total sales revenue from a "Sales Database" and display it in a separate "Sales Revenue Total" database <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>:
1.  Copy the link of the "Sales Database" in Notion <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
2.  Paste this link into the "Database URL" field on MyFormula.com <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
3.  Select the "Sum" function <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
4.  Choose the "Revenue" property from your database <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
5.  Select "All Rows" to calculate the sum for all entries <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. The tool will display the sum (e.g., $1,537) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
7.  To push this value to Notion, click "Add to Notion" <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
8.  Copy the link of the target database (e.g., "DB_Sales Revenue Total") and paste it into MyFormula.com <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
9.  Select the target column (e.g., "Amount") and row (e.g., "Total sales revenue") <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
10. Click "Save to Notion" to update the Notion database <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
11. Save the formula within MyFormula.com for future use (e.g., "Total Sales Revenue") <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### 2. Calculating Sales Revenue for a Specific Month (e.g., March 2025)

To filter and sum revenue for a specific period <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>:
1.  Create a "New Formula" in MyFormula.com <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
2.  Paste the "Sales Database" link <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
3.  Select "Sum" for the "Revenue" field <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
4.  Add a filter condition:
    *   Select the "Date" property <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   Choose "is between" and set the date range (e.g., March 1st to March 31st) <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
5.  Click "Calculate" <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
6.  "Add to Notion," selecting a new target database (e.g., "DB_Sales Revenue March 2025") and its respective "Amount" column and row <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
7.  Save the formula (e.g., "Total Sales Revenue for March 2025") <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

### 3. Calculating Sales Revenue for a Quarter and Specific Category (e.g., Q1 2025 Software)

To apply multiple conditions for a sum calculation <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>:
1.  Create a "New Formula" <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
2.  Paste the "Sales Database" link <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
3.  Select "Sum" for the "Revenue" field <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
4.  Add the first condition:
    *   "Date" property "is between" January 1st to March 31st (for Q1) <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
5.  Add a second condition using the "AND" operator <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>:
    *   Select the "Category" property.
    *   Choose "is" and enter "Software" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
6.  Click "Calculate" <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
7.  "Add to Notion," specifying the target database (e.g., "DB_Sales_Category_Q1_2025") and its "Amount" column and "Q1 2025 sales for software" row <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
8.  Save the formula <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

## Dynamic Updates

After making changes to the original Notion sales database, the calculated values in the separate Notion databases will not automatically update <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. To refresh them:
*   Go to MyFormula.com.
*   Navigate to "Saved Formulas" <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   Click "Refresh all" to update all saved formulas <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   Alternatively, click the "Refresh" icon next to a specific formula to update only that one <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

This process ensures that your derived values in Notion remain current with your source data <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Conclusion

Using a tool like MyFormula.com offers a straightforward way to extend Notion's capabilities for complex calculations, bypassing the need for intricate [[creating_custom_formulas_in_notion | Notion formulas]] or advanced relation/rollup setups <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. It provides a dynamic and user-friendly interface to perform sums with various filters and push the results directly into Notion databases <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

For further queries, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>.