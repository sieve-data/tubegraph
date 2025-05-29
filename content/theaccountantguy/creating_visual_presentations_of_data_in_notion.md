---
title: Creating visual presentations of data in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

To create visual presentations of data in Notion, such as calculating column sums and displaying percentages with progress bars, you can leverage database relationships, rollup properties, and formulas. This method allows for dynamic updates as your data changes.

## Calculating Column Sums and Displaying in Another Database

This process involves setting up two databases and linking them.

### Database Setup
1.  **Main Database:** Create a database with your core data, such as `Salespeople` and their `Sales` amounts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. For example, Harry with $2,100, Eric with $3,400, and Peter with $5,400 <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
2.  **Summary Database:** Create a second database, for instance, named "Total Sales" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This database will hold the aggregated total.

### Establishing a Database Relationship
To link your main sales data to the "Total Sales" summary database:
1.  In your main database, add a new property column <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  Select "Relation" as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  Choose your "Total Sales" database to create the relationship <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Configure the column names for both databases in the relationship:
    *   In the main database, name it "Total Sales" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   In the "Total Sales" database, name it "Sales Details" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
5.  For each entry in your main sales database, select the single entry from the "Total Sales" database in the newly created "Total Sales" column <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This links all individual sales records to the single summary record <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### [[applying_formulas_and_rollup_properties_in_notion | Using Rollup Properties]] to Sum Data
Now, in your "Total Sales" database, you can aggregate the sales figures:
1.  Add a new property column <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
3.  Configure the rollup:
    *   **Relation:** Choose "Sales Details" (the relationship you just created) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   **Property:** Select the "Sales" column from your main database <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   **Calculate:** Change the calculation method to "Sum" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This will display the total sum of all sales <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
4.  Name this rollup column (e.g., "Total Sales R") <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Retrieving the Sum Using Formulas
To display the calculated sum back in your main sales database, you need to first convert the rollup value into a [[using_formulas_in_notion | formula property]] in the "Total Sales" database. This is because you cannot directly roll up a rollup value from another database <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

1.  In your "Total Sales" database, add a new property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  Name it "Total Sales" and set its type to "Formula" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  In the formula editor, simply refer to your "Total Sales R" rollup property (e.g., `prop("Total Sales R")`) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
4.  You can also format this as a currency (e.g., dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

Now you can roll up this formula property into your main database:
1.  In your main sales database, add another "Rollup" property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Configure it:
    *   **Relation:** Choose "Total Sales" (the relation column in this database) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   **Property:** Select the new "Total Sales" formula property you just created in the "Total Sales" database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   **Calculate:** Choose "Sum" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   This will display the total sales sum in your main database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Name this column "Sales Total" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Any changes made to individual sales amounts will automatically update the "Sales Total" sum <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This setup is useful for a [[using_notion_for_sales_performance_overview | sales performance overview]].

## Displaying Percentage Calculations with Bars

To visualize each salesperson's contribution as a percentage of the total sales:

### Calculating Percentages
1.  In your main sales database, add a new "Formula" property <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Name it "Sales in Percentage" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  The formula to calculate the percentage is `prop("Sales") / prop("Sales Total")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Formatting Percentages
To refine the display of the percentage:
1.  **Round to Two Decimals:** Wrap the calculation in `round()` and multiply/divide by 100 to get two decimal places <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. The formula becomes `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
2.  **Change Number Format to Percentage:** Edit the "Sales in Percentage" property and change the "Number format" to "Percentage" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Visualizing with Progress Bars
For an enhanced [[displaying_percentage_calculations_in_notion | visual presentation]]:
1.  In the "Sales in Percentage" property settings, select "Bar" under the "Show as" option <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
2.  This will display a progress bar for each entry, visually representing its percentage contribution <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

This setup ensures that whenever individual sales values are updated, the total sales sum and corresponding percentages and bars are automatically refreshed <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This method of [[building_dashboard_views_in_notion | building dashboard views in Notion]] allows for effective [[analyzing_financial_data_through_notion_templates | analyzing financial data through Notion templates]]. Further exploration of [[presentation_and_dashboard_setup_in_notion | Notion dashboards]] and [[setting_up_templates_and_buttons_in_notion | templates and buttons]] can enhance data management and visualization.