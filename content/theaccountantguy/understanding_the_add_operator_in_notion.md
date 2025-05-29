---
title: Understanding the add operator in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[Using formulas to add numbers in Notion | Adding two numbers together in Notion]] is a simple task that can be accomplished with the use of the 'AD' operator or 'add' function <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

To find the sum of numbers in a Notion database, a three-step approach can be followed <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:
1.  Create a database to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Apply the desired formula to find the sum <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## How to Create a Database in Notion

A Notion database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It is a powerful feature allowing users to create custom databases to store, manage, and track information <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Databases are made up of properties that define the types of data stored within them <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a database in Notion, type `/database` and select "Database inline" from the options to quickly add it to your page <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Setting Up the Database Correctly

Every Notion database includes a default property, which is the first column, always of the 'Title' type and cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a> <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For finding the sum of two numbers, the following properties are required in the database <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   Test Title property (the default Title column) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 Number property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 Number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 Formula property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 Formula property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

To [[adding_properties_in_a_notion_database | add properties in a database]] in Notion, click on the plus symbol at the top-right end of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. From the list of options, select the desired property type, for example, "Number" for 'Paper 1' <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Finding the Sum of Two Numbers in Notion

Once the database is set up, two different formulas can be used to find the sum of two numbers in Notion <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. After adding the 'Paper 1' and 'Paper 2' number properties, [[using_symbols_in_notion_formulas | add two more properties]] and set their type as 'Formula' <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Formula One: Using the Plus Sign (+)

This basic formula involves adding all the numbers together with the use of the plus (`+`) sign <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a> <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

*   **Formula:** `prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a> <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
    *   This formula will find the sum of the values in the 'Paper 1' and 'Paper 2' properties.

### Formula Two: Using the `add()` Function

Notion has a built-in `add()` function designed to help find the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add()` function takes two parameters and will give the output <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a> <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

*   **Examples of `add()` function:**
    *   `add(1, 3)` equals 4 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a> <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
    *   `add("I love", "Notion")` equals "I love Notion" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>
*   **Formula for Paper 1 and Paper 2:** `add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a> <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>

Both of these formulas can be used to [[using_formulas_to_add_numbers_in_notion | find the sum of two numbers]] in a Notion database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.