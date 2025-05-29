---
title: Calculating sum of a column in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

This article outlines how to calculate the sum of a column in Notion using relational databases, rollup properties, and formulas. It also demonstrates how to calculate percentages based on the total sum <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Initial Database Setup

Start with a database that includes rows representing sales people and a column for their sales amounts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. For example:
*   Harry: $2,100
*   Eric: $3,400
*   Peter: $5,400

The goal is to sum these amounts, resulting in $10,900 <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Creating a Second Database for Total Sales

1.  Create a new database by typing `/database` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  Name this new database "Total Sales" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
3.  Delete any default rows in this new database <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Establishing a Relationship Between Databases

To perform calculations across databases, you need to [[creating_a_database_in_notion_for_calculations | create a relationship]] between them <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

1.  In your *original* sales database, add a new property by clicking the `+` button <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  Select "Relation" as the property type <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
3.  Choose the "Total Sales" database to link to <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Configure the relationship properties:
    *   In the original database, name the column "Total Sales" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   In the "Total Sales" database, name the corresponding column "Sales Details" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
5.  In the original sales database, click into the "Total Sales" column for each row and select the single entry from the "Total Sales" database. Copy this down to all rows <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This links all sales entries to the single "Total Sales" record <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Calculating the Sum Using Rollup Properties

To get the sum into the "Total Sales" database:

1.  In the "Total Sales" database, add a new [[using_formulas_and_rollup_properties_in_notion | rollup property]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
2.  Select "Sales Details" as the relationship <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
3.  Select "Sales" as the property to roll up (assuming your sales column is named "Sales") <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
4.  Under "Calculate," choose "Sum" to aggregate all the sales values <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
5.  Name this column "Total Sales Rollup" <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This column will now display the total sum of sales from your original database <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## Converting Rollup to a Formula Property

A direct rollup of a rollup value is not possible in Notion <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. To use the "Total Sales Rollup" in another rollup, you must first convert it to a formula property.

1.  In the "Total Sales" database, add another new property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  Name it "Total Sales" (or similar) and set its type to "Formula" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  In the formula editor, simply link to the "Total Sales Rollup" property (e.g., `prop("Total Sales Rollup")`) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This effectively copies the rollup value into a formula property <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  Optionally, change the number format to currency (e.g., Dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## Bringing the Total Sum Back to the Main Database

Now, bring the calculated total sum back to your original sales database for easy reference.

1.  In your *original* sales database, add another new [[using_formulas_and_rollup_properties_in_notion | rollup property]] <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Select "Total Sales" as the relationship <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  For the property to roll up, select the newly created "Total Sales" *formula* property <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
4.  Under "Calculate," choose "Sum" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
5.  Name this column "Sales Total" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

You will now see the total sum of all sales duplicated in every row of your original sales database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Any changes to individual sales amounts will automatically update this total <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This entire process demonstrates how to [[generating_and_managing_sum_function_results_in_notion | generate and manage SUM function results]] effectively across Notion databases.

## Calculating Sales Percentage

You can use the total sales figure to [[calculating_percentages_in_notion | calculate percentages]] for each individual sale relative to the total.

1.  In your original sales database, add a new "Formula" property and name it "Sales in Percentage" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  Enter the following formula to divide individual sales by the total sales:
    ```notion
    prop("Sales") / prop("Sales Total")
    ```
    This formula uses the "Sales" property from your original database and the "Sales Total" rollup property you just created <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  To round the percentage to two decimal places, modify the formula:
    ```notion
    round(prop("Sales") / prop("Sales Total") * 100) / 100
    ```
    This involves [[formulas_for_multiplication_in_notion | multiplying]] by 100, rounding, and then dividing by 100 <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
4.  Finally, edit the property by clicking on it, then change the "Number format" to "Percentage" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
5.  Optionally, select "Bar" under "Show as" to visualize the percentage as a progress bar <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Now, you have a dynamic percentage calculation and visual representation for each sale relative to the total, which automatically updates with any changes to the sales figures <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This method effectively demonstrates [[using_formulas_to_add_numbers_in_notion | using formulas to add numbers in Notion]] (indirectly through the rollup and sum) and presents results clearly.