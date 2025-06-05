---
title: Modern JavaScript array methods
videoId: Mus_vwhTCq0
---

From: [[fireship]] <br/> 

While [[javascript_basics_and_history | JavaScript]] has long offered traditional `for` loops, modern [[javascript_basics_and_history | JavaScript]] provides more concise and predictable array methods for data manipulation. These methods promote immutability, making code easier to understand and maintain <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

## Accumulating Values with `Array.reduce()`

The `Array.reduce()` method is used to take an array and accumulate its values into a single result <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

It takes a callback [[functions_and_closures_in_javascript | function]] as an argument, where the first argument is the accumulated value, and the second is the current value in the loop <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. For example, to sum all items in an array, you would add the accumulated value to the current value, which, upon completion, yields the total of all elements <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

## Transforming Values with `Array.map()`

`Array.map()` is ideal for transforming each item in an array <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. For instance, to add a 10% tax to each order total in an array, you can simply map the existing values to their original value multiplied by `1.1` <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

## Filtering Values with `Array.filter()`

`Array.filter()` allows you to create a new array containing only the elements that meet a specified condition <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. The callback [[functions_and_closures_in_javascript | function]] passed to `filter` should return `true` for values that should be included in the new array, and `false` otherwise <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. For example, to get only orders greater than 100, the filter callback would check if the value is greater than 100 <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### Why Modern Methods Over Classic Loops?

*   **Conciseness**: Modern array methods can reduce multiple lines of traditional loop code to just one or two <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Readability**: They often make the intent of the code clearer <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Immutability**: Unlike classic `for` loops, these methods typically return new arrays or values, avoiding direct mutation of the original data, which can lead to more predictable code <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Reduced Boilerplate**: They abstract away the need for explicit index management or manual array pushes found in traditional `for` loops <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.