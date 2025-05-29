---
title: Minus sign for subtraction in Notion
videoId: Fz_fpiT29EE
---

From: [[theaccountantguy]] <br/> 

This article explains how to find the difference between two numbers in a Notion database using the minus sign <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This is one of two methods for performing subtraction in Notion, the other being the use of the [[subtract_operator_in_notion | `subtract` operator]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Database Setup for Subtraction

To begin, you need to create a database in Notion <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
1.  Type a forward slash (`/`) and then "database" to view available options <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
2.  The first property of the database is typically a "title" property, which indicates the purpose of the calculation <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
3.  Assign "number" properties to two different columns where your numerical values will be entered <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. These will be the numbers you want to find the difference between <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Applying Formulas for Subtraction

Once your database is set up, you can apply [[Formulas in Notion | formulas]] to calculate the difference. Notion offers two primary ways to subtract:

### 1. Using the `subtract` operator
The `subtract` operator is a formula that takes two numbers as input and returns their difference <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. For example, if you have `Number One` and `Number Two` columns, you would use a formula like `subtract(prop("Number One"), prop("Number Two"))` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### 2. Using the Minus Sign (-)
Alternatively, you can use the standard minus sign (`-`) within a Notion formula to find the difference between two numbers <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This method functions similarly to traditional mathematical subtraction.

For instance, if your number properties are named `Number One` and `Number Two`, the formula to find their difference using the minus sign would be:
`prop("Number One") - prop("Number Two")` <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Both methods allow you to calculate the difference between two numbers in a Notion database <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.