---
title: Creating a database in Notion
videoId: WFKrfFfxyYo
---

From: [[theaccountantguy]] <br/> 

A [[setting_up_and_using_databases_in_notion | database]] in Notion is a collection of structured and organized data <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It's a powerful feature allowing users to [[creating_and_setting_up_a_notion_database | create custom databases]] to store, manage, and track information <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. A Notion [[setting_up_and_using_databases_in_notion | database]] is composed of properties that define the types of data stored within it <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## How to Create a Database

To add a [[setting_up_and_using_databases_in_notion | database]] in Notion, type `/database` to view a list of options <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Selecting "database inline" allows for quick [[creating_and_setting_up_a_notion_database | database creation]] on your Notion page <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Setting Up Database Properties

When [[creating_and_setting_up_a_notion_database | creating a database]], there is always a default property, which is the first column, named "Title" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This property type cannot be changed <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

To [[setting_up_notion_database_properties | add additional properties]] to a [[setting_up_and_using_databases_in_notion | database]], click on the plus symbol located at the top right of the [[setting_up_and_using_databases_in_notion | database]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This presents a list of options for [[setting_up_notion_database_properties | property types]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Example: Setting Up for Summing Numbers

For an example of finding the sum of two numbers, the following properties are required <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   Test Title property (the default Title column) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Paper 1 [[creating_a_database_with_number_properties_in_notion | number property]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
*   Paper 2 [[creating_a_database_with_number_properties_in_notion | number property]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Formula 1 Formula property <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
*   Formula 2 Formula property <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

To add the number properties, select the "number" property type and name it "Paper 1", then repeat for "Paper 2" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Add two more properties and set their type as "Formula" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Formulas for Summing Numbers

Once the [[setting_up_and_using_databases_in_notion | database]] is set up, formulas can be used <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
Two methods for summing numbers:

1.  **Direct Addition**: Use the plus sign (`+`) to add numbers <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   Example formula: `prop("Paper 1") + prop("Paper 2")` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

2.  **`add` Function**: Notion has a built-in `add` function <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `add` function takes two parameters and returns their sum <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
    *   Example: `add(1, 3)` equals `4` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   Example formula: `add(prop("Paper 1"), prop("Paper 2"))` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>