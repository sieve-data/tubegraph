---
title: Basic syntax and features of Lua
videoId: jUuqBZwwkQw
---

From: [[fireship]] <br/> 

[[Introduction to Lua programming | Lua]] is a fast, multi-paradigm scripting language, often considered underrated <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It is designed to be easier to learn than Python, while also being faster and more portable <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Created in 1993 by a team of computer scientists in Brazil, the language was named after the moon <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Core Characteristics
Lua is lightweight and extremely fast <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Its virtual machine maps very closely to [[C language characteristics and usage | C]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. When used with its Just-in-Time (JIT) compiler, it is widely considered the fastest scripting language in the world <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This makes [[Benefits and applications of Lua | Lua ideal for embedding]] into other applications, such as World of Warcraft or Roblox, where users can write Lua to build their own games and features <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Language Simplicity
Lua's ease of learning stems from its design:
*   It has only 21 reserved words <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   It is a dynamic language, so no type annotations are required <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   There are no classes in Lua; functionality is achieved using functions and tables <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Basic Syntax

### Getting Started
To begin with Lua, one typically installs the interpreter and creates a file ending in `.lua` <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Variables
Variables are declared by providing a name and a value <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. By default, variables are global, but they can be made local using the `local` keyword <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
To output a value to the standard output, the `print` function is used <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Functions
Functions are declared using the `function` keyword and closed with the `end` keyword <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Functions in Lua are first-class objects, meaning they can be passed to other functions to support functional programming patterns <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Data Structures: Tables
Lua has only one data structuring mechanism: [[Lua tables and data structures | tables]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. A table is created with braces `{}` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

A table is an associative array, where the index can be replaced with different values <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. By default, it uses integer values, and uniquely, Lua starts array indexing at `1` instead of `0` like most languages <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

Tables can represent various data structures:
*   **Arrays**: Using default integer keys <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Dictionaries**: By giving keys a string value <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   Graphs <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
*   Trees <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

Looping over key-value pairs in a table can be done with a `for` loop <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Concurrency: Coroutines
Although Lua is single-threaded, it supports collaborative multitasking through co-routines <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Co-routines allow functions to be paused (`yield`) and resumed (`resume`) at different points in the code <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Ecosystem
Lua has a very minimal standard library <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, but it boasts a large ecosystem of packages managed by the Luarocks package manager <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## C API
Lua offers a very simple [[C language characteristics and usage | C]] API <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This API allows Lua code to be executed within a [[C language characteristics and usage | C]] program, and conversely, [[C language characteristics and usage | C]] code can be run from a Lua program <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Execution
To execute Lua code, one typically opens a terminal and runs the Lua interpreter <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.