---
title: Using formulas in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[adding_numbers_in_notion | Adding two numbers together in Notion]] is a simple task that can be accomplished using the `ADD` operator or the plus sign operator <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

To find the sum of numbers in a Notion database, a three-step approach is followed <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>:
1.  Create a database <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Apply the desired formula <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: How to Create a Database in Notion

A Notion database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It allows users to create custom databases to store, manage, and track information in a structured and organized manner <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. A database in Notion consists of properties that define the types of data stored within it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a database, type `/database` and select `database inline` to add it quickly to your Notion page <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Step 2: Setting Up the Database Correctly

Every Notion database includes a default property, which is the first column, always of the "title" type and cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For [[adding_numbers_in_notion | finding the sum of two numbers]], the database requires the following properties <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

*   **Test Title property**: The default first column <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Paper 1 Number property**: A number type property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Paper 2 Number property**: Another number type property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Formula 1 Formula property**: A formula type property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Formula 2 Formula property**: Another formula type property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

To add properties, click the plus symbol at the top right of the database and choose the desired property type <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. For example, select the `number` property and name it `Paper 1` <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, two different formulas can be used to [[adding_numbers_in_notion | find the sum of two numbers]] in Notion <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Formula 1: Using the Plus Sign Operator

This basic formula adds all numbers together using the plus (`+`) sign <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

```
prop("Paper 1") + prop("Paper 2")
```
<a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>

### Formula 2: Using the `add` Function

Notion has a built-in `add` operator that also helps [[adding_numbers_in_notion | find the sum of numbers]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function takes two parameters as input <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

Examples:
*   `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   `add("I love", " Notion")` equals `I love Notion` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

To add `Paper 1` and `Paper 2` using this function:

```
add(prop("Paper 1"), prop("Paper 2"))
```
<a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>

### Summary of Formulas

Both of these formulas can be used to [[adding_numbers_in_notion | find the sum of two numbers]] in a Notion database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>:
*   `prop("Number 1") + prop("Number 2")` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>
*   `add(prop("Number 1"), prop("Number 2"))` <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>