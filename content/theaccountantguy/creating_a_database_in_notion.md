---
title: Creating a database in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[creating_databases_in_notion | Creating databases in Notion]] is a fundamental skill for organizing information. This guide outlines the steps to create and set up a database within Notion <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## What is a Database in Notion?
In Notion, a database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a> <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. It is a powerful feature enabling users to create custom databases to store, manage, and track information in a structured and organized manner <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a> <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. A Notion database comprises a collection of "properties" that define the different types of data it can store <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a> <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## How to Create a Database in Notion
To add a database in Notion:
1.  Simply type `/database` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  From the list of options, select "Database - Inline" to quickly add a database to your Notion page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## [[setting_up_a_database_in_notion | Setting Up a Database in Notion]]
After [[creating_databases_in_notion | creating a database]], the next step is to [[setting_up_a_database_in_notion | set up the database correctly]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a> <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Default Property
Any database you create will always have a default property, which is the first column of the database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a> <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This property will always have "Title" as its type, which cannot be changed <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. For example, this default column can be used for a "Test Title" or "Test Name" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a> <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a> <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Required Properties for Calculations
To find the sum of two numbers in a database, the following properties are required <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>:
*   Test Title property (default "Title" column) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 number property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 formula property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 formula property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### How to Add Properties in a Database
To add properties in a database in Notion:
1.  Click on the plus symbol (`+`) at the top right end of the database <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a> <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Once selected, you will get a list of options to choose from for the property type <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a> <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
3.  For example, select the "Number" property and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a> <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

After adding "Paper 1," you will have "Test Title" (the default column) and "Paper 1" number property set up in the database <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a> <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. You would then add "Paper 2" as another number property, and two "Formula" properties for the calculations <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a> <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Finding the Sum of Two Numbers in Notion
Once the database is [[notion_database_setup | set up]], you can use formulas to find the sum of numbers <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a> <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Two different formulas can be used for this purpose <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a> <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>:

### Formula One: Using the Plus Sign
This basic formula involves adding all numbers together using the plus sign (`+`) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a> <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Formula:** `prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a> <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>

### Formula Two: Using the `add` Function
Notion has a built-in `add` operator to help find the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a> <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. The `add` function takes two parameters and provides the output <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a> <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Example:** `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a> <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
*   **Formula:** `add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a> <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>

These two formulas can be used to find the sum of two numbers within a Notion database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a> <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.