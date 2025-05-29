---
title: Creating and managing a database in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

Notion allows users to create and manage databases, establish relationships between them, and perform calculations such as summing columns and calculating percentages. This process involves creating databases, linking them through relations, and using Rollup and Formula properties to display aggregated data.

## Creating a Database
To [[creating_database_in_notion | create a new database]] in Notion:
1.  Type `/` and then `database` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  Name the database (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
3.  Delete any default rows or columns as needed <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Establishing Relationships Between Databases
To link two databases, a "Relation" property is used:
1.  In the database where you want to link, click the `+` button to add a new property <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  Select "Relation" as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  Choose the database you want to link to (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Configure the column names for both databases in the relationship (e.g., "Total Sales" in the first database and "Sales Details" in the linked database) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
5.  Once the relationship is established, a new column will appear in both databases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
6.  In the original database, select the related entry in the new column for each row (e.g., select "Total Sales" for all sales people to link them to the "Total Sales" database) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This will automatically populate the related entries in the linked database <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

For more information, see [[establishing_relationships_between_databases_in_notion | Establishing relationships between databases in Notion]].

## Calculating the Sum of a Column Using Rollup and Formula Properties
This section demonstrates how to calculate the sum of a sales column (e.g., for sales people Harry, Eric, and Peter, with sales of $2,100, $3,400, and $5,400 respectively, totaling $10,900) <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

### Step 1: Summing Values in the Second Database (Rollup)
1.  In the second database (e.g., "Total Sales"), add a new property by clicking the `+` button <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
3.  From the "Rollup" menu, select the established relationship (e.g., "Sales Detail") <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
4.  Select the property to roll up (e.g., "Sales value") <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
5.  Change the calculation to "Sum" to get the total of all sales <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
6.  Name this column (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### Step 2: Transferring the Rollup Value to the First Database (Formula)
A rollup value in the form of a number cannot be directly rolled up again into another database <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. It first needs to be converted into a formula property.

1.  **In the second database:**
    *   Create a new "Formula" property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   Name it (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Set the formula to simply reference the "Total Sales Rollup" property <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This transfers the rollup value into a formula property <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   Optionally, change the number format to currency (e.g., Dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
2.  **In the first database:**
    *   Add a new "Rollup" property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Select the existing relationship (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
    *   Select the newly created "Total Sales" formula property from the second database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   Change the calculation to "Sum" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   This will display the total sales value from the second database onto the first <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
    *   Name this column (e.g., "Sales Total") <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Calculating Percentage and Visualizing Data
To calculate the percentage of individual sales against the total sales:
1.  In the first database, add a new "Formula" property <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
2.  Name it (e.g., "Sales in percentage") <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
3.  Set the formula to `prop("Sales") / prop("Sales Total")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
4.  To round to two decimal places, modify the formula: `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
5.  Change the number format to "Percentage" by clicking "Edit property" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
6.  For visual representation, choose a "Bar" style under "Edit property" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Any changes to individual sales values will automatically update the total sales and percentage calculations in real-time <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

This method allows for robust [[using_databases_in_notion_for_financial_tracking | financial tracking]] and can be adapted for [[setting_up_databases_and_dashboards_in_notion | creating end-to-end dashboards]] for business or individual use cases <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.