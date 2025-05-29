---
title: Using formulas to calculate differences in Notion
videoId: Fz_fpiT29EE
---

From: [[theaccountantguy]] <br/> 

When working with numerical data in Notion databases, it is possible to find the difference between two numbers using [[using_formulas_in_notion | formulas]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This can be achieved through two distinct methods: utilizing the `subtract` operator or employing the standard [[subtracting_numbers_in_notion | minus sign]] (`-`) <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Database Setup

To begin, create a new database in Notion by typing `/database` and selecting from the available options <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

1.  **Title Property**: The first property in the database will be the title property, which indicates the purpose of the calculation <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
2.  **Number Properties**: Assign "Number" properties to two different columns where the numbers for subtraction will be entered <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Methods for Calculating Differences

Once the numbers are in the database, a [[using_formulas_in_notion | formula]] property can be added to calculate the difference.

### 1. Using the `subtract` Operator

The `subtract` operator is a dedicated function for finding the difference between two numerical inputs <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

*   It takes two numbers as input <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   For example, if you have `Number 1` and `Number 2` as properties, the [[using_formulas_in_notion | formula]] would look something like `subtract(prop("Number 1"), prop("Number 2"))` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### 2. Using the Minus Sign (`-`)

Alternatively, the standard [[subtracting_numbers_in_notion | minus sign]] can be used to achieve the same result <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

*   This method is more akin to traditional arithmetic operations.
*   Using the previous example, the [[using_formulas_in_notion | formula]] would be `prop("Number 1") - prop("Number 2")` <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Both methods will yield the difference between the two numbers in your Notion database <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.