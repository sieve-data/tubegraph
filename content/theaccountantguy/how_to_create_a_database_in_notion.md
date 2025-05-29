---
title: How to create a database in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Adding two numbers together in Notion is a simple task that can be accomplished using the `add` operator <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves a three-step approach: creating a database, setting it up correctly, and applying the desired formula <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This guide outlines how to [[creating_a_database_in_notion_for_calculations | create a database in Notion for calculations]].

## What is a Notion Database?

In Notion, a database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature allowing users to create custom databases to store, manage, and track information in a structured and organized manner <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. A Notion database is composed of properties that define the different types of data it can store <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Step 1: Creating a Database in Notion

To add a database in Notion, simply type `/database` into a Notion page <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This will present a list of options for adding a database <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Select "database inline" to quickly add a database to your page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Step 2: [[setting_up_a_database_in_notion | Setting up the Database Correctly]]

When you [[setting_up_a_database_in_notion | create a new database]], it will always have a default property as its first column, which is of "Title" type and cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For the purpose of finding the sum of two numbers, the database will require the following properties:

*   Test Title property (the default first column) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 Number property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 Number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 Formula property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 Formula property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### How to Add Properties in a Database

To add properties to your database, click on the plus symbol (`+`) located at the top right end of the database <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This will display a list of property types to choose from <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For example, select the "Number" property and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Repeat this process for "Paper 2" and add two more properties with the type set as "Formula" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, you can use formulas to find the sum of two numbers <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Formula One: Basic Addition

This formula uses the plus sign (`+`) to add numbers together <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>:

```notion
prop("Paper 1") + prop("Paper 2")
```
This formula will find the sum of values in the "Paper 1" and "Paper 2" properties <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Formula Two: Using the `add` Function

Notion also has a built-in `add` operator specifically for finding the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function takes two parameters as input and returns their sum <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

For example:
*   `add(1, 3)` equals 4 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   `add("I love", " Notion")` equals "I love Notion" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

To add the values from "Paper 1" and "Paper 2" properties using the `add` function, use the following formula:

```notion
add(prop("Paper 1"), prop("Paper 2"))
```
These two formulas demonstrate how to find the sum of two numbers within your Notion database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.