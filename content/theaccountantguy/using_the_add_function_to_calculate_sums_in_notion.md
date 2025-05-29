---
title: Using the add function to calculate sums in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[Adding numbers in Notion using formulas | Adding two numbers together in Notion]] is a straightforward task that can be achieved using the `add` operator <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. To find the sum of numbers in a database, a three-step approach is followed: creating the database, setting it up correctly, and applying the desired formula <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

## Step 1: Create a Database in Notion

A Notion database is a collection of structured and organized data, allowing users to store, manage, and track information <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>. It consists of properties that define the types of data stored <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>.

To create a database in Notion, type `/database` and select "Database - Inline" <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>.

## Step 2: Setting up the Database Correctly

Every Notion database includes a default "Title" property as its first column, which cannot be changed <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>. For [[calculating_sum_of_a_column_in_notion | finding the sum of two numbers]], the database requires the following properties <a class="yt-timestamp" data-t="01:56:56">[01:56:56]</a>:
1.  Test title property <a class="yt-timestamp" data-t="02:02:02">[02:02:02]</a>
2.  Paper 1 number property <a class="yt-timestamp" data-t="02:05:05">[02:05:05]</a>
3.  Paper 2 number property <a class="yt-timestamp" data-t="02:08:08">[02:08:08]</a>
4.  Formula 1 formula property <a class="yt-timestamp" data-t="02:11:11">[02:11:11]</a>
5.  Formula 2 formula property <a class="yt-timestamp" data-t="02:15:15">[02:15:15]</a>

To add properties, click the plus symbol `+` at the top right of the database, then select "Number" for `Paper 1` and `Paper 2`, and "Formula" for the formula properties <a class="yt-timestamp" data-t="02:21:22">[02:21:22]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, you can [[using_formulas_in_notion | use formulas]] to find the sum <a class="yt-timestamp" data-t="03:14:17">[03:14:17]</a>. Notion offers a built-in `add` function for this purpose <a class="yt-timestamp" data-t="04:01:01">[04:01:01]</a>.

### Using the `add` Function

The `add` function is designed to [[adding_numbers_in_notion_using_formulas | add two numbers together]] <a class="yt-timestamp" data-t="04:06:06">[04:06:06]</a>. It takes two parameters as input and returns their sum <a class="yt-timestamp" data-t="04:11:11">[04:11:11]</a>.

Examples:
*   `add(1, 3)` equals 4 <a class="yt-timestamp" data-t="04:17:17">[04:17:17]</a>
*   `add("I love", "Notion")` equals "I love Notion" <a class="yt-timestamp" data-t="04:20:20">[04:20:20]</a>

To [[calculating_total_sales_using_sum_function_in_notion | add the two numbers]] from the `Paper 1` and `Paper 2` properties, use the following formula:
`add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="04:24:26">[04:24:26]</a>

### Alternative: Using the Plus Sign

Another basic formula involves simply [[using_the_plus_sign_to_add_numbers_in_notion | adding numbers together]] with the `+` sign <a class="yt-timestamp" data-t="03:23:23">[03:23:23]</a>.

Formula:
`prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="03:34:34">[03:34:34]</a>

Both methods can be used to [[calculating_sum_of_a_column_in_notion | find the sum of two numbers]] in a database <a class="yt-timestamp" data-t="04:39:39">[04:39:39]</a>.