---
title: Pure Functions in Functional Programming
videoId: fsVL_xrYO0w
---

From: [[fireship]] <br/> 

The most important concept in [[functional_programming_with_typescript | functional programming]] is the [[concept_of_pure_functions_and_higherorder_functions | concept of pure functions]] <a class="yt-timestamp" data-t="01:29:43">[01:29:43]</a>.

## Characteristics of Pure Functions

*   **Input-dependent output** <a class="yt-timestamp" data-t="01:32:04">[01:32:04]</a>: The output of a function should exclusively depend on its inputs <a class="yt-timestamp" data-t="01:36:38">[01:36:38]</a>. For instance, a `toString` function takes a value as an argument and returns that value formatted as a string <a class="yt-timestamp" data-t="01:37:40">[01:37:40]</a>.
*   **No Side-Effects** <a class="yt-timestamp" data-t="01:50:56">[01:50:56]</a>: Functional code should not produce any side-effects <a class="yt-timestamp" data-t="01:51:56">[01:51:56]</a>. Mutating a variable directly, such as a number variable, would make a function impure <a class="yt-timestamp" data-t="01:46:01">[01:46:01]</a>.
*   **No reliance on outside values** <a class="yt-timestamp" data-t="01:55:04">[01:55:04]</a>: Pure functions should not depend on any external values to produce their return value <a class="yt-timestamp" data-t="01:56:56">[01:56:56]</a>.
*   **Immutable Data** <a class="yt-timestamp" data-t="02:07:05">[02:07:05]</a>: A core principle of [[functional_programming_with_typescript | functional programming]] is immutable data <a class="yt-timestamp" data-t="02:07:05">[02:07:05]</a>. This means that data, once created, is never mutated <a class="yt-timestamp" data-t="02:11:03">[02:11:03]</a>. In [[javascript_fundamentals_and_practical_concepts | JavaScript]], this can be simulated using `Object.freeze` on an array <a class="yt-timestamp" data-t="02:16:11">[02:16:11]</a>, which prevents operations like `array.push` that would mutate the data <a class="yt-timestamp" data-t="02:22:24">[02:22:24]</a>.

## Benefits of Pure Functions

*   **Easier to test** <a class="yt-timestamp" data-t="01:59:45">[01:59:45]</a>: Pure functions are simpler to test <a class="yt-timestamp" data-t="01:59:45">[01:59:45]</a>.
*   **Easier to reason about** <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>: They are easier to understand because there's no need to consider anything happening outside the function itself <a class="yt-timestamp" data-t="02:02:13">[02:02:13]</a>.
*   **Concise and Readable Code** <a class="yt-timestamp" data-t="03:44:27">[03:44:27]</a>: Pure functions contribute to concise and readable code <a class="yt-timestamp" data-t="03:44:27">[03:44:27]</a>.
*   **Stateless** <a class="yt-timestamp" data-t="03:46:06">[03:46:06]</a>: Code built with pure functions does not rely on any shared state, which makes it easier to test <a class="yt-timestamp" data-t="03:46:06">[03:46:06]</a>.

Even within [[object-oriented programming]] concepts, a static method on a class can be a [[concept_of_pure_functions_and_higherorder_functions | pure function]] if its job is simply to add one to an input argument <a class="yt-timestamp" data-t="07:16:03">[07:16:03]</a>.