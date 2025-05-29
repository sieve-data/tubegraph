---
title: How to create a database in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[creating_a_database_in_notion | Creating a database in Notion]] is a fundamental step for managing and tracking information in a structured way <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. It's a powerful feature allowing users to create custom databases to store, manage, and track information <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

A Notion database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It consists of a collection of properties that define the different types of data stored within it <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

To find the sum of numbers within one database, a three-step approach can be followed <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>:
1.  [[creating_a_database_in_notion | Create a database]] to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  [[setting_up_databases_and_relationships_in_notion | Set up the database correctly]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Implement the desired formula <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## How to Create a Database in Notion

To add a database in Notion, type `/database` into a Notion page <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This action will present a list of options for adding a database <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Select `database inline` to quickly add a database to your Notion page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Setting Up the Database Correctly

When [[setting_up_databases_and_relationships_in_notion | setting up a database]] in Notion, there is always a default property, which appears as the first column <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This property is always of the "Title" type and its type cannot be changed <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. For instance, this default column can be used to name "Test Name" <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

To facilitate specific calculations, such as summing two numbers, the database would require the following properties <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>:
1.  Test title property <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
2.  Paper 1 number property <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
3.  Paper 2 number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
4.  Formula 1 Formula property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
5.  Formula 2 formula property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### How to Add Properties in a Database

To add properties to a database in Notion, click on the plus symbol (`+`) located at the top-right end of the database <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This will display a list of options for property types <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. For numerical operations, select the "Number" property type and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Repeat this process for "Paper 2" and for the formula properties <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Finding the Sum of Two Numbers in Notion

Once the database is set up, specific formulas can be used to find the sum of two numbers <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Two methods can be applied:

### Formula One: Using the Plus Sign

This basic formula involves adding all numbers together directly with the plus sign (`+`) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Formula:** `prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

### Formula Two: Using the `add` Function

Notion provides a built-in operator, `add`, to help find the sum of numbers <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The `add` function takes two parameters as input and returns their sum <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Example:** `add(1, 3)` equals 4 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   **Example (non-numeric):** `add("I love", " Notion")` equals "I love Notion" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>
*   **Formula for two numbers:** `add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>

Both `prop("Number 1") + prop("Number 2")` and `add(prop("Number 1"), prop("Number 2"))` are valid formulas for [[setting_up_a_database_for_adding_numbers_in_notion | finding the sum of two numbers in a database]] <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.