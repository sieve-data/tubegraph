---
title: JavaScript function basics and anatomy
videoId: gigtS_5KOqo
---

From: [[fireship]] <br/> 

[[Functions and closures in JavaScript | Functions]] are considered the backbone of [[javascript_fundamentals_and_practical_concepts | JavaScript development]] and, while challenging to master, understanding them simplifies the rest of the language <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This article covers the fundamental aspects, from basic anatomy to advanced concepts like closures and recursion <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Anatomy of a Function Declaration

A common way to define a function in [[javascript_fundamentals_and_practical_concepts | JavaScript]] is through a function declaration, also known as a function definition or statement <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Its components include:
*   **`function` keyword**: The declaration begins with this keyword <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Name**: A readable name should be chosen for the function, as naming things is notoriously difficult in computer science <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Parentheses `()`**: These follow the function name <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Parameters**: Inputs to the function, defined within the parentheses <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. A parameter can be thought of as a [[variables_and_scope_in_javascript | variable]] the function can access when called <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Curly braces `{}`**: These enclose the function body, where the logic is defined <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Function Body Logic**: Typically performs a task, returns a value, or both <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
    *   Functions performing a task (e.g., `console.log`) without a `return` statement implicitly return `undefined` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
    *   A `return` statement explicitly sends a calculated value back from the function body, which can be stored in a [[variables_and_scope_in_javascript | variable]] <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

To execute a declared function, it must be *called* by referencing its name and passing actual values as arguments <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Parameters vs. Arguments

*   **Parameters**: The [[variables_and_scope_in_javascript | variable]] inputs used in the function definition <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Arguments**: The actual values or expressions used when calling the function <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## [[Function declarations vs expressions in JavaScript | Function Declarations vs. Expressions]]

In addition to named function declarations, [[functions_and_closures_in_javascript | JavaScript]] also has function expressions, which treat a function as a value <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. A function expression often uses an anonymous function (a function without a name) assigned to a [[variables_and_scope_in_javascript | variable]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Both produce identical results when called <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

Key difference: Hoisting <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
*   **Function Declarations**: Are *hoisted*, meaning they are moved to the top of their scope <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This allows them to be called even before they are declared in the code <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Function Expressions**: Are *not hoisted* <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. The function is not created until that part of the code is reached, leading to an error if called beforehand <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

While there's no universal best practice, many developers today prefer function expressions because:
*   Their non-hoisted nature makes it clearer where they belong in the application context <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   They are less likely to pollute the global namespace <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### Immediately Invoked Function Expressions (IIFEs)

An IIFE is an anonymous function wrapped in parentheses and immediately called by adding another set of parentheses afterwards <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This pattern allows for immediate execution and helps contain [[variables_and_scope_in_javascript | variables]] within their own scope.

## Handling Parameters

Arguments passed to functions can be managed in various ways:

*   **Positional Arguments**: When a function takes multiple arguments, their order matters <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This can become unmanageable with many arguments <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Named Parameters (using [[javascript_objects_and_their_properties | objects]])**: A common solution for functions with many parameters is to use a single [[javascript_objects_and_their_properties | object]] argument <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This [[javascript_objects_and_their_properties | object]] can then be destructured or used directly in the function body <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This approach removes the concern about argument order and offers flexibility for future extensions <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Rest Parameters**: Indicated by three dots (`...`) before a parameter name, rest parameters allow a function to accept an indefinite number of arguments as an array <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## [[Arrow functions and their benefits | Arrow Functions]]

[[Arrow functions and their benefits | Arrow functions]] offer a more compact and concise way to write functions in [[javascript_fundamentals_and_practical_concepts | JavaScript]] <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

Key characteristics:
*   **Syntax**: Defined using a [[variables_and_scope_in_javascript | variable]] name, parentheses for parameters, an arrow (`=>`), and the function body <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
*   **Implicit Return**: If the curly braces are omitted, the function implicitly returns the value of the expression <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. If curly braces are present, a `return` statement is still needed <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Expressions Only**: [[Arrow functions and their benefits | Arrow functions]] are always expressions, meaning they cannot be simply declared like traditional function declarations <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **No `this` Object**: A significant difference is that [[arrow functions and their benefits | arrow functions]] do not have their own `this` object <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Prior to [[arrow functions and their benefits | arrow functions]], every new function had its own `this` context, which led to patterns like assigning `this` to a `self` [[variables_and_scope_in_javascript | variable]] to maintain context <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. [[Arrow functions and their benefits | Arrow functions]] simplify this by lexically binding `this`, removing the need for such workarounds <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **Preference**: [[Arrow functions and their benefits | Arrow functions]] are generally preferred in modern [[javascript_fundamentals_and_practical_concepts | JavaScript]] where possible <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

## Pure Functions

A **pure function** is a concept from functional programming that emphasizes predictability and maintainability <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

*   **Impure Function**: A function that operates on values outside its local scope (e.g., modifying a global [[variables_and_scope_in_javascript | variable]]) <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. This can make code difficult to reason about <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Pure Function**:
    *   Only depends on its input parameters <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
    *   Only mutates [[variables_and_scope_in_javascript | variables]] within its local scope <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
    *   Does not produce any side effects (e.g., external state changes or I/O operations) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
    *   Will always produce the same output given the same inputs <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   Benefits: Easier to test and reason about, and helps in composing applications using [[functions_and_closures_in_javascript | higher-order functions]] <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## [[Functions and closures in JavaScript | Higher-Order Functions]]

[[javascript_fundamentals_and_practical_concepts | JavaScript]] supports first-class functions, meaning functions can be passed as arguments to other functions or returned as values from functions <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. A [[functions_and_closures_in_javascript | higher-order function]] is simply a function that either:
*   Takes other functions as input arguments <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   Returns a new function when called <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

Examples of [[functions and closures in javascript | higher-order functions]]:
*   **`setTimeout`**: A built-in [[javascript_fundamentals_and_practical_concepts | JavaScript]] function that takes a function as its first argument (a "callback function") and executes it after a specified delay <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   **`Array.prototype.map()`**: An array method that takes a function as an argument and calls it for each item in the array, transforming each item based on the function's return value <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. This is a functional alternative to traditional for loops, often combined with [[arrow functions and their benefits | arrow functions]] for concise code <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. While functional techniques can be less performant than `for` loops, this difference is usually negligible in most use cases <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## [[Functions and closures in JavaScript | Closures]]

Whenever a function is defined, it creates a **lexical environment** <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Anything inside curly braces (`{}`) forms its own lexical environment <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. An inner function's lexical environment includes its own local [[variables_and_scope_in_javascript | variables]] and a reference to its outer environment (including the outer function's [[variables_and_scope_in_javascript | variables]] and the global script) <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

This means:
*   An inner function can "remember" and access the local [[variables_and_scope_in_javascript | variables]] of its outer function <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   The outer function, however, cannot access the local [[variables_and_scope_in_javascript | variables]] of the inner function <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

A **closure** is created when an inner function retains access to the outer function's scope even after the outer function has finished executing. This concept is commonly encountered in [[javascript_fundamentals_and_practical_concepts | JavaScript]] interviews and real-world development <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

## Recursion

**Recursion** in [[javascript_fundamentals_and_practical_concepts | JavaScript]] involves a function calling itself within its own body <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. Each time the function calls itself, another instance is pushed onto the call stack <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.

*   **Stopping Condition**: A recursive function must have a stopping condition (also known as a base case) to prevent an infinite loop and a "Stack Overflow" error <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Practical Use**: Recursive algorithms are efficient for traversing tree-like data structures, such as a file system <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

Understanding these concepts is crucial for effective [[javascript_fundamentals_and_practical_concepts | JavaScript]] development, and consistent practice is key to mastering them <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.