---
title: Customizing data presentation in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

Notion allows for robust [[customizing_notion_dashboards_and_views | customization]] and calculation of data, including summing columns and presenting values as percentages with visual bars <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This guide demonstrates how to calculate the sum of a column in one database and display it, along with individual percentages, in another, ensuring automatic updates <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Calculating the Sum of a Column

To calculate the sum of a column, like "Sales Amount," across multiple rows in Notion, you will typically need two databases that are related <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

### Setting Up Databases

1.  **First Database (Sales Data):**
    *   Create a database with sales people listed in rows and their sales amounts in an "Adjustment" column (e.g., Harry: $2,100, Eric: $3,400, Peter: $5,400) <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.
    *   This database will be the source of the individual sales figures <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

2.  **Second Database (Total Sales):**
    *   Create a new database by typing `/` followed by `database` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
    *   Name this database "Total Sales" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Delete any default rows that are not needed <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### Establishing a Relationship Between Databases

To connect the two databases:
1.  In the *first* database, click the `+` button to add a new column <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
2.  Select `Relation` as the property type <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
3.  Choose the "Total Sales" database to create the relationship <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Configure the relationship properties:
    *   For the *first* database, name the column "Total Sales" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   For the "Total Sales" database, name the column "Sales Details" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
5.  A new column will appear in both databases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
6.  In the first database's "Total Sales" column, select the single row entry from the "Total Sales" database and copy it down to all sales data rows <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This links all sales entries to the single total sales entry <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Using the Rollup Property to Sum Values

The `Rollup` property is used to aggregate data from a related database.
1.  In the "Total Sales" database, click the `+` button to add a new property <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select `Rollup` as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
3.  Configure the Rollup:
    *   **Relation:** Select "Sales Detail" (the relationship you just established) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   **Property:** Select the "Sales Amount" column from the first database <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Initially, this will show individual values <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
    *   **Calculate:** Change the calculation to `Sum` <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
4.  This will display the total sum of all sales in the "Total Sales" database <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Rename this column to "Total Sales Rollup" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Presenting Data: Percentages and Bars

To bring the total sales value back to the first database and calculate percentages:

### Converting Rollup to a Formula

Notion does not allow rolling up a `Rollup` value directly <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. You must first convert the `Rollup` value into a `Formula` property.
1.  In the "Total Sales" database, add a new property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  Name it "Total Sales" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  Change its type to `Formula` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
4.  In the formula editor, simply link it to the "Total Sales Rollup" property: `prop("Total Sales Rollup")` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
5.  Format the number to your desired currency (e.g., Dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Rolling Up the Total Sales Formula

Now, you can roll up this formula property into your first database:
1.  In the *first* database, add another `Rollup` property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  **Relation:** Select "Total Sales" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  **Property:** Select the newly created "Total Sales" formula property from the "Total Sales" database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
4.  **Calculate:** Change the calculation to `Sum` <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
5.  This will display the overall total sales value in the first database for each row <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Rename this column "Sales (Total)" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Calculating Percentage Contribution

To see each salesperson's contribution as a percentage of total sales:
1.  In the first database, add a new `Formula` property called "Sales in Percentage" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  Enter the formula: `prop("Sales Amount") / prop("Sales (Total)")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  To round the percentage to two decimal places, modify the formula: `round(prop("Sales Amount") / prop("Sales (Total)") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
4.  Edit the property and change the number format to `Percentage` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Enhancing Presentation with Progress Bars

For a visual representation of percentages:
1.  Edit the "Sales in Percentage" property <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
2.  Select `Bar` under the "Show as" option <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This creates a clear visual bar indicating each individual sales figure's proportion of the total sales <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

[!TIP] All calculations and presentations automatically update if any sales values are changed <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

This method allows for dynamic and insightful data presentation within Notion databases, which is crucial for [[dashboard_presentation_in_notion | dashboard presentation in Notion]] and [[customizing_notion_templates_for_business_needs | customizing Notion templates for business needs]] <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.