---
title: Setting up a database in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[notion_database_setup | Setting up a database in Notion]] is a fundamental step for organizing and managing information efficiently <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This guide outlines the process, specifically for adding numbers within a database using various formulas.

## What is a Database in Notion?
In Notion, a database is a collection of data that can be structured and organized in a variety of ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It is a powerful feature that allows users to [[creating_a_database_in_notion | create custom databases]] to store, manage, and track information in a structured and organized manner <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. A Notion database is made up of a collection of properties that define the different types of data that can be stored within it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Steps to Find the Sum of Numbers in a Notion Database
To find the sum of numbers in a Notion database, follow a three-step approach <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:
1.  [[creating_databases_in_notion | Create a database]] to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  [[setting_up_and_connecting_notion_database_for_pdf_creation | Set up the database correctly]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Put the desired formula that will help find the sum of two numbers <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### Step 1: Creating a Database in Notion
To add a database in Notion, simply type `/database` and select `database inline` from the list of options to quickly add it to your Notion page <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Step 2: Setting Up the Database Correctly
When [[creating_and_managing_databases_in_notion | creating any database]] in Notion, a default property will always be present as the first column <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This default property always has the type "Title" and cannot be changed <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

To find the sum of two numbers, your database will require the following properties <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   Test title property <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 (number property) <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 (number property) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 (formula property) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 (formula property) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

#### How to Add Properties in a Database
To add properties in a database in Notion, click on the plus `+` symbol at the top right end of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Once selected, you will get a list of options to choose from to select the property type <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For example, select the "Number" property and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### Step 3: Finding the Sum of Two Numbers in Notion
Once the database is set up, you can use formulas to calculate the sum of numbers <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Two different formulas can be used for this purpose <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>:

#### Formula 1: Simple Addition Operator
This basic formula adds all numbers together using the plus `+` sign <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
```notion
prop("Paper 1") + prop("Paper 2")
```
This formula adds the values from the "Paper 1" and "Paper 2" number properties <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

#### Formula 2: Use of `add()` Function
Notion also has a built-in `add()` operator to find the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add()` function helps to add two numbers together <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. It takes two parameters and provides the output <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

For example:
*   `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   `add("I love", " Notion")` equals `I love Notion` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

To add the "Paper 1" and "Paper 2" numbers using this function, use the following formula <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>:
```notion
add(prop("Paper 1"), prop("Paper 2"))
```

Both formulas achieve the same result of finding the sum of two numbers in a database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.