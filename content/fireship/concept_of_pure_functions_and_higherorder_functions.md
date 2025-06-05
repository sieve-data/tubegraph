---
title: Concept of pure functions and higherorder functions
videoId: gigtS_5KOqo
---

From: [[fireship]] <br/> 

[[JavaScript fundamentals and practical concepts | Functions]] are considered the backbone of [[JavaScript highlevel features | JavaScript]] development and are a fundamental concept to master, as understanding them makes other aspects of the language relatively easy to grasp <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This article will explore the concepts of [[pure_functions_in_functional_programming | pure functions]] and higher-order functions.

## [[pure_functions_in_functional_programming | Pure Functions]]

A key concept promoted by industry thought leaders is the value of [[pure_functions_in_functional_programming | pure functions]] <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Impure Functions

An impure function is characterized by its reliance on, and modification of, values outside its local scope, such as global variables <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This dependency on and mutation of external variables makes the code difficult to manage and can lead to unpredictable behavior <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

### Definition of a Pure Function

A [[pure_functions_in_functional_programming | pure function]] is defined by the following characteristics <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>:
*   It only depends on its input parameters <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   It only mutates variables within its local scope <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   It does not produce any side effects <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

### Benefits of Pure Functions

Code written with [[pure_functions_in_functional_programming | pure functions]] consistently yields the same output given the same inputs <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This makes the code easier to test and generally simpler to reason about <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Furthermore, [[pure_functions_in_functional_programming | pure functions]] facilitate the composition of applications using collections of higher-order functions <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Higher-Order Functions

[[JavaScript highlevel features | JavaScript]] supports [[Functional Programming with TypeScript | first-class functions]], meaning functions can be treated as values <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This enables them to be passed as arguments to other functions or returned as values from functions <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

The term "higher-order function" (or "higher-order component" in frameworks like React) refers to functions that meet one or both of these criteria <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>:
*   They take other functions as input arguments <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   They return a new function when called <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

### Functions as Arguments

Passing functions as arguments is a common pattern in [[JavaScript highlevel features | JavaScript]], especially in asynchronous programming <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

#### `setTimeout` Example
A simple example of a higher-order function is `setTimeout`, which is built into [[JavaScript highlevel features | JavaScript]] <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. It executes a function after a specified delay <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. `setTimeout` takes a function as its first argument (known as a "callback function") and the delay time as the second argument <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. The [[JavaScript highlevel features | JavaScript]] engine will call this function later, not immediately <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

#### Array `map` Method
[[Functional Programming with TypeScript | Functional programming]] also offers alternatives to traditional for loops <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. The `map` method for arrays is a higher-order function that transforms each item in an array <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. It takes a function as its argument, which is then called for each item in the array, with the function's return value becoming the new transformed item <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. This can be combined with [[functions_closures_and_the_concept_of_this | arrow functions]] for concise, single-line transformations <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. While powerful, these [[Functional Programming with TypeScript | functional techniques]] may be less performant than a standard for loop, though this difference is often negligible in most use cases <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### Functions Returning Functions (Closures)

Another type of higher-order function is one that returns a function <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. When a function is defined, it creates a "lexical environment" <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   Anything within curly braces `{}` constitutes its own lexical environment <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   An inner function has its own lexical environment, including its local variables, and a reference to the outer environment (which includes the outer function and the global script) <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   This means an inner function can "remember" and access the local variables of its outer function <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. Conversely, the outer function cannot access the local variables of the inner function <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

This concept is crucial for understanding [[functions_closures_and_the_concept_of_this | closures]], which are common in [[JavaScript highlevel features | JavaScript]] interviews and real-world applications <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. A common application of [[functions_closures_and_the_concept_of_this | closures]] is seen in patterns like React Hooks, where an outer function defines and maintains local variables that are then accessed and modified by functions returned from it <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

### Recursion

Recursion is another concept where a function calls itself by name within its own body <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. A recursive function must have a "stopping condition" to prevent an infinite loop and a "Stack Overflow" error <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Recursive algorithms are particularly efficient for traversing tree-like data structures, such as a file system <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.