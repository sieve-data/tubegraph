---
title: How to add numbers in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Adding two numbers together in Notion is a simple task that can be achieved using the [[using_the_add_operator_in_notion | AD operator]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This process involves setting up a database, configuring its properties, and applying the correct [[using_formulas_in_notion | formula]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Three-Step Approach to Finding the Sum of Numbers in Notion

To find the sum of numbers within a Notion database, follow this three-step approach <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>:

1.  Create a database <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Apply the desired [[formulas for finding the sum of numbers in notion | formula]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### Step 1: How to Create a Database in Notion

#### What is a Notion Database?

In Notion, a database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature allowing users to create custom databases to store, manage, and track information in a structured and organized manner <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. A Notion database consists of [[properties of numbers in notion | properties]] that define the types of data stored within it <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

#### How to Add a Database in Notion

To add a database in Notion, type `/database` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. From the list of options, select "Database - Inline" to quickly add a database to your Notion page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Step 2: Setting up the Database Correctly

Every newly created database will have a default property as its first column, which is always of the "title" type and cannot be changed <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. In this example, the "test name" is used for this default column <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

To find the sum of two numbers, your database will require the following properties <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:

*   Test Title property <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 (Number property) <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 (Number property) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 (Formula property) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 (Formula property) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

#### How to Add Properties

To add [[properties of numbers in notion | properties]] to a Notion database, click on the plus symbol (`+`) at the top right end of the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. A list of options will appear, allowing you to choose the property type <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For numbers, select the "Number" property and name it "Paper 1" (or "Paper 2") <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Similarly, add two "Formula" properties <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, two different [[formulas for finding the sum of numbers in notion | formulas]] can be used to find the sum of two numbers in Notion <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

#### Formula One: Using the Plus Sign

This basic [[using_formulas_in_notion | formula]] involves adding numbers together using the plus (`+`) sign <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

```notion
prop("Paper 1") + prop("Paper 2")
```
This [[using_formulas_in_notion | formula]] adds the values from the "Paper 1" and "Paper 2" number [[properties of numbers in notion | properties]] <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

#### Formula Two: Using the `add` Function

Notion also has a built-in `add` operator to help find the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function essentially helps to add two numbers together <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. It takes two parameters (arguments) and provides the output <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

For example:
*   `add(1, 3)` equals 4 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   `add("I love", " Notion")` equals "I love Notion" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

To add the values from "Paper 1" and "Paper 2" using the `add` function, use the following [[using_formulas_in_notion | formula]] <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>:

```notion
add(prop("Paper 1"), prop("Paper 2"))
```
This [[using_formulas_in_notion | formula]] uses the `add` function with the "Paper 1" and "Paper 2" [[properties of numbers in notion | properties]] as its arguments <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

---
**Summary:**
Two main [[formulas for finding the sum of numbers in notion | formulas]] can be used to find the sum of two numbers in a Notion database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>:
1.  `prop("Number 1") + prop("Number 2")` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>
2.  `add(prop("Number 1"), prop("Number 2"))` <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>