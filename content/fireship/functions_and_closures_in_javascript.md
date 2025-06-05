---
title: Functions and closures in JavaScript
videoId: lkIFF4maKMU
---

From: [[fireship]] <br/> 

Functions are fundamental building blocks in [[JavaScript basics and history | JavaScript]] that take input (arguments) and optionally return a value <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.

## Function Definitions and Expressions

When the `function` keyword is used by itself, it creates a function definition or statement <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. Functions in [[JavaScript language quirks | JavaScript]] are also considered objects, which means they can be used as expressions <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. This allows them to be assigned to [[variables_and_data_types_in_javascript | variables]] or used in higher-order functions <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.

### Arrow Functions
[[Modern JavaScript array methods | Modern JavaScript]] provides an alternative way to define functions using the arrow syntax <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. Arrow functions are always anonymous and do not have their own `this` value, making them suitable for function expressions <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.

## Arguments and `this` Keyword

When passing arguments to a function, a primitive value (like a number) is passed by value, meaning a copy of the original [[variables_and_data_types_in_javascript | variable]] is created <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>. However, if the argument is an object, it's stored in the Heap memory and passed by reference, allowing multiple parts of the code to potentially mutate the same object <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.

The `this` keyword inside a function references an object based on how the function is called <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.
*   When called from the global scope in a browser, `this` references the `window` object <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
*   If a function is attached to and called by an object, `this` will be a reference to that object <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
*   Functions can also be manually bound to an object using the `bind` method <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.

## Closures

Functions can be nested, which allows for the creation of a closure <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>. A closure encapsulates data and logic, isolating it from the rest of the program <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.

Normally, when a function with a primitive [[variables_and_data_types_in_javascript | variable]] is called, that variable is stored on the call stack (the browser's short-term memory) <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. With a closure, the inner function can still access [[variables_and_data_types_in_javascript | variables]] in the outer function, even after the initial function call has completed <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. This occurs because [[JavaScript language quirks | JavaScript]] automatically stores the data from the outer function in the Heap memory, which persists between function calls <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.