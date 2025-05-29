---
title: Using the add operator in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[how_to_add_numbers_in_Notion | Adding two numbers together in Notion]] is a simple task that can be accomplished with the use of the Add operator <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. To find the sum of numbers in a Notion database, a three-step approach is followed <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>:
1.  Create a database to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Put the desired [[using_formulas_in_Notion | formula]] to find the sum of two numbers <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: How to Create a Database in Notion

In Notion, a database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature for creating custom databases to store, manage, and track information in a structured manner <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. A Notion database is composed of properties that define the types of data it can store <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

To add a database in Notion, type `/database` to get a list of options <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Select `database inline` to quickly add one to your page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Step 2: Setting up the Database Correctly

Every database created in Notion includes a default property as its first column, which is always of the `Title` type and cannot be changed <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. In this example, this column is used for the "test name" <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

To find the sum of two numbers, the database will require the following properties <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>:
1.  Test title property <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
2.  Paper 1 number property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
3.  Paper 2 number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
4.  Formula 1 formula property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
5.  Formula 2 formula property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### How to Add Properties in a Database

To add properties in a Notion database, click the plus (`+`) symbol at the top right of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This will provide a list of options to choose the property type <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For numbers, select the `Number` property and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Repeat this process for "Paper 2" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Add two more properties and set their type as `Formula` for "Formula 1" and "Formula 2" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, there are two different [[formulas_for_finding_the_sum_of_numbers_in_Notion | formulas for finding the sum of two numbers in Notion]] <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Formula 1: Simply Add All Numbers Together (Using `+` operator)

This basic [[using_formulas_in_Notion | formula]] adds all numbers together using the plus sign (`+`) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Logic**: `add all the numbers together with the use of the plus sign` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>
*   **Formula Example**: `prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

### Formula 2: Use of `add` Function

Notion has a built-in `add` operator (function) specifically to help find the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. This `add` function essentially helps to add two numbers together <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Important**: The `add` function takes two parameters as input <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Example**: `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Text Concatenation**: `add("I love", " Notion")` equals `"I love Notion"` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Formula for Paper 1 and Paper 2**: `add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>

These two [[formulas_for_finding_the_sum_of_numbers_in_Notion | formulas]] can be used to find the sum of two numbers in a Notion database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.