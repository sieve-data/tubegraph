---
title: Understanding and setting property types in Notion databases
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

Notion databases are designed to be a flexible collection of data that can be structured and organized in various ways <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. They are a powerful feature, allowing users to create custom databases to store, manage, and track information in an organized manner <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. A Notion database is fundamentally composed of a collection of properties, which define the different types of data that can be stored within it <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.

## [[creating_a_database_in_notion | Creating a Database in Notion]]

To [[creating_a_database_in_notion | create a database]] in Notion, simply type `/database` into your page <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. This will provide a list of options for adding a database <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. Selecting "database inline" allows you to quickly add a database to your Notion page <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

## Setting Up Database Properties

Once a database is [[creating_and_setting_up_a_database_in_notion | created]], the next step is to set up its properties correctly <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.

### Default Property: Title

When [[creating_and_managing_a_database_in_notion | any database is created]] in Notion, it will always include a default property as its first column <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. This property is always of the "Title" type, and its type cannot be changed <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. For example, this column might be used for a "test name" or "test title" <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

### Adding New Properties

To [[creating_database_in_notion | add properties]] to a database in Notion, click on the plus (`+`) symbol located at the top right end of the database <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. Upon selection, a list of options will appear, allowing you to choose the desired property type <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

Common property types mentioned for calculations include:

*   **Number Property**: Used to store numerical data <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. For instance, you could select the "Number" property type and name it "Paper 1" <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.
*   **Formula Property**: Used to perform calculations or display dynamic content based on other properties <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>. To add a formula property, select "Formula" as the property type <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.

### Using Formulas with Properties

Notion's formula properties allow for calculations using values from other properties within the same database <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. Here are two examples for adding numbers:

1.  **Direct Addition with `prop`**: This basic formula adds all numbers together using the plus (`+`) sign <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>. For example, to sum "Paper 1" and "Paper 2" properties, the formula would be `prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.
2.  **Using the `add` function**: Notion also provides a built-in `add` function, which specifically helps to add two numbers <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>. The `add` function takes two parameters as input <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>. For example, `add(prop("Paper 1"), prop("Paper 2"))` would achieve the same sum <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.

By understanding how to [[creating_a_database_in_notion | create]] and [[establishing_relationships_between_databases_in_notion | set up properties]] in Notion databases, users can effectively [[using_notion_for_templates_and_databases | manage and organize]] their information, including performing calculations via formula properties.