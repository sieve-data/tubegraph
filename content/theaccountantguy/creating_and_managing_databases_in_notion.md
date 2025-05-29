---
title: Creating and managing databases in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

[[Creating a database in Notion | Creating a database in Notion]] is a fundamental step for organizing information and performing calculations, such as summing a column. This guide details how to set up and manage multiple Notion databases, establish relationships between them, and use advanced features like rollups and formulas to derive meaningful insights.

## Setting up a Database in Notion

To begin, you need to [[setting_up_a_database_in_notion | set up a database in Notion]]. For example, you might have a database listing salespeople with their respective sales amounts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

### Creating a New Database

1.  Type `/database` to create a new database <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  Name the database, for instance, "Total Sales" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
3.  Delete any default rows that are not needed <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Connecting Databases in Notion

Once you have multiple databases, you can [[connecting_a_database_in_notion | connect them to create relationships]], allowing for more complex data management and calculations.

### Establishing a Relationship

1.  In one of the databases (e.g., the "salespeople" database), click the `+` button to add a new column <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
2.  Select `Relation` as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  Choose the database you want to link to (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Define how the relationship columns will be named in both databases (e.g., "Total Sales" in the first database and "Sales Details" in the "Total Sales" database) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
5.  After creating the relationship, link individual entries. For instance, in the first database, link all salespeople to the "Total Sales" entry in the second database <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This automatically pulls in related information <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Calculating Sums with Rollup

To sum values from one database in another, you use the `Rollup` property. This is a key step in [[creating_and_linking_notion_databases | creating and linking Notion databases]] for advanced calculations.

### Rolling Up Sales Values

1.  In the target database (e.g., "Total Sales"), click the `+` button to add a new column <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select `Rollup` as the property type <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
3.  Choose the relationship property (e.g., "Sales Detail") <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
4.  Select the property to be rolled up (e.g., "sales value") <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
5.  Under "Calculate," change the default setting to `Sum` to aggregate the values <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
6.  Name this new property (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Displaying the Sum in the First Database

To display the calculated sum back in the original database, an additional step is required because a rollup of a number cannot be directly rolled up again <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>, <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

1.  In the "Total Sales" database, create a new `Formula` property <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
2.  Name it (e.g., "Total Sales") and link it to the "Total Sales Rollup" property you just created <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This converts the rollup value into a formula property <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Format the property as currency if needed <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
4.  Now, in the first database, create another `Rollup` property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
5.  Select the `Total Sales` relationship and the new `Total Sales` formula property to roll up <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>, <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
6.  Set the calculation to `Sum` <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This will display the total sales value from the second database in the first database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

## Advanced Calculations: Percentage

You can use the total sum to perform further calculations, such as determining each individual's sales as a percentage of the total.

### Calculating Percentage of Total Sales

1.  Create a new `Formula` property (e.g., "Sales in Percentage") <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  Enter the formula: `prop("Sales") / prop("Sales Total")` to divide individual sales by the total sales <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>, <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
3.  To round to two decimal places, wrap the calculation with `round` and multiply/divide by 100: `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>, <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
4.  Edit the property type to change the number format to `Percentage` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>, <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
5.  Optionally, select `Bar` as the format to visualize the percentage <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

Any changes to individual sales values will automatically update the total sales and percentage calculations <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This demonstrates how to [[creating_databases_in_notion | create databases in Notion]] and [[using_databases_in_notion_for_financial_tracking | use databases in Notion for financial tracking]] and other complex data management tasks. You can further expand on these techniques for [[creating_content_in_notion_databases | creating content in Notion databases]], [[integrating_databases_with_templates_in_notion | integrating databases with templates in Notion]], and even [[setting_up_and_managing_notion_databases_for_pdf_generation | setting up and managing Notion databases for PDF generation]].