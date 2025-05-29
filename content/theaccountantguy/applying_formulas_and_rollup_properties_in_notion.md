---
title: Applying formulas and rollup properties in Notion
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

Notion offers powerful features like [[using_rollup_and_formula_properties_in_notion | rollup and formula properties]] that enable users to track and summarize information across connected databases <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. These properties allow for advanced [[using_notion_for_calculations | calculations]] and dynamic data presentation, helping to create comprehensive dashboards <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Rollup Properties

A [[using_rollup_and_formula_properties_in_notion | rollup property]] is a Notion feature that allows you to derive information from one database onto another, provided the two databases are linked <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. It acts as a bridge, picking up specific data from a "primary" database and displaying it in a "secondary" one <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

### How to Use Rollup Properties

To implement a rollup property, you must first establish a "relation" property between the two databases you wish to connect <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This relation acts as the linking mechanism <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

1.  **Add a New Property**: In the database where you want the rolled-up information to appear, click the `+` icon to add a new property <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
2.  **Select "Rollup" Type**: Choose "Rollup" from the list of property types <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
3.  **Choose a Relationship**: Select the established relation property that links to your desired source database <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. For example, if you have a "Person database" and an "Events database" linked by a "Person" relation, you would select the "Person" relation in the Events database to roll up information about the person <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.
4.  **Select a Property**: Choose the specific property from the related database whose information you want to derive <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
5.  **Choose a Calculation**: In the "Calculate" option, select how you want the data to be aggregated <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>:
    *   `Count values`: Counts the total number of entries linked to the record <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>. For instance, counting the number of events associated with each person <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.
    *   `Count checked`: Specifically counts checkboxes that are ticked <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>. This is useful for tracking completed tasks or attended events <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.

### Example: Event Tracking

In a "Relationship Tracker" dashboard, a rollup property can count the total number of events outlined for each person <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. Another rollup can track how many events have been attended by only counting the checked attendance boxes <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

## Formula Properties

[[using_formulas_in_notion | Formula properties]] in Notion allow you to perform [[using_excellike_formulas_in_notion | Excel-like calculations]] and manipulate data dynamically <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. They can leverage data from other properties, including rollup properties, to generate new insights <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.

### Key Formula Functions

*   **`style()` Function**: This unique Notion function allows for formatting text within a formula <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. You can apply bolding <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>, colors (e.g., blue, green) <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>, and even background colors <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a> to text based on conditions or values.
*   **Conditional Logic (`if` statements)**: Formulas can use `if` conditions to display different text or values based on whether a condition is met <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. For instance, to display "event" for a single event and "events" for multiple events, you can use an `if` condition to check the number of events <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. This helps in maintaining correct grammar for singular and plural terms <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.
*   **[[using_formulas_to_add_numbers_in_notion | Numerical Operations]] and Percentage Calculation**: [[different_methods_to_calculate_sums_in_notion | Formulas]] can perform arithmetic operations like division and multiplication <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>. To calculate a percentage, you would divide the "events attended" rollup by the "number of events" rollup and multiply by 100 <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>.
*   **`round()` Function**: To ensure precise percentage display, the `round()` function can be used to round the calculated value to a specified number of decimal places <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.
*   **Visual Representation**: Beyond just numbers, [[calculating_the_sum_of_a_column_in_notion | formula properties]] can visually represent percentages as a bar or ring <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>, providing an instant visual illustration of progress <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>.

### Example: Attendance Percentage

Building on the event tracking example, a formula property named "Attendance Percentage" can divide the "events attended" rollup value by the "number of events" rollup value, then format it as a percentage bar <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. This allows for [[managing_sales_data_with_formulas_in_notion | managing sales data with formulas in Notion]] or any other data where progress needs to be visualized <a class="yt-timestamp" data-t="00:28:59">[00:28:59]</a>.

For instance, if you uncheck an attendance box for an event, the percentage will dynamically update (e.g., from 100% to 50% if one of two events was unselected) <a class="yt-timestamp" data-t="00:46:37">[00:46:37]</a>. This dynamic update is a core benefit of using [[using_formulas_to_subtract_in_notion | formulas]] in Notion.