---
title: Using rollup and relation properties in Notion
videoId: C9gr5yS8EPc
---

From: [[theaccountantguy]] <br/> 

Notion's powerful database features include [[properties_in_notion_databases | properties]] like "Relation" and "Roll-up" which are crucial for creating interconnected and analytical workspaces, such as a minimalistic budget planner <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>. These properties allow users to link different databases and aggregate data from those linked databases, providing deeper insights and streamlined data management <a class="yt-timestamp" data-t="04:48:06">[04:48:06]</a>.

## Relation Property
The Relation property is used to establish a link between two separate Notion databases <a class="yt-timestamp" data-t="04:40:40">[04:40:40]</a>. This connection enables a database to "know about" entries in another database, allowing for cross-referencing and more complex data structures <a class="yt-timestamp" data-t="04:48:06">[04:48:06]</a>.

### How it's Used
When setting up a Relation property, you link it to another existing database <a class="yt-timestamp" data-t="04:42:01">[04:42:01]</a>. This often involves linking databases "both ways," meaning each database is aware of its connection to the other <a class="yt-timestamp" data-t="08:36:19">[08:36:19]</a>. This bidirectional linking is essential for the Roll-up property to function effectively <a class="yt-timestamp" data-t="08:36:19">[08:36:19]</a>.

### Examples of Relation Property Use
*   **Income Details Database**:
    *   The `Source of Income` column, `Month of Income` column, and `Frequency of Income` column all utilize a Relation property to link to separate databases (e.g., `Income Type database`, `Month of Income database`, `Frequency of Income database`) <a class="yt-timestamp" data-t="04:40:40">[04:40:40]</a><a class="yt-timestamp" data-t="05:01:21">[05:01:21]</a><a class="yt-timestamp" data-t="05:10:48">[05:10:48]</a>. This allows for detailed analysis based on these categories <a class="yt-timestamp" data-t="04:48:06">[04:48:06]</a>.
*   **Expense Details Database**:
    *   The `Month of Expense`, `Expense Classification`, and `Expense Type` columns are linked to other databases via Relation properties <a class="yt-timestamp" data-t="17:26:40">[17:26:40]</a><a class="yt-timestamp" data-t="17:49:09">[17:49:09]</a><a class="yt-timestamp" data-t="17:56:47">[17:56:47]</a>.

## Roll-up Property
The Roll-up property works in conjunction with a Relation property. Once a relation is established between two databases, the Roll-up property allows you to pull specific information from the related database and perform calculations or aggregations on that data <a class="yt-timestamp" data-t="07:30:04">[07:30:04]</a><a class="yt-timestamp" data-t="09:22:31">[09:22:31]</a>.

### How it's Used
1.  **Specify Relation**: First, you select the Relation property that links to the desired database <a class="yt-timestamp" data-t="08:41:22">[08:41:22]</a>.
2.  **Select Property**: Next, you choose the specific [[properties_in_notion_databases | property]] from the related database that you want to "roll up" <a class="yt-timestamp" data-t="08:43:40">[08:43:40]</a>.
3.  **Choose Calculation**: Finally, you select a calculation (e.g., sum, average, count, show original) to perform on the pulled data <a class="yt-timestamp" data-t="08:49:10">[08:49:10]</a>. The "sum" calculation is frequently used to add up numerical values from related entries <a class="yt-timestamp" data-t="08:49:10">[08:49:10]</a><a class="yt-timestamp" data-t="10:39:15">[10:39:15]</a>.

### Examples of Roll-up Property Use
*   **Aggregating Income Data**:
    *   To calculate the total actual income or expected income for a specific income source (e.g., salary, side hustle), a Roll-up property is used <a class="yt-timestamp" data-t="07:46:17">[07:46:17]</a>. It pulls the "Actual Income" or "Expected Income" values from the main income details database via the "Source of Income" relation and sums them up <a class="yt-timestamp" data-t="08:43:40">[08:43:40]</a><a class="yt-timestamp" data-t="09:02:18">[09:02:18]</a>.
    *   Similarly, for monthly income overviews, Roll-up properties calculate the total expected and actual income for each month by rolling up values from the main income database via the "Month of Income" relation <a class="yt-timestamp" data-t="10:04:15">[10:04:15]</a><a class="yt-timestamp" data-t="10:22:23">[10:22:23]</a>.
    *   For frequency of income (recurring vs. one-time), Roll-up properties aggregate total actual and expected income based on the "Frequency of Income" relation <a class="yt-timestamp" data-t="11:44:26">[11:44:26]</a>.
*   **Calculating Variances**: Roll-ups help determine total estimated income, total actual income, and their differences, which can then be used in [[using_formulas_in_notion | formulas]] to calculate percentage changes <a class="yt-timestamp" data-t="13:14:14">[13:14:14]</a>.
*   **Fund Allocation Overview**:
    *   In the fund allocation overview, the total actual income is calculated using a Roll-up property that draws the value from the `Month of Income database` <a class="yt-timestamp" data-t="22:55:04">[22:55:04]</a>.
    *   The total actual expense is similarly rolled up from the `Month of Expense database` <a class="yt-timestamp" data-t="23:06:05">[23:06:05]</a>.

By combining Relation and Roll-up properties, users can build dynamic and interconnected Notion databases that automatically aggregate and analyze data, making complex tracking (like budget planning) more efficient and insightful <a class="yt-timestamp" data-t="04:48:06">[04:48:06]</a><a class="yt-timestamp" data-t="07:30:04">[07:30:04]</a>.