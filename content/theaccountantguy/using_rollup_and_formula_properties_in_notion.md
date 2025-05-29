---
title: Using rollup and formula properties in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[using_notion_for_calculations | use Notion for calculations]], specifically how to calculate the sum of a column, display it in another database, and perform percentage calculations using a combination of rollup and formula properties <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. The examples focus on [[managing_sales_data_with_formulas_in_notion | managing sales data with formulas in Notion]].

## Calculating the Sum of a Column

To calculate the sum of values in a column across multiple rows, you can use a combination of related databases and rollup properties.

### Scenario Setup
Consider a database with `Sales People` listed in rows, each with an `Adjustment Column` showing their `Sales Amount`. For example, Harry has $2,100, Eric has $3,400, and Peter has $5,400 <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The goal is to see the total sum of these amounts (e.g., $10,900) in an adjacent column <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Creating a Second Database
First, create a new database, for instance, named `Total Sales` <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Delete any default rows or columns not needed <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### Establishing a Relationship
1.  In the main `Sales People` database, add a new property by clicking the plus icon <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  Select `Relation` as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  Select the `Total Sales` database to create a relationship <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Configure the relationship names for clarity:
    *   In the first database (Sales People), name it `Total Sales` <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   In the second database (Total Sales), name it `Sales Details` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   This action adds a new column in both databases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
5.  In the `Total Sales` column of the main `Sales People` database, click on the column cells and select the single entry available from the `Total Sales` database <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Copy this down to all sales people's data <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This links all sales records to the single entry in the `Total Sales` database <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Using Rollup Property to Sum
1.  In the `Total Sales` database, add a new property by clicking the plus button <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select `Rollup` as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
3.  Configure the rollup:
    *   Select the `Sales Details` relationship that was just established <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   Choose `Sales` (the column containing the sales amounts) as the property to roll up <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Under `Calculate`, select `Sum` to aggregate all the sales values from the first database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Name this column (e.g., `Total Sales Rollup`) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    This now displays the total sum of sales in the `Total Sales` database <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## Displaying the Total Sum in the First Database

To get this calculated total sum back into the original `Sales People` database, an intermediate step involving a formula is required.

### Challenge with Direct Rollup
A rollup value in one database (e.g., `Total Sales Rollup`) cannot be directly rolled up onto another database if it's already a numerical rollup <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. You must first convert this rollup value into a formula property <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Using a Formula Property
1.  In the `Total Sales` database, add another property and name it (e.g., `Total Sales`) <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
2.  Change its type to `Formula` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
3.  In the formula editor, simply link it to the `Total Sales Rollup` property created earlier. This just passes the rollup value into a formula property <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
4.  Optionally, format the number as currency (e.g., dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Rolling Up the Formula
1.  Return to the original `Sales People` database. Add a new `Rollup` property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Select `Total Sales` as the relationship <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Now, select the `Total Sales` formula property from the `Total Sales` database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
4.  Under `Calculate`, select `Sum` <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    The total sales value from the second database is now visible in the first database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Name this column (e.g., `Sales Total`) <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Advanced Calculation: Percentage of Total Sales
You can [[displaying_percentage_calculations_in_notion | display percentage calculations in Notion]] by [[using_formulas_in_notion | using formulas in Notion]] to show each individual sale's contribution to the total.

1.  In the `Sales People` database, add a new `Formula` property named `Sales in Percentage` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
2.  Enter the formula to divide individual `Sales` by the `Sales Total` (the rollup property just created): `prop("Sales") / prop("Sales Total")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  To format it to two decimal places, wrap the calculation using the `round` function: `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
4.  Click on the property, select `Edit Property`, and change the `Number format` to `Percentage` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
5.  Optionally, select a `Bar` under `Show as` to get a visual representation of the percentage <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Any changes made to individual sales values will automatically update the `Sales Total` and the `Sales in Percentage` calculations <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This demonstrates how to [[using_formulas_to_add_numbers_in_notion | use formulas to add numbers in Notion]] and derive further insights.