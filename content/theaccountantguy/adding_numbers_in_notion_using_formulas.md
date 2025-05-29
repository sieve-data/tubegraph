---
title: Adding numbers in Notion using formulas
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Adding two numbers together in Notion is a straightforward task <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This can be achieved using the [[using_the_add_function_to_calculate_sums_in_notion | add operator]] in Notion's [[using_formulas_in_notion | formulas]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

To find the [[calculating_sum_of_a_column_in_notion | sum of numbers]] in a Notion database, a three-step approach is followed <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:
1.  Create a database <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Apply the desired [[using_formulas_in_notion | formula]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: Creating a Database in Notion

A database in Notion is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature for storing, managing, and tracking information in a structured and organized manner <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. A Notion database comprises a collection of properties that define the types of data stored within it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a database in Notion, type `/database` to get a list of options <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Selecting "database inline" allows you to quickly add a database to your Notion page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Step 2: Setting Up the Database Correctly

Every database created in Notion will have a default property, which is the first column, always typed as "title" and cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For finding the [[calculating_sum_of_a_column_in_notion | sum of numbers]], the following properties are required <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   Test Title property (default 'title' column) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 Number property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 Number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 Formula property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 Formula property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

To add properties, click the plus symbol at the top right of the database <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. From the list of options, select the "number" property type and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Similarly, add "Paper 2" as a number property. To add the formula columns, add two more properties and set their type as "formula" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, you can use two different [[using_formulas_in_notion | formulas]] to find the [[calculating_sum_of_a_column_in_notion | sum of two numbers]] <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Formula One: Using the Plus Sign

This basic [[using_formulas_in_notion | formula]] adds all numbers together using the [[using_the_plus_sign_to_add_numbers_in_notion | plus sign]] (`+`) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

**Syntax:**
```
prop("Paper 1") + prop("Paper 2")
```
This [[using_formulas_in_notion | formula]] directly adds the values from the "Paper 1" and "Paper 2" number properties <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### Formula Two: Using the Add Function

Notion has a built-in [[using_the_add_function_to_calculate_sums_in_notion | add function]] (also known as the [[using_the_add_function_to_calculate_sums_in_notion | add operator]]) to help find the [[calculating_sum_of_a_column_in_notion | sum of numbers]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The [[using_the_add_function_to_calculate_sums_in_notion | add function]] takes two parameters and returns their sum <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

**Examples:**
*   `add(1, 3)` equals 4 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   `add("I love", " Notion")` equals "I love Notion" (demonstrates concatenation with text) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

**Syntax for adding numbers:**
```
add(prop("Paper 1"), prop("Paper 2"))
```
This [[using_formulas_in_notion | formula]] uses the [[using_the_add_function_to_calculate_sums_in_notion | add function]] to sum the "Paper 1" and "Paper 2" properties <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

You can use either `prop("number 1") + prop("number 2")` or `add(prop("number 1"), prop("number 2"))` to find the [[calculating_sum_of_a_column_in_notion | sum of two numbers]] in a database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.