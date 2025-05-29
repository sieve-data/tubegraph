---
title: Calculating total sales revenue using a tool
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

This article outlines how to calculate total sales revenue and other specific sales data within Notion using an external tool, avoiding Notion's native formulas and complexities like relations and rollups <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. The method described allows for Excel-like formula application in Notion <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## The Tool: MyFormulaGen.com

The primary tool used for these calculations is MyFormulaGen.com <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This tool helps derive values from Notion databases without requiring complex Notion formulas <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Initial Setup and API Key Connection

To use MyFormulaGen.com, you need to connect it to your Notion workspace via an API key <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>:
1.  Log in to MyFormulaGen.com <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  Navigate to 'Settings' and click 'Get API Key' <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
3.  Create a 'New integration' in Notion, give it a name (e.g., "Sum formula key"), and select your workspace <a class="yt-timestamp" data-t="00:02:51">[00:03:02]</a>.
4.  Save the integration <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
5.  Copy the 'Internal Integration Secret' from your Notion integration settings <a class="yt-timestamp" data-t="00:03:17">[00:03:22]</a>.
6.  Paste this API key into the 'Notion API key' field on MyFormulaGen.com and click 'Save Settings' <a class="yt-timestamp" data-t="00:03:26">[00:03:33]</a>.

### Connecting Notion Databases

Ensure all Notion databases you plan to use are within a single Notion page. This page can then be connected to the API key, allowing all its contained databases to be accessible to the tool <a class="yt-timestamp" data-t="00:03:40">[00:03:49]</a> <a class="yt-timestamp" data-t="00:13:01">[00:13:09]</a>.
1.  In Notion, on the sales dashboard page containing your databases, click the three dots menu <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
2.  Select 'Connections' <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  Search for and select the API key integration you created (e.g., "Sum formula key") <a class="yt-timestamp" data-t="00:03:55">[00:04:06]</a>.
4.  Click 'Confirm' <a class="yt-timestamp" data-t="00:04:06">[00:04:08]</a>. This connects the page and its contents to the API key <a class="yt-timestamp" data-t="00:04:08">[00:04:17]</a>.

## Calculating Sales Data

The process involves identifying the source database, applying the desired sum function and filters, and then pushing the calculated result into a target Notion database.

### 1. Calculating Total Sales Revenue

To find the total sales revenue from a Notion sales database <a class="yt-timestamp" data-t="00:00:38">[00:00:41]</a>:
1.  In Notion, hover over the source sales database (e.g., with 'Date', 'Product', 'Category', 'Quantity', 'Revenue', 'Payment method', and 'Sales Channel' fields) <a class="yt-timestamp" data-t="00:00:24">[00:00:29]</a>.
2.  Click the six dots menu and select 'Copy link' <a class="yt-timestamp" data-t="00:04:34">[00:04:40]</a>.
3.  In MyFormulaGen.com, paste the copied database link into the designated field <a class="yt-timestamp" data-t="00:05:07">[00:05:10]</a>.
4.  Under 'Formula', select 'Sum' <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
5.  Under 'Notion Property', select the 'Revenue' field <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
6.  For 'Rows to Consider', select 'All Rows' <a class="yt-timestamp" data-t="00:05:28">[00:05:38]</a>.
7.  Remove any default additional filters by clicking the 'X' <a class="yt-timestamp" data-t="00:05:48">[00:05:52]</a>.
8.  Click 'Calculate' to see the sum <a class="yt-timestamp" data-t="00:05:42">[00:05:55]</a>.
9.  To transfer this value to Notion, click 'Add to Notion' <a class="yt-timestamp" data-t="00:06:59">[00:07:00]</a>.
10. Copy the link of your target Notion database (e.g., 'DB_Sales Revenue Total') <a class="yt-timestamp" data-t="00:07:07">[00:07:12]</a>.
11. Paste it into MyFormulaGen.com <a class="yt-timestamp" data-t="00:07:24">[00:07:25]</a>.
12. Select the target 'Column Name' (e.g., 'Amount') and 'Row Name' (e.g., 'Total Sales Revenue') within your target database <a class="yt-timestamp" data-t="00:07:28">[00:07:49]</a>.
13. Click 'Save to Notion' <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. The value will appear in Notion <a class="yt-timestamp" data-t="00:07:57">[00:07:58]</a>.
14. Save the formula in MyFormulaGen.com for future use (e.g., 'Total Sales Revenue') <a class="yt-timestamp" data-t="00:08:01">[00:08:11]</a>.

> [!TIP]
> To update the values in Notion after making changes to the source database, go to 'Saved Formulas' in MyFormulaGen.com and click 'Refresh All' or 'Refresh' for a specific formula <a class="yt-timestamp" data-t="00:08:53">[00:09:21]</a>.

### 2. Deriving Specific Period Sales Data in Notion (e.g., March 2025 Sales Revenue)

To find the sales revenue for a specific month (e.g., March 2025) <a class="yt-timestamp" data-t="00:09:32">[00:09:41]</a>:
1.  Click 'New Formula' in MyFormulaGen.com <a class="yt-timestamp" data-t="00:09:44">[00:09:47]</a>.
2.  Copy and paste the sales database link as before <a class="yt-timestamp" data-t="00:09:49">[00:09:52]</a>.
3.  Select 'Sum' for the 'Formula' and 'Revenue' for the 'Notion Property' <a class="yt-timestamp" data-t="00:09:56">[00:10:00]</a>.
4.  Add a filter: select 'Date' property, choose 'Is Between', and manually enter 'March 1' and 'March 31' <a class="yt-timestamp" data-t="00:10:24">[00:10:39]</a>.
5.  Click 'Calculate' <a class="yt-timestamp" data-t="00:10:54">[00:10:55]</a>.
6.  Create a new target database in Notion for this specific calculation (e.g., 'DB_Sales Revenue March 2025') <a class="yt-timestamp" data-t="00:11:12">[00:11:21]</a>.
7.  Copy its link and use 'Add to Notion' in MyFormulaGen.com to transfer the value, selecting the correct column and row <a class="yt-timestamp" data-t="00:12:46">[00:13:00]</a>.
8.  Save the formula (e.g., 'Total Sales Revenue for March 2025') <a class="yt-timestamp" data-t="00:13:45">[00:13:52]</a>.

### 3. Calculating Sales Revenue for a Specific Quarter and Category (e.g., Q1 2025 Software Category)

To calculate sales revenue based on multiple conditions (e.g., Q1 2025 for 'Software' category) <a class="yt-timestamp" data-t="00:14:41">[00:14:52]</a>:
1.  Click 'New Formula' <a class="yt-timestamp" data-t="00:14:57">[00:14:58]</a>.
2.  Copy and paste the sales database link <a class="yt-timestamp" data-t="00:15:00">[00:15:04]</a>.
3.  Select 'Sum' for the 'Formula' and 'Revenue' for the 'Notion Property' <a class="yt-timestamp" data-t="00:15:11">[00:15:23]</a>.
4.  Add the first condition: Select 'Date' property, choose 'Is Between', and enter 'January 1 2025' and 'March 31 2025' (for Q1) <a class="yt-timestamp" data-t="00:15:32">[00:15:53]</a>.
5.  Set the logical operator to 'And' to ensure both conditions are met <a class="yt-timestamp" data-t="00:16:05">[00:16:22]</a>.
6.  Add a new condition by clicking the plus icon <a class="yt-timestamp" data-t="00:16:29">[00:16:31]</a>.
7.  Select 'Category' property, choose 'Is', and type 'Software' <a class="yt-timestamp" data-t="00:16:33">[00:16:45]</a>.
8.  Click 'Calculate' <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
9.  Create a new target database in Notion (e.g., 'DB_Sales_Category_Q1_2025') <a class="yt-timestamp" data-t="00:18:01">[00:18:11]</a>.
10. Copy its link and use 'Add to Notion' to transfer the value, selecting the appropriate column and row <a class="yt-timestamp" data-t="00:18:58">[00:19:18]</a>.
11. Save the formula (e.g., 'Q1 2025 Sales for Software') <a class="yt-timestamp" data-t="00:19:31">[00:19:39]</a>.

## Conclusion

This method allows users to perform various sales calculations, such as total sales revenue, period-specific sales, or category-specific sales, within Notion without needing to learn or implement complex Notion formulas or relations and rollups <a class="yt-timestamp" data-t="00:22:03">[00:22:00]</a> <a class="yt-timestamp" data-t="00:08:26">[00:08:30]</a>. The formulas are dynamic and can be refreshed to reflect changes in the source data <a class="yt-timestamp" data-t="00:21:52">[00:22:00]</a>.

> [!INFO] Contact
> For queries or assistance, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:22:30">[00:22:47]</a>. More videos covering other Excel formulas will be available <a class="yt-timestamp" data-t="00:22:51">[00:22:55]</a>.