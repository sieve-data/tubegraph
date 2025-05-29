---
title: Creating relationships between databases
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

This article details how to calculate the sum of a column in Notion using database relationships, rollups, and formulas. This method allows for dynamic updates when data changes <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.

## Setting Up Your Databases

To begin, you will need at least two Notion [[creating_databases_for_expense_tracking | databases]].
For example, consider a sales tracking scenario:
1.  **First Database (Sales Data):** Contains individual sales records, such as "sales people" in different rows and their "sales amount" in an "adjustment" column <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.
2.  **Second Database (Total Sales):** This database will be used to aggregate information from the first one. Create it by typing `/database` and name it, for example, "Total Sales" <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Delete any default rows that are not needed <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Establishing a Relationship

The core of this process is [[connecting_notion_databases_with_external_tools_using_api_keys | connecting]] the two [[defining_connection_databases_in_wizzygen | databases]] through a relationship:

1.  In your *first database* (Sales Data), click the `+` button to add a new property <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
2.  Select "Relation" as the property type <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
3.  Choose the *second database* ("Total Sales") to link to <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Configure the relationship properties:
    *   In the first database, name the column that represents the link to "Total Sales" (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
    *   In the second database, name the column that represents the link back to the sales details (e.g., "Sales Details") <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
5.  After creating the relationship, a new column will appear in both [[creating_databases_for_expense_tracking | databases]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
6.  In the first database's "Total Sales" column, click on each cell and select the entry from the "Total Sales" database <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Copy this down for all entries to link them to the single entry in the "Total Sales" database <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This will automatically feed the sales people's information into the second database <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Calculating Totals Using Rollup

Now, use a "Rollup" property in the "Total Sales" database to sum the sales amounts:

1.  In the *second database* ("Total Sales"), click the `+` button to add a new property <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
3.  Under "Relationship," select the relationship you just established (e.g., "Sales Detail") <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
4.  Under "Property," select the column you want to sum (e.g., "Sales value") <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This will show the individual values from the first database <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  Under "Calculate," choose "Sum" to aggregate all values <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
6.  Name this column (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Bringing the Total Back with a Formula Workaround

You cannot directly roll up a "Rollup" value into another database as a number <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. A "Formula" property is needed to convert the rollup into a usable number:

1.  In the *second database* ("Total Sales"), add another new property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  Name it (e.g., "Total Sales") and change its type to "Formula" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  In the formula editor, simply reference the "Total Sales Rollup" property: `prop("Total Sales Rollup")` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This copies the rollup value into a formula property <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  Optionally, change the currency format to dollars or your preferred currency <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
5.  Now, in the *first database* (Sales Data), add another "Rollup" property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
6.  Select the "Total Sales" relationship <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
7.  Select the new "Total Sales" *formula* property from the second database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
8.  Choose "Sum" as the calculation <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
9.  This will display the total sales value from the second database onto the first database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Name this column (e.g., "Sales Total") <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Calculating Percentages and Visualizing Data

You can now calculate percentages for individual sales relative to the total sales:

1.  In the *first database*, add a new "Formula" property (e.g., "Sales in Percentage") <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
2.  The formula to calculate the percentage is `prop("Sales") / prop("Sales Total")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  To round to two decimal places, use: `round(prop("Sales") * 100 / prop("Sales Total")) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
4.  Edit the property and change the number format to "Percentage" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
5.  Further enhance the visualization by selecting "Bar" under the property options <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This provides a visual representation of each individual sale compared to the total <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

Any changes made to the individual sales values in the first database will automatically update the total sales and percentage calculations <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This method demonstrates how to effectively [[using_databases_for_financial_tracking_in_notion | use databases for financial tracking in Notion]] and perform [[automating_expenses_tracking_through_databases | automated expense tracking through databases]].