---
title: Calculating sum of a column in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

To [[using_the_sum_function_in_notion | calculate the sum of a column]] in Notion, especially when you need to use that sum for further calculations within the database, a multi-step process involving multiple databases, relationships, and rollup properties is used <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Initial Database Setup

Start with a database containing numerical data that needs to be summed, such as sales figures for different salespeople <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. For example, a database might list salespeople in rows with a "Sales Amount" column <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Creating a Second Database for Totals

1.  Create a new database by typing `/database` and selecting `Database - Inline` or `Database - Full page` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  Name this new database, for instance, "Total Sales" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
3.  Delete any default rows or columns not needed in this new database <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Establishing a Relationship Between Databases

To connect the two databases:
1.  In the first database (e.g., "Sales People"), add a new property by clicking the `+` button <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  Select `Relation` as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  Choose the second database (e.g., "Total Sales") to create the relationship <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Configure the relationship properties:
    *   In the "Sales People" database, name the relation column "Total Sales" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   In the "Total Sales" database, name the relation column "Sales Details" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
5.  A new column will appear in both databases, linking them <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Populating the Relationship Property

In the first database ("Sales People"), click on the newly created "Total Sales" column for each row and select the single row from the "Total Sales" database <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This links all sales entries to the single total entry <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## Rolling Up Sales Data in the Second Database

1.  In the second database ("Total Sales"), add a new property <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select `Rollup` as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
3.  Configure the rollup:
    *   Under "Relationship," select "Sales Detail" (the relationship pointing to the first database) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   Under "Property," select the "Sales Amount" column from the first database <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Under "Calculate," choose `Sum` to [[adding_numbers_in_notion | add]] all the sales amounts <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
4.  This rollup property will now display the [[using_the_sum_function_in_notion | sum]] of all sales amounts <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. You can name this column "Total Sales Rollup" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Bringing the Total Sales Value Back to the First Database

To use the calculated total in the original database for further calculations, a workaround is needed:
1.  **Convert Rollup to a Formula Property**: In the "Total Sales" database, create a new property.
    *   Name it "Total Sales" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Change its type to `Formula` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   The [[using_formulas_in_notion | formula]] should simply reference the "Total Sales Rollup" property (e.g., `prop("Total Sales Rollup")`) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   Format this property as currency (e.g., Dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
2.  **Rollup the Formula Property**: In the first database ("Sales People"), add another `Rollup` property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Under "Relationship," select "Total Sales" (the relation pointing to the second database) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   Under "Property," select the "Total Sales" *formula property* from the second database <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
    *   Under "Calculate," choose `Sum` <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
3.  This new rollup column in the first database will now display the overall total sales for every row <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

## Calculating Percentage of Total Sales (Optional)

With the individual sales and the total sales available in the same database, you can [[calculating_custom_data_summaries_in_notion | calculate]] percentages:
1.  Add a new `Formula` property to the first database, named "Sales in Percentage" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  The [[using_formulas_in_notion | formula]] to calculate the percentage is `prop("Sales Amount") / prop("Sales Total")` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
3.  To round to two decimal places, modify the [[using_formulas_in_notion | formula]] to `round(prop("Sales Amount") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
4.  Change the "Number format" of this property to `Percentage` <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
5.  Optionally, change the `Show as` format to `Bar` for a visual representation <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

Any changes to individual sales values will automatically update the total sales and the percentage calculations <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.