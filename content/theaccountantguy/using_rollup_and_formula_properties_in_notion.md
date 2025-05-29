---
title: Using rollup and formula properties in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

To calculate the sum of a column and perform further calculations like percentages within Notion, you can leverage a combination of rollup and formula properties across two interconnected databases <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Scenario Setup

Imagine a database listing sales people and their respective sales amounts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. For example:
*   Harry: $2,100 <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
*   Eric: $3,400 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Peter: $5,400 <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
The goal is to calculate the total sum of these amounts ($10,900) <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a> and potentially calculate individual sales as a percentage of this total <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Step-by-Step Implementation

### 1. Create a Second Database

Begin by creating a new database for the aggregate data.
*   Type `/database` to create a new database <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   Name it "total sales" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Delete any default rows in this new database <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### 2. Establish a Relation Property

A relation property links entries between two databases.
*   In your *first* database (e.g., "Sales People"), click the "plus" button to add a new property <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   Select "Relation" as the property type <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   Choose the "total sales" database to create the relationship <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   Configure the property names for clarity:
    *   In the *first* database, name it "total sales" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   In the "total sales" database, name it "sales details" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   Once created, a new column will appear in both databases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   In the first database, link all entries (sales people) to the single entry in the "total sales" database by selecting "total sales" in the new column for each row <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This will populate the "sales details" column in the second database with all linked sales people <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### 3. Calculate Sum using Rollup Property

Now, use a rollup property in the "total sales" database to aggregate the sales data.
*   In the *second* database ("total sales"), add a new property <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   In the rollup settings:
    *   Choose "sales detail" as the relation <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   Select the "sales" property to roll up <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Under "Calculate," choose "Sum" to get the total <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Name this property "total sales R" (Rollup) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This property now displays the sum of all sales from the first database <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### 4. Convert Rollup to Formula Property

A direct rollup of a numerical value from another database cannot be rolled up *back* to the original database for calculations <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. To overcome this, convert the rollup value into a [[formulas_in_notion | formula]] property.
*   In the *second* database ("total sales"), add another new property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   Name it "Total Sales" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   Set its type to "Formula" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   The [[creating_and_saving_custom_formulas_in_notion | formula]] is simply `prop("total sales R")` to link it to the rollup value <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   Optionally, change the number format to "Dollars" or your preferred currency <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### 5. Rollup Total Sales Back to the First Database

Now you can bring the total sales value back to your main database.
*   In the *first* database (e.g., "Sales People"), add a new "Rollup" property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Select "total sales" as the relationship <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   Choose the newly created "Total Sales" formula property to roll up <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   Set the "Calculate" option to "Sum" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   Name this property "Sales (Total)" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   This column will now display the grand total sales value in each row of your main database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

### 6. Calculate Sales Percentage

With individual sales and the total sales in the same database, you can calculate percentages using another [[formulas_in_notion | formula]] property.
*   In the *first* database, add a new "Formula" property <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   Name it "Sales in percentage" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   The basic [[applying_formula_for_multiplication_in_notion | formula]] to divide individual sales by total sales is `prop("Sales") / prop("Sales (Total)")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### 7. Format the Percentage

To present the percentage cleanly:
*   **Round to two decimal places:** Use the `round()` function and multiply/divide by 100 within the [[using_excellike_formulas_in_notion | formula]]:
    `round(prop("Sales") / prop("Sales (Total)") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>
*   **Change number format to Percentage:** Click on the property header, select "Edit property," and change "Number format" to "Percentage" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Add a progress bar (optional):** In the "Edit property" settings, under "Show as," select "Bar" for a visual representation <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Any changes to individual sales amounts will automatically update the total sales and percentage calculations across both databases <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This method allows for complex calculations and dashboards within Notion <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.