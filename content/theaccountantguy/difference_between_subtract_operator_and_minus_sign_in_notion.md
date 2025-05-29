---
title: difference between subtract operator and minus sign in Notion
videoId: Fz_fpiT29EE
---

From: [[theaccountantguy]] <br/> 

Notion offers two primary methods to find the difference between two numbers within a database: using the [[subtract_operator_in_notion | subtract operator]] and using the minus sign <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Both approaches are utilized through [[using_formulas_in_notion | Notion formulas]] to achieve the same result of calculating the difference between two numerical properties <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This capability is part of [[using_notion_for_calculations | Notion's calculation]] features.

## Setting Up Your Notion Database

To begin, you need to create a database in Notion <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This can be done by typing a forward slash (`/`) and selecting "database" from the options <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

1.  **Title Property**: The first property in your database will be a "title" property, which helps signify the purpose of the rows <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
2.  **Number Properties**: Create two distinct number properties to hold the numerical values you wish to compare <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

Once your database is set up with these properties, you can add a new formula property to calculate the difference.

## Methods for Calculating the Difference

### 1. Using the Subtract Operator

The [[subtract_operator_in_notion | subtract operator]] is a specific function designed for [[using_formulas_to_subtract_in_notion | subtracting numbers]] in Notion <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

*   **Functionality**: This operator takes two numbers as input and returns their difference <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **Syntax Example**: If your number properties are named "Number 1" and "Number 2," the formula would typically look like `subtract(prop("Number 1"), prop("Number 2"))` <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### 2. Using the Minus Sign

Alternatively, you can use the standard minus sign (`-`) as an operator to find the difference between two numbers <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

*   **Functionality**: Similar to the [[subtract_operator_in_notion | subtract operator]], the minus sign directly calculates the difference between the first and second number properties specified <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Syntax Example**: Using the same property names, the formula would be `prop("Number 1") - prop("Number 2")` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

Both methods effectively allow you to determine the numerical difference between two entries in your Notion database <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.