---
title: Calculating the sum of a column in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

This article outlines a method to calculate the [[different_methods_to_calculate_sums_in_notion | sum]] of a column in [[using_notion_for_calculations | Notion]] using a combination of relationship and [[applying_formulas_and_rollup_properties_in_notion | rollup properties]], along with [[using_formulas_in_notion | formulas]] <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Scenario Setup <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>

Consider a database containing a list of sales people in different rows <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Each person has a corresponding sales amount in an "adjustment" column <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. For example, Harry has $2,100, Eric has $3,400, and Peter has $5,400 <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The goal is to display the [[different_methods_to_calculate_sums_in_notion | sum]] of all these amounts ($10,900) in an adjacent column <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Steps to Calculate Sum

### 1. Create a Second Database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>

Start by creating a new database <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   Type `/` followed by `database` to create a new database <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   Name this database "Total Sales" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   Delete any default extra rows <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### 2. Establish a Relationship Between Databases <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

Create a relationship property to link your initial sales database with the "Total Sales" database <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   In the first database, click the `+` button to add a new property <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   Select `Relation` as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Choose the "Total Sales" database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   Configure the relationship:
    *   In the first database, name the column "Total Sales" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   In the "Total Sales" database, name the corresponding column "Sales Details" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   A new column will appear in both databases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   In the first database, in the "Total Sales" column, select the "Total Sales" entry for all sales people <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This will link all entries to the single "Total Sales" row in the second database <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### 3. Rollup Sales Values in the Second Database <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>

Now, use a [[applying_formulas_and_rollup_properties_in_notion | rollup property]] in the "Total Sales" database to gather the sales amounts.
*   In the "Total Sales" database, click the `+` button <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Select `Rollup` as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   Configure the rollup:
    *   **Relationship:** Select "Sales Details" (the relationship you just established) <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   **Property:** Select the "Sales" column from the original database <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   **Calculate:** Change the calculation from "Original Value" to `Sum` <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   This will display the total [[different_methods_to_calculate_sums_in_notion | sum]] of all sales values <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Name this column "Total Sales Rollup" <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### 4. Display Sum in the First Database (Via Formula) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>

To bring this total [[different_methods_to_calculate_sums_in_notion | sum]] back to the first database, you cannot directly rollup a rollup property <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. You must first convert the rollup value into a [[using_formulas_in_notion | formula]] property.

*   **Create a Formula Property:**
    *   In the "Total Sales" database, add a new property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   Name it "Total Sales" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Change the property type to `Formula` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   In the formula editor, simply reference the "Total Sales Rollup" property: `prop("Total Sales Rollup")` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   Set the number format to `Dollars` (or your preferred currency) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

*   **Rollup the Formula Property to the First Database:**
    *   In the first database, add another [[applying_formulas_and_rollup_properties_in_notion | rollup property]] <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   **Relationship:** Select "Total Sales" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   **Property:** Select the newly created "Total Sales" *formula* property from the second database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   **Calculate:** Change the calculation to `Sum` <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   The total sales value will now appear in your primary sales database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Name this column "Sales (Total)" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Bonus: Percentage Calculation and Display <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

You can extend this setup to calculate each salesperson's contribution as a [[displaying_percentage_calculations_in_notion | percentage of total sales]].

*   Add a new `Formula` property in the first database, named "Sales in Percentage" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   Use the following [[using_formulas_in_notion | formula]] to divide individual sales by the total sales: `prop("Sales") / prop("Sales (Total)")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   To format this as a percentage with two decimal places and a bar:
    *   Wrap the division in a `round` function and multiply by 100, then divide by 100: `round(prop("Sales") / prop("Sales (Total)") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. This ensures two decimal places <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
    *   Click `Edit property` for the "Sales in Percentage" column <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   Change the number format to `Percentage` <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   Optionally, select `Bar` under `Show as` for a visual representation <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Any changes to individual sales values will automatically update the total sales and percentage calculations <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.