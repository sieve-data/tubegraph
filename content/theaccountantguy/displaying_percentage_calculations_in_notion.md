---
title: Displaying percentage calculations in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

To display percentage calculations in Notion, you first need to establish relationships between databases and use rollup properties to gather necessary sum totals. This allows you to then create a formula that calculates individual percentages relative to a total, which can then be formatted and visualized.

## Prerequisites: Calculating Total Sales

Before calculating percentages, you need a database with individual sales figures and a separate mechanism to [[calculating_the_sum_of_a_column_in_notion | calculate the sum of a column in Notion]]. This typically involves setting up two databases and [[applying_formulas_and_rollup_properties_in_notion | applying formulas and rollup properties in Notion]].

1.  **Initial Sales Database**: Create a database listing sales people and their respective sales amounts (e.g., Harry: $2,100, Eric: $3,400, Peter: $5,400) <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.
2.  **Total Sales Database**: Create a new database, for instance, named "Total Sales" <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Delete any default rows and columns <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
3.  **Create a Relation**:
    *   Add a "Relation" property to the "Total Sales" database, linking it to your initial sales database (e.g., "Sales Details") <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   In the initial sales database, add a "Relation" property linking to the "Total Sales" database (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
    *   In the initial sales database, select the "Total Sales" entry in the new relation column and copy it down to all sales entries. This links all individual sales to the single "Total Sales" entry <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
4.  **Rollup Sales Data**:
    *   In the "Total Sales" database, add a "Rollup" property <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
    *   Configure the rollup to use the "Sales Details" relationship and roll up the "Sales" value <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   Under "Calculate", select "Sum" to get the total of all sales <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Name this property (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
5.  **Convert Rollup to Formula for Visibility**:
    *   A rollup value cannot be directly rolled up to another database. To overcome this, create a new "Formula" property in the "Total Sales" database <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   Set the formula to simply refer to the "Total Sales Rollup" property (e.g., `prop("Total Sales Rollup")`) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. This converts the rollup value into a formula property <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   Format it as desired, e.g., to "Dollars" <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
6.  **Rollup Total Sales onto Initial Database**:
    *   In your initial sales database, add another "Rollup" property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Select the "Total Sales" relationship and roll up the newly created "Total Sales (Formula)" property from the "Total Sales" database <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
    *   Set the calculation to "Sum" <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This will display the total sales value in each row of your main sales database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

## Calculating Percentages

Once you have the individual sales amounts and the total sales amount in the same database, you can calculate percentages.

1.  **Create a Percentage Formula Property**:
    *   Add a new "Formula" property to your initial sales database, naming it something like "Sales in Percentage" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  **Input the Division Formula**:
    *   In the formula editor, divide the "Sales" property by the "Sales Total" property (the rollup created in the previous step): `prop("Sales") / prop("Sales Total")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  **Format for Two Decimal Places**:
    *   To control decimal places, use the `round` function. Multiply the result by 100, round it, and then divide by 100: `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
4.  **Change Number Format to Percentage**:
    *   Click on the property, select "Edit property", then "Number format", and choose "Percentage" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This will convert the decimal values (e.g., 0.19) into percentages (e.g., 19%) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
5.  **Customize with a Progress Bar (Optional)**:
    *   For a visual representation, click "Edit property" again and select "Bar" under the "Show as" option <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. This creates a progress bar showing each individual sale's proportion of the total sales <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

## Dynamic Updates

Any changes made to the individual sales values in your initial database will automatically update the total sales and the percentage calculations and their visualizations in real-time <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This process demonstrates how to [[using_notion_for_calculations | use Notion for calculations]] and [[using_formulas_in_notion | using formulas in Notion]] to create dynamic data presentations, similar to [[using_excellike_formulas_in_notion | using Excel-like formulas in Notion]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This method is one of [[different_methods_to_calculate_sums_in_notion | different methods to calculate sums in Notion]] and is key for [[creating_visual_presentations_of_data_in_notion | creating visual presentations of data in Notion]].