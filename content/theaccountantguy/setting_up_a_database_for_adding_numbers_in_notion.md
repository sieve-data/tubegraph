---
title: Setting up a database for adding numbers in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

This article details how to add two numbers together in Notion using database properties and formulas <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This simple task can be accomplished with the use of Notion's `AD` operator or the plus sign `+` <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

To find the sum of numbers within a Notion database, a three-step approach is followed <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>:
1.  [[creating_a_database_in_notion | Create a database]] to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  [[setting_up_databases_and_relationships_in_notion | Set up the database correctly]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Put the desired formula to find the sum of two numbers <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: Creating a Database in Notion

Before diving into creation, it's helpful to understand what a Notion database is <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. A database in Notion is a collection of structured and organized data, offering a powerful feature for users to [[how_to_create_a_database_in_notion | create custom databases]] to store, manage, and track information <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It consists of various properties that define the types of data stored within it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To [[creating_and_using_databases_in_notion | add a database]] in Notion, simply type `/database` on a page <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. From the list of options, select "Database - Inline" to quickly add a database to your Notion page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Step 2: Setting up the Database Correctly

Every database created in Notion will have a default property as its first column, which is always of "Title" type and cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For the purpose of finding the sum of two numbers, the following properties are required in your database <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:

*   **Test Title Property**: This is the default "Title" column <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Paper 1 Number Property**: A number property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Paper 2 Number Property**: Another number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Formula 1 Formula Property**: A formula property for the first method <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Formula 2 Formula Property**: A formula property for the second method <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### How to Add Properties in a Database

To add new properties in a Notion database:
1.  Click on the plus `+` symbol located at the top right end of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
2.  A list of options will appear to choose the property type <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
3.  Select the "Number" property type and name it "Paper 1" (and similarly for "Paper 2") <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
4.  Add two more properties and set their type as "Formula" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, you can [[using_formulas_to_add_numbers_in_notion | use formulas]] to find the sum of numbers <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Two different formulas can be used for this purpose <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Formula One: Using the Plus Sign `+`

This basic formula adds numbers together using the plus `+` sign <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

```notion
prop("Paper 1") + prop("Paper 2")
```
This formula directly sums the values from the "Paper 1" and "Paper 2" properties <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### Formula Two: Using the `add()` Function

Notion also has a built-in `add()` operator to help find the sum of numbers <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. The `add()` function takes two parameters inside and provides the output <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Examples:
*   `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   `add("I", "love notion")` equals `"I love notion"` (demonstrates it works with text too) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

To add "Paper 1" and "Paper 2" using the `add()` function, use the following formula:

```notion
add(prop("Paper 1"), prop("Paper 2"))
```
This formula also finds the sum of the values from the "Paper 1" and "Paper 2" properties <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

In summary, you can find the sum of two numbers in a Notion database using either `prop("Number 1") + prop("Number 2")` or `add(prop("Number 1"), prop("Number 2"))` <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.