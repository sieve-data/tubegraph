---
title: Establishing relationships between Notion databases
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

This article details how to [[Connecting Relational Databases in Notion | establish relationships between Notion databases]] to perform calculations like summing a column, and then using those sums for further analysis within your data. This process involves creating relationships, using rollup properties, and employing formulas for advanced calculations <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Setting Up Databases <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>

To begin, you will need at least two [[Creating a database in Notion | Notion databases]] to create a relationship.

1.  **Primary Database**: This database contains your individual data entries. For example, a "Sales People" database might list sales individuals and their respective sales amounts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.
2.  **Secondary Database**: This database will be used to aggregate information from the primary database.
    *   Create a new database by typing `/database` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
    *   Name this database (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
    *   Delete any default rows or columns that are not needed <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Creating a Relationship Between Databases <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

A relationship property links entries across two databases, allowing you to pull information from one into the other.

1.  In your primary database, add a new column by clicking the `+` button <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
2.  Select `Relation` as the property type <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
3.  Choose your secondary database (e.g., "Total Sales") to establish the connection <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Configure the relationship names for both databases:
    *   In the primary database, the column can be named "Total Sales" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   In the secondary database, the corresponding column can be named "Sales Details" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
5.  After establishing the relationship, a new column will appear in both databases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
6.  In the primary database's new relation column, select the entry from your secondary database (e.g., the "Total Sales" entry) that you want to associate with each row in the primary database. Copy this association down to all relevant rows <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This links the individual sales records to the single "Total Sales" entry in the secondary database <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Aggregating Data with Rollup <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>

A rollup property pulls specific information from a related database and allows you to perform calculations on it.

1.  In your secondary database (e.g., "Total Sales"), add a new column <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select `Rollup` as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
3.  Configure the rollup:
    *   **Relation**: Select the relationship you just established (e.g., "Sales Detail") <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   **Property**: Choose the column from the primary database that contains the values you want to aggregate (e.g., "Sales amount") <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
    *   **Calculate**: To get the sum of the column, click on "Original Values" and select `Sum` <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
4.  Name this new rollup column (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This column will now display the sum of all sales from your primary database <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

> [!NOTE] Limitations of Rollup Properties
> Directly rolling up a rollup value into another database is not possible if the rollup's result is a number <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. To overcome this, you must first convert the rollup value into a formula property <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Making Rollup Values Available for Further Calculations <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>

To use the summed rollup value in other databases or calculations, convert it into a formula property:

1.  In the secondary database, add a new property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  Name it (e.g., "Total Sales") and change its type to `Formula` <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  In the formula editor, simply reference the rollup property you created (e.g., `prop("Total Sales Rollup")`) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This converts the rollup value into a formula output, making it accessible for further rollups <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  Optionally, format the number as currency (e.g., Dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## Displaying Aggregated Data in the Original Database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>

To display the total sales value (from the secondary database) back in your primary database:

1.  In your primary database, add a new column and select `Rollup` <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Configure this new rollup:
    *   **Relation**: Select the relationship (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   **Property**: This time, select the new `Formula` property you created in the secondary database (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   **Calculate**: Choose `Sum` <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
3.  This will display the total sales value from the secondary database in every row of your primary database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

## Advanced Calculations: Percentage Contribution <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

You can use the aggregated total sales value to perform further calculations, such as determining each individual's percentage contribution to the total sales.

1.  In your primary database, add a new column and select `Formula` <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  Name it (e.g., "Sales in percentage") <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
3.  Enter the formula to divide individual sales by the total sales: `prop("Sales amount") / prop("Sales Total")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
4.  To round to two decimal places and display as a percentage, modify the formula: `round(prop("Sales amount") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
5.  Edit the property and change the "Number format" to `Percentage` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
6.  You can further customize the display by selecting `Bar` in the property settings to visualize the percentage <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Any changes to individual sales values will automatically update the total sales and percentage calculations across all linked databases <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This method allows for dynamic and interconnected [[Setting up and using databases in Notion | database management in Notion]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.