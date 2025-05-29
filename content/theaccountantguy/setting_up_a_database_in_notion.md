---
title: Setting up a database in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

This guide explains [[how_to_create_a_database_in_notion | how to create a database in Notion]] and perform calculations, specifically summing values in a column and calculating percentages based on that sum <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Creating a New Database

To begin, create a new database:
1.  Type `/database` to create a new database <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  Name the database (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Delete any default rows or columns that are not needed <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Establishing a Relationship Between Databases

To calculate the sum of a column from one database and display it in another, you need to establish a relationship between them <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
1.  In the first database (e.g., "Sales People"), click the "plus" button to add a new property <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
2.  Select "Relation" as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  Select the second database (e.g., "Total Sales") to link to <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Define the names for the relationship columns in both databases (e.g., "Total Sales" in the first database and "Sales Details" in the second) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
5.  Once the relationship is created, a new column will appear in both databases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. In the first database, fill the new "Total Sales" column by selecting the name of the second database's entry (e.g., "Total Sales") and copying it down for all relevant rows <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This links the sales people to the total sales entry <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Aggregating Data with Rollup

Use the "Rollup" property to aggregate data from the linked database:
1.  In the second database (e.g., "Total Sales"), click the "plus" button to add a new property <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
3.  From the "Relationship" dropdown, select the established relationship (e.g., "Sales Detail") <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
4.  From the "Property" dropdown, select the column you want to sum (e.g., "Sales") <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
5.  By default, it may show individual values; to sum them, click on the displayed values and select "Sum" from the "Calculate" options <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
6.  Name this new rollup column (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Converting Rollup to Formula for Further Calculations

A rollup value cannot be directly rolled up onto another database. It first needs to be converted into a formula property <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
1.  In the second database, create a new property and name it (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  Change its type to "Formula" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
3.  In the formula editor, simply link it to the "Total Sales Rollup" property <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
4.  Optionally, change the number format to currency (e.g., dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

Now, you can roll up this formula value back to the first database:
1.  In the first database, add a new "Rollup" property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Select the "Total Sales" relationship <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Select the new "Total Sales" formula property from the second database <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
4.  Again, select "Sum" for the calculation <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This will display the grand total sales in the first database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
5.  Name this column (e.g., "Sales Total") <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Performing Percentage Calculations

You can calculate the percentage of each individual sale relative to the total sales:
1.  In the first database, add a new property and name it (e.g., "Sales in Percentage") <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  Change its type to "Formula" <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
3.  Enter the formula to divide individual sales by the total sales (e.g., `prop("Sales") / prop("Sales Total")`) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
4.  To round to two decimal places, wrap the formula: `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
5.  [[Customizing databases in Notion | Customize the number format]] to "Percentage" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Customizing Display

[[Customizing databases in Notion | You can customize the display]] of the percentage column further:
1.  Click on the percentage column's property name and select "Edit property" <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
2.  Under "Show as", select "Bar" to visualize the percentage with a progress bar <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Any changes made to the individual sales values in the first database will automatically update the total sales and percentage calculations across both databases <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This demonstrates [[creating_a_database_in_notion_for_calculations | how to create a database in Notion for calculations]].