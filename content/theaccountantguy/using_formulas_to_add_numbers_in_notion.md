---
title: Using formulas to add numbers in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Adding two numbers together in [[using_notion_for_calculations | Notion]] is a simple task that can be accomplished with the use of the `AD` operator or other [[using_formulas_in_notion | formulas]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

To find the sum of numbers in a database, a three-step approach can be followed <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:
1.  Create a database to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Put the desired [[using_formulas_in_notion | formula]] to find the sum <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## How to Create a Database in Notion

A Notion database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature allowing users to create custom databases to store, manage, and track information in a structured and organized manner <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. A Notion database is made up of a collection of properties that define the different types of data stored within it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a database in Notion, type `/database` to get a list of options <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Select `database inline` to quickly add one to your Notion page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Setting Up the Database Correctly

Every database created in Notion will have a default property as its first column, which is always of the 'title' type and cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

To find the sum of two numbers, the database will require the following properties <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
1.  **Test Title property** <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
2.  **Paper 1 Number property** <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
3.  **Paper 2 Number property** <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
4.  **Formula 1 Formula property** <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
5.  **Formula 2 Formula property** <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### How to Add Properties in a Database
To add properties in a database, click on the plus symbol (`+`) at the top right end of the database <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. From the list of options, select the desired property type <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For example, select the 'number' property and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

Once the 'Test Title' (default) and 'Paper 1' number properties are set up, add two more properties and set their property type as 'Formula' <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Finding the Sum of Two Numbers in Notion

After the database is set up, two [[different_methods_to_calculate_sums_in_notion | different methods to calculate sums]] can be used to find the sum of two numbers in Notion <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Formula One: Using the Plus Sign Operator

This basic [[using_formulas_in_notion | formula]] works by adding all numbers together with the use of the plus (`+`) sign <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

The formula to use is:
```
prop("Paper 1") + prop("Paper 2")
```
This adds the values from the "Paper 1" and "Paper 2" properties <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Formula Two: Using the `add()` Function

Notion has a built-in `add` operator to help find the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function helps to add two numbers together <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

The `add` function takes two parameters and provides the output <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Example**: `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Example**: `add("I", " love Notion")` equals `"I love Notion"` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

To add the two numbers, "Paper 1" and "Paper 2", the following [[using_formulas_in_notion | formula]] is used:
```
add(prop("Paper 1"), prop("Paper 2"))
```
This formula also finds the sum of the values from the "Paper 1" and "Paper 2" properties <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

Both formulas can be used to find the sum of two numbers in a database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>:
*   `prop("Number 1") + prop("Number 2")` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>
*   `add(prop("Number 1"), prop("Number 2"))` <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>