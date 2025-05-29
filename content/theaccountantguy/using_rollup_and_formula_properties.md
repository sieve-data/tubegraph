---
title: Using rollup and formula properties
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

To calculate the sum of a column in Notion, such as total sales, and use that sum for further calculations like percentages, you can leverage a combination of [[using_rollup_and_relation_properties_in_notion | Rollup]] and [[using_formulas_in_notion | Formula properties]] <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This method allows for dynamic updates across related databases.

## Setting Up Databases

First, create a second database in Notion <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. For instance, if you have a sales database with individual sales figures, you might name this new database "Total Sales" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Establishing a Relationship

1.  In your primary database (e.g., "Sales"), click the `+` button to add a new property <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
2.  Select "Relation" as the property type <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
3.  Choose the newly created "Total Sales" database to establish the relationship <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Configure the column names for both databases within this relationship: for the primary database, name it "Total Sales," and for the "Total Sales" database, name it "Sales Details" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
5.  Once the relationship is established, populate the "Total Sales" column in your primary database by selecting "Total Sales" for all entries <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This links all sales records to the single entry in the "Total Sales" database.

## Calculating the Sum with Rollup

1.  In the "Total Sales" database, add a new property by clicking the `+` button <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
3.  In the Rollup configuration:
    *   For the "Relationship" field, select "Sales Detail" (the relation established earlier) <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   For the "Property" field, select the "Sales" property from your primary database <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   For the "Calculate" field, choose "Sum" to aggregate all the sales values <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
4.  Name this new property (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This will display the sum of all sales from your primary database in the "Total Sales" database.

## Rolling Up the Sum into the Primary Database

Directly rolling up a rollup value into another database is not possible <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. To overcome this:

1.  In the "Total Sales" database, create another property, this time selecting "Formula" as the type <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
2.  Name it "Total Sales" (or similar) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
3.  In the [[using_formulas_in_notion | formula]] editor, simply reference the "Total Sales Rollup" property (e.g., `prop("Total Sales Rollup")`) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This effectively converts the rollup value into a [[using_formulas_in_notion | formula]] property <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  Optionally, format the number as currency (e.g., Dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
5.  Now, in your primary database, add another [[using_rollup_and_relation_properties_in_notion | Rollup]] property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
6.  For the "Relationship" field, select "Total Sales" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
7.  For the "Property" field, select the newly created "Total Sales" [[using_formulas_in_notion | formula]] property <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
8.  Choose "Sum" for the "Calculate" field, and the total sales figure will appear in your primary database <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Calculating Percentages Using Formulas

Once you have the total sales in your primary database, you can use [[using_formulas_in_notion | formulas]] to calculate the percentage of individual sales relative to the total:

1.  Add a new "Formula" property to your primary database, for example, "Sales in Percentage" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  The [[using_excelstyle_formulas_in_notion | formula]] to divide individual sales by the total sales would be `prop("Sales") / prop("Sales Total")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  To round the percentage to two decimal places, wrap the calculation with `round()` and multiply/divide by 100: `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
4.  Change the number format of the [[using_formulas_in_notion | formula]] property to "Percentage" <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
5.  For visual representation, you can select "Bar" under the "Show as" option in the property settings <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Any changes made to individual sales figures will automatically update the total sales and the calculated percentages <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.