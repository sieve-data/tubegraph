---
title: Creating and setting up a Notion database
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

Notion databases can be used to organize and calculate data, such as sales figures [00:00:03]. This guide explains how to [[creating_a_database_in_notion | create]] a database, [[establishing_relationships_between_notion_databases | establish relationships]] between databases, and perform calculations like summing columns and calculating percentages.

## Setting Up a New Database

To [[setting_up_and_using_databases_in_notion | set up]] a new database:
1.  Type `/database` in a Notion page [00:00:27]. This creates a new inline database [00:00:29].
2.  Name the database (e.g., "total sales") [00:00:35].
3.  Delete any default rows that are not needed [00:00:37].

## Establishing Relationships Between Databases

To connect two databases (e.g., a "Sales People" database and a "Total Sales" database):
1.  In the first database, add a new property by clicking the `+` button [00:00:52].
2.  Select `Relation` as the property type [00:00:54].
3.  Choose the second database (e.g., "total sales") to create the relationship [00:01:04].
4.  Configure the column names for both databases within the relationship settings. For example, "total sales" for the first database and "sales details" for the second [00:01:14].
5.  A new column will appear in both databases, linking them [00:01:23].
6.  In the first database, click into the newly created relation column for each entry and select the corresponding entry from the second database (e.g., select "total sales" for all sales people) [00:01:33]. This ensures all sales data is linked to the single "total sales" entry in the second database [00:01:43].

## Calculating the Sum of a Column Using Rollup

To sum values from one database in another linked database:
1.  In the *second* database (e.g., "total sales"), click the `+` button to add a new property [00:01:48].
2.  Select `Rollup` as the property type [00:01:50].
3.  **Configure the Rollup:**
    *   **Relationship:** Select the relationship property you just established (e.g., "sales detail") [00:01:55].
    *   **Property:** Select the column from the *first* database whose values you want to sum (e.g., "sales value") [00:02:00].
4.  By default, it will show original values [00:02:19]. To sum them, click on the "Calculate" option and select `Sum` [00:02:26].
5.  Name this rollup column (e.g., "total sales R") [00:02:35]. This property now displays the sum of the linked sales values [00:02:31].

## Displaying the Total Sum in the Original Database

To bring the calculated total sum back to the original database, an additional step is needed because a `Rollup` property cannot be directly rolled up again [00:03:09]:
1.  In the *second* database, add a new `Formula` property [00:03:20].
2.  Name this property (e.g., "total sales") [00:03:22].
3.  In the formula editor, simply link it to the previously created `Rollup` property (e.g., `prop("total sales rollup")`) [00:03:31]. This converts the rollup value into a format that can be rolled up [00:03:35].
4.  Optionally, change the number format (e.g., to Dollars) [00:03:37].
5.  Now, in the *first* database, add another `Rollup` property [00:02:50].
6.  **Configure this new Rollup:**
    *   **Relationship:** Select the "total sales" relationship [00:03:01].
    *   **Property:** Select the new `Formula` property you just created in the second database (e.g., "total sales") [00:03:52].
7.  Set the "Calculate" option to `Sum` [00:03:56].
8.  This new rollup property in the first database will now display the total sum of sales [00:03:58]. Any changes to individual sales figures will automatically update this total [00:04:15].

## Calculating Percentage Contribution

You can also calculate the percentage of each individual sale compared to the total sales:
1.  In the first database, add a new `Formula` property [00:04:26].
2.  Name it (e.g., "sales in percentage") [00:04:26].
3.  **Enter the formula:**
    *   To divide individual sales by the total sales: `prop("Sales") / prop("Sales Total")` [00:04:34].
    *   To format to two decimal places: `round(prop("Sales") / prop("Sales Total") * 100) / 100` [00:04:53].
4.  After creating the formula, click on the property header, select `Edit Property`, and change the `Number Format` to `Percentage` [00:05:08].
5.  For visual representation, you can also select `Bar` in the `Show as` option within the property settings [00:05:19]. This creates a progress bar showing the percentage [00:05:22].

This setup allows for dynamic calculations where any changes to the individual sales values automatically update the total sales and percentage contributions [00:05:35].