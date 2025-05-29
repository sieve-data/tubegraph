---
title: Using the add operator in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[adding_numbers_in_notion | Adding two numbers together in Notion]] is a simple task that can be accomplished using the `add` operator or the plus sign operator within [[formulas in Notion | formulas]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

To find the sum of numbers in a Notion database, follow a three-step approach <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>:
1.  Create a database <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Apply the desired formula to find the sum of two numbers <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: How to Create a Database in Notion

In Notion, a database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature for storing, managing, and tracking information in a structured manner <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. A Notion database consists of properties that define the types of data stored within it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To [[adding_numbers_in_notion | add a database]] in Notion, type `/database` and select `Database - Inline` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This allows you to quickly add a database to your Notion page <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Step 2: Setting Up the Database Correctly

Every database created in Notion will have a default property, which is the first column, set as a `Title` type that cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This default property is created automatically when a new database is made <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. In this example, the test name is written in the first column <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

To find the sum of two numbers in a database, the following properties are required <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:
*   Test Title property <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 Number property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 Number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 Formula property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 Formula property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### How to [[assigning_properties_in_notion | Add Properties]] in a Database

To [[assigning_properties_in_notion | add properties]] in a Notion database, click on the plus symbol (`+`) at the top right end of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This will present a list of options to choose the property type <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Select the `Number` property type and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

Next, [[adding_numbers_in_notion | add two more properties]] and set their property type as `Formula` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, you can use two different [[formulas in Notion | formulas]] to find the sum of two numbers in Notion <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Formula 1: Using the Plus Sign Operator

This basic formula involves adding all the numbers together using the plus sign (`+`) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

The formula to use is:
```
prop("Paper 1") + prop("Paper 2")
```
<a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>

### Formula 2: Using the `add` Function

Notion has a built-in `add` operator (function) that helps find the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function essentially helps to [[adding_numbers_in_notion | add two numbers together]] <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Important notes about the `add` function:
*   `add` takes two parameters as input and provides an output <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   Examples:
    *   `add(1, 3)` equals 4 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   `add("I love", " Notion")` equals "I love Notion" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

To add the two numbers, Paper 1 and Paper 2, use the following formula:
```
add(prop("Paper 1"), prop("Paper 2"))
```
<a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

Both `prop("Number 1") + prop("Number 2")` and `add(prop("Number 1"), prop("Number 2"))` are valid [[formulas in Notion | formulas]] for [[adding_numbers_in_notion | finding the sum of two numbers]] in a database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.