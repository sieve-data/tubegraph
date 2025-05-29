---
title: Subtract operator in Notion
videoId: Fz_fpiT29EE
---

From: [[theaccountantguy]] <br/> 

To find the difference between two numbers in Notion, you can utilize two distinct methods involving [[using_formulas_in_notion | formulas]]: the `subtract` operator or the [[minus_sign_usage_in_notion | minus sign]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Setting Up Your Database

First, you need to create a database in Notion <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This can be done by typing a forward slash (`/`) and then `database` to bring up the list of options <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

Within your database:
*   The first property will typically be a title property, indicating the purpose of the entry <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   You will then need to assign `Number` properties to two different fields, which will contain the numbers you wish to find the difference between <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Using the Subtract Operator

To find the difference, add a new `Formula` property to your database <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Within this [[using_formulas_in_notion | formula]] property, you can use the `subtract` operator.

The `subtract` operator is designed to take two numbers as input and calculate the difference between them <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, if you have two number properties named `Number 1` and `Number 2`, the formula would look like `subtract(prop("Number 1"), prop("Number 2"))` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Using the Minus Sign

Alternatively, you can achieve the same result using the [[minus_sign_usage_in_notion | minus sign]] (`-`) within a [[using_formulas_in_notion | Notion formula]] <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This method is often more concise. For instance, the formula `prop("Number 1") - prop("Number 2")` would also yield the difference between the two numbers.

By implementing either the `subtract` operator or the [[minus_sign_usage_in_notion | minus sign]], you can effectively find the difference between two numbers within a Notion database <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.