---
title: Creating a database in Notion for calculations
videoId: 13jgGp1PbPo
---

From: [[theaccountantguy]] <br/> 

This guide explains how to set up a Notion [[creating_a_database_in_notion | database]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a> to calculate the product of two numbers using two different formulas <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Database Structure <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>

To begin, [[creating_a_database_in_notion | create a database]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> with the following properties:

*   **Name of the Operator**: A `Title` property <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Number 1**: A `Number` property <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   **Number 2**: Another `Number` property <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   **Product (Method 1)**: A `Formula` property.
*   **Product (Method 2)**: Another `Formula` property.

## Calculation Methods

The product of the two numbers can be calculated using two distinct formula methods within Notion.

### Method 1: Using the `multiply()` Operator Formula

This method utilizes Notion's built-in `multiply()` operator <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

1.  Add a new `Formula` property to your [[setting_up_databases_in_notion | database]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.
2.  In the formula editor, input the two number properties as arguments for the `multiply()` function <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
    *   **Example Formula**: `multiply(prop("Number 1"), prop("Number 2"))`
3.  When "Number 1" is `2` and "Number 2" is `3`, the formula will output `6` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Method 2: Using the Multiplication Symbol (`*`)

This method uses the standard multiplication symbol (`*`) directly in the formula <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

1.  Add another `Formula` property to your Notion [[setting_up_databases_in_notion | database]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.
2.  In the formula editor, place the multiplication symbol between the two number properties <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
    *   **Example Formula**: `prop("Number 1") * prop("Number 2")`
3.  This formula achieves the same result as the `multiply()` operator <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

By setting up these formulas, you can effectively calculate the product of two numbers directly within your Notion [[setting_up_databases_in_notion | database]] <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.