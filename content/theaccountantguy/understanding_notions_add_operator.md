---
title: Understanding Notions add operator
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Adding two numbers together in [[notion_overview | Notion]] is a straightforward task that can be accomplished using the `add` operator <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## How to Find the Sum of Numbers in a Database

To find the [[different_methods_to_calculate_sums_in_notion | sum]] of numbers within a [[notion_overview | Notion database]], a three-step approach is followed <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:
1.  Create a [[notion_overview | database]] to hold the data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the [[notion_overview | database]] correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  Apply the desired [[using_formulas_to_add_numbers_in_notion | formula]] to find the [[different_methods_to_calculate_sums_in_notion | sum]] of two numbers <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### What is a Notion Database?

In [[notion_overview | Notion]], a [[notion_overview | database]] is a collection of structured and organized data <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a feature that enables users to create custom [[notion_overview | databases]] for storing, managing, and tracking information in an organized way <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. A [[notion_overview | Notion database]] consists of properties that define the types of data stored within it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

To add a [[notion_overview | database]] in [[notion_overview | Notion]], type `/database` and select "database inline" from the options <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Setting Up the Database Correctly

Every [[notion_overview | database]] in [[notion_overview | Notion]] includes a default property, which is the first column, always of type "title" and cannot be changed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

To find the [[different_methods_to_calculate_sums_in_notion | sum]] of two numbers, the [[notion_overview | database]] should include the following properties <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   Test title property <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 number property <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 number property <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 [[using_formulas_to_add_numbers_in_notion | Formula]] property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 [[using_formulas_to_add_numbers_in_notion | Formula]] property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

To add properties, click the plus symbol at the top right of the [[notion_overview | database]] and select the desired property type, such as "number" for "Paper 1" <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Finding the Sum of Two Numbers in Notion

Once the [[notion_overview | database]] is set up, two different [[using_formulas_to_add_numbers_in_notion | formulas]] can be used to find the [[different_methods_to_calculate_sums_in_notion | sum]] of two numbers <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### Formula One: Using the Plus Sign

This basic [[using_formulas_to_add_numbers_in_notion | formula]] adds all numbers together using the plus (`+`) sign <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

The [[using_formulas_to_add_numbers_in_notion | formula]] is structured as:
`prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

### Formula Two: Using the Add Function

[[notion_overview | Notion]] has a built-in operator, the `add` function, which also helps to find the [[different_methods_to_calculate_sums_in_notion | sum]] of numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function specifically helps to [[using_formulas_to_add_numbers_in_notion | add numbers]] together <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

The `add` operator takes two parameters as input and provides an output <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

Examples:
*   `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   `add("I love", "Notion")` equals `"I love Notion"` (demonstrates string concatenation) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

To [[using_formulas_to_add_numbers_in_notion | add numbers]] from "Paper 1" and "Paper 2" properties, the [[using_formulas_to_add_numbers_in_notion | formula]] is:
`add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>

Both `prop("Number 1") + prop("Number 2")` and `add(prop("Number 1"), prop("Number 2"))` are valid [[using_formulas_to_add_numbers_in_notion | formulas]] for finding the [[different_methods_to_calculate_sums_in_notion | sum]] of two numbers in a [[notion_overview | database]] <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.