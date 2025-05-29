---
title: Setting up a database in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Adding two numbers together in Notion is a simple task that can be accomplished using the 'add' operator or basic addition formulas <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves a three-step approach: creating a database, setting it up correctly, and applying the necessary formulas <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## What is a Database in Notion?

In Notion, a database is a collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It is a powerful feature allowing users to [[creating_a_database_in_notion | create custom databases]] to store, manage, and track information in a structured manner <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. A Notion database comprises a collection of properties that define the different types of data it can store <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Step 1: [[creating_a_database_in_notion | Creating a Database in Notion]]

To [[creating_a_database_in_notion | add a database in Notion]], type `/database` to bring up a list of options <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Selecting "database inline" allows you to quickly add a database to your Notion page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Step 2: [[setting_up_databases_in_notion | Setting Up the Database Correctly]]

When you [[creating_a_database_in_notion | create a new database]], the first column is always a default property with the type "Title," which cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For finding the sum of two numbers, the database will require the following properties <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:

*   **Test Title Property:** The default "Title" column, used for test names <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Paper 1 Number Property:** To hold the first number <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Paper 2 Number Property:** To hold the second number <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Formula 1 Formula Property:** For the first calculation method <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Formula 2 Formula Property:** For the second calculation method <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### How to Add Properties in a Database

To add properties in a Notion database, click the plus symbol (+) at the top right end of the database <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This will present a list of options to choose the property type <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For example, select the "Number" property and name it "Paper 1" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up, you can use formulas to find the sum of two numbers <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Two different formulas can be used <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>:

### Formula One: Basic Addition

This formula works by adding all numbers together using the plus (+) sign <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

*   **Formula:** `prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>

### Formula Two: Using the `add` Function

Notion also has a built-in `add` operator for finding the sum of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function takes two parameters and provides the output <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

*   **Examples:**
    *   `add(1, 3)` equals 4 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
    *   `add("I love", " Notion")` equals "I love Notion" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>
*   **Formula for two numbers:** `add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

By using either `prop("number 1") + prop("number 2")` or `add(prop("number 1"), prop("number 2"))`, you can successfully find the sum of two numbers within your Notion database <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.