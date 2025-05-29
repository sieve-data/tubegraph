---
title: Calculating the sum of a column in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

Calculating the sum of a numerical column in a Notion database, such as total sales, can be achieved using a combination of database relations, rollups, and formulas <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Example Scenario: Sales Database
Consider a database listing sales people with their respective sales amounts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. For instance:
*   Harry: $2,100 <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   Eric: $3,400 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Peter: $5,400 <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>

The goal is to calculate the total sum of these sales, which is $10,900, and display it within the original database <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Step-by-Step Guide to Summing a Column

### 1. Create a Secondary Database
First, create a new, separate database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   Type `/database` to create a new database <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   Name this database (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   Delete any default extra rows, leaving only one main entry for the total <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### 2. Establish a Relation Between Databases
A [[notion_relations_explained | relation]] property links entries between two databases <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   In your *first* database (e.g., "Sales People"), add a new column by clicking the `+` button <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   Select "Relation" as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Choose your newly created "Total Sales" database to link to <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   Define how the relation columns will be named in both databases (e.g., "Total Sales" in the first database and "Sales Details" in the "Total Sales" database) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   In the "Total Sales" column of the *first* database, click on each cell and select the entry from your "Total Sales" database <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Copy this down to all rows <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This step links all sales entries to the single total sales entry in the secondary database <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### 3. Roll Up Sales Values in the Secondary Database
A [[notion_rollup_property | rollup]] property allows you to pull and aggregate data from related entries <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   In the "Total Sales" database, add a new column <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Configure the rollup:
    *   For "Relation," select "Sales Details" (the relation you just created) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   For "Property," choose the "Sales" column from your *first* database <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This brings all the individual sales amounts into this rollup property <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   Under "Calculate," select "Sum" to get the total of all the rolled-up sales values <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Name this column (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### 4. Convert Rollup to a Formula Property
To enable rolling up the summed value back to the first database, the rollup property needs to be converted into a [[using_formulas_in_notion | formula]] property <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   In the "Total Sales" database, add another new column <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   Name it (e.g., "Total Sales") and change its type to "Formula" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   In the formula editor, simply reference your "Total Sales Rollup" property: `prop("Total Sales Rollup")` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   You can set the number format to currency (e.g., Dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### 5. Roll Up the Total Sales Value Back to the First Database
Now you can bring the calculated total sum back to your original "Sales People" database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   In your *first* database ("Sales People"), add a new column <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   Configure this new rollup:
    *   For "Relation," select "Total Sales" (the relation linking to your secondary database) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   For "Property," select the "Total Sales" *formula* property from the second database <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
    *   Under "Calculate," select "Sum" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   Name this column (e.g., "Sales Total") <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Now, the total sum of the sales column will be displayed in this new column in your main database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Any changes to individual sales amounts will automatically update the total sales value <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## Additional Calculations: Percentage of Total Sales
You can further use this total sales value for more calculations, such as determining each salesperson's contribution as a percentage of the total <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   Add a new column in your first database <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   Select "Formula" as the property type <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   Enter the following [[using_excellike_formulas_in_notion | formula]]:
    ```notion
    round(prop("Sales") / prop("Sales Total") * 100) / 100
    ```
    This [[implementing_excellike_formulas_in_notion | formula]] divides individual sales by the total sales, multiplies by 100, rounds to two decimal places, and then divides by 100 again to get the correct percentage value <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   Change the number format of this formula property to "Percentage" <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   Optionally, you can display this percentage as a bar by selecting "Bar" under the "Show as" option in the property settings <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This provides a visual representation of each salesperson's contribution <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

<br>
> [!NOTE] Other Mathematical Operations
> Notion's rollup and formula properties can be used for a variety of other calculations beyond summing, such as [[calculating_product_of_numbers_in_notion | calculating products]], [[adding_numbers_in_notion | adding numbers]], or even [[how_to_calculate_average_in_notion_using_external_tools | calculating averages]] and applying [[applying_formula_for_multiplication_in_notion | multiplication formulas]]. The key is understanding how to leverage relations, rollups, and the extensive range of [[formulas_in_notion | formulas in Notion]].
> While the "Sum" option is readily available for rollups of numerical properties, the [[sum_function_in_notion | SUM function]] specifically refers to how the rollup aggregates values from the related database.

By following these steps, you can effectively calculate and display the sum of a column in Notion, along with derived metrics like percentages <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.