---
title: Creating a database in Notion for calculations
videoId: Fz_fpiT29EE
---

From: [[theaccountantguy]] <br/> 

This article outlines how to find the difference between two numbers within a [[notion_database_setup_for_calculations | Notion database]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Two distinct methods are used for this calculation: the subtract operator and the minus sign <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## [[setting_up_a_database_in_notion | Setting Up the Database]]

To begin, you need to [[how_to_create_a_database_in_notion | create a database]] in Notion <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

1.  Type a forward slash (`/`) and then "database" to access the list of options <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
2.  The initial property created is typically a title property, which serves to identify the record <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
3.  Add two number properties to the database, which will be used to input the numbers for which you want to find the difference <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Finding the Difference Using Formulas

Once your database is set up with the necessary number properties, you can add a formula property to perform calculations.

### Using the Subtract Operator

One way to find the difference is by employing the `subtract` operator in a formula property <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This operator takes two numbers as input and calculates their difference <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

*   **Formula Structure:** `subtract(Number_One, Number_Two)`
*   **Example:** If your number properties are named "Number One" and "Number Two", the formula would be `subtract(prop("Number One"), prop("Number Two"))` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### Using the Minus Sign

Alternatively, you can use the standard minus sign (`-`) in a formula property to achieve the same result <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

*   **Formula Structure:** `Number_One - Number_Two`
*   **Example:** Following the previous example, the formula would be `prop("Number One") - prop("Number Two")` <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

These methods demonstrate how to effectively calculate the difference between two numbers within a [[notion_database_setup_for_calculations | Notion database]] <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.