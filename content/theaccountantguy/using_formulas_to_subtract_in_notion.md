---
title: using formulas to subtract in Notion
videoId: Fz_fpiT29EE
---

From: [[theaccountantguy]] <br/> 

This article discusses how to find the difference between two numbers in Notion using formulas <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Two methods are covered: using the [[subtract_operator_in_notion | subtract operator]] and using the minus sign (-) <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Setting Up Your Notion Database

To begin, you need to create a database in Notion <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
1.  Type a forward slash `/` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
2.  Type "database" to select from the options <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Within your database, you will need to:
*   **Title Property**: The first property is typically the title property, which indicates the purpose of the row <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Number Properties**: Assign "number" properties to the two numbers you wish to find the difference between <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Formula Property**: Add a formula property where the calculation will be performed <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Methods for Subtraction

### 1. Using the `subtract` operator

The `subtract` operator is a formula used to find the difference between two numbers <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   It takes two numbers as input <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   For example, if you have `Number One` and `Number Two` as your input properties, the formula `subtract(prop("Number One"), prop("Number Two"))` will yield the difference <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### 2. Using the Minus Sign (`-`)

Alternatively, you can use the standard minus sign (`-`) to achieve the same result <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   This method is more similar to [[using_excellike_formulas_in_notion | Excel-like formulas]] <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   For example, `prop("Number One") - prop("Number Two")` will also find the difference between the two numbers <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Both methods allow you to effectively calculate the difference between numbers within your Notion database <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This is part of [[using_notion_for_calculations | using Notion for calculations]] and [[using_formulas_in_notion | applying formulas]].