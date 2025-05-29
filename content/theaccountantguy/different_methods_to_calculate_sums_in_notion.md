---
title: Different methods to calculate sums in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Adding two numbers together in Notion is a straightforward process, primarily achieved using the `AD` operator <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. To [[using_formulas_to_add_numbers_in_notion | add two numbers together in Notion]] and [[calculating_the_sum_of_a_column_in_notion | find the sum of numbers]] within a Notion database, a three-step approach is recommended <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:

1.  Create a database to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Apply the desired formula to find the sum <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: Creating a Database in Notion

A database in Notion is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature for storing, managing, and tracking information in a structured manner <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Notion databases consist of properties that define the different types of data stored within them <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a database in Notion, type `/database` and select `Database - Inline` to quickly add it to your page <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Step 2: Setting up the Database Correctly

Every database created in Notion includes a default property, which is the first column, always set as `Title` and cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For the purpose of finding the sum of two numbers, the database will require the following properties <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:

*   **Test Title property** (the default `Title` column) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   **Paper 1 Number property** <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   **Paper 2 Number property** <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   **Formula 1 Formula property** <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   **Formula 2 Formula property** <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

To add new properties, click on the plus symbol (`+`) at the top right end of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. From the list of options, select the desired property type, such as `Number` for "Paper 1" and "Paper 2", and `Formula` for "Formula 1" and "Formula 2" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up with the necessary properties, two different [[using_formulas_in_notion | formulas]] can be used to [[using_formulas_to_add_numbers_in_notion | find the sum of two numbers in Notion]] <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Formula One: Simple Addition with the Plus Sign

This basic formula directly [[using_formulas_to_add_numbers_in_notion | adds all numbers together]] using the plus (`+`) sign <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

```notion
prop("Paper 1") + prop("Paper 2")
```
<a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>

### Formula Two: Using the `add()` Function

Notion includes a built-in `add()` operator specifically designed to [[using_formulas_to_add_numbers_in_notion | help find the sum of numbers]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add()` function takes two parameters and returns their sum <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

For example:
*   `add(1, 3)` equals 4 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   `add("I love", " Notion")` equals "I love Notion" (demonstrating concatenation) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

To [[using_formulas_to_add_numbers_in_notion | add the two numbers]] "Paper 1" and "Paper 2", the formula would be:

```notion
add(prop("Paper 1"), prop("Paper 2"))
```
<a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>

These two [[using_formulas_in_notion | formulas]] provide effective methods for calculating sums of two numbers within a Notion database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.