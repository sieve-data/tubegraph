---
title: Variables and data types in JavaScript
videoId: lkIFF4maKMU
---

From: [[fireship]] <br/> 

[[JavaScript basics and history | JavaScript]] is a programming language that allows developers to build almost anything <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. When learning [[JavaScript basics and history | JavaScript]], understanding variables and data types is fundamental.

## Defining Variables

In [[JavaScript basics and history | JavaScript]], variables are used to store data. There are several ways to define variables <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

### `let` Keyword
The `let` keyword is the most common way to define a variable in modern [[JavaScript basics and history | JavaScript]] <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
Variables declared with `let` are typically named in camel case <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
[[JavaScript language quirks | JavaScript]] is a dynamically typed language, meaning data type annotations are not necessary <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. A `let` variable can be assigned a value later, and if no value is assigned initially, it defaults to the primitive value `undefined` <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. An empty value can also be explicitly represented using `null` <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. The same `let` variable can be reassigned to an entirely different data type later in the code <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

### `const` Keyword
`const` is another common option for defining variables <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. It is used for variables that cannot be reassigned after their initial declaration <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

### `var` Keyword
Historically, `var` was the original way to declare a variable <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. It is generally recommended to ignore its existence altogether in modern [[JavaScript basics and history | JavaScript]] development <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>, although it may still be encountered in existing codebases <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

## Scope of Variables

The reason for different variable declaration methods relates to the lexical environment, which determines where variables are accessible <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

*   **Global Scope**: Variables defined in the global scope are available everywhere in the program <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
*   **Function Scope**: Variables defined inside a function are local to that function and cannot be used outside of it <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
*   **Block Scope**: Variables declared with `let` or `const` inside a statement block (like an `if` condition or loop) are scoped within those braces <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. In contrast, `var` is not block-scoped; it will be "hoisted" up into the local function scope, which can lead to unexpected behavior <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

## Data Types

[[JavaScript language quirks | JavaScript]] is a dynamically typed language, meaning data types are not explicitly declared <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

### Primitive Data Types
There are seven primitive data types built into the language <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>:
*   **Number**: Used for numerical values <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **Undefined**: The default value for variables that have been declared but not yet assigned a value <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
*   **Null**: Represents the explicit absence of any object value <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **String**: Represents textual data <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

### Objects
Any value that is not a primitive data type will inherit from the `Object` class <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. Objects in [[JavaScript basics and history | JavaScript]] are collections of key-value pairs (properties and values) <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

### Passing Arguments
When passing arguments to [[Functions and closures in JavaScript | functions]]:
*   A primitive value (like a number) is passed **by value**, meaning a copy of the original variable is created <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   An object is passed **by reference**, meaning it's stored in the Heap memory, and multiple parts of the code might mutate the same object <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Semicolons
Technically, semicolons in [[JavaScript basics and history | JavaScript]] are optional because the parser will automatically add them if left out <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. However, whether or not to use semicolons is a topic of frequent debate among developers <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.