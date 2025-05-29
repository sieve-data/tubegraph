---
title: Managing sales data with formulas in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

While Notion offers built-in formulas and functions for various [[Using formulas in Notion | calculations]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, this guide explores how to leverage an external tool to implement [[Using Excellike formulas in Notion | Excel-like formulas]] in Notion, specifically focusing on the sum function for managing sales data <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This approach allows users to perform complex [[Using Notion for calculations | calculations]] without directly engaging with Notion's native formula syntax or complex relations and rollups <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Example Sales Database

For demonstration purposes, a sales database is used, featuring fields such as:
*   Date <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   Product <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   Category <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   Quantity <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   Revenue <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   Payment method <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   Sales Channel <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>

The goal is to extract specific sales information, such as total sales revenue, sales revenue for a particular month, and sales revenue for a specific quarter and category <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Using MyFormulaGen.com for Calculations

MyFormulaGen.com is the external tool used to facilitate these [[Using Notion for calculations | calculations]] <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Connecting Notion via API Key

To connect Notion databases with MyFormulaGen.com, an API key is required <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>:
1.  **Access Settings**: In MyFormulaGen.com, navigate to "Settings" and click "Get API key" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
2.  **Create New Integration**: In the Notion API key screen, click "New integration" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
3.  **Name and Select Workspace**: Give the integration a name (e.g., "Sum formula key") and select your Notion workspace <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Click "Save" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
4.  **Copy API Key**: Go back to "Integrations," click on the newly created key, and then click "Show" next to "Internal Integration Secret" to reveal and copy the API key <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
5.  **Paste Key**: Paste the copied API key into the "Notion API key" field on MyFormulaGen.com and click "Save settings" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
6.  **Connect Notion Page**: Ensure all relevant Notion databases are within a single Notion page. Connect this parent page to the created API key by clicking the three dots on the page, selecting "Connections," typing the API key's name, and confirming the connection <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This connects all databases within that page to the API key <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Calculating Total Sales Revenue

To find the total sales revenue from the sales database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>:
1.  **Copy Database Link**: In Notion, hover over the sales database, click the six dots, and select "Copy link" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  **Paste Link in MyFormulaGen.com**: Paste this link into the designated field in MyFormulaGen.com <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
3.  **Define Formula**: Select "sum" as the function and "Revenue" as the property <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Choose "all the rows" for the calculation range <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
4.  **Calculate**: Click "Calculate." If a default filter appears, remove it to calculate the sum of all rows <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
5.  **Add to Notion**: Create a new Notion database (e.g., "DB_Sales Revenue Total") with an "Amount" column <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Copy this new database's link <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
6.  **Specify Target**: In MyFormulaGen.com, click "Add to Notion," paste the target database link, select the "Amount" column, and choose the desired row (e.g., "Total sales revenue") <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
7.  **Save to Notion**: Click "Save to Notion" to push the calculated value to your Notion database <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
8.  **Save Formula**: Save the formula in MyFormulaGen.com for future use <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Calculating Sales Revenue for a Specific Month

To find sales revenue for March 2025 <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>:
1.  **New Formula**: Click "New formula" in MyFormulaGen.com <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
2.  **Paste Database Link**: Paste the sales database link <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
3.  **Define Sum**: Select "sum" for the "Revenue" field for "all the rows" <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
4.  **Add Date Filter**: Add a condition where the "Date" property "is between" March 1st and March 31st <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
5.  **Calculate**: Click "Calculate" to get the filtered sum <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
6.  **Add to Notion**: Create another Notion database (e.g., "DB_Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. Copy its link and paste it into MyFormulaGen.com <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
7.  **Specify Target**: Select the "Amount" column and the corresponding row (e.g., "March 2025 sales revenue") <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
8.  **Save to Notion & Save Formula**: Click "Save to Notion" and save this new formula <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

### Calculating Sales Revenue for a Specific Quarter and Category

To find sales revenue for Q1 2025 for the "Software" category <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>:
1.  **New Formula**: Click "New formula" <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
2.  **Paste Database Link**: Paste the sales database link <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
3.  **Define Sum**: Select "sum" for the "Revenue" field for "all the rows" <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
4.  **Add Date Condition**: Add a condition for "Date" "is between" January 1st, 2025, and March 31st, 2025 (representing Q1) <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
5.  **Add Category Condition**: Add another condition using "AND" (important for multiple criteria) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. Set the "Category" property "is" "Software" <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
6.  **Calculate**: Click "Calculate" <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
7.  **Add to Notion**: Create a third Notion database (e.g., "DB_Sales_Category_Q1_2025") <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>. Copy its link and paste it into MyFormulaGen.com <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.
8.  **Specify Target**: Select the "Amount" column and the corresponding row (e.g., "Q1 2025 sales for software") <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
9.  **Save to Notion & Save Formula**: Click "Save to Notion" and save this formula <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.

## Dynamic Updates and Refreshing Data

When source data in the Notion sales database changes, the calculated values in the target Notion databases will not update automatically <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. To refresh them:
1.  Go to the "Saved formulas" section in MyFormulaGen.com <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
2.  Click "Refresh all" to update all saved formulas <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
3.  Alternatively, click "Refresh" next to a specific formula to update only that one <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

This method allows for dynamic updates of [[Using Notion for sales performance overview | sales performance overview]] and [[Using Notion to track sales receipts | sales receipts]] without needing to manually re-enter data or build complex Notion formulas.

## Conclusion

Using MyFormulaGen.com provides a straightforward way to implement [[Creating custom formulas and linking databases in Notion | custom formulas and linking databases in Notion]] for [[Using formulas to add numbers in Notion | summing numbers]], applying filters, and performing other [[Using formulas to subtract in Notion | calculations]] without delving into the intricacies of Notion's native formula language <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. This approach is dynamic and user-friendly, allowing for multiple operators and conditions to achieve desired results <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

For any queries, feel free to reach out via email at notionformy@gmail.com <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>.