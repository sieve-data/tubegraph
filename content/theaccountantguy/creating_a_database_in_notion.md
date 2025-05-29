---
title: Creating a database in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[setting_up_a_database_in_notion | Creating a database in Notion]] is an essential first step for various data management tasks, such as performing calculations like adding two numbers together <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process typically involves a three-step approach: first, [[creating_and_connecting_databases_in_notion | creating the database]]; second, [[setting_up_databases_in_notion | setting up the database]] correctly; and third, applying the desired formulas <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## What is a Notion Database?

In Notion, a database serves as a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a robust feature enabling users to [[creating_a_database_in_notion_for_calculations | create custom databases]] for storing, managing, and tracking information in a structured and organized manner <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Each Notion database consists of a collection of properties, which define the different types of data that can be stored within it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## How to Create a Database in Notion

To add a database to your Notion page:
1.  Type `/database` <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  A list of options for adding a database will appear <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
3.  Select `Database - Inline` to quickly add a database to your current Notion page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Setting Up the Database Correctly

After [[setting_up_a_database_in_notion | creating a database]], the next crucial step is [[setting_up_and_customizing_notion_database_for_invoices | setting up]] its properties <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Every newly created database includes a default property as its first column, which is always of the "Title" type and cannot be changed <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

For finding the sum of two numbers, a database would typically require the following properties:
*   **Test Title Property**: This is the default "Title" property (e.g., `Test name`) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Paper 1 Number Property**: A property to hold the first number <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Paper 2 Number Property**: A property to hold the second number <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Formula 1 Formula Property**: A property for the first sum calculation <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Formula 2 Formula Property**: A property for the second sum calculation <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### How to Add Properties

To add additional properties to your database:
1.  Click on the `+` symbol located at the top right end of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
2.  A list of options will appear, allowing you to choose the property type <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
3.  For numeric values, select the `Number` property type and name it appropriately (e.g., `Paper 1`) <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
4.  For calculations, add a `Formula` property type <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Finding the Sum of Two Numbers with Formulas

Once the database is [[setting_up_a_database_in_notion_for_financial_tracking | set up]] with the necessary number and formula properties, you can then input formulas to perform calculations <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Formula One: Using the Plus Sign

This basic formula directly adds numbers using the `+` sign <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
```notion
prop("Paper 1") + prop("Paper 2")
```
<a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>

### Formula Two: Using the `add` Function

Notion also includes a built-in `add` function for summing numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function takes two parameters as input <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
```notion
add(prop("Paper 1"), prop("Paper 2"))
```
<a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

These two formulas demonstrate methods for finding the sum of two numbers within a [[creating_databases_for_an_expense_tracker_in_notion | Notion database]] <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.