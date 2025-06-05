---
title: Functional Programming with TypeScript
videoId: fsVL_xrYO0w
---

From: [[fireship]] <br/> 

Debating programming paradigms like object-oriented versus functional programming is compared to debating art, as there is always more than one way to solve a problem, especially in [[functions_and_closures_in_javascript | JavaScript]] <a class="yt-timestamp" data-t="01:13:54">[01:13:54]</a>. There are no absolutes, and every decision involves a trade-off <a class="yt-timestamp" data-t="01:21:40">[01:21:40]</a>. [[object_oriented_programming_with_typescript | Object-oriented]] or imperative approaches provide a clear set of statements to follow, while functional or declarative approaches describe the state and logic involved without dictating the control flow <a class="yt-timestamp" data-t="04:06:56">[04:06:56]</a>.

## Core Concepts of Functional Programming

### Pure Functions
The most important concept in [[pure_functions_in_functional_programming | functional programming]] is [[pure_functions_in_functional_programming | pure functions]] <a class="yt-timestamp" data-t="01:31:07">[01:31:07]</a>.
*   **Definition**: The output of a function should depend only on its inputs <a class="yt-timestamp" data-t="01:33:05">[01:33:05]</a>.
*   **Side-Effects**: Functional code should produce no side-effects, meaning it should not mutate variables directly or rely on any outside values to produce a return value <a class="yt-timestamp" data-t="01:46:17">[01:46:17]</a>. For example, mutating a `number` variable directly within a `toString` function would make it impure <a class="yt-timestamp" data-t="01:46:17">[01:46:17]</a>.
*   **Benefits**: [[pure_functions_in_functional_programming | Pure functions]] are easier to test and reason about because you don't have to consider anything happening outside the function itself <a class="yt-timestamp" data-t="01:59:42">[01:59:42]</a>.

### Immutable Data
Another core principle of [[pure_functions_in_functional_programming | functional programming]] is immutable data <a class="yt-timestamp" data-t="02:06:40">[02:06:40]</a>.
*   **Stateless**: Functional code is stateless, meaning that once data is created, it is never mutated <a class="yt-timestamp" data-t="02:09:59">[02:09:59]</a>.
*   **Simulation in JavaScript**: This can be simulated in [[functions_and_closures_in_javascript | JavaScript]] using `Object.freeze` on an array of numbers, which prevents operations like `array.push` that would mutate the data <a class="yt-timestamp" data-t="02:14:60">[02:14:60]</a>.

## Functions as First-Class Citizens

In [[pure_functions_in_functional_programming | functional programming]], functions are often passed as arguments to other functions, especially in dynamic software applications where data must change <a class="yt-timestamp" data-t="02:27:08">[02:27:08]</a>.

### First-Order Functions
A typical first-order function takes a value and returns a different value, such as appending an emoji to a string <a class="yt-timestamp" data-t="02:34:04">[02:34:04]</a>.

### Higher-Order Functions
A higher-order function either takes a function as an argument or returns a function itself <a class="yt-timestamp" data-t="02:44:03">[02:44:03]</a>.
*   [[functions_and_closures_in_javascript | JavaScript]] has built-in higher-order functions for [[working_with_functions_and_arrays_in_typescript | arrays]] like `map` <a class="yt-timestamp" data-t="02:48:42">[02:48:42]</a>.
*   Instead of `for` loops, a function can be passed to `map`, which will run it on every element in an array and transform the value, providing a concise and elegant way to transform array values <a class="yt-timestamp" data-t="02:53:23">[02:53:23]</a>.

### Functions that Return Functions
Creating functions that return functions is useful for starting with base functionality and extending it with dynamic data <a class="yt-timestamp" data-t="03:07:37">[03:07:37]</a>.
*   This allows for composing more complex functions from a base function <a class="yt-timestamp" data-t="03:21:04">[03:21:04]</a>.
*   The inner function takes arguments and combines them <a class="yt-timestamp" data-t="03:27:06">[03:27:06]</a>.
*   This leads to specialized functions that point to specific data, resulting in concise and readable code that does not rely on shared state, making it easier to test <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

Functional programming becomes more complex and interesting when dealing with asynchronous data and side-effects <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.