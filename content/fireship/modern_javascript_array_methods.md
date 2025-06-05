---
title: Modern JavaScript array methods
videoId: Mus_vwhTCq0
---

From: [[fireship]] <br/> 

Modern JavaScript offers powerful array methods that allow developers to write more concise, readable, and efficient code compared to traditional `for` loops <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. These methods help avoid mutating original array values, leading to more predictable code <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

## Why Use Modern Array Methods?

Traditional `for` loops, while present in nearly every programming language, can lead to verbose and less readable code in JavaScript <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. They often involve mutating values, which can make code unpredictable <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Modern array methods, however, allow developers to express complex operations on arrays in just a few lines of code <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

## Key Array Methods

### `Array.prototype.reduce()`

The `reduce()` method is used to accumulate an array into a single value <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

*   It takes a callback function as an argument <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   The callback function's first argument is the accumulated value, and the second is the current value in the loop <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

**Example: Summing Array Items**

To sum all items in an array, the callback function can simply add the accumulated value to the current value <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. When the loop finishes, it returns the total of all elements <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

### `Array.prototype.map()`

The `map()` method is used to create a new array by transforming each element of the original array <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

**Example: Adding Tax to Order Totals**

To add 10% tax to each order total in an array, you can `map()` each value to itself multiplied by 1.1 <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

### `Array.prototype.filter()`

The `filter()` method creates a new array containing only elements for which the provided callback function returns `true` <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

**Example: Filtering High-Value Orders**

To create an array of orders with values greater than 100, you can use `filter()` where the callback function returns `true` if the value is greater than 100 <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

## [[spread_syntax_in_javascript | Spread Syntax]] with Arrays

The [[spread_syntax_in_javascript | spread syntax]] (`...`) can also be used with arrays to compose new arrays <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. This allows for creating new arrays without mutating the original, similar to how it works with [[javascript_objects_and_their_properties | objects]] <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

**Examples:**

*   **Appending items**: Adding the three dots to the beginning of an array within a new array literal is equivalent to an `Array.prototype.push()` operation, appending new items to the end <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Prepending items**: Adding the three dots to the end of an array within a new array literal is equivalent to an `Array.prototype.shift()` operation, prepending new items to the beginning <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Splicing items**: Original values can be spliced into the middle of a new array for greater flexibility <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

This approach significantly reduces the code needed compared to traditional methods like `push()` <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. Modern JavaScript also handles trailing commas in arrays, which previously could break programs, making code changes in version control systems like Git more concise <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.