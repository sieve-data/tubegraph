---
title: Using the plus sign to add numbers in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[Adding numbers in Notion using formulas | Adding two numbers together in Notion]] is a simple task that can be accomplished using [[Using formulas in Notion | formulas]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This method involves using the plus sign (`+`) operator directly in a Notion formula <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

To [[calculating_sum_of_a_column_in_notion | find the sum of numbers]] in a Notion database, a three-step approach is followed <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:
1.  Create a database to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Put the desired formula that will help [[adding_numbers_in_notion_using_formulas | find the sum of two numbers]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: Creating a Database in Notion

A Notion database is a collection of data structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature for storing, managing, and tracking information <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Databases are made up of properties that define the types of data stored within them <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a database in Notion, type `/database` and select "Database - Inline" from the options <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Step 2: Setting up the Database Correctly

Every Notion database comes with a default "Title" property as its first column, which cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For [[adding_numbers_in_notion_using_formulas | finding the sum of two numbers]], the database requires the following properties <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:

*   **Test Title Property** (default "Title" property) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   **Paper 1 Number Property** <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   **Paper 2 Number Property** <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   **Formula 1 Formula Property** (to use the plus sign formula) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

To add new properties, click the plus symbol (`+`) at the top right of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Select "Number" for `Paper 1` and `Paper 2`, and "Formula" for `Formula 1` <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## Step 3: Finding the Sum Using the Plus Sign Formula

Once the database is set up with the necessary number and formula properties, you can apply the formula to [[adding_numbers_in_notion_using_formulas | find the sum of two numbers]] <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

The formula using the plus sign (`+`) works by adding numbers together <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

**Formula:**
`prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

This formula directly adds the values from the "Paper 1" and "Paper 2" number properties.

**Summary of Formulas for Addition:**
While Notion offers the `add()` function for [[using_the_add_function_to_calculate_sums_in_notion | adding numbers]], the direct `+` operator is also a valid method <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
Both `prop("Number 1") + prop("Number 2")` and `add(prop("Number 1"), prop("Number 2"))` can be used to [[adding_numbers_in_notion_using_formulas | find the sum of two numbers]] in a Notion database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.