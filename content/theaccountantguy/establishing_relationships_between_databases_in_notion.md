---
title: Establishing relationships between databases in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

[[connecting_relational_databases_with_notion_api | Connecting relational databases]] in Notion allows for advanced calculations and reporting, such as summing values from one [[creating_a_database_in_notion | database]] and displaying them in another <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This article outlines how to establish these relationships and perform calculations like total sales and sales percentages.

## Calculating the Sum of a Column

To calculate the sum of a column, like total sales, across multiple entries in a [[creating_a_database_in_notion | Notion database]], you can utilize two [[linking_databases_and_creating_templates_in_notion | linked databases]] and the "Rollup" property <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Step-by-Step Guide

#### 1. Set Up Initial Databases

First, [[creating_a_database_in_notion | create a database]] with sales people and their corresponding sales amounts <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.
Next, [[creating_a_database_in_notion | create a second database]] for tracking total sales <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. For example, name it "Total Sales" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

#### 2. Create a Relationship Property

In your primary sales database, add a new property by clicking the plus button <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
Select "Relation" as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
Choose the "Total Sales" [[creating_a_database_in_notion | database]] to establish the relationship <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
Configure the relationship properties: for the main database, name it "Total Sales," and for the "Total Sales" database, name it "Sales Details" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This action creates a new column in both databases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
In the primary sales database, for each sales person, select the corresponding entry (e.g., "Total Sales") in the new relation column <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Copy this down to all entries to link them to the "Total Sales" database <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This will automatically feed all sales information into the "Total Sales" database <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

#### 3. Use a Rollup Property for Summation

In the "Total Sales" database, add a new property <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
Configure the rollup:
*   **Relationship**: Select the "Sales Details" relationship property you just created <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Property**: Choose the "Sales" property from the primary database <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This brings the sales values from the first database into the second <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Calculate**: Change the calculation method from "Original Values" to "Sum" to get the total <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

Rename this rollup property, for example, "Total Sales Rollup" <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

#### 4. Display Total Sales in the Primary Database

To display this total sales value back in the original database, an additional step is required because you cannot directly roll up a rollup value <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

1.  **Convert Rollup to Formula**: In the "Total Sales" database, create a new property called "Total Sales" and set its type to "Formula" <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. The formula should simply reference your "Total Sales Rollup" property (e.g., `prop("Total Sales Rollup")`) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. You can also format this as currency <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
2.  **Rollup the Formula**: Go back to your primary sales database. Add another "Rollup" property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   **Relationship**: Select "Total Sales" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   **Property**: Now you will be able to select the new "Total Sales" formula property from the "Total Sales" database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   **Calculate**: Set the calculation to "Sum" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    This will display the overall total sales in your primary database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

#### 5. Calculate Sales Percentage and Visualize

To calculate each sales person's contribution as a percentage of total sales:

1.  **Create Formula Property**: In the primary sales database, add a new "Formula" property, e.g., "Sales in Percentage" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  **Percentage Formula**: Divide the individual sales by the total sales (e.g., `prop("Sales") / prop("Sales Total")`) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  **Format Decimals**: To show two decimal places, wrap the formula: `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
4.  **Display as Percentage**: Edit the property and change the "Number Format" to "Percentage" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
5.  **Add Progress Bar**: Further customize the property by selecting "Bar" for a visual representation of the percentage <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

> [!INFO] Dynamic Updates
> All calculations, including total sales and percentages, will automatically update whenever the individual sales values are changed <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

This method of [[linking_notion_databases_for_automated_workflows | linking Notion databases]] and using rollup properties can be applied for various calculations and for [[setting_up_databases_and_dashboards_in_notion | creating dashboards]] for business or individual use cases <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.