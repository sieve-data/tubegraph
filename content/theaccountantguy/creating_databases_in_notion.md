---
title: Creating databases in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Notion offers inbuilt formulas for calculations, but it's also possible to integrate Excel-like formulas using external tools like MyFormulaGen.com [00:00:07]. This guide focuses on [[setting_up_a_database_in_notion | setting up databases]] in Notion and connecting them for advanced calculations without relying on Notion's native relation and rollup features [00:02:00].

## Creating a Database
To [[creating_a_database_in_notion | create a new database]] in Notion:
1.  Type `/database` and select "Database - Inline" [00:00:52].
2.  Rename the database by clicking on its title [00:00:56]. For example, `db_for_sales_revenue_total` [00:00:59].
3.  You can hide the database title if desired [00:01:08].
4.  Rename the main column, for example, to "Sales Revenue Total" [00:01:16].
5.  Add new columns to your database, such as "Description" and "Amount" [00:01:23]. The "Amount" column can be set as a "Number" property [00:01:30].
6.  Populate the database with initial data, like "Total Sales Revenue" [00:01:41].

### Example: Sales Database
A common use case is a sales database with fields such as:
*   Date [00:00:24]
*   Product [00:00:25]
*   Category [00:00:25]
*   Quantity [00:00:26]
*   Revenue [00:00:27]
*   Payment Method [00:00:28]
*   Sales Channel [00:00:29]

## Connecting Databases to MyFormulaGen.com (External Tool)
To use Excel-like sum functions for calculations across Notion databases, you can connect them to MyFormulaGen.com [00:02:06]:

### 1. Set Up an API Key
The first step is to establish a connection between Notion and the tool via Notion's API [00:02:32]:
1.  Log in to MyFormulaGen.com [00:02:13].
2.  Navigate to "Settings" and click "Get API Key" [00:02:40].
3.  On the Notion API page, click "New integration" [00:02:51].
4.  Give the integration a name (e.g., "Sum Formula Key") [00:02:53] and select your Notion workspace [00:02:58].
5.  Click "Save" [00:03:04].
6.  Go to "Integrations," click on your newly created key, and reveal the "Internal Integration Secret" [00:03:11].
7.  Copy this API key [00:03:22] and paste it into the "Notion API Key" field on MyFormulaGen.com [00:03:26].
8.  Click "Save Settings" [00:03:30].

### 2. Share Notion Pages with the Integration
For the tool to access your databases, the Notion pages containing them must be shared with the API integration:
1.  Ensure all relevant databases are housed within a single Notion page (e.g., "Sales Dashboard") [00:03:40].
2.  On that Notion page, click the three dots (`...`) menu at the top right [00:03:49].
3.  Select "Connections" [00:03:51].
4.  Type the name of your API key (e.g., "sum formula key") and select it from the list [00:03:55].
5.  Click "Confirm" [00:04:06]. This connects the entire page, and thus all databases within it, to your API key [00:04:10].

### 3. Retrieve Database URLs
To specify which database to pull data from, you need its URL:
1.  Hover over the database in Notion, click the six dots (`⋮⋮`) next to its title [00:04:32].
2.  Click "Copy link" [00:04:38].
3.  Paste this link into the "Notion database link" field on MyFormulaGen.com [00:05:07].

### 4. Performing Calculations and Updating Notion
Once the database link is entered, the tool will enable the "Notion Property" field, allowing you to define calculations:
1.  Select the desired function (e.g., "Sum") and the property to sum (e.g., "Revenue") [00:05:16].
2.  Apply filters based on your requirements (e.g., "all rows," "odd rows," "even rows," "custom rows," or a specific date range) [00:05:28].
3.  Click "Calculate" to see the result [00:05:41].
4.  To push the result back to Notion, click "Add to Notion" [00:06:59].
5.  Paste the URL of the target database where the calculated value should be placed [00:07:07].
6.  Select the specific column (e.g., "Amount") and row (e.g., "Total Sales Revenue") within the target database [00:07:26].
7.  Click "Save to Notion" [00:07:53]. The value will appear in your Notion database [00:07:56].
8.  Save the formula on MyFormulaGen.com with a descriptive name (e.g., "Total Sales Revenue") [00:08:01].

### Updating Calculated Values
If the data in your source database changes, you can refresh the calculated values in Notion:
1.  Go to the "Saved Formulas" section on MyFormulaGen.com [00:08:14].
2.  Click "Refresh all" to update all saved formulas [00:08:55] or click the refresh icon next to a specific formula to update only that one [00:09:15].

## Advanced Calculations with Filters
You can create more complex formulas by adding conditions:

### Example: Total Sales Revenue for a Specific Month
To find the total sales revenue for March:
1.  [[creating_a_database_in_notion | Create a new database]] for this specific calculation (e.g., `db_sales_revenue_March_2025`) [00:11:04].
2.  On MyFormulaGen.com, create a "New Formula" [00:14:46].
3.  Paste the source sales database link [00:14:50].
4.  Select "Sum" for the "Revenue" property for "all the rows" [00:14:55].
5.  Add a filter for the "Date" property [00:15:24].
6.  Set the condition to "is between" March 1st and March 31st [00:15:30].
7.  "Calculate" the result [00:15:53].
8.  "Add to Notion" and select the appropriate column and row in your newly created March sales database [00:12:02].
9.  Save the formula [00:13:52].

### Example: Sales Revenue for a Specific Quarter and Category
To find sales revenue for Q1 2025 for the "Software" category:
1.  Create a "New Formula" on MyFormulaGen.com [00:14:57].
2.  Paste the source sales database link [00:15:00].
3.  Select "Sum" for the "Revenue" property for "all the rows" [00:15:21].
4.  Add the first condition: "Date" property "is between" January 1st, 2025, and March 31st, 2025 (Q1) [00:15:32].
5.  Use an "And" condition to add a second filter [00:16:05].
6.  Add the second condition: "Category" property "is" "Software" [00:16:34].
7.  "Calculate" the result [00:17:07].
8.  [[connecting_a_database_in_notion | Connect]] this result to a dedicated Notion database (e.g., `db_sales_category_q1_2025`) [00:17:50].
9.  Save the formula [00:19:31].

Using MyFormulaGen.com simplifies complex calculations by abstracting Notion's native formulas, making it dynamic and adaptable for various reporting needs [00:22:10].