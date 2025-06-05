---
title: Lua tables and data structures
videoId: jUuqBZwwkQw
---

From: [[fireship]] <br/> 

[[Introduction to Lua programming | Lua]] is a fast, multi-paradigm scripting language known for being lightweight and extremely fast <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It was designed in Brazil in 1993 and is considered one of the fastest scripting languages globally, especially when used with its Just-in-Time compiler <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This makes it ideal for embedding into other applications, such as World of Warcraft or Roblox, where users can build their own games and features using [[Basic syntax and features of Lua | Lua]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

[[Benefits and applications of Lua | Lua]] is easy to learn, featuring only 21 reserved words <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## The Universal Table: Lua's Data Structuring Mechanism

A unique aspect of [[Basic syntax and features of Lua | Lua]] is that it has only one [[Data Structures and Algorithms | data structuring mechanism]] called a *table* <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This single mechanism is remarkably versatile, capable of representing various [[Data Structures and Algorithms | data structures]] including:
*   Arrays <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   Dictionaries <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   Graphs <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
*   Trees <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

Unlike many other languages, [[Basic syntax and features of Lua | Lua]] does not have classes; however, anything imaginable can be accomplished using a combination of functions and tables <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Creating and Understanding Tables

Tables are created using braces `{}` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Fundamentally, a table in [[Basic syntax and features of Lua | Lua]] is an associative array, meaning that the index in the array can be replaced with different values <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

#### Tables as Conventional Arrays
By default, tables use integer values for their indices <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. A peculiar characteristic of [[Basic syntax and features of Lua | Lua]] is that its table indices start at one, unlike most programming languages that begin at zero <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This default behavior allows tables to function as conventional arrays <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

#### Tables as Dictionaries (Hash Maps)
Tables can also easily function as dictionaries (or hash maps) by assigning string values to the keys <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This allows for iterating over every key-value pair within the table using a `for` loop <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.