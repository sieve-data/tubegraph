---
title: Calculating percentages and formatting data
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

Calculating the sum of a column and then deriving percentages for individual values in Notion involves setting up relationships between databases and utilizing [[using_rollup_and_formula_properties | rollup and formula properties]] <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This method allows for [[calculating_custom_data_summaries_in_notion | custom data summaries]] <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a> and dynamic percentage [[calculating_expense_differences_and_budget_percentages | calculations]] <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a> that automatically update with data changes <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Setting Up Databases

### Initial Sales Database

Begin with a database containing individual sales data, such as a list of salespeople and their respective sales amounts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. For example:
*   Harry: $2,100 <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
*   Eric: $3,400 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Peter: $5,400 <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>

### Creating a Total Sales Database

To calculate the sum of a column, create a second, separate database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
1.  Type `/` and select `database` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  Name this database, for example, `Total Sales` <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
3.  Delete any default rows except one <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### Establishing a Relationship

Connect the two databases using a `Relation` property <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
1.  In the `Total Sales` database, click the `+` icon to add a new property <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  Select `Relation` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  Choose your initial sales database (e.g., "Sales") to link <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
4.  Configure the relationship to show reciprocal properties in both databases (e.g., `total sales` in the first database and `sales details` in the second) <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
5.  Once the relationship is established, link all entries in the sales database to the single entry in the `Total Sales` database <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Calculating Total Sales

### Using a Rollup Property

In the `Total Sales` database, add a `Rollup` property to sum the sales amounts <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
1.  Add a new property and select `Rollup` <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
2.  Select the `sales detail` relation <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
3.  Choose the `Sales` property from the original database to roll up <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
4.  Under `Calculate`, select `Sum` to get the total <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This will display the total sales (e.g., $10,900) <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Converting Rollup to Formula

A direct rollup of a rollup value cannot be performed <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. To make the total sales accessible in the main database, convert the rollup value into a [[using_formulas_for_financial_calculations_in_Notion | formula property]] <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
1.  In the `Total Sales` database, create a new `Formula` property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  Name it, for example, `Total Sales (Formula)` <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  Set the formula to simply reference your rollup property (e.g., `prop("Total Sales Rollup")`) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
4.  Set the number format to `Dollars` or your preferred currency <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Displaying Total Sales in Main Database

Now, bring the total sales value back to your main sales database:
1.  Add another `Rollup` property in the main sales database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Select the `Total Sales` relation <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
3.  Choose the `Total Sales (Formula)` property created in the second database <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
4.  Under `Calculate`, select `Sum` <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This will display the overall total sales for each row <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

## Calculating Individual Sales Percentage

With the individual sales and the total sales available in the same database, you can now [[calculating_profit_and_loss_for_inventory_sales | calculate]] <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a> each salesperson's contribution as a percentage.

### The Percentage Formula

1.  Add a new `Formula` property to your main sales database <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  Name it, for example, `Sales in Percentage` <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
3.  The basic formula to divide individual sales by total sales would be: `prop("Sales") / prop("Sales Total")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Formatting the Output

To format the percentage for better readability:
1.  **Round to two decimal places:** Wrap the division in a `round()` function and multiply/divide by 100 to shift decimals for rounding: `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
2.  **Display as Percentage:** In the property settings, change the `Number format` to `Percentage` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
3.  **Add a Progress Bar:** For a visual representation, in the property settings, select `Bar` under `Show as` <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

The result is a dynamic column showing each salesperson's percentage of total sales with a visual bar <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Dynamic Updates

Any changes made to the individual sales amounts in the first database will automatically update the total sales and the calculated percentages <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This dynamic capability is useful for [[updating_and_managing_budget_summaries | budget summaries]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>, [[using_dynamic_views_for_monthly_and_yearly_savings_tracking | tracking savings]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>, or creating [[analyzing_financial_data_with_a_dashboard | financial dashboards]] <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a> in Notion <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.