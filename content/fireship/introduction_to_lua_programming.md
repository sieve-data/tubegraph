---
title: Introduction to Lua programming
videoId: jUuqBZwwkQw
---

From: [[fireship]] <br/> 

Lua is a fast, multi-paradigm scripting language that is often considered underrated <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is designed to be easier to learn than [[introduction_to_python | Python]], while also offering greater speed and portability <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Overview and History
Named after the moon, Lua was created in 1993 by a team of computer scientists in Brazil <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It is lightweight and exceptionally fast because its virtual machine closely maps to [[getting_started_with_c_programming | C]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. When used with its Just-in-Time (JIT) compiler, Lua is widely regarded as the fastest scripting language globally <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## [[benefits_and_applications_of_lua | Key Features and Applications]]
Lua is ideal for embedding into other applications <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. For example, it's used in games like World of Warcraft and Roblox, where users can write Lua code to build custom games and features <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

Key characteristics include:
*   **Ease of Learning** <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>: It's easy to learn, featuring only 21 reserved words <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Unified Data Structure** <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>: Lua has a single data structuring mechanism called a "table," which can represent arrays, dictionaries, graphs, trees, and more <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Coroutines** <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>: It supports collaborative multitasking through co-routines <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Ecosystem** <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>: While its standard library is minimal, Lua boasts a large ecosystem of packages accessible via the Luarocks package manager <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## [[basic_syntax_and_features_of_lua | Basic Syntax and Features]]

To begin, install Lua and create a file ending with `.lua` <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Variables
Variables are declared by providing a name and a value <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. By default, variables are global, but you can make them local using the `local` keyword <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Lua is a dynamic language, so type annotations are not required <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
To output a value to the standard output, use the `print` function <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

```lua
-- Example
local myVariable = "Hello, Lua!" -- Declares a local variable
print(myVariable) -- Outputs: Hello, Lua!
```

### Functions
Lua does not have classes, but functionality can be achieved using functions and tables <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Functions are declared with the `function` keyword and closed with the `end` keyword <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Functions are first-class objects, meaning they can be passed to other functions, supporting functional programming patterns <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

```lua
function greet(name)
    return "Hello, " .. name .. "!"
end

print(greet("World")) -- Outputs: Hello, World!
```

### Tables
Tables are used to structure data and are created with braces `{}` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. A table is an associative array, allowing indices to be replaced with different values <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. By default, tables use integer values, and curiously, they start indexing at 1 instead of 0 like most other languages <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This allows for conventional arrays <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Dictionaries can be created by giving keys a string value <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

```lua
-- Array-like table (1-based indexing)
local myArray = {"apple", "banana", "cherry"}
print(myArray[1]) -- Outputs: apple

-- Dictionary-like table
local myDictionary = {
    name = "Lua",
    type = "scripting language"
}
print(myDictionary.name) -- Outputs: Lua
```

### Looping
The `for` loop can be used to iterate over every key-value pair in a table <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

```lua
for key, value in pairs(myDictionary) do
    print(key .. ": " .. value)
end
-- Outputs:
-- name: Lua
-- type: scripting language
```

### Coroutines
Although Lua is single-threaded, coroutines allow you to pause and resume a function's execution <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. You create a coroutine and use `yield` to suspend its execution <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Elsewhere in the code, `coroutine.resume` continues execution until a `return` statement is reached <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## [[lowlevel_systems_programming_languages | C API Integration]]
For [[getting_started_with_c_programming | C]] programmers, Lua offers a very simple C API <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This API enables running Lua code within a C program, or conversely, executing C code from a Lua program <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Executing Lua Code
To execute your Lua code, open a terminal and run the Lua interpreter <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.