---
title: Using rollup and formula properties in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[calculating_sum_of_a_column_in_notion | calculate the sum of a column in Notion]] and use that sum for further calculations, such as percentages, by leveraging [[database_relations_and_rollup_properties_in_notion | database relations]], rollup, and [[using_formulas_in_notion | formula properties]].

## Calculating the Sum of a Column

To find the sum of values in a column, such as sales amounts, across multiple rows, you can set up a system involving two databases.

### Initial Setup
Begin with a database containing your data, for example, a list of sales people and their sales amounts [00:00:03].
For instance:
*   Harry: $2,100 <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
*   Eric: $3,400 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Peter: $5,400 <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>

Next, create a new database to hold the total sum. This database can be named, for example, "Total Sales" [00:00:31].

### Establishing a Relationship
To link the sales data to the total sales database, you need to create a [[database_relations_and_rollup_properties_in_notion | relationship]] between them [00:00:42].
1.  In your main sales database, add a new property [00:00:53].
2.  Select "Relation" as the property type [00:00:54].
3.  Choose the "Total Sales" database to create the relationship [00:01:04].
4.  Name the properties in both databases to clearly indicate their purpose (e.g., "Total Sales" in the main database and "Sales Details" in the "Total Sales" database) [00:01:14].
5.  Once the relation is established, link all sales entries in the main database to the single "Total Sales" entry in the new database by selecting "Total Sales" in the newly created relation column for each row [00:01:33]. This action populates the related sales people information in the "Total Sales" database [00:01:43].

### Creating a Rollup for the Sum
A rollup property allows you to aggregate data from a related database [00:01:50].
1.  In the "Total Sales" database, add a new property and select "Rollup" [00:01:50].
2.  For the "Relation" field, select the relationship established (e.g., "Sales Detail") [00:01:57].
3.  For the "Property" field, select the column you want to sum (e.g., "Sales") [00:02:00].
4.  For the "Calculate" field, choose "Sum" [00:02:26]. This will display the total sum of all sales values from the main database [00:02:30].
5.  Name this column appropriately, e.g., "Total Sales Rollup" [00:02:40].

### Converting Rollup to Formula for Further Use
A crucial step for rolling up an existing rollup value into another database is to convert the rollup to a formula property [00:03:09]. Rollup values directly cannot be rolled up again in another database [00:03:14].
1.  In the "Total Sales" database, create another new property [00:03:20].
2.  Change its type to "Formula" [00:03:27].
3.  Within the formula, simply link it to the "Total Sales Rollup" property (e.g., `prop("Total Sales Rollup")`) [00:03:31].
4.  You can also format this formula property as a currency, such as dollars [00:03:37].

### Displaying the Total Sum in the Original Database
To bring the calculated total sum back to your main sales database:
1.  In the main sales database, add a new property [00:02:50].
2.  Select "Rollup" as the property type [00:02:52].
3.  For the "Relation" field, select "Total Sales" (the relation to your second database) [00:03:01].
4.  For the "Property" field, select the *formula* property (e.g., "Total Sales") you created in the "Total Sales" database [00:03:04].
5.  For the "Calculate" field, choose "Sum" [00:03:56].
This will now display the grand total sales value in your main sales database, dynamically updating as sales figures change [00:03:58].

## Calculating Percentages

Once you have the total sales value, you can use it to [[using_formulas_in_notion | calculate percentages]] for each individual sale relative to the total.

### Creating the Percentage Formula
1.  In your main sales database, add a new property and select "Formula" [00:04:26].
2.  To calculate the percentage of each individual sale out of the total sales, [[formulas_for_multiplication_in_notion | divide]] the individual "Sales" amount by the "Sales Total" (the rollup property showing the grand total) [00:04:34].
    *   Formula: `prop("Sales") / prop("Sales Total")` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>

### Formatting the Percentage
To display the percentage clearly with two decimal places:
1.  Edit the formula.
2.  Use the `round()` function and multiply by 100 before dividing by 100 to achieve two decimal places [00:04:50].
    *   Formula: `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
3.  Change the "Number format" of the property to "Percentage" [00:05:10]. This will automatically format the number as a percentage (e.g., 20.00%) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

### Visualizing with a Progress Bar
You can further customize the percentage column to show a progress bar:
1.  Click on "Edit property" for the percentage column [00:05:17].
2.  Under "Show as," select "Bar" [00:05:20]. This provides a visual representation of each individual sale's contribution to the total [00:05:21].

All these values will automatically update as you change the individual sales figures in your main database [00:05:30].