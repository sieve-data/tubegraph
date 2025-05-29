---
title: Using the add operator in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[adding_numbers_in_notion | Adding two numbers together in Notion]] is a straightforward task that can be accomplished using the `AD` operator <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This process involves a three-step approach to find the sum of numbers within a database <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:

1.  Create a database to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Apply the desired [[using_formulas_in_notion | formula]] to find the sum <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: How to Create a Database in Notion

A Notion database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature for storing, managing, and tracking information in a structured manner <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Databases are composed of properties that define the types of data stored within them <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a database in Notion, simply type `/database` and select `Database - Inline` from the options to quickly add it to your page <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Step 2: Setting up the Database Correctly

Every database created in Notion will have a default property as its first column, which is of the `Title` type and cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For this example, this default property is used for "Test Name" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

To [[adding_numbers_in_notion | find the sum of two numbers]], the database requires the following properties <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:

*   Test Title property (the default title property) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 number property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 Formula property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 Formula property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### How to Add Properties in a Database

To add properties, click the plus symbol (`+`) at the top right end of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. From the list of options, select `Number` property and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Repeat this for "Paper 2" and add two more properties, setting their type as `Formula` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, you can use two different [[using_formulas_in_notion | formulas]] to [[adding_numbers_in_notion | find the sum of two numbers]] in Notion <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>:

### Formula One: Using the Plus Sign

This basic [[using_formulas_in_notion | formula]] simply adds all numbers together using the plus (`+`) sign <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

*   **Logic**: Add all the numbers together with the use of the plus sign <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Example Formula**: `prop("paper 1") + prop("paper 2")` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>

### Formula Two: Using the `add()` Function

Notion also has a built-in `add()` operator to help [[adding_numbers_in_notion | find the sum of numbers]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add()` function essentially helps to [[adding_numbers_in_notion | add two numbers together]] <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

*   **Parameters**: The `add()` function takes two parameters inside and returns the output <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Examples**:
    *   `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
    *   `add("I love", "Notion")` equals `"I love Notion"` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>
*   **Formula for Paper 1 and Paper 2**: `add(prop("paper 1"), prop("paper 2"))` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

### Summary of Formulas

To [[adding_numbers_in_notion | find the sum of two numbers]] in a database, you can use:

*   `prop("number one") + prop("number two")` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>
*   `add(prop("number one"), prop("number two"))` <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>