---
title: Creating and setting up a database in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[creating_a_database_in_notion | Creating a database in Notion]] and setting it up is a fundamental task for managing and tracking information in a structured way <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>. This guide outlines the process, using the example of adding two numbers together in Notion <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Overview

The process to find the sum of numbers in one database follows a three-step approach <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>:
1.  [[creating_a_database_in_notion | Create a database]] to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  [[setting_up_databases_and_dashboards_in_notion | Set up the database]] correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Apply the desired formula to find the sum <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: Creating a Database in Notion

Before creating a database, it's important to understand what it is. In Notion, a database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature for users to create custom databases to store, manage, and track information <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. A Notion database comprises a collection of properties that define the different types of data stored within it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a database in Notion, simply type `/database` and select `Database - Inline` from the options to quickly add a database to your page <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Step 2: Setting Up the Database Correctly

When you [[creating_a_database_in_notion | create a new database]] in Notion, there will always be a default property which serves as the first column <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This default property is always of the 'Title' type and cannot be changed <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For the example of adding two numbers, this column is used for the "test name" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

To find the sum of two numbers, your database will require the following properties <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   Test Title property (the default 'Title' column) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 number property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 Formula property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 Formula property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### How to Add Properties in a Database

To add new properties in a Notion database, click on the plus symbol (`+`) located at the top-right end of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This will present a list of options to choose the property type <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

For the example of adding numbers:
*   Select the `Number` property type and name it `Paper 1` <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   Repeat the process to add `Paper 2` as another `Number` property.
*   Add two more properties and set their type as `Formula` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion (Using Formula Properties)

Once the database is [[setting_up_databases_and_dashboards_in_notion | set up]] with the necessary properties, you can use formulas to find the sum of two numbers <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Formula 1: Using the Plus Sign Operator

This basic formula adds all numbers together using the plus sign (`+`) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

```
prop("Paper 1") + prop("Paper 2")
```
This formula adds the values from the 'Paper 1' and 'Paper 2' number properties <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### Formula 2: Using the `add` Function

Notion also has a built-in `add` operator (function) for finding the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function essentially helps to add two numbers together <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

The `add` function takes two parameters as input and provides an output <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   `add("I love", " Notion")` equals `"I love Notion"` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

To add the 'Paper 1' and 'Paper 2' numbers, the formula is <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>:

```
add(prop("Paper 1"), prop("Paper 2"))
```
Both formulas achieve the same result of finding the sum of two numbers within a database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.