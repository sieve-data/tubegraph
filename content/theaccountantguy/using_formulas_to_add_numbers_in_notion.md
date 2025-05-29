---
title: Using formulas to add numbers in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Adding two numbers together in Notion is a straightforward process that can be achieved using various methods <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This guide outlines a three-step approach to accomplish this, leveraging Notion's formula capabilities <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Three-Step Approach to Sum Numbers

To find the sum of numbers within a Notion database, follow these steps:
1.  **Create a Database**: Establish a database to house your data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  **Set Up the Database Correctly**: Configure the database with the necessary properties <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  **Apply the Desired Formula**: Implement a formula to calculate the sum of two numbers <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: How to Create a Database in Notion

A database in Notion is a collection of structured data, allowing users to organize and track information effectively <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It consists of various properties that define the types of data stored <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a database to your Notion page, simply type `/database` and select `Database - Inline` from the options <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Step 2: Setting Up the Database Correctly

Every Notion database comes with a default "Title" property as its first column, which cannot be changed <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. For this example, this column can be used for a "Test Name" or "Test Title" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

To find the sum of two numbers, your database will require the following properties:
*   Test Title property (default) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 **Number** property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 **Number** property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 **Formula** property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 **Formula** property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### How to Add Properties in a Database

To add new properties, click on the plus symbol (`+`) at the top right of your database <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. From the list of options, select the desired property type (e.g., `Number`) and then name it (e.g., "Paper 1") <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Repeat this for "Paper 2" and the two "Formula" properties <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once your database is set up, you can use formulas to calculate the sum of numbers <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Here are two methods:

### Formula One: Simple Addition using the Plus Sign

This basic formula involves adding all numbers together directly using the `+` sign <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

**Formula Example:**
`prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>

### Formula Two: Using the `add` Function

Notion also provides a built-in `add` operator to find the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function takes two parameters and returns their sum <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

**Examples of `add` function usage:**
*   `add(1, 3)` equals 4 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   `add("I love", " Notion")` equals "I love Notion" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

**Formula Example:**
To add "Paper 1" and "Paper 2" using the `add` function:
`add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

These two methods provide flexible ways to calculate the sum of numbers within your Notion database using formulas <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.