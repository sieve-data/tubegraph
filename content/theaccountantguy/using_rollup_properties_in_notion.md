---
title: Using rollup properties in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

[[using_formulas_and_rollup_properties_in_notion | Rollup properties]] in Notion are powerful tools that allow you to aggregate information from one database into another, provided there's an established relationship between them <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. This feature is particularly useful for [[calculating_sum_of_a_column_in_notion | calculating sums]], averages, or other aggregate values across related entries.

## Setting Up for Rollup

To use a rollup property, you first need two databases and a relationship established between them <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.

### Example Scenario: Total Sales Database

Consider a scenario where you have a "Sales" database listing individual sales amounts for salespeople and you want to calculate the total sales in a separate "Total Sales" database <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

1.  **Create a New Database**: Start by creating a new database, for instance, named "Total Sales" <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. Delete any default rows that are not needed <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>.
2.  **Establish a Relationship**:
    *   In your "Sales" database, [[adding_properties_in_a_notion_database | add a new property]] and select "Relation" as the type <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>.
    *   Choose your "Total Sales" database to link to <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.
    *   Configure how the relationship columns are named in both databases (e.g., "Total Sales" in the first database and "Sales Details" in the second) <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
    *   Once the relationship is established, populate the new "Total Sales" column in your "Sales" database by selecting the corresponding entry from the "Total Sales" database for all rows <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. This links the individual sales records to a single entry in the "Total Sales" database <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

## Creating a Rollup Property

Now, in your "Total Sales" database, you can create a rollup property to aggregate data from the linked "Sales" database:

1.  [[adding_properties_in_a_notion_database | Add a new property]] and select "Rollup" as the type <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
2.  **Select Relationship**: Choose the relationship you just established (e.g., "Sales Detail") <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.
3.  **Select Property**: Choose the property from the "Sales" database that you want to roll up (e.g., the "Sales" amount column) <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
4.  **Choose Calculation**: By default, it might show "Original Value" <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>. Click on this option and select "Sum" to calculate the total of all the sales amounts linked to this entry <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.
    *   You can rename this column (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.

## Rolling Up a Rollup Property

Sometimes, you might want to bring the aggregated value (like the "Total Sales Rollup") back to your original "Sales" database. Directly rolling up a rollup value that is a number property isn't possible <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. You need an intermediate step:

1.  In your "Total Sales" database, [[adding_properties_in_a_notion_database | create a new property]] and name it (e.g., "Total Sales") <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.
2.  Change its type to "Formula" <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
3.  In the formula editor, simply link it to your existing "Total Sales Rollup" property <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. This converts the rollup value into a formula property <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
4.  You can then format this formula property as currency (e.g., dollars) <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.
5.  Now, go back to your "Sales" database. [[adding_properties_in_a_notion_database | Add another rollup property]].
6.  Select the relationship with the "Total Sales" database <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.
7.  For the property to roll up, select the newly created "Total Sales" formula property <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
8.  Choose "Sum" as the calculation <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
    *   This will display the total sales value from the "Total Sales" database in your "Sales" database <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.

## Calculating Percentages Using Rollup Values

Once you have the total sales value available in your "Sales" database via the rollup, you can perform further [[using_formulas_and_rollup_properties_in_notion | calculations]]. For instance, to calculate the percentage of individual sales against the total sales:

1.  [[adding_properties_in_a_notion_database | Add a new property]] and select "Formula" as the type <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.
2.  [[using_formulas_for_multiplication_in_notion | Use a formula]] to divide the individual sales amount by the total sales amount (e.g., `prop("Sales") / prop("Sales Total")`) <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
3.  To format the result to two decimal places, [[using_formulas_to_add_numbers_in_notion | wrap]] the calculation: `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
4.  [[calculating_percentages_in_notion | Change the number format]] of the formula property to "Percentage" <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
5.  Optionally, customize the display to show a progress bar representing the percentage <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>.

Any changes to the individual sales values will automatically update the total sales and percentage calculations, demonstrating the dynamic nature of [[using_formulas_and_rollup_properties_in_notion | Notion formulas and rollup properties]] <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.