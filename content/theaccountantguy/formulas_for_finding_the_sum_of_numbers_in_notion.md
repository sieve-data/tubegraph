---
title: Formulas for finding the sum of numbers in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Adding two numbers together in Notion is a straightforward task, achievable through the use of an 'add' operator or function <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This guide outlines a three-step approach to [[how_to_add_numbers_in_notion | find the sum of numbers]] within a Notion database <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Three-Step Approach to Sum Numbers <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>

1.  **Create a database:** Set up a database to hold the data for the numbers you wish to sum <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  **Set up the database correctly:** Configure the database with the necessary properties <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  **Put the desired formula:** Apply the appropriate [[using_formulas_in_notion | formula]] to [[how_to_add_numbers_in_notion | find the sum]] of the two numbers <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: How to Create a Database in Notion <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>

A Notion database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful tool for storing, managing, and tracking information in a structured manner <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Databases are composed of properties that define the types of data stored within them <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a database in Notion, type `/database` and select "database inline" from the options to quickly add it to your page <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Step 2: Setting up the Database Correctly <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>

Every database created in Notion will have a default property as its first column, which is always of the "Title" type and cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For this example, this column is used for a "Test Name" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

To [[how_to_add_numbers_in_notion | find the sum of two numbers]], the following properties are required in your database <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:

1.  Test Title property <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
2.  Paper 1 [[properties_of_numbers_in_notion | number property]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
3.  Paper 2 [[properties_of_numbers_in_notion | number property]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
4.  Formula 1 [[using_formulas_in_notion | formula property]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
5.  Formula 2 [[using_formulas_in_notion | formula property]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### How to Add Properties in a Database <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>

To add properties, click the plus symbol `+` at the top right of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. From the list of options, select the desired property type. For instance, select the "Number" property type and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Repeat this process to add "Paper 2" as a number property, and "Formula 1" and "Formula 2" as [[using_formulas_in_notion | formula properties]] <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>

Once the database is set up, you can use two different [[using_formulas_in_notion | formulas]] to [[how_to_add_numbers_in_notion | find the sum of two numbers]] in Notion <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>:

### Formula 1: Using the Plus Sign `+` <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>

This is a basic [[using_formulas_in_notion | formula]] that adds all numbers together using the `+` sign <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

**Formula:**
`prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>

### Formula 2: Using the `add()` Function <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>

Notion has a built-in operator, the `add()` function, which also [[how_to_add_numbers_in_notion | helps to add two numbers together]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add()` function takes two parameters and returns their sum <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

**Examples:**
*   `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   `add("I", " love Notion")` equals `"I love Notion"` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

**Formula:**
`add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

These two [[using_formulas_in_notion | formulas]] provide effective ways to [[how_to_add_numbers_in_notion | find the sum of two numbers]] within a Notion database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.