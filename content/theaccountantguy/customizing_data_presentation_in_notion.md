---
title: Customizing data presentation in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 
This article details how to calculate and present the sum of a column in Notion, along with steps to customize its display for better data visualization.

## Calculating and Presenting Column Sums in Notion

Notion allows for robust data management, including summing values from a column and presenting this data in a customized format. This process involves creating database relationships, using rollup properties, and applying formulas for advanced calculations and visual enhancements <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

### Setting Up Databases

To begin, you will need at least two databases to establish a relationship for calculations:
1.  **Main Database:** Contains individual data entries (e.g., sales people with their respective sales amounts) <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.
2.  **Summary Database:** A new, separate database (e.g., named "Total Sales") that will hold the aggregated sum <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. You can create this by typing `/database` and selecting "database" <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Establishing Database Relationships

To link your main database to the summary database:
1.  In your main database, add a new property by clicking the `+` button <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  Select "Relation" as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  Choose your summary database (e.g., "Total Sales") to create the relationship <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
4.  Define the column names for both databases (e.g., "Total Sales" in the main database and "Sales Details" in the "Total Sales" database) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
5.  Populate the newly created relation column in your main database by selecting the corresponding entry from the summary database (e.g., "Total Sales") for all relevant rows <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This links all sales entries to the single "Total Sales" record <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Calculating the Sum with Rollup

In your summary database ("Total Sales"):
1.  Add a new property and select "Rollup" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
2.  In the rollup settings, select the relationship you just established (e.g., "Sales Detail") <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
3.  Choose the property from the main database you want to sum (e.g., "Sales value") <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
4.  Under "Calculate," select "Sum" to aggregate all values <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Name this column (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### Transferring the Sum Back to the Main Database

A direct rollup of a rollup value is not possible <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. To transfer the calculated sum back to your main database for further use (e.g., percentage calculations):
1.  **Create a Formula Property in the Summary Database:** Add a new property in your "Total Sales" database, choose "Formula" type, and set its formula to simply reference your "Total Sales Rollup" property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This converts the rollup value into a formula property <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   You can also [[currency_customization_in_notion_dashboards | customize currency]] and other formats for this formula property as needed <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
2.  **Create a Rollup Property in the Main Database:** In your main database, add another "Rollup" property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Select the "Total Sales" relationship <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> and then choose the *formula* property (e.g., "Total Sales") from the summary database <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. Again, set the "Calculate" option to "Sum" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This will display the total sales sum in your main database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

### [[Customizing data presentation in Notion | Customizing Data Presentation]]

Once the sum is available in your main database, you can use it for various [[Customizing Notion templates | customizations]] and calculations:

*   **Percentage Calculation:** Create a new "Formula" property (e.g., "Sales in percentage") in your main database <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Divide the individual sales amount by the total sales sum: `Sales / Sales Total` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Rounding Decimals:** To round the percentage to two decimal places, modify the formula using the `round` function: `round(prop("Sales") / prop("Sales (Total)") * 100) / 100` <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Formatting as Percentage:** Edit the property and change the "Number format" to "Percentage" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Visualizing with Progress Bars:** Further [[Customizing Notion templates for business needs | customize]] the percentage column by selecting "Bar" under the "Show as" option in the property settings <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This provides a visual representation of each individual sale's contribution to the total <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

All these calculations and visualizations automatically update when the underlying sales values change <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This method can be utilized for various analytical purposes and for creating comprehensive dashboards in Notion <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.