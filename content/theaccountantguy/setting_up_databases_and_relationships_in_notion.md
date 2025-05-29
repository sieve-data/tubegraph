---
title: Setting up databases and relationships in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to establish relationships between databases in Notion to perform calculations and create dynamic reports, such as calculating the sum of a column or individual contributions as a percentage of a total.

## Creating a New Database

To begin, you will [[how_to_create_a_database_in_notion | create a new database]] in Notion <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
1.  Type `/` followed by `database` to create a new database <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  Name the database (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Delete any default rows if not needed <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Establishing Relationships Between Databases

To perform calculations across different datasets, you need to [[establishing_links_and_relationships_between_databases_in_notion | create a relationship]] between your primary database (e.g., "Sales People" with individual sales amounts) and your secondary database (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Adding a Relation Property

1.  In one of the databases, click the `+` button to add a new column <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  Select "Relation" as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  Choose the database you want to link to (e.g., "Sales" for the "Total Sales" database, or vice versa) <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### Configuring Relation Names

When creating the relationship, Notion will prompt you to define how the relation columns will appear in both databases <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   For the first database, you might name it "Total Sales" <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   For the second database, you might name it "Sales Details" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
This creates a new column in both databases reflecting the relationship <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Populating Related Entries

In your primary database (e.g., "Sales People"), click on the newly created relation column (e.g., "Total Sales") and select the entry from the linked database (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Copy this entry down to all relevant rows to link each sales person's data to the "Total Sales" database <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This will automatically populate the related entries in the second database <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Aggregating Data with Rollup

In the secondary database (e.g., "Total Sales"), you can use a "Rollup" property to aggregate information from the linked primary database <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Setting up the Rollup Property

1.  Click the `+` button to add a new column <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
3.  Choose the relationship you just established (e.g., "Sales Detail") <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
4.  Select the property you want to aggregate (e.g., "Sales value") <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Calculating the Sum

By default, the rollup might show individual values <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
1.  Click on the Rollup property.
2.  Under "Calculate," select "Sum" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
This will display the total sum of the sales amounts <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. You can name this column "Total Sales (Rollup)" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## Transferring Aggregated Data (Rollup via Formula)

A direct rollup of an aggregated number value from one database to another is not possible <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. First, the rollup value needs to be converted into a formula property <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### The Need for a Formula Property

If you try to roll up a number that is already a rollup calculation from another database, it won't be visible as a selectable property <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### Creating the Formula Property

1.  In the secondary database (e.g., "Total Sales"), add a new property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  Name it (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  Change the property type to "Formula" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
4.  In the formula editor, simply reference the "Total Sales (Rollup)" property <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. This effectively copies the rollup value into a formula property <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
5.  You can also format the currency for this property <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Rolling Up the Formula Value

Now, back in the primary database (e.g., "Sales People"):
1.  Add another Rollup property <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
2.  Select the relationship linked to your "Total Sales" database <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
3.  Select the "Total Sales" formula property you just created <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
4.  Set the calculation to "Sum" (though it will display the single value as it's already a sum) <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
This brings the grand total sales value from the second database back into the first database for each row <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. You can name this column "Sales (Total)" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Performing Further Calculations (e.g., Percentage)

Once the total sales value is available in your primary database, you can use it for further calculations.

### Setting up a Percentage Formula

1.  Add a new "Formula" property (e.g., "Sales in Percentage") <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
2.  Divide the individual "Sales" amount by the "Sales (Total)" amount <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
    *   Example Formula: `prop("Sales") / prop("Sales (Total)")`

### Formatting the Percentage

To format the percentage with two decimal places:
1.  Wrap the division in a `round` function and multiply by 100, then divide by 100 <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
    *   Example Formula: `round(prop("Sales") / prop("Sales (Total)") * 100) / 100` <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
2.  Edit the property and change the "Number format" to "Percentage" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Visualizing with a Progress Bar

For a visual representation:
1.  Edit the percentage formula property <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
2.  Select "Bar" as the display option <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
This provides a visual bar showing each individual's sales contribution relative to the total <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

Any changes to individual sales values will automatically update the total sales and percentage calculations across the linked databases <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This method allows you to effectively [[creating_and_using_databases_in_notion | create and use databases in Notion]] for complex calculations.