---
title: Using formulas in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

[[Formulas in Notion | Formulas]] in Notion enable users to perform calculations and manipulate data within databases, similar to [[using_excellike_formulas_in_notion | Excel-like formulas]]. A common application is to [[adding_numbers_in_notion | add numbers in Notion]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This can be achieved using the `ADD` operator or a simple plus sign <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

To find the sum of numbers in a Notion database, a three-step approach can be followed <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>:
1.  Create a database <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
2.  Set up the database correctly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
3.  [[Applying formula for multiplication in Notion | Apply the desired formula]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Step 1: How to Create a Database in Notion

A database in Notion is a structured collection of data, allowing users to organize and track information <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It consists of various properties that define the types of data stored <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

To add a database:
1.  Type `/database` on a Notion page <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  Select `Database - Inline` from the options to quickly add it to your page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Step 2: Setting Up the Database Correctly

Every Notion database includes a default property as its first column, which is always of the `Title` type and cannot be changed <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. For [[adding_numbers_in_notion | adding two numbers]], the database requires specific properties <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>:

*   **Test Title Property:** The default `Title` property <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Paper 1 Number Property:** A number property for the first number <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Paper 2 Number Property:** A number property for the second number <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Formula 1 Formula Property:** A formula property for the first calculation method <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Formula 2 Formula Property:** A formula property for the second calculation method <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### How to Add Properties in a Database

To add properties:
1.  Click the plus `+` symbol at the top right of the database <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
2.  Choose the desired property type from the list <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For numerical addition, select the `Number` property (e.g., "Paper 1") and then `Formula` properties <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## Step 3: Finding the Sum of Two Numbers in Notion

Once the database is set up with the necessary properties, you can [[implementing_excellike_formulas_in_notion | implement Notion formulas]] to calculate sums <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Formula 1: Using the Addition Operator

This basic formula uses the plus `+` sign to add numbers together <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
```notion
prop("Paper 1") + prop("Paper 2")
```
This formula adds the values from the "Paper 1" and "Paper 2" number properties <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### Formula 2: Using the `add` Function

Notion also includes a built-in `add` function specifically for [[adding_numbers_in_notion | adding numbers]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The `add` function takes two parameters as input <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

**Examples:**
*   `add(1, 3)` will result in `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   `add("I love", " Notion")` will result in `"I love Notion"` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

To [[adding_numbers_in_notion | add the two numbers]] (Paper 1 and Paper 2) using this function:
```notion
add(prop("Paper 1"), prop("Paper 2"))
```
This formula will achieve the same result as the `+` operator for numerical addition <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

By [[creating_and_saving_custom_formulas_in_notion | creating and saving custom formulas]] and [[troubleshooting_and_updating_formulas_in_notion | understanding these approaches]], users can effectively perform calculations and manipulate data in their Notion databases <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. These methods are fundamental [[examples_of_questions_for_notion_formulas | examples of how Notion formulas]] can be used. For more advanced operations, consider [[using_rollup_and_formula_properties_in_notion | using rollup and formula properties]] together.