---
title: Variable declaration and scope in JavaScript
videoId: lkIFF4maKMU
---

From: [[fireship]] <br/> 

JavaScript offers multiple ways to declare variables, each with specific rules regarding their reassignment and accessibility within different parts of the code, known as their scope <a class="yt-timestamp" data-t="03:29:13">[03:29:13]</a>.

## Declaring Variables

Variables are fundamental building blocks in JavaScript for storing data.

### `let` Keyword
The `let` keyword is the most common way to define a variable in modern JavaScript <a class="yt-timestamp" data-t="02:17:34">[02:17:34]</a>.
*   Variables declared with `let` are typically named in camel case <a class="yt-timestamp" data-t="02:20:25">[02:20:25]</a>.
*   JavaScript is a dynamically typed language, meaning no explicit [[javascript_data_types_and_control_flow | data type]] annotations are required when assigning a value <a class="yt-timestamp" data-t="02:24:28">[02:24:28]</a>.
*   If a variable is declared with `let` but not immediately assigned a value, it defaults to the primitive value `undefined` <a class="yt-timestamp" data-t="02:39:10">[02:39:10]</a>.
*   An explicitly empty value can be represented using `null` <a class="yt-timestamp" data-t="02:45:03">[02:45:03]</a>.
*   Variables declared with `let` can be reassigned later to a different value, even if it's an entirely different [[javascript_data_types_and_control_flow | data type]] <a class="yt-timestamp" data-t="02:37:10">[02:37:10]</a>, <a class="yt-timestamp" data-t="02:49:03">[02:49:03]</a>.

### `const` Keyword
The `const` keyword is used for variables that are intended to remain unchanged and cannot be reassigned after their initial declaration <a class="yt-timestamp" data-t="03:14:38">[03:14:38]</a>.

### `var` Keyword (Legacy)
Historically, `var` was the original way to declare variables <a class="yt-timestamp" data-t="03:19:35">[03:19:35]</a>. However, it is generally recommended to avoid using `var` in new code due to its peculiar scoping behavior <a class="yt-timestamp" data-t="03:22:15">[03:22:15]</a>.

### Semicolons
Semicolons at the end of statements are technically optional in JavaScript. If omitted, the JavaScript parser automatically adds them <a class="yt-timestamp" data-t="03:01:21">[03:01:21]</a>.

## [[variables_and_scope_in_javascript | Variable Scope]]

[[variables_and_scope_in_javascript | Variable scope]], determined by the lexical environment, dictates where variables are accessible within the code <a class="yt-timestamp" data-t="03:28:10">[03:28:10]</a>.

### Global Scope
Variables declared in the global scope are available throughout the entire program <a class="yt-timestamp" data-t="03:34:25">[03:34:25]</a>.

### Function (Local) Scope
When a variable is defined inside a [[javascript_function_basics_and_anatomy | function]], it becomes local to that [[javascript_function_basics_and_anatomy | function]] and cannot be accessed from outside it <a class="yt-timestamp" data-t="03:39:17">[03:39:17]</a>.

### Block Scope
With `let` and `const`, variables can be scoped within code blocks, such as those defined by `if` conditions or loops <a class="yt-timestamp" data-t="03:45:15">[03:45:15]</a>. They are only accessible within those braces.

### `var` and Hoisting
Unlike `let` and `const`, `var` is not block-scoped. Variables declared with `var` are "hoisted" up into the nearest [[javascript_function_basics_and_anatomy | function]]'s local scope, which can lead to unexpected behavior and is generally undesirable <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

## Variable Values and Data Types

*   JavaScript has seven primitive [[javascript_data_types_and_control_flow | data types]], such as numbers and strings <a class="yt-timestamp" data-t="02:29:10">[02:29:10]</a>, <a class="yt-timestamp" data-t="02:50:35">[02:50:35]</a>.
*   Any value that is not a primitive will inherit from the `object` class <a class="yt-timestamp" data-t="02:54:25">[02:54:25]</a>.

## Passing Arguments

When variables are passed as arguments to a [[javascript_function_basics_and_anatomy | function]]:
*   **Pass by Value**: Primitive [[javascript_data_types_and_control_flow | data types]] (like numbers) are passed by value, meaning a copy of the original variable is created for the [[javascript_function_basics_and_anatomy | function]] <a class="yt-timestamp" data-t="05:27:53">[05:27:53]</a>.
*   **Pass by Reference**: Objects are passed by reference, as they are stored in the Heap memory. This means that multiple parts of the code might be mutating the same object, which can have implications for program behavior <a class="yt-timestamp" data-t="05:35:46">[05:35:46]</a>.