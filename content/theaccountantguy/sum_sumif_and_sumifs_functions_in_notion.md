---
title: SUM SUMIF and SUMIFS functions in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Notion offers built-in formulas for various calculations, but some advanced summing functionalities, like those found in Excel (e.g., SUM, SUMIF, SUMIFS), can be complex to achieve directly within Notion using its native relation and rollup properties <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a><a class="yt-timestamp" data-t="00:01:06">[01:06]</a>. This guide explores how to leverage an external tool, `myformula.com`, to perform these calculations dynamically and integrate the results directly into Notion databases <a class="yt-timestamp" data-t="00:02:08">[02:08]</a>.

## Getting Started with `myformula.com`

To use `myformula.com` for advanced calculations in Notion, you first need to set up a connection between the two platforms via Notion's API <a class="yt-timestamp" data-t="00:02:13">[02:13]</a>.

### 1. Create a Notion API Key
1.  Log in to `myformula.com` <a class="yt-timestamp" data-t="00:02:20">[02:20]</a>.
2.  Navigate to "Settings" within `myformula.com` and click on "Get API Key" <a class="yt-timestamp" data-t="00:02:41">[02:41]</a>. This will open a new screen where you can create a personal API key <a class="yt-timestamp" data-t="00:02:46">[02:46]</a>.
3.  Click "New integration" <a class="yt-timestamp" data-t="00:02:51">[02:51]</a>.
4.  Give your integration a descriptive name (e.g., "Sum Formula Key") <a class="yt-timestamp" data-t="00:02:53">[02:53]</a>.
5.  Select your Notion workspace <a class="yt-timestamp" data-t="00:03:01">[03:01]</a>.
6.  Click "Save" <a class="yt-timestamp" data-t="00:03:07">[03:07]</a>.
7.  Once created, click on the new integration to reveal its "Internal Integration Secret" <a class="yt-timestamp" data-t="00:03:16">[03:16]</a>.
8.  Click "Show" and then "Copy" the entire API key <a class="yt-timestamp" data-t="00:03:22">[03:22]</a>.
9.  Paste this copied API key into the "Notion API Key" field on `myformula.com` and click "Save Settings" <a class="yt-timestamp" data-t="00:03:26">[03:26]</a>.

### 2. Connect Notion Databases to the API
For `myformula.com` to access your Notion data, you must connect the relevant pages and databases to the API key you just created.

> [!TIP]
> Place all databases you intend to use with `myformula.com` inside a single Notion page. By connecting this parent page to the API key, all contained databases will automatically be connected, simplifying the process <a class="yt-timestamp" data-t="00:03:41">[03:41]</a><a class="yt-timestamp" data-t="00:04:47">[04:47]</a><a class="yt-timestamp" data-t="00:13:01">[13:01]</a>.

1.  In Notion, navigate to the page containing your sales database (or other relevant databases) <a class="yt-timestamp" data-t="00:03:45">[03:45]</a>.
2.  Click the three dots `...` in the top right corner of the page <a class="yt-timestamp" data-t="00:03:50">[03:50]</a>.
3.  Select "Add connections" (or "Connections") <a class="yt-timestamp" data-t="00:03:52">[03:52]</a>.
4.  Search for the name of the API key you created (e.g., "Sum Formula Key") <a class="yt-timestamp" data-t="00:03:55">[03:55]</a>.
5.  Select it and click "Confirm" <a class="yt-timestamp" data-t="00:04:06">[04:06]</a>. This ensures that `myformula.com` has access to the databases on that page <a class="yt-timestamp" data-t="00:04:08">[04:08]</a>.

## Implementing SUM Functions with `myformula.com`

This section demonstrates how to use `myformula.com` to calculate total sums, sums with single conditions (SUMIF), and sums with multiple conditions (SUMIFS), bypassing the need for complex Notion formulas.

### 1. Calculating Total Sales Revenue (SUM)

Let's say you have a "Sales Database" with `Date`, `Product`, `Category`, `Quantity`, `Revenue`, `Payment Method`, and `Sales Channel` fields <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. You want to find the total sales revenue.

1.  **Prepare Notion Database**: Create a new Notion database (e.g., "DB_Sales Revenue Total") with at least two properties: `Description` (Text) and `Amount` (Number) <a class="yt-timestamp" data-t="00:01:21">[01:21]</a>. Add a row named "Total Sales Revenue" <a class="yt-timestamp" data-t="00:01:41">[01:41]</a>.
2.  **Copy Source Database Link**: In Notion, hover over your main "Sales Database" (the source of data), click the six dots `⋮⋮` menu, and select "Copy link" <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
3.  **Configure in `myformula.com`**:
    *   Paste the copied database link into the "Database" field on `myformula.com` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   Select "SUM" as the function <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   Choose "Revenue" as the property to sum <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    *   Ensure "All rows" is selected for the calculation scope <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Remove any default second filter if present <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   Click "Calculate" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. The tool will display the calculated sum (e.g., $1,537) <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
4.  **Add to Notion**:
    *   Click "Add to Notion" <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
    *   Copy the link of your *target* database (e.g., "DB_Sales Revenue Total") <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   Paste it into the designated field in `myformula.com` <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
    *   Select "Amount" as the target column and "Total Sales Revenue" as the target row <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. The calculated total will appear in your Notion database <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
5.  **Save Formula**: Save the formula in `myformula.com` with a descriptive name (e.g., "Total Sales Revenue") <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. This allows for easy re-calculation later <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### 2. Calculating Sales Revenue for a Specific Month (SUMIF)

To find the sales revenue for a particular month (e.g., March 2025), you'll add a date filter.

1.  **Prepare Notion Database**: Create a new Notion database (e.g., "DB_Sales Revenue March 2025") with `Description` and `Amount` properties <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Add a row "Sales Revenue March 2025" <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
2.  **Copy Source Database Link**: Copy the link of your main "Sales Database" <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
3.  **Configure in `myformula.com`**:
    *   Click "New Formula" <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
    *   Paste the source database link <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
    *   Select "SUM" for the "Revenue" property <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   Add a filter condition: select the `Date` property <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   Choose "is between" as the filter type <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
    *   Enter the start and end dates (e.g., "March 1 2025" and "March 31 2025") <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
    *   Click "Calculate" <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. The tool will display the sum for the filtered dates <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
4.  **Add to Notion**:
    *   Click "Add to Notion" <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
    *   Copy the link of the *target* Notion database ("DB_Sales Revenue March 2025") <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
    *   Paste it into `myformula.com` <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
    *   Select "Amount" column and "Sales Revenue March 2025" row <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
5.  **Save Formula**: Save the formula (e.g., "Total Sales Revenue for March 2025") <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

### 3. Calculating Sales Revenue for a Quarter by Category (SUMIFS)

To find the sales revenue for a specific quarter (e.g., Q1 2025) and a particular category (e.g., "Software"), you'll apply multiple conditions.

1.  **Prepare Notion Database**: Create a new Notion database (e.g., "DB_Sales Category Q1 2025") with `Description` and `Amount` properties <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. Add a row "Q1 2025 Sales for Software" <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.
2.  **Copy Source Database Link**: Copy the link of your main "Sales Database" <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
3.  **Configure in `myformula.com`**:
    *   Click "New Formula" <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
    *   Paste the source database link <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
    *   Select "SUM" for the "Revenue" property <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
    *   **First Condition (Date)**:
        *   Add a filter: select the `Date` property <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
        *   Choose "is between" <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.
        *   Enter "January 1 2025" and "March 31 2025" (for Q1) <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
    *   **Second Condition (Category)**:
        *   Click the "Plus" icon to add another condition <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
        *   Ensure the logical operator between conditions is "AND" (important for SUMIFS functionality) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
        *   Select the `Category` property <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
        *   Choose "is" as the filter type <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.
        *   Enter "Software" as the value <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.
    *   Click "Calculate" <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. The tool will display the sum matching both conditions <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.
4.  **Add to Notion**:
    *   Click "Add to Notion" <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
    *   Copy the link of the *target* Notion database ("DB_Sales Category Q1 2025") <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
    *   Paste it into `myformula.com` <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
    *   Select "Amount" column and "Q1 2025 Sales for Software" row <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
    *   Click "Save to Notion" <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.
5.  **Save Formula**: Save the formula (e.g., "Q1 2025 Total Sales for Software") <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

### Refreshing Results in Notion

If the data in your source Notion database changes, the calculated sums in your target Notion databases will not automatically update. To refresh them:

1.  Go to the "Saved Formulas" section in `myformula.com` <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
2.  Click "Refresh All" to re-calculate and update all saved formulas in Notion <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
3.  Alternatively, click the "Refresh" icon next to a specific formula to update only that one <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

This method allows you to perform complex SUM, SUMIF, and SUMIFS operations in Notion without delving into its native formula language, providing a dynamic and user-friendly alternative <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.

For more advanced queries or assistance, you can reach out to Notion Formulator via email at notionformy@gmail.com <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.