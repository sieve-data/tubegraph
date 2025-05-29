---
title: Adding numbers in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Adding two numbers together in Notion is a straightforward task, accomplished using the [[using_the_add_operator_in_notion | AD operator]] <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. To find the sum of numbers in a Notion database, a three-step approach can be followed <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>:

1.  Create a database to hold the data <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.
3.  Apply the desired formula to find the sum of two numbers <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

## Step 1: How to Create a Database in Notion

A database in Notion is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. It's a powerful feature allowing users to create custom databases for storing, managing, and tracking information in a structured and organized manner <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>. Notion databases are composed of properties that define the types of data stored within them <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.

To add a database in Notion, type `/database` and select "Database - Inline" from the options to quickly add it to your Notion page <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

## Step 2: Setting up the Database Correctly

Every database created in Notion includes a default property, which is the first column, always of the type "Title" and cannot be changed <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. For adding two numbers, the database will require the following properties <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>:

*   Test Title property (default) <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>
*   Paper 1 [[creating_number_properties_in_notion | number property]] <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>
*   Paper 2 [[creating_number_properties_in_notion | number property]] <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>
*   Formula 1 [[using_formulas_in_notion | Formula]] property <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>
*   Formula 2 [[using_formulas_in_notion | Formula]] property <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>

To add properties to a database, click the plus symbol at the top right of the database <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. From the list of options, select the [[creating_number_properties_in_notion | number property]] type and name it "Paper 1" <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>. Add two more properties and set their type as [[using_formulas_in_notion | Formula]] <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, you can use two different [[using_formulas_in_notion | formulas]] to find the sum of two numbers in Notion <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

### Formula One: Using the Plus Sign

This basic formula works by adding all numbers together using the plus sign (`+`) <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>.

The formula is:
`prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>

### Formula Two: Using the `add` Function

Notion also has a built-in [[using_the_add_operator_in_notion | add function]] to help find the sum of numbers <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. The [[using_the_add_operator_in_notion | add function]] essentially helps to add two numbers together <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>. It takes two parameters as input and provides the output <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.

Examples:
*   `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>
*   `add("I love", " Notion")` equals `"I love Notion"` <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>

To add "Paper 1" and "Paper 2" together using this method, the formula is:
`add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>

---

In summary, two [[using_formulas_in_notion | formulas]] can be used to find the sum of two numbers in a database <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>:

1.  `prop("Number 1") + prop("Number 2")` <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>
2.  `add(prop("Number 1"), prop("Number 2"))` <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>